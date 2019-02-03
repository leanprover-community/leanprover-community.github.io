---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66698opensetsareunionsofbasiselements.html
---

## Stream: [maths](index.html)
### Topic: [open sets are unions of basis elements](66698opensetsareunionsofbasiselements.html)

---


{% raw %}
#### [ Kevin Buzzard (May 13 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495112):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">open</span> <span class="n">topological_space</span>
<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">lemma</span> <span class="n">union_basis_elemnts_of_open</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
<span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">)}</span> <span class="o">(</span><span class="n">HB</span> <span class="o">:</span> <span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">HU</span> <span class="o">:</span> <span class="n">is_open</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∃</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">),</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">Union</span> <span class="n">f</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="err">∈</span> <span class="n">B</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">},</span>
  <span class="n">existsi</span> <span class="n">β</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">f0</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="o">(</span><span class="n">mem_basis_subset_of_mem_open</span> <span class="n">HB</span> <span class="n">U</span> <span class="n">i</span><span class="bp">.</span><span class="n">property</span> <span class="n">HU</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">f0</span> <span class="n">i</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">f1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="err">∈</span> <span class="n">B</span><span class="o">),</span> <span class="o">(</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">f0</span> <span class="n">i</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">g</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">f1</span> <span class="n">i</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">g1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="o">(</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">i</span> <span class="bp">∧</span> <span class="n">f</span> <span class="n">i</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">f1</span> <span class="n">i</span><span class="o">),</span>
  <span class="n">existsi</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm_iff</span><span class="o">,</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">y</span> <span class="n">Hy</span><span class="o">,</span>
      <span class="k">let</span> <span class="n">i</span> <span class="o">:</span> <span class="n">β</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="n">Hy</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">existsi</span> <span class="o">(</span><span class="n">f</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="n">Hy</span><span class="bp">⟩</span><span class="o">),</span>
      <span class="n">constructor</span><span class="o">,</span>
        <span class="n">existsi</span> <span class="n">i</span><span class="o">,</span>
        <span class="n">refl</span><span class="o">,</span>
      <span class="n">exact</span> <span class="o">(</span><span class="n">g1</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
    <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">y</span> <span class="n">Hy</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">Hy</span> <span class="k">with</span> <span class="n">V</span> <span class="n">HV</span><span class="o">,</span><span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">HV</span> <span class="n">Hy</span><span class="o">,</span><span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">i</span> <span class="n">Hi</span><span class="o">,</span>
      <span class="n">apply</span> <span class="o">(</span><span class="n">g1</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="n">rwa</span> <span class="err">←</span><span class="n">Hi</span><span class="o">,</span>
    <span class="o">},</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">g</span> <span class="n">i</span>
  <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495116):
<p>That's the sort of proof I find very easy to write nowadays in tactic mode.</p>

#### [ Kevin Buzzard (May 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495122):
<p>At its heart though is a triviality.</p>

#### [ Kevin Buzzard (May 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495124):
<p><code>mem_basis_subset_of_mem_open</code> says</p>

#### [ Kenny Lau (May 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495167):
<p>you shouldn't use <code>let</code> for propositions (<code>f0</code>, <code>f1</code>, <code>g1</code>)</p>

#### [ Kevin Buzzard (May 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495169):
<p>for every element <code>x</code> of an open set <code>U</code>, there's some basis element <code>V</code> with <code>x \in V</code> and <code>V \sub U</code></p>

#### [ Kevin Buzzard (May 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495172):
<p>So it's one of those things which is in some sense completely trivial</p>

#### [ Kevin Buzzard (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495177):
<p>however because I have to use classical arguments I find writing a one-liner very hard</p>

#### [ Kenny Lau (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495179):
<p>also I don't think you need choice to do that, there's a trick I read somewhere</p>

#### [ Kevin Buzzard (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495180):
<p>So I just write it in tactic mode and I know I'll never get stuck</p>

#### [ Kenny Lau (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495183):
<p>instead of choosing one of them, choose all of them</p>

#### [ Kevin Buzzard (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495184):
<p>Kenny what I care about is whether I should be concerned that I am writing this sort of proof in 30 lines of tactic mode</p>

#### [ Kenny Lau (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495223):
<p>well I say that <code>classical.some</code> doesn't have a good interface</p>

#### [ Kevin Buzzard (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495224):
<p>and whether I should be striving to write a one-liner in term mode.</p>

#### [ Kevin Buzzard (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495225):
<p>Well I say that you are supposed to be sitting my exam at 10am tomorrow morning, so what are you doing chatting here? ;-)</p>

