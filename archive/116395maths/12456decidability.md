---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12456decidability.html
---

## Stream: [maths](index.html)
### Topic: [decidability](12456decidability.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882267):
tldr; why do we have `linear_order` and `decidable_linear_order`?

I was bitten recently by the fact that some type classes are built on `linear_order`, while some theorems require `decidable_linear_order` (i.e., a linear order in which the relation `a ≤ b` is decidable).
I think I understand why decidability is important from  a practical point of view: you want `dec_trivial` to be able to compute, to decide simple things, say on finite sets. What I don't get is why everything could not be said to be decidable, with the caveat that you should not use `dec_trivial` when something is not computable. Maybe with the possibility to replace noncomputable stuff by computable ones in some types for which you really care about computability. 

Could we base all mathlib on `decidable_linear_order`, removing completely `linear_order`or would it have dreadful consequences? Let me emphasize that I don't care at all about constructivist mathematics, or the strength of axioms used to prove theorems: my question is really about practical consequences, not philosophical ones -- although I can perfectly hear an answer of the form "there is no practical consequence, but we want to keep it separate for philosophical reasons". 

NB: the following typechecks
```lean
noncomputable instance zou {α : Type u} [h : linear_order α] : decidable_linear_order α :=
{
  decidable_le :=
  begin 
    assume a b,
    apply classical.dec,
  end,
  ..h
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882331):
because `abs` wants to be computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882335):
(now it is not the case that `abs` is computable implies the order is decidable, which is something I would want Lean to know, because currently we have a noncomputable `abs` for real)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882398):
What do you mean, it wants to be computable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882423):
it means we want `abs` to be computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882468):
actually I don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882474):
I'll let other people answer this question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147885253):
Here's a guess. Some arguments work fine without decidability, some need decidability. As a mathematician I used to barely notice this because the moment I needed some prop to be decidable I'd just switch on `classical.decidable_prop` or whatever it's called and keep going. More recently I realised that there was a better way to do this -- instead of just switching this on all the time I'd just add the relevant decidability instances to the objects in the results that needed them. This seemed like a more canonical thing to do, because that way people who do care about these things can use my results anyway. Is that an answer to the question or is there more to it in this case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147885430):
I think sometimes you define `linear_order` on a class of types, such that it will be decidable on some of the types but not others, so you don't just want to use classical to define the instance. For reals it's okay to use classical decidability, since you're never going to have proper decidability.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886086):
There is more to it because of the typeclass system. Take for instance `conditionally_complete_linear_order`, which extends `linear_order`. In a theorem, you can not really state the assumption that your order is decidable: if you write `[conditionally_complete_linear_order α] [decidable_linear_order α]`, then the two statements are talking about different orders, so they don't talk to each other. What you would need is a mixin to add decidability, but it is not really there. And if you add `classical.decidable_prop` in the header or as a local instance (which I always do), the type class system is not able to use it to convert linear orders to decidable ones automagically. 

What I can do for instance is change `conditionally_complete_linear_order` to extend `decidable_linear_order` instead of `linear_order`. Indeed, I have done it in my library, it solves all my typeclasses problems, and the library compiles fine. I wonder if the big guys would accept a PR like that, or if there is a reason to avoid this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886650):
Oh I see -- there really is an issue here. Yeah, typeclasses are not great for mathematics sometimes, this is why we have `distrib`s and stuff. But why can't you just add the assumption that your order is decidable? Can't you just make it an extra hypothesis and then feed it to the type class system?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886705):
No because 
```quote
if you write `[conditionally_complete_linear_order α] [decidable_linear_order α]`, then the two statements are talking about different orders, so they don't talk to each other.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886779):
The proper solution is certainly to define yet another class `conditionally_complete_decidable_linear_order`, defined just like `conditionally_complete_linear_order` but replacing `linear_order` with `decidable_linear_order`, and prove an instance going from it to `conditionally_complete_linear_order`. But this is getting super-heavy...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886822):
I mean why can't you just literally put `forall a b, decidable (a <= b)` in?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886823):
just use old structure cmd and you'll be done in one line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886829):
Because `max` is defined on `decidable_linear_order` not `decidable_rel has_le.le`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886830):
As are a bunch of lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886835):
If one could remove `linear_order`and cut the complexity in half, I certainly wouldn't mind :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886837):
And you can't make the correct instance of `decidable_linear_order` from the pieces you have?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886848):
```quote
And you can't make the correct instance of `decidable_linear_order` from the pieces you have?
```
 In each proof, yes you can. But not as a global instance, since there is already an arrow in the other direction and you want to avoid loops.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886898):
