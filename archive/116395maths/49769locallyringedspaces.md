---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49769locallyringedspaces.html
---

## [maths](index.html)
### [locally ringed spaces](49769locallyringedspaces.html)

#### [Scott Morrison (Sep 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171105):
In [`lean-category-theory`](https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/locally_ringed.lean) I've added a definition of `locally_ringed_space`.

#### [Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171115):
```
def structure_sheaf := sheaf.{v+1 v} α Ring

structure ringed_space :=
(𝒪 : structure_sheaf α)

structure locally_ringed_space extends ringed_space α :=
(locality : ∀ x : α, local_ring (stalk_at.{v+1 v} 𝒪 x).1)
```

#### [Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171148):
and that seems to work (without even many sorries in earlier files :-)

#### [Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171149):
But there's quite a bit of work to do in order to actually construct examples.

#### [Patrick Massot (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171150):
Yeah! Let's do that instead of trying to prove 2 is not a square in Z and get depressed

#### [Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171151):
I thought I should try to do the sheaf of cts functions on a topological space.

#### [Scott Morrison (Sep 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171156):
Unfortunately there are going to be some difficulties.

#### [Scott Morrison (Sep 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171180):
In particular, at the moment `stalk_at` is just defined by:
```
def stalk_at (F : sheaf α V) (x : α) : V :=
colimit (F.near x)
```

#### [Scott Morrison (Sep 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171203):
Unfortunately general colimits of rings are pretty gross. My plan had been to construct coequalizers and coproducts in CommRing,

#### [Scott Morrison (Sep 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171208):
and then use general machinery to get colimits.

#### [Scott Morrison (Sep 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171213):
However if you do that, it's going to be very hard to show that a stalk of the structure sheaf is actually germs of continuous functions at that point.

#### [Scott Morrison (Sep 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171271):
I think I'll need to change `colimit` in the definition of `stalk_at` to `directed_colimit` (or `filtered_colimit`?), show that the poset of neighbourhood of `x` is actually directed, and then separately give a formula for directed colimits of commutative rings.

#### [Scott Morrison (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171322):
That formula for directed colimits, when applied to the sheaf of continuous functions, should look exactly like germs.

#### [Scott Morrison (Sep 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133171386):
But if someone wants to do parts of this:
* define filtered categories, and filtered colimits
* construct instances of `has_coproducts`, `has_coequalizers`, and/or `has_filtered_limits` for `Ring`
* show that continuous functions from a topological space to a topological ring forms a topological ring
* define germs of continuous functions
* show that germs are a local ring
then it will get done faster. :-)

#### [Patrick Massot (Sep 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133172131):
I'd love to work on all that, but I really think I should focus on completions of rings, otherwise the perfectoid project will be really stuck

#### [Reid Barton (Sep 01 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133173786):
I definitely plan to define at least filtered categories and colimits

#### [Scott Morrison (Sep 01 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133174627):
@**Reid Barton**, great! I just made a primitive first cut at filtered categories, and shows that inhabited directed posets are filtered.

#### [Scott Morrison (Sep 01 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133174638):
I was going to start trying to define filtered limits in `Ring`, but I think jetlag has caught up with me.

#### [Reid Barton (Sep 01 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133174783):
I'm currently on a train anyways, but is there a branch somewhere where I can follow along with the limits etc.?

#### [Scott Morrison (Sep 01 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133174852):
It's all happening in `master` of `lean-category-theory`

#### [Scott Morrison (Sep 01 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133174856):
Although I'm committing less often because I'm trying to be better and checking that it compiles before pushing :-)

#### [Reid Barton (Sep 01 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133175067):
Ah yes, I see it.

#### [Reid Barton (Sep 01 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133175080):
Yes, that's a nice thing to do when you have users :)

#### [Reid Barton (Sep 01 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally ringed spaces/near/133175086):
Though maybe I could just work in a branch of your library for now

