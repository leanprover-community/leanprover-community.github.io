---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27708Algebraicclosureroadmap.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Algebraic closure roadmap](https://leanprover-community.github.io/archive/113488general/27708Algebraicclosureroadmap.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 14 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135781672):
<p>I've created a roadmap for constructing an algebraic closure of a field: <a href="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md">https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md</a></p>

#### [ Kenny Lau (Oct 14 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135781674):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Oct 14 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135782970):
<p>I just thought of another approach that is very similar: we can construction the "perfect closure" of a ring of char p &gt; 0, and then for a field F we consider its perfect closure Fp, and then do the big polynomial ring thing to Fp instead, and we obtain the field K, and we prove that K is algebrically closed. This would require transitivity of integrality though.</p>

#### [ Kenny Lau (Oct 14 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135783254):
<p>Never mind, forget this other approach.</p>

#### [ Kenny Lau (Oct 14 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135783607):
<p>Do we even have char p?</p>

#### [ Kenny Lau (Oct 14 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135783619):
<p>lol no we don't have</p>

#### [ Kevin Buzzard (Oct 14 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135786179):
<p>So you prefer this approach to the "now repeat steps 22-27 infinitely often and take the direct limit"? Integral elements form a subring -- you will have to wait a bit for this I guess. The direct limit approach avoids this. I guess Mario already explained why he thinks your approach is better though.</p>

#### [ Kenny Lau (Oct 14 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135787184):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> do you like perfect closure?</p>

#### [ Kenny Lau (Oct 14 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135787223):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">padics</span><span class="bp">.</span><span class="n">padic_norm</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">binomial</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">add_pow_char</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="n">p</span><span class="o">)</span>
  <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span><span class="err">^</span><span class="n">p</span> <span class="bp">=</span> <span class="n">x</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">y</span><span class="err">^</span><span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">add_pow</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_self</span><span class="o">,</span> <span class="n">pow_zero</span><span class="o">,</span> <span class="n">choose_self</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">add_left_inj</span><span class="o">],</span>
  <span class="n">transitivity</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_eq_single</span> <span class="mi">0</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">sorry</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span> <span class="n">exfalso</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H</span><span class="o">,</span> <span class="n">exact</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_range</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hp</span><span class="bp">.</span><span class="n">pos</span> <span class="o">}</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">pow_zero</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_zero</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">,</span> <span class="n">choose_zero_right</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">]</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">frobenius</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">x</span><span class="err">^</span><span class="n">p</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="n">p</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">one_pow</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">mul_pow</span> <span class="n">x</span> <span class="n">y</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="n">add_pow_char</span> <span class="n">hp</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">perfect_closure</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">quotient</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">n</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="err">^</span><span class="o">(</span><span class="n">p</span><span class="err">^</span><span class="o">(</span><span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="bp">+</span><span class="n">n</span><span class="o">))</span> <span class="bp">=</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="err">^</span><span class="o">(</span><span class="n">p</span><span class="err">^</span><span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="bp">+</span><span class="n">n</span><span class="o">)),</span>
<span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">n₁</span><span class="o">,</span> <span class="n">x₁</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">n₂</span><span class="o">,</span> <span class="n">x₂</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">n₃</span><span class="o">,</span> <span class="n">x₃</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">w₁</span><span class="o">,</span> <span class="n">h₁</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">w₂</span><span class="o">,</span> <span class="n">h₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">n₂</span> <span class="bp">+</span> <span class="n">w₁</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">x₁</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₃</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n₂</span> <span class="bp">+</span> <span class="n">w₁</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">))</span>
    <span class="bp">=</span> <span class="o">(</span><span class="n">x₁</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₂</span> <span class="bp">+</span> <span class="n">w₁</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₃</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">))</span> <span class="o">:</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_add</span><span class="o">]</span><span class="bp">;</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">add_assoc</span><span class="o">,</span> <span class="n">add_left_comm</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x₂</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₁</span> <span class="bp">+</span> <span class="n">w₁</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₃</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">))</span> <span class="o">:</span> <span class="k">by</span> <span class="n">dsimp</span> <span class="n">only</span> <span class="n">at</span> <span class="n">h₁</span><span class="bp">;</span> <span class="n">rw</span> <span class="n">h₁</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x₂</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₃</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₁</span> <span class="bp">+</span> <span class="n">w₁</span><span class="o">))</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x₃</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₂</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₁</span> <span class="bp">+</span> <span class="n">w₁</span><span class="o">))</span> <span class="o">:</span> <span class="k">by</span> <span class="n">dsimp</span> <span class="n">only</span> <span class="n">at</span> <span class="n">h₂</span><span class="bp">;</span> <span class="n">rw</span> <span class="n">h₂</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">x₃</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n₁</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n₂</span> <span class="bp">+</span> <span class="n">w₁</span> <span class="bp">+</span> <span class="n">w₂</span><span class="o">))</span> <span class="o">:</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_add</span><span class="o">]</span><span class="bp">;</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">,</span> <span class="n">add_left_comm</span><span class="o">]</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135790417):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> For any field F, according to my approach, I build a big field extension L, and then extract the maximally purely inseparable subfield K, and then use this K to make things work. Here, K turns out to be the perfect closure of F. However, I can define the perfect closure of F constructively as a direct limit of F, as I have typed above. We can do the big field extension on top of the perfect closure of F instead of directly over F. This would increase the complexity of the definition of algebraic closure, but I feel like this approach is better because we can have a computable perfect closure.</p>

