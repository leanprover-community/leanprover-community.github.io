---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/17450Howtoinsertdefinitionofafunctioninaproof.html
---

## Stream: [new members](index.html)
### Topic: [How to insert definition of a function in a proof](17450Howtoinsertdefinitionofafunctioninaproof.html)

---


{% raw %}
#### [ Tobias Grosser (Oct 20 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136147887):
<p>Hi, I again have a simple beginners questions. The definition of</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_inv</span> <span class="n">α</span><span class="o">]:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
   <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">optional_ij</span> <span class="o">:=</span> <span class="n">pick_encodable</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">el</span><span class="o">,</span> <span class="n">el</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="k">in</span>
  <span class="k">match</span> <span class="n">optional_ij</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">some</span> <span class="n">ij</span> <span class="o">:=</span>
    <span class="k">let</span> <span class="n">i</span> <span class="o">:=</span> <span class="n">ij</span><span class="bp">.</span><span class="mi">1</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">j</span> <span class="o">:=</span> <span class="n">ij</span><span class="bp">.</span><span class="mi">2</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">A</span> <span class="n">i</span> <span class="n">j</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">A1</span> <span class="o">:=</span> <span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="n">A</span><span class="o">)</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">A1&#39;</span> <span class="o">:=</span> <span class="n">fin_swap</span> <span class="n">A1</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">A1&#39;</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">ursubmx</span> <span class="n">A1&#39;</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">a</span><span class="bp">⁻¹</span> <span class="err">•</span> <span class="n">dlsubmx</span> <span class="n">A1&#39;</span> <span class="k">in</span>
    <span class="k">let</span> <span class="o">(</span><span class="n">L</span><span class="o">,</span> <span class="n">U</span><span class="o">,</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Gaussian_elimination</span> <span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">drsubmx</span> <span class="n">A1&#39;</span> <span class="bp">-</span> <span class="o">(</span><span class="n">v</span> <span class="bp">*</span><span class="err">ₘ</span> <span class="n">u</span><span class="o">))</span> <span class="k">in</span>
    <span class="o">(</span>
      <span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">block_mx</span> <span class="mi">1</span> <span class="mi">0</span> <span class="n">v</span> <span class="n">L</span><span class="o">)),</span>
      <span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">block_mx</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i1</span> <span class="n">j1</span><span class="o">,</span> <span class="n">a</span><span class="o">)</span> <span class="n">u</span> <span class="mi">0</span> <span class="n">U</span><span class="o">)),</span>
      <span class="n">r</span> <span class="bp">+</span> <span class="mi">1</span>
    <span class="o">)</span>
  <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span>
     <span class="o">(</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="mi">0</span>
     <span class="o">)</span>
  <span class="kn">end</span>
<span class="bp">|</span> <span class="n">x</span> <span class="n">y</span> <span class="n">A</span> <span class="o">:=</span>
     <span class="o">(</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="mi">0</span>
</pre></div>


<p>appears in a proof  state:</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_5</span> <span class="o">:</span> <span class="n">ordered_ring</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_8</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_9</span> <span class="o">:</span> <span class="n">has_inv</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_10</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">α</span><span class="o">,</span>
<span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">M</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="o">(</span><span class="n">Gaussian_elimination</span> <span class="n">m</span> <span class="n">m</span> <span class="n">M</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">*</span><span class="err">ₘ</span> <span class="o">((</span><span class="n">Gaussian_elimination</span> <span class="n">m</span> <span class="n">m</span> <span class="n">M</span><span class="o">)</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span> <span class="n">M</span>
</pre></div>


<p>I expected a simple <code>rw Gaussian_elimination</code> to inline the definition of Gaussian_eliminatin into the proof. But unfortunately this did not work out. Any ideas what I did wrong?</p>

#### [ Tobias Grosser (Oct 20 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148002):
<p>I unfortunately just get "failed"</p>

#### [ Chris Hughes (Oct 20 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148305):
<p>It will only reduce if it's applied to <code>m+1</code> or <code>0</code>, not <code>m</code></p>

#### [ Tobias Grosser (Oct 20 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148381):
<p>I see.</p>

#### [ Tobias Grosser (Oct 20 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148383):
<p>Any quick pointer how I introduce m+1 or 0?</p>

#### [ Tobias Grosser (Oct 20 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148439):
<p>Found it. Just need to do 'induction m'.</p>

#### [ Tobias Grosser (Oct 20 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148481):
<p>Thanks a lot, this was easy.</p>

#### [ Tobias Grosser (Oct 20 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149746):
<p>OK, the basecase is now also proofen. Learned the 'ext' tactic and fin_zero_elim.</p>

#### [ Tobias Grosser (Oct 20 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149747):
<p>I am now in</p>
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_5</span> <span class="o">:</span> <span class="n">ordered_ring</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_8</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_9</span> <span class="o">:</span> <span class="n">has_inv</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_10</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">α</span><span class="o">,</span>
<span class="n">n</span> <span class="n">m_n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">m_ih</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_n</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_n</span><span class="o">)</span> <span class="n">α</span><span class="o">),</span>
    <span class="o">(</span><span class="n">Gaussian_elimination</span> <span class="n">m_n</span> <span class="n">m_n</span> <span class="n">M</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">*</span><span class="err">ₘ</span> <span class="o">((</span><span class="n">Gaussian_elimination</span> <span class="n">m_n</span> <span class="n">m_n</span> <span class="n">M</span><span class="o">)</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span> <span class="n">M</span><span class="o">,</span>
<span class="n">M</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">m_n</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">m_n</span><span class="o">))</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="o">(</span><span class="n">Gaussian_elimination</span><span class="bp">._</span><span class="n">match_1</span> <span class="n">m_n</span> <span class="n">m_n</span> <span class="n">M</span>
         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">ij</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">×</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)),</span>
            <span class="n">Gaussian_elimination</span> <span class="n">m_n</span> <span class="n">m_n</span>
              <span class="o">(</span><span class="n">drsubmx</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">xrow</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span> <span class="mi">0</span> <span class="n">M</span><span class="o">)))</span> <span class="bp">+</span>
                 <span class="bp">-</span><span class="o">((</span><span class="n">M</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">))</span><span class="bp">⁻¹</span> <span class="err">•</span> <span class="n">dlsubmx</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">xrow</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span> <span class="mi">0</span> <span class="n">M</span><span class="o">)))</span> <span class="bp">*</span><span class="err">ₘ</span>
                      <span class="n">ursubmx</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">xrow</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span> <span class="mi">0</span> <span class="n">M</span><span class="o">))))))</span>
         <span class="o">(</span><span class="n">pick_encodable</span> <span class="n">α</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">el</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="bp">¬</span><span class="n">el</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">M</span><span class="o">))</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">*</span><span class="err">ₘ</span>
      <span class="o">((</span><span class="n">Gaussian_elimination</span><span class="bp">._</span><span class="n">match_1</span> <span class="n">m_n</span> <span class="n">m_n</span> <span class="n">M</span>
          <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">ij</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">×</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)),</span>
             <span class="n">Gaussian_elimination</span> <span class="n">m_n</span> <span class="n">m_n</span>
               <span class="o">(</span><span class="n">drsubmx</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">xrow</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span> <span class="mi">0</span> <span class="n">M</span><span class="o">)))</span> <span class="bp">+</span>
                  <span class="bp">-</span><span class="o">((</span><span class="n">M</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">))</span><span class="bp">⁻¹</span> <span class="err">•</span> <span class="n">dlsubmx</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">xrow</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span> <span class="mi">0</span> <span class="n">M</span><span class="o">)))</span> <span class="bp">*</span><span class="err">ₘ</span>
                       <span class="n">ursubmx</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">xrow</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="o">(</span><span class="n">ij</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span> <span class="mi">0</span> <span class="n">M</span><span class="o">))))))</span>
          <span class="o">(</span><span class="n">pick_encodable</span> <span class="n">α</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">el</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="bp">¬</span><span class="n">el</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">m_n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">M</span><span class="o">))</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span>
    <span class="n">M</span>
</pre></div>

#### [ Tobias Grosser (Oct 20 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149749):
<p>That seems complicated.</p>

#### [ Tobias Grosser (Oct 20 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149755):
<p>In case anybody wants to drop me a bone, this would be appreciated.</p>

#### [ Chris Hughes (Oct 20 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150894):
<p><code>funext</code> is a start</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150900):
<p>Thanks.</p>

