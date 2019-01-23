---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55612latticehomomorphisms.html
---

## Stream: [general](index.html)
### Topic: [lattice homomorphisms](55612latticehomomorphisms.html)

---

#### [Simon Hudon (Oct 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135284232):
Is there such a thing as a lattice homomorphism in mathlib?

#### [Johannes Hölzl (Oct 10 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135554980):
there is only one for countable suprema: `def ord_continuous (f : α → β) := ∀s : set α, f (Sup s) = (⨆i∈s, f i)`

#### [Mario Carneiro (Oct 10 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135555065):
I think that's arbitrary suprema

#### [Mario Carneiro (Oct 10 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135555155):
I should note that a "complete lattice homomorphism" has to preserve suprema *and* infima. Despite the fact that you can define suprema from infima and vice versa, there are Sup-lattice homs that are not complete lattice homs (see [wiki](https://en.wikipedia.org/wiki/Complete_lattice#Morphisms_of_complete_lattices))

#### [Mario Carneiro (Oct 10 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135555422):
@**Floris van Doorn** By the way, that wiki page also mentions something related to our discussion yesterday, on the presumed existence of "free constructions". Apparently the free complete lattice (in the category of complete lattices and complete lattice homs) does not always exist in ZFC, because you need a proper class collection of conditions

#### [Floris van Doorn (Oct 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135556029):
On free complete lattices: since the meet and the sup operations can have any cardinal as arity, you don't get a universe closed under the free complete lattice operation (probably that is inconsistent). However, with higher inductive types in HoTT you can construct free algebras for infinitary algebraic theories, which are not constructible in ZFC (without large cardinal assumptions), see https://arxiv.org/abs/1705.07088, section 9.

#### [Mario Carneiro (Oct 10 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lattice%20homomorphisms/near/135556327):
I was aware of this result, but when reading it directly I find it is weaker than expected. The paper constructs a HIT F that implies the existence of an uncountable regular cardinal; but ZFC gives scads of uncountable regular cardinals, like aleph_1. They argue that this gives additional power over ZF (which is true, since you can't prove that aleph_1 is regular without choice) but it's not clear to me how this relates to ZFC.

