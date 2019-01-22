---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61444Compactopentopology.html
---

## [maths](index.html)
### [Compact-open topology](61444Compactopentopology.html)

#### [Patrick Massot (Sep 24 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554654):
I see @**Johannes Hölzl**  merged https://github.com/leanprover/mathlib/pull/368 before Reid answered my comments. Was this done on purpose?

#### [Johannes Hölzl (Sep 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554751):
ah, no. I was focusing on the first comment and forgot the other ones...

#### [Patrick Massot (Sep 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554770):
I'm not saying they are crucial comments, but I was still suprised

#### [Johannes Hölzl (Sep 24 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134554771):
but I think also that `ev` could be changed to a `coe`.

#### [Patrick Massot (Sep 24 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134555078):
I rather meant that `C(α, β)` could have a coe to fun, so that the definition of `ev` becomes `def ev : C(α, β) × α → β := λ p, p.1 p.2`, or the maybe more readable `def ev : C(α, β) × α → β | (f, x) := f x`

#### [Reid Barton (Sep 24 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134557901):
Patrick, regarding your very last comment, I've had too many bad experiences writing proofs about things defined by matching, and so I never use pattern matching in definitions in simple cases now. I do regret the loss of readability though. That's why I suggested [lazy matching](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/eta.20for.20structures/near/130734254) (terminology borrowed from Haskell), so you could write `| ~(f, x) := f x` for `:= λ p, p.1 p.2`.

#### [Reid Barton (Sep 24 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134558026):
As for the PR, I'm happy to either pretend it is still open and reply to comments by making a new PR, or just leave it as-is for now, until someone gets annoyed at the name `ev`

#### [Patrick Massot (Sep 25 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589366):
I don't understand the lazy matching discussion. Both the following definition work:
```lean
def f : ℕ × ℕ → ℕ := λ ⟨x, y⟩, x+y

def g : ℕ × ℕ → ℕ | (x, y) := x+y
```
What would you like that doesn't work?

#### [Chris Hughes (Sep 25 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589548):
I think he wants to use notation similar to that to define `f` to be `λ x, x.1 + x.2`

#### [Patrick Massot (Sep 25 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589734):
But this is already this:
```lean
def f  : ℕ × ℕ → ℕ := λ ⟨x, y⟩, x + y
def f' : ℕ × ℕ → ℕ := λ x,  x.1 + x.2

example : f = f' :=
begin
  ext x, 
  cases x, 
  refl
end
```

#### [Chris Hughes (Sep 25 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589904):
He wants to use nice notation for it, the `.1` stuff is better for definitional reduction, but `λ ⟨x, y⟩, x + y` looks nicer.

#### [Johannes Hölzl (Sep 25 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134589937):
The problem happens when you use coercion, e.g. from a subtype. When you use matching:
```lean
definition f : subtype p -> A | ⟨a, ha⟩ := ⟨op a, ha...⟩
lemma coe_f : coe (f a) = op (coe a) := by cases a; refl
```
while using projection gives us a `rfl` proof:
```lean
definition f (x : subtype p) := ⟨op x.1, x.2...⟩
lemma coe_f : coe (f a) = op (coe a) := rfl
```

#### [Patrick Massot (Sep 25 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134590507):
Indeed I was suprised that my `f = f'` is not rfl

#### [Reid Barton (Sep 25 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134592411):
More generally, when you have a function `f : S -> T` and both `S` and `T` are structures, it's better (when possible) to have `T.mk ...` as the outer structure of `f`, and do the pattern matching on `S` inside, rather than having `S.rec_on` as the outer structure and constructing `T` inside.

#### [Reid Barton (Sep 25 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134592472):
Then if you compose with another such function `g : T -> U`, and you form `g (f s)`, the places where `g` pattern matches on its argument will reduce with the `T.mk` which is the outer structure of `f s`.

#### [Reid Barton (Sep 25 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134592488):
If you do it the other way then `g (f s)` will look like `T.rec_on (S.rec_on s ...) ...`, and you won't be able to make any progress unless `s` is already a constructor.

#### [Johannes Hölzl (Oct 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Compact-open%20topology/near/134968087):
FYI: I added a proper constant for the type of continuous maps and renamed the theory to `continuous_map`.

