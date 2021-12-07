# Using leanproject

## Basic usage

Everything is done using the `leanproject` command-line tool. You can
use `leanproject --help` to get the list of available commands and
options.

`leanproject` only supports Lean 3. If you are using Lean 4, the information
on this page is not relevant.

### Getting an existing Lean 3 project

The command to fetch an existing project from GitHub and make sure it
includes a copy of mathlib ready to go is `leanproject get name` where
name is either a git url, such as `https://github.com/leanprover-community/tutorials.git`
or `git@github.com:leanprover-community/tutorials.git`, or a GitHub project
identifier such as `leanprover-community/tutorials`. The organization
name defaults to `leanprover-community` so the simplest way get the tutorials
project is to run:

```text
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
```text
leanproject new my_project
```
If you omit the argument, the project will be created directly inside
the current folder. This new project will be using the latest version of
Lean compatible with mathlib, and include a pre-built mathlib.

### Building a project

Only mathlib itself comes with pre-built olean files. In order to build
oleans in a project (which is needed for every non-trivial project in
order to get decent interactive Lean speed), you can use:
```text
leanproject build
```

### Getting mathlib oleans

In an existing project *depending on* mathlib
(for mathlib itself, use `leanproject get-cache`, see below), you can
run:
```text
leanproject get-mathlib-cache
```
to download a compiled mathlib at the commit currently specified in the
project `leanpkg.toml` (see the next section if you want to update this
commit and get the latest mathlib).

If you already have an existing project and you want to upgrade it then your can use
```text
leanproject pull
```
to run `git pull` and then get mathlib olean files. If the relevant git remote
is not called `origin` then you can indicate its name as in
`leanproject pull my_remote`.

If you have Lean 3 in VS Code open, you should restart Lean by opening the
command palette with `ctrl`+`p` (`cmd`+`p` on macOS) and running the
"Lean: Restart server" command.

### Upgrading mathlib

In an existing project depending on mathlib, you can upgrade to the
latest mathlib version by running:
```text
leanproject upgrade-mathlib
```
This can be abbreviated to `leanproject up`.
By default, this will update the version of Lean 3 used by this project to
match the latest version compatible with mathlib. You can forbid such an
upgrade by using `leanproject --no-lean-upgrade upgrade-mathlib`.

Note that when working in a shared repository, after pushing the changes made
to `leanproject.toml` by this command, collaborators will need to run
`get-mathlib-cache` as described above.

If you have Lean 3 in VS Code open, you should restart Lean by opening the
command palette with `ctrl`+`p` (`cmd`+`p` on macOS) and running the
"Lean: Restart server" command.

## Advanced usage

### Adding mathlib to an existing project

If you already have a Lean project but it doesn't use mathlib yet, you
can go to the project folder and run:
```text
leanproject add-mathlib
```
By default, this will update the version of Lean 3 used by this project to
match the latest version compatible with mathlib. You can forbid such an
upgrade by using `leanproject --no-lean-upgrade add-mathlib`.

### Project olean cache

In any Lean 3 project (including mathlib itself), it can be useful to store and
retrieve olean files, especially if the project has several git branches.
Storing oleans is done by:
```text
leanproject mk-cache
```
while retrieving them is done by:
```text
leanproject get-cache
```

#### Creating caches

Note that while olean files are indeed the primary target here, `mk-cache`
actually stores everything from the `src` and `test` folders of the current
project. Since `mk-cache` uses the current git revision as the key to the
cache, it will refuse to run if your repository is dirty.

If the project is mathlib itself, the caches will be stored in
`$HOME/.mathlib/`. Otherwise, they will be stored in a folder `_cache` inside
the project top-level folder. They are named after the corresponding git
commit hash.

The `--force` option can be used to overwrite existing cache for the current
git revision.

Note that the Mathlib github repository will automatically create caches for
any commits pushed to it, so it is often unecessary to use `mk-cache`.

#### Retrieving caches

When using `get-cache` inside the mathlib project, the local cache in
`$HOME/.mathlib/` will be searched first, before trying to download it.
You can force download by running
`leanproject --force-download get-cache`. This `--force-download` option
can also be used with the `upgrade-mathlib` command.

Frequently a cache is not available for the current commit in a Lean3 project;
typically due to new commits having been made on top of the one that a cache
was built from. In this situation, `get-cache` will fail, but show which
commits do have available caches:
```
$ leanproject get-cache
Looking for my_project oleans for 3b19aed
  locally...
No cache available for revision 3b19aed
Looking for my_project oleans for cf40a75
  locally...
  Found local my_project oleans
