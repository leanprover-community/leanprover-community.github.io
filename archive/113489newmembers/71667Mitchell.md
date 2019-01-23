---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/71667Mitchell.html
---

## Stream: [new members](index.html)
### Topic: [Mitchell](71667Mitchell.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123344776):
Hi @**Mitchell Rowett** ! How is your group theory going?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mitchell Rowett (Mar 06 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345312):
I'm constructing a pull request  for subgroups and cosets as we speak, but I think it will have to wait until morning - I'm having some technical issues.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345420):
My computer tells me you wrote "I think it will have to wait until morning" at 11:55am, so it was still morning :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345423):
Is your technical issue a Git issue or Lean issue?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mitchell Rowett (Mar 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345488):
I think it's a path issue from having two versions of mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345489):
What time is it for you? 10pm or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mitchell Rowett (Mar 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345498):
Yep

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345511):
You should have a Lean package  organized as explained in https://leanprover.github.io/reference/using_lean.html#using-the-package-manager

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345513):
Then there is no more Lean path issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mitchell Rowett (Mar 06 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345573):
Ah, that's embarrassing. I should have thought of that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345635):
well actually mathlib itself has not yet switched to this new layout

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345647):
So I guess I'm wrong when suggesting this about a mathlib PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345670):
I think you should use leanpkg  for all your project except mathlib. Then there is no user-wide copy of mathlib floating around. Each project has its copy and of course your clone of mathlib for PR purposes is its own copy of mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345737):
If you use Linux you can check `$HOME/.lean/_target/deps` to see if you have a user-wide copy of anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345792):
@**Mario Carneiro** are you interested in having a PR moving mathlib to the new fashionable leanpkg layout?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mitchell Rowett (Mar 06 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345861):
Thanks Patrick. It doesn't look like I have a user-wide copy. I think I'm just missing something obvious.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 06 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345867):
@**Patrick Massot**  Has anything changed here recently? Does leanpkg support import renames now or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 06 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345881):
If nothing has changed besides documentation, I'm not seeing why to change mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123345932):
I'm not aware of new features, but Lean issues a warning each time you compile mathlib because the source files are not in `src`. Maybe it's related to new smarter recompilation policies but I'm not sure, we need to ask @**Sebastian Ullrich**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123346013):
@**Mitchell Rowett** What happens exactly when you go to your mathlib working directory and type `lean --make`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 06 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347167):
Using `src/` for a package fixes a few issues related to dependencies and tests. mathlib doesn't have any dependencies, but moving `tests` to `test` and everything else to `src` would at least mean that mathlib users cannot import the tests. And remove the warning message.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 06 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347210):
@**Patrick Massot**
> I think you should use leanpkg for all your project except mathlib.

What do you mean by that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347385):
I meant mathlib has no dependency and is not yet using the new layout so there is no point in using leanpkg here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 06 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mitchell/near/123347443):
Ah, okay. On the flip side, there really is no benefit of `lean --make` over `leanpkg build` even for mathlib.


{% endraw %}
