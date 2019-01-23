---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/41930sigmatypemismatch.html
---

## Stream: [general](index.html)
### Topic: [sigma type mismatch](41930sigmatypemismatch.html)

---

#### [Kevin Buzzard (Mar 26 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220067):
`stalk2` below doesn't typecheck:

#### [Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220112):
```
universe u
variables (X : Type u) (P : set (set X))

definition  stalk1 (x : X) :=
Σ U : {U : set X // x ∈ U ∧ P U}, ℕ

definition  stalk2 (x : X) :=
Σ (U : set X) (Hx : x ∈ U) (PU : P U), ℕ
```

#### [Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220122):
red squiggle is on the sigma in stalk2

#### [Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220123):
error is

#### [Kevin Buzzard (Mar 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220124):
```
type mismatch at application
  Σ (PU : P U), ℕ
term
  λ (PU : P U), ℕ
has type
  P U → Type : Type 1
but is expected to have type
  ?m_1 → Type : Type (max ? 1) 
```

#### [Kevin Buzzard (Mar 26 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220146):
I *think* that I would rather work with stalk2 rather than stalk1

#### [Kevin Buzzard (Mar 26 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220163):
because I tend to avoid subtypes if I can

#### [Kevin Buzzard (Mar 26 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220167):
I am still a bit scared of all the up-arrows

#### [Kevin Buzzard (Mar 26 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124220282):
[background : X is a topological space, P is a basis for the open sets, I'm defining the stalk of a presheaf https://stacks.math.columbia.edu/tag/009H just after 6.30.1; here's a special case https://stacks.math.columbia.edu/tag/0078 which in Lean currently looks like https://github.com/kbuzzard/lean-stacks-project/blob/16a88206397eaa664dd00cf917c78359b7119cb3/src/tag0078.lean#L9 ]

#### [Chris Hughes (Mar 26 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124221257):
Sigma only takes two arguments. Also the type of nat doesn't depend on the set, so you may as well use prod.

#### [Sebastian Ullrich (Mar 26 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124221456):
@**Chris Hughes** It's desugared to nested sigmas. But it still doesn't typecheck because `P U` does not live in `Type _`. I would suggest using structures in favor of nested anything.

#### [Kevin Buzzard (Mar 26 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222122):
@**Chris Hughes**  -- the actual type I want to make is  more complex -- the nat was just a MWE of my problem. @**Sebastian Ullrich** I need to make a type because I am actually interested in a quotient of the type I'm trying to construct. Your observation is that this doesn't typecheck either:

#### [Kevin Buzzard (Mar 26 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222127):
` definition  stalk2 (x : X) (U : set X) (Hx : x ∈ U) := Σ (PU : P U), ℕ`

#### [Kevin Buzzard (Mar 26 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222139):
and I don't really understand why.

#### [Kevin Buzzard (Mar 26 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222146):
But at the end of the day

#### [Kevin Buzzard (Mar 26 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222187):
I would like some sigma type so I can put an equivalence relation on it and form the quotient type.

#### [Kevin Buzzard (Mar 26 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222207):
Are you suggesting I stick with the `stalk1` approach?

#### [Kevin Buzzard (Mar 26 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222271):
Presumably you prefer `A -> B -> C` to `A and B -> C`, i.e. here we avoid the structure [not subtype -- sorry] and prefer the "nested" approach?

#### [Sebastian Ullrich (Mar 26 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124222300):
No, I'm suggesting
```
structure stalk3 (x : X) :=
(U : set X) (Hx : x ∈ U) (PU : P U) (n : ℕ)
```
so that you don't have to worry about every component whether it should be a sigma or a prod or a pprod or ... and on top of that you get projections with meaningful names.

#### [Kevin Buzzard (Mar 26 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124223706):
Oh, I see: and then this is still a type so I can still put an equivalence relation on it. I will try it this way! Thanks!

#### [Kenny Lau (Mar 26 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124230980):
@**Kevin Buzzard** have you tried it? (if not, i’ll do it)

#### [Kevin Buzzard (Mar 26 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231051):
No, I've been at meetings until recently and since then I've been talking to Chris about rings

#### [Kenny Lau (Mar 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231262):
I’ll do it when i get back home then

#### [Kenny Lau (Mar 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231264):
which will happen in 15 minutes

#### [Kevin Buzzard (Mar 26 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%20type%20mismatch/near/124231348):
I pushed as far as I got. Thanks.

