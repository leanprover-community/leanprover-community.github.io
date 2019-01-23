---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46183universalpropertiesagain.html
---

## Stream: [maths](index.html)
### Topic: [universal properties again](46183universalpropertiesagain.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129954498):
Since everybody is doing universal properties and fight reluctant universes and type class inference, let me try to get help. Remember I'm working with Hausdorff completions of uniform space. I have a nice proof of their universal properties and I'd like to run the usual stuff on it. Especially today I need uniqueness for this construction. So I forget about my explicit construction and try to run abstract arguments. See https://gist.github.com/PatrickMassot/beb3b40bec8888b3061d9c410c229467 First trouble: I had to setup explicit universe level in order to get Lean to accept `compare`. Then the instances buried in the structure are hard to get out. I guess I'm on a completely wrong track here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129955775):
@**Mario Carneiro** I'm afraid you were busy typing some advertisement when that thread started (and stopped).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129955820):
Do you have any hint for me?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956129):
What explicit universe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956140):
u

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956197):
Oh yes that is true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956205):
If I put `Type*` everywhere you see `Type u` I can shadowing errors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956216):
Same if I try `Type v` for all beta variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956224):
That's the same thing I was talking about with Kevin

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956242):
the `u` in `space : Type u` is an internal universe variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956258):
so if you make it `v` instead then you will have a bad day

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956295):
so that means you have to explicitly make them the same, which means you need to name the variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956363):
same as who?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956389):
same as `α : Type u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956393):
I'm having a bad day even with named u

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956414):
At least I don't see `.{u}` anywhere in your file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956427):
I get an error in `uniform_continuous_compare`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956433):
I'm fine with α and its completion living in the same universe. That sounds nice and is actually true for my explicit construction (I think)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956443):
about synthesized instance different from inferred

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956453):
exactly, that's the heart of my question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956514):
But why beta has to be in the same universe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956515):
That's easy enough to fix, use `letI` instead of  `haveI`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956544):
Better yet, add this
```lean
attribute [instance]
  completion_package.uniform_structure
  completion_package.completeness
  completion_package.separation
```
and it won't be necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956587):
beta is also an internal universe variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956661):
I'm sure I've seen this trick in the sheaf discussion, but I forgot. Thanks a lot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956668):
it doesn't *have* to be in the sense that you can define it with a different variable, but this will make your life harder and furthermore it doesn't mean what you think it means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956712):
It is impossible to define a field which quantifies over multiple universe levels

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956728):
I was worried I would have a lot of trouble with these instances but this trick seems to fix everything (including removing `@uniform_continuous` ugliness in the definition of `compare`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956744):
that is, something like this doesn't work: `(lift : ∀ {u} {β : Type u} (f : α → β), space → β)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956756):
where `u` is somehow quantified inside the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956821):
What do you think I thought it meant and what would it actually mean? (Grammar clearly tell us we are in the middle of a tricky discussion involving multiple universes)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956836):
Oh, `(lift : ∀ {u} {β : Type u} (f : α → β), space → β)` is what I would have liked to mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956846):
But I don't mind, really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956877):
Luckily, in the vast majority of cases, having a lift in universe u implies a lift in higher universes too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956890):
usually this is due to some zfc style size considerations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957005):
I certainly don't want to run into zfc size considerations. Actually I mostly want to prove that the completion of a product is nicely isomorphic to the product of the completions, taking the opportunity to try abstract non-sense in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957143):
I think you should just stick to universe u

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957223):
it's not quite as strong a theorem as you could state, but all the constructions will go through without any added headache

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957318):
Great, I like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957364):
I'll try to move on. Thanks!

