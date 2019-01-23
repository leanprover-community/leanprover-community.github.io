---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/38132shouldthisbedectrivial.html
---

## Stream: [maths](index.html)
### Topic: [should this be dec_trivial?](38132shouldthisbedectrivial.html)

---

#### [Kevin Buzzard (Nov 18 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920509):
`example (n : ℕ) : n > 0 → n ≤ 6 → fact n < 3 ^ n := dec_trivial -- fails`

I do 6 case splits and `dec_trivial` seems to be able to handle the arithmetic, but I can't do it all in one go. I sometimes run into these. How is one supposed to diagnose what has happened and fix it?

#### [Chris Hughes (Nov 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920516):
Revert n, and put `n \le 6` before `0<n`

#### [Kevin Buzzard (Nov 18 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920517):
Thanks Chris.

#### [Kevin Buzzard (Nov 18 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920557):
I see, so `forall n : nat, n <= X -> P n` works, and I just need to ensure I'm in this format.

#### [Mario Carneiro (Nov 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921371):
sigh... why the horrible case split proofs?

#### [Mario Carneiro (Nov 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921374):
you could reason it instead

#### [Kevin Buzzard (Nov 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921375):
I don't really know what you're saying

#### [Kevin Buzzard (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921379):
or even if you're talking to me

#### [Kevin Buzzard (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921383):
But my job is to solve the problems I set, in Lean

#### [Mario Carneiro (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921386):
if you had to prove that theorem by hand I am sure you wouldn't evaluate 6 factorials

#### [Kevin Buzzard (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921387):
and the problem is "for which positive integers n is n! < 3^n"

#### [Mario Carneiro (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921389):
you can prove that it's true for 5 and stop because monotonicity

#### [Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921440):
ha ha

#### [Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921442):
I'm not sure it's that easy

#### [Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921448):
n! and 3^n are changing in different ways

#### [Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921450):
and things get weird at n=3

#### [Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921452):
I think I have to check all 6

#### [Kevin Buzzard (Nov 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921462):
dec_trivial times out for 7 :-/

#### [Kevin Buzzard (Nov 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921463):
(hence the norm_num approach, which was also troublesome -- see other thread)