#### [ Kenny Lau (Oct 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135790424):
<p>What do you think?</p>

#### [ Kevin Buzzard (Oct 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135790852):
<p>Can you remind me what "the maximally purely inseparable subfield" of a field extension is? I thought maximal separable subextensions behaved well but inseparable extensions behaved less well. But as I told you once before I don't know this stuff at all; I only know what I lecture in Galois theory. I don't need to know about inseparable extensions at all in my work.</p>

#### [ Kenny Lau (Oct 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791109):
<p>Let's call this big operation Big(F). So if F is a field, then Big(F) is an algebraic extension of F. The shortcut way to construct algebraic closure is basically direct limit of Big(...Big(Big(F))...).</p>
<p>The defining property of Big(F) is that <strong>everything in F[X] has a root in Big(F)</strong>.</p>
<p>Now, for the proper way, we still look at Big(F), but we extract the maximal purely inseparable subextension of Big(F) and call it Perf(F). Yes, in general you shouldn't look at the maximal purely inseparable subextension, but for this case it works fine. Now, we prove that <strong>everything in Perf(F)[X] has a root in Big(F)</strong>.</p>
<p>My observation is that this Perf(F) turns out to be the perfect closure of F, and is potentially useful, but unfortunately it's noncomputable here.</p>
<p>My new proposal is that we should define Perf(F) computable as I've defined above, and look at Big(Perf(F)) as the algebraic closure of F instead. I'm saying that this increases complexity but we're using the same property anyway (i.e. <strong>everything in Perf(F)[X] has a root in _</strong>) and if we do this then we have a computable perfect cosure.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791523):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I hope you can understand this and then explain this in a better way. I'm not particularly good at explaining stuff.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791628):
<p>I don't know anything about char p.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791632):
<p>I am still confused about this inseparable sub</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791637):
<p>I don't even know what inseparable means. Does it mean "not separable"?</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791644):
<p>You'll have to send me some links or something. I'm distracted by real life</p>

#### [ Kenny Lau (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791650):
<p>For K/F and x in K, x is "purely inseparable" if x^(p^n) in F for some n.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791698):
<p><a href="https://stacks.math.columbia.edu/tag/09HD" target="_blank" title="https://stacks.math.columbia.edu/tag/09HD">https://stacks.math.columbia.edu/tag/09HD</a></p>

#### [ Kenny Lau (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791700):
<p><a href="https://stacks.math.columbia.edu/tag/046W" target="_blank" title="https://stacks.math.columbia.edu/tag/046W">https://stacks.math.columbia.edu/tag/046W</a></p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791704):
<p>perfect thanks</p>

#### [ Kenny Lau (Oct 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135791719):
<p>right, the second link is about perfect closure</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792161):
<p>Ok I understand what you're doing.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792164):
<p>nice</p>

#### [ Kenny Lau (Oct 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792166):
<p>maybe you should start caring about char p :P</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792176):
<p>Is it true that if L/K is some finite extension of fields and the maximal purely inseparable subextension of L is K again, then L/K is separable? I suspect that this is not true.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792184):
<p>no it isn't true, I think</p>

#### [ Kenny Lau (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792187):
<p>again, I'm not talking about the maximal purely inseparable subextension in general.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792193):
<p>Ok so we have finally isolated the thing which I was worried about.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792198):
<p>(deleted)</p>

#### [ Kenny Lau (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792235):
<p>I'm talking about the perfect closure.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792240):
<p>(deleted)</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792241):
<p>yes sorry, it's max insep sub you can't do, right?</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792242):
<p>by the way your definition of char p is nonstandard, although I'm not sure whether I should care</p>

#### [ Kenny Lau (Oct 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792252):
<p>make up your mind <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> :P</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792256):
<p>you forgot to say that <code>(n : A) != 0</code> for <code>n &lt; p</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792261):
<p>In the case where p is prime and 1 != 0, it's actually equivalent</p>

