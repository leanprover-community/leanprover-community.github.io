---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78620Simplifyditestatements.html
---

## Stream: [general](index.html)
### Topic: [Simplify dite statements](78620Simplifyditestatements.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 10 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233579):
I've noticed the following:
```lean
def p : ℕ → ℕ := λ n, if h : n > 5 then 10 else 0

example (n : ℕ) (hn : n > 5) : p n = 10 :=
begin simp only [dif_pos, hn, p] end -- works

example (n : ℕ) (hn : ¬n > 5) : p n = 0 :=
begin simp only [dif_neg, hn, p] end -- fails 
```

What additional simp lemmas are needed to solve the second example? And is there a tactic in Mathlib with roughly this behavior, reducing dite statements where the positive or negative proof is in the context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 10 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233746):
There is `split_ifs`:
```lean
import tactic.split_ifs

def p : ℕ → ℕ := λ n, if h : n > 5 then 10 else 0

example (n : ℕ) (hn : n > 5) : p n = 10 :=
by unfold p; split_ifs; refl

example (n : ℕ) (hn : ¬n > 5) : p n = 0 :=
by unfold p; split_ifs; refl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233821):
interestingly, this works:
```
example (n : ℕ) (hn : ¬n > 5) : p n = 0 :=
begin simp only [dif_neg hn, p] end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233827):
is it so interesting that it works?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233877):
it is interesting that `simp` won't connect the two parts together in the original version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233890):
I suppose it is because `¬n > 5` is not in simp normal form, so it gets rewritten and then the assumption `hn` doesn't match

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 10 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233938):
No? What is its simp normal form?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131233988):
It still fails if you make the > a <.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234002):
@**Gabriel Ebner** Thanks, that's useful! Somehow I assumed `split_ifs` did something different based on its name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234008):
in mathlib it will rewrite to `n <= 5`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 10 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234091):
```lean 
constant A : ℕ → Prop 
constant had : decidable_pred A 
attribute [instance] had

noncomputable def p : ℕ → ℕ := λ n, if h : A n then 10 else 0

example (n : ℕ) (hn : A n) : p n = 10 :=
begin simp only [dif_pos, hn, p] end -- works

example (n : ℕ) (hn : ¬ A n) : p n = 0 :=
begin simp only [dif_neg, hn, p] end -- fails 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234151):
Even better, it works without `only`:
```lean
example (n : ℕ) (hn : ¬n > 5) : p n = 0 := by simp [p, hn]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234161):
It needs one extra lemma:
```lean
example (n : ℕ) (hn : ¬n > 5) : p n = 0 :=
by simp only [p, hn, dif_neg, not_false_iff]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplify%20dite%20statements/near/131234265):
Aha! Thanks.


{% endraw %}
