---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01495Defininginverseasapartialfunction.html
---

## Stream: [general](index.html)
### Topic: [Defining inverse as a partial function.](01495Defininginverseasapartialfunction.html)

---

#### [Edward Ayers (Nov 01 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914681):
I am investigating defining field inverses so that you have to also give the inverse a certificate that the number being put in is not zero. We can have a separate debate about whether that approach is better than having `inv(0) = 0`, but for now here are my ideas:

My first idea was to treat the 'non-zeroness' as a typeclass then piggyback on the type inference algorithm.
```lean
    universe u
    class not_zero {R : Type u} [ring R] (x : R) := (nz : x ≠ 0)
    class my_division_ring (R : Type u) extends (ring R) :=
    (inv(x:R) [not_zero x]:  R)
    (inv_l : Π (y : R) [not_zero y], y * (inv y)  = 1 )
    (inv_r : Π (y : R) [not_zero y], (inv y) * y  = 1 )
```
Sadly, I get a "failed to synthesize typeclass" error.
Even more sadly, the last two lines of the error read:
```lean
_inst_1 : not_zero y
⊢ not_zero y
```
Why is the elaborator not spotting this? This seems like something the elaborator would be able to do. Supposing that the elaborator could do this, then my idea was that you could write things like:
```lean
instance {R : Type u} [integral_domain R] {x y : R} [not_zero x] [not_zero y] : not_zero (x * y) := ...
```
Are there any roadblocks that are stopping this dream from being a feasible way of defining the inverse function?

#### [Johan Commelin (Nov 01 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914772):
Can this be solved with the `haveI` magic inserting the instance into the type class system at the right points?

#### [Edward Ayers (Nov 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914794):
My second approach was to use auto_params:
```lean
    -- eventually a sophisticated tactic that figures out if an elt is ≠ 0
    meta def nz_tactic := tactic.assumption 
    class dvr (R : Type u) extends (ring R) :=
    (inv(x:R) (p:x ≠ 0):  R)
    (inv_l : Π (x y : R) (p:y≠0), x * (inv y p)  = 1 )
    variables {R : Type u} [dvr R]
    def inv (y : R) (nz : y ≠ 0 . nz_tactic) : R := dvr.inv y nz

    def div (x y : R) (nz : y ≠ 0 . nz_tactic) : R := x * (inv y)
    infix ` /. `:50 := div

    variables {x y : R} 
    variable (xz : x ≠ 0 . nz_tactic) -- I was really hoping that this would be allowed

    example (x y : R) (xz : x ≠ 0) (yz : y ≠ 0) : (1 /. (x * y)) = (1 /. x) * (1 /. y) := sorry
```

#### [Edward Ayers (Nov 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914838):
```quote
Can this be solved with the `haveI` magic inserting the instance into the type class system at the right points?
```
I don't understand what this means.

#### [Johan Commelin (Nov 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914840):
Neither do I.

#### [Johan Commelin (Nov 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914853):
The point is that the problem you described pops up quite often.

#### [Johan Commelin (Nov 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914861):
And then you can write `haveI my_instance, blah` and then the type class system will pick up your instance.

#### [Johan Commelin (Nov 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914867):
And the reason you have to do this explicitly is because Lean 3.4.x is pretty frozen.

#### [Edward Ayers (Nov 01 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914932):
Please could you give a full example of `haveI`?

#### [Edward Ayers (Nov 01 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914948):
I get `[Lean] unknown identifier 'haveI'` errors

#### [Johan Commelin (Nov 01 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914955):
I'll try. For starters, here are 56 examples: https://github.com/leanprover/mathlib/search?q=haveI&unscoped_q=haveI

#### [Edward Ayers (Nov 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915006):
ah it's a tactic

#### [Johan Commelin (Nov 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915020):
Yes, and it has some friends, like `exactI` and I don't know what they do, and how they differ.

#### [Johan Commelin (Nov 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915021):
I'm using them cargo-cult style.

#### [Edward Ayers (Nov 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915095):
So my question now is: Is there a fundamental reason why the elaborator can't do my above example? Eg there might be cases where it causes the elaborator to take unbounded time or something.

#### [Johan Commelin (Nov 01 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915157):
I think the fundamental reason was that Lean 3.4.x is frozen.

#### [Johan Commelin (Nov 01 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915207):
Also, in your `inv_l` and `inv_r` you want `y = x`.

#### [Edward Ayers (Nov 01 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915310):
That's not what I mean by reason. Why would the elaborator be able to do the below example but not the one at the top.
```lean
def sq {R : Type u} [ring R] (a : R) :=  a * a
```
It must be something to do with the fact that the elaborator is looking for typeclasses attached to the type of `a` and not to `a` itself.

#### [Edward Ayers (Nov 01 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915315):
```quote
Also, in your `inv_l` and `inv_r` you want `y = x`.
```
fixed!

#### [Chris Hughes (Nov 01 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915660):
I think it;s actually to do with being left or right of the colon. This doesn't work
```lean
example {R : Type*} : Π [ring R] (a : R), a * a = 1 :=
```

#### [Edward Ayers (Nov 01 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916579):
`    (inv_l (x : R) [not_zero x] : (x * (inv x)  = 1) )` has the same error though.

#### [Chris Hughes (Nov 01 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916787):
Maybe because it's part of a structure. Does the `ring` example work as part of a structure?

#### [Edward Ayers (Nov 01 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916872):
This works:
```lean
    variables {R : Type u} [my_division_ring R]
    def inv (y : R) [not_zero y] : R := my_division_ring.inv y
```

#### [Edward Ayers (Nov 01 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916882):
so maybe it is because it is part of a structure.

#### [Reid Barton (Nov 01 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136919570):
`by exactI` is the most succinct option here

#### [Edward Ayers (Nov 01 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136921820):
Right but ideally I wouldn't even have to use a tactic.

#### [Edward Ayers (Nov 01 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136921827):
The elaborator would just do it.

#### [Edward Ayers (Nov 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923468):
I think that I've got the elaborator to "just do it" now:
```lean
    class not_zero {R : Type u} [ring R] (x : R) := (nz:x ≠ 0)
    class my_division_ring (R : Type u) extends (integral_domain R) :=
    (inv : Π(x:R) [not_zero x],  R)
    (inv_l (x : R) [nz:not_zero x] : x * (@inv x nz)  = 1 )
    (inv_r : Π (x : R) [nz:not_zero x] , (@inv x nz) * x  = 1 )

    variables {R : Type u} [my_division_ring R]
    def inv (y : R) [not_zero y] : R := my_division_ring.inv y

    def div (x y : R) [not_zero y] : R := x * (inv y)
    infix ` ÷ `:50 := div

    variables {x y : R} [not_zero x] [not_zero y]
    instance : not_zero (x * y) := ⟨mul_ne_zero (not_zero.nz x) (not_zero.nz y)⟩

    example : (1 ÷ (x * y)) = (1 ÷ x) * (1 ÷ y) := sorry
```

#### [Edward Ayers (Nov 01 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923562):
So I was badmouthing the elaborator but I only have to be explicit with `inv` within the class definition.

#### [Edward Ayers (Nov 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923605):
I much prefer this approach to making the inverse total.

#### [Edward Ayers (Nov 01 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923739):
But it has its own caveats

#### [Floris van Doorn (Nov 01 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136924201):
One problem you'll run into is that sooner or later type class inference is not going to figure out that arguments are `not_zero`, because the reasons get too complicated. But if you're fine with writing
```
haveI : not_zero t := ...,
```
here and there, it should be fine.

#### [Edward Ayers (Nov 01 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136925306):
Right. The problem is that the reasons get too complicated, so the elaborator would end up needing to be a general purpose prover. It seems to me that in practice, if a function needs an implicit guard proposition like `x != 0`, it is usually easy for a human to work out where the certificate is coming from, so it should be possible to make a tactic that can also figure it out 80% of the time. It would be so useful if one were able to augment the elaborator with ones own tactics, similar to the `(x:P . my_tactic)` syntax, but where I don't have to explicitly write out the tactic name all of the time and one can also write `variables {x : R} (x != 0 . my_tactic)`. 
 I think my ideal syntax would be to extend the typeclass brackets to also take arbitrary propositions.
```lean
    class my_division_ring (R : Type u) extends (integral_domain R) :=
    (inv : Π(x:R) [x ≠ 0],  R)

    variables {x y : R} [x ≠ 0] [y ≠ 0]
    instance : (x * y) ≠ 0 := mul_ne_zero ‹x ≠ 0› ‹y ≠ 0›

```
I know that there are lots of practical difficulties that this would surface, but I think the idea makes sense. The meaning of `[x ≠ 0]` is that this is a fact that needs to be present but which should be hidden from the user as much as possible.

#### [Edward Ayers (Nov 01 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136925627):
You can already pretend that a proposition is a typeclass, but the elaborator doesn't know what to do with them because they don't have the `class` attribute on them.

#### [Simon Hudon (Nov 03 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137113111):
I think you might consider auto params. It allows you to specify a tactic to use to prove non-zeroness

#### [Simon Hudon (Nov 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137113225):
`ˋ`lean
(inv (x : R) (h : x /= 0 . prove_non_zero) : R)
`ˋ`

#### [Simon Hudon (Nov 03 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137113286):
(Sorry for the bad formatting, I’m on my phone)

#### [Reid Barton (Nov 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137116158):
Now I'm confused why this code that I found in Scott's limits branch actually does work:
```lean
class preserves_limits (F : C ⥤ D) :=
(preserves : Π {J : Type v} [small_category J] {K : J ⥤ C} {c : cone K}, is_limit c → is_limit (F.map_cone c))
```

#### [Reid Barton (Nov 03 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137116198):
`J \func C` depends on the `[small_category J]`, and if I delete the latter then I get errors.

