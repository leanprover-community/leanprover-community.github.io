---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43359imagevsmapandinjective.html
---

## Stream: [maths](index.html)
### Topic: [image vs map and injective](43359imagevsmapandinjective.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 22 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128459841):
In `data.finset`, `finset.map` is defined as mapping an `embedding` or an injective function over a `finset`, and `finset.image` is mapping a function over a `finset`. Other mathlib components (e.g `set`, `multiset`, `list`, `array`, etc.) do not make this distinction using this naming scheme.

I think there is a useful distinction to be made here. For example, grep `data/list/basic.lean` for `injective`: these declarations could be changed to use `embedding`. But I'm not sure about the `image` vs `map` naming. Is this a standard thing? If so, can we implement it for other components? If not, can we come up with a meaningful naming distinction for mapping a function and mapping an injective function and implement that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128474541):
The purpose of the distinction is that while `finset.map` and `finset.image` do the same thing, namely compute the image of a finite set under a function, they do so under incomparable hypotheses. Some hypothesis is necessary because we somehow need to ensure that the resulting `finset` has no duplicates. `finset.image` requires the target to have decidable equality, which is a free assumption when doing classical mathematics. `finset.map` requires the function to be injective.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128474621):
`finset.map` is also much cheaper computationally, since it just has to apply the given function n times. I guess this is where the name `map` comes from; computationally, it's just mapping a function over a data structure (the `Prop` part does not exist computationally). `finset.image` has to check the resulting list for duplicates and remove them, which takes time O(n^2).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128474724):
As far as the other types you mentioned are concerned, the "positive" types `multiset`, `list`, `array` have no constraints analogous to the uniqueness in a `finset`, so we can just use the `map` implementation in all cases. For the "negative" type `set` (`set t = t -> Prop`) we can't really hope to compute the image, so we can just use the logical definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586002):
@**Reid Barton** Thanks for the very informative response! I neither noticed the `[decidable_eq β]` on `finset.image` nor realized its impact, so that's good to know.

I'm still not quite clear on what should be named what. Let me propose what I infer and anybody can shoot it down:

* `set.image` is the [logical image](https://en.wikipedia.org/wiki/Image_(mathematics)) of a set.
* `finset.image` is the analog to `set.image` for a finite set. Since `set.image` involves a equality test, it makes since that `finset.image` require `decidable_eq` on `β`.
* `list.map`, `multiset.map`, etc. are the standard (functor) mappings.
* `finset.map` is the implementation equivalent of `list.map`, etc. but requires injectivity to preserve the `finset` properties.

If I describe the situation as above, it makes sense to me.

That said, there are some cases where mapping an injective function over a list is useful. Is it worth creating an additional definition for `list.map` using `embedding` along with associated theorems?

```lean
def list.imap (f : α ↪ β) : list α → list β := list.map f.to_fun
```

I don't have any good thoughts on the name. Is there a standard here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586287):
I don't see a reason to have such a definition, since you can just write `list.map f` with the inserted coercion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586401):
Right. The only reason would be for convenience, not for necessity of proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586527):
```quote
The only reason would be for convenience, not for necessity of proof.
```
In fact, however, could you not say the same thing about `finset.map`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586591):
The main difference, of course, is that `list.map` is useful without injectivity and `finset.map` is not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586724):
I mean that there is no gain besides a slightly longer name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586731):
If you want to use `map` on an injective function, just use it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586773):
with `finset.map` there is a clear difference since the definition is different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128587364):
Oh, I see. You're referring to the use of `list.map` with an injective function. I was referring to the convenience of writing proofs for `map` with injectivity: you wouldn't have to specify `injective f`. Nonetheless, I concede that it's a pretty weak motivation.

