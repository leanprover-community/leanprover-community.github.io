---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58432headreduction.html
---

## Stream: [general](index.html)
### Topic: [head reduction](58432headreduction.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 23 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136343289):
Is there a way to do head reduction on a term until the head changes? So I want to do something very similar to `whnf`, except I want to stop reducing as soon as the head changes.
Alternatively, I want a tactic which does a *single* head reduction step.
If I have to write this myself, is there any way to do the reduction `@nat.rec P h₀ h₁ (succ n) ⟶ h₁ n (@nat.rec P h₀ h₁ n)`without reducing too much?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 23 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136345069):
Here is the backstory, because maybe I'm approaching it wrong.
The `induction` tactic has some flaws, and has one restriction which is very annoying for the HoTT library: all user-defined recursors have to eliminate to **all** universes, including `Prop`, which is unacceptable for HoTT. Therefore, I'm writing my own `hinduction` tactic, which tries to do essentially the same as `induction`tactic.

Now I'm having trouble with the following case. I write `hinduction x using my_rec`. Suppose the type of `x` is `F a b c` and the type of `my_rec` expects something of type `G ? ?`. Now I want to check whether by unfolding `F` and reducing, I can get something with head `G` (and figure out the arguments of `G`). I *do* want to support the case where `G` is a definition, so I *cannot* use the weak-head normal form of `F a b c`. There are a couple possible approaches:
* What I described above: repeatedly do a single head reduction and see if the head is now `G`.
* Maybe I can do `whnf` but unfold all definitions, except `G`?
* I could try to unify `F a b c` with `G _ _`. This last approach is something I think I know how to do, so maybe that is the best solution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136347162):
`whnf` should already stop at definitions that are irreducible. Do you really want to support user recursors on (semi-)reducible definitions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136348052):
I think so. In the HoTT library we define higher inductive types in terms of other higher inductive types. For example, the suspension is defined as a homotopy pushout, and the circle is defined as a suspension. 
Every higher inductive type comes with its own custom induction principle, but I still want to be able to apply theorems about suspensions for the circle. So I don't think I want the circle to be irreducible.
This is how it worked in Lean 2, and it was fine in practice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136349422):
I think you should try to unify the types for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/head%20reduction/near/136349454):
You can figure out the number of underscores by adding them until you get something that is a type


{% endraw %}
