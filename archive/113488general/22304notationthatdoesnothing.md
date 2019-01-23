---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22304notationthatdoesnothing.html
---

## Stream: [general](index.html)
### Topic: [notation that does nothing](22304notationthatdoesnothing.html)

---


{% raw %}
#### [ Johan Commelin (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148107367):
I want something like this:
```lean
local notation ` [`n`] ` := (((id : ℕ → simplex_category) (n)) : simplex_category)
instance : has_coe_to_sort simplex_category := { S := Type, coe := λ n, fin $ n+1 }
```
In other words, it should take whatever is between `[` and `]`, interpret that as a `ℕ`, but interpret `[_]` as an element of `simplex_category`.
In this way, I can talk about `[n+1]` without defining addition or one for `simplex_category`. In this way I can also coerce `[n]` to `fin (n+1)` without defining that coercion for all naturals.
In other words, I would like to make sure that `i : [n+1]` typechecks.

#### [ Simon Hudon (Nov 21 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135059):
Your snippet doesn't work?

#### [ Chris Hughes (Nov 21 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135146):
Isn't this overloaded from `list`

#### [ Chris Hughes (Nov 21 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135157):
Use a different type of brackets?

#### [ Simon Hudon (Nov 21 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135163):
Instead of using `id`, try using:

```lean
def my_brackets (n : nat) : simplex_category := n
local notation ` [`n`] ` := my_brackets n
```

#### [ Simon Hudon (Nov 21 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135203):
Yes, that's also true

#### [ Simon Hudon (Nov 21 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135220):
A lot of brackets are already taken

#### [ Johan Commelin (Nov 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135866):
I now have
```lean
inductive simplex_category
| from_nat : ℕ → simplex_category

namespace simplex_category

local notation ` [`n`] ` := from_nat n

instance : has_coe_to_sort simplex_category :=
{ S := Type,
  coe := λ n, simplex_category.cases_on n (λ n, fin $ n+1) }

instance {Δ : simplex_category} : linear_order Δ := by cases Δ; unfold_coes; apply_instance

instance : category_theory.category simplex_category :=
{ hom := λ Δ Δ', {f : Δ → Δ' // monotone f},
  id := λ _, ⟨_, monotone_id⟩,
  comp := λ _ _ _ f g, ⟨_, monotone_comp f.2 g.2⟩ }
```
It seems to work as intended. It seems like a bit of a trick to define and inductive type that is equivalent to `nat`, but whatever.

#### [ Johan Commelin (Nov 21 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135918):
And I definitely want `[n]` notation. It's just silly that the notation for lists isn't local.

#### [ Kevin Buzzard (Nov 21 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148136538):
Making copies of inductive types is not uncommon. If you want to do congruence mod n on the integers, you run into problems because equivalence relations are a class but you want more than one equivalence relation on the integers. You can fix it by making these fake copies.


{% endraw %}
