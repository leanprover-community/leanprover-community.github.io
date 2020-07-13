# Lean projects

Every non-trivial piece of Lean code needs to live inside a *Lean project*
(sometimes also called Lean package).
This means a folder containing in particular a git repository and a file
`leanpkg.toml` that gathers information about dependencies of the
project, including for instance the version of Lean that should be used.

Managing all this is done by a little python program called `leanproject`. 
This page describes the basic use of this tool, and should be sufficient
for everyday use. 
If this is not enough for your purposes, you can read the
full [leanproject documentation](../leanproject.html).
If you are really curious, you can also read 
[how pieces fit together](../toolchain.html).

There is a [video walkthrough](https://www.youtube.com/watch?v=y3GsHIe4wZ4) of these instructions on YouTube.

## Working on an existing project

Suppose you want to work on an existing project. As example, we will take 
[the tutorial project](https://github.com/leanprover-community/tutorials). 
Open a terminal.

* If you have not logged in since you installed Lean and mathlib, then
  you may need to first type `source ~/.profile` or 
  `source ~/.bash_profile` depending on your OS.

* Go the the directory where you would like this package to live.

* Run `leanproject get tutorials`.

* Launch VS Code, either through your application menu or by typing
  `code tutorials`. (MacOS users need to take a one-off
  [extra step](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line)
   to be able to launch VS Code from the command line.)

* If you launched VS Code from a menu, on the main screen, or in the File menu,
  click "Open folder" (just "Open" on a Mac), and choose the folder 
  `tutorials` (*not* one of its subfolders).

* Using the file explorer on the left-hand side, explore everything you
  want in `tutorials/src`. 
  See the [tutorials instructions](https://github.com/leanprover-community/tutorials/blob/master/README.md)
  for advice about how to do the exercises in this project.

## Creating a Lean project

We will now create a new project depending on mathlib. The following
commands should be typed in a terminal.

* Go to a folder where you want to create a project in a subfolder
  `my_project`, and type `leanproject new my_project`. If you get an
  error message saying `leanproject` is an unknown command and 
  you have not logged in since you installed Lean and mathlib, then
  you may need to first type `source ~/.profile` or `source ~/.bash_profile`.

* Launch VS Code, either through your application menu or by typing
  `code my_project`.

* If you launched VS Code through a menu: on the main screen, or in the
  File menu, click "Open folder" (on a Mac, just "Open"), and
  choose the folder `my_project` (*not* one of its subfolders).

* Your Lean code should now be put inside files with extension `.lean`
  living in `my_project/src/` or a subfolder thereof. In the file explorer
  on the left-hand side of VS Code, you can right-click on `src`, choose
  `New file`, and type a filename to create a file there.

If you want to make sure everything is working, you can start by
creating, say `my_project/src/test.lean` containing:
```lean
import topology.basic

#check topological_space
```
When the cursor is on the last line, the right hand part of VS Code
should display a "Lean Goal" area saying:
`topological_space : Type u_1 → Type u_1`

If, for some reason, you happen to lose the "Lean Goal" area, you
can get it back with <kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>Enter</kbd>
(<kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>Enter</kbd> on MacOS).
Also, you can get the Lean documentation inside VS Code using 
<kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>p</kbd> 
(<kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>p</kbd> on MacOS) and then, 
inside the text field that appears, type "lean doc" and hit <kbd>Enter</kbd>.
Then click "Theorem Proving in Lean" and enjoy.

## Contributing to mathlib

See [How to contribute to mathlib](https://leanprover-community.github.io/contribute/index.html).
