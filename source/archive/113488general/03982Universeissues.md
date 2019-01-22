---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03982Universeissues.html
---

## [general](index.html)
### [Universe issues](03982Universeissues.html)

#### [Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734232):
I seem to not understand universes properly, or more precisely how to use them properly. I ran into the following issue with some code:

#### [Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734247):
```lean
definition foo (X : Type*) := ∀ (β : Type*), true 

theorem baz (X : Type*) (bar: foo X) (β : Type*) : true := 
begin
  have H := bar β, -- error
  admit,
end
```

#### [Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734249):
The error was

#### [Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734254):
```
type mismatch at application
  bar β
term
  β
has type
  Type u_3 : Type (u_3+1)
but is expected to have type
  Type u_2 : Type (u_2+1)
state:
X : Type u_1,
bar : foo X,
β : Type u_3
⊢ true
```

#### [Kevin Buzzard (Apr 06 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734270):
I figured I'd investigate more, so I next wrote this:

#### [Kevin Buzzard (Apr 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734321):
```lean
universes u v w x
set_option pp.universes true 
definition foo' (X : Type u) := ∀ (β : Type v), true 
theorem baz' (X : Type w) (bar' : foo' X) (β : Type x) : true := 
begin
  have H := bar' β, -- error
  admit,
end
```

#### [Kevin Buzzard (Apr 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734337):
and this time I got

#### [Kevin Buzzard (Apr 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734344):
```
type mismatch at application
  bar' β
term
  β
has type
  Type x : Type (x+1)
but is expected to have type
  Type u_1 : Type (u_1+1)
state:
X : Type w,
bar' : foo'.{w u_1} X,
β : Type x
⊢ true
```

#### [Kevin Buzzard (Apr 06 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734362):
This made me realise that I didn't understand what was going on, because there is still this universe `u_1` mentioned, even though I thought I'd just explicitly written down what universe everything was in.

#### [Kevin Buzzard (Apr 06 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734377):
In particular, `bar'` seems to mention this universe `u_1` and I'm not sure where this universe got involved.

#### [Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734425):
Some experimentation led me to something which worked:

#### [Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734429):
```lean
definition foo'' (X : Type u) := ∀ (β : Type u), true 

theorem baz'' (X : Type v) (bar'' : foo'' X) (β : Type v) : true := 
begin
  have H := bar'' β, -- works
  exact H
end
```

#### [Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734435):
i.e. "keep X and beta in the same universe and you'll be fine"

#### [Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734441):
But this raises two questions for me:

#### [Kevin Buzzard (Apr 06 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734444):
1) why wasn't I fine before?

#### [Kevin Buzzard (Apr 06 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734450):
2) Will this fix cause me problems later?

#### [Kevin Buzzard (Apr 06 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734513):
In reality, X is a topological space and it is covered by open sets `U i` where each `i` has type `beta`

#### [Kevin Buzzard (Apr 06 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734523):
that is, `U : beta -> set X`

#### [Kevin Buzzard (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734570):
My instinct is always to just let everything live in different universes because who cares about universes anyway, that's the joy of type theory

#### [Kevin Buzzard (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734615):
In ZFC I would just let X and beta be in Type

#### [Kevin Buzzard (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734623):
but that might be a bridge too far

#### [Mario Carneiro (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734636):
When you defined `foo`, it had two universe parameters, corresponding to the two `Type*` instances

#### [Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734672):
what does that even mean

#### [Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734676):
foo is a thing

#### [Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734677):
and it has a type

#### [Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734681):
which lives in a universe

#### [Mario Carneiro (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734686):
it is universe polymorphic

#### [Mario Carneiro (Apr 06 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734733):
Think of it as being implicitly a forall over the universe variables

#### [Mario Carneiro (Apr 06 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734745):
except that lean has no universe variable binders, so it's all just free variables and substitution

#### [Kevin Buzzard (Apr 06 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734749):
`foo'` mentions a universe I don't even see

#### [Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734760):
or at least something mentions this universe

#### [Mario Carneiro (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734763):
`foo` and `foo'` are the same

#### [Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734774):
wait

#### [Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734777):
are they exactly the same?

#### [Mario Carneiro (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734780):
except `foo'` is more explicit about the two universe variables, `u` and `v`

#### [Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734790):
Should I think that `foo'` is really "for all universes u, ..."

#### [Mario Carneiro (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734791):
yes, they are exactly the same as far as lean is concerned

#### [Mario Carneiro (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734842):
yes. All universe polymorphic functions are like this

#### [Kevin Buzzard (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734852):
like when I make variables and then secretly I am writing "for all v..."

