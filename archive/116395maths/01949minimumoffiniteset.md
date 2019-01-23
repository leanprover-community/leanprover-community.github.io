---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01949minimumoffiniteset.html
---

## Stream: [maths](index.html)
### Topic: [minimum of finite set](01949minimumoffiniteset.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993170):
```quote
with `sup` you don't need to use `iget`. `max` is the better name but I think `sup` has the better behaviour.
```
What is this sup you are talking about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993263):
`finset.sup` defined, or at least used in `multivariate_polynomial`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993324):
Only defined for `semilattice_sup_bot`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993423):
That's unexpected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993424):
Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993428):
I still can't use it though. I'll try harder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993435):
Why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993443):
It takes the sup of the image of a given function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993499):
failed to synthesize type class instance for ⊢ semilattice_sup_bot ℝ

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993510):
It means I need to learn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993514):
what is a semilattice_sup_bot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993517):
reals aren't a semilattice sup bot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993519):
It needs a least element of the type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993522):
`ennreal` is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993533):
the nonnegative (in your case, positif) reals also is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993723):
Using the type of nonnegative real would probably mess up lots of things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993749):
in my norms.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993759):
Incidentally, I just defined some stuff on nonnegative reals this week...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993770):
Like that it is a comm_semiring, and its topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993831):
Nooo! I don't want to do topological commutative semi-ring theory!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993927):
Well, it is very useful for defining the standard simplices. Because it takes care of the condition that all the coordinates are positive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 23 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993946):
is this part of your bigop project? I am dying to have useable matrices and summations in Lean, maybe I will take a look

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126994048):
No, I'm back to calculus while I wait for omega/cooper to be usable, just in case it makes using nat possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 23 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126994149):
well, studying cooper was also on my recreational to-do list, so i'll have to get on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126994166):
I was not able to import it in any way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995176):
@**Johannes Hölzl** The point of my questions about max is to try to get a norm on ℝ^n. But this goes through the dreaded definition of Lean metric spaces. Could you get me started by doing
```lean
instance metric_space.fintype_function {α : Type*} [metric_space α] {β : Type*} [fintype β]
: metric_space (β → α)
```
(using the max distance between images) I think I could manage from there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 23 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995281):
Do you want to use the max distance in general, or just because we don't have sqrt yet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995324):
We started using max on products a long time ago. It's partly for lack of square root tooling, but I also don't see why square root would be better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995353):
The current state of this story is https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995399):
(with products of two types only)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995564):
(and added segfault)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995569):
(no)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995576):
(assertion violation)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995619):
The version up at github has no assertion violation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995689):
And I was linking to this only so that Johannes could see my definition of normed group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 23 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126996448):
For me somehow the Euclidean distance (l_2-norm) as the canonical distance. But yeah, we can first start with the max-distance. That's one advantage of uniform spaces: the produce construction is more canonical :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126997326):
"more canonical" :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126997332):
We didn't formalise canonical yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126997334):
let alone make it a partial order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 24 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127000110):
@**Patrick Massot**  https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105 here is the metric space for finite function.
@**Simon Hudon**  I think I will change `max` to my version of `maxi`. How would you do these kind of proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 24 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127000293):
We can make `imax` (I usually use the `i` as a prefix) as an alternative to `max` defined for inhabited sets if you like. If it is defined as `max.iget` then we get all the theorems for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 24 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127000354):
I want to make `finset.max` a special case of `finset.sup` by defining a `with_bot A := option A`  type which extends the order with `none <= some a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127002306):
I still don't see cases where the current `max` has advantages, or how to do proofs properly. Using `with_bot`, could we just use `sup` instead of the current `max`, and use `sup` + `iget` as `max`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 24 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127003581):
@**Johannes Hölzl**  Sorry, I haven't been following. Which proofs do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 24 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127012241):
Using `with_bot`, `sup` over `with_bot` would be the same as `max` is currently (in particular, it would return an `option`), and then you could postprocess the result with `iget` if that makes sense in your application. I like the way `max` works at the moment because it lets you work relationally with max, i.e. "x is the max of s" rather than a term "max of s" which may or may not actually be a max of s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 24 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014486):
```lean
def maxi [decidable_linear_order β] [inhabited β] (s : finset α) (f : α → β) : β := (s.image f).max.iget

