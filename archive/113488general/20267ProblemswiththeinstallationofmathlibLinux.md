---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20267ProblemswiththeinstallationofmathlibLinux.html
---

## Stream: [general](index.html)
### Topic: [Problems with the installation of mathlib (Linux)](20267ProblemswiththeinstallationofmathlibLinux.html)

---


{% raw %}
#### [ Bruno Bentzen (Oct 10 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135515887):
<p>Hello,</p>
<p>I am trying to get mathlib working in a new package of mine. I did the following</p>
<p>leanpkg new my_project<br>
  cd my_project<br>
  leanpkg add leanprover/mathlib</p>
<p>then I created a test.lean file with import group_theory.subgroup and then #check is_subgroup, and I run</p>
<p>leanpkg build</p>
<p>but although I can see all .olean files in my_project/_target/deps/mathlib/group_theory/, I get the following error message in VS Code: </p>
<p>"invalid import: group_theory.subgroup<br>
 could not resolve import: group_theory.subgroup"</p>
<p>(although I heard that it is less crucial now, I also installed elan as described in <a href="https://github.com/leanprover/mathlib/blob/master/docs/elan.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/elan.md">https://github.com/leanprover/mathlib/blob/master/docs/elan.md</a>).</p>
<p>After a few unsuccessful attempts, I decided to install mathlib globally instead with</p>
<p>leanpkg install leanprover/mathlib</p>
<p>now I have all .olean files in ~/.lean/_target/deps/mathlib but I am still getting the same error.</p>
<p>Finally, I am using Ubuntu and VS Code works perfectly in other Lean projects without mathlib.</p>
<p>Any help would be greatly appreciated!</p>
<p>Best,<br>
Bruno</p>

#### [ Bryan Gin-ge Chen (Oct 10 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135516395):
<p>Hi Bruno, I'm guessing you didn't get any errors when you ran <code>leanpkg build</code> from the console? What happens if you run <code>lean test.lean</code> from the VS code console?</p>

#### [ Mario Carneiro (Oct 10 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135516646):
<p>Make sure you have opened vscode to the folder "my_project"</p>

#### [ Bruno Bentzen (Oct 10 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135516827):
<p>Hi Bryan and Mario! Thank you for your prompt response. I am sorry, I am a still a VS code newbie --- could you please tell me how do I run lean test.lean from the VS code console and how do I open VS code to the my_project folder?</p>

#### [ Bryan Gin-ge Chen (Oct 10 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135517351):
<p>When you open VS Code, you can choose "Open folder" from the "File" menu, click on your <code>my_project</code> directory and press open.</p>
<p>To open a console in VS Code, choose "Terminal" from the "View" menu. That will open a terminal in the directory that you've opened in VS Code.</p>

#### [ Bruno Bentzen (Oct 10 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135519374):
<p>Hi Bryan (and Mario), yes, opening the folder solved the issue! (I'm sorry for the silly question, by the way!)</p>

#### [ Scott Morrison (Oct 10 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135519800):
<p>No problem! We're still sorting out the document and tutorials for these things, so it's great to have questions, so we know what needs to be said!</p>

#### [ Bruno Bentzen (Oct 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135519874):
<p>I see, Scott! Thank you guys!</p>

#### [ Kevin Buzzard (Oct 10 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135520320):
<blockquote>
<p>Hi Bryan (and Mario), yes, opening the folder solved the issue! (I'm sorry for the silly question, by the way!)</p>
</blockquote>
<p>It's not a silly question at all -- in fact it's a valuable data point! The community is currently desperately trying to get some comprehensible and failsafe instructions up and running.</p>

#### [ Bruno Bentzen (Oct 10 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135522854):
<p>I am glad to hear that, thanks Kevin! :)</p>


{% endraw %}
