---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43468degreesofpolynomials.html
---

## Stream: [maths](index.html)
### Topic: [degrees of polynomials](43468degreesofpolynomials.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 07 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/degrees%20of%20polynomials/near/133505238):
@**Chris Hughes** told me a while ago that the degree of a polynomial is a bit of a nightmare, because the zero polynomial has degree -1 or -infinity or something, and these are not nats. It seems that he went with `degree` into `with_bot nat` and `nat_degree` into `nat` (with nat_degree of 0 being 0). I am now faced with goals like

```
hf : ¬f = 0,
hg : ¬g = 0,
hd : nat_degree f < nat_degree g,
⊢ degree f + ↑(nat_degree g - nat_degree f) = degree g
```

There's a lemma saying that if `f` is non-zero then `degree f = ↑(nat_degree f)` but if I go down that route then I can't seem to use `nat.cast_add` etc, probably because although `with_bot nat` is an add_monoid, the coercion is not the usual one from nat to an add_monoid with a 1, it's like the coercion from nat to int. I think that this may mean that all of the lemmas of the form `↑(m+n)=↑m+↑n` for add, mul, le etc all need to be written by hand for this coercion from nat to `with_bot nat`, just like we have `int.coe_nat_add` etc. Am I correct? I ask because I need them for Hilbert Basis and I may as well get on and do them if they need doing. Or am I missing a trick?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 07 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/degrees%20of%20polynomials/near/133505345):
I think `with_bot.coe_add` is the lemma you need.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 07 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/degrees%20of%20polynomials/near/133505354):
oh boy -- so I'm right but they're already there? Thanks Chris!

