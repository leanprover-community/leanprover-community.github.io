---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10127ChurchNumeralPuzzles.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Church Numeral Puzzles](https://leanprover-community.github.io/archive/116395maths/10127ChurchNumeralPuzzles.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 02 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126010843):
<p>I am trying to understand church numerals by writing a collection of basic theorems about them.</p>

#### [ Kevin Buzzard (May 02 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126010845):
<p>I just solved this one:</p>

#### [ Kevin Buzzard (May 02 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126010886):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span>

<span class="kn">namespace</span> <span class="n">chnat</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">definition</span> <span class="n">to_nat</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">ℕ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="mi">0</span>

<span class="n">def</span> <span class="n">of_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">zero</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="c1">-- f (f^n x)</span>

<span class="kn">definition</span> <span class="n">of_nat&#39;</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">of_nat&#39;</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="c1">-- f^n (f x)</span>

<span class="kn">theorem</span> <span class="n">of_nat_is_of_nat&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">of_nat&#39;</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">chnat</span>
</pre></div>

#### [ Kevin Buzzard (May 02 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126010904):
<p>it was harder than I expected though, so I probably missed a trick, which is why I mention it here.</p>

#### [ Gabriel Ebner (May 02 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126011292):
<p>Hmm, this was a pretty straightforward induction:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">of_nat_is_of_nat&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">of_nat&#39;</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="bp">;</span> <span class="n">funext</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">!</span> <span class="bp">*</span><span class="o">,</span>
<span class="n">clear</span> <span class="n">n_ih</span><span class="o">,</span> <span class="n">induction</span> <span class="n">n</span> <span class="n">generalizing</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">!</span> <span class="bp">*</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 02 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012437):
<p>This is the key lemma I've been after:</p>

#### [ Kevin Buzzard (May 02 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012439):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">of_nat_functorial</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span>
<span class="n">a</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">of_nat</span> <span class="n">n</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span> <span class="n">x&#39;</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x&#39;</span><span class="o">))</span> <span class="n">a</span> <span class="n">x</span> <span class="o">:=</span>
</pre></div>

#### [ Kevin Buzzard (May 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012493):
<p>I have never used <code>generalizing</code> or <code>simp!</code> before.</p>

#### [ Kevin Buzzard (May 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012503):
<p>So thanks very much for these!</p>

#### [ Kevin Buzzard (May 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012504):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span></p>

#### [ Kevin Buzzard (May 02 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012553):
<p>I also have this:</p>

#### [ Kevin Buzzard (May 02 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012554):
<p><code>example (m n : ℕ) : of_nat (m + n) = of_nat m + of_nat n := sorry</code></p>

#### [ Chris Hughes (May 02 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126012995):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">of_nat_functorial</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span>
<span class="n">a</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">of_nat</span> <span class="n">n</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span> <span class="n">x&#39;</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x&#39;</span><span class="o">))</span> <span class="n">a</span> <span class="n">x</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">refl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="k">assume</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">a</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">of_nat</span><span class="o">],</span>
  <span class="n">dsimp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="n">of_nat_functorial</span><span class="o">,</span>
  <span class="n">dsimp</span><span class="o">,</span>
   <span class="n">apply</span> <span class="n">congr_arg</span><span class="o">,</span>
   <span class="n">clear</span> <span class="n">of_nat_functorial</span><span class="o">,</span>
   <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span> <span class="n">generalizing</span> <span class="n">x</span><span class="o">,</span>
   <span class="n">refl</span><span class="o">,</span>
   <span class="n">rw</span> <span class="n">of_nat</span><span class="o">,</span>
   <span class="n">dsimp</span><span class="o">,</span>
   <span class="n">rw</span> <span class="n">ih</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (May 02 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126013010):
<p>Not the cleanest, but done.</p>

