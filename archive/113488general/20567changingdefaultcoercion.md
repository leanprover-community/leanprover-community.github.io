---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20567changingdefaultcoercion.html
---

## Stream: [general](index.html)
### Topic: [changing default coercion](20567changingdefaultcoercion.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125456190):
I've just defined the integers mod n, and since they are a `comm_ring` there is a default coercion from `int`. However rather than using the default coercion, it would be nicer to have `quotient.mk` as the coercion. Is there a way to change this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125456275):
I think if you declare the `has_coe` instance, it will use your instance whenever applicable before even trying the coercion from `int` to arbitrary `comm_ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 20 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125457130):
Is there a risk of a diamond here though?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125457174):
You mean like when you have multiple inheritance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 20 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125459795):
```quote
Is there a risk of a diamond here though?
```
What's the diamond? I think that the same idea has been used for coercions from `nat` to `int`. The only risk is if I make a `coe` from `Zmod` to `int`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125460970):
the diamond occurs in 5 years' time when someone else imports your code and then writes down some innocuous-looking coe and stuff doesn't work. My question is whether this is a possibility

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125461446):
Not for any notion of diamond that I've worked with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 20 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125463614):
Somehow what I was concerned about is that if someone one day writes down a coercion from the integers mod n to another comm_ring then they will have to deal with the issue that they now have two coercions from int to the other comm_ring which may not be defeq.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 20 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125463925):
You could define a local instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 20 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125463970):
That way only people editing your file would have to deal with this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 20 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125466482):
@**Kevin Buzzard** I don't think coercions are transitive, so if something is coerced from integers to integers mod n to R, then it will appear as two up arrows. I think these issues happen anyway with int to rat to real etc, and there are a load of lemmas proving equivalence of different permutations of coercions. I don't want a local coercion, because the quotient coercion is the most useful for everyone.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125477762):
There is definitely a "diamond risk", but of an even more trivial variety than an actual diamond: you are talking about two arrows from A to B in the category of typeclass instances, which is only acceptable (by my rule of thumb) if they are defeq, which presumably defeats the purpose of having a second coercion.

That said, in the specific case of replacing the default coercion, you can do it by similar methods to the ones used for `int.of_nat`, as Simon mentions, although you will have to prove lots of lemmas to replace the ones that `int.cast` gives you, and users will need to know that you are doing this since they have to refer to different lemmas.

Coercions are transitive, in the sense that if there is `has_coe A B` and `has_coe B C` and a `C` is needed where `A` is given, Lean will insert a single `coe` up-arrow with a composite typeclass instance. However, mathlib has a simp lemma explicitly to break these composite arrows up, because they work poorly with other simp lemmas that are all keyed to single coercions.


{% endraw %}
