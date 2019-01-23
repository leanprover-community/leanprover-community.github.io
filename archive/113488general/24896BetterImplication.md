---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24896BetterImplication.html
---

## Stream: [general](index.html)
### Topic: [Better Implication](24896BetterImplication.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287484):
I can write `if h:cnd then aa else bb`.
Inside each breach, I have access to `h`.
Suppose I only want to write something like `h:cnd → aa` (`else` branch is `true`).
Is there anyway to do this without writing `if h:cnd then aa else true`?
The similar question is for `h:cnd ∧ aa`.
I rather not use `∀h:cnd, aa`, since if I have `cnd` or its complement in local hypotheses, `simp` does not simplify.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287490):
just write `cnd -> aa`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287549):
I want to use `h` in RHS

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287801):
Here is an example (please ignore the actual definitions, just the usage),
```lean
variable α : Type
def exp (a:α) (h:a≠0) : a * a = a := sorry -- some function that takes an input and requires something to be true about that input
example (a:α) : ∀ a:α, h:a≠0 → a = exp a h -- for any `a` in the domain of `exp`, we have some property
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287816):
the "standard" approach in mathlib is to define the function without assuming the condition, and prove the theorems assuming the condition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287820):
i.e. don't make the condition one of the arguments to the function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287938):
Not sure that is what I wanted. For example, I can always use `if then else`, but then one branch is always useless. I was looking for a solution to this problem, not erasing it. ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287961):
I don't recommend using `if then else` at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288045):
You should use `∀h:cnd, aa` in this case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288152):
Well, `simp` does not handle `∀h:cnd, aa` when I have `h:cnd` in local hypotheses. Right? Any other way, to automatically simplify `∀h:cnd, aa` (this will be more serious when the quantification is part of a bigger condition)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288268):
`specialize`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288534):
I see. Tell me whether these simp lemmas work in your use-case:
```
@[simp] theorem forall_prop_of_true {p : Prop} {q : p → Prop} (h : p) : (∀ h' : p, q h') ↔ q h :=
@forall_const (q h) p ⟨h⟩

@[simp] theorem exists_prop_of_true {p : Prop} {q : p → Prop} (h : p) : (∃ h' : p, q h') ↔ q h :=
@exists_const (q h) p ⟨h⟩

@[simp] theorem forall_prop_of_false {p : Prop} {q : p → Prop} (hn : ¬ p) : (∀ h' : p, q h') ↔ true :=
iff_true_intro $ λ h, hn.elim h

@[simp] theorem exists_prop_of_false {p : Prop} {q : p → Prop} : ¬ p → ¬ (∃ h' : p, q h') :=
mt Exists.fst
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288622):
But I will remark that this situation is rather rare in mathlib, because we try to avoid partial functions, which tend to make rewriting difficult. From the code you've shown here before, you seem to prefer partial functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288748):
Thank you, they help.
Did you just wrote them?
Also, the last one does not type check.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289030):
Yes I did. For the last one you should have `logic.basic` imported

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289044):
I haven't done anything about code generation. But what I have in mind is a type that take parameters and has different fields based on values of those parameters. In C++, I can easily use template to have those fields defined based on the input template arguments. In Lean, I am trying to have the same effect, by making sure that every time I am reading a field, it is defined.
```lean
structure constraint 
          (α : Type*)
          (trvk : triviality_kind)
          (dirk : direction_kind )
          (strk : strictness_kind)
          :=
cnstr ::
  (tri : trvk = triviality_kind.kdyn → triviality)
  (str : strk = strictness_kind.kdyn → strictness)
  (bnd : trvk ≠ triviality_kind.ktrv → α         )
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289117):
(I'm assuming the reason it doesn't typecheck is because it says `Exists.fst` can't be found; that's a hint.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289180):
I would suggest using an inductive type to encode these constraints

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289239):
I think it will be easier for you to return a default value when you can, and an option when there is no reasonable default, to totalize your functions. If you are going for efficiency, this won't achieve it anyway due to thunk generation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289284):
Could you link to your files where you define these `triviality_kind` etc? Let me make a mockup

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289353):
I used that first, but it has its own problem.
For example, suppose I have two constraints and I want to add them.
But not only I want to define addition for constraints with the same type parameters, but also in case the result cannot be represented by a constraint, I want to return a smallest representable constraint that is of the right type. If I push everything inside one inductive type, then I have to put extra condition on the signature of addition (or I don't know how else I can do it).
https://github.com/nima-roohi/lets-learn-some-lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289504):
What does adding constraints mean here? If I understand your model correctly, you want to be able to represent the sets `true`, `{x | x R a}`, and `{x | a R x}` where `R` is `<=` or `<`. Does adding the sets mean all pointwise additions, i.e. `{x + y | x \in c1, y \in c2}`, or the intersection / union of constraints or something else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289557):
`addition` is just an example. You can assume pointwise addition as you defined.
If `α` is, for example, `float` then even addition of two constraints cannot always be represented by a constraint.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289665):
Is there anyway I can change this `notation` so the example will work?
```lean
notation  c`:`h `→` hh := if c:h then hh else true
example : (h : 1>2) → 1>2 := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289768):
Here's more or less what I'm thinking:
```
import algebra.ordered_group

inductive constraint (α : Type*) 
| triv {} : constraint
| le : α → constraint
| lt : α → constraint
| ge : α → constraint
| gt : α → constraint

namespace constraint

def is_trivial {α} : constraint α → bool
| constraint.triv := tt
| _ := ff

def get_bound {α} : constraint α → option α
| constraint.triv := none
| (constraint.le a) := some a
| (constraint.lt a) := some a
| (constraint.ge a) := some a
| (constraint.gt a) := some a
--add others to taste, but you shouldn't need them

protected def mem {α} [preorder α] (x : α) : constraint α → Prop
| constraint.triv := true
| (constraint.le a) := a ≤ x
| (constraint.lt a) := a < x
| (constraint.ge a) := x ≤ a
| (constraint.gt a) := x < a

instance {α} [preorder α] : has_mem α (constraint α) := ⟨constraint.mem⟩

protected def add {α} [ordered_comm_group α] : constraint α → constraint α → constraint α
| constraint.triv c2 := c2
| c1 constraint.triv := c1
| (constraint.le a) (constraint.le b) := constraint.le (a + b)
| (constraint.le a) (constraint.lt b) := constraint.lt (a + b)
| (constraint.lt a) (constraint.le b) := constraint.lt (a + b)
| (constraint.lt a) (constraint.lt b) := constraint.lt (a + b)
| (constraint.ge a) (constraint.ge b) := constraint.ge (a + b)
| (constraint.ge a) (constraint.gt b) := constraint.gt (a + b)
| (constraint.gt a) (constraint.ge b) := constraint.gt (a + b)
| (constraint.gt a) (constraint.gt b) := constraint.gt (a + b)
| _ _ := constraint.triv

instance {α} [ordered_comm_group α] : has_add (constraint α) := ⟨constraint.add⟩

end constraint
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289820):
You can't define the arrow and colon as notations; they are reserved for function types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125290011):
I see what you mean by making a function total.
May be that makes things easier.
But I am not sure about performance of the result code.
Also, in your definition you only have one `le`, but I have two of them (dynamic vs static). So if every time I have to write all the cases, that might be a problem itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125290452):
Okay, version 2:
```
import algebra.ordered_group

