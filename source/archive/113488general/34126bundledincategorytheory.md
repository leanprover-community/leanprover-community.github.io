---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34126bundledincategorytheory.html
---

## [general](index.html)
### [bundled in category_theory](34126bundledincategorytheory.html)

#### [Sean Leather (Oct 04 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135174961):
I just discovered `bundled` in `category_theory.category`:

```lean
structure bundled (c : Type u → Type v) :=
(α : Type u)
[str : c α]
```

This seems very useful. In particular, I'm thinking it can help me remove `[decidable_eq α]` that I have to state everywhere by allowing me to bundle the condition. So, I have a couple of questions:

1. I think it would be helpful to define this outside the `category_theory` directory because it's not inherently tied to category theory. Do people agree? Should it be in `data/bundled.lean` or somewhere else?
2. Do the `[`/`]` brackets do anything different from `(`/`)` here? `#print bundled` doesn't give any clue.
3. What does `str` abbreviate? I've typically seen `str` for string, but I don't think that makes sense here. Is it `structure`? If so, why? It seems more like a type function being bundled with its parameter, so I'm not clear where the `structure` comes in.

#### [Kevin Buzzard (Oct 04 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135175752):
I *believe* that the only difference the `[]` makes within the structure is that you can use type class inference within the structure itself. So I am going to stick my neck out and suggest that in this case, where we don't need str to be inferred in any of the other fields, the `[]` is no different to `()`. Apologies if I've written something misleading / wrong here. I think the way to make type class inference pick up on `str` is to have the obvious instance immediately after the definition of the structure.

#### [Scott Morrison (Oct 04 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135177519):
I think Johannes suggested the `[ ]` here, and I never thought too hard about it.

#### [Scott Morrison (Oct 04 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135177627):
`str` is indeed for `structure`. We earlier had `carrier` instead of `a`.

#### [Scott Morrison (Oct 04 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135177784):
Regarding `bundled`, I've found that it has limited use, because as soon as you're past the first round of examples, you want to bundle up multiple typeclasses, and you're back to writing a custom structure for each set of typeclasses you're interested in.

#### [Sean Leather (Oct 04 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135183550):
I can see how it is not suitable for more involved structures. This applies as well to `sigma`, `subtype`, etc. (And, even for cases that fit those, it often seems better to define your own structure.) That said, it is still a unique point in the design space and useful for many cases in which you don't need/want to define a structure.

#### [Sebastian Ullrich (Oct 04 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135197885):
The binder types (brackets) used in a structure declaration are reflected in the structure's constructor

#### [Kevin Buzzard (Oct 04 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135199650):
Aah so my post is inaccurate. Thanks Sebastian.

#### [Sean Leather (Oct 05 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135236416):
```quote
The binder types (brackets) used in a structure declaration are reflected in the structure's constructor
```
@**Sebastian Ullrich** Ah, of course. Thanks!

#### [Sean Leather (Oct 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135242468):
Here's the resulting [PR](https://github.com/leanprover/mathlib/pull/390).

#### [Johan Commelin (Oct 06 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303706):
I added a comment: https://github.com/leanprover/mathlib/pull/390#discussion_r223174490
```lean
@[reducible] def Meas : Type (u+1) := bundled measurable_space
instance (x : Meas) : measurable_space x := x.inst
```
The comment says:
Would it be possible to autogenerate these instances? Everytime we bundle a class we want an instance like this. This probably means that `bundled` has to become meta. I don't know. But I think it would take away one of those "minor annoyances" if all these instances would just be there, automagically.

#### [Mario Carneiro (Oct 06 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303758):
You can't hook in to inductive aux theorem generation, but you can have a derive handler

#### [Mario Carneiro (Oct 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303764):
You could add an attribute to `Meas` that does the instance generation

#### [Mario Carneiro (Oct 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303766):
but I don't think you will gain much over just writing that one line

#### [Mario Carneiro (Oct 06 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303809):
it's not like there are that many bundled classes. This is a negligible fraction of the work

