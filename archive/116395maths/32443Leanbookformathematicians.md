---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/32443Leanbookformathematicians.html
---

## Stream: [maths](index.html)
### Topic: [Lean book for mathematicians](32443Leanbookformathematicians.html)

---

#### [Kevin Buzzard (May 30 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307658):
I'm writing a book for mathematicians who want to learn Lean.

#### [Kevin Buzzard (May 30 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307661):
Let me know what I should put in it

#### [Kevin Buzzard (May 30 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307663):
Of course I already have a gazillion ideas of my own

#### [Kevin Buzzard (May 30 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307670):
and even some stuff written -- in sphinx.

#### [Kevin Buzzard (May 30 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307698):
sphinx lets me write both maths and Lean code and I am happy with the results.

#### [Kevin Buzzard (May 30 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307715):
Curerntly it's all in a private repo

#### [Kevin Buzzard (May 30 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307725):
but definitely by 1st July when I have a bunch of maths UGs working with me on Lean stuff I will have made it public.

#### [Kevin Buzzard (May 30 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307735):
My goal is to show mathematicians that it is possible to formalise the mathematics that they are interested in, in Lean.

#### [Kevin Buzzard (May 30 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307736):
My target audience is undergraduates

#### [Kevin Buzzard (May 30 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307740):
or PhD students

#### [Kevin Buzzard (May 30 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307749):
but older viewers are also welcome to read it

#### [Kevin Buzzard (May 30 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307750):
It will be based on Lean 3.4.1 and Mathlib 3.4.1 whatever that is

#### [Kevin Buzzard (May 30 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127307789):
(the latter is a moving target, which makes it a bit more annoying to specify succinctly)

#### [Johan Commelin (May 30 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127311161):
I think in a chapter on tactics, you want exercises like the one you had on the semi-quasi-demi-presheaves. The exercise says: try to prove this lemma with all the tactics you have seen so far (and maybe you give an explicit list). And then the reader gets stuck (they should be warned that it is your point to get them stuck). And then you teach them a new tactic (in this case `change`).

#### [Johan Commelin (May 30 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lean%20book%20for%20mathematicians/near/127311192):
That way, maybe we will recognise where to apply that tactic in the future. Because we will get stuck with our standard toolkit, and realise "oh, I remember this kind of stuckness from an exercise in LftWM. I need to use `change`!"

