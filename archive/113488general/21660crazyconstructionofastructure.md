---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21660crazyconstructionofastructure.html
---

## Stream: [general](index.html)
### Topic: [crazy construction of a structure](21660crazyconstructionofastructure.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805454):
I never knew one could do this: https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/ring_theory/localization.lean#L80 (definition of ring structure on a localization).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805506):
Here are the two ways I knew of building instances of a structure:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805508):
```lean
structure foo :=
(bar : ℕ) (baz : Prop)

definition x : foo := {
  bar := 34,
  baz := 2 + 2 = 5 
}

definition y : foo := ⟨3,true⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805518):
The second one I always think of as "pointy brackets are a generic way of building something which needs two (say) "inputs", like a proof of `P and Q`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805558):
The first one I always just assumed was custom notation that only made sense for structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805567):
I don't really know what the link is doing, but I do know that `by {blah,blah,blah}` is pretty much the same as `(begin blah,blah,blah, end)`, which is surely a different usage of the squiggly brackets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 19 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805607):
`by` takes a tactic. The tactic is `refine ...`.
`refine` takes an expression with some holes. The expression is `{ ... }`. Here the `{`...`}` are building a structure, like you already know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 19 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805614):
This pattern has been discussed many times here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 19 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805616):
Put every definition in the refine and then proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 19 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805656):
The `..` at the end is important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 19 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805659):
Well, really the tactic is `refine ...; { ... }` and these other `{}`s are `solve_one begin ... end` or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126807008):
```quote
The `..` at the end is important
```
I don't see any `..` at the end in my link

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126807096):
That's because there are underscores around. If you do what I wrote (define operations, leave out proofs), you need `..`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126807101):
I think


{% endraw %}