#### [ Chris Hughes (Oct 20 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150903):
<p>But it looks really complicated.</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150910):
<p>That's what I feel.</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150950):
<p>Maybe I approach this from the wrong angle.</p>

#### [ Chris Hughes (Oct 20 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150952):
<p>What is <code>pick_encodable</code>?</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150953):
<p>I basically want to show that " (M : matrix (fin m) (fin m) α) : (getL M) *ₘ (getU M) = M :="</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150963):
<p>That comes from: <code>  let optional_ij := pick_encodable (α) (λ el, el ≠ 0) (x+1) (y+1) A in</code></p>

#### [ Tobias Grosser (Oct 20 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150969):
<p>It finds a non-zero element in the matrix.</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151009):
<p>And returns an optional.</p>

#### [ Chris Hughes (Oct 20 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151011):
<p>What is <code>getL</code>?</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151015):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">getL</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_inv</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span>  <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">res</span> <span class="o">:=</span> <span class="n">Gaussian_elimination</span> <span class="n">n</span> <span class="n">m</span> <span class="n">M</span> <span class="k">in</span>
  <span class="n">res</span><span class="bp">.</span><span class="mi">1</span>

<span class="n">def</span> <span class="n">getU</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_inv</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span>  <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">res</span> <span class="o">:=</span> <span class="n">Gaussian_elimination</span> <span class="n">n</span> <span class="n">m</span> <span class="n">M</span> <span class="k">in</span>
  <span class="n">res</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span>
