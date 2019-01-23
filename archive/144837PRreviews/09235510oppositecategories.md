---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/09235510oppositecategories.html
---

## Stream: [PR reviews](index.html)
### Topic: [#510 opposite categories](09235510oppositecategories.html)

---

#### [Johan Commelin (Dec 20 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152239436):
@**Scott Morrison|110087** I saw you fixed some stuff, but Travis is still complaining... If you don't have time for this, just let me know, and I'll try to take a look.

#### [Scott Morrison (Dec 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152241278):
Think I've got it now. That intermediate commit was just getting work from my office computer to my laptop.

#### [Johan Commelin (Dec 22 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152389993):
@**Mario Carneiro** I get that you don't like the idea of making `op` irreducible. So what is the best way forward? Just now I had to compose two arrows `f` and `g`, but `f` lived in the opposite category... so Lean complained. I would love to just write `f.unop` and move on. What do you think is the best solution?

#### [Mario Carneiro (Dec 22 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152390040):
you can have `unop` without making `op` irreducible

#### [Johan Commelin (Jan 17 2019 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/155339244):
@**Mario Carneiro** Would you welcome a PR that puts `op` and `unop` throughout the library without making `op` irreducible?

#### [Mario Carneiro (Jan 17 2019 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/155345431):
sure

#### [Scott Morrison (Jan 19 2019 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156433638):
Ok, #510 no longer actually makes `opposite` irreducible. This PR has some useful cleanup in other category_theory files, as well.

#### [Reid Barton (Jan 22 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597595):
It's hard to understand what is going on when reviewing a commit which contains a combination of substantial changes (like to `op`), general cleanup, and new features.

#### [Reid Barton (Jan 22 2019 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597623):
Miscellaneous cleanup PRs are fine, but they shouldn't be mixed in with actual changes.

#### [Reid Barton (Jan 22 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597697):
Did we come to the conclusion that `opposite` should not be irreducible? Or are we just not changing it for now?

#### [Johan Commelin (Jan 22 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597713):
Mario does not want it to be irreducible. I have no clue what's good. And others seemed to not care very much (-;

#### [Johan Commelin (Jan 22 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597718):
So for now it won't be irreducible.

#### [Reid Barton (Jan 22 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598117):
Hmm, but I see `hom.op` and `hom.unop` are irreducible?

#### [Reid Barton (Jan 22 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598120):
Is that intentional?

#### [Reid Barton (Jan 22 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598126):
and then sometimes they get made not irreducible

#### [Reid Barton (Jan 22 2019 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598378):
I guess I don't really understand what the plan is that involves introducing `op` and `unop` but not making `opposite` irreducible (or even a structure). I feel like we don't have a good chance of putting `op`/`unop` in all the right spots if not forced to do so by irreducibility of `opposite`, and then whatever problem we solve with `op`/`unop` will continue to show up later.

#### [Johan Commelin (Jan 22 2019 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598402):
@**Mario Carneiro** What do you think about :up: ?

#### [Reid Barton (Jan 22 2019 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598476):
I think what we really want is a one-member structure with definitional eta, and this `irreducible` thing is the closest approximation we can make

#### [Reid Barton (Jan 22 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156599932):
I wonder whether we need `category.hom.op` at all

#### [Johan Commelin (Jan 22 2019 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600126):
I've had breakage because Lean thought `f` was in the opposite category and I wanted something in `C`.

#### [Johan Commelin (Jan 22 2019 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600132):
Or are you saying we only need `unop`?

#### [Reid Barton (Jan 22 2019 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600316):
Okay, after some experimentation, removing `category.hom.op` seems like a bad idea

#### [Reid Barton (Jan 22 2019 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600338):
But I'm not very happy about marking them as irreducible but then undoing that in various places.

#### [Reid Barton (Jan 22 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600750):
I think all this `hom.op` stuff doesn't address the real issue though

#### [Reid Barton (Jan 22 2019 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600821):
it's still easy to end up with goals like `F.map g ≫ F.map f = F.map f ≫ F.map g`

#### [Reid Barton (Jan 22 2019 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156601769):
I think the right way to do this would be to give the hom sets the same treatment as the objects, but it seems to be impossible without splitting out the `hom` field into its own class

#### [Reid Barton (Jan 22 2019 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156601780):
which I think we may want to do anyways

#### [Reid Barton (Jan 22 2019 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156603158):
For example, the definition of composition in the opposite category should not be `λ _ _ _ f g, g ≫ f` but `λ _ _ _ f g, (g.unop ≫ f.unop).op`

#### [Reid Barton (Jan 22 2019 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156604715):
I would also be willing to try just using a structure

#### [Reid Barton (Jan 22 2019 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156606540):
In fact, maybe we can even reuse https://github.com/leanprover/mathlib/pull/538?

