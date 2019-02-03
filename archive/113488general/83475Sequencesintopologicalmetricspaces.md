---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83475Sequencesintopologicalmetricspaces.html
---

## Stream: [general](index.html)
### Topic: [Sequences in topological/metric spaces](83475Sequencesintopologicalmetricspaces.html)

---


{% raw %}
#### [ Rohan Mitta (Sep 07 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133532026):
<p>Hi, </p>
<p>I'm trying to prove some propositions about complete metric spaces and need to use sequences for them. I can't seem to find any lemmas in topological_space or metric_space to do with sequences, and was wondering if I should be trying to prove my own basic lemmas about sequences or if I missed something. I also wonder if I'm thinking about sequences properly. </p>
<p>For example,  below I wanted to prove that if Y is a subset of a metric space, and y is an element of the closure of Y, then there exists a sequence in Y converging to y. Am I approaching this correctly? </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">metric_space</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">filter</span>

<span class="kn">theorem</span> <span class="n">lim_sequence_of_mem_closure</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∃</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">f</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">Y</span><span class="o">),</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">f</span> <span class="n">filter</span><span class="bp">.</span><span class="n">cofinite</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span>  <span class="o">:=</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">mem_closure_iff_nhds</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">ball_n</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">ball</span> <span class="n">a</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span><span class="bp">/</span><span class="n">n</span><span class="o">),</span>

  <span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">nonempty</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∈</span> <span class="o">(</span><span class="n">ball_n</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="err">∩</span> <span class="n">Y</span><span class="o">},</span>
    <span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
    <span class="n">apply</span> <span class="bp">@</span><span class="n">nonempty_of_exists</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">true</span><span class="o">),</span>
    <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">this</span> <span class="o">(</span><span class="n">ball_n</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">ball_mem_nhds</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">exists_mem_of_ne_empty</span> <span class="n">H2</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">H3</span> <span class="k">with</span> <span class="n">xn</span> <span class="n">Hxn</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">xn</span><span class="o">,</span> <span class="n">Hxn</span><span class="bp">⟩</span> <span class="o">:</span> <span class="err">↥</span><span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">ball_n</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">∩</span> <span class="n">Y</span><span class="o">}),</span>
    <span class="n">trivial</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>

  <span class="k">have</span> <span class="n">sequence</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="o">(</span><span class="n">H1</span> <span class="n">n</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">sequencevals</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">sequence</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">sequencevals</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">sequencevals</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">Y</span><span class="o">,</span>
    <span class="k">show</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">sequence</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="n">Y</span><span class="o">,</span>
    <span class="k">let</span> <span class="n">sequenceprops</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">((</span><span class="n">sequence</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">property</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">sequenceprops</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span>

<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 07 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133532531):
<p>I think we would want to state this over first countable spaces instead of metric spaces. What are you using it for?</p>

#### [ Rohan Mitta (Sep 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533234):
<p>I want to use it to help me show that a complete subspace Y of a metric space X is closed in X</p>

#### [ Rohan Mitta (Sep 07 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533304):
<p>I'm working towards eventually proving Banach's fixed point theorem but am starting with some easier propositions about complete metric spaces</p>

#### [ Patrick Massot (Sep 07 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533540):
<p>I'm pretty sure the first thing is already there</p>

#### [ Patrick Massot (Sep 07 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533838):
<p>but maybe not</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534094):
<blockquote>
<p>complete subspace Y of a metric space X is closed in X</p>
</blockquote>
<p>This has nothing to do with sequences, it generalizes to uniform spaces</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534290):
<p>It's not the same as your statement, but this lemma writes out the definition of complete so that we can say "a complete subspace Y of X"</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">compact_of_totally_bounded_complete</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">ht</span> <span class="o">:</span> <span class="n">totally_bounded</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">hc</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">{</span><span class="n">f</span><span class="o">:</span><span class="n">filter</span> <span class="n">α</span><span class="o">},</span> <span class="n">cauchy</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">principal</span> <span class="n">s</span> <span class="bp">→</span> <span class="bp">∃</span><span class="n">x</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">compact</span> <span class="n">s</span> <span class="o">:=</span>
</pre></div>

