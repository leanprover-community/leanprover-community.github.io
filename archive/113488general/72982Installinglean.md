---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72982Installinglean.html
---

## [general](index.html)
### [Installing lean](72982Installinglean.html)

#### [Guillermo Barajas Ayuso (Jul 02 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128979128):
Hi guys I'm trying to install lean in my laptop and the following message was displayed when I tried to evaluate 1+1:

Looking for git in: C:\Program Files\Git\cmd\git.exe
Using git 2.18.0.windows.1 from C:\Program Files\Git\cmd\git.exe
> git rev-parse --show-toplevel
fatal: not a git repository (or any of the parent directories): .git


Anyone knows what's going on?

#### [Simon Hudon (Jul 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128979306):
I would guess that you installed `elan` first and `elan` is trying make sure you have the right version of Lean (and maybe `mathlib`) using `git`. Do you have `git`? Is it in your `PATH`?

#### [Guillermo Barajas Ayuso (Jul 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128979365):
A message was displayed before saying that git wasn't found, so I installed it. It should be in my path

#### [Simon Hudon (Jul 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128979510):
If you type `git` in your terminal, what do you get?

#### [Guillermo Barajas Ayuso (Jul 02 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128980408):
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.

#### [Simon Hudon (Jul 02 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128980520):
That's curious. At the root of your project, can you call `git init`?

#### [Reid Barton (Jul 02 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128980572):
I think that there is no project, and/or we don't know what "evaluate 1+1" means

#### [Guillermo Barajas Ayuso (Jul 02 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128981476):
What do you mean by the root of my project? Actually the message didn't depend on me typing anything, I just realized. If I write git init in the terminal the message 

Initialized empty Git repository in C:/Users/guill/.git/

is showed.

#### [Simon Hudon (Jul 02 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128981592):
What did you do to evaluate `1+1`?

#### [Kevin Buzzard (Jul 02 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128981957):
```quote
What do you mean by the root of my project?
```
So one way of using Lean is to make a "project". What happens if you type `lean` or `leanpkg` on the command line?

#### [Kevin Buzzard (Jul 02 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128982119):
If `leanpkg` works then you can change to a nice new folder on the command line and follow the instructions at 

https://leanprover.github.io/reference/using_lean.html#creating-new-packages

to make a new package. Then you can open this folder with VS Code and it might all work. 

When you're using the command line you have a "current working directory", which you might be able to see with a command like `pwd` (whether this works or not depends on exactly which Windows command line tool you're using). You can move between directories with command line commands, you can make new directories and so on. If you can make a new directory called something like `C:\Users\Guillermo\Lean_stuff\my_project` and change into that directory on the command line, and if `leanpkg` is on your path, then all of this might work fine.

#### [Sebastian Ullrich (Jul 02 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing lean/near/128987757):
The message seems to be from VS Code, not Lean or elan

