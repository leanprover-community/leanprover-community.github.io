---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51083checkingimports.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [checking imports](https://leanprover-community.github.io/archive/113488general/51083checkingimports.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jakob von Raumer (Oct 10 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135554082):
<p>whenever I open vscode, lean seems to re-check all imported files... wasn't this better some time ago?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135554225):
<p>(my issue here is that I need to close all other programs, to check some imports from the hott3 library, they use up almost all of my RAM)</p>

#### [ Chris Hughes (Oct 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135554646):
<p>Did you run <code>leanpkg build</code> in the appropriate directory?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555511):
<p>Nope, shame on my, kind of assumed that vscode would somehow invoke that... <span class="emoji emoji-1f601" title="grinning face with smiling eyes">:grinning_face_with_smiling_eyes:</span></p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555567):
<p>Uhm, and <code>leanpkg build</code> also doesn't eat all of my RAMs <span class="emoji emoji-1f40f" title="ram">:ram:</span></p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555870):
<p>But unfortunately it doesn't change the fact that vscode checks everything at startup, even after a successful <code>leanpkg build</code>...</p>

#### [ Johan Commelin (Oct 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555902):
<p>Are you using <code>elan</code>? Did you run <code>leanpkg build</code> in the root of your project, or in a subdir?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556008):
<p>In the root dir... What is <code>elan</code>?</p>

#### [ Johan Commelin (Oct 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556127):
<p>Ok, you are not using <code>elan</code>.</p>

#### [ Johan Commelin (Oct 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556135):
<p>Kevin wrote this page today: <a href="https://xenaproject.wordpress.com/installing-lean-and-mathlib/" target="_blank" title="https://xenaproject.wordpress.com/installing-lean-and-mathlib/">https://xenaproject.wordpress.com/installing-lean-and-mathlib/</a></p>

#### [ Johan Commelin (Oct 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556149):
<p>Jakob, how did you install lean and mathlib?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556619):
<p>Lean: Using the sources</p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556643):
<p>Mathlib: Not sure if I have it at all... but hott3 doesn't depend on it, does it?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556718):
<p>Oh, there's a global installation of mathlib at <code>~/.lean/_target/deps</code></p>

#### [ Johan Commelin (Oct 10 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135557237):
<p>Hmmm... I don't really know enough to help you here.</p>

#### [ Rob Lewis (Oct 10 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135557629):
<p>You have fresh .olean files in your Lean root directory, right? What exactly are you opening in VS Code?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135559479):
<p>What's my lean root directory? I'm opening the folder of a project of mine in VS, which references <code>hott3</code> in its <code>.toml</code></p>

#### [ Rob Lewis (Oct 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135560271):
<p>Wherever you built the executable. If the executable lies in <code>lean/bin/</code>, then you should also have <code>lean/library/</code> with the core lib. The <code>.lean</code> files there should have fresh <code>.olean</code> files. In your project folder, do you have <code>_target/deps/hott3</code>? Are there <code>olean</code> files in there?</p>

#### [ Rob Lewis (Oct 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135560283):
<p>And are there compilation errors when you run <code>leanpkg build</code>?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135561866):
<p>Yes there's <code>.olean</code> files in <code>_target/deps/hott3</code> and not so fresh ones in <code>lean/library</code>... <code>leanpkg buid</code> goes through with warning but no errors.</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135562001):
<p>Hm, but if I run <code>leanpkg build</code> in <code>~/.lean</code>, I get loads of errors</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135562103):
<p>Oh, that's because stuff is not in <code>LEAN_PATH</code></p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135562473):
<p>Hu, but <code>lean --path</code> gives all I would expect...</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563098):
<p>Should <code>leanpkg build</code> build all the deps or just the files needed?</p>

#### [ Patrick Massot (Oct 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563180):
<p>only needed</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563290):
<p>Thanks.</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563297):
<p>And should it build files that haven't changed since the last build?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563570):
<p>If there's only deps and no actual content in <code>~/.lean</code>, how come <code>leanpkg build</code> does anything at all, if I execute it there? <span class="emoji emoji-1f615" title="confused">:confused:</span></p>

#### [ Gabriel Ebner (Oct 10 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135564693):
<p>Forget about <code>~/.lean</code>, it's independent and not used in this case (check <code>lean -p</code>, if it doesn't appear you don't need to worry about it).<br>
The easiest way to ensure all olean files are built is to run <code>lean --make</code> in the project folder.<br>
(You should also open the project folder in vscode (not a subfolder or superfolder), but I don't think that's the problem here.)</p>

#### [ Jakob von Raumer (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135565841):
<p>Now it works <span class="emoji emoji-1f937" title="shrug">:shrug:</span> Not sure what was wrong. I did a rebuild of lean itself</p>

#### [ Patrick Massot (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135565898):
<p>Why do you build Lean?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135565994):
<p>I noticed it's been a while since I last built it</p>

#### [ Patrick Massot (Oct 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135566068):
<p>Why building it at all? What's wrong with the distributed binaries? Are you modifying Lean?</p>

#### [ Jakob von Raumer (Oct 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135566172):
<p>I used to,  ages ago. Before most of the library was moved to <code>mathlib</code>... I guess I could as well use the binaries now.</p>

#### [ Scott Morrison (Oct 11 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135571392):
<p>Yeah, while Lean itself is stable at the moment, all the instructions people are giving assume you're using a binary (ideally provided by elan). <code>lean --make</code> in the <code>library/</code> directory of a built-from-sources copy of Lean can help with the issue you were experiencing.</p>


{% endraw %}
