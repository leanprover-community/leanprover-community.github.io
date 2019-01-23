---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25920structureequality.html
---

## Stream: [general](index.html)
### Topic: [structure equality](25920structureequality.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218426):
How do we prove equality of two terms whose type is a structure mixing data and Prop? I would like to prove each data holding field matches. I thought this has something to do with `no_confusion` but I can't get it to work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218697):
Hum, it seems I can uses cases to access stuff here again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218843):
```lean
structure thing := (a : ℕ) (b : ℕ) 

example (a b c d : ℕ) : thing.mk a b = thing.mk c d :=
begin
   rw thing.mk.inj_eq,
end
```

`simp` also works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218950):
I'm not sure what to do if you haven't done cases.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129219284):
You can also use `congr` or `congr'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 06 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129219344):
What's the difference between `congr` and `congr'`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129219395):
`congr'` takes an argument like `congr' 3` to ask for three iterations of congruence. `congr` just keeps going until it can't anymore. Often, `congr` goes too far

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129221654):
Thanks Chris and Simon. `congr` and `simp` do nothing, `cases` both sides and `rw pequiv.mk.inj_eq ; cc` did the trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129221846):
Sorry, I didn't mention, in either case, you need to `cases` both sides

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222086):
Correction, after cases both sides, `congr ; cc` also works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222164):
and `congr ; tauto` of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222707):
I'm wrapping up a round of optimization of `tauto`. When it works, it should be faster than `cc`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222733):
(and now, it should work more often than before)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222738):
Great!

