---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83804simplemmaabab.html
---

## Stream: [general](index.html)
### Topic: [simp lemma `a + (b + -a) = b`?](83804simplemmaabab.html)

---

#### [Kevin Buzzard (Aug 05 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945303):
@**Guillermo Barajas Ayuso** wanted

```lean
import data.real.basic 

theorem auxiliary_basic (a b : ℝ) (f : ℝ → ℝ → ℝ) :
f a b = f (a + (1 - 1) * (b - a) / (2 ^ 0)) (a + 1 * (b - a) / (2 ^ 0)) := by simp -- fails

```

and `simp` didn't quite do it; it reduces the problem to `a + (b + -a) = b`. There's a non-simp lemma ` add_sub_cancel'_right : a + (b - a) = b` but `by simp [add_sub_cancel'_right]` doesn't work either, presumably because `simp` decides that replacing all `sub`s with `neg`s is a good idea before it can spot how to apply `add_sub_cancel'_right`. On the other hand actually adding what `simp` gets stuck on works fine:

```lean
import data.real.basic 

@[simp] theorem add_bracket_add_neg_self_bracket_cancel {α : Type} [add_comm_group α] {a b : α} :
a + (b + -a) = b := by rw [add_comm,add_assoc,neg_add_self,add_zero]

theorem auxiliary_basic (a b : ℝ) (f : ℝ → ℝ → ℝ) :
f a b = f (a + (1 - 1) * (b - a) / (2 ^ 0)) (a + 1 * (b - a) / (2 ^ 0)) := by simp

```

Should `a + (b + -a) = b` be a simp lemma? It's about time I got the hang of this stuff. It's passing all the rules of thumb I've picked up, but my rules of thumb are not yet watertight...

#### [Patrick Massot (Aug 06 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945623):
It's funny, I came across the exact same problem yesterday. Don't forget you can also use `simp [-sub_eq_add_neg, ...]` to get rid of the annoying "simplification"

#### [Mario Carneiro (Aug 06 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945720):
I'm okay with adding this as a simp lemma, but it doesn't really fix the problem - you will also need lemmas for `a + (b + (c + -a))` and `a + (b + (-a + c))` and so on. The problem is that simp doesn't make any attempt to bring negatives together, so at best you can get lucky if they don't have so far to migrate

#### [Mario Carneiro (Aug 06 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945760):
This is in part what `ring` is for, and Jeremy suggested also focusing an `abel` type tactic focusing only on the additive stuff

#### [Patrick Massot (Aug 06 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945763):
I also wanted to ask for a version of ring working in an abelian group

#### [Kevin Buzzard (Aug 06 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945764):
removing `sub_eq_add_neg` stops Lean from simplifying `(1 - 1)` :-)

#### [Mario Carneiro (Aug 06 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945769):
I think `sub_eq_add_neg` is a bad choice of simp lemma, but I know why it's there - it limits the expressivity of input statements so you need fewer simp lemmas overall

#### [Kevin Buzzard (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945809):
I thought that simp internally put things into some secret ordering using associativity and commutativity?

#### [Mario Carneiro (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945810):
of course if `sub_eq_add_neg` was not a simp lemma we would need `a - a = 0` to be a simp lemma

#### [Patrick Massot (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945812):
Is this also part of what Johannes simplifier work is meant to address?

#### [Mario Carneiro (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945813):
it does, but that ordering does not put `a` and `-a` close together

#### [Kevin Buzzard (Aug 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945815):
```quote
it does, but that ordering does not put `a` and `-a` close together
```
Might I suggest a different secret ordering?

#### [Mario Carneiro (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945822):
this is an active area of research

#### [Kevin Buzzard (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945824):
Oh wow

#### [Kevin Buzzard (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945826):
How come humans are so good at it?

#### [Mario Carneiro (Aug 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945827):
because they use adaptive algorithms that pay attention to the right things

#### [Mario Carneiro (Aug 06 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945868):
and that's really hard and complicated

#### [Mario Carneiro (Aug 06 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945870):
keep in mind that `simp` is used in way more circumstances than doing algebra on commutative groups

#### [Mario Carneiro (Aug 06 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945878):
and you need to keep up performance in the other areas too

#### [Mario Carneiro (Aug 06 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma%20%60a%20%2B%20%28b%20%2B%20-a%29%20%3D%20b%60%3F/near/130945930):
I think Johannes was working on adding "simpprocs" to the simplifier, which would enable this kind of adaptivity. It would notice we are doing algebra and fire up the algebra module that knows to do cancellation and stuff