#### [ Gabriel Ebner (May 02 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126013555):
<p>These lemmas are all induction+simp, if you set them up correctly:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span><span class="o">:</span> <span class="n">has_add</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">X</span> <span class="n">f</span><span class="o">,</span> <span class="n">a</span> <span class="bp">_</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">b</span> <span class="bp">_</span> <span class="n">f</span><span class="bp">⟩</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">chℕ_add</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span><span class="o">,</span> <span class="n">a</span> <span class="bp">_</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">b</span> <span class="bp">_</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">of_nat_f</span> <span class="o">(</span><span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span> <span class="n">generalizing</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">!</span> <span class="bp">*</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="bp">-</span><span class="n">simp</span><span class="o">]</span> <span class="n">add_comm</span>
<span class="kn">lemma</span> <span class="n">of_nat_add</span>  <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">of_nat</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">of_nat</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">generalizing</span> <span class="n">m</span><span class="bp">;</span> <span class="n">funext</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">of_nat</span><span class="o">,</span> <span class="bp">*</span><span class="o">]</span>
</pre></div>

#### [ Gabriel Ebner (May 02 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126013667):
<p>Unfortunately you can't orient <code>of_nat_f</code> the other way around because it won't work as a simp lemma then.</p>

#### [ Kevin Buzzard (May 02 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126015189):
<p>Thanks so much Gabriel!</p>

#### [ Kevin Buzzard (May 03 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126016767):
<p>These proofs are really cool :-)</p>

#### [ Kevin Buzzard (May 03 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126016801):
<p>I understand better the way you think about the question now. I want to prove all the intermediate lemmas first, because historically I have been trained to go forwards. You just keep reducing the problem to simpler statements by induction because dependent type theory is somehow better at pushing backwards.</p>

#### [ Kevin Buzzard (May 03 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126016926):
<p>The one with <code>clear n_ih</code> is interesting!</p>

#### [ Kevin Buzzard (May 03 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017263):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">pow</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="n">chℕ</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">n</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="o">(</span><span class="n">m</span> <span class="n">X</span> <span class="n">g</span><span class="o">))</span> <span class="n">f</span> <span class="n">x</span>
<span class="kn">theorem</span> <span class="n">of_nat_pow</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">of_nat</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">of_nat</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (May 03 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017321):
<p>I think the proof is <code>of_nat_add _ _</code> :)</p>

#### [ Kevin Buzzard (May 03 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017327):
<p>wait a second</p>

#### [ Kevin Buzzard (May 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017334):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span>

<span class="kn">namespace</span> <span class="n">chnat</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">definition</span> <span class="n">to_nat</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">ℕ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="mi">0</span>

<span class="n">def</span> <span class="n">of_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">zero</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="c1">-- f (f^n x)</span>

<span class="n">def</span> <span class="n">pow</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="n">chℕ</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">n</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="o">(</span><span class="n">m</span> <span class="n">X</span> <span class="n">g</span><span class="o">))</span> <span class="n">f</span> <span class="n">x</span>
<span class="kn">theorem</span> <span class="n">of_nat_pow</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">m</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">pow</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>


<span class="kn">end</span> <span class="n">chnat</span>
</pre></div>

#### [ Kevin Buzzard (May 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017344):
<p>I think that runs and asks the question I want to ask :-)</p>

#### [ Kenny Lau (May 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017350):
<p>I thought I already proved it</p>

#### [ Kevin Buzzard (May 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017353):
<p>Can you golf it though?</p>

#### [ Kenny Lau (May 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017355):
<p>...</p>

#### [ Kevin Buzzard (May 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017360):
<p>Did you see Gabriel's proofs?</p>

#### [ Mario Carneiro (May 03 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017446):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span>

<span class="kn">namespace</span> <span class="n">chnat</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="n">def</span> <span class="n">to_nat</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">m</span> <span class="bp">ℕ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="mi">0</span>

<span class="n">def</span> <span class="n">of_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">zero</span><span class="o">)</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">f</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="c1">-- f (f^n x)</span>

<span class="n">def</span> <span class="n">pow</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">n</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span> <span class="n">X</span><span class="o">)</span> <span class="n">f</span> <span class="n">x</span>

<span class="kn">theorem</span> <span class="n">of_nat_pow</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">m</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">pow</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">end</span> <span class="n">chnat</span>
</pre></div>