#### [ Kenny Lau (Oct 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792305):
<p>I know</p>

#### [ Kenny Lau (Oct 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792311):
<blockquote>
<p>yes sorry, it's max insep sub you can't do, right?</p>
</blockquote>
<p>I'll have to ask my friend</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792316):
<p>but we will need a classification theorem about the existence of a characteristic, and I don't think there is any way to make that constructive</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792326):
<p>So we have this abstract (and non-constructive) construction in 22-27 of <a href="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md">https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md</a> which goes from a field F to an algebraic extension L/F with the property that every irred poly in F[X] has a root in L.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792329):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> but if we know the char then we can make it constructive</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792372):
<p>Kenny's observation is that a second way to construct L would be to start with F, then build its perfect closure (which is the direct limit F -&gt; F -&gt; F -&gt; ... where all the maps are x-&gt;x^p)</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792380):
<p>and then apply the non-constructive construction to the perfection instead. Kenny is observing that this "spits out the same L"</p>

#### [ Kenny Lau (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792616):
<blockquote>
<p>yes sorry, it's max insep sub you can't do, right?</p>
</blockquote>
<p>my friend says if K/F is insep then the max insep sub is K/F</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792659):
<p>It's the phrase "the max insep sub" which I'm objecting to. I have no doubt it exists sometimes</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792663):
<p>I'm not objecting, I'm trying to remember what one can and cannot do.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792665):
<p>There's some Keith Conrad notes on this stuff I think.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792666):
<p>ok.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792669):
<p>in general you can find the max sep sub and the max purely insep sub</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792670):
<p>right</p>

#### [ Kenny Lau (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792673):
<p>given K/F, if S(K) is the max sep sub, then [S(K):F] = [K:F]_s</p>

#### [ Kenny Lau (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792678):
<p>(is this an adjunction?)</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792688):
<p>Yes, if you even know the negation of <code>char_zero</code> you can construct a finite characteristic</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792737):
<p>Unfortunately I think a lot of ring theory is hard to do on characteristic almost-zero</p>

#### [ Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792749):
<p>what do you mean by almost-zero</p>

#### [ Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792754):
<blockquote>
<p>Yes, if you even know the negation of <code>char_zero</code> you can construct a finite characteristic</p>
</blockquote>
<p>that's nice</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792826):
<p>I mean in that intuitionistic middle ground between finite and zero characteristic, where you've looked for a while and it looks pretty zero but you can't be sure</p>

#### [ Kenny Lau (Oct 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792833):
<p>I see</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135792878):
<p>I think a lot of arguments can be rephrased to "react to the discovery" that the ring is actually finite characteristic and rearrange the proof, but that's too much work for most mathematicians</p>

#### [ Kenny Lau (Oct 15 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135795521):
<p><a href="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md">https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md</a></p>

#### [ Kenny Lau (Oct 15 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135795522):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> you're the master of finiteness. How would you do 1?</p>

#### [ Kevin Buzzard (Oct 15 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796600):
<p>The maths proof I know goes via observing that this finite group has the property that for all n there are at most n elements of order dividing n (because the poly <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>X</mi><mi>n</mi></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">X^n-1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathrm">1</span></span></span></span> has at most <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span> roots) and cyclic groups are the only finite groups with this property. Morally that's because of the structure theorem for finitely generated modules over a PID ;-)</p>

#### [ Kevin Buzzard (Oct 15 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796725):
<p>What is this discussion doing in #general by the way? How did Chris prove it for Z/pZ? I'm pretty sure he needed it for QR.</p>

#### [ Kenny Lau (Oct 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796739):
<p>oh right, lemme see...</p>

#### [ Kenny Lau (Oct 15 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796907):
<p>ok it's proved in <a href="https://github.com/leanprover/mathlib/blob/master/field_theory/finite.lean#L148-L155" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/field_theory/finite.lean#L148-L155"><code>field_theory/finite.lean</code></a> that the units group of every finite field is cyclic.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796911):
<p>That's not strong enough for you</p>

#### [ Kenny Lau (Oct 15 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796912):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> the same proof can be used to prove that any finite subgroup of the units group of a field is cyclic, so this is not in the maximal generality.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796957):
<p>yes it would not surprise me if the same proof could be made to work</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135796960):
<p>It's great that mathlib is so readable though, isn't it.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797132):
<p>OK super-basic question: I've opened that file in Lean. How do I see the definition of <code>univ.filter</code> painlessly? If I right click on it I get sent to the definition of <code>finset.univ</code></p>

