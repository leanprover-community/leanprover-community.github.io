---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11835rewriteunderapi.html
---

## Stream: [general](index.html)
### Topic: [rewrite under a pi](11835rewriteunderapi.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751362):
```lean
import data.real.basic

lemma quadroots {x : ℝ} : x ^ 2 - 3 * x + 2 = 0 ↔ x = 1 ∨ x = 2 := sorry

example : ∀ x : ℝ, ¬ (x ^ 2 - 3 * x + 2 = 0 → x = 1) :=
begin
  rw quadroots, -- fails
  sorry
end

```

I thought this would work. I have to `intro x` before it does. I know that `rw` can fail to rewrite under a lambda, but this is not a lambda, right? Can Lean also not rewrite under a pi?

#### [ Mario Carneiro (Sep 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751519):
it cannot rewrite under a binder, because it needs to produce a substitution instance in the outer context

#### [ Mario Carneiro (Sep 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751597):
To be clear, you can rewrite expressions that don't make use of the binder, like rewriting `y` to `z` in `\lam x, x = y`

#### [ Mario Carneiro (Sep 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751631):
but since `rw` constructs an `eq.rec` term in the outer context it doesn't make sense to refer to `x`

#### [ Mario Carneiro (Sep 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751697):
Think of it this way: `rw quadroots` is really `rw [quadroots _]`. What should go in for `_`?

#### [ Reid Barton (Sep 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751779):
Interesting. I also encountered this exact question the other day--I expected `rw` to work in a similar situation, rewriting under a Pi, because it wasn't rewriting under a lambda. But I don't remember what ended up happening. It's possible I was in the "doesn't depend on x" situation.

#### [ Reid Barton (Sep 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751917):
Can I think about it this way? I expect `rw` to apply something like "`Pi.congr`". But what is the argument to `Pi.congr`. It should just be an equality I intend to rewrite along, not something of the form `\all x, f x = g x`

#### [ Mario Carneiro (Sep 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751955):
`rw` does not use `Pi.congr` or anything like it

#### [ Mario Carneiro (Sep 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751965):
that's how `simp` works

#### [ Mario Carneiro (Sep 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752021):
`rw` only uses `eq.rec`, i.e. the substitution property of equality

#### [ Reid Barton (Sep 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752051):
Right, okay. But `eq.rec` still has that argument we have to provide

#### [ Mario Carneiro (Sep 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752086):
so your goal has to have the form `|- P a` in the current context, and it is given an equality `|- a = b`, again in the current context (it may have metavariables but they have to be resolved in the current context), to produce `|- P b`

#### [ Mario Carneiro (Sep 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752175):
In particular, it must be possible to write your goal as some function applied to the thing you want to rewrite, and this implies that it can't be a term that exists under a binder

#### [ Mario Carneiro (Sep 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752251):
It's like you only know equality at one point and want to generalize to equality at all points - it doesn't work

#### [ Mario Carneiro (Sep 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752519):
If you use a quantified equality as input to `rw`, it *first* applies some metavariables with the hope of matching them in the term, but before it has entered any binders. So that means you can always specify them yourself and give straight equations to `rw` with no loss of generality, unlike with `simp` where quantified equations are really more powerful

#### [ Kevin Buzzard (Sep 27 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752964):
In my example, it's clear what I mean -- I want to rewrite "forall x, q(x)=0 -> ..." as "forall x, (x=1 or x=2) -> .."

#### [ Kevin Buzzard (Sep 27 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752988):
There doesn't seem to be anything stopping that rewrite in theory

#### [ Kevin Buzzard (Sep 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753029):
I can do it with intro, rw, revert. I'm not sure my users can though.

#### [ Kevin Buzzard (Sep 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753060):
I guess they'll have to ;-)

#### [ Mario Carneiro (Sep 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753132):
Of course, I follow. I'm just saying that's not how `rw` works

#### [ Mario Carneiro (Sep 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753150):
the closest approximation to `rw` + binders is `conv {rw}`

#### [ Kevin Buzzard (Sep 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753184):
Thank you Mario for your explanation. I find now I'm a more mature Lean user that when things like this happen I am now interested in understanding why they're failing (rather than banging my head against a table)

#### [ Kevin Buzzard (Sep 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753303):
```lean
import data.real.basic

lemma quadroots {x : ℝ} : x ^ 2 - 3 * x + 2 = 0 ↔ x = 1 ∨ x = 2 := sorry

example : ∀ x : ℝ, ¬ (x ^ 2 - 3 * x + 2 = 0 → x = 1) :=
begin
  simp only [quadroots], -- WORKS! 
  sorry
end

```

#### [ Mario Carneiro (Sep 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753343):
right. `simp` uses a different algorithm, based on congruence lemmas, which has the advantage that you can rewrite under binders

#### [ Mario Carneiro (Sep 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753465):
Rather than trying to match the goal all in one go like `rw`, it recurses into the term with things like `funext` that actually give you the opportunity to bubble those equalities into the inner context

#### [ Kevin Buzzard (Sep 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753580):
rofl just noticed example is mathematically wrong ;-) [forall needs to go inside the brackets]


{% endraw %}
