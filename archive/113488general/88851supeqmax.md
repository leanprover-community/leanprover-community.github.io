---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88851supeqmax.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [sup_eq_max](https://leanprover-community.github.io/archive/113488general/88851supeqmax.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jul 06 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199027):
<p>Is there a nice way to state the lemma <code>a ⊔ b = max a b</code>, in general, for when <code>sup</code> is not derived from <code>max</code> such as on <code>with_bot</code>, or do I just have to prove it for <code>with_bot</code></p>

#### [ Mario Carneiro (Jul 06 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199724):
<p>You can prove <code>sup a b = max a b</code> on any type for which <code>max</code> makes sense</p>

#### [ Mario Carneiro (Jul 06 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199934):
<p>Oh, I see... There are two <code>lattice</code> structures on <code>with_bot</code> that don't coincide by defeq</p>

#### [ Mario Carneiro (Jul 06 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129199952):
<p>but they are the same since they have the same <code>le</code></p>

#### [ Mario Carneiro (Jul 06 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200322):
<p>unfortunately, despite how I've said that non-defeq diamonds are evil and should be avoided, there is not much I can do about this one since it would require adding a <code>sup</code> field to <code>decidable_linear_order</code> which is in core</p>

#### [ Chris Hughes (Jul 06 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200405):
<p>It makes sense to add this lemma then?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sup_eq_max</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">max</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">le_antisymm</span> <span class="o">(</span><span class="n">sup_le</span> <span class="o">(</span><span class="n">le_max_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">le_max_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span> <span class="o">(</span><span class="n">max_le</span> <span class="n">le_sup_left</span> <span class="n">le_sup_right</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jul 06 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200478):
<p>/me thinks that core shouldn't be in core</p>

#### [ Chris Hughes (Jul 06 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200612):
<p>Why did that message appear next to your name instead of beneath?</p>

#### [ Kevin Buzzard (Jul 06 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200630):
<p>because he only thought it, he didn't post it</p>

#### [ Kevin Buzzard (Jul 06 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200681):
<p>There are rumours that core won't be in core in Lean 4</p>

#### [ Johan Commelin (Jul 06 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sup_eq_max/near/129200728):
<blockquote>
<p>Why did that message appear next to your name instead of beneath?</p>
</blockquote>
<p>Yeah, I'm old. My IRC habits betray me. (Hint: type <code>/me</code> before your message.)</p>


{% endraw %}