<p>golfed</p>

#### [ Kenny Lau (May 03 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017509):
<p>...</p>

#### [ Kevin Buzzard (May 03 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017581):
<p>Mario I guess that in reality I am more interested in the style. Is yours both preferable and golfier? Ultimately I want to write good style Lean.</p>

#### [ Kenny Lau (May 03 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017660):
<p>I wouldn't prefer it</p>

#### [ Kevin Buzzard (May 03 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017666):
<p>ooh the <code>lam g</code> on my part was a rookie error</p>

#### [ Kenny Lau (May 03 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017667):
<p>you see, it uses the equation compiler</p>

#### [ Kenny Lau (May 03 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017674):
<p>and uses "external" definitional equality</p>

#### [ Kenny Lau (May 03 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017718):
<p>like it isn't "expressionally equal" but somehow they made it definitionally equal (by all those ._equation_1) thing</p>

#### [ Kenny Lau (May 03 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017719):
<p>do <code>#print prefix chnat.pow</code> to see what I mean</p>

#### [ Mario Carneiro (May 03 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017740):
<p>huh? There is no fancy business in any of the definitions except <code>of_nat</code>, but that was already defined by eqn compiler</p>

#### [ Kenny Lau (May 03 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017781):
<p>hmm...</p>

#### [ Kenny Lau (May 03 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017791):
<p>they don't do <code>._main</code> if you don't have two cases?</p>

#### [ Mario Carneiro (May 03 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017800):
<p>the eqn compiler always produces <code>._main</code> I guess</p>

#### [ Mario Carneiro (May 03 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017804):
<p>for uniformity I assume</p>

#### [ Kenny Lau (May 03 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017880):
<p>I don't like main</p>

#### [ Kenny Lau (May 03 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017922):
<p>as a sidenote now I prefer <code>trans_rel_left</code> over <code>calc</code> lol</p>

#### [ Kenny Lau (May 03 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017924):
<p>because _ with the tactics</p>

#### [ Kevin Buzzard (May 03 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017938):
<p>Oh you're right Kenny. So Mario does this  mean that the lambda style is preferred in practice?</p>

#### [ Kenny Lau (May 03 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017985):
<p>I think Mario prefers the equation compiler because it looks nicer</p>

#### [ Mario Carneiro (May 03 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017988):
<p>I always locally optimize <code>def T : A -&gt; B := \lam x, t</code> =&gt;  <code>def T (x : A) : B := t</code></p>

#### [ Mario Carneiro (May 03 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126017995):
<p>and <code>def T : B := \lam x, t</code> =&gt; <code>def T : B | x := t</code></p>

#### [ Kenny Lau (May 03 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018003):
<p>what next, <code>\la x, A $ B x</code> =&gt; <code>A \o B</code>?</p>

#### [ Kenny Lau (May 03 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018043):
<p>does your optimization have church rosser?</p>

#### [ Mario Carneiro (May 03 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018044):
<p>that one depends on whether the \o gets in the way later</p>

#### [ Mario Carneiro (May 03 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018045):
<p>but usually yes</p>

#### [ Kenny Lau (May 03 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018048):
<p>even if <code>x</code> is a proposition?</p>

#### [ Mario Carneiro (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018054):
<p>sure, why not?</p>

#### [ Kenny Lau (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018057):
<p>wow</p>

#### [ Kevin Buzzard (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018064):
<p>It's the <code>|</code> that causes the trouble</p>

#### [ Mario Carneiro (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018065):
<p>it often doesn't work as a straight replacement since it could be dependent</p>

#### [ Kevin Buzzard (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018066):
<p>suddenly I have <code>pow._main</code></p>

#### [ Kenny Lau (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018073):
<p>yay we're on the same side for this time</p>

#### [ Mario Carneiro (May 03 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018075):
<p>Yes, the <code>|</code> triggers the equation compiler</p>

#### [ Mario Carneiro (May 03 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018124):
<p>It also gives you the correct (applied) equation lemma</p>

