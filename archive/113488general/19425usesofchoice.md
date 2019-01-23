---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19425usesofchoice.html
---

## Stream: [general](index.html)
### Topic: [uses of choice](19425usesofchoice.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 07 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135362955):
Inspired by my post in the thread "what is wrong with HoTT" I had two questions:

(1) What are some uses of `classical.choice` in mathlib. I'm not interested in uses of LEM or the axiom of choice, but in the strong form of choice which is inconsistent with HoTT. Are the applications of them avoidable if some things were designed a little differently? 

(2) Can you define something of the following type without using choice?
`Π(A : ℕ → Type) (f : Πn, A n → A (n+1)) (n m : ℕ) : n ≤ m → A n → A m`
It is easy to do if `≤` lives in `Type`, by induction on `≤` (as an inductive family), but it is less obvious when `≤` lives in `Prop`, since then it doesn't eliminate into `Type`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 07 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363015):
Re (1): Would you please recall the difference between AoC and "strong form of choice". Mere mathematicians don't exactly know the difference...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 07 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363414):
`classical.choice` states `nonempty A -> A` (it allows you to construct "data" out of a proposition). The axiom of choice states for every surjective function there *exists* a section (which is still a proposition).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363419):
```lean
example (A : ℕ → Type) (f : Πn, A n → A (n+1)) (n m : ℕ) : n ≤ m → A n → A m :=
nat.rec_on m
  (λ n H An, @eq.rec_on _ _ A _ (nat.eq_zero_of_le_zero H) An)
  (λ m ih n H An, if h : n ≤ m then f m (ih n h An)
    else eq.rec_on (le_antisymm H (lt_of_not_ge h)) An) n
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 07 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363463):
@**Floris van Doorn**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 07 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363530):
nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 07 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135364864):
Regarding (1), [this recent thread](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances.20regarding.20naturality) is distantly related (at least we talk about using `choice` in the context of defining the dimension of a vector space.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135371908):
@**Floris van Doorn** One interesting use of `choice` is in `filter.lim`, which constructs the limit of a filter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135371916):
It's a unique choice only if we assume the topology is T2 (and it is a topology)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135371990):
There are also things like `quotient.out` (pick an element from an equivalence class), which are fully nonconstructive. You might be able to encapsulate this in a proof method for subsingletons, though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387211):
@**Floris van Doorn** I think this might be a deal-breaker. I would like to explore it further.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387218):
I don't even know what "eliminating into Prop" or "into Type" means.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387228):
But my gut feeling says that we need to be able to `choose` data.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387461):
```quote
I don't even know what "eliminating into Prop" or "into Type" means.
```
I think it means that if you do `cases` on `A or B` then stuff breaks if your goal is data, because `or` "only eliminates into Prop", i.e. `or.rec` is `protected eliminator or.rec : ∀ {a b C : Prop}, (a → C) → (b → C) → a ∨ b → C`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387465):
The idea is that you can construct choicy things but at the end of the day it has to be in service of proving an exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387467):
Note that the "motive" `C` has to be a Prop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387525):
incidentally, this is the way things are in metamath - with ZFC the axiom of choice ends in an exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387540):
So there might not be a problem after all?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387552):
Can we do algebraic closures with HoTT's AoC?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387560):
And Zorn, and all the other things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387566):
Zorn's lemma proves *there exists* a maximal element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387569):
and *there exists* an algebraic closure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387574):
but unless you can turn these into unique exists this isn't actually a construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387613):
Aah, you forgot to typeset that as *exists*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387620):
Are constructions important for these things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387621):
it is for various conveniences

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387629):
i.e. it is messy to talk about "a complete ordered field" every time you just want R

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387647):
it makes all your theorems longer and gives you more things to juggle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387654):
Ok... I don't understand enough of this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387711):
But for example if all you have is a proof that there exists an alg closure, then you just have a relatively long lived hypothesis saying E is an algebraic closure of F

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387714):
@**Mario Carneiro** Do you think it means that algebraic closures are harder to do in HoTT than in DTT?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387721):
And harder to *use*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387726):
and then when you get to the end of whatever you needed them for you use the exists assumption to discharge the hypothesis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387800):
it means there is no function `alg_closure : field -> field`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387820):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387832):
But we *can* prove that such a function exists.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387839):
but there is a kind of yoneda version `(closure -> p) -> (field -> p)` (where `p : Prop`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387989):


```quote
But we *can* prove that such a function exists.
```
I think in number theory it's very easy to forget that you have to make a big choice here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388234):
This is one of those issues where a whole bunch of stuff (Frobenius elements, traces of Galois representations etc etc) is all built with an implicit understanding that nobody will ever say anything which will depend on the choice of algebraic closure. Some people probably don't check this or even understand it. But you follow what other people do and it works. Any statement you make about "the" absolute Galois group of $$\mathbb{Q}$$ or "the" maximal extension of $$\mathbb{Q}$$ unramified outside a finite set of primes $$S$$ -- all these sentences should have an inbuilt resiliance to changing your choice. The moment you make such a choice you are in some sense running the risk that someone else might need your constructions or theorems but with a different choice, and then you need this `transfer` tactic to make sure that you can move from your choice to theirs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388391):
Now ZF (even without the C) has unique choice, so you can actually do constructions if you can prove the choice doesn't matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388445):
but mathematicians actually take this one step further, by conflating unique with unique up to isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388472):
Well, we are ok with "unique up to contractible choice"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388499):
I am pretty sure that lots of field extension arguments are not unique in the strict sense required by ZFC or DTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388584):
Interestingly HoTT has exactly the right combination of univalence + unique choice to make this work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388666):
actually, maybe not... it depends on how the isomorphisms are presented. If you just prove there exists an isomorphism even HoTT won't swallow it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388691):
The choice of algebraic closure is unique up to hugely non-unique isomorphism and this exactly the problem. It makes talking about elements of absolute Galois groups almost meaningless. Even if you choose a different algebraic closure to me and instantly fix an isomorphism of yours with mine, I might find that I want to fix a different isomorphism of mine with yours, so our dictionaries from moving between the two isomorphic absolute Galois groups are different -- they differ by an inner automorphism. This is why Langlands' philosophy is so successful -- it pushed the idea of looking at representations of Galois groups rather than understanding the structure of the groups themselves. Representations are not changed (up to isomorphism) by an inner automorphism of the group.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388756):
right, it's only stuff that is invariant under inner automorphism that would be HoTT constructible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388839):
ZFC might still have trouble turning this into a construction, unless you can get the carrier to sit still

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388842):
and lean will of course use its global choice function to construct anything you like with no assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135389252):
```quote
and lean will of course use its global choice function to construct anything you like with no assumptions
```
Right -- but then you need the transport de structure tactic to ensure that people can apply the theorem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135415520):
These are interesting comments. My experience in undergraduate math courses is that mathematicians are careful with things like non-unique limits in a topological space which is not T2. But maybe that just in undergraduate math courses :)
For something like algebraic closures, I think mathematicians will be careless, since the algebraic closure is unique, even though the isomorphism between two instances is non-unique. This means that in HoTT you indeed cannot write a function `algebraic_closure : field -> field`. 

What's interesting, is that we can express this situation very nicely in HoTT. In HoTT, the type `field` is considered as the groupoid of fields and isomorphisms. If we just knew that for every field there *exists* an algebraic closure, we can write that as a function: `field -> ∥ field ∥_{-1}`, where `∥ X ∥_{-1}` is called the *propositional truncation* of `X`, which is the HoTT-analogue of `nonempty` (turning a type into a prop by making all elements equal). However, we can express the fact "for every field there exists an algebraic closure unique up to non-unique isomorphism" as a function `field -> ∥ field ∥_{0}`. Here `∥ X ∥_{0}` is the **set** of connected components of `X`, turning a type into a set by making all proof of equality in `X` equal. This means that in HoTT, as long as you are constructing an element in a set (or proposition), you may assume that a given field has a chosen algebraic closure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135415608):
This sounds really cool!


{% endraw %}