#### [ Bryan Gin-ge Chen (Oct 15 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797137):
<p>finset.filter is what you want, presumably</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797138):
<p>right, but I want to get there painlessly</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797200):
<p>The key result is <code>card_order_of_eq_totient</code> just before the one you linked to</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797253):
<blockquote>
<p>finset.filter is what you want, presumably</p>
</blockquote>
<p><em>doh</em> only just realised that this has nothing to do with filters</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797327):
<p>Maybe the proof of <code>card_order_of_eq_totient</code> works with any finite subgroup of the units of alpha if alpha is any field.</p>

#### [ Kenny Lau (Oct 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797439):
<p>I think it would be best for <span class="user-mention" data-user-id="110044">@Chris Hughes</span> to re-prove this in more generality instead of us speculating what could be done</p>

#### [ Johan Commelin (Oct 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797742):
<blockquote>
<p>I think it would be best for <span class="user-mention" data-user-id="110044">@Chris Hughes</span> to re-prove this in more generality instead of us speculating what could be done</p>
</blockquote>
<p>We all know what is possible. Isn't this admitting defeat that mathlib is write-only code? Only the person that wrote the code can maintain it. That doesn't seem good to me.</p>

#### [ Kenny Lau (Oct 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797744):
<p>wat kunnen we doen</p>

#### [ Johan Commelin (Oct 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797809):
<p>In Engels praten?</p>

#### [ Kenny Lau (Oct 15 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797926):
<p>what can we do</p>

#### [ Johan Commelin (Oct 15 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135797990):
<p>We can think really hard about what we mean with "readable". <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> say they can read mathlib, and I believe them. <span class="user-mention" data-user-id="110031">@Patrick Massot</span> and I complain that we cannot read mathlib, and I hope others believe us. <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> says he cannot read mathlib and he doesn't care (and I believe him). But in the end I think people should be able to maintain other peoples code.<br>
The only other option is to seriously look into how we can clone Mario.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135799250):
<p>I find it very hard to read, and impossible without it being open in Lean in front of me. I could probably struggle through a proof with lean though. The fact that I don't see why readability is important is perhaps a slightly different issue. If readability is important then I still don't really understand why we're not all writing lengthy tactic proofs, which are to be honest still my favourite proofs. But I am in no position to comment because it's the maintainers who know what's best so clearly they should (and do) have the final say -- I shall defer to their judgement on these issues.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135799291):
<p>I guess a related issue is that I encourage undergraduates to write tactic proofs -- however Chris and Kenny made the switch no problem</p>

#### [ Kenny Lau (Oct 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135799712):
<p>It actually surprises me that it took me quite a few hours to type out this document despite knowing the construction from top to bottom</p>

#### [ Kenny Lau (Oct 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135799713):
<p>I guess it's just hard for me to organize my thoughts</p>

#### [ Kenny Lau (Oct 15 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135800612):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">padics</span><span class="bp">.</span><span class="n">padic_norm</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">binomial</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">add_pow_char</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="n">p</span><span class="o">)</span>
  <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span><span class="err">^</span><span class="n">p</span> <span class="bp">=</span> <span class="n">x</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">y</span><span class="err">^</span><span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">add_pow</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_range_succ</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_self</span><span class="o">,</span> <span class="n">pow_zero</span><span class="o">,</span> <span class="n">choose_self</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">add_left_inj</span><span class="o">],</span>
  <span class="n">transitivity</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_eq_single</span> <span class="mi">0</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">sorry</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span> <span class="n">exfalso</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H</span><span class="o">,</span> <span class="n">exact</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_range</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hp</span><span class="bp">.</span><span class="n">pos</span> <span class="o">}</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">pow_zero</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_zero</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">,</span> <span class="n">choose_zero_right</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">]</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">frobenius</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">x</span><span class="err">^</span><span class="n">p</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="n">p</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">one_pow</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">mul_pow</span> <span class="n">x</span> <span class="n">y</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="n">add_pow_char</span> <span class="n">hp</span> <span class="o">}</span>

<span class="kn">inductive</span> <span class="n">perfect_closure</span><span class="bp">.</span><span class="n">r</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">intro</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="n">x</span><span class="o">,</span> <span class="n">perfect_closure</span><span class="bp">.</span><span class="n">r</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="err">^</span><span class="n">p</span><span class="o">)</span>

