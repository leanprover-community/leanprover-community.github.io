---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48024simplemmas.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp_lemmas](https://leanprover-community.github.io/archive/113488general/48024simplemmas.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Oct 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135532880):
<p>What is the difference between a 'simp' and a 'congr' below?</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">add_simp</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">add_congr</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">simp_lemmas</span>
</pre></div>

#### [ Edward Ayers (Oct 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135533034):
<p>My guess is that anything of the form <code>lhs = rhs</code> goes in <code>add_congr</code> so <code>simp</code> knows its a congruence relation.</p>
<p>In the C++, I can see that there is a pair of tables for each equivalence relation we have simp lemmas for. One table contains congruences and the other contains simps. So I guess for <code>=</code> and <code>&lt;-&gt;</code> the simps table would be empty? What would be an example of a relation where both the congr and simps table would be occupied?</p>
<p>I remember hearing somewhere that simp can support arbitrary congruence relations.</p>

#### [ Edward Ayers (Oct 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135533129):
<p>I'm interested in expanding on this from <code>simp.md</code> in mathlib's docs.</p>
<blockquote>
<p>### Something that could be added later on:</p>
<p>"Re: documentation. If you mention congruence, you could show off simp's support for congruence relations. If you show reflexivity and transitivity for cong, and have congruence lemmas for +, etc., then you can rewrite with congruences as if they were equations."</p>
</blockquote>

#### [ Edward Ayers (Oct 10 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135533645):
<p>What is on the lhs and rhs for the simp lemma made from this:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">ne_zero</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">units</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span>
<span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Edward Ayers (Oct 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135535720):
<p>Ok now that I've printed out the congruence rules and simp rules for the default set of simp_lemmas I am just confused.</p>

#### [ Edward Ayers (Oct 10 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135536015):
<p>Ah ok, congruence lemmas let you move between different relations:</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">if_simp_congr</span><span class="o">]</span> <span class="bp">#</span><span class="mi">11</span> <span class="o">(</span><span class="err">?</span><span class="n">x_1</span> <span class="bp">↔</span> <span class="err">?</span><span class="n">x_2</span><span class="o">)</span> <span class="o">(</span><span class="err">?</span><span class="n">x_4</span> <span class="bp">=</span> <span class="err">?</span><span class="n">x_6</span><span class="o">)</span> <span class="o">(</span><span class="err">?</span><span class="n">x_5</span> <span class="bp">=</span> <span class="err">?</span><span class="n">x_7</span><span class="o">),</span> <span class="n">ite</span> <span class="err">?</span><span class="n">x_1</span> <span class="err">?</span><span class="n">x_4</span> <span class="err">?</span><span class="n">x_5</span> <span class="bp">=</span> <span class="n">ite</span> <span class="err">?</span><span class="n">x_2</span> <span class="err">?</span><span class="n">x_6</span> <span class="err">?</span><span class="n">x_7</span>
</pre></div>


<p>Whereas simps  don't. I am now curious about whether simp lemmas can be defined for other relations. They have to be transitive and reflexive, but I don't know if it has to be congruent <code>x = y -&gt; f x = f y</code>. Would it be possible to define simp lemmas for  the relation<code>&lt;</code>? What about integer conguence mod n?</p>

#### [ Gabriel Ebner (Oct 10 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135536879):
<p>Simp lemmas and congruence lemmas are very different.  1) They have different variable constraints: for simp lemmas, all variables of the rhs must occur on the lhs.  E.g. <code>g x y = f x</code> is a simp lemma, but <code>f x = g x y</code> is not.  Congruence lemmas on the hand impose a requirement on the hypotheses: e.g. <code>x = y -&gt; f x = f y</code> is a congruence lemma, but <code>x = h x -&gt; f x = f x</code> is not (because the rhs of <code>x = h x</code> is just wrong).</p>

#### [ Gabriel Ebner (Oct 10 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135536979):
<p>2) Their purpose is different.  You use congruence lemmas to specify where to rewrite, and simp lemmas tell you the result of the rewriting.</p>

#### [ Gabriel Ebner (Oct 10 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537089):
<p>Ideally you could use simp to rewrite modulo integer congruence.  As far as I remember there was a technical problem preventing this though.  But there's no fundamental reason why this can't work.</p>

#### [ Gabriel Ebner (Oct 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537137):
<p>I think the most interesting example of a simp relation other than <code>eq</code> is <code>equiv</code> at the moment.  Look at <code>data/equiv.lean</code>.</p>

#### [ Edward Ayers (Oct 10 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537396):
<p>Thanks! As far as I can tell, <code>x = y -&gt; f x = f y</code> is not explicitly in simp_lemmas. simp is assuming the relation is congruent. Is this right?</p>

#### [ Gabriel Ebner (Oct 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537459):
<p>That's a congruence lemma.  And yes, it is generated on-demand using the same tool that powers the <code>congr</code> tactic.</p>

#### [ Edward Ayers (Oct 10 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537491):
<p>So you couldn't do simp with the <code>&lt;</code> relation?</p>

#### [ Gabriel Ebner (Oct 10 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135542107):
<p>No, because 1) <code>&lt;</code> is not reflexive and 2) <code>has_lt.lt</code> is not transitive in general.  I think you can turn <code>nat.le</code> into a simplification relation though.</p>


{% endraw %}
