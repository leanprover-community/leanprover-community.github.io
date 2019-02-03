---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/71667Mitchell.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Mitchell](https://leanprover-community.github.io/archive/113489newmembers/71667Mitchell.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Mar 06 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123344776):
<p>Hi <span class="user-mention" data-user-email="u5796267@anu.edu.au" data-user-id="110504">@Mitchell Rowett</span> ! How is your group theory going?</p>

#### [ Mitchell Rowett (Mar 06 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345312):
<p>I'm constructing a pull request  for subgroups and cosets as we speak, but I think it will have to wait until morning - I'm having some technical issues.</p>

#### [ Patrick Massot (Mar 06 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345420):
<p>My computer tells me you wrote "I think it will have to wait until morning" at 11:55am, so it was still morning <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Mar 06 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345423):
<p>Is your technical issue a Git issue or Lean issue?</p>

#### [ Mitchell Rowett (Mar 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345488):
<p>I think it's a path issue from having two versions of mathlib</p>

#### [ Patrick Massot (Mar 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345489):
<p>What time is it for you? 10pm or something?</p>

#### [ Mitchell Rowett (Mar 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345498):
<p>Yep</p>

#### [ Patrick Massot (Mar 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345511):
<p>You should have a Lean package  organized as explained in <a href="https://leanprover.github.io/reference/using_lean.html#using-the-package-manager" target="_blank" title="https://leanprover.github.io/reference/using_lean.html#using-the-package-manager">https://leanprover.github.io/reference/using_lean.html#using-the-package-manager</a></p>

#### [ Patrick Massot (Mar 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345513):
<p>Then there is no more Lean path issues</p>

#### [ Mitchell Rowett (Mar 06 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345573):
<p>Ah, that's embarrassing. I should have thought of that.</p>

#### [ Patrick Massot (Mar 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345635):
<p>well actually mathlib itself has not yet switched to this new layout</p>

#### [ Patrick Massot (Mar 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345647):
<p>So I guess I'm wrong when suggesting this about a mathlib PR.</p>

#### [ Patrick Massot (Mar 06 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345670):
<p>I think you should use leanpkg  for all your project except mathlib. Then there is no user-wide copy of mathlib floating around. Each project has its copy and of course your clone of mathlib for PR purposes is its own copy of mathlib</p>

#### [ Patrick Massot (Mar 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345737):
<p>If you use Linux you can check <code>$HOME/.lean/_target/deps</code> to see if you have a user-wide copy of anything</p>

#### [ Patrick Massot (Mar 06 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345792):
<p><span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> are you interested in having a PR moving mathlib to the new fashionable leanpkg layout?</p>

#### [ Mitchell Rowett (Mar 06 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345861):
<p>Thanks Patrick. It doesn't look like I have a user-wide copy. I think I'm just missing something obvious.</p>

#### [ Mario Carneiro (Mar 06 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345867):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span>  Has anything changed here recently? Does leanpkg support import renames now or something?</p>

#### [ Mario Carneiro (Mar 06 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345881):
<p>If nothing has changed besides documentation, I'm not seeing why to change mathlib</p>

#### [ Patrick Massot (Mar 06 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345932):
<p>I'm not aware of new features, but Lean issues a warning each time you compile mathlib because the source files are not in <code>src</code>. Maybe it's related to new smarter recompilation policies but I'm not sure, we need to ask <span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Patrick Massot (Mar 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123346013):
<p><span class="user-mention" data-user-email="u5796267@anu.edu.au" data-user-id="110504">@Mitchell Rowett</span> What happens exactly when you go to your mathlib working directory and type <code>lean --make</code>?</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347167):
<p>Using <code>src/</code> for a package fixes a few issues related to dependencies and tests. mathlib doesn't have any dependencies, but moving <code>tests</code> to <code>test</code> and everything else to <code>src</code> would at least mean that mathlib users cannot import the tests. And remove the warning message.</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347210):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span></p>
<blockquote>
<p>I think you should use leanpkg for all your project except mathlib.</p>
</blockquote>
<p>What do you mean by that?</p>

#### [ Patrick Massot (Mar 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347385):
<p>I meant mathlib has no dependency and is not yet using the new layout so there is no point in using leanpkg here</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347443):
<p>Ah, okay. On the flip side, there really is no benefit of <code>lean --make</code> over <code>leanpkg build</code> even for mathlib.</p>


{% endraw %}
