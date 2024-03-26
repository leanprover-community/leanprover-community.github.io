# Controlled installation of Lean 4 on MacOS

This document explains a more controlled installation procedure for Lean on MacOS. There is a quicker way described in the main
[install page](../get_started.html) but it requires more trust.

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for
assistance.

We'll need to set up Lean, an editor that knows about Lean, and [`Mathlib`](https://github.com/leanprover-community/mathlib4/) (the math library).

Rather than installing Lean directly, we'll install a small program called [`elan`](https://github.com/leanprover/elan) which
automatically provides the correct version of Lean on a per-project basis. This is recommended for
all users.

Installing `elan` and mathlib supporting tools
---

1.  Install [Homebrew](https://brew.sh/) if you do not already have it installed.

2.  Run `brew install elan-init` in a terminal window to
    install `elan`.

    Note that Homebrew also contains a formula named simply `lean`, but
    that it installs a fixed version of Lean, rather than one provisioned
    with `elan` as per the above.  Using this formula is as mentioned *not*
    recommended.

3.  Use `elan` to install the latest stable version of `lean` by running
    `elan toolchain install stable`. You can also set the newly-installed
    version to be the default version of `lean` you get when running outside of
    a project (discussed below) by running `elan default stable`.

Installing and configuring an editor
---

There are three editors you can use with Lean, VS Code emacs and neovim.
This document describes using VS Code which currently has the best support for Lean.
For emacs, look at https://github.com/leanprover/lean4-mode. 
For neovim, look at https://github.com/Julian/lean.nvim)

1. Install [VS Code](https://code.visualstudio.com/).
2. Launch VS Code.
3. Click on the extension icon ![(image of icon)](img/new-extensions-icon.png)
   (or ![(image of icon)](img/extensions-icon.png) in older versions) in the side bar on the left edge of
   the screen (or press <kbd>⇧ Shift</kbd><kbd>⌘ Command</kbd><kbd>X</kbd>) and search for `leanprover`.
4. Select the `lean4` extension (unique name `leanprover.lean4`).
5. Click "install" (In old versions of VS Code, you might need to click "reload" afterwards)
6. Verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
   A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
   displayed.

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
