# Tips and Tricks about Lean Projects

These tips and tricks about managing Lean projects should be considered workarounds or common practice. Some care is adviced when trying these non-standard setups.

*Note:* Things here might change as `lake` is being developed, as features described here are not necessarily officially supported by `lake`. This file has been written for Lean `v4.10.0`. If in doubt, ask for help on [Zulip](https://leanprover.zulipchat.com).

## Shared Mathlib

If you start many projects which all use the latest stable version of mathlib, e.g. because you have little
disk space available, it might be worth setting them up using one centralised mathlib instead of
letting every project download there own clone.

Here is a guide on best practise on how to achieve that.

1) First, clone the version of mathlib somewhere on your computer:
   ```bash
   git clone --branch v4.10.0 git@github.com:leanprover-community/mathlib4.git
   ```
   Note that `v4.10.0` is the tag of the latest release, you can look at [mathlib's tags](https://github.com/leanprover-community/mathlib4/tags) to find out which is the most recent release version.

   (If you don't have git setup correctly using an SSH key, you might want to use `git clone --branch v4.10.0 https://github.com/leanprover-community/mathlib4.git` instead.)
2) Go inside your mathlib and download cache:
   ```bash
   cd mathlib
   lake exe cache get
   ```
3) If you ever want to **update** your global mathlib, come back to the mathlib directory and call
   ```bash
   git checkout v4.11.0
   lake exe cache get
   ```
   with the [version](https://github.com/leanprover-community/mathlib4/tags) you'd like to update to.
4) Now if you don't already have a Lean project, create it
   ```bash
   lake new MyProject math.lean
   cd MyProject
   ```
5) In the project `MyProject` you need to modify two things:
   <!-- 1) Make sure `lean-toolchain` contains the string `leanprover/lean4:v4.10.0` with the same version your shared mathlib is at. -->
   * In `lakefile.lean`, replace the line `require "leanprover-community" / "mathlib"` with
     ```
     require mathlib from ".." / "relative" / "path" / "to" / "mathlib4"
     ```
   * Now inside `MyProject` you need to clean up lake:
     ```bash
     rm -rf .lake # because `lake clean` does not remove `.lake/packages/mathlib` which might have been downloaded by `lake new`.
     lake clean # or potentially `lake update -R mathlib` instead
     ````
     *(note: it looks like a bug that with a simple `lake clean`, there might still be a folder `.lake/packages/mathlib` floating around from before you changed the `lakefile.lean`. However, deleting `.lake/` is a reasonably save action as it only contains build artifacts that are fully recovered by the next `lake` call.)*
   * Your project should be ready and when you add `import Mathlib` in a file and click "Restart File" in VSCode, it should be reasonably quick without rebuilding mathlib.
6) When you updated your global mathlib it might be enough to call
   ```
   lake update -R mathlib
   ```
   which would in theory update everything automatically.
   However, if there are breaking changes to the `lakefile` parsing, you might need to
   * edit `lean-toolchain` to be the same as your global mathlib.
   * make sure `lakefile.lean` parses without error in the new version.
   * try `lake update -R mathlib` again.

## Following stable versions of dependencies

If your Lean project only wants to following the stable releases of dependencies (i.e. `v4.10.0`, `v4.11.0`, etc.) you could do the following trick:

In your `lakefile.lean`, add

```lean
def leanVersion : String := s!"v{Lean.versionString}"
```

and then suffix all `require`s with `@ leanVersion`:

```
require "leanprover-community" / "mathlib" @ leanVersion
```

*Note:* for this to work, the corresponding repository needs to have a tag (or branch) for the corresponding Lean version, see e.g. [the mathlib tags](https://github.com/leanprover-community/mathlib4/tags).

If you specified the version for all dependencies in your project, you can then update your project simply by

* Edit `lean-toolchain` to have the new toolchain `leanprover/lean4:v4.11.0`.
* Call `lake update -R`.

  *(note: a blank `lake update -R` is only reasonable if **all** required dependencies in your project have a version specified with `@`)*



## Using local dev version of a dependency

In rare circumstances you might want to use a local copy of a dependency (e.g. `mathlib`) when developing, i.e. to test changes immediately.

You could do this by using a local dependency while developing
```
require mathlib from ".." / "mathlib4"
```
and then change it back to the remote dependency before pushing changes:
```
require "leanprover-community" / "mathlib"
```

However, if you want to do this frequently, here might be a better setup. With the suggested modifications to the `lakefile.lean` below, you get the following behaviour:

* To use the local dependency, call
  ```
  lake update -R -Kmathlib.useDev mathlib
  ```
* To switch back to the remote dependency, call
  ```
  lake update -R mathlib
  ```
* Anybody `require`-ing your project as dependency in there own project will automatically get the remote version of the dependencies.

(*Note:* make sure to read the chapter above about specifying versions when using `lake update`).

For this you need to replace `require "leanprover-community" / "mathlib"` in your `lakefile.lean` with the following instructions:

```lean
/-- The local dependency. Using a relative path. -/
def LocalMathlib : Dependency := {
  name := `mathlib
  src? := some <| .path (".." / "mathlib4")
  scope := ""
  version? := none
  opts := {}
}

/-- The remote dependency. Note that "master" is the version you want. -/
def RemoteMathlib : Dependency := {
  name := `mathlib
  src? := some <| .git "https://github.com/leanprover-community/mathlib4.git" "master" none
  scope := "leanprover-community"
  version? := none
  opts := {}
}

/- Choose `mathlib` dependency locally if `-Kmathlib.useDev` is provided. -/
open Lean in
#eval (do
  let depName := if get_config? mathlib.useDev |>.isSome then
    ``LocalMathlib else ``RemoteMathlib
  modifyEnv (fun env => Lake.packageDepAttr.ext.addEntry env depName)
  : Elab.Command.CommandElabM Unit)
```