lemma maxi_empty : (∅ : finset α).maxi f = default β
```

I don't understand how `maxi_empty` is useful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 24 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014487):
@**Simon Hudon** the proofs in https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105 Its a little bit of a special case (we are working essentially in R >= 0) and we explicitly want `s = empty -> max s = 0`. Without adding my own rules for `maxi` (a.k.a. `imax`) I would need a lot of annoying case distinctions (ala `finset.univ = empty`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 24 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014574):
At least at the beginning `maxi_empty` is helpful: the following rules have a special condition to compare to the default when `s = empty`, which can be resolved using `by simp * at *`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 24 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014687):
I see: `(hd : s = ∅ → b ≤ default β)` is what you mean. So with an `option` result, you don't need that? But you still think using `inhabited` is better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 24 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014782):
```lean
lemma le_maxi_of_forall {b : β} (hb : ∀a∈s, b ≤ f a) (hd : s = ∅ → b ≤ default β) : b ≤ s.maxi f
```

looks a lot [like](https://github.com/leanprover/mathlib/pull/133/commits/351dd66c84cc45c53f7de49836f0086d35071327#diff-e7d41a6a4fb2225734fc2fb30e4dceeeR1069)

```lean
theorem le_max_of_mem {a b : α} {s : finset α} (h : a ≤ b) : a ∈ s → a ≤ max b s
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 24 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014831):
BTW, I'm really just trying to wrap my head around the use of `inhabited` and why it's better. I'm not trying to claim mine is universally better or anything. Since I haven't tried to implement it or use it myself, I don't have an intuition for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 24 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015010):
`le_maxi_of_forall` is slightly different, as it is about a lower bound. Either `s` is empty, than you compare it to the default: handling the case where `s` is empty, **or** where the default value is well defined. In your `le_max_of_mem` case you show that an element is a lower bound, also there is no difference between non-empty `s` and `b` being well defined.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 24 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015170):
Right. But they both deal with a “default,” whether that be `b` in `le_max_of_mem` or `default β` in `le_maxi_of_forall`. That's the similarity I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 24 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015318):
I'm not a fan of these `inhabited` solutions because `default` is (supposed to be) a completely arbitrary element with no semantic value. It's not supposed to be compared to stuff because in a given structure you have no idea what it could be. If it happens to work out in some type, that should be treated as coincidence and should not be relied on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 24 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015323):
which is why I find the hypothesis ` s = ∅ → b ≤ default β` very strange

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 24 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015335):
if you care about having a particular fallback value, there is `get_or_else` for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127197478):
@**Mario Carneiro** and @**Johannes Hölzl** did you decide something about this `max` debate? Can I use https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105 or is it already outdated with respect to current mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127197858):
I'm not sure yet. I didn't try to write the proof only using the `option` variant of `max`. @**Sean Leather** did you use `max` already?
But we have a new possibility now: use `nnreal` to define `dist` and `norm` (or maybe `nndist`). Then we can use `sup` and don't need to worry about the empty case. It should still easily embed into `real`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127197894):
I don't understand how `nnreal` could help here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127198066):
Please, please, please don't use nnreals for dist and norm! I tried to do something like that for Gromov hyperbolic space (except that I needed distances taking the value infinity, so I used ennreal). And then I had to start everything over again using ereal once I was deep enough in the theory, when I had to do serious computations and inequalities, as the fact that subtraction on ennreal (or nnreal, or nat) is truncating things makes everything a total mess -- I think Patrick has been bitten by this quite a few times, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127198135):
Oh yes, I don't want more crazy substraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127200413):
```quote
I'm not sure yet. I didn't try to write the proof only using the `option` variant of `max`. @**Sean Leather** did you use `max` already?
```
@**Johannes Hölzl** No, I haven't started using the `max` in mathlib.

