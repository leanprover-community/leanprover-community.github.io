---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45033Sillyfunctiononthereals.html
---

## Stream: [maths](index.html)
### Topic: [Silly function on the reals](45033Sillyfunctiononthereals.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 28 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130481903):
I overheard people talking about this function the other day. Can anyone prove its existence?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 28 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130481906):
```lean
import data.real.basic

lemma silly_function : ∃ f : ℝ → ℝ, ∀ x y a : ℝ, x < y → ∃ z : ℝ, x < z ∧ z < y ∧ f z = a := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 28 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130481954):
that's the Conway base-13 function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130482878):
[other functions with this property are available]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130482926):
https://en.wikipedia.org/wiki/Conway_base_13_function . It's an extreme counterexample to "is the converse of the intermediate value theorem true?"


{% endraw %}