#### [ Mario Carneiro (May 03 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018133):
<p>rather than the lambda equation lemma</p>

#### [ Kenny Lau (May 03 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018134):
<p>I don't like that</p>

#### [ Kevin Buzzard (May 03 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018164):
<p>But Kenny is that just because you haven't learned how to use the more complex type properly?</p>

#### [ Kevin Buzzard (May 03 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018169):
<p>What is an example of where this causes you problems?</p>

#### [ Kenny Lau (May 03 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018171):
<p>heh... I use the equation compiler all the time</p>

#### [ Kenny Lau (May 03 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018172):
<p>I just don't like it</p>

#### [ Kevin Buzzard (May 03 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018175):
<p>and I am asking why exactly</p>

#### [ Kenny Lau (May 03 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018218):
<p>i don't know</p>

#### [ Mario Carneiro (May 03 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018232):
<p>I understand wanting a simple underlying term, but that's an issue best aimed at the equation compiler</p>

#### [ Kevin Buzzard (May 03 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018242):
<p>I am just learning all these tricks now. I have learned that when you write a substantial amount of code you end up picking stuff up as you need it; Kenny you wrote a lot of code a lot quicker than me.</p>

#### [ Kevin Buzzard (May 03 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018247):
<p>Mario, did you do my Ackermann church question? ;-)</p>

#### [ Kenny Lau (May 03 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018250):
<p>I'm convinced you can't do it</p>

#### [ Kenny Lau (May 03 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018252):
<p>you need a higher order functional</p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018256):
<p>since chNat lives in Type 1</p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018295):
<p>you need an empowered chNat that lives in Type 2</p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018296):
<p>Ackermann isn't primitive recursive</p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018297):
<p>its image is in Delta_1 not Delta_0</p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018299):
<p>in the arithmetic hierarchy</p>

#### [ Kevin Buzzard (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018300):
<p><code>def ack : chℕ → chℕ → chℕ := sorry -- KB didn't try this one</code></p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018302):
<p>whatever that means</p>

#### [ Kevin Buzzard (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018303):
<p>(for good reason!)</p>

#### [ Mario Carneiro (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018306):
<p>what ackermann church question</p>

#### [ Kevin Buzzard (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018308):
<p>fill in the def above</p>

#### [ Kenny Lau (May 03 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018309):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> make ackermann using church</p>

#### [ Kevin Buzzard (May 03 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018311):
<p>so that it commutes with usual ack on nat</p>

#### [ Kenny Lau (May 03 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018324):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> or do you already know that one can't do it</p>

#### [ Kevin Buzzard (May 03 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018327):
<p>I don't have a clue</p>

#### [ Mario Carneiro (May 03 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018329):
<p>You can do it</p>

#### [ Kevin Buzzard (May 03 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018330):
<p>I just think this is really cool :-)</p>

#### [ Kevin Buzzard (May 03 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018334):
<p>How do you know you can do it?</p>

#### [ Kenny Lau (May 03 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018375):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I tried to do it and found myself requiring a more complex term in each iteration</p>

#### [ Kenny Lau (May 03 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018379):
<p>you can't iterate on (chN -&gt; chN) either</p>

#### [ Kevin Buzzard (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018387):
<p>When a computer scientist says "you can do it" do they mean "there exists some computer code which does that job" or "it's possible to construct, in polynomial time, some computer code which does that job"</p>

#### [ Kenny Lau (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018390):
<p>the former</p>

#### [ Mario Carneiro (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018391):
<p>I mean there is a solution in less than 50 chars</p>

#### [ Kevin Buzzard (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018393):
<p>:-)</p>

#### [ Kenny Lau (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018394):
<p>??????</p>

#### [ Kenny Lau (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018395):
<p>50 chars....</p>

#### [ Mario Carneiro (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018396):
<p>so just go through all the lambda terms, you'll get it</p>

#### [ Kevin Buzzard (May 03 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018398):
<p>that's not polynomial time though</p>

#### [ Mario Carneiro (May 03 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018438):
<p>heck no</p>

