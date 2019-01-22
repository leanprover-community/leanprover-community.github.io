---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66274piinstances.html
---

## [general](index.html)
### [pi instances](66274piinstances.html)

#### [Patrick Massot (Mar 12 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598593):
@**Mario Carneiro** and @**Johannes Hölzl** could you have a look at the wonderful tactics that @**Simon Hudon** wrote for me in https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean and tell me whether this is suitable for mathlib? Remember the mathematical goals is to have instances of algebraic structures for Pi products of groups, rings, modules etc. and the Lean goal is to avoids writing tons of lines like https://github.com/PatrickMassot/lean-differential-topology/blob/f47348abf8515e23bd485683d8b351c7fd89c70f/src/indexed_product.lean#L92

#### [Mario Carneiro (Mar 12 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598652):
It seems a bit overkill, but it is clearly effective and I'd hate to throw a nice tactic like that away. Sure, PR away

#### [Mario Carneiro (Mar 12 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598704):
(Re: overkill, consider that the tactic + proofs have actually *increased* the overall size of the file, from 100 to 156 lines, and it looks like you already have covered most of the algebraic hierarchy there, so I think that's nearly its complete applicability.)

#### [Patrick Massot (Mar 12 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598754):
I think the psychological impact will be different when those instances will be spread over five files instead of one

#### [Simon Hudon (Mar 12 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598756):
Would it make more worthwhile if we used the same tactic to prove that `vector n α` conforms to a given structure if `α` does and that it is true for other applicative functors than `vector n`?

#### [Patrick Massot (Mar 12 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598797):
And also, I think this is really cool tactic. I can't wait for the making of tutorial that Simon promised to write soon.

#### [Simon Hudon (Mar 12 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123598844):
:) I'll get right on that. I might procrastinate a bit with the `mono` tactic, I hope you'll forgive me

#### [Mario Carneiro (Mar 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599072):
I can see how this would generalize to all applicative functors, and I agree that would increase the applicability. (Again, I'm not actually rejecting the tactic version, it is always nice to have a new tactic if only as a future example and base for later expermentation. I just probably would have tried to find a more efficient way to write the proofs, say by using `refine`, rather than automating the entire process.)

#### [Simon Hudon (Mar 12 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599166):
Cool

#### [Simon Hudon (Mar 12 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599179):
I do take your point that it's making more code rather than less. It should withstand a lot of reengineering of the hierarchy though.

#### [Simon Hudon (Mar 12 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599286):
I'm not sure you could do much better than the one-line proofs that were there. For me, I think that was an interesting exercise. I'm especially interested to see how the code can be improved now

#### [Mario Carneiro (Mar 12 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599296):
since all the proofs follow the same script, you can abbreviate it with `refine {..}; funext; simp` or what have you

#### [Simon Hudon (Mar 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599342):
but for `simp` to work, don't you need all the laws of all the involved classes to be labelled `simp`?

#### [Simon Hudon (Mar 12 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599395):
I don't know how I'd implement it but if we could use the same tag system that the `case` system relies on, when we call `refine { .. }` we could tag each goal with the field that it responds to.

#### [Simon Hudon (Mar 12 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599401):
It would be more generally applicable and would probably shrink those scripts

#### [Mario Carneiro (Mar 12 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599413):
I would just add anything that isn't a simp lemma to the bracket list until it works

#### [Mario Carneiro (Mar 12 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599458):
Here obviously I'm thinking as a proof writer not a tactic writer

#### [Mario Carneiro (Mar 12 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599468):
It's a cool idea to use tags with `refine {..}`. You would have to ask @**Sebastian Ullrich** about that

#### [Simon Hudon (Mar 12 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599469):
That makes sense and that's robust enough

#### [Simon Hudon (Mar 12 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123599510):
Glad you like it :) I'll talk to him about it

#### [Kevin Buzzard (Mar 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123601977):
```quote
(Re: overkill, consider that the tactic + proofs have actually *increased* the overall size of the file, from 100 to 156 lines, and it looks like you already have covered most of the algebraic hierarchy there, so I think that's nearly its complete applicability.)
```
Kenny and I had to prove that a slightly complicated structure was a ring, and our current effort looks like this:

#### [Kevin Buzzard (Mar 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123601978):
https://github.com/kbuzzard/lean-stacks-project/blob/60db6a688861ec7a735e5818eb3d992cf8e2d7a5/src/scheme.lean#L368

#### [Kevin Buzzard (Mar 12 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123602037):
There's a lot of repeating `λ _, structure_presheaf_value.ext _ _ _ _ $ λ _ _, ` which I felt might have been better dealt with by a general "maps to a ring with certain properties form a ring" tactic.

#### [Simon Hudon (Mar 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123602167):
I can have a look and see if the same tactics could apply

#### [Simon Hudon (Mar 12 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi instances/near/123602301):
I'll have a look tomorrow. Time for bed now

