---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53220whatisthefastestwaytoprovethis.html
---

## Stream: [general](index.html)
### Topic: [what is the fastest way to prove this](53220whatisthefastestwaytoprovethis.html)

---


{% raw %}
#### [ Kenny Lau (Apr 25 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125675713):
<div class="codehilite"><pre><span></span><span class="n">p</span> <span class="n">q</span> <span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">,</span>
<span class="n">xp</span> <span class="n">xq</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span>
<span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">hm</span> <span class="o">:</span> <span class="err">↑</span><span class="n">t</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">*</span> <span class="n">m</span><span class="o">,</span>
<span class="n">hn</span> <span class="o">:</span> <span class="err">↑</span><span class="n">t</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">q</span> <span class="bp">*</span> <span class="n">n</span><span class="o">,</span>
<span class="n">hpqt</span> <span class="o">:</span> <span class="n">xp</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">m</span> <span class="bp">=</span> <span class="n">xq</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">n</span>
<span class="err">⊢</span> <span class="n">xp</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">q</span> <span class="bp">=</span> <span class="n">xq</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">p</span>
</pre></div>

#### [ Chris Hughes (Apr 25 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680907):
<p>Best I could do. It's not easy to keep it short.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">}</span> <span class="o">{</span><span class="n">xp</span> <span class="n">xq</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">q</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span>
    <span class="o">(</span><span class="n">hpqt</span> <span class="o">:</span> <span class="n">xp</span> <span class="bp">*</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">xq</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">xp</span> <span class="bp">*</span> <span class="n">q</span> <span class="bp">=</span> <span class="n">xq</span> <span class="bp">*</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">hm0</span> <span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_ne_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">lt_irrefl</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">trans_rel_left</span>
    <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span> <span class="n">mul_zero</span><span class="o">]</span> <span class="n">at</span> <span class="n">hm</span><span class="o">))),</span>
<span class="k">have</span> <span class="n">hm&#39;</span> <span class="o">:</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">p</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:=</span> <span class="k">show</span> <span class="o">((</span><span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">p</span> <span class="bp">*</span> <span class="n">m</span><span class="o">,</span> <span class="k">from</span> <span class="n">hm</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hn&#39;</span> <span class="o">:</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">q</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">show</span> <span class="o">((</span><span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">q</span> <span class="bp">*</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">hn</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
<span class="o">(</span><span class="n">domain</span><span class="bp">.</span><span class="n">mul_right_inj</span> <span class="n">hm0</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_assoc</span> <span class="n">xq</span><span class="o">,</span> <span class="err">←</span> <span class="n">hm&#39;</span><span class="o">,</span> <span class="n">hn&#39;</span><span class="o">,</span> <span class="n">mul_left_comm</span><span class="o">,</span> <span class="err">←</span> <span class="n">hpqt</span><span class="o">,</span> <span class="n">mul_left_comm</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">])</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680964):
<p>thanks</p>

#### [ Chris Hughes (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680967):
<p>What's the fastest way to prove this?</p>
<div class="codehilite"><pre><span></span><span class="n">even_sum_four_squares</span> <span class="o">{</span><span class="n">n</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span>
    <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
    <span class="bp">∃</span> <span class="n">w</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">w</span> <span class="bp">*</span> <span class="n">w</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">z</span> <span class="bp">*</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">∧</span>
    <span class="n">w</span> <span class="bp">*</span> <span class="n">w</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">]</span> <span class="bp">∧</span> <span class="n">y</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">z</span> <span class="bp">*</span> <span class="n">z</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680971):
<p>aha</p>

#### [ Chris Hughes (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680977):
<p>That was horrible</p>

#### [ Chris Hughes (Apr 25 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680996):
<p>I just did a bazillion cases on whether things were odd or even.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684665):
<p>A mathematician would say that clearly two of a,b,c have the same parity</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684677):
<p>so let w and x be those two</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684692):
<p>I would like to prove it in Lean with some kind of WLOG</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684696):
<p>"wlog a and b have the same parity"</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684699):
<p>because I can switch c with either a or b if necessary</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684705):
<p>So here the symmetry is three-fold.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684749):
<p>The question is invariant under any permutation of the set {a,b,c}</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684753):
<p>and I know two of those elements must be congruent mod 2</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684754):
<p>so WLOG they're a and b</p>

#### [ Chris Hughes (Apr 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684855):
<p>Very difficult to say nicely in lean</p>

#### [ Chris Hughes (Apr 25 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684879):
<p>This was my proof</p>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">]</span> <span class="o">:=</span>
  <span class="n">modeq_zero_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">H</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">dvd_mul_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