#### [ Kevin Buzzard (May 03 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018448):
<p>Just to be clear, we're talking about the church numeral type without the axiom.</p>

#### [ Kevin Buzzard (May 03 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018459):
<p><code>def chℕ := Π X : Type, (X → X) → X → X</code></p>

#### [ Kenny Lau (May 03 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018461):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> so what is wrong with my analysis?</p>

#### [ Mario Carneiro (May 03 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018467):
<p>Ah, I see what you mean now</p>

#### [ Mario Carneiro (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018518):
<p>In lambda calculus it's untyped so there is no problems</p>

#### [ Kenny Lau (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018519):
<p>exactly</p>

#### [ Mario Carneiro (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018522):
<p>but lean has universe issues</p>

#### [ Kenny Lau (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018523):
<p>we're in typed lamdba calculus</p>

#### [ Kevin Buzzard (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018525):
<p>as opposed to his rather more well-behaved friend <code>chℕfree := {m : Π X : Type, (X → X) → X → X // ∀ (X Y : Type) (a : X → Y) (f : X → X) (x : X),
  m (X → Y) (λ g, g ∘ f) a x = a (m X f x)}</code></p>

#### [ Kevin Buzzard (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018526):
<p>which comes with a free theorem</p>

#### [ Mario Carneiro (May 03 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018530):
<p>you can still do it but you need inductive types, I think</p>

#### [ Kevin Buzzard (May 03 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018540):
<p>oh wait I can do it by cheating!</p>

#### [ Kevin Buzzard (May 03 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018549):
<p>There's a projection from church nat to nat</p>

#### [ Mario Carneiro (May 03 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018550):
<p>exactly</p>

#### [ Mario Carneiro (May 03 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018551):
<p>so you do an induction on <code>nat -&gt; nat</code></p>

#### [ Kenny Lau (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018553):
<p>that's cheating</p>

#### [ Kevin Buzzard (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018567):
<p>so I can define an "incorrect" pow</p>

#### [ Kevin Buzzard (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018594):
<p>But this is cheating</p>

#### [ Kevin Buzzard (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018596):
<p>Is this what they do with pred?</p>

#### [ Mario Carneiro (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018597):
<p>like I said, you need inductive types</p>

#### [ Kenny Lau (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018598):
<p>that's like asking can I define pow by of_nat and to_nat</p>

#### [ Kevin Buzzard (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018600):
<p>If you were to project to nat and then project back with any of add, mul or pow</p>

#### [ Mario Carneiro (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018602):
<p>I think you are right that chN only allows primrec definitions directly</p>

#### [ Kevin Buzzard (May 03 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018605):
<p>you would get a different answer to the "pure" answers which exist</p>

#### [ Kenny Lau (May 03 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018627):
<blockquote>
<p>I mean there is a solution in less than 50 chars</p>
</blockquote>
<p>this wouldn't work. how are you going to check if a given lambda term produces ack?</p>

#### [ Mario Carneiro (May 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018668):
<p>solve the halting problem of course</p>

#### [ Kevin Buzzard (May 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018669):
<p>in the proof I'm envisaging</p>

#### [ Kenny Lau (May 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018675):
<p>you...</p>

#### [ Kevin Buzzard (May 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018677):
<p>:-)</p>

#### [ Kevin Buzzard (May 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018684):
<p>it's going to follow from some cunning unravelling isn't it?</p>

#### [ Mario Carneiro (May 03 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018841):
<p>wait, no I lied again, it is possible</p>

#### [ Kenny Lau (May 03 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018844):
<p>hmm</p>

#### [ Mario Carneiro (May 03 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018846):
<p>the motive is <code>X → X</code></p>

#### [ Kenny Lau (May 03 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126018890):
<p>you need to store a function each time</p>

#### [ Kevin Buzzard (May 03 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019177):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nat_of_chnat_of_nat</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">to_nat</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- exercise</span>

