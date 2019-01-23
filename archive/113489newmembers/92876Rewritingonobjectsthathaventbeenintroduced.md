---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/92876Rewritingonobjectsthathaventbeenintroduced.html
---

## Stream: [new members](index.html)
### Topic: [Rewriting on objects that haven't been introduced](92876Rewritingonobjectsthathaventbeenintroduced.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147983997):
I have the following term in my goal:
```lean
tendsto (λ (h : ℝ), ((f + g) (x + h) - (f x + g x) - (f' x + g' x) * h) / h) (nhds 0) (nhds (0 + 0))
```
And want to rewrite `pi.add_apply` to the `(f + g) (x + h)` term. But I can't, since `h` is not really a variable. Is there any way to work with rewrites on `h` without introducing everything before it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984304):
`simp` can do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984323):
Try `simp only [pi.add_apply]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984354):
In this case it's probably definitionaly true, so you could probably also use `change`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984402):
Ok, sure, that works here -- but in a situation where the rewrite can't be done with `simp` (e.g. if it involves `\l`), is there a more general solution? I mean, what is `simp` actually using behind the scenes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984408):
something like `tendsto (λ (h : ℝ), (f (x + h) + g (x + h) - (f x + g x) - (f' x + g' x) * h) / h) (nhds 0) (nhds (0 + 0))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984423):
`conv` can be the answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984435):
but `simp` can also go under binders sometimes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984444):
Hm, hadn't heard of `conv`. Interesting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984465):
https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984520):
One more question -- to get the goal in the form above with `nhds(0 + 0)` and stuff, I couldn't just use a simple rewrite `rw ←zero_add`, because `rw` becomes too overzealous and turns both `0`s to `0+0` (instead I had to `have` a statement that the new goal implies the old goal and prove that by `rw zero_add`). Is there any way to gain some control over the rewrite and make it transform things one at a time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984625):
See https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg and also the `conv` doc I mentioned in my previous answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984664):
Thanks, I'll have a look at it.


{% endraw %}
