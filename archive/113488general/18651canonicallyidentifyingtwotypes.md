---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18651canonicallyidentifyingtwotypes.html
---

## Stream: [general](index.html)
### Topic: ["canonically" identifying two types](18651canonicallyidentifyingtwotypes.html)

---

#### [Kevin Buzzard (Apr 27 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765228):
How can I beef up "equiv" into "canonical isomorphism"?

#### [Kevin Buzzard (Apr 27 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765384):
I think that's my question.

#### [Kevin Buzzard (Apr 27 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765424):
I will formulate something a bit more precise in a sec.

#### [Mario Carneiro (Apr 27 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765431):
Q1: what does that mean? Is "isomorphism" sufficient?

#### [Kevin Buzzard (Apr 27 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768206):
The proof of `funext` uses quot.sound

#### [Kevin Buzzard (Apr 27 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768208):
but if we restrict to two types in the same universe

#### [Kevin Buzzard (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768222):
```lean
  ∀ {α : Sort u} {β : α → Sort u} {f₁ f₂ : Π (x : α), β x},
    (∀ (x : α), f₁ x = f₂ x) → f₁ = f₂
```

#### [Kevin Buzzard (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768229):
so a slightly weaker result

#### [Kevin Buzzard (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768230):
can one prove this without quot.sound?

#### [Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768288):
I'm trying to work out what a mathematician means when they say that two objects are "canonically isomorphic".

#### [Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768292):
To coin a phrase, it's like pornography.

#### [Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768294):
You know it when you see it.

#### [Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768300):
I have not yet found a formulation that I like in dependent type theory.

#### [Kevin Buzzard (Apr 27 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768308):
and I think that this is an underlying source of some of my frustrations in trying to do mathematics in Lean.

#### [Kevin Buzzard (Apr 27 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768310):
Here's a probably much easier question:

#### [Kevin Buzzard (Apr 27 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768312):
what's the inverse of funext called?

#### [Kenny Lau (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768335):
`congr_fun`

#### [Kenny Lau (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768354):
wait, inverse not converse

#### [Kevin Buzzard (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768366):
that's what I wanted

#### [Kevin Buzzard (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768367):
no axioms

#### [Kevin Buzzard (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768368):
different universes

#### [Kenny Lau (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768378):
inverse?

#### [Kenny Lau (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768380):
not A implies not B?

#### [Kevin Buzzard (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768381):
Is it possible to express the notion that two types are "the same" without ever mentioning any terms?

#### [Kenny Lau (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768383):
`==`

#### [Kevin Buzzard (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768388):
Kenny you answered my question

#### [Kenny Lau (Apr 27 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768435):
inverse is `mt \o congr_fun` :P

#### [Kevin Buzzard (Apr 27 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768436):
Here are two notions of being "close to each other in type theory", which in my mind are both certainly implied by being "the same".

#### [Kevin Buzzard (Apr 27 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768448):
```lean
universe zfc
--#print extfun_app

-- Here is a notion from dependent type theory.
/-- `α ≃ β` is the type of functions from `α → β` with a two-sided inverse. -/
variables {α β : Type zfc}

structure equiv (α : Type zfc) (β : Type zfc) :=
(to_fun    : α → β)
(inv_fun   : β → α)
(left_inv  : function.left_inverse inv_fun to_fun)
(right_inv : function.right_inverse inv_fun to_fun)


variable (to_fun : α → β)
variable (inv_fun : β → α)

#reduce function.left_inverse inv_fun to_fun 
-- ∀ (x : α), to_fun (inv_fun x) = x
-- note round brackets -- explicitly demand the term

#reduce function.right_inverse inv_fun to_fun
-- ∀ (x : β), to_fun (inv_fun x) = x
-- note round brackets -- explicitly demand the term

-- Here is a notion from category theory, translated into dependent type theory.
/-- The notion of being isomorphic in a category  -/
structure isom (α : Type zfc) (β : Type zfc) :=
(to_fun : α → β)
(inv_fun : β → α)
(left_inv : inv_fun ∘ to_fun = id)
(right_inv : to_fun ∘ inv_fun = id)
```

#### [Kevin Buzzard (Apr 27 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768450):
I have stuck to one universe

#### [Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768463):
because I am a traditionalist

#### [Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768494):
Why does Lean prefer `equiv` (which is in core Lean) to `isom`?

#### [Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768495):
Is `isom` in there somewhere?

#### [Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768496):
These structures are canonically isomorphic, but I don't know the definition of canonically isomorphic

#### [Kenny Lau (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768502):
because `equiv` is more usable

#### [Kevin Buzzard (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768503):
but in dependent type theory the only way I know to construct bijective maps between them is using quot.sound

#### [Kenny Lau (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768504):
Just look at my proof in the other thread

#### [Kenny Lau (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768505):
before and after changing composition equality

#### [Kevin Buzzard (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768508):
Is it just universally true that equiv is better than isom?

#### [Kevin Buzzard (Apr 27 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768548):
I don't know what other thread you're talking about.

#### [Kevin Buzzard (Apr 27 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768549):
But I would genuinely be interested to know.

#### [Kevin Buzzard (Apr 27 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768552):
My memory is not what it was.

#### [Kevin Buzzard (Apr 27 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768576):
Anyway, I was wondering whether if one stuck to one universe, whether the restricted funext, which sounds to me like it could logically be a strictly weaker assertion, could be proved without the axiom.

#### [Kenny Lau (Apr 27 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768619):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof.20of.20the.20five.20lemma

#### [Kevin Buzzard (Apr 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768685):
Mario, I ultimately want to formalise some possibly specialised notion of being canonically isomorphic, which I can use to do amazing rewrites which a mathematician does all the time but which I find difficult to do in dependent type theory. My problem in dependent type theory is that I sometimes run into terms which are not definitionally equal, but which are "only" canonically isomorphic.

#### [Kevin Buzzard (Apr 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768686):
Because I am facing quite a tedious job otherwise

#### [Kevin Buzzard (Apr 27 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768742):
I think I want to make a new structure which is more useful to me than definitional equivalence.

#### [Kevin Buzzard (Apr 27 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768743):
It is not Lean's `=` because I want it to apply to terms of different types.

#### [Kevin Buzzard (Apr 27 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768788):
and I am quite happy to restrict to objects within one universe

#### [Kenny Lau (Apr 27 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768795):
why don't you just quotient everything with equiv

#### [Kevin Buzzard (Apr 27 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768899):
Wow, props can be equal : `@eq` is defined on `Sort u_1`

#### [Kevin Buzzard (Apr 27 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768902):
Is that concept used?

#### [Kevin Buzzard (Apr 27 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768904):
being canonically isomorphic only applies to types.

#### [Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768943):
```quote
Is that concept used?
```
a lot

#### [Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768944):
but mostly in `simp`

#### [Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768945):
`simp` rewrites Props

#### [Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768948):
using `propext`

#### [Kevin Buzzard (Apr 27 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769002):
Is this in Lean or mathlib:

#### [Kevin Buzzard (Apr 27 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769003):
`instance group_of_equiv [group α] (H : equiv α β) : group β := sorry`

#### [Kevin Buzzard (Apr 27 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769014):
If alpha and beta are canonically isomorphic, then any group structure on alpha trivially gives you a group structure on beta, any mathematician knows that.

#### [Scott Morrison (Apr 27 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769069):
I am slowly coming around to the opinion that "canonical" as used by mathematicans doesn't actually mean much, but is instead code for "we both know what is going on, and I'm just confirming that you one you have in mind is probably the one I have in mind too".

#### [Kevin Buzzard (Apr 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769113):
`instance set_equiv_of_equiv (H : equiv α β) : equiv (set α) (set β) := sorry`

#### [Kevin Buzzard (Apr 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769114):
doesn't typecheck

#### [Kevin Buzzard (Apr 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769115):
`equiv` is not a class

#### [Kevin Buzzard (Apr 27 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769125):
but if `\a` and `\b` are canonically isomorphic, then so are their power sets -- any mathematician knows that.

#### [Scott Morrison (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769131):
We could make `equiv` a class, and have the convention that we'll only even make instances that "every mathematician knows is the right one".

#### [Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769182):
But do I want to restrict myself like that?

#### [Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769184):
I am not sure

#### [Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769185):
There are two abelian groups which show up in the Langlands Philosophy

#### [Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769188):
And the Langlands Philosophy says that they are canonically isomorphic

#### [Scott Morrison (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769195):
Well... an isomorphism from `a` to `b` gives an isomorphism from `2^a` to `2^b`, sure. If you bless one as canonical, I guess that blesses the result as canonical too.

#### [Kevin Buzzard (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769198):
In fact, more generally there are two non-abelian groups which show up and Langlands conjectures that they are canonically isomorphic, and this is one of the reasons that we call it philosophy sometimes -- it is not quite mathematics.

#### [Kevin Buzzard (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769202):
But back to the abelian groups

#### [Scott Morrison (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769206):
But by that do you just mean that there's a particularly interesting/sensible isomorphism between them, and the point is not to say "these are isomorphic", but "this is an isomorphism between ..."?

#### [Kevin Buzzard (Apr 27 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769246):
Mathematicians have written down not just one, but two canonical isomorphisms between these groups!

#### [Kevin Buzzard (Apr 27 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769247):
And they're different!

#### [Kevin Buzzard (Apr 27 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769249):
One is called "global class field theory normalised so that uniformisers become identified with geometric Frobenius"

#### [Scott Morrison (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769255):
So what does canonical mean here? (I am not really confident in my skepticism of the word "canonical". I am happy to come back to the fold if the story is good.)

#### [Kevin Buzzard (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769256):
and the other is called "global class field theory normalised so that uniformisers become identified with arithmetic Frobenius"

#### [Kevin Buzzard (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769260):
The two canonical isomorphisms between the groups are related. If we write the group law multiplicatively, as is standard,

#### [Kevin Buzzard (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769261):
then if one of them is f(x)=y

#### [Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769263):
the other is f(x)=1/y

#### [Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769303):
and mathematicians choose at random which one to use

#### [Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769305):
and some even sometimes forget to say which one

#### [Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769308):
perhaps because the one they used was the most common one when the paper was written

#### [Kevin Buzzard (Apr 27 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769321):
So I am pretty sure I want to allow myself more than one canonical isomorphism between two objects

#### [Johan Commelin (Apr 27 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769721):
So, here is Kevin's remark in a down to earth example: every abelian group has a canonical automorphism, and in fact, it has two of those: the identity, and the map `a \mapsto -a`.

#### [Kevin Buzzard (Apr 27 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769731):
@**Kenny Lau** -- you wrote my function! Many thanks!

#### [Johan Commelin (Apr 27 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769733):
Of course, in the case of automorphisms, we agree that `id` is slightly more canonical then the -1 map

#### [Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769777):
But these were two different groups

#### [Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769778):
and this has caused confusion in the mathematical community

#### [Johan Commelin (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769779):
Exactly

#### [Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769781):
I think that's interesting.

#### [Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769782):
Nowadays people are careful to state which of the normalisations they are using

#### [Kevin Buzzard (Apr 27 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769789):
and unfortunately, and perhaps counter-intuitively, it can sometimes be a little tricky to figure out how to translate the statements of theorems proved using one convention into the analogous statements about the same objects had we used the other convention in the paper.

#### [Johan Commelin (Apr 27 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769790):
But Kevin, if we go for the restricted version of canonical first. The one that Scott suggested. That would already be incredibly helpful, right?

#### [Kenny Lau (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769831):
```quote
@**Kenny Lau** -- you wrote my function! Many thanks!
```
which function?

#### [Johan Commelin (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769835):
If there is one 'blessed' isomorphism, it can be traced through al sorts of constructions, and induce 'blessed' equivalences/isomorphism between other objects

#### [Johan Commelin (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769837):
Like with power sets, or group structures, etc...

#### [Kevin Buzzard (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769838):
```quote
But by that do you just mean that there's a particularly interesting/sensible isomorphism between them, and the point is not to say "these are isomorphic", but "this is an isomorphism between ..."?
```
I am quite happy to state the isomorphism. But what I want from it is a huge quota of free constructions and proofs.

#### [Kevin Buzzard (Apr 27 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769894):
I want `canonical_isomorphism` to extend (possibly a restricted universe version of) `equiv`

#### [Johan Commelin (Apr 27 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769898):
At the Lean wizards: Kevin is pointing out an incredibly important thing. As in, it is a difference in kind, not just a difference in degree.

#### [Johan Commelin (Apr 27 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769901):
It will give super-linear improvements in the de Bruijn factor.

#### [Kevin Buzzard (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769922):
and I want functions like

#### [Kevin Buzzard (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769942):
```lean
instance group_of_equiv [group α] (H : canonically_isomorphic α β) : group β := sorry
```

#### [Kenny Lau (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769947):
transport of structure

#### [Kenny Lau (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769951):
@**Mario Carneiro** maybe you could automate this?

#### [Johan Commelin (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769952):
I personally feel (but I'm a novice) that this is one of the big road blocks for formalisation of a lot of maths in the algebraic geometry corner

#### [Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769959):
I have this big Pokemon to kill

#### [Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769960):
called proof that an affine scheme is a scheme

#### [Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769962):
and it is now in its final stage

#### [Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769967):
and I want to destroy it with a one liner like this

#### [Chris Hughes (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769968):
What happened to Kenny's idea of quotienting by isomorphism?

#### [Kenny Lau (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769969):
Chris Hughes appears

#### [Kevin Buzzard (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770009):
I don't know how to implement that

#### [Kevin Buzzard (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770012):
Did you see my "three lemma" Chris?

#### [Johan Commelin (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770014):
What exactly does Kenny mean by "quotienting by isomorphism"?

#### [Johan Commelin (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770016):
Because that might be to crude...

#### [Kevin Buzzard (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770017):
I want to prove that if `A -> B -> C` is exact and we are given isomorphisms `A -> A'` and `B -> B'` and `C -> C'`

#### [Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770027):
then there is a completely obvious new exact sequence `A' -> B' -> C'`

#### [Kenny Lau (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770029):
I already proved it

#### [Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770030):
I know

#### [Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770034):
but i don't want you to spend 70 lines proving it

#### [Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770037):
I want to to agree with me that it is obvious

#### [Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770038):
and hence is only worth one line

#### [Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770086):
because a mathematician is capable of replacing `B` with the canonically isomorphic `B'` in one line

#### [Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770090):
so I can prove the theorem in 3 lines

#### [Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770092):
and I don't see anything wrong with my proof

#### [Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770095):
at every stage the next line is "do the obvious thing"

#### [Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770106):
```quote
but i don't want you to spend 70 lines proving it
```
... by which I mean

#### [Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770108):
thank you very much Kenny for proving the result for me

#### [Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770112):
and don't you think it's interesting that it took 70 lines

#### [Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770117):
but for the purposes of this thread I want 3 lines

#### [Kenny Lau (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770160):
lol

#### [Kevin Buzzard (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770163):
I want to `rw [H : canonically_isomorphic A A']`

#### [Kevin Buzzard (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770164):
and then you can guess the rest

#### [Johan Commelin (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770166):
`[...] := by repeat {transport_de_structure}`

#### [Kevin Buzzard (Apr 27 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770173):
This is exactly another one of those concepts which I have been interested in all my life but have only really now found the language to talk about them in

#### [Kevin Buzzard (Apr 27 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770225):
and perhaps this is very difficult to do in dependent type theory

#### [Kevin Buzzard (Apr 27 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770229):
because replacing `f A` with `f A'` can be quite complicated in general

#### [Kevin Buzzard (Apr 27 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770232):
but the point is that `A` and `A'` are *mathematical objects*

#### [Kevin Buzzard (Apr 27 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770235):
not these stupid general types

#### [Kevin Buzzard (Apr 27 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770246):
and so what I am hoping is that for a possibly restricted class of types there is some powerful relation on them

#### [Kevin Buzzard (Apr 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770285):
called "canonically isomorphic"

#### [Kevin Buzzard (Apr 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770291):
which you construct with functions in both directions, proofs that the composites are the identity either way (as in equiv not isom), and a little bit of extra magic

#### [Kevin Buzzard (Apr 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770294):
possibly

#### [Kevin Buzzard (Apr 27 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770300):
and then for hopefully a class of types including the kind of types showing up in mathematics

#### [Kevin Buzzard (Apr 27 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770348):
a lot of stuff can be moved around painlessly, substituting one type for a canonically isomorphic one.

#### [Kevin Buzzard (Apr 27 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770352):
So who fancies proving `equiv A B -> scheme A -> scheme B`

#### [Kevin Buzzard (Apr 27 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770366):
Wait, for what generality is this true?

#### [Johan Commelin (Apr 27 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770369):
Hmmm, Kevin, I think there are two things at play

#### [Johan Commelin (Apr 27 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770417):
There is functoriality, and transport de structure

#### [Johan Commelin (Apr 27 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770419):
and they are related, but slightly different

#### [Johan Commelin (Apr 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770423):
I don't know exactly how to explain the difference

#### [Johan Commelin (Apr 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770428):
(And maybe they actually are not)

#### [Chris Hughes (Apr 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770430):
Is this totally disgusting?
```lean
structure isom (G H : Σ α : Type*, group α) :=
(f : G.1 ≃ H.1)
(to_fun_hom : @is_group_hom _ _ G.2 H.2 f.to_fun)
(inv_fun_hom : @is_group_hom _ _ H.2 G.2 f.inv_fun)

def is_isom (G H : Σ α : Type*, group α) := nonempty (isom G H)
```

#### [Scott Morrison (Apr 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770537):
Really you want to prove `equiv A B -> equiv (scheme A) (scheme B)`.

#### [Johan Commelin (Apr 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770539):
Chris, but what does it do?

#### [Scott Morrison (Apr 27 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770580):
Or even better: `scheme` is an endofunctor of the category of types and equivalences.

#### [Johan Commelin (Apr 27 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770581):
Isn't that too general? You need some ring structures flying around, right?

#### [Scott Morrison (Apr 27 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770633):
I'm not sure what you mean, Johan. How would rings come into the picture? We're just doing abstract nonsense with types here.

#### [Chris Hughes (Apr 27 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770638):
If you quotient then you can rw. That's the idea. But it might be completely useless.

#### [Johan Commelin (Apr 27 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770639):
Scott, never mind, you are right

#### [Johan Commelin (Apr 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770686):
Ok, so then we want your proposed theorem to come for free. Does that make sense?

#### [Johan Commelin (Apr 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770688):
And then, if we have an actual equivalence between A and B, we get an equivalence between (scheme A) and (scheme B) for free

#### [Johan Commelin (Apr 27 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770702):
And I guess it comes for free for all endofunctors, and endofunctors compose

#### [Johan Commelin (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770708):
So we might need to mark lots of definitions with [endofunctor]

#### [Johan Commelin (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770751):
And maybe then we are happy?

#### [Scott Morrison (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770752):
So... which functions `F : Type × ... × Type → Type` extend to endofunctors of `Equiv` (the category of types and equivalences)?

#### [Kevin Buzzard (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770754):
```lean
import data.equiv 

theorem over_optimistic (F : Type → Type) (α β : Type) (H : equiv α β) :
equiv (F α) (F β) := sorry
```

#### [Scott Morrison (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770755):
Most things I can think of...

#### [Kenny Lau (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770758):
```quote
Is this totally disgusting?
```lean
structure isom (G H : Σ α : Type*, group α) :=
(f : G.1 ≃ H.1)
(to_fun_hom : @is_group_hom _ _ G.2 H.2 f.to_fun)
(inv_fun_hom : @is_group_hom _ _ H.2 G.2 f.inv_fun)

def is_isom (G H : Σ α : Type*, group α) := nonempty (isom G H)
```
```
the last parameter is redundant

#### [Kenny Lau (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770760):
proof: exercise for M1P2

#### [Kevin Buzzard (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770764):
Chris -- I know it can be done! My point is that I should not be wasting my time having to do it!

#### [Scott Morrison (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770830):
I need someone who actually groks type theory to give a counterexample to Kevin's `over_optimistic`. :-)

#### [Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770836):
So my `over_optimistic` question is a question for the CS people. Presumably that is not provable. I am very unfussed about you using any of Lean's axioms here. Is

#### [Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770840):
...yeah what Scott said

#### [Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770845):
The thing is that for the types I am most interested in when I am doing mathematics

#### [Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770847):
like groups and rings

#### [Kevin Buzzard (Apr 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770851):
the proof is "it's trivial"

#### [Scott Morrison (Apr 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770891):
(and lists and manifolds and braided monoidal categories)

#### [Kevin Buzzard (Apr 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770892):
exactly

#### [Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770897):
I have run into a ridiculous issue in my schemes code and Kenny has dug me out of a hole with 70 lines of code which no human should have to write

#### [Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770902):
and indeed no mention is made of the argument in the stacks project

#### [Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770903):
which is written in ZFC

#### [Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770905):
This is an area where translation to DTT seems hard

#### [Kevin Buzzard (Apr 27 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770949):
currently

#### [Kevin Buzzard (Apr 27 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770951):
I have some "canonically isomorphic" objects

#### [Kevin Buzzard (Apr 27 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770954):
and whilst I don't know what that means

#### [Johan Commelin (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770961):
Hmmmz where is `left_inverse` defined again?

#### [Scott Morrison (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770962):
I fear that someone is about to come along and say: "HoTT!"

#### [Johan Commelin (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770966):
Yes, I was about to do that

#### [Johan Commelin (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770974):
For 30 minutes I had the urge to say that I think this is *exactly* what Voevodsky tried to solve. His answer was HoTT

#### [Scott Morrison (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770976):
Voevodsky said things like: "the point is you can actually say what you mean by transport of structure"...

#### [Kenny Lau (Apr 27 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771023):
```quote
Hmmmz where is `left_inverse` defined again?
```
ctrl shift f

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771039):
I do know that from the fact that they are all canonically isomorphic that I can prove all the hypotheses in Kenny's theorem

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771040):
Kenny has taken the problem down one level

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771041):
there is a really weird part of the argument actually, which is worth mentioning here and is evidence to suggest that I am living in a dream world.

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771042):
I have B canonically isomorphic to B' (I have the maps)

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771043):
I have A canonically isomorphic to A' (in the sense that I have a structure which is an approximation to such a thing, and will do for now)

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771044):
but the proofs are going to be really tedious

