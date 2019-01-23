---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/58383495multiplicity.html
---

## Stream: [PR reviews](index.html)
### Topic: [#495 multiplicity](58383495multiplicity.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 29 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148810765):
`multiplicity` requires a decidable dvd argument currently. However there are applications where we don't have decidable dvd in general but we do for particular elements, in particular, for multiplicities of roots of polynomials over a comm ring, it is decidable whether or not `X - C a` divides a polynomial but not easily in general - the divisor needs to be monic. What's the best way of dealing with this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855628):
This is probably a noobie question, but why is it decidable whether `(X - C a)` divides some polynomial? Are you assuming that `a` comes from a ring with decidable eq?
Anyway, I would personally just ignore the problem. If some lemma doesn't work in generality without decidability, just assume it as an argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855644):
I am assuming decidable equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855656):
I guess they're equivalent, because `a = b` iff `X - C a` divides `X - C b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855790):
```quote
I am assuming decidable equality
```
 So then, what is the problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855802):
Aaah, wait.... This is of course not the same as being classical.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855811):
That divisibility of polynomials is not decidable in general even with decidable equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855813):
I should stop thinking about this stuff. I've got enough "real-math" problems :rolling_on_the_floor_laughing:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855816):
is that true? it's not clear to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855866):
What? That I have enough problems? :upside_down: :grinning_face_with_smiling_eyes:  I do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855876):
divisibility by `X - C a` is decidable because it's true iff the polynomial is zero when evaluated at `a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855896):
but I could imagine a more complicated polynomial factoring algorithm that decides divisibility

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855921):
You'd need decidable divisibility over the base ring at least

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855932):
Divisbility by monic polynomials is easily decidable the way I have it set up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148856160):
Over a semiring you'd also need decidable additive divisibility.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857274):
```quote
Over a semiring you'd also need decidable additive divisibility.
```
 You mean decidable addibility?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 30 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857281):
he means that this needs to be decidable: whether there is c with a+c=b

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857325):
I think the name consistent with convention is probably decidable subtractibility.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857344):
You remove axioms and this is what you get :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857403):
maybe it is possible to work in the splitting field of the ring, and check if the roots match up there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857445):
I guess it should be decidable by some analogue of algebraic numbers, although strange ideal quotients may make things harder than in Q

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 30 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148858045):
The splitting field won't have decidable equality though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/150679435):
```quote
but I could imagine a more complicated polynomial factoring algorithm that decides divisibility
```
 Factoring is thorny over a general ring. For example $$(x+1)(x-1)$$ and $$(x+3)(x-3)$$ are both equal to $$x^2-1$$ over $$\mathbb{Z}/8\mathbb{Z}$$. It's a bit terrifying -- again over $$\mathbb{Z}/8\mathbb{Z}$$, $$4x^2+x$$ divides $$2x^2$$ even though 4 doesn't divide 2.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/152029219):
@**Chris Hughes** Would it be possible to split this PR into smaller pieces? For example: 1 PR that adds `enat`; 1 PR that makes lots of little changes in several files; 1 PR that adds the notion `multiplicity`; and finally 1 PR that replaces `padic_val` with `multiplicity`.


{% endraw %}
