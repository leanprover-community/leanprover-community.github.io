# Controlled installation of Lean and mathlib on MacOS

This document explains a more controlled installation procedure for Lean and
mathlib on MacOS. There is a quicker way described in the main
[install page](macos.html) but it requires more trust.  Of course you can get
even more details about what is going on by reading the bash script that will
be downloaded below:
[elan_init](https://github.com/Kha/elan/blob/master/elan-init.sh).

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for
assistance.

We'll need to set up Lean, an editor that knows about Lean, and `mathlib` (the standard library).

Rather than installing Lean directly, we'll install a small program called `elan` which
automatically provides the correct version of Lean on a per-project basis. This is recommended for
all users.

Installing `elan`
---

1. We'll need a terminal, along with some basic prerequisites.
  Install [homebrew](https://brew.sh/), then run `brew install gmp coreutils` in a terminal
    (`gmp` is required by `lean`, `coreutils` by `leanpkg`).

2. At a terminal, run the command

   `curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh`

   and hit enter when a question is asked.

   It is recommended that you re-login, so that your environment knows about `elan`.
   (Alternatively, type `source $HOME/.elan/env` to update the current terminal.)


Installing mathlib supporting tools
---

At a terminal, run the command
  ```bash
  brew install python3 pipx
  pipx ensurepath
  pipx install mathlibtools
  ```

This will install tools that, amongst other things, let you download compiled binaries for mathlib.

Installing and configuring an editor
---

There are two editors you can use with Lean, VS Code and emacs.
This document describes using VS Code (for emacs, look at https://github.com/leanprover/lean-mode).

1. Install [VS Code](https://code.visualstudio.com/).
2. Launch VS Code.
3. Click on the extension icon ![(image of icon)](img/new-extensions-icon.png)
   (or ![(image of icon)](img/extensions-icon.png) in older versions) in the side bar on the left edge of
   the screen (or press <kbd>⇧ Shift</kbd><kbd>⌘ Command</kbd><kbd>X</kbd>) and search for `leanprover`.
4. Click "install" (In old versions of VS Code, you might need to click "reload" afterwards)
5. Verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
   A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
   displayed.

You can now read instructions about creating and working on [Lean projects](project.html)
