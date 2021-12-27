# Controlled installation of Lean and mathlib on MacOS

This document explains a more controlled installation procedure for Lean and
mathlib on MacOS. There is a quicker way described in the main
[install page](macos.html) but it requires more trust.

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for
assistance.

We'll need to set up Lean, an editor that knows about Lean, and [`mathlib`](https://github.com/leanprover-community/mathlib/) (the standard library).

Rather than installing Lean directly, we'll install a small program called [`elan`](https://github.com/leanprover/elan) which
automatically provides the correct version of Lean on a per-project basis. This is recommended for
all users.

We'll also install [`mathlib-tools`](https://github.com/leanprover-community/mathlib-tools),
which, amongst other things, let you download compiled binaries for `mathlib`.

Installing `elan` and mathlib supporting tools
---

1.  Install [Homebrew](https://brew.sh/) if you do not already have it installed.

2.  Run `brew install elan mathlibtools` in a terminal window to
    install `elan`, as well as the supporting toolset for working with
    `mathlib`.

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

There are two editors you can use with Lean, VS Code and emacs.
This document describes using VS Code (for emacs, look at https://github.com/leanprover/lean-mode).

1. Install [VS Code](https://code.visualstudio.com/).
2. Launch VS Code.
3. Click on the extension icon ![(image of icon)](img/new-extensions-icon.png)
   (or ![(image of icon)](img/extensions-icon.png) in older versions) in the side bar on the left edge of
   the screen (or press <kbd>⇧ Shift</kbd><kbd>⌘ Command</kbd><kbd>X</kbd>) and search for `leanprover`.
4. Select the `lean` extension (unique name `jroesch.lean`). There is also a
   `lean4` extension, but that one does not work with mathlib.
5. Click "install" (In old versions of VS Code, you might need to click "reload" afterwards)
6. Verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
   A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
   displayed.

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)

Aside: Migrating From Older Installations
---

Older versions of this installation guide recommended a different method
of installation, involving manually installing `elan` directly from
GitHub, procuring `pipx` and using that to install `mathlib-tools`
(`leanproject`).

If you have installed things this way, you can migrate to the newer
installation mechanism by running:

  ```sh
  pipx uninstall mathlibtools && brew install mathlibtools
  ```

and

  ```sh
  elan self uninstall && brew install elan
  ```

for `mathlib-tools` and `elan` respectively.