No cache was available for 3b19aed. A cache was found for the ancestor cf40a75.
To see the intermediate commits, run:
  git log --graph 3b19aed cf40a75^!
Run `leanproject get-cache --rev` on one of the available commits above.
```
In this scenario, running `leanproject get-cache --rev cf40a75` will fetch an
older cache which will be partially valid. Another option is just to run
`leanproject get-cache --fallback=download-first` which will automatically use
the first cache found for a parent commit.

If you have Lean 3 in VS Code open, you should restart Lean by opening the
command palette with `ctrl`+`p` (`cmd`+`p` on macOS) and running the
"Lean: Restart server" command.

### Import graphs

If you want to generate a graph file showing your project import
structure, you can run:
```text
leanproject import-graph my_graph_file_name.suffix
```
where the suffix will determine the output format. It must be either
`dot` or `graphml` or `gexf`, (or `pdf`, `svg` or `png` if
[graphviz](https://www.graphviz.org/) is installed).
If you want to restrict the graph to files leading to a certain file
`my_subproject/my_file.lean` then you can run:
```text
leanproject import-graph --to my_subproject.my_file my_graph_file_name.suffix
```
Dually, if you want to see all files using `my_subproject/my_file.lean`
then you can run:
```text
leanproject import-graph --from my_subproject.my_file my_graph_file_name.suffix
```
Combining `--to` and `--from` is possible.

### Reducing imports

When adding imports to a file incrementally it is easy to end up with a long list 
of imports where some imports include others transitively.
`leanproject` can be used to print a list of removable imports using the command
```text
leanproject reduce-imports --file my_file.lean
```
by adding the optional tag `--sed` a sed script will be produced instead that will 
remove the unneeded lines for you when run.
Calling this command with no file argument will print removable imports in the
entire project.

### Git hooks

If you want leanproject to fetch olean caches after each `git checkout`,
and make olean caches after each `git commit` in the current project,
you can run:
```text
leanproject hooks
```
Beware this will overwrite any `post-checkout` or `post-commit` file you
might have in your project `.git/hooks`.

### Cache download url handling

By default, leanproject will try to find mathlib olean files hosted on an
Azure server. You permanently override the base url it uses by running:
```text
leanproject set-url my_url
```
so that leanproject will look for caches at
`my_url/relevant_git_hash.tar.gz`. You can override this base url
for one invocation using `leanproject --from-url my_url ...`
(where `...` denotes a command and its arguments).

### Global mathlib install

If you want to use mathlib outside of a Lean 3 project, you can run:
```text
leanproject global-install
```
This will put a pre-compiled mathlib inside `$HOME/.lean`, the user-wide
Lean project whose dependencies can be used by lean files outside
projects. You can upgrade this project using:
```text
leanproject global-upgrade
```

This is generally discouraged, as this can lead to trouble if you end up
working with Lean 3 projects that depend on different versions of Lean 3 /
mathlib.

## Troubleshooting

If `leanproject` ends with a mysterious error message, you can run it
using the `--debug` flag, e.g. `leanproject --debug new my_project`.
It will then probably output a python trace that you'll be able to paste
in a GitHub issue or on [Zulip](https://leanprover.zulipchat.com/).

Another common problem you may encounter when editing mathlib files is the 
["orange bars of hell"](https://leanprover-community.github.io/glossary.html#orange-bar-of-hell).
When this problem arises the orange bars in the sidebar of the editor 
(e.g. VSCode) alongside a Lean file, which normally indicate which parts of 
the file Lean is still evaluating, refuse to disappear or update.  

* The first thing to try if this occurs is to close any inactive editor 
tabs and then restart Lean. (In VSCode, press `ctrl-shift-p` or `cmd-shift-p` 
to open the Command Palette and then run the command `Lean: Restart`). 

* If the problem persists after restarting, this may be because your local 
copy of the 
(pre-compiled olean files)[https://leanprover-community.github.io/glossary.html#cache] 
is mismatched or faulty in some other way, and so Lean is having to (re)compile 
all the imported mathlib files.  This takes a long time, making Lean appear 
unresponsive.  In this case, make sure any changes in your current branch 
are committed, switch to the `master` branch, and then re-download the mathlib 
cache by typing `leanpkg configure && leanproject get-mathlib-cache` at the terminal.

* If this still fails to fix the problem, or if you get some other error message
when following the above procedure, post a message in the `#new members` channel 
of the [Zulip](https://leanprover.zulipchat.com/) chat, and our friendly 
community will do our best to help get you going again!
