---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11809ofastrueproofs.html
---

## [general](index.html)
### [of_as_true proofs](11809ofastrueproofs.html)

#### [Joe Hendrix (Dec 28 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152632359):
I'm trying to build up a mental model of the efficiency of using decidable predicates to construct proofs in tactics..
Let's say I have a decidable predicate `P : nat -> Prop` with an instance `h : decidable_pred P`, and a concrete value `x : nat` in a tactic.  
I can match on `h x` within the tactic monad (which I think is using the VM), and see if the prop is true or false.
However, I'd also like to have an expression for the proof of `P x`.  I seem to be able to do that via an expression like `@of_as_true _ (h x) trivial`, but I think this results in the elaborator needing to reduce `h x` to whnf.  I think of this as slower than the VM, since among other things nat will have a unary representation. 
Is the above correct, and is so is there some way like reflection to have the VM (or the compiler in Lean 4) run `h x` and efficiently construct the needed proof?

#### [Mario Carneiro (Dec 28 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152634914):
No, you can't directly produce a "fast" kernel proof from a "fast" VM function. For many common operations on `nat`, `norm_num` will produce efficient kernel proofs using VM evaluation to guide the construction, but the method is generally completely different than what the decidable instance does

#### [Joe Hendrix (Dec 28 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638440):
Good to know I'm not missing something.  I think it would be useful to have some way to write a verified decision procedure in logic mode, and then be able to use it to discharge proof obligations in tactic mode.
For similar reasons, I started down the path of building up `has_reflect` instances for datatypes in proofs (e.g., `has_reflect (and P Q)`), but it's (1) a lot of work, and (2) still unclear how to support for some properties.  Specifically, I have `decidable (\forall (x : fin n), P x)`, but I'm struck on `has_reflect (\forall (x : fin n), P x)`.

#### [Mario Carneiro (Dec 28 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638542):
hm, that's an interesting use of `has_reflect`. Usually we don't use `has_reflect` for propositions, what's the goal here?

#### [Mario Carneiro (Dec 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638564):
I think what you want is actually `decidable`, or at least `semidecidable` (where `semidecidable p` is basically `option p`)

#### [Mario Carneiro (Dec 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638567):
but you are limited by the same things as `decidable` proofs

#### [Joe Hendrix (Dec 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638568):
The idea for that use was to get the VM to produce the proof object using the decidable instance, then call `has_reflect.reflect` to construct the appropriate expression.

#### [Mario Carneiro (Dec 28 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638610):
decidable instances don't have proof objects

#### [Mario Carneiro (Dec 28 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638613):
they put all the computation in the kernel

#### [Joe Hendrix (Dec 28 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638624):
I'm referring to the proof object `p` that is the argument to `decidable.is_true p`

#### [Mario Carneiro (Dec 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638671):
You could infer `decidable p`, normalize it to `is_true h` and return `h`, but this is going to be almost as slow as kernel computing it

#### [Mario Carneiro (Dec 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638673):
you are "elaborator computing" it in this case

#### [Joe Hendrix (Dec 28 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639243):
I think I haven't been clear.  I use the tactic `decidable_tac` below that uses uses the elaborator fairly often.  As a work around to get more use of the VM, I was hoping to be able to use both `decidable` and `has_reflect` instances to get something a bit more efficient in the `decidable_reflected` tactic below:

```
meta def decidable_tac : tactic unit := do
  tgt ← tactic.target,
  tactic.apply ((`(@of_as_true) : expr) tgt),
  tactic.exact `(trivial)

meta def decidable_reflected (P:Prop) [h:decidable P] [g:has_reflect P] : tactic unit := do
  match h with
  | decidable.is_true p := tactic.exact (g p)
  | decidable.is_false q := tactic.fail "Prop false"
  end
```

Unfortunately, I can't actually write the necessary `has_reflect` instances.  It seems like I would need some more support within Lean (perhaps constants that auto generated reflect instances for propositions).

#### [Mario Carneiro (Dec 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639535):
You can't write `has_reflect` instances for many propositions

#### [Mario Carneiro (Dec 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639536):
like `or`

#### [Mario Carneiro (Dec 28 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639635):
A `has_reflect` instance is a function that produces an expression that is a proof of `p`, provided `p` is in fact true

#### [Mario Carneiro (Dec 28 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639645):
So `decidable p` implies `has_reflect p` because you can evaluate the decidable instance and take the proof out

#### [Joe Hendrix (Dec 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639695):
Yep, I got `and` and `true`  and thought this would work, then got stuck with forall.  I tried `or` while writing up the example, and got the error about only being able to return a value of type `P`.

#### [Mario Carneiro (Dec 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639711):
If you know one or the other of the propositions is decidable, you can reflect an `or`

#### [Mario Carneiro (Dec 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639715):
but really decidable is the one you want, it's closed under all the operations

#### [Joe Hendrix (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639761):
Here was my attempt at `or`, but I can't match on the or value due to proof irrelevance:
```
meta instance or.reflect (P Q : Prop) [reflected P] [reflected Q] [hp:has_reflect P] [hq:reflected Q]
: has_reflect (P ∨ Q)
| (or.inl p) := `(or.inl).subst (hp p)
| (or.inr q) := `(or.inr).subst (hq q)
```

