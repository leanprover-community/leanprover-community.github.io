---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72982Installinglean.html
---

## Stream: [general](index.html)
### Topic: [Installing lean](72982Installinglean.html)

---


{% raw %}
#### [ Guillermo Barajas Ayuso (Jul 02 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128979128):
<p>Hi guys I'm trying to install lean in my laptop and the following message was displayed when I tried to evaluate 1+1:</p>
<p>Looking for git in: C:\Program Files\Git\cmd\git.exe<br>
Using git 2.18.0.windows.1 from C:\Program Files\Git\cmd\git.exe</p>
<blockquote>
<p>git rev-parse --show-toplevel<br>
fatal: not a git repository (or any of the parent directories): .git</p>
</blockquote>
<p>Anyone knows what's going on?</p>

#### [ Simon Hudon (Jul 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128979306):
<p>I would guess that you installed <code>elan</code> first and <code>elan</code> is trying make sure you have the right version of Lean (and maybe <code>mathlib</code>) using <code>git</code>. Do you have <code>git</code>? Is it in your <code>PATH</code>?</p>

#### [ Guillermo Barajas Ayuso (Jul 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128979365):
<p>A message was displayed before saying that git wasn't found, so I installed it. It should be in my path</p>

#### [ Simon Hudon (Jul 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128979510):
<p>If you type <code>git</code> in your terminal, what do you get?</p>

#### [ Guillermo Barajas Ayuso (Jul 02 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128980408):
<p>usage: git [--version] [--help] [-C &lt;path&gt;] [-c &lt;name&gt;=&lt;value&gt;]<br>
           [--exec-path[=&lt;path&gt;]] [--html-path] [--man-path] [--info-path]<br>
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]<br>
           [--git-dir=&lt;path&gt;] [--work-tree=&lt;path&gt;] [--namespace=&lt;name&gt;]<br>
           &lt;command&gt; [&lt;args&gt;]</p>
<p>These are common Git commands used in various situations:</p>
<p>start a working area (see also: git help tutorial)<br>
   clone      Clone a repository into a new directory<br>
   init       Create an empty Git repository or reinitialize an existing one</p>
<p>work on the current change (see also: git help everyday)<br>
   add        Add file contents to the index<br>
   mv         Move or rename a file, a directory, or a symlink<br>
   reset      Reset current HEAD to the specified state<br>
   rm         Remove files from the working tree and from the index</p>
<p>examine the history and state (see also: git help revisions)<br>
   bisect     Use binary search to find the commit that introduced a bug<br>
   grep       Print lines matching a pattern<br>
   log        Show commit logs<br>
   show       Show various types of objects<br>
   status     Show the working tree status</p>
<p>grow, mark and tweak your common history<br>
   branch     List, create, or delete branches<br>
   checkout   Switch branches or restore working tree files<br>
   commit     Record changes to the repository<br>
   diff       Show changes between commits, commit and working tree, etc<br>
   merge      Join two or more development histories together<br>
   rebase     Reapply commits on top of another base tip<br>
   tag        Create, list, delete or verify a tag object signed with GPG</p>
<p>collaborate (see also: git help workflows)<br>
   fetch      Download objects and refs from another repository<br>
   pull       Fetch from and integrate with another repository or a local branch<br>
   push       Update remote refs along with associated objects</p>
<p>'git help -a' and 'git help -g' list available subcommands and some<br>
concept guides. See 'git help &lt;command&gt;' or 'git help &lt;concept&gt;'<br>
to read about a specific subcommand or concept.</p>

#### [ Simon Hudon (Jul 02 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128980520):
<p>That's curious. At the root of your project, can you call <code>git init</code>?</p>

#### [ Reid Barton (Jul 02 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128980572):
<p>I think that there is no project, and/or we don't know what "evaluate 1+1" means</p>

#### [ Guillermo Barajas Ayuso (Jul 02 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128981476):
<p>What do you mean by the root of my project? Actually the message didn't depend on me typing anything, I just realized. If I write git init in the terminal the message </p>
<p>Initialized empty Git repository in C:/Users/guill/.git/</p>
<p>is showed.</p>

#### [ Simon Hudon (Jul 02 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128981592):
<p>What did you do to evaluate <code>1+1</code>?</p>

#### [ Kevin Buzzard (Jul 02 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128981957):
<blockquote>
<p>What do you mean by the root of my project?</p>
</blockquote>
<p>So one way of using Lean is to make a "project". What happens if you type <code>lean</code> or <code>leanpkg</code> on the command line?</p>

#### [ Kevin Buzzard (Jul 02 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128982119):
<p>If <code>leanpkg</code> works then you can change to a nice new folder on the command line and follow the instructions at </p>
<p><a href="https://leanprover.github.io/reference/using_lean.html#creating-new-packages" target="_blank" title="https://leanprover.github.io/reference/using_lean.html#creating-new-packages">https://leanprover.github.io/reference/using_lean.html#creating-new-packages</a></p>
<p>to make a new package. Then you can open this folder with VS Code and it might all work. </p>
<p>When you're using the command line you have a "current working directory", which you might be able to see with a command like <code>pwd</code> (whether this works or not depends on exactly which Windows command line tool you're using). You can move between directories with command line commands, you can make new directories and so on. If you can make a new directory called something like <code>C:\Users\Guillermo\Lean_stuff\my_project</code> and change into that directory on the command line, and if <code>leanpkg</code> is on your path, then all of this might work fine.</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Installing%20lean/near/128987757):
<p>The message seems to be from VS Code, not Lean or elan</p>


{% endraw %}
