---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36054uncheckedcast.html
---

## Stream: [general](index.html)
### Topic: [unchecked cast](36054uncheckedcast.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005017):
```lean
#eval @unchecked_cast int nat (-3) -- 2147483645
#eval @unchecked_cast (list nat) (list nat) [3] -- [3]
#eval @unchecked_cast nat (list nat) 3 -- []
#eval @unchecked_cast nat (nat → nat) 3 3
-- vm check failed: cidx(closure) == 0 (possibly due to incorrect axioms, or sorry)
#eval @unchecked_cast (list (list nat)) (list nat) [[3]]
-- vm check failed: is_mpz(o) (possibly due to incorrect axioms, or sorry)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005054):
quite fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005957):
can you cast int to nat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005964):
Lean always has fun trying to do that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005972):
oh duh that's exactly what you just did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005990):
Is this related to why Lean times out if you try to do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 15 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006063):
I doubt it. I don't think the kernel or the elaborator care about the VM representation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006455):
How come the VM can deal with integers bigger than 2^32 if it is storing things in this classical manner?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006602):
```lean
#eval @unchecked_cast int nat (-21474836450) -- -21474836450
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006604):
looks like `-21474836450` is a natural number!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007206):
@**Kevin Buzzard** for small enough integers it stores them in 4-bytes, for bigger ones it uses the GMP multiprecision library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 15 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007226):
```quote
How come the VM can deal with integers bigger than 2^32 if it is storing things in this classical manner?
```
My guess is that a nat is 31 bits for the nat, plus one more bit that says we need more bits. An int is probably `30` bits plus a sign and one more bit for if we need more bits.
```lean
#eval @unchecked_cast nat int (2 ^ 30) -- -1073741824
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 15 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007280):
https://gmplib.org

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007294):
rofl the "need help" bit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 15 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134013568):
Interesting, it hadn't occurred to me that you could define `unchecked_cast` (in `meta`) yourself, without a special constant.
I wonder how badly you can break things with it. I tried casting a nat to a function nat -> nat and then applying it, hoping for a crash, but all I got was a boring vm check failure.

