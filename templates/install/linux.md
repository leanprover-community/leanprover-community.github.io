# Installing Lean and mathlib on Linux

This document explains how to get started with Lean and mathlib on a generic Linux distribution (there is a [specific page](debian.html) for Debian and derived distributions such as Ubuntu).

All commands below should be typed inside a terminal.

* Lean itself doesn't depend on much infrastructure, but supporting tools
  needed by most users require `git`, `curl`, and `python3` (on Debian and
  Ubuntu also `python3-pip` and `python3-venv`). So the first step is to get those.

* The next step installs a small tool called [`elan`](https://github.com/leanprover/elan) which will handle
  updating Lean according to the needs of your current project (hit Enter
  when a question is asked). It will live in `$HOME/.elan` and add a
  line to `$HOME/.profile`.
  ```bash
  curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
  ```

* You will also need a code editor that has a Lean plugin. The
  recommended choice is [Visual Studio Code](https://code.visualstudio.com/).
  The alternative is to use Emacs, and its [lean-mode](https://github.com/leanprover/lean-mode).

  1. Install [VS Code](https://code.visualstudio.com/).
  2. Launch VS Code.
  3. Click on the extension icon ![(image of icon)](img/new-extensions-icon.png)
     (or ![(image of icon)](img/extensions-icon.png) in older versions) in the side bar on the left edge of
     the screen (or press <kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>X</kbd>) and search for `leanprover`.
  4. Select the `lean` extension (unique name `jroesch.lean`). There is also a
     `lean4` extension, but that one does not work with mathlib.
  5. Click "install" (In old versions of VS Code, you might need to click "reload" afterwards)
  6. Verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
    A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
    displayed.

* Then we install a small tool called `leanproject` that which will handle
  updating mathlib according to the needs of your current project. We use
  [pipx](https://pipxproject.github.io/pipx/) to perform the installation.
  ```bash
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath
  source ~/.profile
  pipx install mathlibtools
  ```

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