<span class="c1">-- breakthough! I implemented my exciting new foo function on church numerals</span>
<span class="n">def</span> <span class="n">foo</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">choo</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">foo</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">n</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">amazing_compatibility</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
<span class="n">of_nat</span> <span class="o">(</span><span class="n">foo</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">choo</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">choo</span><span class="o">,</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">nat_of_chnat_of_nat</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 03 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019267):
<p>That makes me slightly sad</p>

#### [ Kevin Buzzard (May 03 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019292):
<p>I spent some time today thinking about the Church Numeral which given X and f and x, returns x unless X = nat and f = succ and x = 0, in which case it returns 1</p>

#### [ Kevin Buzzard (May 03 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019341):
<p>it's quite a good way of reminding yourself exactly how far you can expect to push things</p>

#### [ Kevin Buzzard (May 03 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019415):
<p>e.g. I believe that funny numeral doesn't commute with + 1 and this can be easily checked via  very concrete calculation on nat</p>

#### [ Kevin Buzzard (May 03 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019425):
<p>so you know you shouldn't be trying to prove that add commutes</p>

#### [ Kevin Buzzard (May 03 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019428):
<p>I'm not sure what Mr Ackermann would have thought about evaluating his function there</p>

#### [ Mario Carneiro (May 03 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019502):
<p>By the way, you got the free statement a bit off:</p>
<div class="codehilite"><pre><span></span>def chℕfree := {m : Π X : Type, (X → X) → X → X //
  ∀ (X Y : Type) (a : X → Y) (f : X → X) (g : Y → Y),
  a ∘ f = g ∘ a → m Y g ∘ a = a ∘ m X f}
</pre></div>

#### [ Kevin Buzzard (May 03 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019642):
<p>Do you think that's the same?</p>

#### [ Kevin Buzzard (May 03 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019651):
<p>You are quantifying over g too</p>

#### [ Kevin Buzzard (May 03 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019661):
<p>It might be the same</p>

#### [ Mario Carneiro (May 03 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019775):
<p>It might be the same, but my version fits a more regular pattern</p>

#### [ Mario Carneiro (May 03 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019789):
<p>and it doesn't require evaluating <code>m</code> at a function type</p>

#### [ Mario Carneiro (May 03 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019821):
<p>It's basically saying that if <code>a : f -&gt; g</code> is a natural transformation, then so is <code>m</code></p>

#### [ Mario Carneiro (May 03 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019871):
<p>That's probably a poor reading, but something like that</p>

#### [ Mario Carneiro (May 03 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019886):
<p>What makes <code>chN</code> not quite as powerful as system T is that <code>chN</code> isn't a type in the internal sense</p>

#### [ Mario Carneiro (May 03 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126019930):
<p>with impredicative quantification (like in system F) this would work</p>

#### [ Mario Carneiro (May 03 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020008):
<p>Godel's system T is simply typed lambda calculus with arrows and products, and a type <code>N</code> with <code>0 : N</code> and <code>S : N -&gt; N</code> and <code>iter_A : (A -&gt; A) -&gt; A -&gt; N -&gt; A</code></p>

#### [ Mario Carneiro (May 03 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020060):
<p>Then <code>N</code> there is just like lean's <code>ℕ</code>, but <code>chℕ</code> is not a substitute because it lives in <code>Type 1</code> so it is not a type in STLC</p>

#### [ Kevin Buzzard (May 03 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020250):
<p>This is really interesting</p>

#### [ Kevin Buzzard (May 03 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020253):
<p>I identified nat as the universal object</p>

#### [ Kevin Buzzard (May 03 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020256):
<p>and just wrote down some kind of standard maths functory thing about evaluating the universal object at a map</p>

#### [ Kevin Buzzard (May 03 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020304):
<p>but, like induction, you might think about universal objects in a different way to us</p>

#### [ Kevin Buzzard (May 03 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020312):
<p>I think I see what I'm missing</p>

#### [ Kevin Buzzard (May 03 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020322):
<p>In my world, a would be a map in the category</p>

#### [ Kevin Buzzard (May 03 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020323):
<p>and I would be assuming m was a functor</p>

#### [ Kevin Buzzard (May 03 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020325):
<p>and trying to represent it</p>

#### [ Kevin Buzzard (May 03 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126020332):
<p>but m being a functor is an extra condition which I have forgotten about because in the examples I know it is always there</p>

#### [ Kevin Buzzard (May 03 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126022755):
<p><code>example : equiv ℕ chℕfree := ⟨to_chfr,of_chfr,inv₁,inv₂⟩ </code></p>

#### [ Kevin Buzzard (May 03 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126022901):
<p>Mario's definition definitely works. I wonder if mine (which is implied by Mario's) is too weak.</p>

