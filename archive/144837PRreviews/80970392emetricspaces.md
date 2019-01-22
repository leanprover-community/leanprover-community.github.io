---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/80970392emetricspaces.html
---

## [PR reviews](index.html)
### [#392 emetric spaces](80970392emetricspaces.html)

#### [Johan Commelin (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384309):
I am wondering: `dist` of a metric space takes values in `ℝ`, while the `edist` of an emetric space takes values in `ennreal`. Should the latter maybe take values in `with_top ℝ`?

#### [Johan Commelin (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384322):
I haven't thought this through carefully. I just noted it while reading through the code.

#### [Mario Carneiro (Oct 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384347):
`ennreal` has nicer properties than `with_top R`

#### [Mario Carneiro (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384408):
I think we had a conversation about going the other way, i.e. using `nnreal` for the codomain of `dist`

#### [Kenny Lau (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384413):
If X is a metric space, is P(X) an emetric space?

#### [Mario Carneiro (Oct 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384434):
I think there is a Hausdorff something or other about this

#### [Mario Carneiro (Oct 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384439):
https://en.wikipedia.org/wiki/Hausdorff_distance

#### [Mario Carneiro (Oct 08 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384480):
it's not all sets, just compact sets

#### [Johan Commelin (Oct 08 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384489):
And the axiom `(dist_nonneg : ∀ x y, dist x y ≥ 0)` in the definition of metric space. This is redundant, because it follows from `edist_dist`.

#### [Kenny Lau (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384518):
@**Mario Carneiro** compactness just ensures that it is finite

#### [Mario Carneiro (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384520):
oh wait, the Hausdorff distance is defined on all sets but it is only an extended pseudometric

#### [Kenny Lau (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384526):
and in any case I'm just talking about d(X,Y) := inf d(x,y)

#### [Mario Carneiro (Oct 08 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384538):
that's not even zero on the same sets

#### [Kenny Lau (Oct 08 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384589):
it is

#### [Mario Carneiro (Oct 08 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384604):
it is

#### [Mario Carneiro (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384611):
but it's not an iff

#### [Sebastien Gouezel (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384619):
The Hausdorff distance is an edistance on closed subets.

#### [Sebastien Gouezel (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384627):
This is one of the motivations to introduce this notion of emetric spaces.

#### [Sebastien Gouezel (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384634):
It restricts to a genuine distance on compact nonempty subsets.

#### [Mario Carneiro (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384641):
Another motivation is the infinite product space

#### [Mario Carneiro (Oct 08 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384692):
with supremum metric

#### [Sebastien Gouezel (Oct 08 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384732):
The axiom `dist_nonneg` is not redundant. When I write `edist x y = ↑(nnreal.of_real (dist x y))`, it would be true if `dist x x = -1`, say, as `nnreal.of_eal` sends `-1`to `0`.

#### [Sebastien Gouezel (Oct 08 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384881):
`ennreal` is very much better behaved than `ereal` from the algebraic point of view. So, if you know that something is nonnegative, you should really favor `ennreal` over `ereal` from a usability point of view. On the opposite, `real` is better behaved than `nnreal` (subtraction is nice on `real`), so if you have the choice between the two better use reals. The main difference is that you will often subtract distances, but you should never subtract edistances as they can be infinite.

#### [Mario Carneiro (Oct 08 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135384893):
why the finiteness assumption in `emetric_space_pi`

#### [Sebastien Gouezel (Oct 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135385019):
If you take an infinite product of emetric spaces, with the sup distance, then the topology you get is typically not the product topology. So, this is not a good notion.

#### [Kevin Buzzard (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135387840):
```quote
it is
```
not on the empty set...

#### [Johan Commelin (Oct 08 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135387951):
We need an Ofer Gabber emoji

#### [Mario Carneiro (Oct 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135387962):
we'll make you a CS guy yet... you get an honorary degree in zeroology

#### [Kevin Buzzard (Oct 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135388367):
I am proud to be a zerologist. In fact one of the nicest comments a speaker ever said to me was in a talk when I noted that an assertion made by the speaker did not make sense when $$n=0$$ and I pointed this out, and they said "I did not know Gabber was in the audience!".

#### [Kevin Buzzard (Oct 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/135388431):
I nearly responded "well he's certainly not giving the talk"

#### [Johan Commelin (Nov 09 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#392 emetric spaces/near/147372294):
This PR is now merged! Hurray! :tada: :octopus:

