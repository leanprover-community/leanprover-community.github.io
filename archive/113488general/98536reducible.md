---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98536reducible.html
---

## Stream: [general](index.html)
### Topic: [@[reducible]](98536reducible.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124484786):
When should I use `@[reducible] def` and when to just use `def`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493291):
`ge` is tagged `reducible`, because I don't want to double the amount of theorems I have about inequalities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493292):
I just want `a ge b` to unfold to `b le a` as soon as possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493333):
so whenever the elaborator or whatever runs into `ge` it should just think "that's notation for `le` and I will just unfold it right here and now"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493341):
"because then stuff like `rw` will work better, I will be able to rw theorems about `le` in terms involving `ge`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 01 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493393):
Which doesn't work because `rw` and `simp` match the term head literally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493485):
What if you use `abbreviation` instead of `@[reducible]`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493488):
oh yes I remember this being a problem with rw!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493494):
There was maybe even some issue about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 01 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493784):
> What if you use `abbreviation` instead of `@[reducible]`?

 `abbreviation` is `@[reducible]` + a kernel reducibility annotation, which you can most likely ignore. So use `abbreviation` if you like it more than `@[reducible] def`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493830):
what will happen if I just make everything reducible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124493831):
when is `@[reducible]` not desired?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494193):
I think you have problems with readability after a while

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494195):
You define an exciting new thing and mark it reducible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494196):
and want to prove basic lemmas about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494199):
but the moment Lean does anything with it, it unfolds the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124494205):
and it's then harder to use because you have to keep folding it up again when you want to apply the previous lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558714):
Should I make these reducible?
```
def orbit : set X :=
{ y | ∃ g : G, g • x = y }

def stab : set G :=
{ g | g • x = x }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 03 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558770):
the answer is almost always no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 03 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558782):
instead, you should have a simp lemma that says `g \in stab x <-> g \bu x = x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Breducible%5D/near/124558783):
aha

