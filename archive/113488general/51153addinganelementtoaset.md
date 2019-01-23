---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51153addinganelementtoaset.html
---

## Stream: [general](index.html)
### Topic: [adding an element to a set](51153addinganelementtoaset.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 26 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330334):
The notation `+` is attached to `has_add.add : X -> X -> X`. Mathematicians use `+` in more general ways though. I find myself wanting to write `r + J` for `r` an element of, and `J` a subset of, an additive abelian group (`J` is a subgroup in fact). This is standard notation in mathematics and I suspect I can't have it given the set-up we have. Does anyone have any thoughts as to how I might try and represent such an idea in Lean? I can make the object I want no problem, the issue is simply that I want the notation to be as close to what a mathematician would write as possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330459):
It's called a coset.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330461):
specifically, a left coset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 26 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330474):
I've seen cosets in group theory but unfortunately this is an additive group ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330478):
`additive`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 26 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331527):
How scalable is this `additive` idea I wonder? I recently wanted a free abelian group with group law multiplication but ultimately settled on group law addition because thay was what the finsupp construction gave me and I couldn't face cluttering everything up with additive and multiplicative everywhere.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331592):
as scalable as I made it in my constructive tensor product

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331599):
```lean
def free_abelian_group : Type u :=
additive $ abelianization $ free_group α
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331610):
and the proof that it works is that I built the whole tensor product out of the free abelian group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 26 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331623):
`(+ r) '' J`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 26 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331660):
I would prefer `((-) r) ⁻¹' J`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 26 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331735):
I would prefer readable notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 26 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130332818):
I would prefer the notation mathematicians use, i.e. what we can't have.

