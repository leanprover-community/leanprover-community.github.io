---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56118newisgrouphom.html
---

## Stream: [maths](index.html)
### Topic: [new is_group_hom](56118newisgrouphom.html)

---


{% raw %}
#### [ Patrick Massot (Apr 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152694):
<p>Recently <code>is_group_hom</code> became a class. Previously we had </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_group_anti_hom</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">f</span> <span class="n">a</span>

<span class="kn">namespace</span> <span class="n">is_group_anti_hom</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">is_group_anti_hom</span> <span class="n">f</span><span class="o">)</span>
<span class="n">include</span> <span class="n">H</span>

<span class="kn">theorem</span> <span class="n">inv</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span><span class="bp">⁻¹</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>and I could then write</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span>
<span class="n">def</span> <span class="n">conj</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">a</span><span class="bp">*</span><span class="n">b</span><span class="bp">*</span><span class="n">a</span><span class="bp">⁻¹</span>

<span class="kn">lemma</span> <span class="n">inv_conj</span> <span class="o">:</span> <span class="o">(</span><span class="n">conj</span> <span class="n">b</span> <span class="n">a</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="n">conj</span> <span class="n">b</span> <span class="o">(</span><span class="n">a</span><span class="bp">⁻¹</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">conj_is_mph</span><span class="bp">.</span><span class="n">inv</span> <span class="n">a</span>
</pre></div>


<p>Is there such a compact way to write the proof of inv_conj with the new <code>is_group_hom</code>? I'm not talking about the LHS/RHS switch. I'm talking about the ability to use projection notation instead of writing <code>(is_group_hom.inv (conj b) a).symm</code></p>

#### [ Kenny Lau (Apr 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152701):
<p>I already complained about this :P</p>

#### [ Patrick Massot (Apr 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152704):
<p>I'm not really complaining</p>

#### [ Kenny Lau (Apr 16 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152712):
<p>right, but the answer is still you can't use projection</p>

#### [ Patrick Massot (Apr 16 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152719):
<p>I slightly prefer the old way in this case but I'm open to learning about advantages of the new way</p>

#### [ Kenny Lau (Apr 16 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152841):
<blockquote>
<p>Now you do <code>is_group_hom.one f</code> I think</p>
</blockquote>
<p><span class="emoji emoji-261d" title="point up">:point_up:</span> <a href="#narrow/stream/113488-general/subject/is_group_hom.2Emul/near/124970169" title="#narrow/stream/113488-general/subject/is_group_hom.2Emul/near/124970169">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/is_group_hom.2Emul/near/124970169</a></p>

#### [ Mario Carneiro (Apr 16 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152927):
<p>You should be using <code>inv_conj</code> in your proofs anyways, so this is a one-time cost</p>

#### [ Kenny Lau (Apr 16 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152943):
<p>but what is <code>conj_is_mph</code>?</p>

#### [ Patrick Massot (Apr 16 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152945):
<p>Hm, I didn't realize it was almost exactly the same question (I was vaguely aware of Kenny asking something about this change but didn't check)</p>

#### [ Mario Carneiro (Apr 16 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152946):
<p>also you should probably swap <code>inv_conj</code> for the same reason <code>is_group_hom.inv</code>  was swapped</p>

#### [ Patrick Massot (Apr 16 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153006):
<p>Indeed my only use of this lemma was a <code>rw [&lt;-invconj]</code></p>

#### [ Patrick Massot (Apr 16 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153022):
<p>I'm trying (once more...) to get back to old stuff because I hope I'll have time to resume</p>

#### [ Patrick Massot (Apr 16 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153069):
<p>I tried to work on the pi instance PR. But I failed in the preparatory work</p>

#### [ Patrick Massot (Apr 16 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153077):
<p>I wanted to properly dispatch the content of Johannes' <code>prod_module.lean</code></p>

#### [ Patrick Massot (Apr 16 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153084):
<p>But trying to move stuff always gets Lean to go crazy</p>

#### [ Patrick Massot (Apr 16 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153093):
<p>everything gets frozen in VSCode and I only end up with a broken mathlib</p>

#### [ Patrick Massot (Apr 16 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153141):
<p>Maybe I should PR everything into the <code>prod_module</code> black-hole and then let you or Johannes decide when this becomes a problem</p>

#### [ Kenny Lau (Apr 16 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153171):
<div class="codehilite"><pre><span></span>import algebra.group

variables {α : Type} [group α] (a b : α)

def conj := a * b * a⁻¹

instance conj.is_group_hom : is_group_hom (conj a) :=
λ x y, by simp [conj, mul_assoc]

lemma inv_conj : conj a (b⁻¹) = (conj a b)⁻¹ :=
is_group_hom.inv (conj a) b
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153213):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> c'est c'que tu veux?</p>

#### [ Patrick Massot (Apr 16 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153251):
<p>I know how to do this (except I went with <code>by finish [is_group_hom, conj]</code> in the instance proof. I was only asking how to properly use the new interface</p>

#### [ Kenny Lau (Apr 16 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153261):
<p>right, which I demonstrated</p>


{% endraw %}
