# Controlled installation of Lean 4 on Debian/Ubuntu

Note that these are legacy instructions provided by the community. The recommended
way to install Lean and to create a project is to follow the instructions in
[the official Lean documentation](https://docs.lean-lang.org/lean4/doc/quickstart.html).

## Legacy instructions

This document explains a more controlled installation procedure
for Lean 4 and mathlib on Linux distributions derived from Debian (Debian
itself, Ubuntu, LMDE,...). There is a quicker way described in the main
[install page](debian.html) but it requires more trust.
Of course you can get even more details about what is going on by
reading the bash script that will be downloaded below:
[elan_init](https://github.com/leanprover/elan/blob/master/elan-init.sh).

* Lean itself doesn't depend on much infrastructure, but supporting tools
  needed by most users require `git` and `curl`. So the first step is:
  ```bash
  sudo apt install git curl
  ```

* The next step installs a small tool called `elan` which will handle
  updating Lean according to the needs of your current project (hit Enter
  when a question is asked). It will live in `$HOME/.elan` and adds a
  line to `$HOME/.profile`.
  ```bash
  curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
  ```

* There are three editors you can use with Lean, VS Code, emacs and neovim. The
  recommended choice is [Visual Studio Code](https://code.visualstudio.com/) which has
  the most complete and well-tested support for Lean.
  ```bash
  wget -O code.deb https://go.microsoft.com/fwlink/?LinkID=760868
  sudo apt install ./code.deb
  rm code.deb
  code --install-extension leanprover.lean4
  ```

  Now open VS Code, and verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
   A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
   displayed.

  Alternatively, you can use Emacs and its [lean4-mode](https://github.com/leanprover/lean4-mode) or
  neovim and its [lean.nvim extension](https://github.com/Julian/lean.nvim).

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
