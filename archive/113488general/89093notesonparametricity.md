---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89093notesonparametricity.html
---

## Stream: [general](index.html)
### Topic: [notes on parametricity](89093notesonparametricity.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125810022):
Since the subject of parametricity came up, here are some papers which may be of interest and should be relatively readable for mathematicians (especially those who are also Lean users). These papers pertain to non-dependently typed languages; I don't know what differences there might be in the dependently typed setting.
* Types, abstraction and parametric polymorphism http://www.cse.chalmers.se/edu/year/2010/course/DAT140_Types/Reynolds_typesabpara.pdf
* Theorems for free! http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.38.9875

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 28 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125810743):
Reid, thanks for those links. The Fable about complex numbers was a good illustration.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 28 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125810841):
However, I think it is slightly different from transport of structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 28 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125812837):
Theorems for free! is exactly the paper that covers the right generic approach to parametricity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825527):
@**Johan Commelin** You're right that what those papers talk about isn't quite transport of structure. Instead it's the question about transfer of structure commuting with user-defined functions. For example the free theorem for `list` implies in particular that any defined function of type `list a \to list a` must commute with the "transfer of structure" equivalence `list a \simeq list b` that arises from an equivalence `a \simeq b`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825533):
(The "transfer of structure" equivalence in this case just being the list map function.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825621):
I think the reason that the scope does not extend to transfer of structure itself is that in the languages used in those papers, type constructors like `list : Type \to Type` are not definable, or at least do not have the same status as value-level functions, and so they are not in the universe of things to which one might apply parametricity theorems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825677):
But I guess if you extend the idea of parametricity to a setting (like Lean) where you can have user-defined functions which produce `Type`, then you get a parametricity result which is "one category level higher" in that it produces an equivalence between two types, rather than an equation between two values

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 28 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125826902):
I see. I'm going to give Wadlers "Theorems for free" a close look. I think it contains important ideas.

