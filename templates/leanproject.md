# Using leanproject

## Basic usage

Everything is done using the `leanproject` command-line tool. You can
use `leanproject --help` to get the list of available commands and
options.

### Getting an existing Lean project

The command to fetch an existing project from GitHub and make sure it
includes a copy of mathlib ready to go is `leanproject get name` where
name is either a git url, such as `https://github.com/leanprover-community/tutorials.git`
or `git@github.com:leanprover-community/tutorials.git`, or a GitHub project
identifier such as `leanprover-community/tutorials`. The organization
name defaults to `leanprover-community` so the simplest way get the tutorials
project is to run:

```
leanproject get tutorials
```
You can specify a git branch name `my_branch` by appending 
`:my_branch` at the end of the specified name (without space).
By default this branch should be an existing branch.
Use `leanproject get -b project_name:branch_name` to get
the project `project_name` and then create a branch `branch_name`
and start working on it.
You can also specify a target directory name as a second argument to the
command.

### Creating a new project

You can create a project in a new folder `my_project` by running:
```
leanproject new my_project
```
If you omit the argument, the project will be created directly inside
the current folder. This new project will be using the latest version of
Lean compatible with mathlib, and include a pre-built mathlib.

### Building a project

Only mathlib itself comes with pre-built olean files. In order to build
oleans in a project (which is needed for every non-trivial project in
order to get decent interactive Lean speed), you can use:
```
leanproject build
```

### Getting mathlib oleans

In an existing project depending on mathlib (or in mathlib itself), you
can run:
```
leanproject get-mathlib-cache
```
to download a compiled mathlib at the commit currently specified in the
project `leanpkg.toml` (see the next section if you want to update this
commit and get the latest mathlib).

### Upgrading mathlib

In an existing project depending on mathlib, you can upgrade to the
latest mathlib version by running:
```
leanproject upgrade-mathlib
```
This can be abbreviated to `leanproject up`.
By default, this will update the version of Lean used by this project to
match the latest version compatible with mathlib. You can forbid such an
upgrade by using `leanproject --no-lean-upgrade upgrade-mathlib`.

## Advanced usage

### Global mathlib install

If you want to use mathlib outside of a Lean project, you can run:
```
leanproject global-install
```
This will put a pre-compiled mathlib inside `$HOME/.lean`, the user-wide
Lean project whose dependencies can be used by lean files outside
projects. You can upgrade this project using:
```
leanproject global-upgrade
```

### Adding mathlib to an existing project

If you already have a Lean project but it doesn't use mathlib yet, you
can go to the project folder and run:
```
leanproject add-mathlib
```
By default, this will update the version of Lean used by this project to
match the latest version compatible with mathlib. You can forbid such an
upgrade by using `leanproject --no-lean-upgrade add-mathlib`.

### Project olean cache

In any Lean project, it can be useful to store and retrieve olean files,
especially if the project has several git branches. Storing oleans is
done by:
```
leanproject mk-cache
```
while retrieving them is done by:
```
leanproject get-cache
```
One should note that, although olean files are indeed the primary target
here, these commands actually store everything from the
`src` and `test` folders of the current project.

If the project is mathlib itself, the caches will be stored in
`$HOME/.mathlib/`. Otherwise, they will be stored in a folder `_cache` inside
the project top-level folder. They are named after the corresponding git
commit hash.

In general, using these commands in a dirty git repository (*ie* a
repository whose working copy contains uncommitted changes) is a bad
idea. You can do it anyway by running `leanproject mk-cache --force` or
`leanproject get-cache --force` respectively.

The `--force` option will also overwrite existing cache for the current
git revision.

When using `get-cache` inside the mathlib project, the local cache in
`$HOME/.mathlib/` will be searched first, before trying to download it.
You can force download by running 
`leanproject --force-download get-cache`. This `--force-download` option
can also be used with the `upgrade-mathlib` command.

### Import graphs

If you want to generate a graph file showing your project import
structure, you can run:
```
leanproject import-graph my_graph_file_name.suffix
```
where the suffix will determine the output format. It must be either
`dot` or `graphml` or `gexf`, (or `pdf`, `svg` or `png` if
[graphviz](https://www.graphviz.org/) is installed).
If you want to restrict the graph to files leading to a certain file
`my_subproject/my_file.lean` then you can run:
```
leanproject import-graph --to my_subproject.my_file my_graph_file_name.suffix
```
Dually, if you want to see all files using `my_subproject/my_file.lean` 
then you can run:
```
leanproject import-graph --from my_subproject.my_file my_graph_file_name.suffix
```
Combining `--to` and `--from` is possible.

### Git hooks

If you want leanproject to fetch olean caches after each `git checkout`,
and make olean caches after each `git commmit` in the current project,
you can run:
```
leanproject hooks
```
Beware this will overwrite any `post-checkout` or `post-commit` file you
might have in your project `.git/hooks`.

### Cache download url handling

By default, leanproject will try to find mathlib olean files hosted on an
Azure server. You permanently override the base url it uses by running:
```
leanproject set-url my_url
```
so that leanproject will look for caches at
`my_url/relevant_git_hash.tar.gz`. You can override this base url
for one invocation using `leanprover --from-url my_url ...`
(where `...` denotes a command and its arguments).

## Troubleshooting

If `leanproject` ends with a mysterious error message, you can run it 
using the `--debug` flag, e.g. `leanproject --debug new my_project`. 
It will then probably output a python trace that you'll be able to paste
in a GitHub issue or on [Zulip](https://leanprover.zulipchat.com/).
