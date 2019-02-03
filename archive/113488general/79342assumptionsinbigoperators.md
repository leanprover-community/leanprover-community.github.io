---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79342assumptionsinbigoperators.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [assumptions in big_operators](https://leanprover-community.github.io/archive/113488general/79342assumptionsinbigoperators.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 02 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135034421):
<p>I was browsing through big_operators and found:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_nat_cast</span>
<span class="c1">-- gives</span>
<span class="kn">theorem</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_nat_cast</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="err">↑</span><span class="o">(</span><span class="n">sum</span> <span class="n">s</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="err">↑</span><span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">sum_hom</span> <span class="n">coe</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">)</span>
</pre></div>


<p>Is this bad? I assume <code>[_inst_1 : comm_monoid β] [_inst_2 : add_comm_monoid β]</code> is not intended.</p>

#### [ Kevin Buzzard (Oct 02 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035071):
<p>How does Lean know that the up-arrows mean "coerce to beta"?</p>

#### [ Johan Commelin (Oct 02 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035165):
<p>I don't know. Probably <code>nat.cast</code></p>

#### [ Chris Hughes (Oct 02 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035363):
<p>Johan just posted the output of <code>#print</code>. In the actual theorem, the type is given explicitly</p>

#### [ Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035637):
<p>Sorry, I could have been clearer about that...</p>

#### [ Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035695):
<p>Is there a way to see if this happens more often in mathlib?</p>

#### [ Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035707):
<p>Chris, you can probably use your tools to figure out if this theorem is actually ever used.</p>

#### [ Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035716):
<p>I predict it isn't. Because otherwise this double instance problem would have been noticed before.</p>

#### [ Patrick Massot (Oct 02 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035754):
<p>I'm not sure. As  I already pointed out, there are theorems with redundant instances in mathlib</p>

#### [ Kevin Buzzard (Oct 02 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035756):
<blockquote>
<p>Johan just posted the output of <code>#print</code>. In the actual theorem, the type is given explicitly</p>
</blockquote>
<p>Oh -- I'm an idiot. Thanks Chris.</p>

#### [ Johan Commelin (Oct 02 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135036066):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> hmmm... can your tools help to discover this? Of course not very automatically. But maybe generate a list of all theorems that assume <code>[blah X]</code> and <code>[add_blah X]</code>. I guess it almost never happens that this is intended.</p>

#### [ Patrick Massot (Oct 02 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135036552):
<p>doing this is in my long TODO list, but it's very low priority</p>

#### [ Chris Hughes (Oct 02 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135036869):
<p>Searching <code>sum_nat_cast</code> in VScode tells me it's used once in <code>probability mass function</code>. It's casting to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span></span></span></span> there, so no problems synthesizing the <code>comm_monoid</code> instance. It is a mistake though and should be changed.</p>


{% endraw %}