<span class="n">def</span> <span class="n">perfect_closure</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="n">quot</span> <span class="o">(</span><span class="n">perfect_closure</span><span class="bp">.</span><span class="n">r</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">perfect_closure</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="o">(</span><span class="n">perfect_closure</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">refine</span> <span class="n">quot</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ×</span><span class="n">α</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">:</span><span class="bp">ℕ×</span><span class="n">α</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span>
      <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="err">^</span><span class="n">p</span><span class="err">^</span><span class="n">y</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="err">^</span><span class="n">p</span><span class="err">^</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">))</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">y1</span> <span class="n">y2</span> <span class="n">H</span><span class="o">,</span> <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">n</span> <span class="n">y</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">quot</span><span class="bp">.</span><span class="n">sound</span><span class="o">,</span>
      <span class="n">dsimp</span> <span class="n">only</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_comm</span><span class="o">,</span> <span class="n">pow_mul</span><span class="o">],</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_pow</span><span class="o">],</span>
      <span class="n">constructor</span> <span class="o">},</span>
    <span class="n">intros</span> <span class="n">x1</span> <span class="n">x2</span> <span class="n">H</span><span class="o">,</span> <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">m</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">ext</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">quot</span><span class="bp">.</span><span class="n">sound</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="n">only</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_comm</span><span class="o">,</span> <span class="n">pow_mul</span><span class="o">],</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_pow</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_add</span><span class="o">],</span>
    <span class="n">constructor</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">e</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">e</span><span class="o">,</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">m</span><span class="o">,</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">f</span><span class="o">,</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">g</span><span class="o">,</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">r</span><span class="o">,</span> <span class="n">z</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">add_assoc</span><span class="o">,</span> <span class="n">mul_pow</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_add</span><span class="o">,</span>
      <span class="o">(</span><span class="n">pow_mul</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_comm</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">],</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span> <span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="mi">1</span><span class="o">),</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">e</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">zero_add</span><span class="o">,</span> <span class="n">one_pow</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_zero</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">,</span> <span class="n">pow_one</span><span class="o">]),</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">e</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">add_zero</span><span class="o">,</span> <span class="n">one_pow</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_zero</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">pow_one</span><span class="o">]),</span>
  <span class="n">mul_comm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">e</span> <span class="n">f</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">e</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">m</span><span class="o">,</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">f</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">]))</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">perfect_closure</span>
</pre></div>

#### [ Scott Morrison (Oct 15 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135803490):
<p>I find it very hard to read most of mathlib, and I think we're making a mistake leaving things so unreadable!</p>

#### [ Mario Carneiro (Oct 15 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135803507):
<p>I don't try to read mathlib without lean running</p>

#### [ Mario Carneiro (Oct 15 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135803512):
<p>and I don't think that we can reasonably achieve that level of readability (I don't think it's the direction we are going)</p>

#### [ Mario Carneiro (Oct 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135803562):
<p>Tactic proofs are readable since you can step through all the steps, and term proofs are readable because they have bounded complexity, as long as you can get at the types of things</p>

#### [ Mario Carneiro (Oct 15 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135803615):
<blockquote>
<blockquote>
<p>I think it would be best for <span class="user-mention" data-user-id="110044">@Chris Hughes</span> to re-prove this in more generality instead of us speculating what could be done</p>
</blockquote>
<p>We all know what is possible. Isn't this admitting defeat that mathlib is write-only code? Only the person that wrote the code can maintain it. That doesn't seem good to me.</p>
</blockquote>
<p>I assume the reason Kenny said this is because Chris has the best understanding of the formalization choices and relevant proof approaches, not because he's the only one who can read his proof</p>

#### [ Johan Commelin (Oct 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135806498):
<p>Readable with Lean open is good enough for me. But I can't even read term-mode proofs with Lean open. (Unless I work really really hard, but usually I just give up.)</p>

#### [ Bryan Gin-ge Chen (Oct 15 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135807472):
<p>I have noticed the following trade-off in functionality of the VS code extension. If I hover over some defined variables / hypotheses in a tactic mode proof, often lean just gives me something useless like the definition of <code>exact</code> or <code>rw</code> or <code>intro</code>. Hovering is more reliably useful inside term mode proofs.</p>

#### [ Bryan Gin-ge Chen (Oct 15 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135807534):
<p>It also would be nice if that type info from hovering could be displayed in the infoview window, so that it's not just completely blank when I'm examining a term-mode proof.</p>

#### [ Mario Carneiro (Oct 15 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135807689):
<p>It will actually give you term mode information if it's actually an expr parser in the tactic (such as after <code>exact</code> or in <code>rw</code> brackets)</p>

#### [ Mario Carneiro (Oct 15 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135807692):
<p>but the name parser doesn't give you any information, so <code>intro</code> hovering doesn't work</p>