</pre></div>

#### [ Tobias Grosser (Oct 20 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151022):
<p>That's the full algorithm:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_inv</span> <span class="n">α</span><span class="o">]:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
   <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">optional_ij</span> <span class="o">:=</span> <span class="n">pick_encodable</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">el</span><span class="o">,</span> <span class="n">el</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="k">in</span>
  <span class="k">match</span> <span class="n">optional_ij</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">some</span> <span class="n">ij</span> <span class="o">:=</span>
    <span class="k">let</span> <span class="n">i</span> <span class="o">:=</span> <span class="n">ij</span><span class="bp">.</span><span class="mi">1</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">j</span> <span class="o">:=</span> <span class="n">ij</span><span class="bp">.</span><span class="mi">2</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">A</span> <span class="n">i</span> <span class="n">j</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">A1</span> <span class="o">:=</span> <span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="n">A</span><span class="o">)</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">A1&#39;</span> <span class="o">:=</span> <span class="n">fin_swap</span> <span class="n">A1</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">A1&#39;</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">ursubmx</span> <span class="n">A1&#39;</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">a</span><span class="bp">⁻¹</span> <span class="err">•</span> <span class="n">dlsubmx</span> <span class="n">A1&#39;</span> <span class="k">in</span>
    <span class="k">let</span> <span class="o">(</span><span class="n">L</span><span class="o">,</span> <span class="n">U</span><span class="o">,</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Gaussian_elimination</span> <span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">drsubmx</span> <span class="n">A1&#39;</span> <span class="bp">-</span> <span class="o">(</span><span class="n">v</span> <span class="bp">*</span><span class="err">ₘ</span> <span class="n">u</span><span class="o">))</span> <span class="k">in</span>
    <span class="o">(</span>
      <span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">block_mx</span> <span class="mi">1</span> <span class="mi">0</span> <span class="n">v</span> <span class="n">L</span><span class="o">)),</span>
      <span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="o">(</span><span class="n">fin_swap</span> <span class="o">(</span><span class="n">block_mx</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i1</span> <span class="n">j1</span><span class="o">,</span> <span class="n">a</span><span class="o">)</span> <span class="n">u</span> <span class="mi">0</span> <span class="n">U</span><span class="o">)),</span>
      <span class="n">r</span> <span class="bp">+</span> <span class="mi">1</span>
    <span class="o">)</span>
  <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span>
     <span class="o">(</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="mi">0</span>
     <span class="o">)</span>
  <span class="kn">end</span>
