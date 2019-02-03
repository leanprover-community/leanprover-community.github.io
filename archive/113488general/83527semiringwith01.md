---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83527semiringwith01.html
---

## Stream: [general](index.html)
### Topic: [semiring with 0 ≠ 1](83527semiringwith01.html)

---


{% raw %}
#### [ Chris Hughes (May 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453723):
<p>Is there a type class for a semiring with <code>0 ≠ 1</code>?</p>

#### [ Chris Hughes (May 12 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453838):
<p>I tried <code>[semiring α] [zero_ne_one_class α]</code> but then I ended up with two different definitions of one.</p>

#### [ Kenny Lau (May 12 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453884):
<p>try to use old structure command and build a new class</p>

#### [ Kenny Lau (May 12 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453888):
<p>the diamond death you just experienced</p>

#### [ Johan Commelin (May 12 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454045):
<blockquote>
<p>I tried <code>[semiring α] [zero_ne_one_class α]</code> but then I ended up with two different definitions of one.</p>
</blockquote>
<p>Did you also end up with two different definitions of zero?</p>

#### [ Chris Hughes (May 12 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454136):
<p>Yes.</p>

#### [ Chris Hughes (May 12 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454244):
<p>Same question for <code>ring</code>.</p>

#### [ Chris Hughes (May 12 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454826):
<p>Would it have been better to define <code>zero_ne_one_class</code> as </p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">zero_ne_one_class</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">zero_ne_one</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≠</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (May 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454972):
<p>Yes. There is not much I can do about it</p>

#### [ Johan Commelin (May 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454984):
<p>Well, we can define our own <code>has_zero_ne_one</code>, right?</p>

#### [ Johan Commelin (May 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454986):
<p>In the way that Chris suggested</p>

#### [ Mario Carneiro (May 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455074):
<p>Sure. I would ask the reason for the use though, it seems not so useful</p>

#### [ Chris Hughes (May 12 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455083):
<p>I'm doing univariate polys, and I'm trying to prove <code>degree_of (X : uv_polynomial α) = 1</code></p>

#### [ Mario Carneiro (May 12 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455142):
<p>how is degree_of defined?</p>

#### [ Mario Carneiro (May 12 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455145):
<p>and X</p>

#### [ Chris Hughes (May 12 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455188):
<p>after unfolding it looks like this <code>sup ((single 1 1).support) id = 1</code></p>

#### [ Chris Hughes (May 12 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455190):
<p>unfolding single makes it become this <code>sup (ite (1 = 0) ∅ (singleton 1)) id = 1</code></p>

#### [ Mario Carneiro (May 12 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455201):
<p>is there decidable equality?</p>

#### [ Mario Carneiro (May 12 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455202):
<p>or are you classical</p>

#### [ Chris Hughes (May 12 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455241):
<p>Yes.</p>

#### [ Chris Hughes (May 12 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455242):
<p>there is decidable equality</p>

#### [ Chris Hughes (May 12 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455340):
<p>I could probably get around it by proving alternative lemmas like <code>degree_of_monomial</code>. Or just make <code>0 \ne 1</code> an argument to the theorem.</p>

#### [ Mario Carneiro (May 12 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455572):
<p>I used a typeclass <code>nonzero_ring</code> in my metamath formalization of this one. Perhaps <code>is_nonzero</code> can be a typeclass depending on <code>ring</code> instead of <code>has_zero</code> and <code>has_one</code>?</p>

#### [ Mario Carneiro (May 12 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455622):
<p>nonzero semiring seems like a bad idea though, it's not nearly as nice as it sounds since it is not cancellative</p>

#### [ Kevin Buzzard (May 12 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455825):
<p>Chris, from a mathematical point of view I am not so sure that people care too much about semirings. However I know lean is different. All I'm saying is that if it's easier to work with rings than semirings then from the point of view of mathematical applications you'll be losing essentially nothing.</p>

#### [ Chris Hughes (May 12 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126457579):
<p>I have the same problem with rings.</p>

#### [ Chris Hughes (May 12 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126458132):
<blockquote>
<p>I used a typeclass <code>nonzero_ring</code> in my metamath formalization of this one. Perhaps <code>is_nonzero</code> can be a typeclass depending on <code>ring</code> instead of <code>has_zero</code> and <code>has_one</code>?</p>
</blockquote>
<p>Do you mean extending <code>ring</code> or with <code>ring</code> as an argument?</p>

#### [ Mario Carneiro (May 12 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126460138):
<p><code>nonzero_ring</code> would <code>extends ring</code>, <code>is_nonzero : Prop</code> would have <code>[ring A]</code></p>


{% endraw %}