#### [ Mario Carneiro (Sep 07 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534555):
<p>This is what I recommend proving:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">is_closed_of_complete</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hc</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">{</span><span class="n">f</span><span class="o">:</span><span class="n">filter</span> <span class="n">α</span><span class="o">},</span> <span class="n">cauchy</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">principal</span> <span class="n">s</span> <span class="bp">→</span> <span class="bp">∃</span><span class="n">x</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">is_closed</span> <span class="n">s</span> <span class="o">:=</span>
</pre></div>

#### [ Rohan Mitta (Sep 07 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534739):
<p>Okay, I see, I'll try that. Thanks!<br>
I've still got somewhat of a problem  because I can't see a way around using sequences for the proof of Banach's fixed point theorem, so I will need to eventually find a good way of dealing with them in order to do that. That can be a task for later at this point though.</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535426):
<p>The banach fixed point theorem looks pretty tied to metric spaces. I'm not sure how you could state it for uniform spaces. One possibility is some kind of well ordered filtration of the elements of the uniformity such that the contraction mapping forward maps each entourage to one that is strictly greater in the well order. That is, you have a antitone map <code>o</code> from entourages to ordinals such that if <code>S</code> is an entourage, then <code>o (map F S) &gt; o S</code></p>

#### [ Patrick Massot (Sep 07 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535501):
<p>Are you trying to help him or scare him?</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535662):
<p>...that said, I think you should just try to prove the regular BFP on metric spaces</p>

#### [ Patrick Massot (Sep 07 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535712):
<p>Is your definition of a complete subspace of a uniform space equivalent to asking the induced uniformity is complete?</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535843):
<p>yes</p>

#### [ Patrick Massot (Sep 07 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535857):
<p>it seems so</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535859):
<p>we will probably want a proof of equivalence, but I'm not sure how hard the statement is</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535895):
<p>I guess <code>complete_space s</code> is a Prop so that should work</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536009):
<p>Then again, we have the theorem <code>complete_space s &lt;-&gt; is_closed s</code> so I guess the latter is a simpler way to write it :)</p>

#### [ Patrick Massot (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536079):
<p>For Rohan, I would say that relevant lemmas as <code>cauchy_vmap</code> in <code>uniform_space.lean</code> and <code>is_closed_iff_nhds</code> in <code>topological_space.lean</code></p>

#### [ Patrick Massot (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536083):
<p>What?</p>

#### [ Patrick Massot (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536086):
<p>Which theorem?</p>

#### [ Mario Carneiro (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536120):
<p>I mean once Rohan proves it</p>

#### [ Patrick Massot (Sep 07 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536128):
<p>ah ok</p>

#### [ Rohan Mitta (Sep 07 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536676):
<p>Thanks so much both of you! I'm going to sleep now but I'll see what I can do on it over the weekend.</p>

#### [ Patrick Massot (Sep 07 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133537576):
<p>is it actually true if the uniform spaces are not separated?</p>

#### [ Patrick Massot (Sep 07 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133537768):
<p>anyway, my wife calls me, so I'll give you my try. Note that the number of <code>@</code> suggests I'm doing it wrong (looks like I'm fighting the interface):</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">[</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">X</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">aux</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">vmap</span> <span class="o">(</span><span class="bp">λ</span>  <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="n">y</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">f</span> <span class="bp">≠</span> <span class="err">⊥</span> <span class="bp">↔</span> <span class="n">f</span> <span class="err">⊓</span> <span class="n">filter</span><span class="bp">.</span><span class="n">principal</span> <span class="n">Y</span> <span class="bp">≠</span> <span class="err">⊥</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">rohan</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">@</span><span class="n">complete_space</span> <span class="n">Y</span> <span class="o">(</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">vmap</span> <span class="o">(</span><span class="bp">λ</span>  <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="n">y</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">u</span><span class="o">))</span> <span class="o">:</span> <span class="n">is_closed</span> <span class="n">Y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">letI</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">Y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">vmap</span> <span class="o">(</span><span class="bp">λ</span>  <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="n">y</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">u</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">is_closed_iff_nhds</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">x</span> <span class="n">ne_bot</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">cauchy_vmap</span> <span class="n">Y</span> <span class="n">X</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span>  <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="n">y</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="n">le_refl</span> <span class="bp">_</span><span class="o">)</span> <span class="n">cauchy_nhds</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">aux</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">specialize</span> <span class="n">this</span> <span class="n">ne_bot</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span> <span class="n">this</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">x&#39;</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Sep 07 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133537887):
<p>I this the aux lemma sounds plausible. The status in the main proof is:</p>
<div class="codehilite"><pre><span></span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">x&#39;</span> <span class="o">:</span> <span class="err">↥</span><span class="n">Y</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">vmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="err">↥</span><span class="n">Y</span><span class="o">),</span> <span class="n">y</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x&#39;</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">Y</span>
</pre></div>


