---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46163congrwithsubsingleton.html
---

## Stream: [general](index.html)
### Topic: [congr with subsingleton](46163congrwithsubsingleton.html)

---


{% raw %}
#### [ Reid Barton (Jun 15 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141922):
<p>Is this a bug in <code>congr</code>?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">subsingleton</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">congr</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">subsingleton</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">congr</span> <span class="c1">-- ok</span>
</pre></div>

#### [ Kenny Lau (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141939):
<p>what is supposed to the state after the first <code>by congr</code>?</p>

#### [ Reid Barton (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141945):
<p>"no goals"</p>

#### [ Kenny Lau (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141948):
<p>oh</p>

#### [ Reid Barton (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141949):
<p>Actually, I made the second example slightly poor.</p>

#### [ Reid Barton (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141956):
<p>Edited now.</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141958):
<p>Not in the sense that I'm not surprised by the result</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142002):
<p><code>congr</code> only gets its subsingleton optimization when it actually applies a function</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142007):
<p>because it simplifies the congruence lemma for <code>f</code></p>

#### [ Mario Carneiro (Jun 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142018):
<p>so if <code>congr_core</code> applies 0 times the optimization never gets a chance</p>

#### [ Reid Barton (Jun 15 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142028):
<p>I see</p>

#### [ Reid Barton (Jun 15 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142047):
<p>I have a more complicated example where <code>congr</code> fails even when there is a function being applied, but I need to minimize it first.</p>

#### [ Reid Barton (Jun 15 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142090):
<p>Is <code>simp</code> supposed to understand subsingletons then? What exactly does it do with them? It can't handle either of these goals</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142125):
<p><code>simp</code> uses <code>congr</code> to enter a term, so it gets subsingleton handling indirectly that way</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142133):
<p>but it won't rewrite <code>x</code> to <code>y</code> if that's what you mean</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142180):
<p>mostly it's helpful for carrying along dependent arguments</p>

#### [ Reid Barton (Jun 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142183):
<p>Oh, so by "it [<code>congr</code>] simplifies the congruence lemma" you don't mean using <code>simp</code>?</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142191):
<p>No, I mean that the congruence lemma that is generated lacks an equality subgoal for any subsingleton arguments</p>

#### [ Reid Barton (Jun 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142196):
<p>is this stuff in C++, in <code>mk_specialized_congr_lemma</code>?</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142203):
<p>yes</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142207):
<p>but you can see the resulting lemma by using the <code>mk_congr_lemma</code> function</p>

#### [ Reid Barton (Jun 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142838):
<p>OK, the reason <code>congr</code> didn't work in my actual code is because I only have a subsingleton instance for a particular value of one of the type arguments, and the generated congruence lemma was too general and didn't specify the value of that type.</p>

#### [ Reid Barton (Jun 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128143036):
<p>(Namely, I have a subsingleton instance for <code>a ⟶ b</code> only when <code>a</code> is the initial object of a category)</p>


{% endraw %}
