#!/usr/bin/env python3

from pathlib import Path
import os
from contextlib import contextmanager
import subprocess
import shutil
import stat
import tempfile
import re
import logging
from datetime import datetime
from typing import Tuple

import urllib3
import certifi
import requests
from github import Github
from git import Repo
import toml
from bs4 import BeautifulSoup

from mathlibtools.lib import LeanProject, download
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(prevdir)

DIST_LIN = Path('linux')/'trylean'
DIST_WIN = Path('windows')/'trylean'
DIST_MAC = Path('macos')/'trylean'
DISTS = [DIST_LIN, DIST_WIN, DIST_MAC]
DIST_ALL = Path('all')
DATA_LIN = DIST_LIN/'vscodium'/'data'
DATA_WIN = DIST_WIN/'vscodium'/'data'
DATA_MAC = DIST_MAC/'vscodium'/'codium-portable-data'

log = logging.getLogger("Make Lean bundle")
log.setLevel(logging.INFO)
if (log.hasHandlers()):
    log.handlers.clear()
log.addHandler(logging.StreamHandler())

# We need to tell python that .vsix files are secretely zip files
shutil.register_unpack_format('VScode extension', ['.vsix'],
        shutil._unpack_zipfile)

g = Github()
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


def unpack_archive(fname: Path, tgt_dir: Path) -> None:
    """Unpack zip or tar.gz archive."""
    # Unfortunately, zip file extraction from shutil does not preverse exec permission
    if fname.suffix == '.zip':
        subprocess.run(['unzip', str(fname), '-d', str(tgt_dir)])
    else:
        shutil.unpack_archive(fname, tgt_dir)

def latest_release(project: str) -> str:
    """
    Webscrap the latest release of a GitHub project.
    This avoids using the GitHub API with its limit rate.
    project can be for instance 'VSCodium/vscodium'
    or 'leanprover/vscode-lean'.
    This is a brittle function that will probably break
    if used with other projects than the above two.
    """
    resp = requests.get(f'https://github.com/{project}/releases')
    assert resp.status_code == 200
    soup = BeautifulSoup(resp.content, "html.parser")
    prefix = f'/{project}/releases/tag/'
    links = [a.get('href') for a in soup.find_all('a') if a.get('href').startswith(prefix)]
    max_ver = [0]
    max_link = ''
    for link in links:
        ver = list(map(int, link.replace(prefix, '').strip('v').split('.')))
        if ver > max_ver:
            max_ver = ver
            max_link = link.replace(prefix, '')
    assert max_link
    return max_link

def get_asset(project: str, name: str, name_re: str, target: Path) -> None:
    """
    Download and unpack asset from a GitHub release.
    project: the GitHub project id, e.g. leanprover-community/lean
    name: Human readable name of the asset, for logging purposes
    name_re: a regex matched against the asset name
    target: a folder Path where the asset will be extracted. It will be
            created if needed.
    """
    log.info(f'Searching for {name}')
    release = g.get_repo(project).get_latest_release()
    asset = next(x for x in release.get_assets() if re.match(name_re, x.name))
    target.mkdir(parents=True, exist_ok=True)
    log.info(f'Downloading {asset.name}')
    with tempfile.TemporaryDirectory() as tmpdirname:
        archive_path = Path(tmpdirname)/asset.name
        download(asset.browser_download_url, archive_path)
        log.info('Unpacking')
        unpack_archive(archive_path, target)

def touch_olean(dest: Path) -> None:
    """Set access and modification time to now for all olean below dest."""
    now = datetime.now().timestamp()
    for p in dest.glob('**/*.olean'):
        os.utime(str(p), (now, now))

def get_lean(version: str) -> None:
    """Get Lean, and rename it to get rid of the version number"""
    base_url = f'https://github.com/leanprover-community/lean/releases/download/v{version}/'

    fname = f'lean-{version}-linux.tar.gz'
    download(base_url + fname, DIST_LIN/fname)
    unpack_archive(DIST_LIN/fname, DIST_LIN)
    (DIST_LIN/fname).unlink()

    fname = f'lean-{version}-windows.zip'
    download(base_url+fname, DIST_WIN/fname)
    unpack_archive(DIST_WIN/fname, DIST_WIN)
    (DIST_WIN/fname).unlink()

    fname = f'lean-{version}-darwin.zip'
    download(base_url+fname, DIST_MAC/fname)
    unpack_archive(DIST_MAC/fname, DIST_MAC)
    (DIST_MAC/fname).unlink()

    for dest in DISTS:
        next(dest.glob('lean-*')).replace(dest/'lean')
        touch_olean(dest/'lean'/'lib'/'lean'/'library')

def get_vscodium():
    """Get VScodium, the open source version of VScode *binaries*"""
    get_asset('VSCodium/vscodium', 'VScodium for Linux', r'VSCodium-linux-x64.*.tar.gz',
              DIST_LIN/'vscodium')
    get_asset('VSCodium/vscodium', 'VScodium for Windows', r'VSCodium-win32-x64.*.zip',
              DIST_WIN/'vscodium')
    get_asset('VSCodium/vscodium', 'VScodium for MacOS', r'VSCodium-darwin.*.zip',
              DIST_MAC/'vscodium')

