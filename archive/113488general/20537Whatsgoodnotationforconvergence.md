---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20537Whatsgoodnotationforconvergence.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [What's good notation for convergence?](https://leanprover-community.github.io/archive/113488general/20537Whatsgoodnotationforconvergence.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jan-David Salchow (Jan 15 2019 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162064):
<p>To avoid introducing constants, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> asked me to change</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- The notion of convergence of sequences in topological spaces. -/</span>
<span class="n">def</span> <span class="n">converges_to</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">limit</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">,</span> <span class="n">limit</span> <span class="err">∈</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">n0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">n0</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="n">n</span><span class="o">)</span> <span class="err">∈</span> <span class="n">U</span>
</pre></div>


<p>(and a similar definition for convergence in metric spaces) into notation.</p>
<p>I'm struggling to find good notation. My first try was</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="n">x</span> <span class="bp">`</span><span class="err">⟶</span><span class="n">t</span><span class="bp">`</span> <span class="n">limit</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">,</span> <span class="n">limit</span> <span class="err">∈</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">n0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">n0</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="n">n</span><span class="o">)</span> <span class="err">∈</span> <span class="n">U</span>
</pre></div>


<p>but this only works for a fixed topological space X. Is there a way to determine the domain for (the sequence) x without using meta programming? Or is the price for using notation that you always have to specify sequence, limit, and domain?</p>

#### [ Johannes Hölzl (Jan 15 2019 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162103):
<p>Uh, no, more like: <code>notation x </code>⟶t<code> limit := tendsto x at_top (nhds limit)</code></p>

#### [ Johannes Hölzl (Jan 15 2019 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162107):
<p>never put a big term on the right of a <code>notation</code></p>

#### [ Johannes Hölzl (Jan 15 2019 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162167):
<p>also the term we want to operate on should be using <code>tendsto</code> and then we have different views on <code>tendsto</code> telling us how to unfold tendsto into a concrete representation.</p>
<div class="codehilite"><pre><span></span><span class="n">tendsto</span> <span class="n">x</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">limit</span><span class="o">)</span> <span class="bp">&lt;-&gt;</span> <span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">,</span> <span class="n">limit</span> <span class="err">∈</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">n0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">n0</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="n">n</span><span class="o">)</span> <span class="err">∈</span> <span class="n">U</span>
</pre></div>

#### [ Jan-David Salchow (Jan 15 2019 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155168674):
<p>I see, that's better :)</p>

#### [ Jan-David Salchow (Jan 15 2019 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155168742):
<p>The difference between equality and iff is a propext, why is it better to state it as an equality?</p>

#### [ Mario Carneiro (Jan 15 2019 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155170227):
<p>usually it's stated as an iff</p>

#### [ Johannes Hölzl (Jan 15 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155173772):
<p>its an iff now ;-)</p>


{% endraw %}
