# Lean projects

In general, if you just open a single `.lean` file in your text editor
and try to compile it, you'll get a bunch of confusing errors.
Every non-trivial piece of Lean code needs to live inside a *Lean project*
(sometimes also called a Lean package).
A "Lean project" is more than just a folder that you've named "My Lean stuff".
Rather, it's a folder containing some very specific things:
in particular, a *git repository* and a file
`lakefile.lean` that gathers information about dependencies of the
project, including for instance the version of Lean that should be used.

If you're interested in contributing to mathlib you only need to set up
a Lean project once, which you can use for all your contributions —
you don't need to set up a new Lean project for each new contribution.

Setting up and managing all this is done by a program called `lake` (this is
a portmanteau of `lean` and `make`).
This page describes the basic use of this tool, and should be sufficient
for everyday use.
If this is not enough for your purposes, you can read the
full [lake documentation](https://github.com/leanprover/lean4/blob/master/src/lake/README.md).

## Working on an existing project

Suppose you want to work on an existing project. As example, we will take
[the Mathematics in Lean book](https://github.com/leanprover-community/mathematics_in_lean).
Open a terminal.

* If you have not logged in since you installed Lean and mathlib, then
  you may need to first type `source ~/.profile` or
  `source ~/.bash_profile` depending on your OS.
  If you are on Windows, and don't know how to do this, another option is to restart your computer.

* Go the the directory where you would like this package to live. You do not need to create a new folder yourself, the next command will create a `mathematics_in_lean` subfolder for you.

* Run `git clone https://github.com/leanprover-community/mathematics_in_lean.git`.

* Run `cd mathematics_in_lean`

* Run `lake exe cache get` (note: this command currently only works in projects which import `mathlib4` as a dependency)

* Launch VS Code, either through your application menu or by typing
  `code .`. (MacOS users need to take a one-off
  [extra step](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line)
   to be able to launch VS Code from the command line.)

* If you launched VS Code from a menu, on the main screen, or in the File menu,
  click "Open folder" (just "Open" on a Mac), and choose the folder
  `mathematics_in_lean` (*not* one of its subfolders).

* Using the file explorer on the left-hand side, explore everything you
  want in `MIL`.
  See the [MIL instructions](https://github.com/leanprover-community/mathematics_in_lean/blob/master/README.md)
  for advice about how to do the exercises in this book.

## Creating a Lean project

We will now create a new project depending on mathlib. The following
commands should be typed in a terminal.

* Go to a folder where you want to create a project in a subfolder
  `my_project`, and type `lake +leanprover/lean4:nightly-2024-04-24 new my_project math`. Do not worry about the date in the previous command, it ensures you will use a sufficiently recent version of `lake` but has no impact on the version of `lean` your project will use. If you get an
  error message saying `lake` is an unknown command and
  you have not logged in since you installed Lean, then
  you may need to first type `source ~/.profile` or `source ~/.bash_profile`.
The keyword `math` at the end of this command adds `mathlib4` to the dependencies of your project, so that you can use `import Mathlib` in your project files.

* Go inside the `my_project` folder and type `lake update` and then `mkdir MyProject`.
  * Windows users seeing a `curl: (35) schannel: next InitializeSecurityContext failed` error should read [this note](#troubleshooting).

* Launch VS Code, either through your application menu or by typing
  the `code .` command.

* If you launched VS Code through a menu: on the main screen, or in the
  File menu, click "Open folder" (on a Mac, just "Open"), and
  choose the folder `my_project` (*not* one of its subfolders).

* Your Lean code should now be put inside files with extension `.lean`
  living in `my_project/MyProject/` or a subfolder thereof. In the file explorer
  on the left-hand side of VS Code, you can right-click on `MyProject`, choose
  `New file`, and type a filename to create a file there.

If you want to make sure everything is working, you can start by
creating, say `my_project/MyProject/Test.lean` containing:
```lean
import Mathlib.Topology.Basic

#check TopologicalSpace
```
When the cursor is on the last line, the right hand part of VS Code
should display a "Lean Infoview" area saying:
`TopologicalSpace.{u} (α : Type u) : Type u`.

Note that you can import your own files in the project. For instance if you created a
file `my_project/MyProject/Definitions.lean`, you can start a new file
`my_project/MyProject/Lemmas.lean` with `import MyProject.Definitions`.

If, for some reason, you happen to lose the "Lean Infoview" area, you
can get it back with <kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>Enter</kbd>
(<kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>Enter</kbd> on MacOS).
Also, you can get the Lean documentation inside VS Code using
<kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>p</kbd>
(<kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>p</kbd> on MacOS) and then,
inside the text field that appears, type "lean doc" and hit <kbd>Enter</kbd>.
Then click "Mathematics in Lean" or "Theorem Proving in Lean" and enjoy.

## Updating Mathlib in your project

If you have a project depending on Mathlib, and you want to update to the latest version of Lean and Mathlib, you have to do two steps:
* Update the `lean-toolchain` file in your repository to the latest version. You can do this automatically by running the following in the root directory of your repository.
```
curl -L https://raw.githubusercontent.com/leanprover-community/mathlib4/master/lean-toolchain -o lean-toolchain
```
* run `lake update`. This will update Lean, Mathlib and download the new Mathlib cache for you. (Note: on project that use `leanblueprint`/`doc-gen`, you currently have to run `lake -R -Kenv=dev update`).

You should then check whether all files in your repository still compile.
You can do this by running `lake exe mk_all && lake build`.

More information about Lake can be found [here](https://github.com/leanprover/lean4/tree/master/src/lake).

## Contributing to mathlib

See [How to contribute to mathlib](https://leanprover-community.github.io/contribute/index.html).

## Troubleshooting

* Some Windows users have reported an error like this when running `lake exe cache get`:

```
  curl: (35) schannel: next InitializeSecurityContext failed: Unknown error (0x80092012) - The revocation function was unable to check revocation for the certificate
```

If you see this error, you likely have an antivirus program that scans each downloaded file, which results in errors.
Please disable your antivirus program and then run `lake exe cache get!`.
The exclamation mark forces `lake` to re-download the cache files it failed to download before running this command.
(If you are uncomfortable disabling your antivirus, try to follow [these instructions](https://leanprover.zulipchat.com/#narrow/stream/287929-mathlib4/topic/lake.20exe.20cache.20get.20errors/near/389019448)
and then run `lake exe cache get!`).
You can turn on your antivirus program on afterwards.
However, some users also reported that the antivirus programs significantly slow down Lean during normal usage.
If Lean is slower than what is expected, either turn off your antivirus program or tell it to ignore/allow the operation of `lean.exe`.

* Sometimes under Windows a corrupted version of Lean is downloaded while installing/updating Lean. If this happens, this will result in an error
```
uncaught exception: no such file or directory (error code: 2)
```
If this happens, you can manually delete your corrupted version of Lean by following the following two steps:
  - Go to your user folder and navigate to `.elan > toolchains` (typically `C:\Users\<username>\.elan\toolchains`), and delete the offending toolchain
  - Go to `.elan > update-hashes` (e.g. `C:\Users\<username>\.elan\update-hashes`) and delete the file with the same name.
The toolchain will be automatically redownloaded the next time you call `lake update`, `lake exe cache get`, `lake build` or open a Lean file in VSCode in a repository that uses that toolchain.

* If you would like to cleanup Lean files, these are stored in the following places.
  - Dependencies of a project are in the `.lake` folder of that project.
  - Lean toolchains are stored in `~/.elan/toolchains`. You can safely delete old toolchains from here. Whenever you delete toolchains, you should also delete the corresponding files from `~/.elan/update-hashes`.
  - Compressed and compiled Mathlib files are stored in `~/.cache/mathlib`. These can be safely deleted.
  - Lean 3 users might still have a folder `.mathlib` in their user directory.
