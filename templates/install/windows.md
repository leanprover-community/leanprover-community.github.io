# Installing Lean 4 on Windows

Note that these are legacy instructions provided by the community. The recommended
way to install Lean and to create a project is to follow the instructions in
[the official Lean documentation](https://docs.lean-lang.org/lean4/doc/quickstart.html).

## Legacy instructions

This document explains how to get started with Lean 4 and mathlib.

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for
assistance.

<!--
TODO: make a new video walkthrough.
There is a [video walkthrough](https://www.youtube.com/watch?v=y3GsHIe4wZ4) of these instructions on YouTube.
-->

We'll need to set up Lean, an editor that knows about Lean, and `mathlib4` (the standard library).
Rather than installing Lean directly, we'll rely on a small program called [`elan`](https://github.com/leanprover/elan) which
automatically provides the correct version of Lean on a per-project basis. This is recommended for
all users.

## Installing `Visual Studio Code`

We recommend that everyone use `VS Code` as their editor for working in Lean.
You can install `VS Code` for your operating system from [https://code.visualstudio.com/download](https://code.visualstudio.com/download).

## Installing `git`

Dependencies between Lean 4 projects are implemented via pointers to git repositories,
so you will need `git` installed on your computer.

You may have this set up already, in which case you can skip this step.

Otherwise, we recommend that you install [`Git for Windows`](https://gitforwindows.org/).
You will be asked many questions during installation, and we recommend you accept the defaults for all of them
*except* for the default editor, for which you should select `Visual Studio Code`, rather than the default choice of `vi`.

We recommend running ``git config --global core.autocrlf input`` to make sure
that you don't change the line endings of text files you edit.

## Installing the `lean4` extension in `VS Code`

Open `VS Code`, and in the "activity bar" along the left hand edge of the screen
click on the "extension" icon ![(image of icon)](img/new-extensions-icon.png).

In the search box that appears, type `lean4`, and then select the `lean4` extension that appears,
and click the install button.

## Setting up `elan` and `lean`

You can either have the `VS Code` extension install `elan` and `lean` for you,
or do it manually. We recommend having the extension do it, but give instructions for both.

### Have the extension install `elan` and `lean`

Under the `File` menu, select `New text file`.
A new window labelled `Untitled-1` will appear.

There will be a prompt in this window saying `Select a language`,
which you should click on and select `Lean4`.
(You can alternatively find where `VS Code` says `Plain text` in the bottom right of your screen, and change the language here,
or press `ctrl+shift+p` to open the command palette, and select `Change language mode`.)

Once you've set the language to `Lean4`, a dialog will appear in the bottom right of your screen,
saying `Failed to start 'lean' language server` with a button `Install Lean using Elan`.

Click this button, and inside a terminal window within `VS Code` you should see the installation process begin.
It will take on the order of a minute to download and install `Lean`.

When this finishes, return to the `Untitled-1` editor, and type

```lean
#eval 18 + 19
```

If you see a blue underline appear under `#eval`, and the result `37` displayed in the right hand side `Lean info view` panel,
then you have successfully installed Lean 4!

You can skip ahead to read the instructions about creating and working on [Lean projects](project.html).
This page will show you how to work with mathlib4, the main mathematical library for Lean,
or to work with a new or existing project that depends on mathlib4.

### Installing `elan` yourself

Open a command prompt (`cmd`) and execute the following commands:

```shell
curl -O --location https://elan.lean-lang.org/elan-init.ps1
powershell -ExecutionPolicy Bypass -f elan-init.ps1
del elan-init.ps1
```

Alternatively you can open a `git bash` window, and run

```shell
curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
```

In either case, it should take about a minute to install `elan`.
Afterwards, in `VS Code` you can open a text file and either set the language to `Lean4` (or just save it with a `.lean` extension),
and then try

```lean
#eval 18 + 19
```

as described above to check that Lean is responding to you.

You can now read the instructions about creating and working on [Lean projects](project.html).
