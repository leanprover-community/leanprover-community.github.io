---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66435Whattacticforcesbetareductioningoalorhypothesis.html
---

## Stream: [general](index.html)
### Topic: [What tactic forces beta reduction in goal or hypothesis](66435Whattacticforcesbetareductioningoalorhypothesis.html)

---

#### [Kevin Sullivan (Oct 10 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135516798):
Clearly a newbie question -- but I don't see the answer at hand. Sorry to have to ask. E.g., if my current goal is 3 * 3 -= 8, how, in a tactic script, do I force the * expression to be evaluated, yielding 9 = 8 as the new goal?

#### [Simon Hudon (Oct 10 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135516869):
If you're dealing with number literals, use `norm_num`. It works whether you have large numbers or small ones. Reduction will get pretty slow.

#### [Kevin Buzzard (Oct 10 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135521476):
Because `3 * 3 = 9` is true by definition, if your goal is `3 * 3 = ...` then in tactic mode you can change it to `9 = ...` with the `show` tactic. 

```lean
example (h : 9 = 8) : 3 * 3 = 8 :=
begin
  show 9 = 8,
  exact h,
end

```

#### [Kevin Buzzard (Oct 10 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135521541):
The funny thing is that this works too:

```lean
example (h : 9 = 8) : 3 * 3 = 8 :=
begin
  exact h,
end
```

because Lean is quite happy to treat `3 * 3` and `9` as equal objects when attempting to convince itself that the hypothesis really is equal to the goal.

#### [Kevin Sullivan (Oct 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135541690):
The more general case  is one where the current goal involves expressions in which functions are applied to arguments. I'm looking for the tactic that simplifies the goal by reducing all of the (or perhaps selected) function application expressions to values.

#### [Patrick Massot (Oct 10 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135541985):
If you are ready to provide the new goal explicitly then `change` will do that

#### [Kevin Sullivan (Oct 10 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542310):
I was hoping to be able to just use a "simpl" (or whatever) tactic. Seems that Lean doesn't natively provide such a thing. I find that surprising.

#### [Patrick Massot (Oct 10 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542359):
Hold on

#### [Patrick Massot (Oct 10 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542610):
you could try something like:
```lean
meta def tactic.interactive.beta_red : tactic unit := `[dsimp only [] {beta := tt}]

example {α : Type*}  (a : α) : (λ x, x) a = a :=
begin
  beta_red, 
  refl
end
```

#### [Patrick Massot (Oct 10 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542635):
and probably set other config flag to false

#### [Patrick Massot (Oct 10 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542646):
I think we already has the same discussion before (or a closely related one)

#### [Kevin Buzzard (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135565975):
Maybe `unfold` is what you're looking for? Do you want to post an example of what you're trying to do?

