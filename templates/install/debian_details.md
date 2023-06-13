<div class="alert alert-info">
<p>
We are currently updating the Lean community website to describe working with Lean 4,
but most of the information you will find here today still describes Lean 3.
</p>
<p>
Pull requests updating this page for Lean 4 are very welcome.
There is a link at the bottom of this page.
</p>
<p>
Please visit <a href="https://leanprover.zulipchat.com">the leanprover zulip</a>
and ask for whatever help you need during this transitional period!
</p>
<p>
The website for Lean 3 has been <a href="https://leanprover-community.github.io/lean3/">archived</a>.
If you need to link to Lean 3 specific resources please link there.
</p>
</div>

# Controlled installation of Lean and mathlib on Debian/Ubuntu

This document explains a more controlled installation procedure
for Lean and mathlib on Linux distributions derived from Debian (Debian itself,
Ubuntu, LMDE,...). There is a quicker way described in the main
[install page](debian.html) but it requires more trust.
Of course you can get even more details about what is going on by
reading the bash script that will be downloaded below:
[elan_init](https://github.com/leanprover/elan/blob/master/elan-init.sh).

* Lean itself doesn't depend on much infrastructure, but supporting tools
  needed by most users require `git`, `curl`, and `python`. So the first step is:
  ```bash
  sudo apt install git curl python3 python3-pip python3-venv
  ```

* The next step installs a small tool called `elan` which will handle
  updating Lean according to the needs of your current project (hit Enter
  when a question is asked). It will live in `$HOME/.elan` and adds a
  line to `$HOME/.profile`.
  ```bash
  curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
  ```

* There are two editors you can use with Lean, VS Code and emacs. The
  recommended choice is [Visual Studio Code](https://code.visualstudio.com/).
  ```bash
  wget -O code.deb https://go.microsoft.com/fwlink/?LinkID=760868
  sudo apt install ./code.deb
  rm code.deb
  code --install-extension jroesch.lean
  ```

  Now open VS Code, and verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
   A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
   displayed.

  The alternative is to use Emacs, and its [lean-mode](https://github.com/leanprover/lean-mode).

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