inductive direction | lower | upper

inductive constraint (α : Type*) 
| triv {} : constraint
| mk (dir : direction) (strict : bool) (dynamic : bool) (bound : α) : constraint

namespace constraint
open direction

def is_trivial {α} : constraint α → bool
| triv := tt
| _ := ff

def get_bound {α} : constraint α → option α
| triv := none
| (mk a s d b) := some b

protected def mem {α} [preorder α] (x : α) : constraint α → Prop
| triv := true
| (mk lower ff d a) := a ≤ x
| (mk lower tt d a) := a < x
| (mk upper ff d a) := x ≤ a
| (mk upper tt d a) := x < a

instance {α} [preorder α] : has_mem α (constraint α) := ⟨constraint.mem⟩

protected def add {α} [ordered_comm_group α] : constraint α → constraint α → constraint α
| (mk lower s1 d1 a) (mk lower s2 d2 b) := mk lower (s1 || s2) (d1 || d2) (a + b)
| (mk upper s1 d1 a) (mk upper s2 d2 b) := mk upper (s1 || s2) (d1 || d2) (a + b)
| _ _ := constraint.triv

instance {α} [ordered_comm_group α] : has_add (constraint α) := ⟨constraint.add⟩

end constraint
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 19 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125290742):
Thank you.
I guess the biggest difference between what you wrote and what I have is that, assuming we are defining the same concept, in my definition when `dynamic` is `ff` then there is no field named `strict` (at least intuitively). If I preserve that restriction throughout my definition, (I hope) that transforming these into a code would be easier, at least when I do it manually!!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125291309):
I'm making up stuff as I go along re: the actual semantics, but I assume it looks something like this:
```
import algebra.ordered_group

inductive direction | lower | upper
inductive strictness | stt | nst | dyn

namespace strictness

def is_strict : strictness → bool
| stt := tt
| _ := ff

def join : strictness → strictness → strictness
| dyn _ := dyn
| _ dyn := dyn
| stt _ := stt
| _ stt := stt
| _ _ := nst

end strictness

inductive constraint (α : Type*) 
| triv {} : constraint
| mk (dir : direction) (strict : strictness) (bound : α) : constraint

namespace constraint
open direction

def is_trivial {α} : constraint α → bool
| triv := tt
| _ := ff

def get_bound {α} : constraint α → option α
| triv := none
| (mk a s b) := some b

protected def mem {α} [preorder α] (x : α) : constraint α → Prop
| triv := true
| (mk lower s a) := if s.is_strict then a < x else a ≤ x
| (mk upper s a) := if s.is_strict then x < a else x ≤ a

instance {α} [preorder α] : has_mem α (constraint α) := ⟨constraint.mem⟩

protected def add {α} [ordered_comm_group α] : constraint α → constraint α → constraint α
| (mk lower s1 a) (mk lower s2 b) := mk lower (s1.join s2) (a + b)
| (mk upper s1 a) (mk upper s2 b) := mk upper (s1.join s2) (a + b)
| _ _ := constraint.triv

instance {α} [ordered_comm_group α] : has_add (constraint α) := ⟨constraint.add⟩

end constraint
```

