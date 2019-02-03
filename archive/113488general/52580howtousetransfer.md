---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52580howtousetransfer.html
---

## Stream: [general](index.html)
### Topic: [how to use transfer](52580howtousetransfer.html)

---


{% raw %}
#### [ Mario Carneiro (Oct 06 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299504):
<p>Okay, here is a mockup use of <code>transfer</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">inductive</span> <span class="n">xnat</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">xnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">xnat</span><span class="bp">.</span><span class="n">zero</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">xnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="mi">0</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">to_xnat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">to_xnat</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">succ</span>

<span class="n">def</span> <span class="n">of_xnat</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_xnat</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">succ</span>

<span class="kn">theorem</span> <span class="n">to_of_xnat</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">to_xnat</span> <span class="o">(</span><span class="n">of_xnat</span> <span class="n">n</span><span class="o">))</span> <span class="bp">=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">to_of_xnat</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">of_to_xnat</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">of_xnat</span> <span class="o">(</span><span class="n">to_xnat</span> <span class="n">n</span><span class="o">))</span> <span class="bp">=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">of_to_xnat</span> <span class="n">n</span><span class="o">)</span>

<span class="n">def</span> <span class="n">rel</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">to_xnat</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">x</span>

<span class="kn">lemma</span> <span class="n">rel_zero</span> <span class="o">:</span> <span class="n">rel</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">rel_succ</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span><span class="o">)</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">exact</span> <span class="n">rfl</span>
<span class="kn">lemma</span> <span class="n">rel_one</span> <span class="o">:</span> <span class="n">rel</span> <span class="mi">1</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">xnat</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="o">[</span><span class="n">exact</span> <span class="n">m</span><span class="o">,</span> <span class="n">exact</span> <span class="n">n_ih</span><span class="bp">.</span><span class="n">succ</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">to_xnat_add</span> <span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">to_xnat</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">to_xnat</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">to_xnat</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">to_xnat_add</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">rel_add</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span><span class="o">)</span> <span class="o">(</span><span class="bp">+</span><span class="o">)</span> <span class="o">(</span><span class="bp">+</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">apply</span> <span class="n">to_xnat_add</span>

<span class="kn">lemma</span> <span class="n">rel_eq</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span> <span class="err">⇒</span> <span class="n">iff</span><span class="o">)</span> <span class="o">(</span><span class="bp">=</span><span class="o">)</span> <span class="o">(</span><span class="bp">=</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">exact</span>
<span class="bp">⟨λ</span> <span class="n">e</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">of_to_xnat</span><span class="o">]</span> <span class="kn">using</span> <span class="n">congr_arg</span> <span class="n">of_xnat</span> <span class="n">e</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="bp">_⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">relator</span><span class="bp">.</span><span class="n">bi_total</span> <span class="n">rel</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">to_of_xnat</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">,</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">transfer</span><span class="bp">.</span><span class="n">transfer</span> <span class="o">[</span><span class="bp">``</span><span class="n">relator</span><span class="bp">.</span><span class="n">rel_forall_of_total</span><span class="o">,</span> <span class="bp">``</span><span class="n">rel_eq</span><span class="o">,</span> <span class="bp">``</span><span class="n">rel_add</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Olson (Oct 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299649):
<p>Coincidentally I was playing with some proofs recently where I wished I had automatic transport. I'm playing with (regular) languages, and I've manually proven language equivalences like <code>L₁ ≃ L₃ → L₂ ≃ L₄ → L₁ ∪ L₂ ≃ L₃ ∪ L₄</code> which feel a lot like the <code>A ≃ B → P A ≃ P B</code> univalent transport</p>

#### [ Johan Commelin (Oct 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299658):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks a lot for this mock-up! Do you mind if I post my thoughts about it?</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299697):
<p>of course, that's the idea</p>

#### [ Scott Olson (Oct 06 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299698):
<p>I wonder if <code>transfer</code> would apply here? It might run intro trouble because these is an equivalence of functions, and <code>funext</code>-as-a-theorem would still be something cubical types have and Lean doesn't, but I haven't thought this through</p>

#### [ Johan Commelin (Oct 06 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299700):
<p>Should we take it to a different thread?</p>

#### [ Johan Commelin (Oct 06 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299706):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> wrote a mockup use of <code>transfer</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">inductive</span> <span class="n">xnat</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">xnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">xnat</span><span class="bp">.</span><span class="n">zero</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">xnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="mi">0</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">to_xnat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">to_xnat</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">succ</span>

<span class="n">def</span> <span class="n">of_xnat</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_xnat</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">succ</span>

<span class="kn">theorem</span> <span class="n">to_of_xnat</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">to_xnat</span> <span class="o">(</span><span class="n">of_xnat</span> <span class="n">n</span><span class="o">))</span> <span class="bp">=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">to_of_xnat</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">of_to_xnat</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">of_xnat</span> <span class="o">(</span><span class="n">to_xnat</span> <span class="n">n</span><span class="o">))</span> <span class="bp">=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">of_to_xnat</span> <span class="n">n</span><span class="o">)</span>