#### [ Bryan Gin-ge Chen (Oct 15 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135808091):
<p>What do you mean by an "expr parser"? </p>
<p>Sometimes I get useful info in exact, but I find that <a href="/user_uploads/3121/36syMjdcu-ypF40akvYCYOVf/Screenshot-2018-10-15-01.16.27.png" target="_blank" title="Screenshot-2018-10-15-01.16.27.png">more often than not I don't:</a> </p>
<div class="message_inline_image"><a href="/user_uploads/3121/36syMjdcu-ypF40akvYCYOVf/Screenshot-2018-10-15-01.16.27.png" target="_blank" title="more often than not I don't:"><img src="/user_uploads/3121/36syMjdcu-ypF40akvYCYOVf/Screenshot-2018-10-15-01.16.27.png"></a></div><p>The cursor disappeared when I took the screenshot, but it's hovering over the <code>ha</code> near the bottom left corner of the popup.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135809910):
<p>This thread arguably isn't the right place for this conversation -- which I do think is interesting. I think there could be a place for Lean which is comprehensible to humans -- but maybe that's not mathlib. <a href="https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/example_sheet_01/Sht1Q2/S0102.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/example_sheet_01/Sht1Q2/S0102.lean">Here's the answer to some homework</a>. I'm not sure anyone reads Bourbaki either.</p>

#### [ Chris Hughes (Oct 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135826061):
<blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> the same proof can be used to prove that any finite subgroup of the units group of a field is cyclic, so this is not in the maximal generality.</p>
</blockquote>
<p><a href="https://github.com/leanprover/mathlib/pull/423" target="_blank" title="https://github.com/leanprover/mathlib/pull/423">https://github.com/leanprover/mathlib/pull/423</a></p>

#### [ Chris Hughes (Oct 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135826105):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Johan Commelin (Oct 15 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135826327):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Nice! But I think that what Kenny is after is more general. For any arbitrary field <code>K</code> it is true that every finite subgroup of <code>units K</code> is cyclic.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135833000):
<p>Sure but it [subgroup of cyclic is cyclic]'s pretty darn useful!</p>

#### [ Kevin Buzzard (Oct 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135833012):
<p>It's used all the time in 2nd year algebra, which I would imagine Chris is learning now.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135861242):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">frobenius</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">x</span><span class="err">^</span><span class="n">p</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you think I should make this definition at all?</p>

#### [ Mario Carneiro (Oct 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135861271):
<p>Only if you can layer some additional structure on it</p>

#### [ Kenny Lau (Oct 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135861281):
<p>what do you mean?</p>

#### [ Mario Carneiro (Oct 15 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135861357):
<p>like if you define a bundled homomorphism or something</p>

#### [ Kenny Lau (Oct 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135861497):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">perfect_closure</span><span class="bp">.</span><span class="n">r</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">intro</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="n">x</span><span class="o">,</span> <span class="n">perfect_closure</span><span class="bp">.</span><span class="n">r</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135861499):
<p>like this?</p>

