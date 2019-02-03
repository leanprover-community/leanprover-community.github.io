---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39810avoidingsubtypeeq.html
---

## Stream: [maths](index.html)
### Topic: [avoiding subtype.eq](39810avoidingsubtypeeq.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 21 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541236):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">eq</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">hab</span> <span class="c1">-- fails</span>
<span class="kn">end</span>
<span class="c1">-- rewrite tactic failed, motive is not type correct</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">eq</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">subst</span> <span class="n">hab</span> <span class="c1">-- fails</span>
<span class="kn">end</span>
<span class="c1">-- subst tactic failed, hypothesis &#39;hab&#39; is not of the form (x = t) or (t = x)</span>
<span class="c1">-- would have worked if hab was a = b</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">eq</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hab</span><span class="o">,</span>
<span class="kn">end</span>
<span class="c1">-- do I have to do it like this?</span>
</pre></div>

#### [ Kevin Buzzard (Aug 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541258):
<p>Is there any way of doing the rewrite without using <code>subtype.eq</code>? i.e. some high-powered tactic? I've had some luck with <code>subst</code> in the past but not here.</p>

#### [ Kevin Buzzard (Aug 21 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541320):
<p>dammit <code>simp</code> works this time :-) It didn't work in my real world example!</p>

#### [ Mario Carneiro (Aug 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541352):
<p><code>by congr'</code></p>

#### [ Patrick Massot (Aug 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541430):
<p>Makes me think: shouldn't <code>lemma subtype.ext</code> be marked as an extensionality lemma?</p>

#### [ Kevin Buzzard (Aug 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541758):
<p>I'm trying to reproduce the problem that <span class="user-mention" data-user-id="120726">@Luca Gerolla</span> has. He had <code>rw</code> failing because of the motive issue, <code>subst</code> failing because the hypothesis wasn't variable=term, and <code>simp</code> timing out. I have <code>simp</code> taking ages:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span>
<span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">X</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">),</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">=</span> <span class="n">X</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">),</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">hab</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>but not timing out yet.</p>

#### [ Kevin Buzzard (Aug 21 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542034):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">f</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">),</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">),</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">hab</span><span class="o">]</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span>
<span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">X</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">),</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">=</span> <span class="n">X</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">),</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">hab</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>For me, the yellow bars take far longer for the <code>f</code> version than the <code>X</code> version. Is that expected? I still haven't got the timeout but I get quite a long pause with the <code>f</code> version.</p>

#### [ Mario Carneiro (Aug 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542095):
<p>use <code>congr'</code></p>

#### [ Kevin Buzzard (Aug 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542434):
<p>fair enough. I used <code>apply congr_arg</code>.</p>

#### [ Luca Gerolla (Aug 21 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542590):
<p>Was the fact that <code>ha</code> and <code>hab</code> were "lost" (i.e. left with _) that caused the deterministic timeout with <code>simp</code>?</p>

#### [ Luca Gerolla (Aug 21 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542609):
<p>Thanks for this, I was completely unaware of the <code>congr</code> tactic - another good learning!</p>

#### [ Kevin Buzzard (Aug 21 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542694):
<p>Luca I've failed to reproduce your timeout in a controlled setting so far and I don't really want to post a 1300 line file :-)</p>

#### [ Kevin Buzzard (Aug 21 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542711):
<p><code>congr</code> unfolds as many layers as it can (i.e. reduces <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">f(g(x))=f(g(y))</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mclose">)</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>=</mo><mi>y</mi></mrow><annotation encoding="application/x-tex">x=y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span> and <code>congr' 1</code> just removes one layer.</p>

#### [ Luca Gerolla (Aug 21 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542761):
<p>I completely understand! :-)</p>

#### [ Luca Gerolla (Aug 21 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542787):
<blockquote>
<p><code>congr</code> unfolds as many layers as it can (i.e. reduces <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">f(g(x))=f(g(y))</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mclose">)</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>=</mo><mi>y</mi></mrow><annotation encoding="application/x-tex">x=y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span> and <code>congr' 1</code> just removes one layer.</p>
</blockquote>
<p>That's quite helpful, probably I should implement <code>congr</code> also in other similar proofs</p>

