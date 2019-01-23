---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40911classvsdefagain.html
---

## Stream: [maths](index.html)
### Topic: [class vs def again](40911classvsdefagain.html)

---


{% raw %}
#### [ Patrick Massot (Jul 16 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776099):
Variation on a well-known theme: should uniform continuity of a map `f` between uniform spaces `a` and `b` be a `def` or a `class`? Or should we bundle `f` and its uniform continuity?  Currently we have a `def` and no bundling. As usual, this is all convenient to prove properties of individual maps, or compositions of two such maps. Now let's get functorial. I want to promote each such `f` to a map between the respective Hausdorff completions of `a` and `b`.  Of course in math this would be called `completion_lift f`. This currently doesn't make sense in mathlib, we need a term `h : uniform_continuous f`. So we could write `completion_lift f h`. But `f` can be inferred from `h`, so common sense dictates it should be an implicit argument, and we end up with `completion_lift h`. And it looks *weird*. And it gets worse when stating and proving properties of `completion_lift`, especially functoriality that should read `completion_lift f' ∘ f = (completion_lift f') ∘ completion_lift f ` but actually reads `completion_lift (uniform_continuous.comp h h') = (completion_lift h') ∘ completion_lift h`.

#### [ Patrick Massot (Jul 16 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776108):
What should we do?

#### [ Patrick Massot (Jul 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776783):
See https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean for the concrete situation

#### [ Patrick Massot (Jul 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776974):
I had a lot of fun doing all this after proving the universal mapping property for completions. It was fun because it was really very close to a paper and pencil proof. But I wouldn't find it fun to do this ten times. I can't wait until we get nice abstract non-sense in mathlib. How far are we from merging @**Scott Morrison** PR? Has anyone heard from Scott recently?

#### [ Mario Carneiro (Jul 17 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778526):
The last few times I've been asked this I advocated the bundled function approach and it's worked well thus far

#### [ Patrick Massot (Jul 17 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778652):
Question is then how to handle the existing code base? How to avoid duplicating too much stuff. I guess we still want to keep the current Prop

#### [ Mario Carneiro (Jul 17 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778896):
Hm, good point. Is it possible to define `completion_lift f` without the continuity assumption?

#### [ Mario Carneiro (Jul 17 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778901):
i.e. take a default value

#### [ Patrick Massot (Jul 17 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778911):
It depends on `dense_embedding.extend` we were discussing earlier today

#### [ Patrick Massot (Jul 17 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778935):
see https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L95-L96

#### [ Mario Carneiro (Jul 17 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778936):
`dense_embedding.extend` doesn't require continuity

#### [ Mario Carneiro (Jul 17 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778979):
oh, weird, a unique exists

#### [ Patrick Massot (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778993):
well, it doesn't require it until `ext_e_eq`

#### [ Patrick Massot (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778999):
unique exitsts are everywhere in this abstract nonsense business

#### [ Patrick Massot (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779005):
That's an important part of the universal property

#### [ Mario Carneiro (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779008):
oh sure, but mathlib basically never uses it

#### [ Mario Carneiro (Jul 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779056):
it always defines the unique thing with a concrete term

#### [ Patrick Massot (Jul 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779058):
that's because it lacks basic category theory support

#### [ Patrick Massot (Jul 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779066):
I don't want a definition with a concrete term, I want the abstract interface, as in my file

#### [ Mario Carneiro (Jul 17 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779069):
no, there are plenty of places where math dictates a unique existence, it's just easier to work with terms

#### [ Mario Carneiro (Jul 17 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779079):
If you look at scott's development I think he's done the same

#### [ Patrick Massot (Jul 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779121):
even the explicit construction of `completion` and `to_completion` will need to be complemented by a uniqueness up to unique iso result. This is my plan for tomorrow, as well as deducing that completion of a product is isomorphic to product of completions

#### [ Mario Carneiro (Jul 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779122):
I'm sure Kevin can discuss his experiences with `sqrt_exists`

#### [ Patrick Massot (Jul 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779137):
Probably the best is to have an explicit term *and* a uniqueness lemma

#### [ Mario Carneiro (Jul 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779148):
right

#### [ Mario Carneiro (Jul 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779152):
the uniqueness lemma says something like `x = my_thing <-> property`

#### [ Patrick Massot (Jul 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779198):
I still don't know how to do that in this case. Because that `de.ext` is only half the construction. Then it must still descend to a quotient (lift to a quotient in Lean-speak)

#### [ Patrick Massot (Jul 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779201):
https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L99

#### [ Mario Carneiro (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779202):
Still, you've constructed the term

#### [ Mario Carneiro (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779208):
`g` in the proof

#### [ Patrick Massot (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779210):
this uses uniform continuity

#### [ Patrick Massot (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779214):
no, `g` needs `compat`

#### [ Mario Carneiro (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779220):
right, it's defined by lift on the quotient

#### [ Mario Carneiro (Jul 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779283):
I'm not asking you to prove the theorem without the assumption, or even do the construction without uniform continuity

#### [ Mario Carneiro (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779292):
I want to see if you can do a similar thing to what I did for `extend`

#### [ Patrick Massot (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779295):
Then I don't understand what you suggest

#### [ Mario Carneiro (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779297):
If `A` is empty, is `completion A` also empty?

#### [ Patrick Massot (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779300):
yes

#### [ Patrick Massot (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779303):
(I hope)

#### [ Patrick Massot (Jul 17 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779342):
In my mind it is certainly empty

#### [ Patrick Massot (Jul 17 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779346):
but I'm not an expert in zerology

#### [ Mario Carneiro (Jul 17 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779426):
Then you can follow a similar proof to what I did. Define `completion.extend f` by cases on `uniform_continuous f`. If it is, do the regular thing. Otherwise, we can pick an arbitrary element of `B` by `choice`. We know it is nonempty because we are given an element of `completion A` so we can prove `A` is nonempty, so `a : A` means `f a : B`

#### [ Patrick Massot (Jul 17 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779662):
Oh. This is twisted

#### [ Patrick Massot (Jul 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779781):
I'll try that tomorrow, before moving on to products. It seems we don't have an instance for completion of a product of complete spaces, so there will be preparation work.

#### [ Patrick Massot (Jul 17 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779858):
If I'm lucky I'll even get a `dense_embedding.extend` without inhabitants in mathlib when I'll wake up :wink:

#### [ Patrick Massot (Jul 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779882):
@**Kevin Buzzard** don't hesitate to have a look at the current state of https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean and comment. It's all for the perfectoid project.

#### [ Kevin Buzzard (Jul 17 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129798324):
Patrick I'm really grateful for all of this. The perfectoid project shouldn't be too hard to do. The hard part with schemes was proving that the structure presheaf on Spec(R) was a sheaf because this had all sorts of unexpected pitfalls. The analogous statement for adic spaces isn't true -- an affinoid adic space is *defined* to be an affinoid pre-adic space Spa(R) for which the structure presheaf happens to be a sheaf, so that is a huge hurdle that we don't have to deal with. Completions are, I think, the main technical issue left, and you are dealing with them. I will try and focus on continuous valuations.

#### [ Johan Commelin (Jul 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129917105):
```quote
Has anyone heard from Scott recently?
```
I haven't seen Scott here for a while. Maybe it's time for (winter?) holidays down under?

#### [ Patrick Massot (Jul 19 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129921084):
Maybe. He also doesn't answer emails.

#### [ Patrick Massot (Jul 19 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129931031):
His webpage revealed https://tqft.net/calendar/ which pretty clearly indicates winter vacations.

#### [ Johan Commelin (Jul 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129935705):
It also means he should be back next week (-;


{% endraw %}
