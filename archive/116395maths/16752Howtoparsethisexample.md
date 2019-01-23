---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/16752Howtoparsethisexample.html
---

## Stream: [maths](index.html)
### Topic: [How to parse this example?](16752Howtoparsethisexample.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) None proffered (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060242):
How to parse this example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) None proffered (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060265):
example : (∃ x, p x → r) ↔ (∀ x, p x) → r

#### [![Click to go to Zulip](../../assets/img/zulip2.png) None proffered (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060288):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) None proffered (Aug 07 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060615):
Is it (1) [(∃ x, p x → r)] ↔[ (∀ x, p x) → r] for CCCC CCCC TNTN TTTT in M8/VL4; or 
Is it (2)  [(∃ x, p x → r) ↔ (∀ x, p x)] → r for CCCC TTTT TNTN TTTT in M8/VL4.
In either case, Eqs. 1 or 2 are not tautologous (all designated proof value of T).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131067561):
```lean
variables (α : Type) (p : α → Prop) (r : Prop)
example : ( (∃ x, p x → r) ↔ (∀ x, p x) → r ) = ( (∃ x, p x → r) ↔ ( (∀ x, p x) → r ) ) := rfl
```

Apparently it's the former: (1).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 08 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131078022):
@**None proffered** the parse is (1) as Kevin says. I don't know what "CCCC CCCC TNTN TTTT" means; what is M8/VL4? This theorem is not true when the domain of `x` is empty. I assume you got this example from `tests/finish3.lean`, which proves two versions of this:
```lean
variables (A : Type) (p : A → Prop) (r : Prop)
example (a : A) : (∃ x, p x → r) ↔ (∀ x, p x) → r := begin safe [iff_def]; exact h a end
example : (∃ x, p x → r) → (∀ x, p x) → r := by finish
```
So it is provable in one direction unconditionally, but the bidirectional version requires some `a : A`, i.e. `A` has to be nonempty.


{% endraw %}
