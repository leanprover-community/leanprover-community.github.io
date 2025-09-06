# Installing Lean 4 on Linux

Note that these are legacy instructions provided by the community. The recommended
way to install Lean and to create a project is to follow the instructions in
[the official Lean documentation](https://docs.lean-lang.org/lean4/doc/quickstart.html).

## Legacy instructions

This document explains how to get started with Lean and mathlib on a generic Linux distribution (there is a [specific page](debian.html) for Debian and derived distributions such as Ubuntu).

All commands below should be typed inside a terminal.

* Lean itself doesn't depend on much infrastructure, but supporting tools
  needed by most users require `git` and `curl`. So the first step is to get those.

* The next step installs a small tool called [`elan`](https://github.com/leanprover/elan) which will handle
  updating Lean according to the needs of your current project (hit Enter
  when a question is asked). It will live in `$HOME/.elan` and add a
  line to `$HOME/.profile`.
  ```bash
  curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
  ```

* You will also need a code editor that has a Lean plugin. The
  recommended choice is [Visual Studio Code](https://code.visualstudio.com/) which currently
  has the best Lean support.
  The alternatives are to use Emacs and its [lean4-mode](https://github.com/leanprover/lean4-mode)
  or neovim and its  [lean.nvim extension](https://github.com/Julian/lean.nvim).

  1. Install [VS Code](https://code.visualstudio.com/).
  2. Launch VS Code.
  3. Click on the extension icon ![(image of icon)](img/new-extensions-icon.png)
     (or ![(image of icon)](img/extensions-icon.png) in older versions) in the side bar on the left edge of
     the screen (or press <kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>X</kbd>) and search for `leanprover`.
  4. Select the `lean4` extension (unique name `leanprover.lean4`). 
  5. Click "install" (In old versions of VS Code, you might need to click "reload" afterwards)
  6. Verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
    A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
    displayed.

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