<span class="bp">|</span> <span class="n">x</span> <span class="n">y</span> <span class="n">A</span> <span class="o">:=</span>
     <span class="o">(</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span><span class="o">))</span> <span class="n">α</span><span class="o">)),</span>
      <span class="mi">0</span>
     <span class="o">)</span>
</pre></div>

#### [ Tobias Grosser (Oct 20 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151024):
<p>It computes a matrix L, a matrix U and the rank of the matrix M.</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151130):
<p>I feel I should proof something simpler.</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151131):
<p>E.g. that the result matrix is in upper triangular form.</p>

#### [ Chris Hughes (Oct 20 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151312):
<p>What are <code>xrow</code> and <code>fin_swap</code> and <code>block_mx</code>?</p>

#### [ Tobias Grosser (Oct 20 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151515):
<p><a href="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean" target="_blank" title="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean">https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean</a></p>

#### [ Tobias Grosser (Oct 20 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151629):
<p><a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&amp;rep=rep1&amp;type=pdf" target="_blank" title="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&amp;rep=rep1&amp;type=pdf">http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&amp;rep=rep1&amp;type=pdf</a></p>

#### [ Tobias Grosser (Oct 20 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151630):
<p>Is the relevant paper.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151670):
<p>I just started playing around with it. See sec 3.1 for the relevant algorithm.</p>

#### [ Chris Hughes (Oct 20 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151823):
<p>That is surprising. I was going to say that my instinct would be to do it totally differently, and express each Gaussian elimination operation, as multiplication by a well chosen matrix, and prove the properties of the matrices that correspond to the Gaussian elimination operations. Georges Gonthier probably knows what he's doing though.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151874):
<p>I am new to lean. Probably this problem is too difficult for now, but I feel I understand matrices so I want to follow a proof that already exists, is interesting and at the same time useful.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151877):
<p>If you have advices what would be reasonable steps and which parts would be useful for mathlib, that would certainly be helpful.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151886):
<p>The paper justifies some of the choices they have taken.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151926):
<p>Now the proof structure itself can likely be changed without affecting everything that uses Gaussian elimination.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151927):
<p>Would be interesting to see if your proof idea might even be nicer than their original proof idea.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151977):
<p>I doubt that the proof structure depends a lot on coq vs. lean, but if your proof is more accessible to people less advanced than Georges, this would be interesting to me.</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152216):
<p>My guess is that translating so strictly from Coq is not going to come out well</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152260):
<p>The thing about translations is that even though the axioms are similar, the <em>language</em>, in the informal sense, is different. We use different modes of speech for the same kinds of things</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152265):
<p>and the library is "written in that language", meaning that you will encounter friction if you don't use it</p>

#### [ Scott Morrison (Oct 20 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152284):
<p>My student <span class="user-mention" data-user-id="120536">@Jack Crawford</span> has also been looking at gaussian elimination. He's been using an inductive type describing individual steps of row operations.</p>