<span class="n">def</span> <span class="n">rel</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">to_xnat</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">x</span>

<span class="kn">lemma</span> <span class="n">rel_zero</span> <span class="o">:</span> <span class="n">rel</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">rel_succ</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span><span class="o">)</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">exact</span> <span class="n">rfl</span>
<span class="kn">lemma</span> <span class="n">rel_one</span> <span class="o">:</span> <span class="n">rel</span> <span class="mi">1</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">xnat</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="o">[</span><span class="n">exact</span> <span class="n">m</span><span class="o">,</span> <span class="n">exact</span> <span class="n">n_ih</span><span class="bp">.</span><span class="n">succ</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">to_xnat_add</span> <span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">to_xnat</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">to_xnat</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">to_xnat</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">to_xnat_add</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">rel_add</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span><span class="o">)</span> <span class="o">(</span><span class="bp">+</span><span class="o">)</span> <span class="o">(</span><span class="bp">+</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">apply</span> <span class="n">to_xnat_add</span>

<span class="kn">lemma</span> <span class="n">rel_eq</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span> <span class="err">⇒</span> <span class="n">iff</span><span class="o">)</span> <span class="o">(</span><span class="bp">=</span><span class="o">)</span> <span class="o">(</span><span class="bp">=</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">exact</span>
<span class="bp">⟨λ</span> <span class="n">e</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">of_to_xnat</span><span class="o">]</span> <span class="kn">using</span> <span class="n">congr_arg</span> <span class="n">of_xnat</span> <span class="n">e</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="bp">_⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">relator</span><span class="bp">.</span><span class="n">bi_total</span> <span class="n">rel</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">to_of_xnat</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">,</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">transfer</span><span class="bp">.</span><span class="n">transfer</span> <span class="o">[</span><span class="bp">``</span><span class="n">relator</span><span class="bp">.</span><span class="n">rel_forall_of_total</span><span class="o">,</span> <span class="bp">``</span><span class="n">rel_eq</span><span class="o">,</span> <span class="bp">``</span><span class="n">rel_add</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Oct 06 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299754):
<p>First of all: I think for general applicability I think we need a quick way to construct <code>rel</code> from an `equiv.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299803):
<p>And then I have several conflicting thoughts...</p>

#### [ Johan Commelin (Oct 06 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299809):
<p>One is, given <code>nat</code> and the definition of <code>xnat</code> I would like to just immediately transfer <code>comm_semiring</code> to <code>xnat</code>.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299810):
<p>All the structure and proofs should be transferable using automation.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299853):
<p>On the other hand, one might find oneself in the situation where both sides are already equipped with some structure. In this case both already have a <code>0</code> and a <code>+</code>.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299854):
<p>It is easy to define <code>equiv.rel : A ~= B -&gt; A -&gt; B -&gt; Prop</code></p>

#### [ Johan Commelin (Oct 06 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299861):
<p>Right, I'm collecting things that you find easy to define (-;</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299868):
<p>immediately transferring structures is both more difficult and not necessarily what we want</p>

#### [ Johan Commelin (Oct 06 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299870):
<p>So, suppose that both have a <code>0</code> and <code>+</code> like in your example.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299910):
<p>I would prefer an expedited method for showing that pre-existing structures are compatible with an equiv</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299911):
<p>..oh wait, that's group_iso etc</p>

#### [ Johan Commelin (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299912):
<p>Exactly</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299913):
<p>so problem solved?</p>

#### [ Johan Commelin (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299917):
<p>So we show that <code>to_xnat</code> is an <code>add_monoid</code> iso. And then?</p>

#### [ Johan Commelin (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299921):
<p>Then there should be an easy way to extract those <code>rel</code>-lemmas</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299926):
<p>oh yes, that's a one liner</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299927):
<p>rel for add is literally map_add with some dressing</p>

#### [ Johan Commelin (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299928):
<p>After that, proving that <code>xnat</code> is a <code>comm_monoid</code> should be <code>by transfer</code>.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299930):
<p>Or something like that.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299931):
<p>we could put that in the theorems for group_iso</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299972):
<p>But I am wary about <em>constructing</em> structure using <code>transfer</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299975):
<p>you might use <code>transfer</code> to prove that the addition is commutative, like I showed, but the definitions themselves should stand on their own</p>

#### [ Johan Commelin (Oct 06 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299981):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">rel_zero</span> <span class="o">:</span> <span class="n">rel</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">rel_succ</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span><span class="o">)</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">exact</span> <span class="n">rfl</span>
<span class="kn">lemma</span> <span class="n">rel_one</span> <span class="o">:</span> <span class="n">rel</span> <span class="mi">1</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">rel_add</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span><span class="o">)</span> <span class="o">(</span><span class="bp">+</span><span class="o">)</span> <span class="o">(</span><span class="bp">+</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">apply</span> <span class="n">to_xnat_add</span>

<span class="kn">lemma</span> <span class="n">rel_eq</span> <span class="o">:</span> <span class="o">(</span><span class="n">rel</span> <span class="err">⇒</span> <span class="n">rel</span> <span class="err">⇒</span> <span class="n">iff</span><span class="o">)</span> <span class="o">(</span><span class="bp">=</span><span class="o">)</span> <span class="o">(</span><span class="bp">=</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rintro</span> <span class="n">m</span> <span class="bp">_</span> <span class="bp">⟨⟩</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">⟨⟩;</span> <span class="n">exact</span>
<span class="bp">⟨λ</span> <span class="n">e</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">of_to_xnat</span><span class="o">]</span> <span class="kn">using</span> <span class="n">congr_arg</span> <span class="n">of_xnat</span> <span class="n">e</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="bp">_⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">relator</span><span class="bp">.</span><span class="n">bi_total</span> <span class="n">rel</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">to_of_xnat</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">,</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">transfer</span><span class="bp">.</span><span class="n">transfer</span> <span class="o">[</span><span class="bp">``</span><span class="n">relator</span><span class="bp">.</span><span class="n">rel_forall_of_total</span><span class="o">,</span> <span class="bp">``</span><span class="n">rel_eq</span><span class="o">,</span> <span class="bp">``</span><span class="n">rel_add</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>I would wish that this could all be compressed into 2 or 3 lines.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299983):
<p>I don't think it needs to, it can be done in generality</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300030):
<p>the stuff about applying <code>transfer.transfer</code> is not nice though, it should be easier than that</p>

#### [ Johan Commelin (Oct 06 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300039):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Why are you cautious about <code>transfer</code>ing structure?</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300041):
<p>because it leads to bad definitional reduction</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300044):
<p>there are very few cases when it is the right thing to do</p>

#### [ Johan Commelin (Oct 06 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300094):
<p>Hmmm, maybe I'm sad about that. I would have to see how it turns out in practice...</p>

#### [ Johan Commelin (Oct 06 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300134):
<p>I would wish that if someone inadvertently defined <code>xnat</code>, then we could just say: "Aaah, that's <code>equiv</code> to <code>nat</code>. Bam!!! from now one it is a <code>comm_semiring</code> and you can use all theorems about <code>nat</code> for your <code>xnat</code>."</p>

#### [ Johan Commelin (Oct 06 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300144):
<p>Hmm, I want to use more.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300182):
<p>I want to use that it is not just some random <code>equiv</code>. I want to use that they are structurally equivalent. Is that a thing?</p>

#### [ Johan Commelin (Oct 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300186):
<p>They are the <em>same</em> inductive type.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300187):
<p>But I'm getting distracted, I think.</p>

#### [ Scott Olson (Oct 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300193):
<p>So you're interested in duplicated definitions, not e.g. <code>nat</code> vs. <code>binnat</code>?</p>

#### [ Johan Commelin (Oct 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300234):
<p>Well, not really. Like I said, I was getting distracted.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300239):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Ok, I think I know what I want. I want you to remove every mention of <code>rel</code> in your example.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300240):
<p>That's the key part that makes transfer work</p>

#### [ Johan Commelin (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300241):
<p>In the proof that addition is commutative, I want to invoke <code>big_transfer</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300242):
<p>you could remove everything else</p>

#### [ Johan Commelin (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300243):
<p>And it will ask me for a <code>rel</code></p>

#### [ Johan Commelin (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300279):
<p>And I will answer: use this <code>equiv</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300283):
<p>but it is a logical relations proof, not a rewrite proof</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300287):
<p>That's fine, I think</p>

#### [ Johan Commelin (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300288):
<p>And then it says: Good. But then you need to prove these goals: <code>rel_zero</code>, <code>rel_add</code>.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300289):
<p>the user layer can handle that</p>

#### [ Johan Commelin (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300290):
<p>And it generates those two goals. And I prove them with <code>tidy</code>.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300291):
<p>But the user layer here <em>really</em> needs work</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300297):
<p>there is nothing, it's not even an interactive tactic</p>

#### [ Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300298):
<p>And there you have a 4 line tactic proof of commutativity. And all the other stuff above is gone.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300301):
<p>Aaah...!</p>

#### [ Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300303):
<p>When I asked whether there was a tactic for <code>transfer</code>, you said "Yes". And I immediately assumed it was interactive.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300304):
<p>Lol</p>

#### [ Johan Commelin (Oct 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300343):
<p>For me tactic implies interactive. Silly me.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300344):
<p>In the int.basic example, there is a local redefinition of <code>transfer</code> to get the big list of relevant rel theorems for this particular relation</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300345):
<p>because it is often the case that you will want to use the same relation, or pair of structures, in multiple nearby proofs</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300350):
<p>in <code>int.basic</code> it is of course used for each of the axioms of the ring structure</p>

#### [ Johan Commelin (Oct 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300351):
<p>But, can a tactic automatically infer what it needs to know about a relation, given a certain goal?</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300352):
<p>no, it doesn't even know the target</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300391):
<p>For example in my mockup I have a goal on <code>xnat</code> and I said <code>transfer</code> with no info</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300393):
<p>how would it know that I am transferring to <code>nat</code> instead of something else? and why that relation instead of something else?</p>

#### [ Johan Commelin (Oct 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300401):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">interactive</span><span class="bp">.</span><span class="n">transfer</span> <span class="n">my_equiv</span><span class="bp">.</span><span class="n">to_rel</span><span class="o">,</span>
  <span class="o">{</span> <span class="c1">-- prove rel_zero },</span>
  <span class="o">{</span> <span class="c1">-- prove rel_add }</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Oct 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300403):
<p>Would that be possible?</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300408):
<p>I think we will need to rewrite transfer anyway, I very much doubt the one in core works well enough for our purposes</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300449):
<p>(at least we should copy it to mathlib and give it a nice front end)</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300452):
<p>That would be possible, but like I said you want more reuse than that</p>

#### [ Johan Commelin (Oct 06 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300454):
<p>Cool</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300470):
<p>that might prove your theorem now, but in the very next theorem you will probably want this relation again and you would have to prove <code>rel_zero</code> again</p>

#### [ Johan Commelin (Oct 06 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300471):
<p>Yes, the VScode "Turn this goal into lemma" keyboard-shortcut will take care of the reuse.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300515):
<p>I don't think we have to worry about proof obligations much here</p>

#### [ Johan Commelin (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300516):
<p>It will take everything between a pair of <code>{ .. }</code> and turn it into a proof of the subgoal. It will suggest a name for the lemma. And it will apply that lemma where previously the <code>{ .. }</code> were written.</p>

#### [ Johan Commelin (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300517):
<p>But I'm getting distracted again <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Mario Carneiro (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300518):
<p>it will usually already have all the info it needs to prove these obligations</p>

#### [ Johan Commelin (Oct 06 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300526):
<p>Right.</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300529):
<p>e.g. if you are proving rel_zero and rel_add that means you have a group iso and so you probably assumed it was a group iso, and so these theorems will already be proven</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300570):
<p>The main point behind the <code>rel</code> stuff is to build up relations on bigger things, i.e. kernels and short exact sequences</p>

#### [ Johan Commelin (Oct 06 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300572):
<p>But then <code>interactive.transfer</code> needs to remember that the <code>rel</code> came from an <code>equiv</code>. Then it could use type class search to find those results.</p>

#### [ Johan Commelin (Oct 06 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300573):
<blockquote>
<p>The main point behind the <code>rel</code> stuff is to build up relations on bigger things, i.e. kernels and short exact sequences</p>
</blockquote>
<p>This could all be <code>equiv.to_rel</code>, right?</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300581):
<p>there is nothing to remember, the relation is explicitly <code>equiv.rel e</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300585):
<p>not sure what you mean by that last bit</p>

#### [ Johan Commelin (Oct 06 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300586):
<p>But then transfer will have a hard time finding theorems about <code>e</code>, not?</p>

#### [ Johan Commelin (Oct 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300627):
<p>I meant that to me <code>equiv</code> seems a lot more natural than <code>rel</code>. And usually we will have an <code>equiv</code> floating around. Even for kernels and s.e.s's</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300628):
<p>We will have to think about how to discover/supply rel theorems to transfer. Currently it just accepts a big ugly list of names</p>

#### [ Johan Commelin (Oct 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300630):
<p>Or some <code>Isom</code> in a category. So we will need <code>Isom.rel</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300635):
<p>Note that rel is a <em>lot</em> more general</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300637):
<p>The relation need not be an equiv</p>

#### [ Johan Commelin (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300638):
<p>Yes, I know. I'm not sure if I care</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300639):
<p>Almost all of these theorems hold with much weaker assumptions</p>

#### [ Johan Commelin (Oct 06 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300679):
<p>I suggest that the interactive transfer generates a list of goals.<br>
Then we can prove <code>by transfer my_rel; tidy</code>.</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300684):
<p>I think it will discharge all its goals</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300691):
<p>except the main goal</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300695):
<p>I wonder whether it should deliver its iff statement instead of changing the goal... that way it can apply on hyps too</p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301646):
<p>I was reading <a href="https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf" target="_blank" title="https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf">https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf</a> again and I saw that Isabelle's transfer can do <code>The transfer proof method can replace a universal with an equivalent bounded quantifier:
e.g., (∀n::nat. n &lt; n + 1) is transferred to (∀x::int ∈ {0..}. x &lt; x + 1).</code></p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301653):
<p>This sounds suspiciously like the number casting tactic mentioned in this chat earlier</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301695):
<p>Of course our <code>transfer</code> is based on isabelle's <code>transfer</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301696):
<p>The number casting tactic uses rewrites instead of logical relations</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301698):
<p>Maybe it would be better to use transfer for this ...?</p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301754):
<p>I think <code>transfer</code> in Lean will want this anyway at some point, so the same machinery may as well do double duty...? I'm unsure of what the implications are</p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301795):
<p>I do like that relations are stronger than rewrites</p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301800):
<p>I'm reading some of the follow-on papers and there are some tactics that automatically generate refinement theorems for converting algorithms over finsets to concrete algorithms over data structures like rb-trees etc</p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301801):
<p>using transfer or derivatives of</p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301860):
<p>it appears someone in Coq wanted to port <code>transfer</code> too: <a href="https://arxiv.org/pdf/1505.05028.pdf" target="_blank" title="https://arxiv.org/pdf/1505.05028.pdf">https://arxiv.org/pdf/1505.05028.pdf</a></p>

#### [ Andrew Ashworth (Oct 06 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301861):
<p>example 2 in the coq paper is exactly xnat and nat...</p>

#### [ Johan Commelin (Oct 06 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301901):
<p>The number casting tactic would be transferring data as well, right? Not only proofs...</p>

#### [ Kevin Buzzard (Oct 06 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306619):
<blockquote>
<p>They are the <em>same</em> inductive type.</p>
</blockquote>
<p>I remember when I used to go on about this sort of thing. For computer scientists there is a very precise notion of <em>the same</em> and it's asking a lot more than what we have -- it means they are literally the same object -- structurally equal. Two inductive types with canonically isomorphic definitions are just canonically isomorphic, which is a much weaker notion. For each notion of "the same" (these groups are "the same", these topological spaces are "the same") we have to formalise our notion of sameness (e.g. with an equiv or a beefed-up equiv structure with extra proof such as "...and the maps are also group homomorphisms") and then understand exactly which constructions descend to equivalence classes. "The same" is a fluid concept in mathematics, it is really a bunch of equivalence relations. I discovered in the schemes project that it was very costly to think of the open set <code>U</code> and the open set <code>id'' U</code> (the image of U under the identity map) as "the same", because they really were not <em>the same</em>. They were "equal because of a theorem" and this is a much weaker statement. Stuff like <code>congr_arg</code> and <code>congr_fun</code> work because <code>eq</code> (which is a random inductive type remember, not at all related to whether things are <em>the same</em>) has a good recursor.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306664):
<p>There was a thread a while ago now, possibly on gitter, where I got extremely frustrated about how <code>U</code> and <code>id'' U</code> could even <em>possibly</em> not be <em>the same</em> and it took a lot of talking from Mario and Kenny to peel me off the ceiling. Once I realised that the correct map from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="script">F</mi></mrow><mo>(</mo><mi>U</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathcal{F}(U)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathcal" style="margin-right:0.09931em;">F</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="script">F</mi></mrow><mo>(</mo><mi>i</mi><mi>d</mi><mo>(</mo><mi>U</mi><mo>)</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathcal{F}(id(U))</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathcal" style="margin-right:0.09931em;">F</span></span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mord mathit">d</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span><span class="mclose">)</span></span></span></span> was not <code>id</code> but <code>res</code> all my problems went away.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306746):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mi>d</mi><mo>(</mo><mi>U</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">id(U)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">i</span><span class="mord mathit">d</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span></span></span></span> are canonically isomorphic in the computer-scientist's version of the category of open sets on a topological space, but the moment you start treating them as <em>the same</em> you get a whole bunch of errors about motives not being type correct which Reid did show me how to fight against if necessary. However these techniques turned out not to be needed once I understood that the canonical isomorphisms were not <code>id</code> but <code>res</code>.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306755):
<p>In the mathematician's model of this category, these sets are <em>the same</em>.</p>


{% endraw %}
