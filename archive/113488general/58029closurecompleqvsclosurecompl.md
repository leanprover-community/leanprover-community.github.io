---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58029closurecompleqvsclosurecompl.html
---

## Stream: [general](index.html)
### Topic: [closure_compl_eq vs closure_compl](58029closurecompleqvsclosurecompl.html)

---


{% raw %}
#### [ Kenny Lau (Oct 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058320):
<p><a href="/user_uploads/3121/799w6_d5y5HxDNH8PGRRdgyJ/2018-10-02-6.png" target="_blank" title="2018-10-02-6.png">closure_compl_eq vs closure_compl</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/799w6_d5y5HxDNH8PGRRdgyJ/2018-10-02-6.png" target="_blank" title="closure_compl_eq vs closure_compl"><img src="/user_uploads/3121/799w6_d5y5HxDNH8PGRRdgyJ/2018-10-02-6.png"></a></div><p><a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L261-L271" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L261-L271">https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L261-L271</a></p>

#### [ Kenny Lau (Oct 02 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058346):
<p>lemme <code>blame</code> this...</p>

#### [ Kenny Lau (Oct 02 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058452):
<p>it's <a href="https://github.com/leanprover/mathlib/commit/afefdcbb46f85e471ca258373d33e92a9d2dd61c#diff-6e52fa1a2004f6ddfddb7023e1ec2709R243" target="_blank" title="https://github.com/leanprover/mathlib/commit/afefdcbb46f85e471ca258373d33e92a9d2dd61c#diff-6e52fa1a2004f6ddfddb7023e1ec2709R243">this change</a> that moved the latter theorem from <code>topology/topological_space.lean</code> to <code>analysis/topology/topological_space.lean</code></p>

#### [ Patrick Massot (Oct 02 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058454):
<p>oh wow, there are actually adjacent!</p>

#### [ Kenny Lau (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058529):
<p>actually, below and above these theorems:</p>

#### [ Kenny Lau (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058578):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">interior_compl_eq</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">-</span> <span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">closure</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">closure_eq_compl_interior_compl</span><span class="o">]</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">closure_compl_eq</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">closure</span> <span class="o">(</span><span class="bp">-</span> <span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">interior</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">closure_eq_compl_interior_compl</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">closure_compl</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">closure</span> <span class="o">(</span><span class="bp">-</span><span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">interior</span> <span class="n">s</span> <span class="o">:=</span>
<span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">closure_subset_iff_subset_of_is_closed</span><span class="o">,</span> <span class="n">compl_subset_compl</span><span class="o">,</span> <span class="n">subset</span><span class="bp">.</span><span class="n">refl</span><span class="o">])</span>
  <span class="k">begin</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">compl_subset_comm</span><span class="o">,</span> <span class="n">subset_interior_iff_subset_of_open</span><span class="o">,</span> <span class="n">compl_subset_comm</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">subset_closure</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">is_open_compl_iff</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">is_closed_closure</span>
  <span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">interior_compl</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">-</span><span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">closure</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">-</span> <span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span> <span class="bp">-</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">-</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">closure</span> <span class="o">(</span><span class="bp">-</span> <span class="o">(</span><span class="bp">-</span> <span class="n">s</span><span class="o">))</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">closure_compl</span><span class="o">]</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">closure</span> <span class="n">s</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Kenny Lau (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135058582):
<p>just like a sandwich</p>

#### [ Johannes Hölzl (Oct 02 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135061762):
<p>gone <a href="https://github.com/leanprover/mathlib/commit/fff12f5889c7cd5a9169b42433eb14f3b53e7614" target="_blank" title="https://github.com/leanprover/mathlib/commit/fff12f5889c7cd5a9169b42433eb14f3b53e7614">https://github.com/leanprover/mathlib/commit/fff12f5889c7cd5a9169b42433eb14f3b53e7614</a></p>

#### [ Kenny Lau (Oct 02 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135061814):
<p>I'm quite surprised they have no dependencies...</p>

#### [ Kevin Buzzard (Oct 03 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135085888):
<p>I guess one could try and use meta magic to search for theorems with two distinct names?</p>

#### [ Patrick Massot (Oct 03 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/closure_compl_eq%20vs%20closure_compl/near/135086020):
<p>In principle this is very easy</p>


{% endraw %}