#### [Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771048):
and I can prove that the diagram commutes

#### [Kevin Buzzard (Apr 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771087):
my chat is being garbled

#### [Scott Morrison (Apr 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771098):
(So which bits are by Kenny, and which by "Kevin"? :-)

#### [Kevin Buzzard (Apr 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771103):
but one of the arguments that it commutes is : ring hom x is the same as ring hom x' because they're both the unique ring hom

#### [Kevin Buzzard (Apr 27 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771104):
and similarly ring hom y = ring hom y'

#### [Kevin Buzzard (Apr 27 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771111):
and now we deduce that group hom x+y equals group hom x'+y'

#### [Kevin Buzzard (Apr 27 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771114):
not from the universal property itself, in some sense

#### [Kevin Buzzard (Apr 27 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771116):
well, from some shadow of the universal property applied to +

#### [Scott Morrison (Apr 27 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771226):
Does anyone know how things like `@[derive decidable_eq]` work?

#### [Scott Morrison (Apr 27 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771235):
Perhaps we can have `@[derive transportable]`, so when you write

#### [Scott Morrison (Apr 27 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771245):
````
@[derive transportable]
structure Scheme (a : Type) := ...
````

#### [Scott Morrison (Apr 27 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771290):
we automatically get an instance of `transportable Scheme`, which just means Scheme is functorial w.r.t equiv.

#### [Johan Commelin (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771300):
That was what I was hinting at with the [endofunctor] annotations

#### [Johan Commelin (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771303):
But: I don't know lean...

#### [Scott Morrison (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771306):
ah, I see!

#### [Scott Morrison (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771310):
Good suggestion. :-)

#### [Johan Commelin (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771311):
Well, your suggestion is clearly more fleshed out.

#### [Sebastian Ullrich (Apr 27 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771358):
@**Scott Morrison** Take a look at https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22

#### [Johan Commelin (Apr 27 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771419):
```quote
we automatically get an instance of `transportable Scheme`, which just means Scheme is functorial w.r.t equiv.
```
In other words, that `over_optimistic Scheme` is a theorem, right?

#### [Scott Morrison (Apr 27 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771433):
Well, even more than just `over_optimistic Scheme`.

#### [Scott Morrison (Apr 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771479):
We want to know that the `equiv`s  you get at the `Scheme` level compose in the same way they did on the original types.

#### [Kevin Buzzard (Apr 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771491):
So let's not jump the gun -- can you prove if A equiv B then a ring on A gives a ring on B?

#### [Kenny Lau (Apr 27 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771503):
in 70 lines?

#### [Kevin Buzzard (Apr 27 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771507):
:-)

#### [Kevin Buzzard (Apr 27 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771513):
Kenny I'm sure you could do it in ten

#### [Scott Morrison (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771516):
Sure we can do it on `ring`, or any given example. (Or rather: Kenny can :-)

#### [Kevin Buzzard (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771559):
I mean

#### [Scott Morrison (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771560):
but it seems rather likely that the computer can do it too, by looking at the structure fields, and working out where the parameter types appear, and plugging appropriate copies of the equivalence or its inverse everywhere.

#### [Kevin Buzzard (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771565):
right

#### [Scott Morrison (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771569):
For many simple types (list, ring, ...) this is certainly going to work.

#### [Kevin Buzzard (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771573):
I mean "prove it without ploughing through the axioms"

#### [Scott Morrison (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771584):
You mean ploughing through the axioms of "ring"?

#### [Kevin Buzzard (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771586):
yes, I want a one-line proof

#### [Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771624):
that if A equiv B then a ring structure on A gives one on B

#### [Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771629):
does that exist?

#### [Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771631):
Could it be a tactic?

#### [Scott Morrison (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771632):
No, I think in general there just isn't a one-line proof, that would work unchanged if your substituted ring for group.

#### [Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771633):
Is it already a theorem?

#### [Scott Morrison (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771634):
but yes, it can easily be a tactic

#### [Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771636):
and the tactic would sometimes fail?

#### [Scott Morrison (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771637):
and it can be one that's easy to use: just add @[derive transportable] in front of every structure.

#### [Scott Morrison (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771643):
and yes, conceivably it might sometime fail, but I don't see where yet

#### [Kevin Buzzard (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771644):
I have no understanding at all the moment anyone says `transportable`

#### [Scott Morrison (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771653):
(In fact, I'm really upset that I don't see where it might fail. I'll buy anyone a beer who explains a counterexample to Kevin's `over_optimistic` :-)

#### [Scott Morrison (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771654):
Sorry, I made up the word `transportable` just now.

#### [Kenny Lau (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771695):
heh?

#### [Kenny Lau (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771702):
I mean, f can send int to empty and nat to unit

#### [Scott Morrison (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771703):
@**Kevin Buzzard**, do you understand what I mean by "the category of types and equivalences"?

#### [Kenny Lau (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771706):
so int and nat are equivalent but empty and unit are not

#### [Kevin Buzzard (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771709):
not yet

#### [Kevin Buzzard (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771711):
Maybe I do understand

#### [Kevin Buzzard (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771712):
Are the objects all in one universe?

#### [Scott Morrison (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771719):
But Kenny, how would you actually construct such an `f` in Lean?

#### [Johan Commelin (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771721):
@**Scott Morrison** Just write down the definition of `structure transportable (F : Type* \to Type*)`

#### [Johan Commelin (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771725):
/me has never written a structure in Lean before, otherwise he would do it

#### [Johan Commelin (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771726):
Or should it be a class?

#### [Johan Commelin (Apr 27 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771767):
So that `@[derive]` will automagically create instances of that class

#### [Johan Commelin (Apr 27 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771784):
/me goes back to TPIL

#### [Scott Morrison (Apr 27 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771827):
````
class transportable (f : Type u → Type u) := 
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))
````

#### [Scott Morrison (Apr 27 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771839):
and I claim that @**Simon Hudon** knows how to implement @[derive transportable] for many type constructors. :-)

#### [Johan Commelin (Apr 27 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771889):
Yes, that would be very cool

#### [Scott Morrison (Apr 27 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771933):
@**Kevin Buzzard**, this is just saying we have a category which I'll call `Equiv`, whose objects are `Type u` for some universe `u`, and the homs between `\a` and `\b` are just `equiv \a \b`. Then a function  `f : Type u -> Type u` is "transportable" exactly if it extends to a functor `Equiv \to Equiv` (i.e. `f` is what that functor does on objects).

#### [Johan Commelin (Apr 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771950):
Can we have different universes?

#### [Scott Morrison (Apr 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771951):
sure.

#### [Johan Commelin (Apr 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771952):
In other words, `f` need not be "strictly endo"

#### [Scott Morrison (Apr 27 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771964):
(It's important that all the universes in classes are visible in the class parameters, but here they would be visible in the parameter `f : Type u -> Type v`.)

#### [Scott Morrison (Apr 27 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772036):
@**Kevin Buzzard**  --- I'm not at all sure if this is useful. It may be saying simple things in complicated ways, that don't actually solve your problems. But perhaps it does. (And if it does, I'm guessing automatically generating instances of `transportable` could be achieved within a few days (/weeks if Simon doesn't want to help :-)).

#### [Johan Commelin (Apr 27 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772091):
```quote
```lean
instance group_of_equiv [group α] (H : canonically_isomorphic α β) : group β := sorry
```
```
It would solve things like this, if I'm not mistaken

#### [Simon Hudon (Apr 27 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772095):
```quote
and I claim that @**Simon Hudon** knows how to implement @[derive transportable] for many type constructors. :-)
```
Do you have a proof of that?

#### [Johan Commelin (Apr 27 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772098):
Yes, you are working on it

#### [Scott Morrison (Apr 27 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772141):
:-)

#### [Johan Commelin (Apr 27 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772144):
And it seems that you get a beer if you can prove that you can't do it in one go...

#### [Scott Morrison (Apr 27 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772149):
(Sorry, I don't mean to say things like this to pressure you into doing things. Just to express my gratitude for all your recent help! No good deed goes unpunished...)

#### [Johan Commelin (Apr 27 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772211):
Learning how to write tactics and such is on my todo list

#### [Johan Commelin (Apr 27 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772214):
But I first need to get two papers out of the door...

#### [Simon Hudon (Apr 27 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772215):
(Haha! No worries! Can people hear us when we whisper in here?)

#### [Simon Hudon (Apr 27 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772225):
Yeah and writing tutorials about it is on mine

#### [Simon Hudon (Apr 27 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772269):
I can look into it. I still don't know much about `derive` but I need to understand it for `traversable`. I can kill two birds with one stone

#### [Chris Hughes (Apr 27 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772286):
Would it help to make everything isomorphic to a type a type class, and then prove things about the class of isomorphic types? Might be completely stupid.

#### [Johan Commelin (Apr 27 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772496):
Well, you loose track of different isomorphisms between the same to types

#### [Johan Commelin (Apr 27 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772500):
And that will create trouble down the road, I guess

#### [Simon Hudon (Apr 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773177):
Type classes are really better when instances are unique. Lean does not enforce that idea but conceptually, if the type class is not unique, the instance is an implicit argument everywhere but the exact choice of instance makes a big difference.

#### [Simon Hudon (Apr 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773186):
It's like you're omitting a central piece of information every time

#### [Johan Commelin (Apr 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773189):
But for Scott's proposal, that would be the case, right?

#### [Simon Hudon (Apr 27 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773404):
You mean the instance would be unique?

#### [Johan Commelin (Apr 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773683):
I think so

#### [Johan Commelin (Apr 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773687):
You derive an instance, right.

#### [Johan Commelin (Apr 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773694):
So there is only one of them. And people just shouldn't define additional instances

#### [Simon Hudon (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773760):
What if other instances could be useful?

#### [Simon Hudon (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773770):
Sorry, I'm kind of jumping in the middle here so I'm missing some context

#### [Johan Commelin (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773771):
Hmm, we only want to use the fact that the class is inhabited

#### [Johan Commelin (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773775):
Ok, so this is the thing

#### [Simon Hudon (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773782):
Is it meant to be used with type constructors like `list`?

#### [Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773783):
Say you have two types. `A` and `B`

#### [Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773790):
and you know that `A` is a group. You also know `equiv A B`

#### [Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773794):
Then we would like to know that `B` is also a group.

#### [Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773799):
And we want Lean to do this for us.

#### [Johan Commelin (Apr 27 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773858):
So, after lots of discussions, Scott came up with a strategy.

#### [Johan Commelin (Apr 27 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773864):
We define a class `transportable` (or some other name, but mathematicians know this fact as "transport of structure")

#### [Johan Commelin (Apr 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773868):
And we tag lots of definitions with `@[derive transportable]`

#### [Johan Commelin (Apr 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773873):
And then, MAGIC!

#### [Johan Commelin (Apr 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773886):
In particular, you can only derive transportable for things of type `Type u \to Type v`

#### [Simon Hudon (Apr 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773944):
In this case, that would be `group`, right?

#### [Johan Commelin (Apr 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773947):
And if `f` and `g` are two things that are `transportable`, then we want `(f,g)` to also be transportable, by some fact that we hope *you* can prove

#### [Johan Commelin (Apr 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773955):
Right, `group`, `ring` etc should be examples

#### [Simon Hudon (Apr 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773969):
I see, I see. That actually seems like a good use of classes

#### [Johan Commelin (Apr 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773978):
and if something is defined as a `structure`, hopefully we can also derive this from how its built.

#### [Simon Hudon (Apr 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773986):
I'll look into doing that. If I could have a use case, that would help a lot

#### [Johan Commelin (Apr 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774035):
And so we only need some really basic things where we actually *prove* that we have an instance. The rest is done by `derive` and *us* putting annotations in mathlib.

#### [Johan Commelin (Apr 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774046):
@**Scott Morrison** Is that a faithful representation of your ideas?

#### [Johan Commelin (Apr 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774143):
@**Simon Hudon** The use case is that Kevin is now facing a goal that would follow from this (and probably tomorrow he has another dozen). A mathematician would spend at most 3 words to "prove" such a fact. Kenny needed 70 lines to prove this particular goal of Kevin. But a variant of that goal can pop up any time.

#### [Scott Morrison (Apr 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774155):
Here's a mockup of what we want:
````
class canonical_equiv (α : Sort*) (β : Sort*) extends equiv α β.

class transportable (f : Type u → Type u) := 
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))

-- Finally a command like: `initialize_transport group` would create the next two declarations automagically:

def group.transportable : transportable group := sorry
instance group.transport {α β : Type u} [R : group α] [e : canonical_equiv α β] : group β := (@transportable.on_equiv group group.transportable _ _ e.to_equiv).to_fun R
````

#### [Scott Morrison (Apr 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774206):
The challenge is to implement the command `initialize_transport` (sounds like Star Trek! :-)

#### [Scott Morrison (Apr 27 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774254):
It will need to inspect its argument, which will be something like `ring` or `list`, and create an instance of `transportable ring` or `transportable list`, etc.

#### [Scott Morrison (Apr 27 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774269):
(i.e. fill in the `sorry` above)

#### [Scott Morrison (Apr 27 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774306):
The final step of `initialize_transport` is trivial: just emit the final instance declaration above.

#### [Johan Commelin (Apr 27 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774314):
Right, so `initialize_transport` (or `derive_transportable`) would look at `group` and say, oh, I know how to transport `mul` and `inv` and `one` from `A` to `B`

#### [Scott Morrison (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774315):
Exactly.

#### [Johan Commelin (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774323):
Because those are just functions... and someone told me how to do that

#### [Scott Morrison (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774325):
I don't have a strong sense of how hard that it. :-)

#### [Simon Hudon (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774327):
Nice idea :)

#### [Simon Hudon (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774336):
I think keep it as my treat today between writing sessions

#### [Scott Morrison (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774337):
But basically the thing you hand to `initialize_transport` will usually just be some inductive type

#### [Johan Commelin (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774338):
And then there are the axioms, and it should be able to transport their proof as well...

#### [Scott Morrison (Apr 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774379):
(e.g. a structure)

#### [Johan Commelin (Apr 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774383):
And now you want to "inductively" deduce that almost everything a mathematician like Kevin would define is an example of `transportable`

#### [Scott Morrison (Apr 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774407):
Yes: more advanced versions of `initialize_transport` will probably do some induction: notice that internal features have already been provided with instance of transportable, and make sure of that.

#### [Scott Morrison (Apr 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774420):
I should sleep, but I'll try to think of examples of wanting to do that while I sleep. :-)

#### [Simon Hudon (Apr 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774470):
Awesome! That sounds like sweet dreams

#### [Johan Commelin (Apr 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775365):
Here are some more basics. But I think you already got the idea.
```lean
import data.equiv

universes u v w

class transportable (f : Type u → Type v) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))

-- Our goal is an automagic proof of the following
theorem group.transportable : transportable group := sorry

-- These we might need to define and prove by hand
def Const : Type u → Type v := λ α, punit
def Fun : Type u → Type v → Type (max u v) := λ α β, α → β
def Prod : Type u → Type v → Type (max u v) := λ α β, α × β
def Swap : Type u → Type v → Type (max u v) := λ α β, β × α

lemma Const.transportable (α : Type u) : (transportable Const) := sorry
lemma Fun.transportable (α : Type u) : (transportable (Fun α)) := sorry
lemma Prod.transportable (α : Type u) : (transportable (Prod α)) := sorry
lemma Swap.transportable (α : Type u) : (transportable (Swap α)) := sorry


-- And then we can define
def Hom1 (α : Type u) : Type v → Type (max u v) := λ β, α → β
def Hom2 (β : Type v) : Type u → Type (max u v) := λ α, α → β
def Aut : Type u → Type u := λ α, α → α

-- And hopefully automagically derive
lemma Hom1.transportable (α : Type u) : (transportable (Hom1 α)) := sorry
lemma Hom2.transportable (β : Type v) : (transportable (Hom1 β)) := sorry
lemma Aut.transportable (α : Type u) : (transportable Aut) := sorry

-- If we have all these in place...
-- A bit of magic might actually be able to derive `group.transportable` on line 11.
-- After all, a group just is a type plus some functions... and we can now transport functions.
```

#### [Johan Commelin (Apr 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775387):
Aah, and to prove the axioms for the transported functions, we need to be able to transport propositions

#### [Simon Hudon (Apr 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775647):
Thanks! Transporting propositions shouldn't be too hard. I have a few ideas on how to do it

#### [Simon Hudon (Apr 27 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775719):
With my recent popularity, maybe I should cash in on this new market: [IMG_8067.jpeg](/user_uploads/3121/boyZ4T9BeLmq-lWnSs0tiqdb/IMG_8067.jpeg)

#### [Kevin Buzzard (Apr 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779148):
I have proved the fundamental theorem of `has_mul`

#### [Kevin Buzzard (Apr 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779150):
What a great way to spend a day.

#### [Kenny Lau (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779199):
what is that theorem?

#### [Kevin Buzzard (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779205):
```lean
universe zfc_u 
variables {α β : Type zfc_u}

-- ideas around the concept of α being canonically isomorphic to β

namespace zfc 

-- mod of equiv so I can save typing
structure equiv' (α : Type zfc_u) (β : Type zfc_u) :=
(i    : α → β)
(j    : β → α)
(ij : ∀ (x : α), j (i x) = x)
(ji  : ∀ (y : β), i (j y) = y)

-- it's equiv to equiv, it is absolutely fundamental for the notion of canonical isomorphism, and I like
-- the notation better because it gets everywhere.

--#print has_mul
--@[class]
--structure has_mul : Type u → Type u
--fields:
--has_mul.mul : Π {α : Type u} [c : has_mul α], α → α → α

-- Fundamental theorem of has_mul

--#print prefix has_mul -- stuff
--set_option pp.notation false
definition equiv_mul {α β : Type zfc_u} : equiv' α β → equiv' (has_mul α) (has_mul β) := λ E,
{ i :=  λ αmul,⟨λ b1 b2, E.i (@has_mul.mul α αmul (E.j b1) (E.j b2))⟩,
  j := λ βmul,⟨λ a1 a2, E.j (@has_mul.mul β βmul (E.i a1) (E.i a2))⟩, -- didn't I just write that?
                                                                      -- should we introduce E-dual?
  ij := λ f, begin 
    cases f, -- aargh why do I struggle
    suffices :  (λ (a1 a2 : α), E.j (E.i (f (E.j (E.i a1)) (E.j (E.i a2))))) = (λ a1 a2, f a1 a2),
      by rw this,
    funext,
    simp [E.ij,E.ji], -- got there in the end
  end,
  ji := -- I can't even do this in term mode so I just copy out the entire tactic mode proof again.
 λ g, begin 
    cases g, -- aargh why do I struggle
    suffices :  (λ (b1 b2 : β), E.i (E.j (g (E.i (E.j b1)) (E.i (E.j b2))))) = (λ b1 b2, g b1 b2),
      by rw this,
    funext,
    simp [E.ij,E.ji], -- got there in the end
  end, -- didn't I just write that?
}

```

#### [Kevin Buzzard (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779217):
it is `equiv_mul`

#### [Kevin Buzzard (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779219):
but it would be happily renamed

#### [Kenny Lau (Apr 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779251):
that's quite interesting

#### [Kevin Buzzard (Apr 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779255):
@**Simon Hudon** Can you see that I repeat every line of code twice?

#### [Kevin Buzzard (Apr 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779259):
I have this vague idea that this is not best practice

#### [Simon Hudon (Apr 27 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779350):
No, you're right. I think this should and could be derived automatically.

#### [Kevin Buzzard (Apr 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779523):
```quote
Would it help to make everything isomorphic to a type a type class, and then prove things about the class of isomorphic types? Might be completely stupid.
```
I am just catching up with chat. I've been trying to work out some of these proofs by hand.

#### [Kevin Buzzard (Apr 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779529):
That sounds like a really cool idea though

#### [Kevin Buzzard (Apr 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779575):
By the way -- the reason I did `has_mul` is that there is another type class which I am targetting.

#### [Kenny Lau (Apr 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779576):
```quote
```quote
Would it help to make everything isomorphic to a type a type class, and then prove things about the class of isomorphic types? Might be completely stupid.
```
I am just catching up with chat. I've been trying to work out some of these proofs by hand.
```
it's called cardinal

#### [Kevin Buzzard (Apr 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779586):
:-)

#### [Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779603):
Is `cardinal` a far more useful object than I had realised?

#### [Kenny Lau (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779608):
no

#### [Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779610):
:-)

#### [Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779618):
Kenny can you prove the fundamental theorem of ring?

#### [Kenny Lau (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779624):
I can, but I won't

#### [Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779628):
how many lines would it take you

#### [Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779631):
the fundamental theorem of ring is a trivial result

#### [Kevin Buzzard (Apr 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779653):
I wanna build a tactic :-)

#### [Kenny Lau (Apr 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779672):
a ring has many structures, you know

