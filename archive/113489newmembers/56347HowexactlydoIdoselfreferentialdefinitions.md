---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56347HowexactlydoIdoselfreferentialdefinitions.html
---

## Stream: [new members](index.html)
### Topic: [How exactly do I do self-referential definitions?](56347HowexactlydoIdoselfreferentialdefinitions.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792425):
I'm trying to define a relation R such that `for all x, x R (x + 1)` and `transitive R`. Now I know I could probably do this inductively, but I don't want to (because I want the method to apply even if I had, e.g. `symmetric R`). My instinct was to use a non-constructive definition, like this (I know this is nonsense,  but it's just a sketch of what I want to do):

```lean
local attribute [instance] classical.prop_decidable
noncomputable def double_cosets (x y : ℤ): ℤ → ℤ → Prop :=
    if y = x + 1 then true
    transitivity double_cosets
```

But that doesn't work because 

 1. `true` becomes the value of a relation, when I really want that to be the *proposition it maps to*.
 2.  Lean doesn't understand the self-reference.

How do I define it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792448):
`trans_gen`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792451):
Take the transitive closure of your original relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792454):
isn't this just `<`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792499):
```lean
import logic.relation

inductive original : ℕ → ℕ → Prop
| r : ∀ n, original n (n+1)

def R := relation.trans_gen original
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792504):
@**Mario Carneiro** I think he wants to experiment instead of creating new things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792508):
alternatively:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792509):
```lean
inductive R : ℕ → ℕ → Prop
| basic : ∀ n, R n (n+1)
| trans : ∀ a b c, R a b → R b c → R a c
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792548):
Now you can prove things about `R` by induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792549):
It might be interesting to look at the definition of `<` on the natural numbers at this point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792556):
Huh, that makes sense. So induction can be used for *anything* self-referential?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792557):
not anything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792558):
and to tie this up with an earlier conversation, you could even look at the proof that `<` on `nat` is decidable, which is an algorithm which, given two nats, spits out which is the smallest.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792600):
and I would define a function N -> N -> bool instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792603):
to emphasize that it is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792614):
Whenever you want the "least relation satisfying some properties" that's an inductive predicate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792618):
and "smallest type closed under some operations" is an inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792619):
the relation doesn't have to be decidable, and the proof that it is usually goes by rather different methods than the original

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792668):
There are interesting examples of nondecidable predicates like "in the span of s" in a group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792682):
So what is the `noncomputable` kind of definition for? Isn't my definition non-constructive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792728):
`inductive` things are always computable, it's `definition` that is noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792729):
I think it's fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792733):
`Prop` is a strange thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792736):
you can have non-decidable propositions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792738):
that doesn't make it noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792740):
No, I get that -- my point is that the definition is non-constructive, isn't it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792757):
it isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792760):
you're just defining a proposition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792762):
it is not nonconstructive because you aren't actually constructing anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792764):
it's like you can write down what it means for a program to halt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792765):
you just can't evaluate that statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792837):
Yeah, you're right, I got confused.

