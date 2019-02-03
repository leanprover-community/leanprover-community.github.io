---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96722continuousofconst.html
---

## Stream: [maths](index.html)
### Topic: [continuous_of_const](96722continuousofconst.html)

---


{% raw %}
#### [ Patrick Massot (Dec 17 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152017837):
<p>This is very much related to my question in the <a href="#narrow/stream/113488-general/subject/Empty.20or.20not.20empty/near/152017713" title="#narrow/stream/113488-general/subject/Empty.20or.20not.20empty/near/152017713">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Empty.20or.20not.20empty/near/152017713</a>, but has some (tiny) math content. Can anyone golf the following ridiculous lemma?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_of_const</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">by_cases</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">true</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">rw</span> <span class="k">show</span> <span class="n">f</span> <span class="bp">=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">ext</span> <span class="n">x</span><span class="bp">;</span> <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">continuous_const</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">U</span> <span class="n">Uin</span><span class="o">,</span>
    <span class="n">convert</span> <span class="n">is_open_empty</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_empty_iff_forall_not_mem</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">exfalso</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">trivial</span><span class="bp">⟩</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>@Kenny, can you can rid of axiom of choice here? I don't even know where it crops in.</p>

#### [ Patrick Massot (Dec 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152017862):
<p>Of course you need to import <code>analysis.topology.topological_space</code></p>

#### [ Kenny Lau (Dec 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018202):
<p>I don't think I can do much regarding axiom of choice</p>

#### [ Kenny Lau (Dec 17 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018645):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>

<span class="kn">lemma</span> <span class="n">continuous_of_const</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="n">f</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_cases</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">hs</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">,</span> <span class="n">hs</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_open_empty</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">hs</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">exists_mem_of_ne_empty</span> <span class="n">hs</span> <span class="k">in</span>
    <span class="k">have</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_univ_of_forall</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="k">from</span> <span class="n">h</span> <span class="n">y</span> <span class="n">x</span> <span class="bp">▸</span> <span class="n">hy</span><span class="o">,</span>
    <span class="n">this</span> <span class="bp">▸</span> <span class="n">is_open_univ</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Dec 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018872):
<p>Nice effort, but it doesn't change much (about the same length, same axioms)</p>

#### [ Mario Carneiro (Dec 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018977):
<p>isn't there a lemma that says a constant proposition is open?</p>

#### [ Mario Carneiro (Dec 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018987):
<p><code>is_open_const</code></p>

#### [ Kenny Lau (Dec 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019040):
<p>but this is a different formulation of "constant"</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019054):
<p>right, but it is the one you want here, I think</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019083):
<p>it doesn't avoid LEM (because it's used in the proof) but you can defer the case splitting to it</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019353):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_of_const</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="n">f</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">convert</span> <span class="bp">@</span><span class="n">is_open_const</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span><span class="bp">;</span> <span class="n">exact</span>
  <span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">fa</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">fa</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">fb</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">show</span> <span class="n">f</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="k">from</span> <span class="n">h</span> <span class="n">b</span> <span class="n">a</span> <span class="bp">▸</span> <span class="n">fb</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Dec 17 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019362):
<p>nice</p>

#### [ Patrick Massot (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019456):
<p>I have a long way to go before becoming a true obfuscation master...</p>

#### [ Patrick Massot (Dec 17 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019513):
<p>Thanks anyway!</p>


{% endraw %}