#### [Mario Carneiro (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734853):
exactly

#### [Kevin Buzzard (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734858):
But where is this `u_1` coming from?

#### [Kevin Buzzard (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734860):
Didn't I name all my universes with `foo'`?

#### [Mario Carneiro (Apr 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734877):
`foo'` has two universe variables, named `u` and `v` in the definition, but since it's like a forall, whenever you use it these variables can be substituted for other things

#### [Kevin Buzzard (Apr 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734880):
gotcha

#### [Kevin Buzzard (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734925):
So `foo'` is `for all universes u and v, [what I wrote]`

#### [Kevin Buzzard (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734930):
so why do I get a problem?

#### [Kevin Buzzard (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734932):
why can't we just do universe unification or something?

#### [Mario Carneiro (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734940):
`u_1` is the name of a universe variable in `baz'`, since you reference `foo' X` which only fixes its first parameter by unification, lean invents a second variable `u_1` so it becomes `bar' : foo'.{w u_1} X`

#### [Kevin Buzzard (Apr 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734953):
aah

#### [Kevin Buzzard (Apr 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734955):
yes I just independently realised this

#### [Kevin Buzzard (Apr 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734965):
But now `bar'` should be "for all universes u_1, ..."

#### [Mario Carneiro (Apr 06 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735011):
it is

#### [Mario Carneiro (Apr 06 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735027):
`bar'.{w x u_1}` has type `forall (X : Type w) (bar' : foo'.{w u_1} X) (β : Type x), true`

#### [Mario Carneiro (Apr 06 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735048):
And since `u_1` and `x` are separate universe variables being generalized, inside the proof you can't assume they are equal

#### [Mario Carneiro (Apr 06 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735061):
so `bar' β` is a type error since `bar'` accepts a `Type u_1`

#### [Kevin Buzzard (Apr 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735108):
OK so you have convinced me that the underlying way that universes work mean that my initial attempts should not work.

#### [Kevin Buzzard (Apr 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735113):
So now the question is should I try to re-arrange things to make them work?

#### [Mario Carneiro (Apr 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735122):
just write `foo'.{w x}` instead of `foo'` in the type of `bar'`

#### [Kevin Buzzard (Apr 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735127):
Or should I go down the "might bite me later and I have no understanding as to whether it will" route of letting all universes be u

#### [Kevin Buzzard (Apr 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735130):
aah, oh great, so I can do what I want to do.

#### [Mario Carneiro (Apr 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735186):
In general, I try to avoid types with "internal universe variables" like `foo'` here, which has a forall whose universe is not constrained by the input parameters

#### [Kevin Buzzard (Apr 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735198):
```lean
definition  foo' (X : Type u) :=  ∀ (β : Type v), true

theorem  baz' (X : Type w) (β : Type x) (bar' : foo'.{w x} X) : true :=
begin
have H := bar' β, -- works :-)
exact H,
end
```

#### [Kevin Buzzard (Apr 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735206):
I need to think about the last thing you said

#### [Mario Carneiro (Apr 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735215):
that means to prefer `def foo' (X : Type u) := ∀ (β : Type u), true` over `def foo' (X : Type u) := ∀ (β : Type v), true`

#### [Kevin Buzzard (Apr 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735219):
because this is a massively minimised thing and in reality I will have to decide whether I can try to avoid the thing you want me to avoid

#### [Kevin Buzzard (Apr 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735225):
Thanks a lot for the fix and the advice though.

#### [Kevin Buzzard (Apr 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735281):
How do I know whether the thing you prefer will be safe for me?

#### [Kevin Buzzard (Apr 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735290):
hmm, I need to go and feed children

#### [Kevin Buzzard (Apr 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735295):
thanks

#### [Mario Carneiro (Apr 06 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735417):
It is slightly less universe parametric (it requires that two variables be the same), so you may need extra `ulift`s around, which may or may not be better than the often required `.{w x}` stuff that arises with this approach

#### [Mario Carneiro (Apr 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735479):
Generally you will have to be "universe conscious" when working with definitions with internal universe variables - lots of things will require annotation. `cardinal`, `ordinal`, and `Set` (the ZFC sets) are like this

#### [Mario Carneiro (Apr 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735490):
`category` may also be, this exact thing was a point of discussion with Scott a few weeks ago

#### [Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942604):
What is happening here:

#### [Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942641):
```lean
universe u

structure scheme :=
(β : Type u)
      
theorem scheme_of_affine_scheme (R : Type u) : scheme :=
{ β := R -- universe issue
}

/-

type mismatch at field 'β'
  R
has type
  Type u : Type (u+1)
but is expected to have type
  Type u_1 : Type (u_1+1)

-/
```

