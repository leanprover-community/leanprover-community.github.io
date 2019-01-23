---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/82236Instanceaffectsothersections.html
---

## Stream: [new members](index.html)
### Topic: [Instance affects other sections](82236Instanceaffectsothersections.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154128043):
```lean
import data.finsupp
variables {σ : Type*} {α : Type*}

section a
variables [comm_semiring α] [decidable_eq σ] [decidable_eq α] [linear_order (σ →₀ ℕ)] [@decidable_rel (σ →₀ ℕ) (≤)]

instance : decidable_linear_order (σ →₀ ℕ) := {
    decidable_le := _inst_5,
    decidable_eq := by apply_instance,
    .._inst_4
}
end a

section b
variables [integral_domain α] [decidable_eq σ] [decidable_eq α] [linear_order (σ →₀ ℕ)] [@decidable_rel (σ →₀ ℕ) (≤)]

end b
```

The error message : "is maximum class-instance resolution depth has been reached (the limit can be increased by setting option 'class.instance_max_depth') (the class-instance resolution trace can be visualized by setting option 'trace.class_instances')" at the `(≤)` in `section b`
seems like `section b` is affected by the `decidable_linear_order` instance in `section a`, but I don't understand why, and how to fix this...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 01 2019 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154128780):
I don't have access to Lean right now but is the issue that the instance gives you a linear order on the finsupp and then in section b you are putting another unrelated order on the finsupp and hence breaking the golden rule of typeclasses -- one instance per type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129611):
instances are not scoped to sections

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129654):
It's just as though you wrote `instance <long string of variables> : decidable_linear_order (σ →₀ ℕ)` at the top level.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129664):
If you want to make a scoped instance, you can write an ordinary definition and then give it `local attribute [instance]` inside a `section`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 01 2019 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129771):
Leaving aside the `section` issue, I think this is a bad instance, because there's a cycle, there's a `linear_order` to `decidable_linear_order` instance, and a `decidable_linear_order` to `linear_order` instance somewhere in the library. This sort of thing can cause type class inference to get stuck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129920):
@**Kevin Buzzard**  actually the order in `section a` and `section b` are the same in my case, but some functions in `section a` are only depend on `comm_semiring α`, while functions in `section b` are depend on `integral_domain α`. I can only think of using seperate sections like this to avoid confilict between `comm_semiring α` and `integral_domain α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129984):
From what you've provided so far it looks like the hypotheses involving $$\alpha$$ are independent of the hypotheses involving $$\sigma$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154129987):
that is, no hypothesis involves both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130045):
@**Reid Barton**  you mean like ?
```lean
def x [decidable_eq σ] [linear_order (σ →₀ ℕ)] [@decidable_rel (σ →₀ ℕ) (≤)]
: decidable_linear_order (σ →₀ ℕ) := {
    decidable_le := _inst_3,
    decidable_eq := by apply_instance,
    .._inst_2
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130110):
Yes, or using `variables` the way you do now is also fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130249):
Then when a lemma needs this decidable_linear_order instance, it won't automatically infer this instance right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 01 2019 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130299):
That's right, but you can "install" the instance locally in a proof using `letI`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130345):
@**Chris Hughes**  Yeah..you're right...
but I can't just add an instance `[decidable_linear_order (σ →₀ ℕ)]`,  as it might cause conflict between `finsupp.decidable_eq` and `decidable_linear_order.decidable_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 01 2019 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130587):
`decidable_linear_order.decidable_eq` isn't an instance, so it's okay.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154130992):
But I do encounter such kind of error... some term looks just the same, and I couldn't use `rw` tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154131487):
This is the minimal example I can figure out so far...
there is a type mismatch at `rw union_min'` which says `h₁` uses `finsupp.decidable_eq` but the third parameter of `union_min'` is expected to use `eq.decidable`

```lean

import linear_algebra.multivariate_polynomial
import data.finset
variables {σ : Type*} {α : Type*} {β : Type*}


lemma ne_empty_union [decidable_eq α] {s₁ s₂ : finset α} : ¬ (s₁ = ∅ ∧ s₂ = ∅) ↔ s₁ ∪ s₂ ≠ ∅ := sorry

section a
variables [has_zero β] [decidable_eq α] [decidable_eq β]
lemma support_ne_empty (a : α →₀ β) : a ≠ 0 ↔ a.support ≠ ∅ := by finish

end a

section b
variables [decidable_linear_order α]
lemma union_min' {s₁ s₂ : finset α} (hs₁ : s₁ ≠ ∅) (hs₂ : s₂ ≠ ∅) (hs₃ : s₁ ∪ s₂ ≠ ∅):
(s₁ ∪ s₂).min' hs₃ = min (s₁.min' hs₁) (s₂.min' hs₂) := sorry

end b

section c
variables [decidable_eq σ] [decidable_eq α] [decidable_linear_order (σ →₀ ℕ)]
variables [comm_semiring α] 

lemma x {p q : mv_polynomial σ α} (hp : p ≠ 0) (hq : q ≠ 0) (hpq : p + q ≠ 0) : p + q ≠ 0 :=
begin
    have h₁ := (ne_empty_union.1 (not_and_of_not_left (q.support = ∅) ((support_ne_empty p).1 hp))),
    let h : finset.min' _ h₁ = finset.min' _ h₁ := by refl,
    rw union_min' ((support_ne_empty p).1 hp) ((support_ne_empty q).1 hq) h₁ at h,
end

end c
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 01 2019 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154135743):
I'm not sure I understand your question, but you may like:
```lean
lemma x {p q : mv_polynomial σ α} (hp : p ≠ 0) (hq : q ≠ 0) (hpq : p + q ≠ 0) : p + q ≠ 0 :=
begin
    have h₁ := ne_empty_union.1 (not_and_of_not_left (q.support = ∅) $ (support_ne_empty p).1 hp),
    have := union_min' ((support_ne_empty p).1 hp) ((support_ne_empty q).1 hq) (by convert h₁),
    exact hpq
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 01 2019 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154136362):
and I suspect that filling in the decidable_linear_order instance would help avoiding the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 01 2019 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154136639):
It's not a nice solution, but adding this line before `x` works `local attribute [instance, priority 0] finsupp.decidable_eq`. There's not a good solution for this sort of thing in general at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 01 2019 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Instance%20affects%20other%20sections/near/154137734):
@**Patrick Massot**  @**Chris Hughes**  Thanks a lot! Both solutions seems to solve my problem.


{% endraw %}
