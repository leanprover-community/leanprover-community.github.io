---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/42829Defininginstances.html
---

## [maths](index.html)
### [Defining instances](42829Defininginstances.html)

#### [Sebastien Gouezel (Oct 13 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135736954):
I am trying to define an instance of a normed space starting from a norm satisfying the right axioms, but I would need some help. Here is the situation:
```lean
def normed_group_of_norm {α : Type} [a: add_comm_group α] [b: has_norm α]
(norm_triangle : ∀x y: α, norm (x + y) ≤ norm x + norm y)
(norm_zero : norm (0 : α) = 0)
(eq_of_norm_eq_zero : ∀(x:α), norm x = 0 → x = 0)
(norm_neg : ∀(x:α), norm (-x) = norm x) : normed_group α :=
have A: metric_space α := metric_space.mk''
{ dist := λx y, norm (x - y),
  dist_self := by simp [norm_zero],
  eq_of_dist_eq_zero := λx y hxy, sub_eq_zero.1 (eq_of_norm_eq_zero _ hxy),
  dist_comm := λx y, begin have A := norm_neg (x-y), simp at A, simp [A.symm] end,
  dist_triangle :=λx y z, by simpa using norm_triangle (x-y) (y-z)
},
{
   dist_eq := sorry,
    ..a, ..b, ..A
}
```
A normed group is an abelian group together with a norm, with the property that the distance should be given by `dist x y = norm(x-y)`. It extends metric spaces, so I first define the metric space structure I want (`A` above), and then I just have to check this equality, which is by definition of `A`. But I do not see how to get access to the formula in the definition of `A`, so I am stuck...

#### [Kenny Lau (Oct 13 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135736958):
don't we already have this?

#### [Sebastien Gouezel (Oct 13 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737005):
No, I don't think so. Normed groups are defined in `analysis/normed_space.lean`, but there is no constructor just in terms of a norm.

#### [Kenny Lau (Oct 13 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737063):
is there anything about `abs`?

#### [Sebastien Gouezel (Oct 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737111):
My question is not specifically about this situation, it is rather that there is something I don't know about the syntax or the way to access fields.

#### [Kenny Lau (Oct 13 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737157):
(maybe unrelated) I recall there's no wrapper for `norm_mul`

#### [Sebastien Gouezel (Oct 13 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737621):
Here is the same question in a completely basic setting:
```lean
structure my_test := (f : ℕ → ℕ)

lemma foo : true :=
have A : my_test := {f := λx, x},
have B: ∀x, A.f x = x := begin intros x, sorry end,
trivial
```
I just want to get access to the definition of the field `f` in the structure I have constructed.

#### [Kenny Lau (Oct 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737675):
that isn't possible because `have` doesn't store data

#### [Johannes Hölzl (Oct 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737677):
Yes: you need to use `let m : metric_space A := ...` instead of the `have`

#### [Sebastien Gouezel (Oct 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135737679):
Thanks!

#### [Patrick Massot (Oct 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738014):
Sébastien, I'm not sure I understand your question, but https://github.com/leanprover/mathlib/blob/master/analysis/normed_space.lean#L276 does define a normed stuff instance explicitly

#### [Sebastien Gouezel (Oct 13 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738272):
Yes, but the metric space structure had already been defined before on \R. I am maximally lazy here: starting just from the norm, I want to define simultaneously the metric space and the normed space. In the same way, when you have a distance, you don't want to define by hand the topological structure, then the uniform structure, then the metric space structure: you want a constructor that does all this for you.

#### [Sebastien Gouezel (Oct 13 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738327):
And it works perfectly thanks to the hints of Kenny and Johannes:
```lean
structure normed_group.core (α : Type) [add_comm_group α] [has_norm α] :=
(norm_triangle : ∀x y: α, norm (x + y) ≤ norm x + norm y)
(norm_zero : norm (0 : α) = 0)
(eq_of_norm_eq_zero : ∀(x:α), norm x = 0 → x = 0)
(norm_neg : ∀(x:α), norm (-x) = norm x)

def normed_group_of_norm {α : Type} [a: add_comm_group α] [b: has_norm α]
(m : normed_group.core α) : normed_group α :=
let A : metric_space α := metric_space.mk''
{ dist := λx y, norm (x - y),
  dist_self := by simp [m.norm_zero],
  eq_of_dist_eq_zero := λx y hxy, sub_eq_zero.1 (m.eq_of_norm_eq_zero _ hxy),
  dist_comm := λx y, begin have A := m.norm_neg (x-y), simp at A, simp [A.symm] end,
  dist_triangle :=λx y z, by simpa using m.norm_triangle (x-y) (y-z)
} in
{ dist_eq := λx y, rfl,
  ..a, ..b, ..A
}
```
(Don't try this, it depends on my emetric spaces pull request for the metric space constructor)

#### [Kenny Lau (Oct 13 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738347):
I would define the metric space separately first

#### [Kenny Lau (Oct 13 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738348):
and avoid `let`

#### [Kenny Lau (Oct 13 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738385):
if you still want to keep it, I would add `set_option zeta.compiler true`

#### [Johan Commelin (Oct 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738400):
@**Sebastien Gouezel** The `let` statements aren't parsed away, they go all the way down to the kernel. Sometimes I wish there was a "syntactic sugar" variant, maybe called `where`.

#### [Johan Commelin (Oct 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738402):
But like Kenny suggests, you might want to split it up any way.

#### [Sebastien Gouezel (Oct 13 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738462):
How would you avoid the `let`? I insist on having one single constructor that takes a `normed_group.core` and gives a normed group, that's really the point here.

#### [Johan Commelin (Oct 13 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738665):
This constructor could call another one, right?

#### [Johan Commelin (Oct 13 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738711):
If you just factor out the `let`-statement into a separate `instance`. Or am I missing something?

#### [Johan Commelin (Oct 13 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining instances/near/135738727):
Maybe some `refine_struct` magic could also help. But I'm not an expert on this.

