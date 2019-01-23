---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00033implicitargumentsandring.html
---

## Stream: [general](index.html)
### Topic: [implicit arguments, and `ring`](00033implicitargumentsandring.html)

---

#### [Scott Morrison (Sep 29 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878744):
Hi @**Mario Carneiro**, I noticed an unfortunate feature of `ring`.

#### [Scott Morrison (Sep 29 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878745):
I'd got stuck doing this:
```
example (x y : ℕ) (h : x ^ 2 + 3 * y ^ 2 = 4) : false :=
begin
ring at h,
simp at h,
ring at h,
simp at h,
-- ...
end
```

#### [Scott Morrison (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878784):
where it looks like the goal isn't changing.

#### [Scott Morrison (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878788):
It just says 
```
x y : ℕ,
h : x ^ 2 + 3 * y ^ 2 = 4
⊢ false
```

#### [Scott Morrison (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878791):
but with pp.all true, you can see if flipping back and forth:

#### [Mario Carneiro (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878803):
You shouldn't use `ring` nonterminally

#### [Mario Carneiro (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878808):
at least not automatically (i.e. in `tidy`)

#### [Mario Carneiro (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878815):
if it doesn't close the goal, assume it failed

#### [Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878817):
Yes, I know, but I want to for a moment anyway. :-)

#### [Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878818):
Ah, okay. :-)

#### [Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878821):
But that takes all the fun out of it.

#### [Mario Carneiro (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878823):
`ring` rewrites the goal into sum-of-products form for ease of reading when it fails

#### [Scott Morrison (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878827):
Because sometimes `ring at *, exfalso, linarith` can get stuff done.

#### [Mario Carneiro (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878829):
this form disagrees with simp normal form in some places

#### [Scott Morrison (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878870):
The problem I was having here is actually just in the implicit arguments flipping back and forth.

#### [Scott Morrison (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878874):
The expression "itself" is not being changed by either `simp` or `ring`.

#### [Mario Carneiro (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878881):
wait, maybe I don't understand then

#### [Mario Carneiro (Sep 29 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878882):
what is changing?

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878894):
With usual pretty printing, neither `simp` nor `ring` do anything, and the goal just looks like
```
x y : ℕ,
h : x ^ 2 + 3 * y ^ 2 = 4
⊢ false
```

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878896):
but with pp.all we get:

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878898):
```
x y : nat,
h :
  @eq.{1} nat
    (@has_add.add.{0} nat nat.has_add
       (@has_pow.pow.{0 0} nat nat nat.has_pow x (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
       (@has_mul.mul.{0} nat
          (@mul_zero_class.to_has_mul.{0} nat
             (@semiring.to_mul_zero_class.{0} nat
                (@comm_semiring.to_semiring.{0} nat
                   (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                      nat.canonically_ordered_comm_semiring))))
          (@bit1.{0} nat nat.has_one nat.has_add (@has_one.one.{0} nat nat.has_one))
          (@has_pow.pow.{0 0} nat nat nat.has_pow y (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))))
    (@bit0.{0} nat nat.has_add (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
⊢ false
```

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878899):
after the `simp`

#### [Mario Carneiro (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878900):
oh, it's nat.pow isn't it

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878901):
and then

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878905):
```
x y : nat,
h :
  @eq.{1} nat
    (@has_add.add.{0} nat nat.has_add
       (@has_pow.pow.{0 0} nat nat
          (@monoid.has_pow.{0} nat
             (@semiring.to_monoid.{0} nat
                (@comm_semiring.to_semiring.{0} nat
                   (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                      nat.canonically_ordered_comm_semiring))))
          x
          (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
       (@has_mul.mul.{0} nat
          (@mul_zero_class.to_has_mul.{0} nat
             (@semiring.to_mul_zero_class.{0} nat
                (@comm_semiring.to_semiring.{0} nat
                   (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                      nat.canonically_ordered_comm_semiring))))
          (@bit1.{0} nat nat.has_one nat.has_add (@has_one.one.{0} nat nat.has_one))
          (@has_pow.pow.{0 0} nat nat
             (@monoid.has_pow.{0} nat
                (@semiring.to_monoid.{0} nat
                   (@comm_semiring.to_semiring.{0} nat
                      (@canonically_ordered_comm_semiring.to_comm_semiring.{0} nat
                         nat.canonically_ordered_comm_semiring))))
             y
             (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))))
    (@bit0.{0} nat nat.has_add (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))
⊢ false
```

#### [Scott Morrison (Sep 29 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878906):
after the `ring`

#### [Mario Carneiro (Sep 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878947):
right, `ring` prefers monoid powers but that's not simp normal form

#### [Scott Morrison (Sep 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878950):
Okay, I see.

#### [Scott Morrison (Sep 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878951):
Nothing to be done, then!

#### [Mario Carneiro (Sep 29 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878962):
`ring ` doesn't make any attempt to be in simp normal form; if you need that you should just call `ring, simp`

#### [Mario Carneiro (Sep 29 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134878965):
but even better is to just ignore the pretty failure mode

#### [Kenny Lau (Sep 29 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments%2C%20and%20%60ring%60/near/134879165):
it's a feature!