#### [Kevin Buzzard (Apr 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779687):
yeah and you solve them all with the same tactic

#### [Kevin Buzzard (Apr 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780187):
rofl

#### [Kenny Lau (Apr 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780189):
```lean
import data.equiv

def transport_ring {α β : Type*} [ring α] (f : α ≃ β) : ring β :=
{ add := λ x y, f (f.symm x + f.symm y),
  zero := f 0,
  neg := λ x, f (-f.symm x),
  mul := λ x y, f (f.symm x * f.symm y),
  one := f 1,
  add_assoc := λ x y z, by simp; from add_assoc _ _ _,
  zero_add := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (zero_add _),
  add_zero := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (add_zero _),
  add_left_neg := λ x, by simp; from add_left_neg _,
  add_comm := λ x y, by simp; from add_comm _ _,
  mul_assoc := λ x y z, by simp; from mul_assoc _ _ _,
  one_mul := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (one_mul _),
  mul_one := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (mul_one _),
  left_distrib := λ x y z, by simp; from left_distrib _ _ _,
  right_distrib := λ x y z, by simp; from right_distrib _ _ _, }
```

#### [Kevin Buzzard (Apr 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780193):
I have proved the fundamental theorem of mul

#### [Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780198):
and now I have to prove the fundamental theorem of add

#### [Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780201):
why would I do that

#### [Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780202):
but add is canonically isomorphic to mul

#### [Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780203):
I just said I won't

#### [Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780204):
I am doing it

#### [Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780209):
done 10 mins

#### [Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780212):
I just do a regular expression substitution

#### [Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780213):
and I have the fundamental theorem of add

#### [Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780215):
you win

#### [Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780217):
but I would rather have a tactic

#### [Kenny Lau (Apr 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780310):
```lean
import data.equiv
def why_would_one {α} : has_add α ≃ has_mul α :=
{ to_fun := λ ⟨f⟩, ⟨f⟩,
  inv_fun := λ ⟨f⟩, ⟨f⟩,
  left_inv := λ ⟨f⟩, rfl,
  right_inv := λ ⟨f⟩, rfl }
```

#### [Patrick Massot (Apr 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780411):
It reminds me of the situation with https://github.com/PatrickMassot/lean-differential-topology/commit/f47348abf8515e23bd485683d8b351c7fd89c70f#diff-bbdfb4d2f4b405102cb35c772afdd2cc which was automated into https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L56

#### [Patrick Massot (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780413):
So I'm pretty optimistic there will be a tactic

#### [Patrick Massot (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780457):
What would be even better would be Simon getting tired of writing our tactics and writing tactic writing tutorials instead

#### [Kenny Lau (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780460):
aha

#### [Kenny Lau (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780466):
Give a man a fish, and you feed him for a day; show him how to catch fish, and you feed him for a lifetime.

#### [Kevin Buzzard (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780685):
I made an instance

#### [Kevin Buzzard (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780692):
```lean
definition mul_is_add {α : Type zfc_u} : equiv' (has_mul α) (has_add α) :=
{ i := λ ⟨mul⟩,⟨mul⟩,
  j := λ ⟨mul⟩,⟨mul⟩,
  ij := λ ⟨x⟩,begin -- *sigh*
    constructor,
  end ,
  ji := λ ⟨z⟩, by constructor
}

```

#### [Kenny Lau (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780697):
but that's what I just did

#### [Kevin Buzzard (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780700):
I am behind

#### [Kevin Buzzard (Apr 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780739):
I am working it all out myself

#### [Kenny Lau (Apr 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780745):
nice

#### [Sean Leather (Apr 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780753):
```quote
Give a man a fish, and you feed him for a day; show him how to catch fish, and you feed him for a lifetime.
```
Unless there is no body of water nearby...

#### [Kevin Buzzard (Apr 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780788):
OK Kenny, well done on ring. My next challenge for you is `topological_field`

#### [Kenny Lau (Apr 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780794):
nope.

#### [Kevin Buzzard (Apr 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780796):
and it's a challenge to Simon as well

#### [Kevin Buzzard (Apr 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780910):
```lean
import data.equiv

def transport_ring {α β : Type} [topological_field α] (f : α ≃ β) : topological_field β := sorry
```

#### [Kevin Buzzard (Apr 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780912):
Who will win out of man and machine

#### [Kevin Buzzard (Apr 27 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780962):
and I am sitting here in ZFC and remarking that it is trivial

#### [Kevin Buzzard (Apr 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781022):
Aah Kenny I just saw your has_mul

#### [Kevin Buzzard (Apr 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781063):
well I proved the fundamental theorem of has_mul before

#### [Kevin Buzzard (Apr 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781069):
so can you now deduce the fundamental theorem of has_add?

#### [Andrew Ashworth (Apr 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781632):
did you take a look at the `transfer` paper I linked way back? That's how in core lean they move proofs between `int` and `(a , b) : nat * nat`, which (and maybe I'm not understanding the details here very well) is your problem of transporting proofs between isomorphic types?

#### [Andrew Ashworth (Apr 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781815):
also as far as I can tell from my (limited) experience with hott; isomorphisms are just as hard to deal with as they are in dtt, there's no magic sauce rewriting. you can try reading https://github.com/cmu-phil/Spectral, which is a lean repository about the Serre spectral sequence

#### [Andrew Ashworth (Apr 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781820):
I have no idea what a spectral sequence might be, but you can see that dealing with isomorphisms is no easier from reading the source code...

#### [Kevin Buzzard (Apr 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781905):
Kenny I thought of a much easier challenge for you

#### [Kevin Buzzard (Apr 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781906):
https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism

#### [Kevin Buzzard (Apr 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781909):
much less boring than topological fields

#### [Kevin Buzzard (Apr 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781965):
can you define `mul_to_add` at the bottom?

#### [Mario Carneiro (Apr 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781997):
The `over_optimistic` theorem is a weak form of univalence. To see how they are related, just plug in `eq A` for the function `F`; then `A = A` is equiv to `A = B` and hence the latter is also inhabited. It is currently an open question whether this theorem is consistent with lean, but I believe it to be. (It is inconsistent with VM evaluation though.)

The second part of this conversation has developed a plan for showing that even if you can't prove that all functions are functorial, you might be able to show that all definable functions are functorial by working in the metatheory (i.e. giving a tactic that produces the required term). It is not contradictory that it might be possible that all lean definable terms are functorial in an appropriate sense even if you can't prove it for *all* terms, as the internal theory understands the quantifier. So this is not a "proof or counterexample" kind of question.

This topic is usually known in the type theory literature as "parametricity", and it is on my todo list for my paper.

#### [Kevin Buzzard (Apr 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782104):
`definition mul_to_add {α β : Type} : equiv' α β → equiv' (has_add α) (has_add β) := sorry`

#### [Johan Commelin (Apr 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782105):
Right, so we are kind of proposing a pragmatic approach to HoTT and univalence

#### [Johan Commelin (Apr 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782114):
Kevin, did you see Scott's proposal for a class + decorators?

#### [Johan Commelin (Apr 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782122):
I think you won't need to prove any of these "fundamental theorems" anymore, once we get that implemented

#### [Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782181):
So in layman's terms, when can I expect a three-line proof of `exact_sequence A B C -> exact_sequence A' B' C'` which is just three rewrites?

#### [Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782183):
I would be very happy to work on such a thing

#### [Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782184):
because I really want it :-)

#### [Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782188):
Can I incorporate Scott's proposal into my proofs somehow?

#### [Kevin Buzzard (Apr 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782195):
Or is Scott's code purely for someone who is writing a tactic?

#### [Kevin Buzzard (Apr 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782232):
I just find these quite fun and satisfying to do by hand, and I feel like if I try to get really good at them

#### [Kevin Buzzard (Apr 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782238):
then I might understand better how to write a tactic which is doing some of the job for me

#### [Kevin Buzzard (Apr 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782248):
I would be very happy if anyone wanted to comment on https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonically_isomorphic.lean

#### [Kevin Buzzard (Apr 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782252):
I would really like to get some canonical proofs.

#### [Kevin Buzzard (Apr 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782255):
Kenny can you beat any of mine?

#### [Johan Commelin (Apr 27 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782394):
@**Kevin Buzzard** No, we can't use Scott's proposal yet. The idea is that someone proves inductively the *universal* fundamental theorem for structures (or probably: inductive types). And then we only need to prove the fundamental theorem for some basic types and we will get all the others for free.

#### [Johan Commelin (Apr 27 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782443):
And it seems like Simon thought this was interesting, and might try to implement it pretty soon.

#### [Kevin Buzzard (Apr 27 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782446):
Can you formalise what you think the universal fundamental theorem is?

#### [Johan Commelin (Apr 27 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782448):
Hmm, I don't know enough lean yet.

#### [Johan Commelin (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782453):
Actually, no.

#### [Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782457):
Can @**Scott Morrison** or @**Mario Carneiro** ?

#### [Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782461):
Is there some kind of conjecture we can make?

#### [Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782462):
and give a constructive proof?

#### [Johan Commelin (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782464):
@**Kevin Buzzard** The idea is that we "tag" every structure for which we want to prove it. And then actually Lean does it itself.

#### [Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782466):
so like the type class inference machinery?

#### [Johan Commelin (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782467):
This is what the `@[derive transportable]` should do

#### [Kevin Buzzard (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782510):
so can one formulate some theorem which should be true for every...something...which is tagged with this tag?

#### [Johan Commelin (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782511):
Lean will see that you are defining some `structure` and for all its fields it already knows that they are transportable. And thus it proves a theorem for the new structure as well.

#### [Kevin Buzzard (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782512):
In Lean, I mean?

#### [Kevin Buzzard (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782514):
What will the theorem be?

#### [Johan Commelin (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782516):
Yes. That theorem is your `over_optimistic`

#### [Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782521):
I see.

#### [Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782526):
And we should be able to prove it for all F tagged with some tag

#### [Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782527):
...automatically?

#### [Johan Commelin (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782528):
Well, not *we* but even Lean

#### [Johan Commelin (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782529):
After we taught it the ultimate basics.

#### [Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782530):
and this would be...a tactic?

#### [Johan Commelin (Apr 27 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782572):
@**Kevin Buzzard** Again, I'm not a meta-expert. But basically, it will be an automatically applied tactic.

#### [Johan Commelin (Apr 27 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782573):
This is what `derive` seems to do...

#### [Johan Commelin (Apr 27 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782580):
But, I now I'm in waters that I don't really know

#### [Kevin Buzzard (Apr 27 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782587):
I have been fretting over what canonical isomorphism means for many years now

#### [Johan Commelin (Apr 27 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782596):
See also my snippet:
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365

#### [Kevin Buzzard (Apr 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782646):
https://mathoverflow.net/a/19663

#### [Kenny Lau (Apr 27 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782704):
```quote
Kenny can you beat any of mine?
```
https://github.com/kckennylau/Lean/blob/master/canonically_isomorphic.lean

#### [Kevin Buzzard (Apr 27 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782724):
So is this `transportable` class some completely well-known and well-studied class in type theory?

#### [Johan Commelin (Apr 27 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782965):
I think at least in *homotopy* type theory

#### [Johan Commelin (Apr 27 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783111):
I like your MO answer

#### [Kevin Buzzard (Apr 27 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783470):
How do I reduce this goal

```lean
⊢ {to_fun := A1,
     inv_fun := A2,
     left_inv := 3,
     right_inv := A4} =
    {to_fun := B1, inv_fun := B2, left_inv := B3, right_inv := B4}
```
into the four goals `A1=B1`, `A2=B2` etc?

#### [Kenny Lau (Apr 27 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783473):
`congr`

#### [Patrick Massot (Apr 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783548):
```quote
So in layman's terms, when can I expect a three-line proof of `exact_sequence A B C -> exact_sequence A' B' C'` which is just three rewrites?
```
What I'm going to write is not what you are hoping for, and unrelated to the big dreams of general transport of structures

#### [Patrick Massot (Apr 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783550):
But I still think it's useful

#### [Patrick Massot (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783589):
I spend most of my Lean time being frustrated by obvious statements, and then see Mario prove them

#### [Kenny Lau (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783597):
```quote
How do I reduce this goal

```lean
⊢ {to_fun := A1,
     inv_fun := A2,
     left_inv := 3,
     right_inv := A4} =
    {to_fun := B1, inv_fun := B2, left_inv := B3, right_inv := B4}
```
into the four goals `A1=B1`, `A2=B2` etc?
```
oh and that should be part of your interface

#### [Patrick Massot (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783603):
In my experience, what happens is my mind refuses to decompose the statement and/or think about the proper setup

#### [Patrick Massot (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783609):
Then Mario decomposes the problem into three or four lemmas and each of them is a one-liner

#### [Patrick Massot (Apr 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783626):
So let me try a decomposition in your case

#### [Patrick Massot (Apr 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783679):
I would define sequences of rings and maps between them (assuming we don't have an abelian categories lib right now).

#### [Patrick Massot (Apr 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783698):
And the corresponding maps, ie sequences of maps with all squares commuting

#### [Patrick Massot (Apr 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783713):
Then define complexes as sequences where two consecutive maps compose to zero

#### [Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783772):
prove isomorphic sequences have conjugated maps

#### [Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783774):
deduce a sequence isomorphic to a complex is a complex

#### [Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783775):
define homology of complexes

#### [Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783782):
define exact sequences as acyclic complexes

#### [Patrick Massot (Apr 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783788):
prove isomorphic complexes have isomorphic homology

#### [Patrick Massot (Apr 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783798):
deduce your lemma (and the version with n rings instead of only 3)

#### [Patrick Massot (Apr 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783804):
I'm not saying the total number of lines will be 3

#### [Patrick Massot (Apr 27 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783846):
But all those definitions and lemmas will be needed very soon anyway

#### [Patrick Massot (Apr 27 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783853):
(with more definitions of course, especially homotopy equivalences and quasi-iso)

#### [Patrick Massot (Apr 27 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783920):
You also want a lemma relating my definition of exact sequence to the direct one

#### [Patrick Massot (Apr 27 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783929):
So, the proof of your lemma wouldn't by three `rw` by three `apply` (or one `simp` maybe)

#### [Kenny Lau (Apr 27 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783955):
```lean
theorem equiv'.ext {α β : Type zfc_u} :
  ∀ {e₁ e₂ : equiv' α β} (H : ∀ x, e₁.i x = e₂.i x), e₁ = e₂
| ⟨i₁, j₁, ij₁, ji₁⟩ ⟨i₂, j₂, ij₂, ji₂⟩ H :=
begin
  congr, { funext, apply H },
  simp at H,
  funext x,
  rw [← ji₁ x, ij₁, H, ij₂]
end
```

#### [Kenny Lau (Apr 27 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783964):
@**Kevin Buzzard**

#### [Johan Commelin (Apr 27 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784003):
@**Kenny Lau** Sweet.

#### [Kevin Buzzard (Apr 27 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784017):
I did Level 1 of Johan's level set!

#### [Kenny Lau (Apr 27 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784020):
what level set?

#### [Kevin Buzzard (Apr 27 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784021):
```lean
-- level 1
lemma Const.transportable : (transportable Const) := { 
  on_equiv := λ α β H,⟨λ _,punit.star,λ _,punit.star,λ α,begin cases α,simp end,λ α,begin cases α,simp end⟩,
  --I was repeating myself in that last line.
  on_refl := λ α,begin 
  congr,
  { funext s,cases s,refl},
  { funext s,cases s,refl} -- I just wrote this
  end,
  on_trans := λ α β γ Hαβ Hβγ,by congr
  }  
```

#### [Johan Commelin (Apr 27 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784073):
@**Kenny Lau** 
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365

#### [Kevin Buzzard (Apr 27 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784079):
Patrick I think your proof is very different to Kenny's

#### [Kevin Buzzard (Apr 27 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784083):
and I like it much better

#### [Kenny Lau (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784090):
what is his proof?

#### [Kevin Buzzard (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784095):
and I think that perhaps when Mario said earlier that Kenny should "work on his long game", maybe he meant thinking like this

#### [Johan Commelin (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784104):
Well, I think we ultimately should have Patrick's idea and Scott's proposal work together.

#### [Kevin Buzzard (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784107):
Kenny

#### [Kevin Buzzard (Apr 27 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784109):
I put the levels up on xena

#### [Johan Commelin (Apr 27 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784161):
In other words, a whole series of definitions, that are all tagged with `@[derive transport_of_structure]`

#### [Johan Commelin (Apr 27 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784167):
And then we get Kevin's requested lemma for free

#### [Kevin Buzzard (Apr 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784240):
@**Kenny Lau** https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism

#### [Kevin Buzzard (Apr 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784241):
I am one ahead of you

#### [Kenny Lau (Apr 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784242):
thx

#### [Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784245):
on the Johan challenge

#### [Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784262):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean

#### [Kenny Lau (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784265):
and then `derive` will work?

#### [Kenny Lau (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784267):
How does `derive` work?

#### [Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784271):
we have to work at the start

#### [Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784272):
and then the machines take over

#### [Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784313):
and then I can have a three line proof of the three lemma

#### [Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784322):
saying that if A -> B -> C is exact then A' -> B' -> C' is exact

#### [Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784326):
all I have to do is prove some diagrams commute

#### [Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784328):
and say that some things are canonically isomorphic

#### [Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784330):
which is obvious in ZFC

#### [Kevin Buzzard (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784346):
Mathematicians will not use this software unless they can do stuff that they find easy in maths, in Lean

#### [Kevin Buzzard (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784350):
and I thought that I enjoyed doing algebraic geometry in Lean

#### [Kevin Buzzard (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784351):
until I ran into this issue

#### [Kenny Lau (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784352):
I mean, the mechanism behind `@[derive __]`

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784397):
Either Simon will write it

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784399):
or Scott will write it

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784400):
or I will have to write it

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784401):
with their help

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784403):
or you can write it

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784404):
or Chris

#### [Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784414):
Maybe it would be trivial for Mario, I have no idea

#### [Kenny Lau (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784416):
you're this close from listing everyone's name

#### [Kenny Lau (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784419):
this close.

#### [Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784424):
but I can certainly believe that the more easy levels we solve by hand

#### [Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784430):
the easier it will be to write the tactic

#### [Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784434):
and I really like solving these levels

#### [Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784438):
they're even better then Zelda

#### [Kenny Lau (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784445):
```lean
class transportable (f : Type u → Type v) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))
```

#### [Kenny Lau (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784446):
functor :D

#### [Kenny Lau (Apr 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784510):
why no use symbol?

#### [Johan Commelin (Apr 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784511):
@**Kenny Lau** https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22
and also L44-L45

#### [Johan Commelin (Apr 27 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784584):
@**Kenny Lau** It is indeed a functor, but only on equivalences. That is how Scott first defined it (informally). But I guess we might not want this def'n to depend on a category lib. The category lib probably wants to depend on transport of structure...

#### [Johan Commelin (Apr 27 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784596):
By the way, I suggest a name for the tactic that proves transport of structure: `chuck_norris`

#### [Kevin Buzzard (Apr 27 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784599):
Kenny feel free to make the file a lot better

#### [Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784606):
+1 for `chuck_norris`

#### [Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784607):
but I would be happy to hear alternatives

#### [Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784613):
One of the reasons people go on about `sledgehammer`

#### [Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784616):
is that it has a really cool name

#### [Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784617):
and `crush` too

#### [Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784621):
I would vote for any Pokemon move name

#### [Kenny Lau (Apr 27 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784755):
```lean
lemma Const.transportable : (transportable Const) :=
{ on_equiv := λ α β e, ⟨λ _, punit.star, λ _, punit.star, λ ⟨⟩, rfl , λ ⟨⟩, rfl⟩,
  on_refl  := λ α, equiv.ext _ _ $ λ ⟨⟩, rfl,
  on_trans := λ α β γ e1 e2, equiv.ext _ _ $ λ ⟨⟩, rfl }

lemma Fun.transportable (α : Type u) : (transportable (Fun α)) :=
{ on_equiv := λ β γ e, ⟨λ f x, e (f x), λ f x, e.symm (f x),
    λ f, funext $ λ x, e.inverse_apply_apply (f x),
    λ f, funext $ λ x, e.apply_inverse_apply (f x)⟩,
  on_refl  := λ β, equiv.ext _ _ $ λ f, rfl,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ f, rfl }
```

#### [Kenny Lau (Apr 27 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785025):
```lean
theorem prod.ext' {α β : Type*} {p q : α × β} (H1 : p.1 = q.1) (H2 : p.2 = q.2) : p = q :=
prod.ext.2 ⟨H1, H2⟩

lemma Prod.transportable (α : Type u) : (transportable (Prod α)) :=
{ on_equiv := λ β γ e, ⟨λ x, (x.1, e x.2), λ x, (x.1, e.symm x.2),
    λ f, prod.ext' rfl $ e.inverse_apply_apply f.2,
    λ f, prod.ext' rfl $ e.apply_inverse_apply f.2⟩,
  on_refl  := λ β, equiv.ext _ _ $ λ x, prod.ext' rfl rfl,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ f, rfl }

lemma Swap.transportable (α : Type u) : (transportable (Swap α)) :=
{ on_equiv := λ β γ e, ⟨λ x, (e x.1, x.2), λ x, (e.symm x.1, x.2),
    λ f, prod.ext' (e.inverse_apply_apply f.1) rfl,
    λ f, prod.ext' (e.apply_inverse_apply f.1) rfl⟩,
  on_refl  := λ β, equiv.ext _ _ $ λ x, prod.ext' rfl rfl,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ f, rfl }
```

#### [Kenny Lau (Apr 27 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785027):
@**Kevin Buzzard**

