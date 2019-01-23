---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12504intcastisunique.html
---

## Stream: [maths](index.html)
### Topic: [int.cast is unique](12504intcastisunique.html)

---

#### [Johan Commelin (Jan 21 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541423):
Do we already know that `int.cast` is the unique ring hom `ℤ → R`?

#### [Kevin Buzzard (Jan 21 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541435):
I knew that, yes.

#### [Johan Commelin (Jan 21 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541482):
Did your Lean also know it?

#### [Kevin Buzzard (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541503):
Eew, is it some pretty grim induction?

#### [Johan Commelin (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541568):
I don't know, I just want to use it if it's in mathlib.

#### [Kevin Buzzard (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541575):
Yes, I don't think I've seen my Lean know it...

#### [Johan Commelin (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541579):
I can probably write a proof in a couple of minutes...

#### [Kevin Buzzard (Jan 21 2019 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541683):
If we have two ring homomorphisms from $$A$$ to $$B$$ then the subset of $$A$$ where they coincide is a subring. Do we know that $$\mathbb{Z}$$ has no subrings other than itself?

#### [Chris Hughes (Jan 21 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156542839):
`int.eq_cast`

#### [Johan Commelin (Jan 21 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156543031):
Aah... nice. Too bad it isn't stated in terms of ring homs.

