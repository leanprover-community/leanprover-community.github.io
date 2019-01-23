---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20674customwellfounded.html
---

## Stream: [general](index.html)
### Topic: [custom well-founded](20674customwellfounded.html)

---


{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289818):
```lean
inductive red.step : list (α × bool) → list (α × bool) → Prop
| bnot {L₁ L₂ x b} : red.step (L₁ ++ (x, b) :: (x, bnot b) :: L₂) (L₁ ++ L₂)
```

How do I tell Lean that whenever `red.step L1 L2` is true, it is also true that `list.sizeof L2 < list.sizeof L1`?

#### [ Kenny Lau (Apr 19 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289821):
I don't want to provide a custom proof at the end of every recursion

#### [ Mario Carneiro (Apr 19 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289871):
You could prove that `red.step` itself is well-founded...

#### [ Kenny Lau (Apr 19 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289872):
it's in the wrong direction though

#### [ Mario Carneiro (Apr 19 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289874):
`swap red.step` then

#### [ Kenny Lau (Apr 19 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289890):
what is swap?

#### [ Mario Carneiro (Apr 19 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289892):
exactly what it sounds like

#### [ Mario Carneiro (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289895):
it's defined in `init.function` and swaps a binary operator (aka relation converse)

#### [ Mario Carneiro (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289937):
oh, I guess it is in `function` ns

#### [ Kenny Lau (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289939):
right

#### [ Kenny Lau (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289940):
so if I prove that `swap red.step` is well-founded, then I won't have to worry about anything?

#### [ Kenny Lau (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289987):
do you suppose I prove `has_well_founded (list (α × bool))`?

#### [ Mario Carneiro (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289991):
No, except perhaps locally if you like

#### [ Kenny Lau (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289993):
I mean, is it `has_well_founded (list (α × bool))` that I should prove?

#### [ Kenny Lau (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289994):
and then I can use recursion?

#### [ Mario Carneiro (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289995):
yes

#### [ Kenny Lau (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290000):
because "prove well-founded" is kinda vague of an instruction

#### [ Mario Carneiro (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290004):
you can also define a `well_founded` proof and then refer to it in your wf definition using `using_well_founded`

#### [ Mario Carneiro (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290010):
there are several examples of that in mathlib, just look for the keyword

#### [ Kenny Lau (Apr 19 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290053):
as I said, I don't want to write a custom proof at the end of every recursion

#### [ Kenny Lau (Apr 19 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290054):
I will be doing recurison much

#### [ Kenny Lau (Apr 19 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290109):
how would I prove that `red.step` is well-founded?

#### [ Kenny Lau (Apr 19 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290113):
I don't know how to use list lengths to prove that it is well-founded

#### [ Johannes Hölzl (Apr 19 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290273):
my first idea would be to use `subrelation.wf` and `inv_image.wf`.

#### [ Kenny Lau (Apr 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291560):
```lean
H1 : step L₁ L₄,
⊢ function.swap step L₄ L₁
```

#### [ Kenny Lau (Apr 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291563):
Lean's automater couldn't match this with "assumption"

#### [ Kenny Lau (Apr 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291564):
@**Mario Carneiro**

#### [ Mario Carneiro (Apr 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291620):
try `exact this` as the tactic instead

#### [ Kenny Lau (Apr 19 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291756):
can I not change the tactic ;_;

#### [ Kenny Lau (Apr 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291845):
Now I used `λ L₁ L₂, red.step L₂ L₁` as the well-founded relation instead and Lean is giving me ths ;_;

#### [ Kenny Lau (Apr 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291850):
```lean
match failed
state:
α : Type u,
L₃ : list (α × bool),
red.trans : ∀ (_p : Σ' {L₁ L₂ : list (α × bool)} (a : red L₁ L₂), red L₂ L₃), red (_p.fst) L₃,
L₁ L₂ L₄ : list (α × bool),
H1 : step L₁ L₄,
H2 : red L₄ L₂,
H23 : red L₂ L₃
⊢ step L₁ L₄
```

#### [ Kenny Lau (Apr 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291860):
keru mouri

#### [ Kenny Lau (Apr 19 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291948):
@**Mario Carneiro** sauva mi

#### [ Mario Carneiro (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291962):
You should use `using_well_founded` like I said

#### [ Kenny Lau (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291996):
I don’t want to use it after every single recursion ;_;

#### [ Mario Carneiro (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291997):
it's just one line, which you can copy around

#### [ Chris Hughes (Apr 20 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125467953):
@**Kenny Lau** 
```lean
def red : list α → list α → Prop := sorry

axiom red_length (l₁ l₂ : list α) : red l₁ l₂ → l₁.length < l₂.length

lemma red_well_founded : well_founded (@red α) := subrelation.wf red_length
(measure_wf list.length)
```
This might help if you haven't already worked it out.

#### [ Kenny Lau (Apr 21 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125473548):
@**Chris Hughes** thanks, but it still bugs me to provide a proof of well-foundedness

#### [ Kenny Lau (Apr 21 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125473597):
so in the end I proved
```lean
theorem red.sizeof : ∀ {L₁ L₂ : list (α × bool)}, red.step L₁ L₂ → L₂.sizeof < L₁.sizeof
```

and then in recursions I do:
```lean
theorem red.append : ∀ {L₁ L₂ L₃ L₄ : list (α × bool)},
  red L₁ L₃ → red L₂ L₄ → red (L₁ ++ L₂) (L₃ ++ L₄)
| _ _ _ _ red.refl red.refl := red.refl
| _ _ _ _ red.refl (red.step_trans H3 H4) := have _ := red.sizeof H3,
  red.step_trans (red.step.append_left H3) (red.append red.refl H4)
| _ _ _ _ (red.step_trans H1 H2) H3 := have _ := red.sizeof H1,
  red.step_trans (red.step.append_right H1) (red.append H2 H3)

```


{% endraw %}
