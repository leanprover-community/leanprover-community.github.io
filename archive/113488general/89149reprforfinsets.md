---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89149reprforfinsets.html
---

## Stream: [general](index.html)
### Topic: [repr for finsets](89149reprforfinsets.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 20 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364636):
Is there a way to define a has_repr instance for finsets ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 20 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364637):
I would like to run some algorithms with eval

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 20 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364702):
One option: use `finset.sort`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 20 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364765):
oh ! that's cool, i never noticed it. Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 20 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364782):
No problem. If you come up with something useful, please share it with us.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364852):
do you need a total order to use it? You could probably get rid of that constraint if you convert each element to string and then sorting the result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364936):
yes total order is an assumption. good idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364939):
By “get rid of,” you mean push the total order off onto the string, right? That's not a bad idea for all of the constraints.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365001):
Yes, we need a total order on strings but this is readily available. Basically, what I meant was "weaken the assumptions to make it more generally usable". What are the other constraints?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 20 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365019):
Right, that's what I thought. So `finset.image` to `string` and `finset.sort` the result.

```
variables (r : α → α → Prop) [decidable_rel r] [is_trans α r] [is_antisymm α r] [is_total α r]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365103):
Not quite. In this situation, `α` is now `string` so `r` is now the linear order on strings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365291):
I don't understand. Something like `finset.sort (<) ∘ finset.image to_string` doesn't work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 20 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365353):
there are missing instances for string, they shouldn't be too hard to write

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365478):
Yes it does. But because we're using `(<)` on string, we have weaker assumptions about `α` and we can discharge the assumptions about `string` once and for all. That means that `to_repr` has type:

```lean
def to_repr {α} [has_to_repr α] : finset α -> string
```

instead of

```lean
def to_repr {α} [has_to_repr α] [decidable_linear_order α] : finset α -> string
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365628):
That of course depends on how `to_string : α → string` is defined for your `α`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365630):
You also need to make sure that  has_repr.to_repr for  \alpha is injective (and maybe use map instead of image)
but that's not so interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365654):
Interesting, I didn't think of injectivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365661):
You could get around it by first converting to a `multiset` I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 20 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365720):
But injectivity might be a good law to have in `has_to_repr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 20 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128380291):
It's a good point that we can sort strings here, I hadn't thought of that. I'll add a has_repr instance for multiset and finset then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 20 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128381791):
While you're at it, you could add one for pnat (`nat.repr \circ subtype.val`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 20 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382396):
or `subtype.has_repr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 20 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382427):
I also made an instance of has_to_string pnat (when I was goofing around with pnat a few weeks ago).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 20 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382504):
Why were you goofing around with pnat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 20 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382797):
I was trying to get on top of exactly what one should do when defining a new structure in Lean. If I had to define pnat I would start by writing down the definition as a subtype, and then I realised that I would not really know what to do next. So I read pnat.lean quite carefully to try and get a feeling for it. I then read `real.lean` for the same sort of reason.


{% endraw %}
