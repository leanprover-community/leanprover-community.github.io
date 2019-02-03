---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09652fixLEANPATH.html
---

## Stream: [general](index.html)
### Topic: [fix LEAN_PATH](09652fixLEANPATH.html)

---


{% raw %}
#### [ garySebastian (Apr 01 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124468992):
<p>I've tried to get lean to work on Xubuntu, macOS, and nixos; all three are having the same issue where importing anything (including standard), yields an error: "file standard not found in the LEAN_PATH". I've done a lot of looking around and can't find any relevant information on LEAN_PATH. I have lean in my system PATH. I'm not sure what it wants from me.</p>

#### [ Simon Hudon (Apr 01 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124469133):
<p>Do you use <code>leanpkg</code>?</p>

#### [ garySebastian (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124469340):
<p>I've tried creating a new project and doing configure/messing with the leankpkg.path, but it doesn't seem to do anything.</p>

#### [ Simon Hudon (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124469437):
<p>Setting <code>LEAN_PATH</code> by hand leads to nothing but trouble so I suggest you unset it (if you set it yourself), create a Lean project with <code>leanpkg init</code>and using <code>leanpkg add</code> for your dependencies</p>

#### [ garySebastian (Apr 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124470287):
<p>Thank you for the advice so far, but I'm still getting the same error after trying both leanpkg add <a href="https://github.com/leanprover/mathlib" target="_blank" title="https://github.com/leanprover/mathlib">https://github.com/leanprover/mathlib</a> and <a href="https://github.com/leanprover/stdlib.git" target="_blank" title="https://github.com/leanprover/stdlib.git">https://github.com/leanprover/stdlib.git</a>. They're both in the _build directory within the project, and they were both added to the leanpkg.path file and leanpkg.toml files.</p>

#### [ Simon Hudon (Apr 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124470526):
<p>can you show me your <code>leanpkg.toml</code> file and tell me where you put your source file?</p>

#### [ Patrick Massot (Apr 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124482877):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> and <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  This is one more motivating example for you. We really need to make it simpler for people to start using Lean</p>

#### [ Kenny Lau (Apr 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124482878):
<p>I concur</p>

#### [ Patrick Massot (Apr 01 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124482884):
<p>I mean: I know you are working hard, I only want to point out further encouragement.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493380):
<p>Doesn't this all depend on how you are running Lean?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493383):
<p>For example, I _think_ that if you use VS Code and open a folder</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493384):
<p>and there's e.g. some <code>leanpkg.path</code> file in the root of that folder</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493386):
<p>then I think VS Code will look at that file before it looks at the <code>LEAN_PATH</code> environment variable [NB but apparently I am wrong]</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493392):
<p>What is this <code>_build</code> directory you're talking about <span class="user-mention" data-user-id="111151">@garySebastian</span> ?</p>

#### [ Gabriel Ebner (Apr 01 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493394):
<p>Neither vscode nor emacs touches the LEAN_PATH environment variable.  If it is set, it takes precedence over any <code>leanpkg.path</code> file.  Please don't set the <code>LEAN_PATH</code> environment variable.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493438):
<p>If you just follow the step by step instructions for making a new project and adding mathlib, I think it will add mathlib into a directory called <code>_target</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493440):
<p>(I am talking about using <code>leanpkg</code>)</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fix%20LEAN_PATH/near/124493486):
<p>and everything should magically work because <code>leanpkg</code> will get your <code>leanpkg.path</code> right and you won't need to set <code>LEAN_PATH</code> at all by the looks of things</p>


{% endraw %}
