---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05921Provingfromoptionalparameter.html
---

## Stream: [new members](index.html)
### Topic: [Proving from optional parameter](05921Provingfromoptionalparameter.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 13 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147601867):
How do I fill in the sorry?

```lean
example (c : ℝ) (f : ℝ → ℝ) (g : ℝ → ℝ := λ (x : ℝ), f (2 * c - x)) :  ∀ x, g x = f (2 * c - x) := sorry
```

Presumably I need to intro and input an `x` into `g` somehow -- but how? I know the specific example can be rewritten in a way that makes the proof `by assumption`, but this situation cropped up in another proof.

#### [ Chris Hughes (Nov 13 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147602168):
I don't think this is true. The `:=` notation for `g`, just assigns a default value to `g`, if the user doesn't specify one when using the lemma, but you still have to prove for any `g`, since the user can override the default and use whatever value for `g` they like when using the lemma.

#### [ Kevin Buzzard (Nov 13 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147608991):
Maybe you want `let g := ... in ...`?

#### [ Chris Hughes (Nov 13 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147610158):
If you have `let g := something` in some proof, you can prove `g = something`   with `rfl`.


{% endraw %}