#### [Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942655):
Seems to me that scheme has decided that it wants to live in a different universe to beta and R

#### [Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942656):
oh

#### [Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942657):
heh

#### [Kevin Buzzard (May 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942661):
ignore the irrelevant names

#### [Kevin Buzzard (May 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942676):
If I change theorem to definition, it works

#### [Kevin Buzzard (May 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942682):
And this works too:

#### [Kevin Buzzard (May 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942700):
```lean
theorem scheme_of_affine_scheme (R : Type u) : scheme.{u} :=
{ β := R -- works
}

```

#### [Kevin Buzzard (May 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942731):
OK so maybe the answer is simply "don't use theorem to define something which isn't a Prop"

#### [Kevin Buzzard (May 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942856):
```lean
definition scheme_of_affine_scheme (R : Type u) : scheme :=
{ β := R -- works
}
```

#### [Kevin Buzzard (May 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942867):
I guess I don't understand what's going on, but on the other hand I can see I was doing something dumb.

#### [Chris Hughes (May 22 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943048):
This gives some small insight.
```lean
set_option pp.universes true
def scheme_of_affine_scheme (R : Type u) : scheme :=
begin
-- R : Type u
-- ⊢ scheme.{?l_1}
end

lemma scheme_of_affine_scheme (R : Type u) : scheme :=
begin
-- R : Type u
-- ⊢ scheme.{u_1}
end
```

#### [Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943257):
Aah so in the first case scheme is in some universe and Lean isn't too fussed, it will decide later

#### [Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943303):
but in the second case Lean decided to go for it and make a decision

#### [Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943307):
because it's a lemma so the universe is supposed to be Prop

#### [Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943312):
and it wasn't Prop so Lean panicked

#### [Chris Hughes (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/127406709):
The lemma `card_univ` below does not work without the `.{u}` in the `fintype` instance
```lean
import data.set.finite
open set fintype
universe u

def equiv_univ (α : Type u) : α ≃ (set.univ : set α) :=
{ to_fun := λ a, ⟨a, mem_univ _⟩,
  inv_fun := λ a, a.1,
  left_inv := λ a, rfl,
  right_inv := λ ⟨a, ha⟩, rfl }

@[simp] lemma card_univ {α : Type u} [fintype α] [fintype.{u} (set.univ : set α)]: 
  @fintype.card (set.univ : set α) _ = fintype.card α := 
eq.symm (@card_congr α (set.univ : set α) _ _ (equiv_univ α))
```
The following do not work.
```lean
set_option pp.universes true
@[simp] lemma card_univ {α : Type u} [fintype α] [fintype (set.univ : set α)]: 
  fintype.card (set.univ : set α) = fintype.card α := 
eq.symm (card_congr (equiv_univ α))
```
Gives the error
```
failed to synthesize type class instance for
α : Type u,
_inst_1 : fintype.{u} α,
_inst_2 : fintype.{?l_1} ↥univ.{u}
⊢ fintype.{u} ↥univ.{u}
```
and  
```lean
set_option pp.universes true
@[simp] lemma card_univ {α : Type u} [fintype α] [f : fintype (set.univ : set α)]: 
  @fintype.card (set.univ : set α) f = fintype.card α := 
eq.symm (@card_congr α (set.univ : set α) _ f (equiv_univ α))
```
Gives the error
```
type mismatch at application
  card_congr.{u u_1} (equiv_univ.{u} α)
term
  equiv_univ.{u} α
has type
  equiv.{u+1 (max 1 (u+1))} α
    (@coe_sort.{(max (u+1) 1) (max 1 (u+1))+1} (set.{u} α) (@set.has_coe_to_sort.{u} α) (@set.univ.{u} α)) : Type u
but is expected to have type
  equiv.{u+1 u_1+1} α
    (@coe_sort.{(max (u+1) 1) (max 1 (u+1))+1} (set.{u} α) (@set.has_coe_to_sort.{u} α)
       (@set.univ.{u} α)) : Type (max (max u u_1) u_1 u)
```
What's going on here? And will the `.{u}` in the fintype instance make the lemma more difficult to use. It worked in my application, but will it always work?

#### [Gabriel Ebner (Jun 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/127406993):
> And will the .{u} in the fintype instance make the lemma more difficult to use.

No, not at all.  It is the only possible choice, the elaborator just can't figure it out for whatever reason.

#### [Gabriel Ebner (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/127407052):
(The universe parameter `.{u}` is always there, whether you write it explicitly or not.)