def get_lean_extension():
    """Get the Lean extension, and move it to the right place"""
    lean_extension_path = DIST_ALL/'extension'
    lean_extension_path.mkdir(parents=True, exist_ok=True)
    ver = latest_release('leanprover/vscode-lean')
    fname = f"lean-{ver.strip('v')}.vsix"
    download(f"https://github.com/leanprover/vscode-lean/releases/download/{ver}/{fname}",
            lean_extension_path/fname)
    unpack_archive(lean_extension_path/fname, lean_extension_path)
    for dest in [DATA_LIN, DATA_WIN, DATA_MAC]:
        shutil.copytree(lean_extension_path/'extension', dest/'extensions'/'lean')


    # Write relevant VScode settings
    SETTINGS = """{
        "files.exclude": {
            "**/.git": true,
            "**/.svn": true,
            "**/.hg": true,
            "**/CVS": true,
            "**/.DS_Store": true,
            "**/*.olean": true
        },
        "lean.executablePath": "%extensionPath%/../../../../lean/bin/lean"
        "editor.minimap.enabled": false,
        "window.titleBarStyle": "custom",
    }
    """
    for dest in [DATA_LIN, DATA_WIN, DATA_MAC]:
        user = dest/'user-data'/'User'
        user.mkdir(parents=True, exist_ok=True)
        with (user/'settings.json').open('w') as settings:
            settings.write(SETTINGS)

def get_mathlib(rev: str) -> None:
    """Get mathlib"""
    log.info('Cloning mathlib')
    repo = Repo.clone_from('https://github.com/leanprover-community/mathlib.git',
            str(DIST_ALL/'mathlib'))
    repo.git.checkout(rev)
    mathlib = LeanProject.from_path(DIST_ALL/'mathlib')
    mathlib.get_cache()

    for dest in DISTS:
        shutil.copytree(DIST_ALL/'mathlib', dest/'mathlib')
        touch_olean(dest/'mathlib')

def get_tutorials() -> Tuple[str, str]:
    """Get some file to play with"""
    log.info('Getting tutorial files')
    with tempfile.TemporaryDirectory() as tmpdirname:
        Repo.clone_from('https://github.com/leanprover-community/tutorials.git',
                tmpdirname, multi_options=['--depth=1'])
        for dest in DISTS:
            shutil.copytree(Path(tmpdirname)/'src', dest/'src',
                    dirs_exist_ok=True)
        conf = toml.load(Path(tmpdirname)/'leanpkg.toml')

    lean_ver = conf['package']['lean_version'].split(':')[1]
    mathlib_ver = conf['dependencies']['mathlib']['rev']

    # Setup leanpk.path
    log.info('Setting up leanpkg.path')
    LEANPKG_PATH = "builtin_path\npath ../mathlib/src/\npath solutions\n"
    for dest in DISTS:
        (dest/'src'/'leanpkg.path').write_text(LEANPKG_PATH)
    return lean_ver, mathlib_ver

def mk_launcher() -> None:
    """Create Launcher"""
    BASH_SCRIPT = """#!/bin/bash
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
    cd $DIR
    ./vscodium/codium $DIR/src
    """
    DESKTOP_FILE="""[Desktop Entry]
    Type=Application
    Name=Try Lean
    Exec=./trylean
    Categories=Application;
    """
    (DIST_LIN/'trylean').write_text(BASH_SCRIPT)
    (DIST_LIN/'trylean').chmod(stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)
    (DIST_LIN/'trylean.desktop').write_text(DESKTOP_FILE)
    (DIST_LIN/'trylean.desktop').chmod(stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)
    MAC_BASH_SCRIPT = """#!/bin/bash
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
    cd $DIR
    open ./vscodium/VSCodium.app --args $DIR/src
    """
    with (DIST_MAC/'trylean').open('w') as path:
        path.write(MAC_BASH_SCRIPT)
    (DIST_MAC/'trylean').chmod(stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

    BAT_SCRIPT = r""".\vscodium\VSCodium src
    """
    with (DIST_WIN/'trylean.bat').open('w') as path:
        path.write(BAT_SCRIPT)

def zip_all() -> None:
    # Zip all
    log.info('Making Linux archive')
    shutil.make_archive('trylean_linux', 'gztar', root_dir='linux', base_dir='trylean')
    log.info('Making Windows archive')
    shutil.make_archive('trylean_windows', 'zip', root_dir='windows', base_dir='trylean')
    log.info('Making MacOS archive')
    shutil.make_archive('trylean_darwin', 'gztar', root_dir='macos', base_dir='trylean')

if __name__ == '__main__':
    lean_version, mathlib_sha = get_tutorials()
    get_lean(lean_version)
    get_vscodium()
    get_lean_extension()
    get_mathlib(mathlib_sha)
    mk_launcher()
    zip_all()