<p>which looks promising, except maybe if things are not separated</p>

#### [ Reid Barton (Sep 07 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133538194):
<p>The book I looked at on uniform spaces had a lot of Hausdorff assumptions which were not always really required, but rather seemed to be used as a device to ward off evil spirits</p>

#### [ Kevin Buzzard (Sep 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133540912):
<p>So Rohan is a mathematics undergraduate and whilst this filter stuff might be a cool way to do it (and I know he's read my filter blog post), I think there is some merit in seeing a proof which is more what mathematics undergraduates are used to. So here are some dumb questions. Is the epsilon-delta definition of a sequence tending to a limit in Lean? I'm assuming the fact that open balls are open and that x is in the closure of Y iff Y intersects every open set containing x. Given all this, it seems to me to be completely feasible to prove the lemma "the way a mathematician proves it".</p>

#### [ Mario Carneiro (Sep 08 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133542300):
<p>There is an epsilon delta definition of continuity in a metric space, but I don't think we've unfolded the definition of a sequence limit</p>

#### [ Mario Carneiro (Sep 08 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133542312):
<p>The sequence limit is provided via the <code>at_top</code> filter on <code>nat</code></p>

#### [ Kevin Buzzard (Sep 08 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563057):
<p><span class="user-mention" data-user-id="120559">@Rohan Mitta</span> why not write down the mathematics proof you want to work in Lean and then see if you can get it to work. You might want to make some auxiliary definitions. I am still a bit unclear about whether the predicate "this sequence (i.e. function nat -&gt; X) tends to this limit in the metric space X" is in Lean. I'm sure there will be some fancy filter version which works for second countable uniform semi-topologies or whatever, but the thing you're thinking about is a common notion in undergraduate mathematics and in my mind that is justifiction enough for it to be its own special predicate. I guess you could define it for topological spaces using open sets, and then prove that for metric spaces it's equivalent to the epsilon delta definition. This all sounds like very reasonable stuff to dump into an M2PM5 directory on the UROP repo (or the topology directory).</p>

#### [ Reid Barton (Sep 08 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563487):
<p>I don't think we have the epsilon-N description of convergent sequences. For continuous functions we do have the epsilon-delta description, see <code>continuous_of_metric</code> and adjacent theorems.</p>

#### [ Patrick Massot (Sep 08 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563488):
<p>We should definitely have this. I'll need it for teaching.</p>

#### [ Patrick Massot (Sep 08 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563493):
<p>But it should be very easy to define</p>

#### [ Patrick Massot (Sep 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133564349):
<p>It's lunch time, so I can't golf the second half:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">open</span> <span class="n">filter</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">u</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span>
  <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">N</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">u</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">mem_map</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">H</span> <span class="o">(</span><span class="n">ball_mem_nhds</span> <span class="bp">_</span> <span class="n">εpos</span><span class="o">),</span>
 <span class="bp">λ</span> <span class="n">H</span> <span class="n">s</span> <span class="n">s_nhd</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">mem_map</span><span class="o">,</span> <span class="n">mem_at_top_sets</span><span class="o">],</span>
    <span class="n">rcases</span> <span class="n">mem_nhds_iff_metric</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s_nhd</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">sub</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">N</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">n</span> <span class="n">nN</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">sub</span> <span class="o">(</span><span class="n">mem_ball</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">H</span> <span class="n">nN</span><span class="o">)</span>
  <span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Patrick Massot (Sep 09 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621575):
<p>I'm returning to this thread because I think this should go into mathlib:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">seq_tendsto_iff</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">u</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span>
  <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">N</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">u</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">mem_map</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">H</span> <span class="o">(</span><span class="n">ball_mem_nhds</span> <span class="bp">_</span> <span class="n">εpos</span><span class="o">),</span>
 <span class="bp">λ</span> <span class="n">H</span> <span class="n">s</span> <span class="n">s_nhd</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">sub</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_nhds_iff_metric</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s_nhd</span> <span class="k">in</span>
   <span class="k">let</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span> <span class="k">in</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">nN</span><span class="o">,</span>
   <span class="n">sub</span> <span class="err">$</span> <span class="n">mem_ball</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">H&#39;</span> <span class="n">nN</span><span class="bp">⟩⟩</span>
</pre></div>


<p>Mario, what do you think?</p>

#### [ Patrick Massot (Sep 09 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621588):
<p>For teaching purposes, we could even define a new abbreviation like <code>seq_tendsto u a</code> for <code>tendsto u at_top (nhds a)</code> but maybe this kind of things does not belong to mathlib</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621628):
<p>You can split that into two parts; first state it for an arbitrary filter and then reduce to the <code>nhds</code> filter</p>

#### [ Patrick Massot (Sep 09 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621635):
<p>Too late: I turned it into term mode, so now it's read-only</p>

#### [ Patrick Massot (Sep 09 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621640):
<p>It cannot be modified anymore</p>

#### [ Patrick Massot (Sep 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623215):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">tendsto_nhds_iff</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">u</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span>
  <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">f</span><span class="bp">.</span><span class="n">sets</span><span class="o">,</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">u</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">u</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">ball</span> <span class="n">a</span> <span class="n">ε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">H</span> <span class="err">$</span> <span class="n">ball_mem_nhds</span> <span class="n">a</span> <span class="n">εpos</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">H</span> <span class="n">s</span> <span class="n">s_nhd</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">sub</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_nhds_iff_metric</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s_nhd</span> <span class="k">in</span>
   <span class="k">let</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">N_in</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩⟩</span> <span class="o">:=</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span> <span class="k">in</span> <span class="n">f</span><span class="bp">.</span><span class="n">sets_of_superset</span> <span class="n">N_in</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">b_in</span><span class="o">,</span> <span class="n">sub</span> <span class="err">$</span> <span class="n">H&#39;</span> <span class="n">b_in</span><span class="o">)</span><span class="bp">⟩</span>
</pre></div>

#### [ Patrick Massot (Sep 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623218):
<p>Obfuscating is so fun</p>

#### [ Patrick Massot (Sep 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623220):
<p>I understand how one could get addicted to it</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623281):
<p>you missed a spot - <code>⟨N, ⟨N_in, H'⟩⟩</code> could be <code>⟨N, N_in, H'⟩</code></p>