#### [ Mario Carneiro (Aug 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542860):
<p>also with <code>congr'</code> if at any point a subgoal matches a hypothesis the subgoal will be closed</p>

#### [ Mario Carneiro (Aug 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542875):
<p>hence why <code>a / 2 = b / 2 |- X ⟨(a/2)/(1/2),ha⟩ = X ⟨(b/2)/(1/2),hb⟩</code> is provable by <code>congr'</code></p>

#### [ Patrick Massot (Aug 21 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132543105):
<blockquote>
<p>also with <code>congr'</code> if at any point a subgoal matches a hypothesis the subgoal will be closed</p>
</blockquote>
<p>Good to know. <a href="https://github.com/leanprover/mathlib/pull/270" target="_blank" title="https://github.com/leanprover/mathlib/pull/270">https://github.com/leanprover/mathlib/pull/270</a></p>

#### [ Kevin Buzzard (Aug 21 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132543959):
<p><code>simp</code> is taking far longer than the profiler says. If I write this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">simplify</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">X234</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">3</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">p</span> <span class="o">((</span><span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">3</span><span class="o">)))</span>
<span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">f</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">a</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">3</span><span class="o">),</span><span class="n">ha</span><span class="bp">⟩</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">b</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span><span class="bp">/</span><span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">3</span><span class="o">),</span><span class="n">hb</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hab</span><span class="o">]</span>
</pre></div>


<p>then the profiler says that elaboration takes under 0.5 seconds, but if I change the name of the theorem then I see the orange bars for around 4 seconds (on a reasonable machine). </p>
<p>Possibly unrelated: I'd never seen this sort of thing in the simp trace debugging output before:</p>
<div class="codehilite"><pre><span></span>[simplify] iff: function.injective f
[simplify] eq: function.injective f
[simplify] eq: f
[simplify] eq: function.injective
[simplify.failure] proof stuck at: function.injective f
[simplify.failure] failed to prove: ?x_3 : function.injective f
1. [simplify.failure] fail to instantiate emetas: &#39;function.injective.eq_iff&#39; at
f (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹) _) = f (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹) _)
partially instantiated lemma:
@function.injective.eq_iff {x // p x} ℝ f ?x_3
  (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹)
     (@eq.rec ℝ (a / 2 / (1 / 3)) (λ (val : ℝ), (λ (x : ℝ), p x) val) ha (b / 2 / 3⁻¹)
        (@(λ [c : has_div ℝ] (a a_1 : ℝ) (e_2 : a = a_1) (a_2 a_3 : ℝ) (e_3 : a_2 = a_3),
            @congr ℝ ℝ (@has_div.div ℝ c a) (@has_div.div ℝ c a_1) a_2 a_3
              (@congr_arg ℝ (ℝ → ℝ) a a_1 (@has_div.div ℝ c) e_2)
              e_3)
           (@division_ring_has_div ℝ real.division_ring real.division_ring)
           (a / 2)
           (b / 2)
           hab
           (1 / 3)
           3⁻¹
           (@one_div_eq_inv ℝ real.division_ring 3))))
  (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹)
     (@eq.rec ℝ (b / 2 / (1 / 3)) (λ (val : ℝ), (λ (x : ℝ), p x) val) hb (b / 2 / 3⁻¹)
        (@(λ [c : has_div ℝ] (a a_1 : ℝ) (e_2 : a = a_1) (a_2 a_3 : ℝ) (e_3 : a_2 = a_3),
            @congr ℝ ℝ (@has_div.div ℝ c a) (@has_div.div ℝ c a_1) a_2 a_3
              (@congr_arg ℝ (ℝ → ℝ) a a_1 (@has_div.div ℝ c) e_2)
              e_3)
           (@division_ring_has_div ℝ real.division_ring real.division_ring)
           (b / 2)
           (b / 2)
           (@eq.refl ℝ (b / 2))
           (1 / 3)
           3⁻¹
           (@one_div_eq_inv ℝ real.division_ring 3))))
</pre></div>


{% endraw %}
