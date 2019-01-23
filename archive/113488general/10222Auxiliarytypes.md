---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10222Auxiliarytypes.html
---

## Stream: [general](index.html)
### Topic: [Auxiliary types](10222Auxiliarytypes.html)

---


{% raw %}
#### [ Kenny Lau (Dec 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490448):
I've been thinking about auxiliary types. Types like `additive` and `multiplicative`. Types that help the type-class inference system do its job. Interestingly I don't see a wide use of auxiliary types. I understand that one of the inconveniences is that sometimes you want to refer to elements of the original type, and transferring between the real type and the auxiliary type might prove a bit troublesome. What are your thoughts on auxiliary types?

#### [ Kenny Lau (Dec 12 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490470):
So for example there are `def`initions that should be instances, but is not so because the typeclass system could not possibly figure out the argument. What if we then created auxiliary types to solve this problem?

#### [ Mario Carneiro (Dec 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490751):
auxiliary types can be used to help here

#### [ Mario Carneiro (Dec 12 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490855):
for example, if you have a module on `B` from a ring hom `f : A -> B`, then this is a bad instance because the ring hom `f` is not a typeclass but it is required for the instance. If you have a wrapper type `ring_hom_module f := B`, then lean can handle it because it is now inferred by unification instead of typeclass inference

#### [ Mario Carneiro (Dec 12 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490860):
This is how `Qp` works, for example

#### [ Kenny Lau (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490927):
what is Qp?

#### [ Mario Carneiro (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490931):
actually never mind, that's not a good example (it is an example of something else)

#### [ Mario Carneiro (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490937):
padic rats

#### [ Kenny Lau (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490940):
actually I've been using exactly the same example and it has been working great

#### [ Kenny Lau (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490947):
I'm now experimenting them on semidirect products

#### [ Mario Carneiro (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490959):
aha, `zmodp` is an example

#### [ Mario Carneiro (Dec 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151491042):
it has an explicit argument `hp : prime p` so that lean can derive the field instance

#### [ Mario Carneiro (Dec 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151491051):
semidirect product is a pretty good example

#### [ Kenny Lau (Dec 12 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151494819):
@**Mario Carneiro** it worked great with dihedral

#### [ Kenny Lau (Dec 12 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151494900):
https://github.com/kckennylau/Lean/blob/master/semidirect_product.lean

#### [ Simon Hudon (Dec 12 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151494983):
(deleted)

#### [ Kenny Lau (Dec 16 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151873964):
I think we should use auxiliary types for modules

#### [ Kevin Buzzard (Dec 16 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151874110):
@**Mario Carneiro** you hoped that Kenny would know how to fix modules but he knows several possible solutions. Which is best?

#### [ Mario Carneiro (Dec 16 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151874162):
what is the proposal exactly?

#### [ Kevin Buzzard (Dec 16 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151876446):
I don't even understand the outparam proposal, I am still an outparam amateur

#### [ Kevin Buzzard (Dec 16 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151876486):
There's an old thread which goes through it which I will dig up at some point

#### [ Kenny Lau (Dec 16 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151876777):
something like:
```lean
universes u v

class has_scalar (α : Type u) (γ : Type v) := (smul : α → γ → γ)

infixr ` • `:73 := has_scalar.smul


structure module.core (R : Type u) [ring R] (M : Type v) [add_comm_group M] extends has_scalar R M :=
(smul_add : ∀ (r:R) (x y:M), r • (x + y) = r • x + r • y)

def module_type {R : Type u} [ring R] {M : Type v} [add_comm_group M] (m : module.core R M) := M
```


{% endraw %}