#### [Mario Carneiro (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639766):
exactly

#### [Mario Carneiro (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639768):
In a tactic, a proof value isn't very useful. It's only going to help avoid some code paths that weren't going to be exercised anyway

#### [Joe Hendrix (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639769):
Interesting `and` did not complain even though it looks like it recurses:
```
meta instance and.reflect (P Q : Prop) [reflected P] [reflected Q] [hp:has_reflect P] [hq:has_reflect Q]
: has_reflect (P ∧ Q)
| ⟨p,q⟩ := (`(and.intro).subst (hp p)).subst (hq q)
```

#### [Mario Carneiro (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639770):
`and` has large elimination because it only has one constructor

#### [Joe Hendrix (Dec 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639815):
The proof value is needed just so I can discharge theorems I'm proving.

#### [Mario Carneiro (Dec 28 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639823):
so if you have a function `p -> expr` coming from your has reflect instance, you could just as well have a function producing `option expr` with no proof preconditions

#### [Mario Carneiro (Dec 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639879):
So when you are writing a has_reflect instance you are just constructing a proof from nothing. Sometimes that's easy, like `and`, sometimes that requires backtracking like `or`, and sometimes it's really hard

#### [Mario Carneiro (Dec 28 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639936):
How are you supposed to use `decidable_reflected`?

#### [Mario Carneiro (Dec 28 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639938):
nothing says what `P` is

#### [Mario Carneiro (Dec 28 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639949):
it seems like it's mixing meta levels, and that's why you need `has_reflect`

#### [Mario Carneiro (Dec 28 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639952):
`decidable_tac` is the same as `exact_dec_trivial` afaict

#### [Joe Hendrix (Dec 28 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639997):
Let me work on an example.  Is `exact_dec_trivial` in Lean standard library or mathlib?

#### [Mario Carneiro (Dec 28 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640005):
It's in mathlib, but it's literally `exact dec_trivial` which is core only

#### [Joe Hendrix (Dec 28 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640062):
I forget why I didn't just use `exact dec_trivial` -- I may not have known about it, I've used that tactic for a while now.

#### [Mario Carneiro (Dec 28 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640118):
note that `dec_trivial` is notation for `of_as_true (by trivial)`; the tactic is there I think to stage the elaboration

#### [Mario Carneiro (Dec 28 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640234):
Okay, so I think I understand now what you are trying to do. You need a combination of `decidable` and `has_reflect` that produces exprs rather than proof values. You can automatically construct one by reflecting a decidable instance, but you can also produce much smarter proofs for nats and such

#### [Joe Hendrix (Dec 28 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640287):
That's right.  I want proof search to run within the VM (or compiler in Lean 4), then either I can reflect on the generated proof, or maybe just have some magic constant that pretends to do it for me (say a safe version of `sorry`).
(edit, apparently I can't spell)

#### [Mario Carneiro (Dec 28 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152641068):
@**Joe Hendrix** Here's an example of what I mean. Unfortunately I had to fight lean somewhat to write the instance, possibly the ergonomics of instance writing needs work.
```lean
@[class] meta inductive reflect_decidable (p : Prop)
| is_true (h : p) : /-reflected h-/ expr → reflect_decidable
| is_false (h : ¬ p) : /-reflected h-/ expr → reflect_decidable
open reflect_decidable

meta instance {p q : Prop} [reflected p] [reflected q] :
  ∀ [reflect_decidable p] [reflect_decidable q],
  reflect_decidable (p ∨ q)
| (is_true h e) _ := is_true (or.inl h) (expr.app `(@or.inl p q) e)
| _ (is_true h e) := is_true (or.inr h) (expr.app `(@or.inr p q) e)
| (is_false h₁ e₁) (is_false h₂ e₂) :=
  is_false (not_or h₁ h₂) (expr.mk_app `(@not_or p q) [e₁, e₂])

meta instance : reflect_decidable true := is_true trivial `(trivial)

open tactic
meta def by_reflection : tactic unit :=
do tgt ← target,
  let ty := `(reflect_decidable %%tgt),
  inst ← mk_instance ty,
  is_true _ e ← @tactic.eval_expr (reflect_decidable true)
    (by delta reflected; exact ty) inst,
  exact e

def ex : true ∨ true := by by_reflection
#print ex -- or.inl trivial
```

#### [Joe Hendrix (Dec 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152644194):
That would kind of work.  One downside is that `reflect_decidable` is meta.  I'm interested in trying to write provably correct decision procedures, not just proof producing.  I'll try this approach in the short term though.

#### [Mario Carneiro (Dec 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152645158):
it has to be meta, because it's creating `expr`s

#### [Mario Carneiro (Dec 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152645165):
this is a limitation of lean 3 tactic framework

#### [Mario Carneiro (Dec 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152645210):
You could create objects that are like `expr` but not meta, and then post process at the end, but that would add some extra overhead