#### [ Kenny Lau (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495227):
<p>proving that determinant is multiplicative (not in Lean)</p>

#### [ Kevin Buzzard (May 13 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495229):
<p>I talked about interface to classical.some recently and Simon wrote <code>ccases</code> and Mario wrote <code>classical.rec_on</code></p>

#### [ Kevin Buzzard (May 13 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495269):
<p>so there are some interfaces if you need them</p>

#### [ Kenny Lau (May 13 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495274):
<p>well you didn't use them</p>

#### [ Kevin Buzzard (May 13 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495276):
<p><a href="#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125696468" title="#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125696468">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125696468</a></p>

#### [ Kevin Buzzard (May 13 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495282):
<p><a href="#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125695647" title="#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125695647">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125695647</a></p>

#### [ Kevin Buzzard (May 13 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495283):
<p>I didn't use them because I have my own interface now -- see f,f1 and g,g1</p>

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495284):
<p>I don't really like it but it was easier to do it like that than find the thread</p>

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495324):
<p>that's not true</p>

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495325):
<p>I didn't use them because I didn't know how to use them in the middle of a function</p>

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495327):
<p>well, I didn't know how to use Simon's, and Mario's is in some sense just as complicated as what I did</p>

#### [ Kevin Buzzard (May 13 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495334):
<p>I was not in a situation where I had <code>exists x, p x</code> and I wanted <code>x</code> and <code>H : p x</code></p>

#### [ Kevin Buzzard (May 13 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495336):
<p>I was in a situation where I wanted to construct a function</p>

#### [ Kevin Buzzard (May 13 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495337):
<p>so I had <code>forall i, exists x, p i x</code></p>

#### [ Kevin Buzzard (May 13 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495383):
<p>and I wanted a map sending i to x</p>

#### [ Kevin Buzzard (May 13 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495384):
<p>hey, maybe I'm just saying that the interface for classical.some isn't great</p>

#### [ Kevin Buzzard (May 13 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495393):
<p>I guess I wanted a map sending i to x and a map sending i to a proof of p i x</p>

#### [ Kevin Buzzard (May 13 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495394):
<p>More precisely, I wanted a map <code>f</code> sending <code>i</code> to <code>x</code> and a map <code>f_proof</code> sending <code>i</code> to a proof of <code>p i (f i)</code></p>