These issues do seem to come up sometimes. I get the feeling that the type class system is not quite right for maths sometimes. Chris had problems with diamonds coming from very innocuous issues as well, where he had two instances of a singleton (but not a Prop) which were not defeq and this really hurt him.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886950):
The issue you raise really not mathematical. It's just showing that Lean cannot cope with a situation which comes up very naturally in mathematics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887001):
There was the whole metric space  / topological space farce too -- the topological space underlying the product of two metric spaces was canonically isomorphic to but not defeq to the product of the underlying topological spaces, and because the type class system was involved Johannes had to jump through all sorts of hoops. This was presented to Patrick and me as some sort of clever trick but all the time I could see that something was wrong in the underlying system. It seemed to be the case that type class inference works great if all functors are forgetful, but the moment you want to do something where you're not in this situation you are in trouble.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887014):
```quote
The issue you raise really not mathematical. It's just showing that Lean cannot cope with a situation which comes up very naturally in mathematics.
```
 Let me disagree with this: in mathematics, everything is decidable, so there is just one class and the issue disappears.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887018):
right -- but you are just talking about your specific problem. I'm saying that you are a mathematician running into problems with the type class inference system, and you are by no means alone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 17 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887061):
Yes, I can see I'm not alone!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887062):
I agree that the other issues are in some sense more non-mathematical than yours :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887068):
but also in Chris' issue there was just one instance, and the issue didn't disappear, because he had two copies of it and they weren't defeq even though they were trivially equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887082):
All of us want, in some sense, to be able to insert proofs into the system. "Yes I know you now have two instances of [blah], but here's a proof that they're the same, now stop moaning"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887124):
You really want to put [decidable_linear_order] into your system and also a hypothesis that the underlying linear orders are the same one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887126):
But that can't be done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887134):
Who knows if this will be solved in Lean 4 Kenny. I thought Sebastian said that they weren't going to change the type class system.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887135):
No doubt Mario will wake up at some point and come up with another workaround

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 17 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887137):
but is workarounds what we really want?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 17 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887551):
I get the sense that `decidable_linear_order` should have been a mix-in, but we can't just change it because it's in core.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895225):
I am okay with `conditionally_complete_linear_order` extending `decidable_linear_order`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895226):
your instance is called `classical.DLO` by the way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895284):
To quote myself from somewhere, we want to assume decidability when decidability is decidable. So when it's either definitely the case (like `rat`) or definitely not the case (like `real`). As chris points out there are times when you are doing a construction over generic types, and there decidability can sometimes cause problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 18 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895287):
> when decidability is decidable

@.@"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895330):
But yes, this is in part because the typeclass exists, in core, and we have to deal with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 18 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895338):
just use `classical.decidable_decidable`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895341):
For `conditionally_complete_linear_order`, this is already hopelessly non-computable (you can't define anything with the type of `Sup`) so decidability is fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 18 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895437):
Aren't integers a conditionally complete linear order?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895442):
there is no computable instance of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895449):
because you can't compute a Sup

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895485):
even on `bool` it's not computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 18 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895882):
This is a somewhat-related question I had from back when I was messing with partitions. How much extra stuff would we have to write if we wanted to have a computable Sup over finsets rather than arbitrary sets?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 18 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895924):
zero, because it's there already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 18 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895978):
Oh, you're right! I stared at `finset.sup` before but I didn't understand what I was looking at until now.