#### [ Scott Morrison (Oct 20 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152293):
<p>It acts like a "relation" between two matrices, but carries the data of the elementary matrix to multiply by.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152330):
<p>Are you talking about Jack?</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152334):
<p>I mean, I obviously have no idea what the right approach is.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152336):
<p>Just use this to learn stuff.</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152341):
<p>It might help to try to invent your own gaussian elimination</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152343):
<p>rather than porting from coq</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152350):
<p>Use the coq development and wikipedia to help you with the maths, and just focus on the lean encoding part</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152391):
<p>So you feel my translation from coq is not very ideomatic in lean?</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152394):
<p>that's right</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152397):
<p>It seems to do what I want, so I am reasonably happy with it.</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152401):
<p>in particular, I would work more with fintypes and less with fin n</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152402):
<p>As I don't really know lean, I have zero feeling what would be more ideomatic</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152410):
<p>OK, I can change this. Not sure though if this would change the overall algorithm a lot.</p>

#### [ Mario Carneiro (Oct 20 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152415):
<p>I would be curious to hear how Jack is doing things differently</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152416):
<p>It might be interesting to look into the code from <span class="user-mention" data-user-id="120536">@Jack Crawford</span></p>

#### [ Tobias Grosser (Oct 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152456):
<p>Yes.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152467):
<p>He promised to share the code, but his now on exam leave.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152478):
<p>It seems Scott gave already quite some input on <span class="user-mention" data-user-id="120536">@Jack Crawford</span> 's code, so I assume it is more ideomatic.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152479):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> , what is your goal with GE?</p>

#### [ Jack Crawford (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152480):
<p>I really need to clean a few things up first and am currently on mobile so don’t have my code with me, but as Scott said, I’m just using inductive types to break row equivalence down into steps</p>

#### [ Jack Crawford (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152483):
<p>I’ll share the code as soon as I have it neater and a little more complete</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152523):
<p>Would it make sense to build up a matrix theory similar to <a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&amp;rep=rep1&amp;type=pdf" target="_blank" title="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&amp;rep=rep1&amp;type=pdf">http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&amp;rep=rep1&amp;type=pdf</a></p>

#### [ Tobias Grosser (Oct 20 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152525):
<p>mathcomp.mxalgebra?</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152526):
<p>Or is this not even useful in the context of lean?</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152530):
<p><span class="user-mention" data-user-id="120536">@Jack Crawford</span> , no need to rush.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152535):
<p>I would be glad to look over your code to learn from it.</p>

#### [ Jack Crawford (Oct 20 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152577):
<p>I have an inductive type that represents a single “step” of a row equivalence, with a constructor for scaling, swapping, and linear addition of matrices, and then I have another inductive type that gives me the transitive closure of this.</p>

#### [ Jack Crawford (Oct 20 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152640):
<p>Then I have a few functions that perform individual steps of the GE algorithm (putting the pivot in the right place, scaling the pivot, eliminating down the column). Then I show that the result of each of these steps are row-equivalent (by my previous inductive definition of row-equivalence) with the original matrix, and then I make a new function that just combines these steps of the Gaussian elimination in the obvious way, and show that it is also row-equivalent by carrying through my proofs that each of the individual steps that it is composed of is row-equivalent</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152643):
<p>I see.</p>

#### [ Jack Crawford (Oct 20 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152684):
<p>and from my row-equivalence I can get the proof that the invertible matrix which represents all of the steps of the row reduction, times the original matrix, is in fact the row-reduced version of the matrix</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152685):
<p>I see,</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152691):
<p>Do you also compute an extended gaussian elimination similar to what 'Georges Gonthier' does?</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152695):
<p>Meaning, do you e.g. have proofs about the rank of the matrix?</p>

#### [ Jack Crawford (Oct 20 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152907):
<p>Not yet, I haven’t actually gotten to proving much at all yet because I’ve had to re-write substantial parts of my code a few times over now. Hopefully this will be the final iteration! Haven’t really given much of a thought to matrix rank yet</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136153002):
<p>OK. Please ping me when it's time to look at your code.</p>

#### [ Tobias Grosser (Oct 20 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136153003):
<p>Also, feedback on the Georges paper would be interesting.</p>


{% endraw %}
