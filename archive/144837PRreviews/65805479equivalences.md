---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/65805479equivalences.html
---

## Stream: [PR reviews](index.html)
### Topic: [#479 equivalences](65805479equivalences.html)

---

#### [Scott Morrison (Nov 16 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792343):
This one was overdue, and lurking in my other repository.

#### [Scott Morrison (Nov 16 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792347):
* Define `equivalence C D` for an equivalence of categories,
* `[refl]`, `[symm]`, and `[trans]` for equivalences,
* a typeclass `is_equivalence` to decorate functors,
* and the proofs that a functor is an equivalence if and only if it is fully faithful and essentially surjective.

#### [Scott Morrison (Nov 16 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792389):
One thing to note: `ess_surj` here is the constructive version, that picks a particular up-to-isomorphism-preimage for every object, not merely asserting that one exists.

#### [Scott Morrison (Nov 16 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792396):
If this is upsetting, I can add an extra constructor that uses choice and just takes the existence statement.

#### [Reid Barton (Nov 16 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793562):
I think it might be best to just make `ess_surj` a Prop

#### [Reid Barton (Nov 16 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793709):
I'm actually not sure... when does one really use the fact that ess. surj. + fully faithful implies an equivalence?

#### [Mario Carneiro (Nov 16 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793744):
I thought that was the only purpose of ess surj

#### [Reid Barton (Nov 16 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793912):
I see... I guess the point is that you don't have to construct the functoriality of the inverse functor

#### [Reid Barton (Nov 16 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793968):
or the naturality of one of the isomorphisms

#### [Reid Barton (Nov 16 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793980):
or both isomorphisms actually

#### [Reid Barton (Nov 16 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147794043):
Maybe it would be simplest to just discard `ess_surj` and inline its fields into arguments of `equivalence_of_fully_faithfully_ess_surj`

#### [Reid Barton (Nov 16 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147794205):
The same thing happens for adjunctions (https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L280)

#### [Reid Barton (Nov 16 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147794676):
But in actual math, providing that structure would always be trivial, anyways

#### [Reid Barton (Nov 16 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147795637):
I guess another way of putting it is: when would you need choice to prove that a functor (which you're proving is an equivalence) is essentially surjective, rather than just writing down a formula for an inverse image of an object

#### [Scott Morrison (Nov 16 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147801654):
I’d be happy with the inlining solution.

#### [Scott Morrison (Nov 28 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148697250):
@**Reid Barton**, what do you think here? Inlining `ess_surj` feels to me like to makes the code more cluttered, and I don't really understand the argument against having it.

#### [Johan Commelin (Nov 28 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148697336):
I wouldn't mind keeping it. I think it might turn out to be useful... although I don't have a concrete example. But I think essential images show up, and probably we want to know that functors are essentially surjective onto their essential image, etc...

#### [Scott Morrison (Nov 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698817):
Besides this question about `ess_surj`, the equivalences branch is now ready to go. It's mostly the basic facts about equivalences.

#### [Scott Morrison (Nov 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698824):
It also contains a new category theory-specific  tactic `slice`.

#### [Scott Morrison (Nov 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698840):
```
/--
`slice` is a conv tactic; if the current focus is a composition of several morphisms,
`slice a b` reassociates as needed, and zooms in on the `a`-th through `b`-th morphisms.

Thus if the current focus is `(a ≫ b) ≫ ((c ≫ d) ≫ e)`, then `slice 2 3` zooms to `b ≫ c`.
 -/
```

#### [Scott Morrison (Nov 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698845):
```
/--
`slice_lhs a b { tac }` zooms to the left hand side, uses associativity for categorical
composition as needed, zooms in on the `a`-th through `b`-th morphisms, and invokes `tac`.
-/
```

#### [Scott Morrison (Nov 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698864):
There's also a note in the PR:
```
-- TODO someone might like to generalise this tactic to work with other associative structures.
```
but that someone is not me at the moment, and hopefully won't hold up this PR.

#### [Scott Morrison (Nov 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698918):
(It's possible @**Simon Hudon** will be interested, however, as he's done similar stuff already.)

#### [Mario Carneiro (Nov 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700202):
@**Scott Morrison|110087** oh dear, something went wrong in the merge. Did I miss a dependent PR?

#### [Scott Morrison (Nov 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700271):
I don't think so?

#### [Scott Morrison (Nov 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700278):
Shall I rebase onto current master?

#### [Scott Morrison (Nov 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700281):
Or is it too late for that? :-)

#### [Scott Morrison (Nov 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700305):
It looks okay to me? I see it sitting on top of master now.

#### [Scott Morrison (Nov 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700446):
Oh, I see there are problems.

#### [Scott Morrison (Nov 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700487):
ok, fix coming

#### [Scott Morrison (Nov 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700495):
I think it's minor, some imports, but I'm not sure how they got messed up.

#### [Scott Morrison (Nov 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700541):
It looks like changing the line `import category_theory.embedding` to `import category_theory.fully_faithful` at the top of `category_theory/equivalences.lean` solves the problem.

#### [Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700584):
I've no idea how it was passing locally and on travis with that wrong, but okay. :-)

#### [Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700595):
I guess just that `.olean` files never get deleted!?

#### [Mario Carneiro (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700599):
right

#### [Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700602):
Is it best if you make that change?

#### [Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700609):
Or should I make a commit on community?

#### [Mario Carneiro (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700618):
eh, it's not checked out here, just send a PR

#### [Scott Morrison (Nov 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700659):
ok, I will fix some documentation failures I'm noticing at the same time :-)

#### [Mario Carneiro (Nov 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700709):
ok

#### [Scott Morrison (Nov 28 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148701010):
#500

#### [Reid Barton (Nov 28 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148711889):
```quote
@**Reid Barton**, what do you think here? Inlining `ess_surj` feels to me like to makes the code more cluttered, and I don't really understand the argument against having it.
```
My only objection is that the name `ess_surj` is wrong, because "essentially surjective" is a property but `ess_surj F` values are not unique in any sense at all (except when `F` is actually an equivalence).

#### [Reid Barton (Nov 28 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148711978):
It should be named `ess_left_inverse_on_objects` (or maybe right--I've lost any grasp I may have once had on the difference between left and right), or `ess_surj_data` or `ess_surj_choices` or something.

#### [Scott Morrison (Nov 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148741371):
Okay! I will rename it to something sufficiently unpleasant looking to warn people off. :-)