#### [ Patrick Massot (Sep 09 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623299):
<p>Oh you're right, the reader could infer from my version that N_in and H' go together</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623339):
<p>By the way, if this proof was replaced with <code>by finish</code> I would argue it is even more obfuscatory</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623681):
<blockquote>
<p>∀ ε &gt; 0, ∃ (N : ℕ), ∀ {n}, n ≥ N → dist (u n) a &lt; ε</p>
</blockquote>
<p>Aah, it's just like the old days</p>

#### [ Patrick Massot (Sep 09 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623752):
<p>The things we do for our students...</p>

#### [ Patrick Massot (Sep 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624326):
<p>Mario, how would you call</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">t</span> <span class="o">[</span><span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">semilattice_sup</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">s</span> <span class="err">∈</span> <span class="o">(</span><span class="n">at_top</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">),</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">n</span><span class="o">)</span> <span class="bp">↔</span>
<span class="o">(</span><span class="bp">∃</span> <span class="n">N</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">N</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>


<p>And do you have a one line long proof? It's meant to be a variation on <code>mem_at_top_sets</code> but deducing it is surprisingly painful here</p>

#### [ Patrick Massot (Sep 09 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624432):
<p>My proof is</p>
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">mem_at_top_sets</span><span class="o">,</span> <span class="n">exists_prop</span><span class="o">],</span>
  <span class="n">split</span> <span class="bp">;</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rcases</span> <span class="n">h</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h&#39;</span><span class="bp">⟩⟩</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">b</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">n</span> <span class="n">nb</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">h&#39;</span> <span class="bp">_</span> <span class="o">(</span><span class="n">h</span> <span class="n">n</span> <span class="n">nb</span><span class="o">)</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rcases</span> <span class="n">h</span> <span class="k">with</span>  <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="n">h&#39;</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">a</span> <span class="bp">≥</span> <span class="n">N</span> <span class="o">},</span>
    <span class="n">exact</span> <span class="bp">⟨⟨</span><span class="n">N</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h&#39;</span><span class="bp">⟩</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 09 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624586):
<p>I don't think there is a one line proof, although both conditions are equivalent to <code>{n | p n} ∈ at_top.sets</code></p>

#### [ Mario Carneiro (Sep 09 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624645):
<p>wait, isn't the proof <code>rfl</code>?</p>

#### [ Patrick Massot (Sep 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624657):
<p>No</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624661):
<p>I mean</p>
<div class="codehilite"><pre><span></span>lemma t [inhabited α] [semilattice_sup α] {p : α → Prop} :
  {n | p n} ∈ at_top.sets ↔ (∃ N : α, ∀ n, n ≥ N → p n) := iff.rfl
