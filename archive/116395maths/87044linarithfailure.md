---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/87044linarithfailure.html
---

## Stream: [maths](index.html)
### Topic: [linarith failure](87044linarithfailure.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363230):
I've started doing basic analysis in Lean with the undergraduates and I'm really using `linarith` a lot, it's really handy for this sort of thing. I was trying to prove that 1/n tended to zero using it, and I ran into this: 

```lean
example (a b c : ℝ) (h1 : 1 / a < b) (h2 : b < c) : 1 / a < c := by linarith -- fails

```

Is that a bug, or am I asking too much?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363405):
that looks like a bug

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363437):
does `generalize : 1/a = x; linarith` work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 17 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363577):
Yeah, that should be within scope. I'm guessing it's still too aggressive about ignoring nonlinear things, instead of trying to work with the linear parts. I fixed something related a while back iirc, but maybe not enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363825):
`linarith h1 h2` should work if it's a filtering problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363832):
Yes, generalizing works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363853):
`linarith` takes arguments??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363871):
apparently (reading the src now)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 17 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363877):
It might reject it at the parsing step though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 17 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363904):
I'll look into it soon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 17 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155363935):
linarith takes arguments, in case you have lots of hypotheses and know which ones are contradictory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365130):
PS this was great:

```lean
example (x y : ℝ) : abs (x + y) ≤ abs x + abs y :=
begin
  unfold abs, unfold max,
  -- goal with three ite's in
  split_ifs,
  -- 8 goals
  repeat {linarith},
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365202):
You can replace that `, repeat` with a `;`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365214):
But that's less readable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155365246):
It requires knowing what `;` does, but then it's readable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 17 2019 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366709):
This is buried a little deeper than I expected. It's a mistake in the part of `linarith` that normalizes non-integer coefficients (in `norm_hyp_aux` I think). I'll fix it, but not tonight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366787):
Thanks for chasing this up! I really want to let undergraduates see that doing basic analysis in Lean is really easy, the triangle inequality proof went down really well!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366901):
I'm also very interested in this. Do you have files to share?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155366917):
I've only given one lecture so far and I've done barely anything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367083):
https://github.com/ImperialCollegeLondon/M1P1-lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367161):
I proved a sequence has at most one limit; I used ring to prove things like e + e = 2 * e and Kenny was in the front row exploding.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367175):
But I can't teach all the students the 100 lemmas each of which can be proved by ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367186):
I want to just teach them ring instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367420):
My plan is to track their lectures and prove the interesting theorems as they're proved in class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367472):
wow, you really jumped right in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367509):
in the ITP class Jeremy and I are teaching we've barely got to what a `def` is, how `variable` and `section` work and so on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367534):
I asked the lecturer. He said that he was going to assume that the reals were a complete archimedean field and develop everything from that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367547):
This is why we need mathematicians to teach proof assistants

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/155367632):
so my plan was to spend the term trying to prove the things he proved, but in Lean. I would imagine that many of them are in mathlib already, but I didn't even look at the definition of a sequence tending to a limit in case it used cofinite filters. Of course I used the epsilon / N definition, because that's what they're told.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 17 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith%20failure/near/156324714):
Never mind, I fixed it tonight. There could be some similar cases that this fix misses though.


{% endraw %}
