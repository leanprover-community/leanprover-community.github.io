---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26286induction.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [induction](https://leanprover-community.github.io/archive/113488general/26286induction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jul 23 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145340):
<p>Occasionally I find myself having the goal <code>\forall n, P n</code> that I want to prove by induction. But (as a mathematician) I always allow myself to use <code>P m</code> for all <code>m &lt; n</code> in the induction step. So I would like to rewrite my initial goal into <code>\forall n m, m &lt; n \to P m</code>. Is a statement like that already in mathlib?</p>

#### [ Kenny Lau (Jul 23 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145429):
<blockquote>
<p>Occasionally I find myself having the goal <code>\forall n, P n</code> that I want to prove by induction. But (as a mathematician) I always allow myself to use <code>P m</code> for all <code>m &lt; n</code> in the induction step. So I would like to rewrite my initial goal into <code>\forall n m, m &lt; n \to P m</code>. Is a statement like that already in mathlib?</p>
</blockquote>
<p>strong induction?</p>

#### [ Johan Commelin (Jul 23 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145449):
<p>I don't know anything about strong induction. Is that the name for the thing I am talking about?</p>

#### [ Kenny Lau (Jul 23 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145519):
<p>it's called strong induction.</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span>
<span class="c1">-- nat.strong_induction_on :</span>
<span class="c1">--  ∀ {p : ℕ → Prop} (n : ℕ), (∀ (n : ℕ), (∀ (m : ℕ), m &lt; n → p m) → p n) → p n</span>
</pre></div>

#### [ Chris Hughes (Jul 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130157350):
<p>Read the section in TPIL on the equation compiler and the docs in mathlib on the equation compiler.</p>


{% endraw %}