</pre></div>

#### [ Patrick Massot (Sep 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624704):
<p>I need to go sleeping but <span class="user-mention" data-user-id="120559">@Rohan Mitta</span> you can use <a href="https://gist.github.com/PatrickMassot/1b2d39011855ba43f3bf00c08051ad9e" target="_blank" title="https://gist.github.com/PatrickMassot/1b2d39011855ba43f3bf00c08051ad9e">https://gist.github.com/PatrickMassot/1b2d39011855ba43f3bf00c08051ad9e</a> if you want to play with sequences in metric spaces. The lemma at bottom bridges the gap between what you see in lectures and mathlib context</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624711):
<p>oh, this is just <code>mem_at_top_sets</code></p>

#### [ Patrick Massot (Sep 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624715):
<p>yes</p>

#### [ Patrick Massot (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624758):
<p>the last bit you wrote is mem_at_top_sets</p>

#### [ Patrick Massot (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624763):
<p>The question is: how to deduce my <code>t</code> lemma from this</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624764):
<p>The fact <code>(∃ (s : set α) (H : s ∈ F.sets), ∀ n, n ∈ s → p n) ↔ {n | p n} ∈ F.sets</code> is true in any filter</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624769):
<p>it's just saying that a filter is upward closed</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624790):
<p>frankly I'd avoid it simply because the lhs is needlessly verbose</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624832):
<p>just use <code>upward_sets</code> if it looks like the hypotheses of the lhs are about to appear</p>

#### [ Patrick Massot (Sep 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624839):
<p>See the link above: the goal of this lemma is to allow the last proof to be so short</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624891):
<p>I would state the previous theorem differently:</p>
<div class="codehilite"><pre><span></span>lemma tendsto_nhds_iff (u : β → α) (f : filter β) (a : α) : tendsto u f (nhds a) ↔
  ∀ ε &gt; 0, {n | dist (u n) a &lt; ε} ∈ f.sets := sorry
</pre></div>

#### [ Mario Carneiro (Sep 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624907):
<p>this would be even nicer if we had a quantifier-like notation for <code>{n | p n} ∈ f</code>, but I can live with this</p>

#### [ Rohan Mitta (Sep 13 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133882373):
<p>Is this true? I can see how to go from an arbitrary sequence in a metric space to a filter, but don't see how it is possible in general to get from an arbitrary filter to a sequence. </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">metric_space</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">filter</span>
<span class="n">noncomputable</span> <span class="n">theory</span>

<span class="kn">lemma</span> <span class="n">complete_iff_seq_complete</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">complete_space</span> <span class="n">α</span> <span class="bp">↔</span> <span class="o">(</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">),</span> <span class="n">cauchy</span> <span class="o">(</span><span class="n">filter</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="n">at_top</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">tendsto</span> <span class="n">f</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span> <span class="n">intros</span> <span class="n">H</span> <span class="n">f</span> <span class="n">Hf</span><span class="o">,</span>
    <span class="n">exact</span> <span class="o">(</span><span class="bp">@</span><span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="bp">_</span> <span class="n">Hf</span><span class="o">),</span>
  <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Sep 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133884917):
<p>You can get a sequence by for each n taking ε = 1/n and then applying the Cauchy property to the entourage of points at distance less than ε, and picking a point from the set you get out. <code>cauchy_of_metric</code> does some of this work for you</p>

#### [ Reid Barton (Sep 13 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133885019):
<p>I haven't checked but I expect this this defines a Cauchy sequence which you can then use to show the original filter converges.</p>


{% endraw %}
