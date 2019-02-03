---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89520monotone.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [monotone](https://leanprover-community.github.io/archive/113488general/89520monotone.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 29 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357030):
<p>sehr geehrter <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> , monotone doesn't mean what you think it means</p>

#### [ Johannes Hölzl (Mar 29 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357527):
<p>What is the difference between <a href="https://github.com/leanprover/mathlib/blob/master/order/basic.lean#L19" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/basic.lean#L19">https://github.com/leanprover/mathlib/blob/master/order/basic.lean#L19</a><br>
<code>def monotone (f : α → β) := ∀⦃a b⦄, a ≤ b → f a ≤ f b</code><br>
and<br>
<code> class is_ord_hom (f : α → α) : Prop :=  (ord : ∀ x y, x ≤ y → f x ≤ f y) </code>?<br>
Monotone is a little bit more general, but not a type class...</p>

#### [ Kenny Lau (Mar 29 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357537):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> monotone means increasing <strong>or</strong> decreasing</p>

#### [ Kenny Lau (Mar 29 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357538):
<p>at least in where I'm from</p>

#### [ Johannes Hölzl (Mar 29 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357653):
<p>Not in order theory, the "Monotonicity in order theory" section in <a href="https://en.wikipedia.org/wiki/Monotonic_function" target="_blank" title="https://en.wikipedia.org/wiki/Monotonic_function">https://en.wikipedia.org/wiki/Monotonic_function</a> tells us that it means what you maybe call an increasing function.</p>

#### [ Kenny Lau (Mar 29 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357695):
<p>fair enough</p>


{% endraw %}
