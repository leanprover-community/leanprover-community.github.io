---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51454startswith.html
---

## Stream: [general](index.html)
### Topic: [startswith](51454startswith.html)

---

#### [Patrick Massot (Jan 04 2019 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412396):
Do we have something like `string.startswith : string -> string -> bool` somewhere?

#### [Mario Carneiro (Jan 04 2019 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412486):
There are `<:+` and `<+:` for comparing lists, you could use that

#### [Gabriel Ebner (Jan 04 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412836):
Omg. Did you get these hieroglyphs from Haskell or from Scala?

#### [Patrick Massot (Jan 04 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412845):
I currently use
```lean
def string.startswith (s s' : string) : Prop := (s'.to_list).is_prefix_of s.to_list

instance (s s') : decidable (string.startswith s s') := 
by unfold string.startswith ; apply_instance
```

#### [Patrick Massot (Jan 04 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412905):
I guess one of your hieroglyphs stands for `list.is_prefix_of`

#### [Patrick Massot (Jan 04 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412913):
But my hope was really that all this should be there already

#### [Mario Carneiro (Jan 04 2019 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154412954):
the hieroglyphs were a terrible idea that I now regret

#### [Mario Carneiro (Jan 04 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413617):
I agree that we should have this function already defined. In particular, you can make a more efficient implementation by working with string iterators instead of lists

#### [Mario Carneiro (Jan 04 2019 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413665):
I should load up the docs for strings in haskell or java and copy everything I see

#### [Patrick Massot (Jan 04 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413755):
I vote for doing that as soon as all topology and commutative algebra PR will be merged!

#### [Mario Carneiro (Jan 04 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413832):
I'm working on #464, making good progress

#### [Mario Carneiro (Jan 04 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413893):
what commutative algebra PRs?

#### [Patrick Massot (Jan 04 2019 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154413934):
I'm joking, keep going on analysis. You'll have many nights in Amsterdam for algebra

#### [Sebastien Gouezel (Jan 04 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154431401):
```quote
I'm working on #464, making good progress
```
 Btw, I updated the PR two days ago, but if you started working on the previous version you can of course disregard the modifications I made.

#### [Mario Carneiro (Jan 04 2019 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/startswith/near/154431693):
yeah, I noticed and have already incorporated your changes