<span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">mod_two_eq_zero_or_one</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">a</span><span class="o">))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">ha</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">mod_two_eq_zero_or_one</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">b</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">hb</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="o">,</span> <span class="n">d</span><span class="o">,</span> <span class="n">H</span><span class="o">,</span> <span class="n">even_add_even</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span>
      <span class="n">modeq_add_cancel_left</span> <span class="o">(</span><span class="k">show</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">],</span> <span class="k">from</span> <span class="n">even_add_even</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">)</span>
      <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">h&#39;</span><span class="o">)</span><span class="bp">⟩</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">hb</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">mod_two_eq_zero_or_one</span> <span class="o">(</span><span class="n">c</span> <span class="bp">*</span> <span class="n">c</span><span class="o">))</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">hc</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">c</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">d</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span> <span class="n">even_add_even</span> <span class="n">ha</span> <span class="n">hc</span><span class="o">,</span>
        <span class="n">modeq_add_cancel_left</span> <span class="o">(</span><span class="k">show</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">],</span> <span class="k">from</span> <span class="n">even_add_even</span> <span class="n">ha</span> <span class="n">hc</span><span class="o">)</span>
          <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">h&#39;</span><span class="o">)</span><span class="bp">⟩</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">hc</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">d</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span>
        <span class="n">modeq_add_cancel_left</span> <span class="o">(</span><span class="k">show</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">],</span> <span class="k">from</span> <span class="n">odd_add_odd</span> <span class="n">hb</span> <span class="n">hc</span><span class="o">)</span>
          <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">h&#39;</span><span class="o">),</span>
        <span class="n">odd_add_odd</span> <span class="n">hb</span> <span class="n">hc</span><span class="bp">⟩</span><span class="o">)))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">ha</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">mod_two_eq_zero_or_one</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">b</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">hb</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">mod_two_eq_zero_or_one</span> <span class="o">(</span><span class="n">c</span> <span class="bp">*</span> <span class="n">c</span><span class="o">))</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">hc</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="o">,</span> <span class="n">a</span><span class="o">,</span> <span class="n">d</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span> <span class="n">even_add_even</span> <span class="n">hb</span> <span class="n">hc</span><span class="o">,</span>
        <span class="n">modeq_add_cancel_left</span> <span class="o">(</span><span class="k">show</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">],</span> <span class="k">from</span> <span class="n">even_add_even</span> <span class="n">hb</span> <span class="n">hc</span><span class="o">)</span>
          <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">h&#39;</span><span class="o">)</span><span class="bp">⟩</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">hc</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">c</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">d</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span> <span class="n">odd_add_odd</span> <span class="n">ha</span> <span class="n">hc</span><span class="o">,</span>
        <span class="n">modeq_add_cancel_left</span> <span class="o">(</span><span class="k">show</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">],</span> <span class="k">from</span> <span class="n">odd_add_odd</span> <span class="n">ha</span> <span class="n">hc</span><span class="o">)</span>
          <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">h&#39;</span><span class="o">)</span><span class="bp">⟩</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">hb</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="o">,</span> <span class="n">d</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span> <span class="n">odd_add_odd</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span>
      <span class="n">modeq_add_cancel_left</span> <span class="o">(</span><span class="k">show</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">≡</span> <span class="mi">0</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">2</span><span class="o">],</span> <span class="k">from</span> <span class="n">odd_add_odd</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">)</span>
          <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">h&#39;</span><span class="o">)</span><span class="bp">⟩</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684938):
<p>It looks a bit like a sonnet</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685035):
<p>My WLOG observation was that, just as we have a 2-variable WLOG which says that if the question is invariant under switching the two variables and we know that some predicate must be satisfied by some arrangement of the variables (e.g. x &lt;= y), then we may assume that the predicate is satisfied by the default arrangement,</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685084):
<p>there is a 3-variable generalisation which says that if the question is invariant under all permutations of three variables and you can find some predicate which is true for some arrangement (e.g. "two of these three variables get sent to the same element under a map to a type with two elements") then WLOG it's true for the default arrangement</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685158):
<p>I am very interested in making Lean do things which mathematicians find trivial, painlessly, so I quite like thinking about things such as this.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685188):
<p>I regard issues such as the one you brought up as a barrier to getting mathematicians to adopt automated proof checking as part of their routine</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685241):
<p>If you find yourself needing this kind of WLOG again I'd be interested to hear.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685282):
<p>I'd happily spend some time over the summer trying to learn how to write tactics such as this. In this case it feel like it's a generalisation of Simon's WLOG</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685390):
<p>If you had it then the proof would be Wlog3 a %2 = b % 2, by tactic.ring (showing that permuting the variables doesn't change the assumption)</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685395):
<p>and then let w be a, x be b etc</p>

#### [ Johan Commelin (Apr 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685490):
<p>So now we need <span class="user-mention" data-user-id="110026">@Simon Hudon</span> to write an n-variable WLOG tactic... (-;</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685677):
<p>I think that the 2-variable WLOG is a powerful tool which genuinely does come up in practice</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685686):
<p>I am less convinced that the 3-variable WLOG shows up so much</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685689):
<p>however it sounds like a good exercise for the beginner</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685692):
<p>or possibly an incredibly difficult one</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685739):
<p>I think the n-variable one should definitely be left to Hudon ;-)</p>

#### [ Simon Hudon (Apr 25 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685774):
<p>Interesting! In my previous prover, I had n-variable permutations in wlog but after talking to Assia, I started thinking that it was not the most useful generalization</p>

#### [ Simon Hudon (Apr 25 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685793):
<p>n-pairs of swaps seemed more interesting</p>

#### [ Simon Hudon (Apr 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685855):
<p>If you come up with another example where 3+ variable permutation is useful, I'll implement it</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686172):
<p>I agree that one should find out what users actually need in practice before leaping into multi-variable WLOG. I can't believe I just said that phrase.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686237):
<p>The reason I suggested 3-variable WLOG is that at some point I suspect that it will do my Lean understanding some good if I were to actually write a tactic, and Chris and I will be spending the summer working on Lean together (with 13 other people)</p>

#### [ Simon Hudon (Apr 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686426):
<p>Are you becoming a ... pragmatist?  <em>gasp</em></p>

#### [ Kevin Buzzard (Apr 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686446):
<p>no, I just want to learn</p>

#### [ Simon Hudon (Apr 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686447):
<p>But seriously, it is certainly a fun exercise. Let me know if you have questions</p>


{% endraw %}