#### [ Kevin Buzzard (May 03 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023071):
<p>So I understand the category theory language much better than this DTT stuff.</p>

#### [ Kevin Buzzard (May 03 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023076):
<p>I want to say that Type is a category.</p>

#### [ Mario Carneiro (May 03 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023077):
<p>It is</p>

#### [ Kevin Buzzard (May 03 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023078):
<p>Then m wants to be a functor from Type to Type</p>

#### [ Kevin Buzzard (May 03 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023080):
<p>but Church's naive definition just demands a map on objects</p>

#### [ Mario Carneiro (May 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023123):
<p>In languages where the naive definition works, that's because of parametric polymorphism</p>

#### [ Mario Carneiro (May 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023124):
<p>i.e. everything is functorial</p>

#### [ Kevin Buzzard (May 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023125):
<p>I don't know what that means</p>

#### [ Mario Carneiro (May 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023127):
<p>HoTT is a lot like this</p>

#### [ Kevin Buzzard (May 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023128):
<p>Oh I see</p>

#### [ Mario Carneiro (May 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023130):
<p>the language is crafted such that you can't write badly behaved terms at all</p>

#### [ Mario Carneiro (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023138):
<p>everything is "fibrant"</p>

#### [ Mario Carneiro (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023139):
<p>whatever that means</p>

#### [ Kevin Buzzard (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023140):
<p>Let me modify Type</p>

#### [ Kevin Buzzard (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023142):
<p>so that its objects are still terms whose type is Type</p>

#### [ Mario Carneiro (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023143):
<p>but that's basically why univalence works</p>

#### [ Kevin Buzzard (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023144):
<p>but the morphisms are equivs</p>

#### [ Kevin Buzzard (May 03 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023146):
<p>Now m is a map on objects</p>

#### [ Kevin Buzzard (May 03 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023186):
<p>and the data of the equiv is exactly what m needs to be extendible to a map on morphisms I suspect</p>

#### [ Mario Carneiro (May 03 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023187):
<p>Check this out: <a href="http://www.cs.bham.ac.uk/~udr/papers/logical-relations-and-parametricity.pdf" target="_blank" title="http://www.cs.bham.ac.uk/~udr/papers/logical-relations-and-parametricity.pdf">http://www.cs.bham.ac.uk/~udr/papers/logical-relations-and-parametricity.pdf</a></p>

#### [ Kevin Buzzard (May 03 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023193):
<p>In fact I guess it's exactly when X and Y biject that I would even dream of identifying <code>(X-&gt;X) -&gt; X -&gt; X</code> and the analogous term for <code>Y</code></p>

#### [ Mario Carneiro (May 03 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023194):
<p>It argues that naturality is the wrong idea and should be replaced by parametricity</p>

#### [ Mario Carneiro (May 03 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023196):
<p>I need to finish digesting it though, so don't quote me on that</p>

#### [ Mario Carneiro (May 03 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023241):
<p>Notice though that the condition I gave does not require that a is an equiv</p>

#### [ Mario Carneiro (May 03 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023244):
<p>I think that's going to be true in general</p>

#### [ Mario Carneiro (May 03 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023245):
<p>It really is a functoriality condition</p>

#### [ Kevin Buzzard (May 03 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023249):
<p>You have to be careful</p>

#### [ Kevin Buzzard (May 03 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023254):
<p>Given a map A to B</p>

#### [ Mario Carneiro (May 03 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023255):
<p>it's just this weird higher order functoriality thing</p>