#### [Kenny Lau (Apr 27 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785091):
```lean
lemma Hom1.transportable (α : Type u) : (transportable (Hom1 α)) :=
Fun.transportable α
```
?

#### [Kevin Buzzard (Apr 27 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785192):
```lean
-- level 2
lemma Fun.transportable (α : Type u) : (transportable (Fun α)) := {
    on_equiv := λ β γ Hβγ,⟨
        λ f a,Hβγ.to_fun (f a),
        λ f a,Hβγ.inv_fun (f a),
        λ f,by funext a;exact Hβγ.left_inv (f a),
        λ g,by funext a;exact Hβγ.right_inv (g a) 
    ⟩,
    on_refl := λ β,by congr,
    on_trans := λ β γ δ Hβγ Hγδ,by congr
}
```

#### [Kevin Buzzard (Apr 27 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785196):
I see you caught up :-)

#### [Kenny Lau (Apr 27 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785199):
I'm faster :P

#### [Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785256):
Kenny you repeat yourself in your code

#### [Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785259):
you say most things twice

#### [Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785261):
this means it is bad code, right?

#### [Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785263):
Can you write better code?

#### [Kenny Lau (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785264):
let's see whether you can avoid repeating yourself lol

#### [Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785268):
You know the dual of an equiv is an equiv

#### [Kevin Buzzard (Apr 27 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785278):
I repeat myself IRL

#### [Kevin Buzzard (Apr 27 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785354):
```quote
I'm faster :P
```
Yes but you're working on my conjecture ;-)

#### [Kenny Lau (Apr 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785534):
```lean
lemma Hom1.transportable (α : Type u) : (transportable (Hom1 α)) :=
Fun.transportable α

lemma Hom2.transportable (β : Type v) : (transportable (Hom2 β)) :=
{ on_equiv := λ α γ e, ⟨λ f x, f (e.symm x), λ f x, f (e x),
    λ f, funext $ λ x, congr_arg f $ e.inverse_apply_apply x,
    λ f, funext $ λ x, congr_arg f $ e.apply_inverse_apply x⟩,
  on_refl  := λ β, equiv.ext _ _ $ λ f, rfl,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ f, rfl }

lemma Aut.transportable : (transportable Aut) :=
{ on_equiv := λ α β e, ⟨λ f x, e (f (e.symm x)), λ f x, e.symm (f (e x)),
    λ f, funext $ λ x, by simp,
    λ f, funext $ λ x, by simp⟩,
  on_refl  := λ α, equiv.ext _ _ $ λ f, funext $ λ x, rfl,
  on_trans := λ α β γ e1 e2, equiv.ext _ _ $ λ f, funext $ λ x, rfl, }
```

#### [Kevin Buzzard (Apr 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785536):
Kenny my proof of `Const.transportable.on_trans` is better than yours

#### [Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785577):
@**Kevin Buzzard** all done. now I can shorten my proof lol

#### [Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785585):
well

#### [Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785587):
`on_trans := λ α β γ Hαβ Hβγ,by congr`

#### [Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785589):
I like term mode :P

#### [Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785592):
don't you lie to me

#### [Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785593):
you like golf

#### [Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785595):
lol

#### [Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785599):
:-)

#### [Kevin Buzzard (Apr 27 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785704):
in `Fun_transportable.on_equiv` you have `e.inverse_apply_apply (f x)`

#### [Kevin Buzzard (Apr 27 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785712):
and I have `e.left_inv (f a)`

#### [Kevin Buzzard (Apr 27 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785733):
which is better?

#### [Kenny Lau (Apr 27 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785854):
they say `e.symm` and etc are more idiomatic

#### [Kenny Lau (Apr 27 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785871):
because they are actually simp lemmas

#### [Kenny Lau (Apr 27 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785877):
so I can just replace it with `by simp` and outgolf you

#### [Kevin Buzzard (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785886):
So I should switch to all this `apply_inverse_apply` stuff?

#### [Kenny Lau (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785929):
no, you should use `simp`

#### [Kevin Buzzard (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785930):
And you use `coe_to_fun` to get the function directly?

#### [Kenny Lau (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785934):
yes

#### [Kevin Buzzard (Apr 27 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786016):
OK I pushed

#### [Kevin Buzzard (Apr 27 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786025):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean

#### [Kevin Buzzard (Apr 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786034):
has levels 1 and 2 solved

#### [Kevin Buzzard (Apr 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786043):
and I'll now look at your other work Kenny

#### [Kevin Buzzard (Apr 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786048):
Let me know if you think the solutions can be improved @**Kenny Lau**

#### [Kenny Lau (Apr 27 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786270):
```lean
import data.equiv
#check equiv.refl 

universes u v w

class transportable (f : Type u → Type v) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))

-- Our goal is an automagic proof of the following (level 20)
theorem group.transportable : transportable group := sorry

-- These we might need to define and prove by hand
def Const : Type u → Type v := λ α, punit
def Fun : Type u → Type v → Type (max u v) := λ α β, α → β
def Prod : Type u → Type v → Type (max u v) := λ α β, α × β
def Swap : Type u → Type v → Type (max u v) := λ α β, β × α

-- level 1
lemma Const.transportable : (transportable Const) :=
{ on_equiv := λ α β e, equiv.punit_equiv_punit,
  on_refl  := λ α, equiv.ext _ _ $ λ ⟨⟩, rfl,
  on_trans := λ α β γ e1 e2, equiv.ext _ _ $ λ ⟨⟩, rfl }

lemma Fun.transportable (α : Type u) : (transportable (Fun α)) :=
{ on_equiv := λ β γ e, equiv.arrow_congr (equiv.refl α) e,
  on_refl  := λ β, equiv.ext _ _ $ λ f, rfl,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ f, funext $ λ x,
    by cases e1; cases e2; refl }

theorem prod.ext' {α β : Type*} {p q : α × β} (H1 : p.1 = q.1) (H2 : p.2 = q.2) : p = q :=
prod.ext.2 ⟨H1, H2⟩

lemma Prod.transportable (α : Type u) : (transportable (Prod α)) :=
{ on_equiv := λ β γ e, equiv.prod_congr (equiv.refl α) e,
  on_refl  := λ β, equiv.ext _ _ $ λ ⟨x, y⟩, by simp,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ ⟨x, y⟩, by simp }

lemma Swap.transportable (α : Type u) : (transportable (Swap α)) :=
{ on_equiv := λ β γ e, equiv.prod_congr e (equiv.refl α),
  on_refl  := λ β, equiv.ext _ _ $ λ ⟨x, y⟩, by simp,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ ⟨x, y⟩, by simp }

-- And then we can define
def Hom1 (α : Type u) : Type v → Type (max u v) := λ β, α → β
def Hom2 (β : Type v) : Type u → Type (max u v) := λ α, α → β
def Aut : Type u → Type u := λ α, α → α

-- And hopefully automagically derive
lemma Hom1.transportable (α : Type u) : (transportable (Hom1 α)) :=
Fun.transportable α

lemma Hom2.transportable (β : Type v) : (transportable (Hom2 β)) :=
{ on_equiv := λ α γ e, equiv.arrow_congr e (equiv.refl β),
  on_refl  := λ β, equiv.ext _ _ $ λ f, rfl,
  on_trans := λ β γ δ e1 e2, equiv.ext _ _ $ λ f, funext $ λ x,
    by cases e1; cases e2; refl }

lemma Aut.transportable : (transportable Aut) :=
{ on_equiv := λ α β e, equiv.arrow_congr e e,
  on_refl  := λ α, equiv.ext _ _ $ λ f, funext $ λ x, rfl,
  on_trans := λ α β γ e1 e2, equiv.ext _ _ $ λ f, funext $ λ x,
    by cases e1; cases e2; refl }

-- If we have all these in place...
-- A bit of magic might actually be able to derive `group.transportable` on line 11.
-- After all, a group just is a type plus some functions... and we can now transport functions.
```

#### [Kenny Lau (Apr 27 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786273):
golfed

#### [Kenny Lau (Apr 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786284):
@**Kevin Buzzard**

#### [Kenny Lau (Apr 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786301):
https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean

#### [Kevin Buzzard (Apr 27 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787049):
This is looking good

#### [Kenny Lau (Apr 27 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787068):
unfortunately, they wrote a destructor for `equiv.prod_congr` but not `equiv.arrow_congr`

#### [Kevin Buzzard (Apr 27 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787133):
Wooah what is going on in that proof of `Prod.transportable.on_equiv`

#### [Kenny Lau (Apr 27 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787138):
that's the example of a good destructor

#### [Kevin Buzzard (Apr 27 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787210):
kenny you still didn't beat the boss

#### [Kenny Lau (Apr 27 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787228):
who is the boss?

#### [Kevin Buzzard (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787429):
@**Johan Commelin** Kenny did all your levels

#### [Kevin Buzzard (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787430):
except for group

#### [Kenny Lau (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787432):
I thought `group` is to be automated lol

#### [Kevin Buzzard (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787439):
https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean

#### [Kevin Buzzard (Apr 27 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787450):
So I think that you were looking for destructors in `equiv.lean`

#### [Kevin Buzzard (Apr 27 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787454):
which is a really good place to look for them

#### [Kevin Buzzard (Apr 27 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787504):
@**Simon Hudon** what is the next move?

#### [Kevin Buzzard (Apr 27 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787520):
Are these solutions in any way useful to help writing a general tactic which would prove `equiv a b -> equiv (topological_field a) (topological_field b)`?

#### [Kevin Buzzard (Apr 27 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787526):
What needs to be done next?

#### [Simon Hudon (Apr 27 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787601):
I'm looking into automating those proofs. I'm keeping it for later tonight, when I've met my writing goals for the week

#### [Simon Hudon (Apr 27 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787647):
I have a tactic, `refine_struct`, on the back burner which I might have to finish to facilitate this exercise

#### [Kevin Buzzard (Apr 27 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787731):
Simon is there anything I can do to help?

#### [Simon Hudon (Apr 27 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787876):
Thanks for offering. Are you thinking of something in particular?

#### [Kevin Buzzard (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787888):
I don't understand how https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/proof.20of.20the.20five.20lemma/near/125768238 fits into the picture

#### [Kevin Buzzard (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787896):
Simon I am just interested in the question and it's the weekend

#### [Kevin Buzzard (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787907):
I really enjoyed playing some of Johan's levels

#### [Kenny Lau (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787910):
I enjoyed outgolfing kevin :P

#### [Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787954):
and I wondered if you might say something of the form "please give me a human proof of `foo.transportable`

#### [Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787958):
because these proofs are all really easy to do

#### [Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787960):
because Kenny has found a million tricks

#### [Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787970):
so the two motivations for doing more levels are

#### [Kevin Buzzard (Apr 27 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787971):
(1) it's fun

#### [Kevin Buzzard (Apr 27 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787980):
(2) it might help you see patterns

#### [Kevin Buzzard (Apr 27 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787984):
(3) it might be necessary to get the automation off the ground

#### [Simon Hudon (Apr 27 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788036):
I don't know how much fun it would be but how do you feel about writing a few sentences on some of the tricks that Kenny found?

#### [Simon Hudon (Apr 27 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788097):
... or a minimal example for them

#### [Johan Commelin (Apr 27 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788446):
Ok, really cool

#### [Johan Commelin (Apr 27 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788486):
I knew that Hom1 would be easy, given Fun

#### [Johan Commelin (Apr 27 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788500):
But currying should also help, right?

#### [Johan Commelin (Apr 27 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788504):
to express some of the lemmas in terms of others...

#### [Johan Commelin (Apr 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788596):
@**Kenny Lau** You did not dissappoint me (-;

#### [Kenny Lau (Apr 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788603):
:D

#### [Johan Commelin (Apr 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788704):
By the way, what do you think... `transportable` or `transport_of_structure` ?

#### [Johan Commelin (Apr 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788707):
I think I actually prefer the latter...

#### [Johan Commelin (Apr 27 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788792):
@**Kenny Lau** `Aut = Fun \circ Prod`. Doesn't that help?

#### [Johan Commelin (Apr 27 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788837):
I hope it does... because that is how a mathematician would prove it...

#### [Johan Commelin (Apr 27 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788844):
Aaah, so maybe here is "level 3": show that transportable stuff composes

#### [Johan Commelin (Apr 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788852):
Lean is a nightmare on the machine that I am typing on.

#### [Johan Commelin (Apr 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788859):
So I can't actually do anything myself (-;

#### [Patrick Massot (Apr 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788866):
Have you compiled mathlib on this machine?

#### [Johan Commelin (Apr 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788873):
@**Kevin Buzzard** If you are looking for another small challenge, maybe show that if `f` and `g` are transportable, then so is `g \circ f`.

#### [Johan Commelin (Apr 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788917):
@**Patrick Massot** An old version... it took more then an hour and the machine was unusable and almost overheating.

#### [Kenny Lau (Apr 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788922):
```quote
@**Kenny Lau** `Aut = Fun \circ Prod`. Doesn't that help?
```
unfortunately the transitive destructor is not available :P

#### [Johan Commelin (Apr 27 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788929):
This is a Thinkpad X61: older than my kids...

#### [Kenny Lau (Apr 27 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788933):
I might have to prove those destructors

#### [Johan Commelin (Apr 27 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788938):
That sounds like it is useful

#### [Kenny Lau (Apr 27 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789003):
oh that isn't a transitive destructor though

#### [Kenny Lau (Apr 27 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789007):
I mean, `@[trans]` won't work

#### [Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789226):
here is a recent Lean tip -- occasionally get your file and give it a good shake

#### [Kenny Lau (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789235):
@**Johan Commelin** how is Aut = Fun \o Prod?

#### [Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789241):
I think Gabriel changed the VS Code Lean extension

#### [Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789244):
so it only compiles parts of the file

#### [Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789246):
and sometimes it can get confused

#### [Kenny Lau (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789247):
the compiler is very slow for me recently

#### [Kenny Lau (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789249):
I often have to wait 10+ minutes before things compile

#### [Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789250):
and giving it a shake works well for me

#### [Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789253):
oh that's not good

#### [Johan Commelin (Apr 27 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789302):
@**Kenny Lau** That was a bit of a brain-fart. Sorry

#### [Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789314):
```lean
local attribute [simp] transportable.on_refl transportable.on_trans

def transportable.trans (f : Type u → Type v) (g : Type v → Type w)
  [transportable f] [transportable g] : transportable (g ∘ f) :=
{ on_equiv := λ α β e, show g (f α) ≃ g (f β), from transportable.on_equiv g (transportable.on_equiv f e),
  on_refl  := λ α, by simp,
  on_trans := λ α β γ e₁ e₂, by simp }
```

#### [Johan Commelin (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789315):
Mi mas go slip nau. Gutpela wok olgeta! Lukim!

#### [Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789317):
I like my addition

#### [Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789318):
https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean

#### [Kevin Buzzard (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789320):
```quote
I don't know how much fun it would be but how do you feel about writing a few sentences on some of the tricks that Kenny found?
```
I would love to do that.

#### [Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789322):
tok pisin :o

#### [Johan Commelin (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789327):
Em nau.

#### [Kevin Buzzard (Apr 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790151):
Hey! `topological_ring _` is a `Prop` not a `Type`

#### [Kevin Buzzard (Apr 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790167):
`theorem topological_ring.transportable : transportable topological_ring := sorry`

#### [Kevin Buzzard (Apr 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790210):
gives an error

#### [Kevin Buzzard (Apr 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790214):
```lean
type mismatch at application
  transportable topological_ring
term
  topological_ring
has type
  Π (α : Type ?) [_inst_1 : topological_space α] [_inst_2 : ring α], Prop : Type (?+1)
but is expected to have type
  Type ? → Type ? : Type (max (?+1) (?+1))
```

#### [Kevin Buzzard (Apr 27 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790240):
My new toy is broken

#### [Kevin Buzzard (Apr 27 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790251):
`class transportable (f : Type u → Type v) :=`

#### [Kevin Buzzard (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790311):
it's not that it's a prop

#### [Kevin Buzzard (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790314):
is the issue that it's not a function?

#### [Kenny Lau (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790321):
right

#### [Kevin Buzzard (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790331):
but a topological ring is the same as a group

#### [Kevin Buzzard (Apr 27 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790357):
if I have a topological ring structure on X and a canonical isomorphism `X -> Y` then I want a topological ring structure on `Y`

#### [Kevin Buzzard (Apr 27 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790950):
What is `theorem topological_ring.transportable ` ?

#### [Kevin Buzzard (Apr 27 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791009):
```lean
import analysis.topology.topological_structures
#check topological_ring
```

#### [Kevin Buzzard (Apr 27 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791026):
this doesn't typecheck

#### [Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791027):
```lean
theorem topological_ring.transportable : transportable
  (λ R : (Σ (α : Type u), (topological_space α) × (ring α)) , 
    @topological_ring R.fst (R.snd).1 (R.snd).2) := sorry
```

#### [Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791031):
What am I doing wrong?

#### [Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791039):
Simon -- I was writing some goals in the docs

#### [Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791044):
and transfer of a topological ring structure is one of the goals

#### [Kevin Buzzard (Apr 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791207):
we can write this

#### [Kevin Buzzard (Apr 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791210):
`def transport_ring {α β : Type} [topological_field α] (f : α ≃ β) : topological_field β := sorry`

#### [Kevin Buzzard (Apr 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791214):
but I don't understand how to embed it in the `transportable` class

#### [Kevin Buzzard (Apr 27 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792177):
Kenny you posted this earlier:

#### [Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792187):
```lean
import data.equiv

def transport_ring {α β : Type*} [ring α] (f : α ≃ β) : ring β :=
{ add := λ x y, f (f.symm x + f.symm y),
  zero := f 0,
  neg := λ x, f (-f.symm x),
  mul := λ x y, f (f.symm x * f.symm y),
  one := f 1,
  add_assoc := λ x y z, by simp; from add_assoc _ _ _,
  zero_add := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (zero_add _),
  add_zero := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (add_zero _),
  add_left_neg := λ x, by simp; from add_left_neg _,
  add_comm := λ x y, by simp; from add_comm _ _,
  mul_assoc := λ x y z, by simp; from mul_assoc _ _ _,
  one_mul := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (one_mul _),
  mul_one := λ x, by simp; from (equiv.apply_eq_iff_eq_inverse_apply _ _ _).2 (mul_one _),
  left_distrib := λ x y z, by simp; from left_distrib _ _ _,
  right_distrib := λ x y z, by simp; from right_distrib _ _ _, }
```

#### [Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792191):
and if I change the top lines to

#### [Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792208):
```lean
import data.equiv
universes u v
def transport_ring {α : Type u} {β : Type v} [ring α] (f : α ≃ β) : ring β :=
```

#### [Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792210):
then your code doesn't compile any more

#### [Kenny Lau (Apr 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792257):
this is interesting

#### [Kevin Buzzard (Apr 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792259):
Are you only proving `transport_ring` for types in the same universe, and is this easier to do than the general case?

#### [Kevin Buzzard (Apr 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792706):
```lean
import data.equiv
import analysis.topology.topological_structures

def transport_topological_ring {α β : Type} 
  [topological_space α] [ring α] [topological_ring α] (f : α ≃ β) : @topological_ring β sorry sorry := sorry
```

#### [Chris Hughes (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792744):
I doesn't seem like it would be any easier in the same universe.

#### [Kevin Buzzard (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792746):
Least it typechecks

#### [Kevin Buzzard (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792751):
I tried putting Kenny's proof into the same universe and there were still errors

#### [Kevin Buzzard (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792754):
there are universe subtleties I don't understand

#### [Kevin Buzzard (Apr 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792796):
Chris this is all your fault :-)

#### [Kevin Buzzard (Apr 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792804):
You proved the lemma only for rings canonically isomorphic to the rings I wanted

#### [Reid Barton (Apr 28 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795177):
By adding more `transportable` classes for type constructors with multiple arguments, we could extend these ideas to situations where we have an isomorphism which respects some existing structure and we want to transport some additional structure (or property) across it. Here is a sketch of the idea: https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad

#### [Reid Barton (Apr 28 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795238):
The key point is the definition
```lean
def is_homeomorphism {α β : Type u} [tα : topological_space α] [tβ : topological_space β] (e : α ≃ β) :=
tβ = transport topological_space e tα
```
which seems to be more fundamental than the category-style definition "continuous function with a continuous inverse", since the definition of `transport` does not even need the notion of continuous function.

#### [Kevin Buzzard (Apr 28 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795266):
This proof does not work:

#### [Kevin Buzzard (Apr 28 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795307):
```lean
def Const : Type u → Type v := λ α, punit
lemma Const.transportable : (transportable Const) :=
{ on_equiv := λ α β e, equiv.punit_equiv_punit,
  on_refl  := λ α, equiv.ext _ _ $ λ ⟨⟩, rfl,
  on_trans := λ α β γ e1 e2, by congr}
```

#### [Kevin Buzzard (Apr 28 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795310):
but this proof works:

#### [Kevin Buzzard (Apr 28 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795316):
```lean
def Const : Type u → Type v := λ α, punit
lemma Const.transportable : (transportable Const) :=
{ on_equiv := λ α β e, equiv.punit_equiv_punit,
  on_refl  := λ α, equiv.ext _ _ $ λ ⟨⟩, rfl,
  on_trans := λ α β γ e1 e2, equiv.ext _ _ $ λ ⟨⟩, rfl }
```

#### [Kevin Buzzard (Apr 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795325):
and this proof works:

#### [Kevin Buzzard (Apr 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795331):
```lean
def Const' : Type u → Type v := λ α, punit
lemma Const'.transportable : (transportable Const) := { 
  on_equiv := λ α β H,⟨λ _,punit.star,λ _,punit.star,λ ⟨⟩,rfl,λ ⟨⟩,rfl⟩,
  on_refl := λ α, equiv.ext _ _ (λ ⟨⟩,rfl),
  on_trans := λ α β γ Hαβ Hβγ,by congr
  } 
```

#### [Kevin Buzzard (Apr 28 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795386):
I am interested in the idea of filling in fields using tactics but I can only use `congr` if I set it up in a certain way

#### [Kevin Buzzard (Apr 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795472):
```quote
did you take a look at the `transfer` paper I linked way back? That's how in core lean they move proofs between `int` and `(a , b) : nat * nat`, which (and maybe I'm not understanding the details here very well) is your problem of transporting proofs between isomorphic types?
```
Can you remind me of the link?

#### [Kevin Buzzard (Apr 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795475):
@**Andrew Ashworth**

#### [Kevin Buzzard (Apr 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795476):
My search skills are weak today

#### [Kevin Buzzard (Apr 28 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795552):
```quote
The key point is the definition
```lean
def is_homeomorphism {α β : Type u} [tα : topological_space α] [tβ : topological_space β] (e : α ≃ β) :=
tβ = transport topological_space e tα
```
which seems to be more fundamental than the category-style definition "continuous function with a continuous inverse", since the definition of `transport` does not even need the notion of continuous function.
```
At some point I am going to want more than just an equiv -- I will want that two canonical isomorphisms `equiv A A'` and `equiv B B'` commute with some given maps `A -> B` and `A' -> B'` which are both "defined naturally".

#### [Kevin Buzzard (Apr 28 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795611):
For example Reid, I proved that if `D(g) sub D(f)` then not only is `f` a unit in `R[1/g]`, but the rings `R[1/g]` and `R[1/f][1/gbar]` were canonically isomorphic, where `gbar` is the image of `g` in `R[1/f]`

#### [Kevin Buzzard (Apr 28 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795634):
And by "prove that they're canonically isomorphic" I mean in practice that I proved that I could write down an isomorphism of R-algebras which was also the unique R-algebra homomorphism in either direction.

#### [Kevin Buzzard (Apr 28 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795640):
and I am pretty sure that I don't need to prove any more "canonicalness" for my application to schemes.

#### [Kevin Buzzard (Apr 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795686):
The idea is that `f : R` is now fixed

#### [Kevin Buzzard (Apr 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795695):
and `g : { g : R // D(g) sub D(f) }` varies

#### [Kevin Buzzard (Apr 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795699):
and `A g := R[1/g]`

#### [Kevin Buzzard (Apr 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795702):
and `A' g := R[1/f][1/gbar]`

#### [Kevin Buzzard (Apr 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795711):
Does this fit into your "extra structure" idea?

#### [Reid Barton (Apr 28 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795894):
`B` is `A g'` for another `g'`?

#### [Reid Barton (Apr 28 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795909):
Or something else entirely?

#### [Kenny Lau (Apr 28 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795971):
I'm back

#### [Reid Barton (Apr 28 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796055):
It sounds like you want to prove that your isomorphism between `R[1/g]` and `R[1/f][1/gbar]` is natural (in the category theory sense) when these two localization constructions are viewed as functors of something (R and/or g?), and that is probably not a purely formal fact that follows from transporting across "equalities". (On the other hand, it is probably a slightly less formal fact that follows easily from some universal property.)

#### [Kevin Buzzard (Apr 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796240):
docs

#### [Kevin Buzzard (Apr 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796244):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonical.md

#### [Kevin Buzzard (Apr 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796245):
permanlink

#### [Kenny Lau (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796294):
speaking of which, it's almost a month since your last post in xena

#### [Kevin Buzzard (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796296):
don't know how to do permalink

#### [Kenny Lau (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796298):
https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md

#### [Kenny Lau (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796299):
there you go

#### [Kenny Lau (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796303):
try deleting the file :P

#### [Kevin Buzzard (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796305):
I want to focus on schemes Kenny, and I guess the situation is that it would be nice to resolve this canonical isomorphism issue before I go any further

#### [Kevin Buzzard (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796313):
I will probably blog about this though

#### [Kenny Lau (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796317):
should I write a guest post

#### [Reid Barton (Apr 28 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796376):
(You can click on the commit id near the right side of the blue bar, and then View)

#### [Reid Barton (Apr 28 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796713):
Let me address the question at the end of those docs, since your "three lemma" was what prompted the gist I linked earlier.
You could define a structure indexed on A B C that consists of abelian group structures on A B C and group homomorphisms f : A -> B and g : B -> C. The input to the "three lemma" is an isomorphism of such structures.
The further structure would be exactness of the sequence, i.e., the equation ker g = im f; that's what you want to transport to the new sequence.

#### [Reid Barton (Apr 28 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796852):
Simply transporting the combined structure of "being an exact sequence" across your isomorphisms A -> A', B -> B', C -> C' won't be enough, since you also need to know that the transported group structures and maps agree with your original ones.

#### [Reid Barton (Apr 28 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796860):
(for which you need precisely that the maps are group isomorphisms and the squares commute)

#### [Reid Barton (Apr 28 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796932):
I guess if you had lemmas to calculate the components of the transported structure, then that would be another way to do it.

#### [Reid Barton (Apr 28 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797044):
I need to make dinner but I'll try to produce some example code later

#### [Kevin Buzzard (Apr 28 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797105):
I see! I find it much easier to understand this example.

#### [Kevin Buzzard (Apr 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797107):
So one makes a new structure

#### [Kevin Buzzard (Apr 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797113):
and then attempts to transport it

#### [Kevin Buzzard (Apr 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797115):
This sounds like a beautiful way of thinking about it.

#### [Kevin Buzzard (Apr 28 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797487):
Kenny you are welcome to write a guest post

#### [Kevin Buzzard (Apr 28 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797493):
On whatever topic you like

#### [Andrew Ashworth (Apr 28 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125798645):
the transfer paper is here:  https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf

#### [Kevin Buzzard (Apr 28 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125798996):
Thanks Andrew.

#### [Kevin Buzzard (Apr 28 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799001):
Reid -- you probably know the full story anyway, but let me spell it out.

#### [Kevin Buzzard (Apr 28 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799058):
Chris proved a lemma saying that if `R` is a ring and `f1,f2,...,fn` are elements which generate the unit ideal, then the structure sheaf on Spec(R) satisfies the sheaf axiom with respect to the open cover D(f1),..,D(fn).

#### [Kevin Buzzard (Apr 28 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799065):
Formally, as you know, this says that the canonical map from `R` to $$\Pi_i R[1/f_i]$$ is an injection,

#### [Kevin Buzzard (Apr 28 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799110):
with image equal to the kernel of the usual map $$\Pi_i R[1/f_i] \to \Pi_{i,j} R[1/f_if_j]$$

#### [Kevin Buzzard (Apr 28 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799118):
and note that this latter map sends $$(s_i)_{i\in I}$$ to $$(s_i-s_j)_{i,j}$$

#### [Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799120):
which is not a ring homomorphism

#### [Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799128):
but it is a difference of two such

#### [Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799133):
and hence the whole map is a group homomorphism

#### [Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799137):
Now I have done some abstract ring theory in Lean over the last few weeks, working on "an interface for localisation"

#### [Kevin Buzzard (Apr 28 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799181):
and I have now proved some technical lemma which says that if $$D(g)\subseteq D(f)$$ then $$R[1/g]$$ is canonically isomorphic to $$R[1/f][1/gbar]$$

#### [Kevin Buzzard (Apr 28 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799182):
with $$gbar$$ the image of $$g$$

#### [Kevin Buzzard (Apr 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799191):
and canonical isomorphism for me at this point means that we are given an element of `equiv` $$(R[1/g])$$ $$(R[1/f][1/gbar])$$

#### [Kevin Buzzard (Apr 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799193):
(maths notation is better than Lean)

#### [Kevin Buzzard (Apr 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799194):
with the following wonderful properties:

#### [Kevin Buzzard (Apr 28 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799236):
1) the functions are ring homs (and hence ring isoms)

#### [Kevin Buzzard (Apr 28 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799238):
2) The only $$R$$-algebra hom from $$R[1/g]$$ to $$R[1/f][1/gbar]$$ is our given element.

#### [Kevin Buzzard (Apr 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799246):
I am _hoping_ that this is a good definition of "canonical isomorphism" here.

#### [Kevin Buzzard (Apr 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799249):
These are the facts which I isolated as important

#### [Kevin Buzzard (Apr 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799250):
I made a structure for each of them

#### [Kevin Buzzard (Apr 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799308):
```lean
structure R_alg_equiv {R : Type u} {α : Type v} {β : Type w} [comm_ring R] [comm
_ring α] [comm_ring β]
  (sα : R → α) (sβ : R → β) extends ring_equiv α β :=
(R_alg_hom : sβ = to_fun ∘ sα)

```

#### [Kevin Buzzard (Apr 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799360):
```lean
structure is_unique_R_alg_hom {R : Type u} {α : Type v} {β : Type w} [comm_ring R] [comm_ring α] [comm_ring β] 
(sα : R → α) (sβ : R → β) (f : α → β) [is_ring_hom sα] [is_ring_hom sβ] [is_ring_hom f] : Prop :=
(R_alg_hom : sβ = f ∘ sα)
(is_unique : ∀ (g : α → β) [is_ring_hom g], sβ = g ∘ sα → g = f)

```

#### [Kevin Buzzard (Apr 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799370):
(NB it was `is_unique_R_alg_hom` which I noticed was not a `Prop` even though it could be -- I made it a Prop.)

#### [Kevin Buzzard (Apr 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799381):
I have lots of cunning ways of producing unique R-algebra homs

#### [Kevin Buzzard (Apr 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799386):
for example given a ring hom `R -> \beta` with the property that every element of a mult subset `S` gets sent to a unit

#### [Kevin Buzzard (Apr 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799428):
I have a unique `R`-alg com `R[1/S] -> beta`

#### [Kevin Buzzard (Apr 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799431):
I am hoping that the ideas I already have will be enough to see me through

#### [Kevin Buzzard (Apr 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799440):
so I am going to try and define the structures that we want to identify and then see if I can figure out what needs doing.

#### [Kevin Buzzard (Apr 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799448):
@**Kenny Lau** In short I am saying that your proof of exactness being preserved stinks

#### [Kevin Buzzard (Apr 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799454):
and it would be better to have a proof which looks a whole lot more abstract

#### [Kevin Buzzard (Apr 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799497):
because then when next week I have to prove something ten times longer but just as trivial

#### [Kevin Buzzard (Apr 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799500):
we can get xena to do it for us

#### [Scott Morrison (Apr 28 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125800546):
Wow... a lot happened while I slept. :-)

#### [Simon Hudon (Apr 28 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125800763):
Let this be a lesson to you: don't sleep

#### [Kevin Buzzard (Apr 28 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801226):
Does this look OK:

#### [Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801228):
```lean
import data.equiv
-- recall the interface for equiv:
-- C : equiv α β;
-- the function is C, the function the other way is C.symm, which is also the equiv the other way
-- and the proofs are C.inverse_apply_apply and C.apply_inverse_apply
universes u v w u' v' w'

open equiv 

-- Scott's basic class.
class transportable (f : Type u → Type v) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))

variables 
{α : Type u} {β : Type v} {γ : Type w} {α' : Type u'} {β' : Type v'} {γ' : Type w'}

structure canonically_isomorphic_functions 
(Cα : equiv α α') (Cβ : equiv β β') (f : α → β) (f' : α' → β') -- extends equiv α α', equiv β β'
:= 
(commutes : ∀ a : α, Cβ (f a) = f' (Cα a))
-- is there a better way to do this with "extends"?

-- Do I need an interface for this? Why can't I make this a simp lemma?
theorem canonically_isomorphic_functions.diag_commutes
(Cα : equiv α α') (Cβ : equiv β β') (f : α → β) (f' : α' → β')
(C : canonically_isomorphic_functions Cα Cβ f f') : ∀ a : α, Cβ (f a) = f' (Cα a) := C.commutes 

definition canonically_isomorphic_functions.refl :
Π {α : Type u} {β : Type v} (f : α → β), canonically_isomorphic_functions 
(equiv.refl α) (equiv.refl β) f f := λ α β f,⟨λ a, rfl⟩

definition canonically_isomorphic_functions.symm :
∀ (f : α → β) (f' : α' → β') (Cα : equiv α α') (Cβ : equiv β β'),
canonically_isomorphic_functions Cα Cβ f f' → 
canonically_isomorphic_functions Cα.symm Cβ.symm f' f := 
λ f f' Cα Cβ Cf,⟨λ a',begin
  suffices : Cβ.symm (f' (Cα (Cα.symm a'))) = f (Cα.symm a'),
    by simpa using this,
  suffices : Cβ.symm (Cβ (f (Cα.symm a'))) = f (Cα.symm a'),
    by simpa [Cf.commutes (Cα.symm a')],
  simp,
end 
⟩


definition canonically_isomorphic_functions.trans :
∀ (f : α → β) (f' : α' → β') (g : β → γ) (g' : β' → γ') 
(Cα : equiv α α') (Cβ : equiv β β') (Cγ : equiv γ γ'),
canonically_isomorphic_functions Cα Cβ f f' → 
canonically_isomorphic_functions Cβ Cγ g g' → 
canonically_isomorphic_functions Cα Cγ (g ∘ f) (g' ∘ f') := 
λ f f' g g' Cα Cβ Cγ Cf Cg,⟨λ a,begin
  show Cγ (g (f a)) = g' (f' (Cα a)),
  rw [Cg.commutes,Cf.commutes]
end⟩
```

#### [Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801279):
Scott, I was inspired by your structure

#### [Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801280):
Did you see the docs?

#### [Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801284):
It's a summary of what happened

#### [Kevin Buzzard (Apr 28 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801299):
@**Reid Barton** Can you fit these canonically isomorphic functions into your way of thinking?

#### [Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801342):
@**Scott Morrison** Johan expanded out your idea into a series of little definitions

#### [Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801345):
And @**Kenny Lau** filled them all in

#### [Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801346):
https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean

#### [Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801350):
@**Reid Barton** wrote something I didn't understand yet:

#### [Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801351):
https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad

#### [Kevin Buzzard (Apr 28 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801359):
and I wrote some docs

#### [Kevin Buzzard (Apr 28 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801360):
https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md

#### [Kevin Buzzard (Apr 28 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801407):
and now I am wondering about whether it's a good idea to think of the concept that a square with equivs down the sides commutes

#### [Kevin Buzzard (Apr 28 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801411):
as an equiv between the other two sides

#### [Kevin Buzzard (Apr 28 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801426):
The definition doesn't seem to fit into your "transportable" yoga

#### [Kevin Buzzard (Apr 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801480):
and this

#### [Kevin Buzzard (Apr 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801481):
`theorem topological_ring.transportable : transportable topological_ring := sorry`

#### [Kevin Buzzard (Apr 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801482):
is a type mismatch

#### [Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801490):
but on the other hand I am pretty sure I want to transport topological rings

#### [Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801495):
@**Simon Hudon** I wrote docs

#### [Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801497):
Do you want me to add anything else?

#### [Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801499):
I am currently working on formalising a high-level proof of the exactness statement I want

#### [Reid Barton (Apr 28 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801605):
I haven't really caught up on any of the recent discussion, but regarding the commutative square with two equivs $$e_A : A \to A'$$ and $$e_B : B \to B'$$, my current way of thinking about this is that transporting the structure of a map $$f : A \to B$$ along these two equivs produces a map $$A' \to B'$$ which will be given by the formula $$e_B \circ f \circ e_A^{-1}$$

#### [Reid Barton (Apr 28 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801610):
and the condition that your square commutes can then be reinterpreted as saying that the bottom map is the map that you get by transporting the top map along the sides

#### [Kevin Buzzard (Apr 28 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801620):
So is this a relation between $$f$$ and $$f'$$ like `equiv`?

#### [Kevin Buzzard (Apr 28 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801622):
Or is this a transportation of the structure?

#### [Simon Hudon (Apr 28 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801623):
@**Kevin Buzzard** Thanks! 

```quote
I am currently working on formalising a high-level proof of the exactness statement I want
```
That's a good idea. Maybe apologize everywhere you'd expect to derive a transferable instance

#### [Kevin Buzzard (Apr 28 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801661):
Right

#### [Kevin Buzzard (Apr 28 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801664):
or admit defeat

#### [Reid Barton (Apr 28 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801665):
Which in turn, is going to be the condition you need to know that the fact that you transported across the isomorphisms (like exactness) is actually about your original maps A' -> B' -> C'.

#### [Reid Barton (Apr 28 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125803762):
@**Kevin Buzzard** I finished writing up the proof of the "three lemma" from `transportable` instances/lemmas which could plausibly be autogenerated. It's still pretty gross and could probably use some refinement.
https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff

#### [Reid Barton (Apr 28 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125804891):
Updated version uses a simp attribute to handle all the goals at once

#### [Reid Barton (Apr 28 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805096):
@**Simon Hudon**, you might also be interested in the above--stuff defined as `magic` is what I would like to have autogenerated

#### [Johan Commelin (Apr 28 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805104):
```quote
By adding more `transportable` classes for type constructors with multiple arguments, we could extend these ideas to situations where we have an isomorphism which respects some existing structure and we want to transport some additional structure (or property) across it. Here is a sketch of the idea: https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad
```
I want some emphasis on this remark by Reid.

#### [Johan Commelin (Apr 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805143):
This is very important. And our current proposal does not fit...

#### [Johan Commelin (Apr 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805146):
So, how about this: Every time we define/prove a coercion, we also derive `transportable2` in the other direction.

#### [Johan Commelin (Apr 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805153):
Which means, if you have two `int` that are equal, and one of them came from a `nat`, then the other one came from the same `nat`

#### [Johan Commelin (Apr 28 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805210):
But also, if you have a `ring R` that is group-isomorphic to some `group G`, then you get a ring structure on `G` for free, and the underlying group structure of this new ring structure is exactly the group structure on `G` that you started with.

#### [Johan Commelin (Apr 28 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805211):
I think coercions exactly determine where transport of structure applies.

#### [Johan Commelin (Apr 28 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805440):
@**Reid Barton** Is what I'm saying canonically isomorphic to your remarks? I.e., did I transport the structure of your remarks?

#### [Kevin Buzzard (Apr 28 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806580):
So I pushed my work on "canonically isomorphic functions" between canonically isomorphic types

#### [Kevin Buzzard (Apr 28 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806581):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/sheaf_canonical.lean

#### [Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806594):
Let me state what I think the state of things is

#### [Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806595):
We had an idea about defining a class called transportable

#### [Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806597):
and I want to define a structure called a canonical isomorphism

#### [Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806598):
which doesn't have to be the maths one

#### [Kevin Buzzard (Apr 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806638):
but it has to be good enough to deal the mortal blow to the final boss in affine schemes.

#### [Kevin Buzzard (Apr 28 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806648):
Transportable originally ate a function `Type -> Type` or perhaps `Type u -> Type v` depending on what mood people were in. Because this is a CS thing I suppose we will end up with `Type u -> Type v`

#### [Kevin Buzzard (Apr 28 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806649):
But now we want it to eat more

#### [Kevin Buzzard (Apr 28 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806690):
for example we want it to eat the instance of the type class resolution system which sends a ring to an additive group

#### [Kevin Buzzard (Apr 28 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806699):
and spit out a theorem that says that if a equiv a' then the square commutes up to definitional equality.

#### [Kevin Buzzard (Apr 28 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806700):
by which I mean Lean definitional equality, ideally.

#### [Kevin Buzzard (Apr 28 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806742):
the square goes from ring a to ring a' on the top, from group a to group a' on the bottom, and the maps down are coming from the type class inference system

#### [Kevin Buzzard (Apr 28 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806745):
So which instances of type class inference will commute with equiv in this way?

#### [Kevin Buzzard (Apr 28 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806802):
Can we not _assume_ that if alpha is a type which happens to have both a group structure and a ring structure then the group structure associated to the ring structure is the one which the type class inference system would associate to the ring structure?

#### [Kevin Buzzard (Apr 28 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806803):
Because if this is not the case then the Diamond is nigh, right?

#### [Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806843):
So this would seem like the correct theorem to prove

#### [Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806848):
Oh I have a question @**Johan Commelin** !

#### [Reid Barton (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806849):
Kevin, I'm not sure how helpful this remark will be, but your `canonically_isomorphic_functions Cα Cβ f f'` is in my setup `f' = transport2 (→) Cα Cβ f`

#### [Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806850):
Do you know those WIP docs?

#### [Andrew Ashworth (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806852):
a tactic that takes two types, a function relating the two, and from Prop (input 1) return Prop (input 2), is that what people are discussing?

#### [Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806853):
Mario gave me an example of a way to break the type class resolution system in a really annoying way

#### [Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806858):
What happens if you try and prove that those maps are all canonical?

#### [Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806861):
Does that make any sense?

#### [Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806863):
Reid, I am sure you are thinking about it in a better way than me

#### [Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806865):
and I am absolutely convinved that we should get this as abstract as possible

#### [Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806866):
thanks for the pointer!

#### [Johan Commelin (Apr 28 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806904):
@**Andrew Ashworth** Yes, more or less.

#### [Reid Barton (Apr 28 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806908):
@**Johan Commelin**, I'm not sure what you mean by coercion. Are you talking about `has_coe`?

#### [Johan Commelin (Apr 28 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806909):
@**Andrew Ashworth** The basic example. Given `a b : Type`, `equiv a b` and also `[group a]` we want to automagically have `group b`

#### [Andrew Ashworth (Apr 28 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806915):
i'll mention again the transfer tactic in core lean that produces `int` from `pairs of nat`, and the paper that describes it is linked earlier... unless i'm totally off-base

#### [Johan Commelin (Apr 28 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806917):
@**Reid Barton** I'm still a novice. But I guess that is what I mean.

#### [Kevin Buzzard (Apr 28 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806918):
https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md

#### [Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806958):
In the "to be tidied" section

#### [Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806960):
there is Mario busting the type class inference system

#### [Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806962):
following an idea of mine

#### [Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806963):
trying to find a fairly explicit example of how it can bust

#### [Kevin Buzzard (Apr 28 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806966):
because two natural numbers are equal but the proof is not "rfl"

#### [Kevin Buzzard (Apr 28 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807014):
The type class system breaks quite badly if you find two different ways of getting from A to B

#### [Kevin Buzzard (Apr 28 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807015):
On the other hand I am pretty sure that I want to allow more than one canonical isomorphism between two objects

#### [Andrew Ashworth (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807021):
transfer in action: constructing an efficient representation of `int` from the pre-int pair of nat... https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean

#### [Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807022):
For example I think I want the sum of two canonical isomorphisms from a group to a group to be a canonical isomorphism

#### [Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807024):
I know int.basic pretty well

#### [Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807025):
What does this have to do with anything?

#### [Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807026):
I understand the int typeclass

#### [Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807066):
and you are saying that int canonically bijects with nat + nat?

#### [Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807067):
I would say that that bijection is not canonical

#### [Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807068):
It's a junk theorem I think

#### [Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807069):
In a parallel universe int was constructed as a quotient type on nat x nat

#### [Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807072):
or one day Leo changes int to this

#### [Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807075):
and nobody notices

#### [Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807076):
because maybe we all use the int interface

#### [Andrew Ashworth (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807079):
isn't that the tactic machinery you're interested in, however?

#### [Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807080):
Evidence that that bijection is not canonical is that it does not behave well with respect to arithmetic operations like +

#### [Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807081):
Oh -- I see

#### [Johan Commelin (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807084):
@**Kevin Buzzard** Concerning Mario's example. Basically, you prove that `nat \times nat` has a ring structure, and then coerce by taking the sum. But the sum is not a ring homomorphism... Is that what is going on?

#### [Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807085):
I'm afraid my eyes glaze over whenever I see tactic machinery

#### [Kevin Buzzard (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807123):
I don't understand it at all

#### [Reid Barton (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807133):
It actually is using `nat \times nat`.

#### [Kevin Buzzard (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807134):
@**Johan Commelin** no multiplication is involved

#### [Kevin Buzzard (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807151):
no multiplication of nats at least

#### [Kenny Lau (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807153):
```quote
because maybe we all use the int interface
```
nope. lots of things in mathlib use the definition of int

#### [Kevin Buzzard (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807156):
Johan -- the only canonical thing you are allowed to do with nats is add them up in Mario's example

#### [Kevin Buzzard (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807157):
So there's a type which carries a nat

#### [Kevin Buzzard (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807194):
and one which carries two nats

#### [Kevin Buzzard (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807197):
and the type class inference system will take you from the two nat guys to the one nat guys by just adding up their two nats

#### [Johan Commelin (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807198):
Ah, sorry, brainfarting again

#### [Kevin Buzzard (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807202):
But there is also this product construction

#### [Reid Barton (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807203):
Er, to clarify, the `int` transfer stuff (which I don't know anything about) uses `nat \times nat`

#### [Kevin Buzzard (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807209):
and you just add up the nats

#### [Kevin Buzzard (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807214):
so now there's two ways of getting from a pair `(a,b)` of two-nat guys

#### [Kevin Buzzard (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807215):
to one one-nat guy

#### [Kevin Buzzard (Apr 28 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807256):
and `(r+s)+(t+u)` is not definitionally equal to `(r+t)+(s+u)`

#### [Kevin Buzzard (Apr 28 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807257):
you need a proof by induction for that

#### [Johan Commelin (Apr 28 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807259):
Right, that's what is going on

#### [Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807264):
and then rw stops working

#### [Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807268):
because rw keeps track of the exact definitions of the instances

#### [Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807269):
no

#### [Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807270):
the types keep track

#### [Johan Commelin (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807271):
@**Andrew Ashworth** Which lines should we look at, to see transfer in action, in int/basic.lean

#### [Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807273):
and rw looks at the types

#### [Andrew Ashworth (Apr 28 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807315):
@**Johan Commelin** line 399 proves the integers form a ring

#### [Andrew Ashworth (Apr 28 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807324):
the setup starts at line 269

#### [Johan Commelin (Apr 28 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807367):
I have the instinctive feeling that this is related, but somewhat different from what we are discussing.

#### [Kevin Buzzard (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807370):
I guess I understand much less of this part of int.nat than I remembered

#### [Kevin Buzzard (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807375):
what is all this rel stuff?

#### [Johan Commelin (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807378):
But maybe I don't get what this part of the file is trying to prove

#### [Kevin Buzzard (Apr 28 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807437):
I see.

#### [Kevin Buzzard (Apr 28 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807439):
`rel_int_nat_nat (z : int)`

#### [Kevin Buzzard (Apr 28 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807442):
is the set of pairs (a,b) in nat x nat

#### [Kevin Buzzard (Apr 28 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807446):
such that a - b = z

#### [Kevin Buzzard (Apr 28 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807447):
so it's the equivalence class

#### [Johan Commelin (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807486):
@**Andrew Ashworth** Are you saying: there is a ring structure on a quotient of `nat \times nat` and there is a bijection between `Z` and this quotient. And this is how we transfer the ring structure onto `Z`

#### [Johan Commelin (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807487):
Is that what is going on?

#### [Johan Commelin (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807489):
I think it is. And if so, that is a perfect example.

#### [Kevin Buzzard (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807490):
So there's all this rel stuff

#### [Kevin Buzzard (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807492):
and suddenly there are some transfer tactics and it's all over.

#### [Kevin Buzzard (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807493):
Who wrote that stuff?

#### [Andrew Ashworth (Apr 28 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807494):
johannes hoezl

#### [Johan Commelin (Apr 28 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807499):
```quote
Who wrote that stuff?
```
`git blame`

#### [Johan Commelin (Apr 28 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807501):
https://github.com/leanprover/lean/blame/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/data/int/basic.lean#L393

#### [Johan Commelin (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807543):
Andrew, so now, we want to abstract this notion of transfer, and automatically derive it for lots of structures, given equivalences between types.

#### [Kevin Buzzard (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807544):
I see

#### [Kevin Buzzard (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807545):
Maybe he has something to say about what it means to be canonically isomorphic.

#### [Kevin Buzzard (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807546):
Johannes introduced the transfer method

#### [Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807594):
Scott introduced this class with this cool `transportable` name and I've spent some time over the last 24 hours (I should probably sleep at some point) creating instances of this class and moving them around.

#### [Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807597):
What started me off was Johan's list of levels

#### [Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807600):
If we have a more general idea

#### [Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807601):
do we have another game to play?

#### [Kevin Buzzard (Apr 28 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807647):
Johan -- here's how to catch an instance of the type class resolution system

#### [Kevin Buzzard (Apr 28 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807648):
```
theorem T {α : Type u} [ring α] : add_group α := by apply_instance 
#print T
```

#### [Kevin Buzzard (Apr 28 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807654):
`apply_instance` is a tactic which tries to solve things by type class inference

#### [Johan Commelin (Apr 28 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807659):
Ok, let me think about how that might be useful

#### [Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807683):
Unfortunately I don't think we have an instance of `transportable add_group` yet

#### [Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807701):
Kenny wrote the ring one

#### [Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807702):
and one could copy

#### [Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807706):
These maps are in general forgetful functors

#### [Reid Barton (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807707):
I think you would just delete all the lines which don't appear in `add_group`, yeah.

#### [Reid Barton (Apr 28 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807708):
Then I guess your square involving forgetful functors and transported equivalences ought to commute definitionally

#### [Kevin Buzzard (Apr 28 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807716):
```
@[instance, priority 100]
def add_comm_group.to_add_group : Π (α : Type u) [s : add_comm_group α], add_group α :=
λ (α : Type u) [s : add_comm_group α],
  {add := add_comm_group.add s,
   add_assoc := _,
   zero := add_comm_group.zero α s,
   zero_add := _,
   add_zero := _,
   neg := add_comm_group.neg s,
   add_left_neg := _}
```

#### [Kevin Buzzard (Apr 28 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807717):
I am sure it will

#### [Kevin Buzzard (Apr 28 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807758):
A different class of instance is the following:

#### [Kevin Buzzard (Apr 28 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807771):
Wait

#### [Kevin Buzzard (Apr 28 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807772):
this fails:

#### [Kevin Buzzard (Apr 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807803):
```lean
theorem T {α : Type u} {β : Type v} [group α] [group β] :
group α × β := by apply_instance 
```

#### [Kevin Buzzard (Apr 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807814):
I was assuming "product of groups is a group" would be there

#### [Kevin Buzzard (Apr 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807815):
Maybe it's in mathlib

#### [Reid Barton (Apr 28 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807912):
I think you're talking about instances like
```lean
instance blah [ring t] : some_other_thing t := ...
```

#### [Reid Barton (Apr 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807968):
Which is essentially just some arbitrary user-defined function `ring t \to some_other_thing t`

#### [Reid Barton (Apr 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808150):
So now your question from earlier becomes whether an arbitrary function of type `Π α : Type, ring α → add_comm_group α` will commute with the equivalences `ring α ≃ ring β`, `add_comm_group α ≃ add_comm_group β` obtained by transportation of structure along an equivalence `α ≃ β`.  The answer is (probably) that it is true for every function you can define in Lean, but you can't prove it as a theorem within Lean that applies to an arbitrary function. This is parametricity again

#### [Johan Commelin (Apr 28 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808311):
Ok, and now we need some magic to automaticlly prove it for every function that we define.

#### [Johan Commelin (Apr 28 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808314):
And then we don't care that we can't prove it for arbitrary functions. And we don't have to repeat ourselves in dozens of tiny variations.

#### [Kevin Buzzard (Apr 28 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808358):
Here's an instance for "product of groups is a group"

#### [Kevin Buzzard (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808359):
```lean
definition prod_group (G : Type u) (H : Type v) [HG : group G] [HH : group H] : group (G × H) :=
{ mul := λ ⟨g1,h1⟩ ⟨g2,h2⟩, ⟨g1 * g2,h1 * h2⟩,
  mul_assoc := λ ⟨g1,h1⟩ ⟨g2,h2⟩ ⟨g3,h3⟩,prod.ext.2 ⟨mul_assoc _ _ _,mul_assoc _ _ _⟩, 
  one := ⟨HG.one,HH.one⟩,
  one_mul := λ ⟨g,h⟩, prod.ext.2 ⟨one_mul _,one_mul _⟩,
  mul_one := λ ⟨g,h⟩, prod.ext.2 ⟨mul_one _,mul_one _⟩,
  inv := λ ⟨g,h⟩, ⟨group.inv g,group.inv h⟩,--begin end,--λ ⟨g,h⟩, ⟨HG.inv g,HH.inv h⟩,
  mul_left_inv := λ ⟨g,h⟩, prod.ext.2 ⟨mul_left_inv g,mul_left_inv h⟩
}
```

#### [Reid Barton (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808360):
Yes, though it doesn't sound very easy, because the meta-level argument is some induction over the definition of the function, and I'm not sure whether a tactic even has access to the syntactic definition of a function

#### [Reid Barton (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808365):
Maybe Mario could comment when he reappears

#### [Johan Commelin (Apr 28 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808463):
```quote
I'm not sure whether a tactic even has access to the syntactic definition of a function
```
Right. This is the important question. If one of the Lean experts could help out, that would be awesome.

#### [Scott Morrison (Apr 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808787):
Yes, in the tactic world we can look at the syntactic definitions of things.

#### [Scott Morrison (Apr 28 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808826):
It's all just `expr`s.

#### [Mario Carneiro (Apr 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125813008):
Geez, you guys work too fast. I was going to say as a followup to my last post that parametricity is not as simple as `transportable`, and it seems like you are already running into its limitations. The problem is that it only works for unary type operators `Type u -> Type v`, but for the induction to work you need a parametricity statement for many different sorts of higher order type operators. For example, a `Type -> Type -> Type` operator is parametric if whenever `A ~= A'` and `B ~= B'` then `F A B ~= F A B`. A `(Type -> Type) -> Type` operator is parametric if whenever `F` and `F'` are such that `A ~= A'` implies `F A ~= F' A'`, then `G F ~= G F'`.

There is some recursive definition of parametric that goes over the type of the higher-order functor, but you can't even define this recursion in lean since `Type` is not inductively generated by the Pi type and other stuff. But you can define tactics that produce such definitions, and tactics that prove that everything you care about satisfy its appropriate parametricity theorem. This is what "Theorems for free!" is about.

#### [Mario Carneiro (Apr 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125813265):
Also, in the presence of `choice` parametricity fails, so it's not actually true that all lean-definable terms are parametric. For example, given choice you have that everything is decidable, in particular type equality, so you can make definitions like `if x = nat then nat else empty` which is nonempty on `nat` and empty on `int` even though `nat ~= int`.

#### [Mario Carneiro (Apr 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125813314):
Or at least, that would be a counterexample if you knew `nat != int`. This comes back to the possible consistency of `A ~= B -> A = B`; assuming it's consistent with lean `nat != int` is not provable, although there are certainly models of lean which refute `nat = int`.

#### [Johan Commelin (Apr 28 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125819688):
@**Scott Morrison** There you have your counterexample.

#### [Kevin Buzzard (Apr 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820700):
I am not interested in weird questions about whether int is equal to nat.

#### [Kevin Buzzard (Apr 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820703):
It seems to me that a canonical isomorphism is a pair of things

#### [Kenny Lau (Apr 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820705):
I don't remember anyone asking your opinion :P

#### [Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820706):
firstly an equiv

#### [Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820707):
:-)

#### [Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820710):
and secondly a promise

#### [Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820714):
and the promise is that you promise not to do stuff which isn't respected by the equiv

#### [Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820716):
And in ZFC this promise is brushed under the carpet and there is a gentleman's agreement

#### [Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820756):
and all good mathematicians are aware of the agreement

#### [Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820760):
But in dependent type theory we have a bunch of uncultured computer scientists

#### [Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820761):
who don't know our gentlemanly ways

#### [Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820763):
and they are asking to see more details of the promise

#### [Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820764):
and what is worse

#### [Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820768):
they are demanding that we keep our promises.

#### [Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820772):
They are not buying the argument that we are gentlemen who keep our promises

#### [Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820773):
they want to see proof

#### [Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820777):
so now it is the mathematician's job to give them that proof.

#### [Kevin Buzzard (Apr 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820819):
There is a wonderful story which goes back to a paper by Dick Gross in the early 1990s which was crucial in Wiles' original proof of Fermat's Last Theorem

#### [Kenny Lau (Apr 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820820):
```quote
But in dependent type theory we have a bunch of uncultured computer scientists
```
right. you just said this in front of a bunch of computer scientists.

#### [Kevin Buzzard (Apr 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820823):
Kenny: my provocative language is intentional

#### [Kevin Buzzard (Apr 28 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820829):
I am trying to isolate what I believe is an important issue

#### [Kevin Buzzard (Apr 28 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820831):
and I am using provocative language in an attempt to explain it and to get people interested in it.

#### [Kevin Buzzard (Apr 28 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820832):
The story is that Dick Gross needed to analyse two cohomology groups

#### [Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820872):
and these cohomology groups were coming from two completely different cohomology theories

#### [Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820874):
but someone had written down a map between them which was completely natural and depended on no choices

#### [Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820876):
and they had proved that this map was an isomorphism

#### [Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820877):
and had asserted that it was a canonical isomorphism

#### [Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820879):
and we all believed them

#### [Kevin Buzzard (Apr 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820885):
And Dick Gross needed to use some extra structure on these cohomology theories

#### [Kevin Buzzard (Apr 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820887):
each of the cohomology theories came with a bunch of linear maps called Hecke operators

#### [Kevin Buzzard (Apr 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820890):
which are completely canonically defined operators

#### [Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820941):
and Gross asserted without proof that the canonical isomorphism identified the canonically-defined actions of the Hecke operators on each of the theories

#### [Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820943):
and the referee was Jean-Pierre Serre

#### [Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820944):
and he caught this

#### [Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820945):
and he demanded that Gross prove it

#### [Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820948):
and this would have held up publication of this important paper for probably quite some time

#### [Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820949):
so Gross said no

#### [Kevin Buzzard (Apr 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820958):
and instead he wrote in the introduction to his paper that his theorem depended on unchecked compatibilities between canonically defined operators on canonically isomorphic objects

#### [Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820999):
And Brian Conrad got a student of his to work out the details and the student wrote an entire PhD thesis checking that the diagrams did indeed commute

#### [Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821000):
because the proof was by no means formal

#### [Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821001):
and I am now wondering

#### [Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821002):
whether actually

#### [Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821005):
one could write a tactic to prove that theorem

#### [Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821006):
That would be an extraordinary project

#### [Kevin Buzzard (Apr 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821009):
because that would be a computer not only checking the main result of a Stanford student's PhD thesis

#### [Kevin Buzzard (Apr 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821013):
it would be a computer program which automatically generated the main result of a Stanford student's PhD thesis.

#### [Kevin Buzzard (Apr 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821014):
A _mathematics_ student.

#### [Kevin Buzzard (Apr 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821053):
And the reason a tactic might be able to prove this

#### [Kevin Buzzard (Apr 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821054):
would be that when you prove that various maps are isomorphisms

#### [Kevin Buzzard (Apr 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821055):
you don't just say "they are canonical"

#### [Kevin Buzzard (Apr 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821056):
you write down what you mean, properly

#### [Kevin Buzzard (Apr 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821063):
and then you check that all the operations that you do respect the canonical maps

#### [Kevin Buzzard (Apr 28 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822241):
OK so here is a challenge to the mathematics / computer science community:

#### [Kevin Buzzard (Apr 28 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822282):
write a tactic which proves that Gross' canonically defined Hecke operators on his canonically isomorphic spaces all match up with each other

#### [Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822286):
That sounds like a really fun project

#### [Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822290):
because it will need a mix of genuinely deep mathematics

#### [Kenny Lau (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822291):
for M1R?

#### [Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822292):
and clever programming

#### [Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822293):
Kenny, that would be a great first year project :-)

#### [Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822295):
It would be an even better PhD project.

#### [Simon Hudon (Apr 28 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125826517):
```quote
```quote
But in dependent type theory we have a bunch of uncultured computer scientists
```
right. you just said this in front of a bunch of computer scientists.
```
I'm not sure if it's that I'm too uncultured to be insulted but it feels like Kevin paid the CS / formal methods community a beautiful compliment

#### [Johan Commelin (Apr 28 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125827355):
@**Kevin Buzzard** I love this story!

#### [Johan Commelin (Apr 28 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125827363):
Is this story only oral folklore? Or is there some written version (besides what you just wrote down in the chat)? I would love to be able to point others towards this story

#### [Kevin Buzzard (Apr 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831766):
just google for Bryden Cais' PhD thesis

#### [Kevin Buzzard (Apr 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831768):
I think it would be an absolutely monumental challenge to get a computer to prove it

#### [Kevin Buzzard (Apr 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831809):
but anyone who tried would probably learn a lot about what a mathematician means when they say something is canonical

#### [Kevin Buzzard (Apr 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831813):
Bryden is in AZ now

#### [Kevin Buzzard (Apr 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831822):
and go from there to Dick Gross' paper

#### [Kevin Buzzard (Apr 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831862):
and see the explanation about the unchecked compatibilities, a throw-away "well this is not 100% rigorous" admission in a paper which a few years later was to play a fundamental role in Wiles' proof of Fermat's Last Theorem.

#### [Kevin Buzzard (Apr 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831863):
And mathematicans worried not one jot

#### [Kevin Buzzard (Apr 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831864):
See Wiles' FLT paper and verify it references Gross' paper.

#### [Kevin Buzzard (Apr 28 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831872):
perhaps because one day we knew a computer would come along and check the details.

#### [Kevin Buzzard (Apr 28 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831918):
I bet Taylor-Wiles (the paper that fills in the gap) references the paper too.

#### [Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831926):
Absolutely wonderful.

#### [Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831927):
I just checked.

#### [Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831928):
http://www.math.ias.edu/~rtaylor/hecke.pdf

#### [Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831931):
Seminal paper by Taylor and Wiles filling in the gap in Wiles' proof of Fermat's Last Theorem.

#### [Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831933):
Theorem: We fill in a gap.

#### [Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831935):
Footnote: WARNING : paper contains gap

#### [Kevin Buzzard (Apr 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831980):
but we're not worried about that one

#### [Kevin Buzzard (Apr 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831986):
And there was me thinking we were doing ZFC

#### [Kevin Buzzard (Apr 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831987):
When did we stop?

#### [Kevin Buzzard (Apr 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832031):
Bryden Cais thesis 2007, 12 years after FLT proved.

#### [Kevin Buzzard (Apr 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832033):
You know what, I am pretty sure that the experts knew that there was a way around Gross' problems.

#### [Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832036):
So probably nobody made a fuss

#### [Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832040):
they only occurred in certain "higher weight" situations

#### [Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832042):
and the applications to FLT may not need that level of generality

#### [Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832043):
but I'm not sure you'll find a published explanation of this