#### [ Kenny Lau (Oct 16 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135866443):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">frobenius_mul</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">mul_pow</span> <span class="n">x</span> <span class="n">y</span> <span class="n">p</span>
<span class="kn">theorem</span> <span class="n">frobenius_iterate_mul</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span><span class="err">^</span><span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span><span class="err">^</span><span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span><span class="err">^</span><span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="o">[</span><span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">iterate_zero</span><span class="o">],</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">iterate_succ&#39;</span><span class="o">,</span> <span class="n">frobenius_mul</span><span class="o">,</span> <span class="bp">*</span><span class="o">]]</span>
<span class="kn">theorem</span> <span class="n">frobenius_one</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">one_pow</span> <span class="bp">_</span>
<span class="kn">theorem</span> <span class="n">frobenius_iterate_one</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span><span class="err">^</span><span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="o">[</span><span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">iterate_zero</span><span class="o">],</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">iterate_succ&#39;</span><span class="o">,</span> <span class="n">frobenius_one</span><span class="o">,</span> <span class="bp">*</span><span class="o">]]</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135866446):
<p>what's the right way to achieve maximum generality?</p>

#### [ Johan Commelin (Oct 16 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135869283):
<p>My first personal reaction is that <code>p</code> should be the first parameter.</p>

#### [ Kenny Lau (Oct 16 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135914776):
<p><a href="https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean">https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean</a></p>

#### [ Kenny Lau (Oct 16 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135914788):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how is this? Is it mathlib ready?</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135919893):
<p>It's okay, I have some comments but they would be best put on a PR. But sure, there is no structural problem with having this in mathlib</p>

#### [ Kenny Lau (Oct 17 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/135956262):
<p><a href="https://github.com/leanprover/mathlib/pull/425" target="_blank" title="https://github.com/leanprover/mathlib/pull/425">https://github.com/leanprover/mathlib/pull/425</a></p>

#### [ Chris Hughes (Oct 18 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136062832):
<p>I generalized my theorem to any finite subgroup of an integral domain. What file should it go in since it's no longer particular to finite fields?</p>

#### [ Kenny Lau (Oct 18 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136066001):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Oct 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136066041):
<p>Not sure, what's the most advanced stuff you use?</p>

#### [ Mario Carneiro (Oct 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136066092):
<p>Maybe somewhere in <code>ring_theory</code> basics or something</p>

#### [ Chris Hughes (Oct 18 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136066451):
<p>Polynomials and <code>group_theory.order_of_element</code>.</p>

#### [ Mario Carneiro (Oct 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136066599):
<p>do either of those depend on the other?</p>

#### [ Chris Hughes (Oct 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/136067170):
<p>No.</p>

#### [ Kenny Lau (Nov 05 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146801908):
<p>The first step is merged!</p>

#### [ Kenny Lau (Nov 05 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146801910):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Nov 05 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146802277):
<p>Nice! Algebraic closures are so key to everything. I would like to one day start stating non-trivial facts about p-adic Galois representations, which are representations of the absolute Galois group of a number field -- these things are a key part of the Langlands philosophy. Galois theory and algebraic closures are a key part of this dream. I would imagine that many other theorem provers have Galois theory and algebraic closures and p-adic numbers in some form, but with Lean it sort-of feels like they will all be in the same place at the same time and one could start thinking about these far deeper things once they're there.</p>

#### [ Kenny Lau (Nov 05 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146803609):
<p><a href="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md">https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md</a></p>

#### [ Kenny Lau (Nov 05 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146808711):
<p>and we have perfect closure now! <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Nov 06 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146889094):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I have finished proving hilbert basis theorem</p>

#### [ Kevin Buzzard (Nov 06 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146889213):
<p>nice! Now you can prove that if B is a finitely-generated algebra over a noetherian ring then B is Noetherian</p>

#### [ Johan Commelin (Nov 06 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146889239):
<p>Also... do we already know that <code>int</code> is noetherian <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Kevin Buzzard (Nov 06 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146889310):
<p>One should prove that PID's are Noetherian and that int is a PID I guess</p>

#### [ Kevin Buzzard (Nov 06 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146889320):
<p>Both of these might be in / easy</p>

#### [ Johan Commelin (Nov 06 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146889347):
<p>The latter is in.</p>

#### [ Patrick Massot (Nov 06 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146890579):
<p>It seems like <a href="https://github.com/leanprover-community/mathlib/blob/f7fde9faf98efa91d49e8f699263d72b3c4d5b0f/ring_theory/hilbert_basis.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/f7fde9faf98efa91d49e8f699263d72b3c4d5b0f/ring_theory/hilbert_basis.lean">https://github.com/leanprover-community/mathlib/blob/f7fde9faf98efa91d49e8f699263d72b3c4d5b0f/ring_theory/hilbert_basis.lean</a> begins with lots of lemmas that should be moved to other files</p>

#### [ Patrick Massot (Nov 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146894970):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> could you comment on how you felt that our API to polynomials and modules was behaving during your proof of Hilbert basis?</p>

#### [ Kenny Lau (Nov 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146894976):
<p>eh... can be better</p>

#### [ Patrick Massot (Nov 06 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146895260):
<p>do you have specific ideas?</p>

#### [ Kenny Lau (Nov 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146904524):
<p>Actually there isn't many problems, it's just some missing lemmas.</p>

#### [ Kenny Lau (Nov 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/146904535):
<p>which isn't a big deal at all, because one can just add them in</p>

#### [ Kenny Lau (Nov 09 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147365605):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span> We will have integral closure by tonight</p>

#### [ Johan Commelin (Nov 09 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147366017):
<p>Cool!</p>

#### [ Kevin Buzzard (Nov 09 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147368104):
<p>Shouldn't you be catching up on all the lectures you missed while you were absent from your course? ;-)</p>

#### [ Kenny Lau (Nov 10 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147412357):
<p>I shall continue tomorrow.</p>

#### [ Kenny Lau (Nov 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449421):
<p>We have integral closure now.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449645):
<p>Can you prove that the integers of a number field are a Dedekind domain?</p>

#### [ Kenny Lau (Nov 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449656):
<p>wow you keep pushing me</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449665):
<p>There are a bunch of equivalent definitions</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449709):
<p>The one which would be easiest would be to show that if K is a field of char 0 which is finite-dimensional over Q then the integral closure of Z in this field (the ring of integers) is Noetherian, an integral domain, integrally closed, and that every non-zero prime ideal is maximal.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449719):
<p>The latter follows from the fact that a non-zero ideal contains an integer and hence the quotient of the ring of integers by a non-zero ideal is a finite set, and then observe that a finite integral domain is a field.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449759):
<p>The reason this is of interest is that one of the main theorems in an undergraduate algebraic number theory course is that every non-zero ideal in the integers of a number field factors uniquely into prime ideals</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449765):
<p>however the correct generality in which this theorem should be proved is that it's true for all Dedekind domains</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449774):
<p>Ok here is a more reasonable question: can you prove that the integral closure of the integral closure is the integral closure?</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449777):
<p>I mean if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>⊆</mo><mi>S</mi></mrow><annotation encoding="application/x-tex">R\subseteq S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is the integral closure of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> and then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mrow><mo mathvariant="normal">′</mo><mo mathvariant="normal">′</mo></mrow></msup></mrow><annotation encoding="application/x-tex">R''</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is the integral closure of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo>=</mo><msup><mi>R</mi><mrow><mo mathvariant="normal">′</mo><mo mathvariant="normal">′</mo></mrow></msup></mrow><annotation encoding="application/x-tex">R'=R''</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147449816):
<p>Then you'd know that the ring of integers of a number field is integrally closed in its field of fractions</p>

#### [ Kenny Lau (Nov 10 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147450331):
<p>sure, give me another weekend...</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451036):
<p>I must be honest, I would rather see Gal(Q-bar/Q)...</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451038):
<p>no wait</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451041):
<p>I would rather see all of these things</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451096):
<p>Kenny here is a genuine much harder challenge. I would like to see a continuous group homomorphism from the absolute Galois group of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Q}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.85556em;vertical-align:-0.16667em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><msub><mi>L</mi><mi>n</mi></msub><mo>(</mo><msub><mi mathvariant="double-struck">Z</mi><mi>p</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">GL_n(\mathbb{Z}_p)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span>, unramified outside a finite set <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> of places.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451104):
<p>Everything you are doing is in some sense working up to this; it's a fundamental object in Langlands' philosophy.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451108):
<p>I'm sure Johan would be equally pleased to see this. One motivation for doing it is, just like perfectoid spaces, it is a fundamental object in modern number theory which seems to me to be a million miles from anything in any theorem prover at this point. And it really is not that difficult to do, in some sense. All the things you're doing are important for the definition of this object.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451221):
<p>I think we have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><msub><mi>L</mi><mi>n</mi></msub><mo>(</mo><msub><mi mathvariant="double-struck">Z</mi><mi>p</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">GL_n(\mathbb{Z}_p)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span>, the topology is not hard, and you are working towards the absolute Galois group.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451293):
<p>An even longer term goal would to be to formalise the statement of the conjecture that Toby and I make in <a href="https://arxiv.org/abs/1009.0785" target="_blank" title="https://arxiv.org/abs/1009.0785">https://arxiv.org/abs/1009.0785</a> (conjecture 3.2.1). This is a rigorous statement which one could argue is a formalisation of what part of Langlands' philosophy is.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147451343):
<p>Before this paper, everyone knew that something like 3.2.1 should be true but nobody had stated it precisely, and several people were well aware that more naive guesses as to what the conjecture should be were provably false.</p>

#### [ Kevin Buzzard (Nov 11 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147452506):
<p>This thread should be in #maths, by the way. Is it possible to change it?</p>

#### [ Kevin Buzzard (Nov 11 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147452517):
<p>Kenny, here's another reasonable suggestion: <a href="https://en.wikipedia.org/wiki/Going_up_and_going_down" target="_blank" title="https://en.wikipedia.org/wiki/Going_up_and_going_down">https://en.wikipedia.org/wiki/Going_up_and_going_down</a> . I have Bruns-Herzog in my office if you need a copy.</p>

#### [ Kevin Buzzard (Nov 11 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147452559):
<p>This is the correct way to prove that non-zero prime ideals are maximal in the integers of a number field.</p>

#### [ Kevin Buzzard (Nov 11 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147452566):
<p>And Matsumura</p>

#### [ Kenny Lau (Nov 11 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic%20closure%20roadmap/near/147479317):
<blockquote>
<p>I mean if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>⊆</mo><mi>S</mi></mrow><annotation encoding="application/x-tex">R\subseteq S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is the integral closure of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> and then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mrow><mo mathvariant="normal">′</mo><mo mathvariant="normal">′</mo></mrow></msup></mrow><annotation encoding="application/x-tex">R''</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is the integral closure of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo>=</mo><msup><mi>R</mi><mrow><mo mathvariant="normal">′</mo><mo mathvariant="normal">′</mo></mrow></msup></mrow><annotation encoding="application/x-tex">R'=R''</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span> done</p>


{% endraw %}
