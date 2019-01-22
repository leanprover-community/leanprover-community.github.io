---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36869linarithnat.html
---

## [general](index.html)
### [linarith & nat](36869linarithnat.html)

#### [Reid Barton (Sep 30 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134918920):
@**Rob Lewis** I started remembering to use `linarith` to solve some easy goals like `f < g -> -f - -g <= 0 -> false`.
Do you have a sense of how hard it would be to support `-` on nat? I guess at least in simple cases there should be a translation to a new linear system (maybe involving adding an extra variable).

#### [Rob Lewis (Sep 30 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919195):
Yeah, there's a translation that can be done. My instinct: it would take more work to go from the current state to supporting `-` than it took to go from no `nat` support to here. The bigger worry is that these are all just stopgaps, ultimately we want `omega` or `cooper` or something nat/int specific. `linarith` will never work completely right on `nat`.

#### [Mario Carneiro (Sep 30 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919295):
does linarith support `max` and `min`?

#### [Mario Carneiro (Sep 30 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919307):
Maybe focus effort on that, and then you can get nat.sub easy by rewriting it to a `max`

#### [Rob Lewis (Sep 30 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919411):
Not natively. You can unfold them, `split_ifs`, and then call `linarith` a bunch of times. That's exactly how the translation would go, and it's not efficient, you get an explosion of `linarith` calls.

#### [Mario Carneiro (Sep 30 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919422):
So `linarith` only handles convex regions?

#### [Mario Carneiro (Sep 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919468):
You can interpret a `max` or `min` as a conjunction sometimes, and then there is no case split

#### [Mario Carneiro (Sep 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919470):
but when the inequality is the wrong way you get a disjunction and have to case split

#### [Mario Carneiro (Sep 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919471):
I don't see any way to avoid exponential blowup

#### [Reid Barton (Sep 30 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919525):
Right, that makes sense.

#### [Rob Lewis (Sep 30 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919571):
Yeah. `linarith` has no fancy logic handling at all, and again, I'm not sure how much it's worth bundling more and more into the current tactic. Eventually you just end up approximating an SMT solver.

#### [Reid Barton (Sep 30 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919572):
On the other hand, sometimes the problems we want to solve are quite small. Like I had this one: define `def I (j : ℕ) : ℕ := if j ≤ e then e - j else j`, and then prove `lemma II {j : ℕ} : I (I j) = j`. (`e` is some constant nat.)

#### [Reid Barton (Sep 30 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919620):
Haha, that's the trick isn't it. Once you write the tactic to do X, then everything will start to look like "almost X, if only..."

#### [Kevin Buzzard (Sep 30 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134920648):
With `ring` I started to learn how to use what we had to get what I wanted in two lines rather than one. For example if the goal is `(x+1)^2 < x^2+2*x+2`then instead of thinking "a souped-up `ring` should make progress here" you prove `h : x^2+2*x+2=(x+1)^2+1 := by ring` and then rewrite. For `ring` in particular, having a very clear idea of exactly what it can and can't do is of great help to me, and I am beginning to understand `simp` and `dec_trivial` in the same way. I only wish I had a better grasp on what things like `cc`, `linarith` and `finish` did -- these are still tactics which I apply "randomly" in some sense (like how I used to apply `simp` when I was a beginner).

#### [Tobias Grosser (Sep 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134926271):
We use (outside of the theorem proover world) a simplification and decision procedure for Presburger arithmetic based on linear programming / dual simplex.

#### [Tobias Grosser (Sep 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134926325):
While probably the easiest is to implement omega / cooper / or Leo's extensions to cooper as used in Z3, I am interested in exploring an approach based on the mathematics implemented in a constraint based math library such as isl, visible e.g. at nhttp://playground.pollylabs.org/.

#### [Tobias Grosser (Sep 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134926332):
I am interested to discuss this topic in more depth (and will also be in Freiburg).

