---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04805notationquestion.html
---

## Stream: [general](index.html)
### Topic: [notation question](04805notationquestion.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173744):
The following might be impossible in Lean but I thought I'd ask. It's just an issue with notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173745):
```lean
variables {S : Type} (R : S → S → Prop)
local infix `♥` : 50 := R

definition euclidean₁ := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z 
definition euclidean₂ (R : S → S → Prop) := ∀ {{x y z : S}}, R x y → R x z → R y z 
definition euclidean₃ (R : S → S → Prop) := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173746):
(`\heartsuit` gives the heart, by the way)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173754):
So mathematicians would normally _define_ a new relation with the infix notation, in contrast to functional programmers who want to define `R` first and then set up infix notation for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173755):
This has the following annoying-for-mathematicians consequence.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173794):
Definition 1 above is not so great because you can't see what you are defining -- it should say "euclidean1 heartsuit" or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173795):
Definition 2 is correct, but doesn't use the notation, so mathematicians are left wondering why we have `R x y` instead of `x R y` or `x heartsuit y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173796):
(infix notation is more normal in mathematics than CS perhaps)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173804):
And definition 3 is wrong because the heart in the definition is unrelated to the R -- the heart is attached to the variable R and definition 3 introduces a new one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173805):
My dream is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173806):
`definition euclidean_dream (R) := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173843):
but of course that doesn't even typecheck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173847):
Is there any way I can make my dream definition typecheck?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173848):
Actually I guess my dream is the impossible:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173849):
`definition euclidean_dream ♥ := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173896):
I don't mind a few incomprehensible lines with set-up beforehand, my question I guess is simply whether I can introduce a local variable in a definition and instantly have access to notation for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 06 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126174227):
@**Kevin Buzzard** Something like this proposal? https://github.com/leanprover/lean/issues/1522#issuecomment-294872715

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126174466):
Yes! I didn't mention it in my posts above but I did try to do this with the type class notation types (indeed I wrote `has_heart` :-) ) but I couldn't get that to work either because `definition blah (S : Type) (R : S -> S -> Prop) [has_heart S]` wouldn't attach the heart to R and I couldn't figure out how to make the attachment whilst keeping it all looking clean and uncluttered. I am currently thinking a lot about trying to write code which looks really clean to mathematicians, who we can think of here as people who know exactly what a transitive binary relation is but have no idea what a typeclass is and don't want to see clutter when they are actually doing or reading mathematics in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 06 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126176900):
In Haskell you can convert an infix operator to an ordinary (prefix) function by surrounding the operator in parentheses. You can also use this notation at a binding site.
The hypothetical Lean equivalent would be
```lean
definition euclidean {S : Type} ((♥) : S → S → Prop) := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 06 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126178574):
Lean would need to be told the associativity and left binding power, or at least default options for such things.


{% endraw %}
