---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52991makeexplicitargumentimplicit.html
---

## [general](index.html)
### [make explicit argument implicit](52991makeexplicitargumentimplicit.html)

#### [Zesen Qian (Jul 30 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130584404):
Hi, is it possible to temprorarily make an argument implicit? Say, instead of `id bool true`, I write something like `id _ true` and let the elaborator to infer the omitted argument for me. (id : \forall A, A -> A is completely explicit)

#### [Zesen Qian (Jul 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585249):
funny, seems lean can already do it exactly like I demonstrated. never knew that.

#### [Reid Barton (Jul 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585255):
You can already write `id _ true` and the elaborator will infer the argument (though `true` is a `Prop`, not a `bool`).
Did you have something else in mind?

#### [Reid Barton (Jul 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585263):
Ah, okay.

#### [Reid Barton (Jul 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585319):
A useful trick with this is also to define a notation ``local notation `id'` := id _`` if you want to make an argument implicit in an entire file/section of code.

#### [Zesen Qian (Jul 30 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585371):
@**Reid Barton** good, thanks.

