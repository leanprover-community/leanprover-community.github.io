---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48938optiontroubles.html
---

## Stream: [general](index.html)
### Topic: [option troubles](48938optiontroubles.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135487811):
I have `x : option X`, and `h : x ≠ none`. How do I turn this into a `y : X` such that `x = some y`? I want to use `option.get` and `option.is_some`. But I can't figure out how to use `h`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135487845):
```lean
example {X : Type} (x : option X) (h : x ≠ none) : X := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135487859):
Or something like that. I should probably not just return an `y : X`, but also the proof that `x = some y`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488210):
```lean
example {α : Sort*} (x : option α) : x ≠ none → {y // x = some y} :=
option.rec_on x (absurd rfl) (λ y _, ⟨y, rfl⟩)
```
There should be a lemma that says `is_some_iff_ne_none`, but it seems to be missing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488265):
Depending on the use, it might be more convenient to just do the `cases`, `absurd` at the usage site

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488560):
Thanks @**Chris Hughes** and @**Reid Barton** !

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488579):
as in 
```lean
example {X : Type} (x : option X) (h : x ≠ none) : {y // x = some y} := 
begin
  cases x with a,
  exact absurd (by simpa [h]) not_false,   
  exact ⟨a, rfl⟩
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135489285):
there is `is_none_iff_eq_none`, but nothing connecting `is_some` and `is_none`. I guess we need a few more variants

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135489316):
but the basic story is `option.get` is supposed to do this


{% endraw %}
