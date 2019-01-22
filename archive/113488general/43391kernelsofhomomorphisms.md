---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43391kernelsofhomomorphisms.html
---

## [general](index.html)
### [kernels of homomorphisms](43391kernelsofhomomorphisms.html)

#### [Johan Commelin (Apr 23 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125580755):
Ok, I'm making my feet wet with a first attempt at formalising something. I want to say write down the assumption im(f) = ker(g), where f and g are group homomorphisms. I guess im(f) will be something like `f ' A.univ`. I tried to find kernels in `algebra.group` but did not find anything. Are kernels somewhere else?

#### [Andrew Ashworth (Apr 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582195):
https://github.com/leanprover/mathlib/search?utf8=✓&q=ker&type=

#### [Andrew Ashworth (Apr 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582201):
it's a little sparse

#### [Johan Commelin (Apr 23 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582221):
Aah, ok. So I should use the github search for this. Thanks

#### [Johan Commelin (Apr 23 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582732):
What am I doing wrong here?
```lean
universes u
variables
{A : Type u} [group A]
{B : Type u} [group B]
{f : A → B} [is_group_hom f]

definition ker f := is_group_hom.ker f
definition im f := f '' (@univ A)
```

#### [Johan Commelin (Apr 23 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582735):
Lean does not like my definition of `ker` and`im`

#### [Johan Commelin (Apr 23 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582746):
I get squiggles under the `f`

#### [Johan Commelin (Apr 23 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582759):
{% raw %}
`invalid binder declaration, delimiter/bracket expected (i.e., '(', '{', '[', '{{')`{% endraw %}

#### [Reid Barton (Apr 23 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125584258):
You can write
```lean
variables (f)
definition ker := is_group_hom.ker f
definition im := f '' (@univ A)
```
though I'm not sure whether it is very good style

#### [Patrick Massot (Apr 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125586882):
Could use `def im := set.range f`

#### [Kevin Buzzard (Apr 23 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589015):
`definition ker f := ...` is no good because everything to the left of the `:=` has to either be a variable and skipped completely, or a term together with its type. Just `f` by itself doesn't work.

#### [Kevin Buzzard (Apr 23 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589020):
As Reid Barton says, you can skip the `f` completely

#### [Kevin Buzzard (Apr 23 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589029):
but you might want to write
```lean
import group_theory.subgroup
universes u
variables {A : Type u} [group A] {B : Type u} [group B]

definition ker (f : A → B) [is_group_hom f] := is_group_hom.ker f
```

#### [Patrick Massot (Apr 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589134):
Why do you want to enforce the same universe?

#### [Kevin Buzzard (Apr 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589905):
Patrick, although your comment is of course sensible, and probably Johan should write `universes u v` and then `{B : Type v}`, in ZFC we only have universe and it never bothered us before :-)

#### [Patrick Massot (Apr 23 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589922):
If you don't care (like I don't care) then use `Type*` until it bites you

#### [Mario Carneiro (Apr 24 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125592932):
The lean syntax requires parentheses around arguments left of `:=`, so `def ker (f) := ...` would work. But it would be a different `f` than the one in the variable statement, so its type could be different (it will be inferred) and in particular it will not be assumed to be a group_hom

#### [Mario Carneiro (Apr 24 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125593086):
By the way, the parentheses used to be optional, until we discovered that it enables the following evil example:
```
example inconsistent : false := trivial
```
(hint: it's not proving false)