#### [ Mario Carneiro (May 03 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023256):
<p>It seems like logical relations generate the condition well</p>

#### [ Kevin Buzzard (May 03 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023258):
<p>You don't get a map (A to A) to (B to B)</p>

#### [ Kevin Buzzard (May 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023300):
<p>So I don't know what you mean when you say functoriality is true "in general"</p>

#### [ Kevin Buzzard (May 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023301):
<p>I can only see a functor in the equiv category</p>

#### [ Kevin Buzzard (May 03 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023308):
<p>Maybe we mean different things by functorially</p>

#### [ Mario Carneiro (May 03 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023309):
<p>I mean that if you write down some more complicated thing than chN I can write down a more complicated parametricity constraint for it</p>

#### [ Mario Carneiro (May 03 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023310):
<p>and I can always do this</p>

#### [ Mario Carneiro (May 03 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023311):
<p>and it will involve a function a : X -&gt; Y</p>

#### [ Mario Carneiro (May 03 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023313):
<p>and that function will usually not be required to be an equiv</p>

#### [ Kevin Buzzard (May 03 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023363):
<p>I can't make that concept into a functor</p>

#### [ Kevin Buzzard (May 03 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023404):
<p>For me, F (X -&gt; Y) is a map F X -&gt; F Y</p>

#### [ Mario Carneiro (May 03 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023412):
<p>Here's the setup: we define a collection of logical relations [R] : X -&gt; Y -&gt; Prop. The important one is for arrows: <code>[R -&gt; S] : (X -&gt; X') -&gt; (Y -&gt; Y') -&gt; Prop</code> is defined by</p>
<div class="codehilite"><pre><span></span>f [R -&gt; S] g &lt;-&gt; \forall x y, x [R] y -&gt; f x [S] g y
</pre></div>

#### [ Mario Carneiro (May 03 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023452):
<p>At the base types we define <code>[R] : X -&gt; Y -&gt; Prop</code> by <code>x [R] y &lt;-&gt; a x = y</code></p>

#### [ Mario Carneiro (May 03 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023454):
<p>where <code>a : X -&gt; Y</code> is our fixed morphism to commute over</p>

#### [ Mario Carneiro (May 03 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023460):
<p>Applying this definition to <code>[(R -&gt; R) -&gt; R -&gt; R]</code> gives exactly the condition I wrote down</p>

#### [ Kevin Buzzard (May 03 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023463):
<p>Oh so you're going to tell me that the function I'm looking for is actually a relation</p>

#### [ Mario Carneiro (May 03 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023623):
<p>And we can go further to even get the <code>a</code> part: we can define <code>[∀ X, R] : (∀ X:Type, P X) -&gt; (∀ X:Type, Q X) -&gt; Prop</code> by</p>
<div class="codehilite"><pre><span></span>F [∀ X, R] G &lt;-&gt; ∀ X Y : Type, ∀ (a : X -&gt; Y), F X [R] G Y
</pre></div>


<p>(here if <code>X</code> appears in <code>R</code> it's referring to the relation for the function <code>a</code>)</p>

#### [ Mario Carneiro (May 03 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023635):
<p>Finally, a term is parametrically polymorphic if it is related to itself at its type, i.e. <code>m [∀ X, (X -&gt; X) -&gt; X -&gt; X] m</code> for the case of <code>chN</code></p>

#### [ Mario Carneiro (May 03 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126023674):
<p>This is how logical relations work, and how the theorems for free statements are derived</p>

#### [ Kevin Buzzard (May 03 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Church%20Numeral%20Puzzles/near/126050623):
<blockquote>
<p>Check this out: <a href="http://www.cs.bham.ac.uk/~udr/papers/logical-relations-and-parametricity.pdf" target="_blank" title="http://www.cs.bham.ac.uk/~udr/papers/logical-relations-and-parametricity.pdf">http://www.cs.bham.ac.uk/~udr/papers/logical-relations-and-parametricity.pdf</a></p>
</blockquote>
<p>That paper</p>


{% endraw %}
