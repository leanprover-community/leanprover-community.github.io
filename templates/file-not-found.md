# File not found

Are you setting up your first Lean project, and seeing this error message? The problem might be:
- Did you open a bare file in VS Code? Try opening the root folder
  of your Lean package instead. See ["Creating a Lean project"](install/project.html).
- Is the Lean package configured correctly? Does a `leanpkg.path` file exist
  in the directory and contain valid locations? If not, try running
  `leanproject get-mathlib-cache` if your project depends on mathlib, or
  `leanpkg configure` otherwise.
