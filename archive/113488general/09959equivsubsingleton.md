---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09959equivsubsingleton.html
---

## Stream: [general](index.html)
### Topic: [equiv_subsingleton](09959equivsubsingleton.html)

---


{% raw %}
#### [ Johan Commelin (Jan 14 2019 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155086021):
<p>I couldn't find this in mathlib. Is this considered useful enough to include?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">equiv_subsingleton</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">subsingleton</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">subsingleton</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">α</span> <span class="err">≃</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">g</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">subsingleton</span><span class="bp">.</span><span class="n">elim</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">subsingleton</span><span class="bp">.</span><span class="n">elim</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>
</pre></div>


<p>If so, where should it go?</p>

#### [ Chris Hughes (Jan 14 2019 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155086282):
<p>Only one of them needs to be a subsingleton.</p>

#### [ Chris Hughes (Jan 14 2019 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155087369):
<p>I misread the statement</p>

#### [ Kenny Lau (Jan 14 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155119532):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> it isn't a lemma</p>

#### [ Reid Barton (Jan 15 2019 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155147420):
<p>Yes it is useful. Not sure about the name though, it should be in the <code>equiv</code> namespace. Perhaps <code>equiv.of_subsingleton</code>?</p>


{% endraw %}
