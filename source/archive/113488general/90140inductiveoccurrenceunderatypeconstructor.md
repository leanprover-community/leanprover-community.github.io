---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90140inductiveoccurrenceunderatypeconstructor.html
---

## [general](index.html)
### [inductive occurrence under a type constructor](90140inductiveoccurrenceunderatypeconstructor.html)

#### [Arseniy Alekseyev (Jul 18 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838639):
I've got a rose tree definition:

    inductive tree : Type
    | branch : list tree -> tree

The interesting/unusual part here is that the recursive occurrence of "tree" is inside a list, so this can only work if `list` is strictly positive, which makes elaboration perhaps tricky, but it does get accepted.
On this type I defined a function:

    open tree
    def f : tree → string
    | (branch _) := "hello"

which works

    #eval (f (branch []))
    -- ^ "hello"

but refuses to compute during typechecking:

    example : f (branch []) = "hello" :=
      eq.refl "hello"
    -- type mismatch, term
    --   eq.refl "hello"
    -- has type
    --   "hello" = "hello"
    -- but is expected to have type
    --   f (branch list.nil) = "hello"

I poked around the `_mut_` and found that the thing gets elaborates to something roughly like this:

    mutual inductive tree, lst
    with tree : Type
    | branch : lst -> tree
    with lst : Type
    | nil : lst
    | cons : tree → lst → lst

And if I do this encoding manually then the function suddenly computes fine.

Basically my question is: what's going wrong in the original example?

#### [Mario Carneiro (Jul 18 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838763):
> The interesting/unusual part here is that the recursive occurrence of "tree" is inside a list, so this can only work if list is strictly positive, which makes elaboration perhaps tricky, but it does get accepted.

Lean compiles nested inductive types like these to plain inductive types by unfolding the inductive definitions under the hood. This usually doesn't matter so much but you should be aware that this isn't the kernel being lenient, it is the equation compiler doing extra work

#### [Arseniy Alekseyev (Jul 18 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838764):
Having formulated the question now I can find a relevant wiki page too: https://github.com/leanprover/lean/wiki/Inductive-datatypes. I guess the answer is making it compute is hard.

#### [Mario Carneiro (Jul 18 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838837):
> but refuses to compute during typechecking:

The equation compiler defaults to well founded recursion for definitions on mutual and nested inductives. These have the side effect that the definition's equalities are not by rfl, so you have to use the provided equalities instead of definitional equality

#### [Arseniy Alekseyev (Jul 18 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838862):
do those have predictable names?

#### [Mario Carneiro (Jul 18 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838923):
they are called `f.equations.stuff` but `rw`, `simp` and `unfold` will use them by direct reference to the definition:
```lean
example : f (branch []) = "hello" := by unfold f
```

#### [Mario Carneiro (Jul 18 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838932):
`rw f` and `simp [f]` also work

#### [Arseniy Alekseyev (Jul 18 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838984):
oh!

#### [Mario Carneiro (Jul 18 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838985):
```
#print prefix f
```
```
f : tree → string
f._main : tree → string
f._main.equations._eqn_1 : ∀ (_x : list tree), f._main (branch _x) = "hello"
f._sunfold : tree → string
f.equations._eqn_1 : ∀ (_x : list tree), f (branch _x) = "hello"
```
the operative lemma is `f.equations._eqn_1`

#### [Arseniy Alekseyev (Jul 18 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839065):
Do #eval/#reduce also use these equations then? (they are both able to reduce this)

#### [Mario Carneiro (Jul 18 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839079):
`#reduce` does not, it unfolds everything by rfl but it also unfolds theorems and stuff as well which is what makes this work

#### [Arseniy Alekseyev (Jul 18 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839147):
Those f.equations are pretty cool, thank you!

#### [Mario Carneiro (Jul 18 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839192):
`#eval` does not use equations at all, it does unbounded recursion using the original match equations and ignores all the encoding stuff

#### [Mario Carneiro (Jul 18 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839226):
(Your example doesn't show too much of this since it is nonrecursive, but recursive definitions use a completely different meta implementation in `#eval`)