#### [Kevin Buzzard (Apr 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832083):
I'll ask Conrad whether he thinks his student proved Fermat's Last Theorem

#### [Scott Morrison (Apr 29 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125834143):
@**Johan Commelin** ,
```quote
@**Scott Morrison** There you have your counterexample.
```
I haven't quite caught up on this thread, but does this mean that "in the presence of `choice` I owe @**Mario Carneiro**  a beer"? Ok, I'll honour that anyway.

#### [Reid Barton (Apr 29 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839073):
Do we have parametricity for things which are not `noncomputable`?

#### [Kevin Buzzard (Apr 29 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839370):
I will remark that the thing I want to prove is functorial, is noncomputable.

#### [Kevin Buzzard (Apr 29 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839420):
attempting to make it computable would not be a question I was that interested in

#### [Kevin Buzzard (Apr 29 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839421):
but I am unsure as to whether or not it can be done. This goes back to the old question of how to represent the functions on a standard open in an affine scheme

#### [Johan Commelin (Apr 29 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125846328):
@**Scott Morrison** I guess so... you didn't post any formal requirements, and I am not a judge (-;

#### [Kevin Buzzard (Apr 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854648):
Church numerals are kind of cool

#### [Kenny Lau (Apr 29 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854656):
what is that message related to?

#### [Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854697):
https://github.com/kbuzzard/xena/blob/06476597bd53a111bb3060d2d583e04c972d5204/canonical_isomorphism/church_blog_questions.lean

#### [Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854698):
Kenny, there are some more challenges for you

#### [Kenny Lau (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854699):
nice, i love challenges

#### [Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854700):
I'm sure you won't have much trouble with succ, add and mul

#### [Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854701):
do you know how to do pow?

#### [Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854702):
And what about Ackermann?

#### [Kenny Lau (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854707):
oh i thought you were talking about those proofs in your file

#### [Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854708):
And can you prove the equiv?

#### [Kenny Lau (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854709):
they aren't equivalent

#### [Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854710):
The link I just posted is to a file with some sorries

#### [Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854711):
but I can fill in some of the sorries

#### [Kenny Lau (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854712):
they aren't provable

#### [Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854713):
stop

#### [Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854714):
some are provable because I proved them

#### [Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854715):
you need to look at the file

#### [Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854752):
for each sorry in the file, either fill it in, or tell me confidently that it cannot be filled in

#### [Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854755):
that's your challenge

#### [Kenny Lau (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854756):
ok

#### [Kenny Lau (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854757):
I saw the word blog :D

#### [Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854758):
yes, I am going to write another blog post

#### [Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854760):
talking of blog posts

#### [Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854761):
I have a file which is both beautiful and disgusting

#### [Kevin Buzzard (Apr 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854767):
beautiful because all the proofs are really uncluttered

#### [Kenny Lau (Apr 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854768):
that tone in `KB doesn't understand` though lmao

#### [Kevin Buzzard (Apr 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854769):
disgusting because I use constants

#### [Kevin Buzzard (Apr 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854814):
Kenny -- is nat some inductive type which is somehow canonically associated to the Pi type of church numerals?

#### [Kevin Buzzard (Apr 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854815):
look at my definition of `to_nat`

#### [Kevin Buzzard (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854816):
it takes all the ingredients of nat exactly once, and nothing more

#### [Kenny Lau (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854821):
sure, `Π X : Type, (X → X) → X → X` is the Church encoding of the type `nat`

#### [Kevin Buzzard (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854822):
I don't know what that means

#### [Kevin Buzzard (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854823):
which types have a church encoding?

#### [Kenny Lau (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854824):
inductive types I guess

#### [Kenny Lau (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854825):
not very sure

#### [Kenny Lau (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854826):
maybe pi types as well

#### [Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854865):
so you cannot formalise the assertion you just made?

#### [Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854866):
You are making some informal statement?

#### [Kenny Lau (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854867):
I don't know everything about church encoding

#### [Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854868):
but is there some rigorous statement that an expert can make?

#### [Kenny Lau (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854869):
I believe so

#### [Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854870):
"church encoding" has a formal definition?

#### [Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854876):
What is the church encoding of a scheme?

#### [Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854877):
what is the church encoding of int as defined in Lean?

#### [Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854878):
what is the church encoding of list?

#### [Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854879):
what is the church encoding of bool?

#### [Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854880):
what is the church encoding of false?

#### [Kenny Lau (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854881):
```quote
what is the church encoding of bool?
```
`X -> X -> X` :P

#### [Kenny Lau (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854918):
```quote
what is the church encoding of false?
```
`X`

#### [Kevin Buzzard (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854921):
Does the church encoding of anything just have one type X?

#### [Kenny Lau (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854922):
```quote
Does the church encoding of anything just have one type X?
```
didn't I just answer that question

#### [Kevin Buzzard (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854923):
No

#### [Kevin Buzzard (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854924):
you only answered it for bool and false

#### [Kevin Buzzard (Apr 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854930):
and nat

#### [Kenny Lau (Apr 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854931):
what do you mean by one type X?

#### [Kevin Buzzard (Apr 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854932):
I mean that all your answers so far (for nat, bool and false) only had one letter in

#### [Kenny Lau (Apr 29 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854972):
oh, I misunderstood "anything"

#### [Kenny Lau (Apr 29 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854973):
english ~

#### [Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855019):
did you do ack yet?

#### [Kenny Lau (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855020):
I've been searching church encoding online

#### [Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855021):
here's a much easier

#### [Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855022):
one

#### [Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855023):
`pred`

#### [Kevin Buzzard (Apr 29 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855028):
The untyped lambda calculus is so last year

#### [Kevin Buzzard (Apr 29 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855030):
I want to know how it works in Lean

#### [Kevin Buzzard (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855068):
although these questions might not be good for this thread, because did you say that it was not true that nat was equiv to church nat?

#### [Kevin Buzzard (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855071):
or not provable?

#### [Kenny Lau (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855072):
if your functions are computable, then I believe they will represent some natural number

#### [Kenny Lau (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855075):
but noncomputable functions are permitted in Lean, breaking the equivalence

#### [Kenny Lau (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855076):
(but I can't give you any example :P)

#### [Kevin Buzzard (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855124):
So one can write down a `noncomputable` church nat which is provably not in the image of `of_nat`?

#### [Kenny Lau (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855127):
I don't know

#### [Kenny Lau (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855128):
maybe you can write something like `if X == int then _ else _`

#### [Kevin Buzzard (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855129):
well maybe it won't come up in the mechanics exam

#### [Kenny Lau (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855130):
...

#### [Kenny Lau (Apr 29 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855214):
```quote
what is the church encoding of list?
```
`list A = X -> (A -> X -> X) -> X` I guess. can't find anything online

#### [Kenny Lau (Apr 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855302):
```quote
what is the church encoding of int as defined in Lean?
```
`nat -> nat -> X`, I guess

#### [Kevin Buzzard (Apr 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855303):
that doesn't look like something that Church would like

#### [Kevin Buzzard (Apr 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855304):
it has something in which isn't X

#### [Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855309):
or -> or ()

#### [Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855311):
Is it OK?

#### [Kenny Lau (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855313):
but `list` isn't a type

#### [Kenny Lau (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855314):
`list` is a function from types to types

#### [Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855315):
I see

#### [Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855317):
I thought those were types too ;-)

#### [Kevin Buzzard (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855354):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean

#### [Kenny Lau (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855356):
```lean
#check list
--list : Type u_1 → Type u_1
```

#### [Kevin Buzzard (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855358):
I slightly updated the church numerals file

#### [Kevin Buzzard (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855359):
I am a bit unclear about what is provable and what isn't.

#### [Kevin Buzzard (Apr 29 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855364):
I also have a file with some solutions in

#### [Kevin Buzzard (Apr 29 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855370):
and the only reason I did not push it

#### [Kevin Buzzard (Apr 29 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855372):
is because the definition of `pow` on church nats is so beautiful that I wanted to let you find it if you hadn't seen it already

#### [Kenny Lau (Apr 29 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856002):
interesting

#### [Kevin Buzzard (Apr 29 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856248):
I am finally trying to write down a "canonical isomorphism" proof of the result I need to apply Chris' Lemma to the affine scheme boss

#### [Kevin Buzzard (Apr 29 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856249):
Does this structure already have a name?

#### [Kevin Buzzard (Apr 29 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856250):
```lean
structure is_unique_ring_hom {α : Type v} {β : Type w} [ring α] [ring β] (f : α → β) [is_ring_hom f] : Prop :=
(is_unique : ∀ (g : α → β) [is_ring_hom g], g = f)
```

#### [Kevin Buzzard (Apr 29 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856294):
```lean
class is_ring_hom {α : Type u} {β : Type v} [ring α] [ring β] (f : α → β) : Prop :=
(map_add : ∀ {x y}, f (x + y) = f x + f y)
(map_mul : ∀ {x y}, f (x * y) = f x * f y)
(map_one : f 1 = 1)
```

#### [Kevin Buzzard (Apr 29 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856305):
(sorry, I was half rings and half commutative rings)

#### [Kevin Buzzard (Apr 29 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856306):
(I am all rings now)

#### [Kenny Lau (Apr 29 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856635):
I don't think it has a name

#### [Kenny Lau (Apr 29 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858145):
https://github.com/kckennylau/Lean/blob/master/church_blog_questions.lean

#### [Kenny Lau (Apr 29 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858173):
@**Kevin Buzzard** I don't think Ack can be done

#### [Kevin Buzzard (Apr 29 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858640):
What is your opinion of the other `sorry`s?

#### [Kenny Lau (Apr 29 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858642):
can't be done

#### [Kevin Buzzard (Apr 29 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858654):
Are there any for which you feel that you can convince me rigorously that they can't be done?

#### [Kenny Lau (Apr 29 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858655):
the last one, I think

#### [Kevin Buzzard (Apr 29 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858697):
`theorem is_it_true (X : Type) (f : X → X) (x : X) : f x = x := sorry`

#### [Kevin Buzzard (Apr 29 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858700):
that theorem looks really appealing to me

#### [Kenny Lau (Apr 29 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858703):
I think you want `f : \Pi X : Type, X \to X`

#### [Kevin Buzzard (Apr 29 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859158):
```lean
-- bad church numeral
local attribute [instance] classical.prop_decidable
noncomputable definition satan (X : Type) (f : X → X) (x : X) := dite (X = ℕ) (λ H,begin show X,rw H,rw H at x,exact x end) (λ _,f x)
#check (satan : chℕ) -- 1 everywhere apart from nat, where it's zero

theorem satan_is_bad : of_nat (to_nat satan) = satan → false :=
begin
intro H,
have H2 : (of_nat (to_nat satan)) bool bnot tt = satan bool bnot tt := by rw H,
-- now what?
sorry
end 
```

#### [Kevin Buzzard (Apr 29 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859159):
Trying to write down a counterexample

#### [Kenny Lau (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859165):
aha, I used `==` and I failed

#### [Kenny Lau (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859169):
turns out you need `=` instead

#### [Kevin Buzzard (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859170):
well, it typechecks

#### [Kevin Buzzard (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859171):
but it's not over yet

#### [Kevin Buzzard (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859172):
unless you see that it's over

#### [Kenny Lau (Apr 29 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859211):
so what is your thought and why are you stuck?

#### [Kevin Buzzard (Apr 29 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860599):
well presumably now I have to prove things like bool ne nat

#### [Kenny Lau (Apr 29 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860603):
oh I thought you can just feed in `bool` to both sides

#### [Kenny Lau (Apr 29 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860604):
and have one side give `ff` and the other side give `tt`

#### [Kevin Buzzard (Apr 29 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860693):
```lean
theorem satan_is_bad : of_nat (to_nat satan) = satan → false :=
begin
intro H,
have H2 : (of_nat (to_nat satan)) bool bnot tt = satan bool bnot tt := by rw H,
unfold to_nat at H2,
unfold satan at H2,
simp at H2,
change tt = _ at H2,
-- H2 : tt = dite (bool = ℕ) (λ (H : bool = ℕ), eq.mpr _ (eq.mp _ tt)) (λ (_x : ¬bool = ℕ), ff)
-- now what?
sorry
end 
```

#### [Kevin Buzzard (Apr 29 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860695):
if only I had a good destructor for dite

#### [Kenny Lau (Apr 29 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860700):
oh, you need to prove that `bool` and `nat` are not equal lol

#### [Kevin Buzzard (Apr 29 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860701):
exactly

#### [Kenny Lau (Apr 29 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860741):
cardinality :rolling_on_the_floor_laughing:

#### [Kevin Buzzard (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860751):
```lean
theorem satan_is_bad : of_nat (to_nat satan) = satan → false :=
begin
intro H,
have H2 : (of_nat (to_nat satan)) bool bnot tt = satan bool bnot tt := by rw H,
unfold to_nat at H2,
unfold satan at H2,
simp at H2,
change tt = _ at H2,
suffices : ¬ (bool = ℕ),
simp [this] at H2,assumption,
-- ⊢ ¬bool = ℕ
sorry
end 
```

#### [Kevin Buzzard (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860752):
Indeed it's the only problem left

#### [Kenny Lau (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860753):
if they're equal then their cardinality is equal

#### [Kenny Lau (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860754):
but bool is finite

#### [Kevin Buzzard (Apr 29 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860756):
can you do it?

#### [Kenny Lau (Apr 29 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860795):
heh...

#### [Kevin Buzzard (Apr 29 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860798):
`example : ¬bool = ℕ := sorry`

#### [Kenny Lau (Apr 29 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860850):
tactic mode slows things down

#### [Reid Barton (Apr 29 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125861579):
It would be a lot easier if you changed `bool` to `empty`

#### [Kenny Lau (Apr 29 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125861595):
hmm

#### [Kenny Lau (Apr 29 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125861598):
maybe we should use `false` instead

#### [Kevin Buzzard (Apr 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862258):
the proof crucially uses "this map X -> X is not this other map"

#### [Kevin Buzzard (Apr 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862261):
so I can't see how we can use empty or false :-/

#### [Kevin Buzzard (Apr 29 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862304):
but we can use any type which is provably not \N and which provably has a map which is not the identity map

#### [Reid Barton (Apr 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862356):
Oh I see, sorry

#### [Kenny Lau (Apr 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862365):
I have never proved that two types are not the same

#### [Kevin Buzzard (Apr 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862409):
I think there is some notion of finite and infinite, and it will be known that bool is finite and nat is infinite

#### [Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862410):
of course a = b implies a equiv b

#### [Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862415):
by rw

#### [Kenny Lau (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862416):
```quote
by rw
```
**by `eq.rec_on`**

#### [Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862427):
that's what I said

#### [Kenny Lau (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862429):
:P

#### [Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862430):
:-)

#### [Reid Barton (Apr 29 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862640):
As a further step, you could try adding the "free theorem" for the type `Π X : Type, (X → X) → X → X` as a field of your church numerals and then see if you can prove `of_nat (to_nat c) = c`

#### [Chris Hughes (Apr 29 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863436):
```lean
import data.set.finite

example : bool ≠ ℕ := λ h, 
by haveI : fintype ℕ := eq.rec_on h (by apply_instance);
exact set.not_injective_nat_fintype @nat.succ_inj
```

#### [Kenny Lau (Apr 29 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863443):
lol

#### [Chris Hughes (Apr 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863503):
Not very often you get to use `eq.rec_on` for something that's not a prop.

#### [Kenny Lau (Apr 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863505):
it is a prop

#### [Chris Hughes (Apr 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863554):
`fintype` isn't

#### [Kenny Lau (Apr 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863556):
oh, I misunderstood

#### [Kenny Lau (Apr 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863558):
your proof makes me laugh for some reason

#### [Kevin Buzzard (Apr 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863615):
```lean
theorem satan_is_bad : of_nat (to_nat satan) = satan → false :=
begin
intro H,
have H2 : (of_nat (to_nat satan)) bool bnot tt = satan bool bnot tt := by rw H,
unfold to_nat at H2,
unfold satan at H2,
simp at H2,
change tt = _ at H2,
suffices : ¬ (bool = ℕ),
simp [this] at H2,assumption,
exact bool_not_nat,
end 
```

#### [Kevin Buzzard (Apr 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863618):
so it really is not provable

#### [Kenny Lau (Apr 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863622):
nice!

#### [Chris Hughes (Apr 29 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863668):
What's satan?

#### [Kenny Lau (Apr 29 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863675):
```lean
noncomputable definition satan (X : Type) (f : X → X) (x : X) := dite (X = ℕ) (λ H,begin show X,rw H,rw H at x,exact x end) (λ _,f x)
```

#### [Chris Hughes (Apr 29 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863766):
What's `of_nat`?

#### [Kenny Lau (Apr 29 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863768):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean

#### [Chris Hughes (Apr 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863920):
What's the purpose of church nats?

#### [Kenny Lau (Apr 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863925):
to defeat satan

#### [Kenny Lau (Apr 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863926):
well church numerals is an essential part of lambda calculus

#### [Chris Hughes (Apr 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864023):
Am i doing something wrong
```lean
--KB can't do this one. Is it unprovable? If so, move definition of to_nat much further down.
example (m : chℕ) : to_nat (succ m) = nat.succ (to_nat m) := rfl
```

#### [Kenny Lau (Apr 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864024):
I also used `rfl` lol

#### [Chris Hughes (Apr 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864232):
Is this cheating?
```lean
def add : chℕ → chℕ → chℕ := λ a b, of_nat (to_nat a + to_nat b)
```

#### [Kenny Lau (Apr 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864240):
yes it is

#### [Chris Hughes (Apr 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864756):
Stuck on add_succ

#### [Kenny Lau (Apr 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864757):
you can do it

#### [Chris Hughes (Apr 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864775):
Is it even true? There are loads of chnats that aren't constructed from naturals.

#### [Kenny Lau (Apr 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864776):
it is true

#### [Chris Hughes (Apr 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864913):
Are you sure `add_succ` is true? `succ_add` certainly is. I think it's the wrong approach to try to prove that.

#### [Kenny Lau (Apr 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864952):
depends on your definition of add

#### [Chris Hughes (Apr 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865010):
` λ a b X f, (a X f) ∘ (b X f)`

#### [Kenny Lau (Apr 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865013):
then destruct `a`

#### [Chris Hughes (Apr 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865054):
I proved of_nat_add without it, so I'm okay.

#### [Chris Hughes (Apr 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865060):
I ended up with this
```
m n : chℕ,
X : Type,
f : X → X,
x : X
⊢ m X f (f (n X f x)) = f (m X f (n X f x))
```

#### [Kenny Lau (Apr 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865063):
what is the theorem?

#### [Chris Hughes (Apr 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865243):
 m + succ n = succ (m + n)

#### [Kenny Lau (Apr 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865246):
oh...

#### [Kenny Lau (Apr 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865249):
sorry

#### [Kenny Lau (Apr 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865253):
I thought it was one of the questions from the file and then I reflexively answered that it's true

#### [Kevin Buzzard (Apr 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865379):
Apparently defining pred is interesting

#### [Chris Hughes (Apr 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865486):
pretty sure `add_comm` isn't true. all you need is two functions whose composition doesn't commute surely?

#### [Chris Hughes (Apr 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865785):
Just disproved `add_comm`

#### [Kenny Lau (Apr 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865788):
nice!

#### [Kevin Buzzard (Apr 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865903):
the problem is that a church numeral has to be defined on every type

#### [Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865910):
If you were to specialise to one specific type X then they won't commute

#### [Kenny Lau (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865915):
the problem is that noncomputable functions exist

#### [Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865916):
right

#### [Kenny Lau (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865922):
now I haven't even started dinner and you have already finished it

#### [Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865924):
also right

#### [Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865927):
but I have a lot of tidying up to do

#### [Kenny Lau (Apr 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865967):
heh

#### [Chris Hughes (Apr 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866020):
```quote
the problem is that a church numeral has to be defined on every type
If you were to specialise to one specific type X then they won't commute
```
What do you mean?

#### [Chris Hughes (Apr 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866185):
I fixed has_pow `instance : has_pow chℕ chℕ := ⟨pow⟩`

#### [Kevin Buzzard (Apr 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866347):
I mean that you can't say "I can think of a type X and two functions f and g which don't commute, so done", because a church numeral is defined on all types

#### [Kevin Buzzard (Apr 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866350):
But of course if you do the trick I did then this gets round it, at a cost of making the function noncomputable

#### [Chris Hughes (Apr 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866405):
You can.
```lean
lemma not_add_comm : ∃ a b : chℕ, a + b ≠ b + a := 
⟨λ X f x, dite (ℕ = X) (λ h, eq.rec_on h (nat.succ (eq.rec_on h.symm x : ℕ))) (λ _, x),
λ X f x, dite (ℕ = X) (λ h, eq.rec_on h (2 * (eq.rec_on h.symm x : ℕ))) (λ _, x),
λ h,
begin
  have := congr_fun h ℕ,
  have := congr_fun this id,
  have := congr_fun this 0,
  simp [has_add.add, add] at this,
  exact absurd this dec_trivial,
end⟩
```
Are you saying that the definition is not correct?

#### [Chris Hughes (Apr 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866797):
Or maybe my definition of add is incorrect.