#### [ Kevin Buzzard (May 13 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495433):
<p>(rather than a proof of <code>p i (classical.some _)</code></p>

#### [ Kevin Buzzard (May 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495439):
<p>and it still irks me a bit that I can't use a tactic which just builds these functions for me (with exactly those types, so no classical.some mentioned anywhere in the types, just in the definitions of the terms of these types)</p>

#### [ Kevin Buzzard (May 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495441):
<p>because my constructions of f f1 g and g1 involved building f, copying the type of the some_spec, editing it to replace classical.some _ with f i, then building f1, and this is a purely mechanical procedure.</p>

#### [ Kevin Buzzard (May 13 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495489):
<p>i.e. I started by writing</p>

#### [ Kevin Buzzard (May 13 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495490):
<div class="codehilite"><pre><span></span>  <span class="k">let</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">f0</span> <span class="n">i</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">f1</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">f0</span> <span class="n">i</span><span class="o">),</span>
</pre></div>

#### [ Kevin Buzzard (May 13 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495530):
<p>and then I looked at the type of <code>f1</code> in the context, edited it to remove all trace of <code>classical.some</code> (replacing it with <code>f i</code>) and then inserted the explicit type of <code>f1</code>.</p>

#### [ Kevin Buzzard (May 13 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495531):
<p>It somehow all feels like both a waste of time and something which students would find confusing.</p>

#### [ Kevin Buzzard (May 13 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495536):
<p>Kenny can you write a proof in term mode?</p>

#### [ Mario Carneiro (May 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496195):
<p>You shouldn't be using classical.some in the first place in this proof. It complicates things and there's no need. Before you start optimizing your use don't forget to see if another proof strategy works better by making canonical choices only</p>

#### [ Kevin Buzzard (May 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496206):
<p>I am a classical guy and have no feeling as to when I can get away with constructive maths</p>

#### [ Kevin Buzzard (May 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496259):
<p>I just wrote the first proof I thought of</p>

#### [ Kevin Buzzard (May 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496298):
<p>and I still find this sort of proof a joy to write</p>

#### [ Mario Carneiro (May 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496746):
<p>I would go for the version with a set first:</p>
<div class="codehilite"><pre><span></span>lemma sUnion_basis_elemnts_of_open {α : Type u} [topological_space α]
{B : set (set α)} (HB : is_topological_basis B) {U : set α} (HU : is_open U) :
∃ (S : set (set α)), U = ⋃₀ S ∧ S ⊆ B :=
⟨{b ∈ B | b ⊆ U}, set.ext (λ a,
   ⟨λ ha, let ⟨b, hb, ab, bu⟩ := mem_basis_subset_of_mem_open HB _ ha HU in
              ⟨b, ⟨hb, bu⟩, ab⟩,
    λ ⟨b, ⟨hb, bu⟩, ab⟩, bu ab⟩),
 λ b h, h.1⟩

lemma Union_basis_elemnts_of_open {α : Type u} [topological_space α]
{B : set (set α)} (HB : is_topological_basis B) {U : set α} (HU : is_open U) :
∃ (β : Type u) (f : β → set α), U = (⋃ i, f i) ∧ ∀ i : β, f i ∈ B :=
let ⟨S, su, sb⟩ := sUnion_basis_elemnts_of_open HB HU in
⟨S, subtype.val, su.trans set.sUnion_eq_Union&#39;, λ ⟨b, h⟩, sb h⟩
</pre></div>


<p>(I didn't start out planning to write a term proof, but there never really came a point where I needed a tactic)</p>

#### [ Kevin Buzzard (May 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496845):
<p>Right -- I generally switch to tactic mode when I want to do something like a rw which I'm too lazy to figure out with the funny triangle thing. But here I switched because it just felt easier with the classical.stuff and I felt I'd been beaten too early, that was the reason I asked.</p>

#### [ Kevin Buzzard (May 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496886):
<p>I see the constructivist's trick now -- thanks.</p>

#### [ Kevin Buzzard (May 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496892):
<p>That was the idea I was missing -- I feel confident that I could have generated a term proof now.</p>

#### [ Kevin Buzzard (May 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496936):
<p>PS the mis-spelling of <code>elements</code> in the name was not intentional :-)</p>

#### [ Kevin Buzzard (May 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496941):
<p>I wanted to write "Union_of_basis_elements_of_open" but then I had two different ofs with two different meanings</p>

#### [ Kevin Buzzard (May 13 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496982):
<p>PS1 is this already in mathlib? I couldn't find it. It is the canonical thing you do with a basis!</p>

#### [ Reid Barton (May 13 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126501829):
<blockquote>
<p>I was in a situation where I wanted to construct a function<br>
so I had forall i, exists x, p i x<br>
and I wanted a map sending i to x</p>
</blockquote>
<p>Use <code>classical.axiom_of_choice</code></p>

#### [ Reid Barton (May 13 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126501880):
<div class="codehilite"><pre><span></span><span class="gu">@@ -11,6 +11,3 @@</span>
   let f0 := λ i : β, (mem_basis_subset_of_mem_open HB U i.property HU),
<span class="gd">-  let f := λ i, classical.some (f0 i),</span>
<span class="gd">-  let f1 : ∀ (i : β), ∃ (H : (f i) ∈ B), (i.val ∈ (f i) ∧ (f i) ⊆ U) := λ i, classical.some_spec (f0 i),</span>
<span class="gd">-  let g := λ i, classical.some (f1 i),</span>
<span class="gd">-  let g1 : ∀ (i : β), (i.val ∈ f i ∧ f i ⊆ U) := λ i, classical.some_spec (f1 i),</span>
<span class="gi">+  cases classical.axiom_of_choice f0 with f hf,</span>
   existsi f,
<span class="gu">@@ -25,3 +22,3 @@</span>
         refl,
<span class="gd">-      exact (g1 i).left,</span>
<span class="gi">+      exact (hf i).snd.1</span>
     },
<span class="gu">@@ -29,3 +26,3 @@</span>
       cases Hy with V HV,cases HV with HV Hy,cases HV with i Hi,
<span class="gd">-      apply (g1 i).2,</span>
<span class="gi">+      apply (hf i).snd.2,</span>
       rwa ←Hi,
<span class="gu">@@ -34,3 +31,3 @@</span>
   { intro i,
<span class="gd">-    exact g i</span>
<span class="gi">+    exact (hf i).fst</span>
   }
</pre></div>

#### [ Mario Carneiro (May 13 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126501890):
<p>Oh yes, sorry for not engaging with the original question, Reid is right that you should use <code>axiom_of_choice</code> here</p>


{% endraw %}