#### [Chris Hughes (Apr 29 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867627):
I disproved `free_chnat` as well
```lean
theorem free_chnat : ¬∀ (A B : Type), ∀ f : A → B, 
∀ r : chℕ, ∀ a : A, r (A → B) (λ g, f) f a = r (A → B) (λ g, g) f a 
 := λ h, begin
 let r : chℕ := (λ X f x, dite ((ℕ → ℕ) = X) (λ h, eq.rec_on h 
    (let f : (ℕ → ℕ) → (ℕ → ℕ) := eq.rec_on h.symm f in 
    ite (f = id) id nat.succ)) (λ _, x)),
  have := (h ℕ ℕ id r 8),
  have h₁ : (λ (g : ℕ → ℕ), id) ≠ id := λ h, absurd (congr_fun (congr_fun h nat.succ) 0) dec_trivial,
  have h₂ : (λ (g : ℕ → ℕ), g) = id := rfl,
  simp [r, id, h₁, h₂] at this,
  exact absurd this dec_trivial,
end
```

#### [Kevin Buzzard (Apr 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867731):
yes, those free theorems aren't very good are they

#### [Kevin Buzzard (Apr 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867733):
I would ask for my money back

#### [Kevin Buzzard (Apr 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867740):
The free theorem for `Pi X, X` is: for all X, for all f : X -> X, for all x : X, f x = x :-)

#### [Chris Hughes (Apr 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867742):
Is it because we're defining church numerals as something bigger than those that can be constructed from nats?

#### [Kevin Buzzard (Apr 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867746):
I think constructively it's very difficult to tell the difference between church numerals and numerals

#### [Kevin Buzzard (Apr 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867785):
you have to use this dite trick and make it noncomputable

#### [Chris Hughes (Apr 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867790):
Probably. But that doesn't make the lemmas true. It just makes them undisprovable

#### [Kevin Buzzard (Apr 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867798):
I think that in some other logics they might be provable

#### [Kevin Buzzard (Apr 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867799):
I am certainly not an expert in these variants of the lambda calculus

#### [Kevin Buzzard (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867837):
Chris I have been failing to apply your lemma :-)

#### [Chris Hughes (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867845):
The 00EJ?

#### [Kevin Buzzard (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867846):
yes

#### [Chris Hughes (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867849):
Because of the isomorphism problem?

#### [Kevin Buzzard (Apr 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867856):
I have some situation with a bunch of types each of which are canonically isomorphic to your types that you proved something about

#### [Kevin Buzzard (Apr 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867858):
but I have got distracted

#### [Kevin Buzzard (Apr 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867867):
and am trying to write quite a high-level proof which mirrors how I actually think about the question

#### [Chris Hughes (Apr 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867920):
Did the tactics session get anywhere?

#### [Kevin Buzzard (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867966):
There was a preliminary idea about how to model the notion of being canonically isomorphic

#### [Chris Hughes (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867967):
To make tactics that prove it's a ring?

#### [Kevin Buzzard (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867968):
but then we realised that it wasn't strong enough

#### [Kevin Buzzard (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867980):
and I am now trying to write down some abstract ideas at a high level to see if I can make any sense out of them

#### [Kevin Buzzard (Apr 29 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867989):
It seems to me that when a mathematician says that two things are canonically isomorphic they are making a promise

#### [Chris Hughes (Apr 29 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867990):
I don't understand how it could have been someone's PhD project to prove a result still held for an isomorphic thing

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867993):
the project did something else

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868035):
but this came out in the wash

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868040):
But the problem was hard

#### [Chris Hughes (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868041):
I see.

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868042):
Here was the problem.

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868045):
We have two finite-dimensional vector spaces V and W

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868048):
and we have two linear maps T : V -> V and T' : W -> W

#### [Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868053):
and T and T' are both defined "by using the same sort of ideas"

#### [Kevin Buzzard (Apr 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868059):
but on two different spaces

#### [Kevin Buzzard (Apr 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868069):
and then there's a theorem that there's a "canonical isomorphism" phi from V to W

#### [Kevin Buzzard (Apr 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868070):
which means "an isomorphism which somehow dropped out really nicely"

#### [Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868112):
and what Dick Gross used without proof was that phi (T v) = T' (phi v)

#### [Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868117):
for all v

#### [Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868120):
and his proof was not a formal one

#### [Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868122):
his proof was "this must be true because that's surely how it works"

#### [Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868124):
"because everything is canonical"

#### [Kevin Buzzard (Apr 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868133):
V and W were two different cohomology theories attached to the same space

#### [Kevin Buzzard (Apr 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868143):
and T and T' were defined using some other spaces (the same other spaces for T and T')

#### [Kevin Buzzard (Apr 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868187):
e.g. maps between spaces often induce maps between cohomology theories

#### [Kevin Buzzard (Apr 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868188):
but it was just a case of making sure that all the diagrams commuted

#### [Kevin Buzzard (Apr 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868195):
and some of the definition were done using very abstract algebra and the diagrams were difficult to chase

#### [Simon Hudon (Apr 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868198):
Short digression:

I'm working on deriving `transportable`. Do you guys have a preference between making such instances lemmas (i.e. you can't unfold them) or definitions?

#### [Kevin Buzzard (Apr 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868201):
that's an interesting question Simon

#### [Kevin Buzzard (Apr 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868243):
transportable is what we can transfer equiv over, right?

#### [Simon Hudon (Apr 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868246):
Exactly

#### [Simon Hudon (Apr 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868250):
Here's the class:

```
class transportable (f : Type u → Type v) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))
```

#### [Kevin Buzzard (Apr 29 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868260):
I guess if I had a group on X and an equiv from X to Y I'd definitely like to be able to get at the induced group on Y

#### [Simon Hudon (Apr 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868302):
Ah very good. Right now, the instances I'm generating are kind of messy. I'll try to structure them so that you can look into them then

#### [Kevin Buzzard (Apr 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868306):
but that might be a different question

#### [Kevin Buzzard (Apr 29 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868317):
I am not sure I can give a definitive answer to your question

#### [Simon Hudon (Apr 29 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868319):
If I don't structure them but I make them definitions, you still benefit from defeq

#### [Kevin Buzzard (Apr 29 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868375):
My impression was that for theoretical reasons some people wanted things more general than maps between types to be transportable

#### [Simon Hudon (Apr 29 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868378):
You mean like groups, rings, etc?

#### [Kevin Buzzard (Apr 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868427):
I think the issue raised was that if X and Y were equiv and then X got a group structure, then Y would get a group structure, but if then X got a ring structure on top of that, which induced the group structure, then one would want to push over both the ring structure on Y and the proof that the ring structure on Y reduced to the group structure

#### [Kevin Buzzard (Apr 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868428):
But I am not too worried about this at the minute. We might just want to try a prototype at the minute

#### [Kevin Buzzard (Apr 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868429):
to see if we can get anything working

#### [Kevin Buzzard (Apr 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868438):
I have thought about this a certain amount today. If X and Y have extra structure, e.g. if they're both rings, then there is ring_equiv, which equiv + assumption that the maps are ring isomorphisms

#### [Simon Hudon (Apr 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868440):
Cool. I'm going to push it on a repo on Github before making a PR for mathlib. This way you can play with it and tell me what you need

#### [Kevin Buzzard (Apr 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868481):
And if two things are ring-equiv then you can get some more theorems

#### [Kevin Buzzard (Apr 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868482):
e.g. if something is a module for one ring then it becomes a module for the other ring

#### [Kevin Buzzard (Apr 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868485):
That would not be true if the rings were just equiv

#### [Simon Hudon (Apr 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868492):
That's going to be interesting. I'll have to think on how to do that

#### [Kevin Buzzard (Apr 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868493):
So some wise people made some comments about this earlier

#### [Simon Hudon (Apr 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868496):
```quote
That would not be true if the rings were just equiv
```
Does that mean ring-equiv also asserts that the ring operations respect the underlying isomorphism?

#### [Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868536):
right

#### [Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868539):
If X is a ring

#### [Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868540):
then this means in practice that you have add and mul and neg and one and zero

#### [Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868541):
and all of those transfer

#### [Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868542):
so if you have an equiv X = Y

#### [Simon Hudon (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868543):
Right and you need access to their definitions

#### [Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868549):
then you can transfer them all over from X to Y

#### [Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868552):
On the other hand if X and Y are already rings

#### [Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868553):
and you decide that there's a canonical isomorphism between them

#### [Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868555):
then you're going to have to prove that the add mul neg etc all transfer over from one to the other

#### [Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868556):
and once you've done that, you have a better class of equiv which is specifically for rings

#### [Kevin Buzzard (Apr 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868596):
and you can prove more theorems with it

#### [Kevin Buzzard (Apr 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868604):
each of which is trivial to a mathematician

#### [Kevin Buzzard (Apr 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868610):
such as "oh look, M is a free R-module and R is isomorphic to S so M is now a free S-module"

#### [Kevin Buzzard (Apr 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868661):
or "M is a Noetherian Cohen-Macauley R-module which is R-generated by these three elements and R is isomorphic to S so now M is a Noetherian Cohen-Macauley S-module which is S-generated by these three elements"

#### [Kevin Buzzard (Apr 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868662):
and the definition of Cohen-Macauley is pretty complicated

#### [Kevin Buzzard (Apr 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868663):
but it complies with the unwritten promise

#### [Kevin Buzzard (Apr 30 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868667):
which is that it only depends on the underlying ring up to ring-isomorphism

#### [Kevin Buzzard (Apr 30 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868678):
It seems to me that mathematicians have got a really good intuitive feeling for these promises

#### [Simon Hudon (Apr 30 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868728):
Nice

#### [Simon Hudon (Apr 30 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868774):
Given a structure like group or ring, if you derive `transportable` it gives automatically the isomorphism between the properties of the structures whenever you have an isomorphism between two types

#### [Simon Hudon (Apr 30 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868815):
I'm getting close to a complete derivation and it works with group so far. It will be fun to see you try it with other structures

#### [Mario Carneiro (Apr 30 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125874746):
```quote
The free theorem for `Pi X, X` is: for all X, for all f : X -> X, for all x : X, f x = x :-)
```
That's not correct. You need to quantify over polymorphic functions: for all f : (\forall X, X -> X), for all X, for all x : X, f X x = x

#### [Mario Carneiro (Apr 30 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125874930):
As Kenny and others have noted, the definition of chN is not correct in dependent type theories like lean because there are additional polymorphic functions that are not parametric. However, you can repair the church nat construction by taking a subtype to enforce that the polymorphic functions are functorial. For example, church unit is:
```
def ch_unit := { f : ∀ X : Type, X → X // ∀ (X Y) (g : X → Y) x, f Y (g x) = g (f X x) }
```
Can you see the correct condition for church nat?

#### [Mario Carneiro (Apr 30 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125874995):
By the way, to generate the type of a church encoding, the idea is just look at the recursor for the inductive type. For example, ignoring dependencies in the motive, the type of nat.rec is `∀ C, C → (C → C) → ℕ → C`, so if you move the `ℕ → `to the beginning this is exactly the canonical map from N to chN (and the remainder `∀ C, C → (C → C) → C` is chN itself). (The ordering of the two arguments is not important, and only reflects that `zero` is the first constructor and `succ` is the second.)

#### [Reid Barton (Apr 30 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875260):
@**Simon Hudon**, did you see https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff?

#### [Reid Barton (Apr 30 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875554):
I'm thinking now that having a `class` is problematic because the type of the transport function depends on the parameters of the structure in a way that I don't think can be encoded in a `class` declaration. Plus I don't see any real advantage to having the class anyways. Rather we could just generate definitions `group.transport`, `ring.transport` etc.

#### [Simon Hudon (Apr 30 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875922):
I don't think I see your point

#### [Reid Barton (Apr 30 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875971):
My two messages above are unrelated to each other

#### [Reid Barton (Apr 30 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875978):
so I'm not sure what the point that you don't see is :simple_smile:

#### [Reid Barton (Apr 30 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876020):
The gist is supposed to be an example of what we want to have autogenerated: everything defined by `magic`

#### [Reid Barton (Apr 30 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876032):
But making `group.transportable` be an instance of a class is unnecessary and in general awkward (my gist already contains three classes, and if there are dependencies between the parameters of a structure then things get even more complicated)

#### [Simon Hudon (Apr 30 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876229):
Does your gist illustrate the awkwardness that you're referring to?

#### [Reid Barton (Apr 30 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876246):
To the extent that I already had to define three separate classes `transportable`, `transportable2`, `transportable3`

#### [Reid Barton (Apr 30 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876252):
It doesn't illustrate what happens when there are dependencies between arguments

#### [Simon Hudon (Apr 30 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876298):
But if you don't make them classes you still need to define records, no?

#### [Reid Barton (Apr 30 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876311):
Well the instance called `group.transportable` is only really used as `transport group`, so `transport group` can just be named `group.transport` and no need for a structure.

#### [Reid Barton (Apr 30 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876352):
If we need the `on_refl` and `on_trans` fields then they can be called `group.transport_on_refl` or something

#### [Reid Barton (Apr 30 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876409):
By analogy, there's no class that contains all the `.rec` functions which are defined for inductive types

#### [Simon Hudon (Apr 30 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876510):
I see that you're arguing against the necessity. I don't see any issue with using a class nonetheless. And the upside of having one is that it allows you to generalize lemmas or definitions. It might be that, as you seem to suggest, there's no ground breaking theorems about those classes. It can still allow you to reduce the boilerplate code

#### [Reid Barton (Apr 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876762):
Well at a minimum, you'd need one class per number of type arguments, unless there is a clever way to express `transportable2` in terms of `transportable` twice.

#### [Reid Barton (Apr 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876766):
I'm not entirely sure what should happen when there are dependencies between arguments. https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad shows one possibility. Here `t1_space` has two arguments, a type `α` and a topology on `α`. Since the second argument is not a type, there is no equivalence in that position.

#### [Simon Hudon (Apr 30 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125877059):
Having three separate classes does not seem like much of a problem to me. But you can probably equate `transportable2 f` to `transportable (uncurry f)`, that way, you can use some of the same definitions for both. And for dependent arguments, if it's more trouble than it's worth, you may have a more ad hoc approach (without classes) for those cases.

#### [Mario Carneiro (Apr 30 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125880638):
The range of possible `transportable` classes is unbounded, not just because of things like `transportable2` for other values of 2 but also because of higher order functors like `(Type -> Type) -> Type`, and Pi types like `\forall A, group A -> Type`. If a tactic generated the transportable theorem for a functor, it would need to select the theorem statement from an unbounded class of statements, namely the "free theorems"

#### [Mario Carneiro (Apr 30 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125880688):
You can express `transportable2` in a more modular way, by generalizing `equiv`. Define an `~=` relation on (many) types by induction as follows: If `x y : Type` then `x ~= y` means `equiv x y` (i.e. the usual sense), and if `f g : A -> B` then `f ~= g` iff `\forall x y, x ~= y -> f x ~= g y`. Then `transportable x` means `x ~= x`. This generalizes `transportable2` and `transportable3`, and also yields transportable for `F : (Type -> Type) -> Type`, asserting that if `f ~= g` at `Type -> Type` then `F f ~= F g`.

#### [Kevin Buzzard (Apr 30 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125881912):
```quote
As Kenny and others have noted, the definition of chN is not correct in dependent type theories like lean because there are additional polymorphic functions that are not parametric. However, you can repair the church nat construction by taking a subtype to enforce that the polymorphic functions are functorial.
```
You have put the "free theorem" in with the definition! It really is free now :-)

#### [Kevin Buzzard (Apr 30 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125881965):
If you demand that a church numeral is functorial, then the naturals are a universal object because they are freely generated by `x : X` (zero) and `f : X -> X` (succ), so any church numeral will be determined by its behaviour on the universal object, with proof by a trivial diagram chase.

#### [Kevin Buzzard (Apr 30 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125881967):
And so a church numeral is uniquely determined by what it does on nat, which is precisely the missing theorem for proving the equiv between church nat and nat

#### [Kevin Buzzard (Apr 30 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882007):
A follow-up to the paper should be "Dependent type theory : extra conditions for free"

#### [Kevin Buzzard (Apr 30 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882009):
doesn't sound as marketable

#### [Kevin Buzzard (Apr 30 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882053):
Initially I had thought that church numerals were just some stupid trick for encoding nat. I hadn't until now realised that they were a literal translation of the inductive definition of nat into another language.

#### [Kevin Buzzard (Apr 30 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882071):
But I hadn't got the translation quite right -- I was using the definition I found in Software Foundations. Maybe they are the translation into some other flavour of theory e.g. some lambda calculus thing

#### [Kevin Buzzard (Apr 30 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882116):
So satan was bad after all -- he shouldn't really be allowed to be a church nat because he's not functorial enough.

#### [Kevin Buzzard (May 01 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125958209):
Some more church nat puzzles

#### [Kevin Buzzard (May 01 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125958215):
```lean
def chℕ := Π X : Type, (X → X) → X → X

namespace chnat 

open nat

definition to_nat : chℕ → ℕ := λ m, m ℕ nat.succ 0 

def of_nat : ℕ → chℕ 
| (zero) := λ X f x, x
| (succ n) := λ X f x, f (of_nat n X f x) -- f (f^n x)

definition of_nat' : ℕ → chℕ 
| 0 := λ X f x, x
| (n + 1) := λ X f x, of_nat' n X f (f x) -- f^n (f x)

theorem nat_of_chnat_of_nat (n : ℕ) : to_nat (of_nat n) = n := sorry
theorem nat_of_chnat_of_nat' (n : ℕ) : to_nat (of_nat' n) = n := sorry
theorem of_nat'_is_of_nat (n : ℕ) : of_nat n = of_nat' n := sorry 

end chnat
```

#### [Kevin Buzzard (May 01 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125958222):
I haven't proved all of them, I expected them all to be true.

#### [Kevin Buzzard (May 10 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359013):
The typeclass `is_group_hom` (in `algebra/group.lean` in mathlib) transports across a lot of structure

#### [Kevin Buzzard (May 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359063):
For example, `equiv.Pi_congr_right` says that if (F i) and (G i) biject for all i, then Pi i, F i bijects with Pi i, G i

#### [Kevin Buzzard (May 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359070):
but if the bijections are all group homs then the product bijection is also a group hom

#### [Kevin Buzzard (May 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359073):
and the proof is idea-free

#### [Kevin Buzzard (May 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359117):
so instead of having to write my own instance for this (which I just did)

#### [Kevin Buzzard (May 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359133):
```lean
instance is_add_group_hom.equiv.Pi_congr_right {γ : Type u} {F : γ → Type u} {G : γ → Type u} [∀ i, add_group (F i)]
[∀ i, add_group (G i)] (H : ∀ i : γ, F i ≃ G i) [∀ i, is_add_group_hom (H i)] :
 is_add_group_hom (equiv.Pi_congr_right H) := ⟨λ a b, funext $ λ i, 
 show H i ((a i) + (b i)) = H i (a i) + H i (b i),
```

#### [Kevin Buzzard (May 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359135):
(OK so it was additive group homs, which is a slightly different typeclass)

#### [Kevin Buzzard (May 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359143):
this should surely have been auto-generated for me when the type class inference system realised I needed it. Right?

#### [Kevin Buzzard (May 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359150):
Similarly, given

#### [Kevin Buzzard (May 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359187):
```lean
definition Pi_lift_map₁ {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
  (H : ∀ i : γ, F i → G i) : (Π i, F i) → Π i, G i := λ Fi i, H i (Fi i)
```

#### [Kevin Buzzard (May 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359192):
I should get a free instance of "all the H i are group homs implies their product is"

#### [Kenny Lau (May 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359252):
that's the UMP of product right

#### [Kevin Buzzard (May 10 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359306):
Pi_lift_map2 is the UMP of product

#### [Mario Carneiro (May 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359317):
This is not exactly trivial. It's conceivable it falls out of the `Pi_instance` tactic stuff, but you do have to make use of some lemmas and funext in appropriate places

#### [Kevin Buzzard (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359366):
I would like to make Lean behave more like a mathematician

#### [Kevin Buzzard (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359369):
and mathematicians know that the function one is easy

#### [Kevin Buzzard (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359371):
and they instantly deduce the equiv one

#### [Mario Carneiro (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359372):
I can see `simp` being able to do this one with some hints

#### [Mario Carneiro (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359376):
the equiv one is literally the same theorem though

#### [Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359382):
There's a meta-hint for this sort of thing

#### [Mario Carneiro (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359384):
that is trivial even by lean's standards

#### [Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359385):
"To prove axiom X for the product, use axiom X on the factors"

#### [Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359388):
I agree it's the same theorem, that's why it has the same proof

#### [Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359391):
but you told me to write it twice

#### [Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359392):
because you said Lean needs to be told it twice

#### [Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359393):
Right?

#### [Mario Carneiro (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359394):
you should apply the theorem, not prove it twice

#### [Kevin Buzzard (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359445):
heh

#### [Mario Carneiro (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359447):
def X := proof, def Y := X

#### [Kevin Buzzard (May 10 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359507):
ha ha

#### [Kevin Buzzard (May 10 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359509):
proof `is_add_group_hom.Pi_lift H` fails

#### [Kevin Buzzard (May 10 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359510):
proof `is_add_group_hom.Pi_lift (λ i, H i)` succeeds

#### [Kevin Buzzard (May 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359518):
Lean knows it's looking for something of a certain type lam i, map

#### [Kevin Buzzard (May 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359519):
and H i is an equiv which coerces to map

#### [Kevin Buzzard (May 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359520):
but it's not smart enough to do it without the i

#### [Mario Carneiro (May 10 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126360142):
what about `is_add_group_hom.Pi_lift _`?

#### [Kevin Buzzard (May 10 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126365134):
nope

#### [Kevin Buzzard (Oct 08 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/135390412):
Ooh look, this is back in the days when I used to post one paragraph as ten one-sentence posts.

I finally got around to making this an issue.

https://github.com/leanprover/mathlib/issues/408

