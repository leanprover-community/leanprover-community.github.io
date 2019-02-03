---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64146howtocallthislemma.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [how to call this lemma](https://leanprover-community.github.io/archive/113488general/64146howtocallthislemma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Aug 07 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131039906):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">quux</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="n">sum</span> <span class="n">univ</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">sum</span> <span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040023):
<p>Ooh, and if you don't know a name, but you know a <em>proof</em>... that's fine too.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040821):
<p>Johan, I think Kenny might have generated a proof of this once, when I was trying to figure out induction.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040877):
<p><a href="https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/" target="_blank" title="https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/">https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/</a></p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040889):
<p>check out def4 in <a href="https://github.com/kckennylau/Lean/blob/master/proofs_by_induction.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/proofs_by_induction.lean">https://github.com/kckennylau/Lean/blob/master/proofs_by_induction.lean</a></p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040899):
<p>Apparently it uses a lemma called <code>chris</code>. I'm not sure if this is the official mathlib-sanctioned name.</p>

#### [ Johan Commelin (Aug 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131041195):
<p>Ok, thanks. I'll take a look in a minute!</p>

#### [ Chris Hughes (Aug 07 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042444):
<p>I proved a slightly weaker version</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">quux</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">sum</span> <span class="n">univ</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="bp">_⟩</span>  <span class="bp">+</span> <span class="n">sum</span> <span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">insert_erase</span> <span class="o">(</span><span class="n">mem_univ</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="bp">_⟩</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))),</span>
    <span class="n">sum_insert</span> <span class="o">(</span><span class="n">not_mem_erase</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span> <span class="n">add_left_inj</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span>
<span class="n">sum_bij</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">lt_of_le_of_ne</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span>
  <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">vne_of_ne</span> <span class="o">(</span><span class="n">mem_erase</span><span class="bp">.</span><span class="mi">1</span> <span class="n">ha</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">⟩</span> <span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">mem_univ</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">veq_of_eq</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">_</span><span class="o">))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">hb</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">b</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_of_lt</span> <span class="n">b</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">mem_erase</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">fin</span><span class="bp">.</span><span class="n">ne_of_vne</span> <span class="o">(</span><span class="n">ne_of_lt</span> <span class="n">b</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span> <span class="n">mem_univ</span> <span class="bp">_⟩</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">cases</span> <span class="n">b</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042466):
<p>Why is it weaker?</p>

#### [ Johan Commelin (Aug 07 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042478):
<p>Also, apparently I ought to be using <code>finset.range</code>...</p>

#### [ Chris Hughes (Aug 07 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042484):
<p>I used <code>⟨n, nat.lt_succ_self _⟩</code> instead of <code>\u n</code></p>

#### [ Johan Commelin (Aug 07 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042536):
<p>Aaah, but that is better.</p>

#### [ Johan Commelin (Aug 07 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042543):
<p>Silly me didn't understand that <code>\u n</code> is difficult.</p>

#### [ Johan Commelin (Aug 07 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042561):
<p>I think you can use <code>nat.le_refl _</code> for some golfing.</p>

#### [ Johan Commelin (Aug 07 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042583):
<p>But I will first think about the <code>finset.range</code> version. Maybe it becomes a whole lot easier.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046567):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">quux</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span>
<span class="o">:</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">n</span> <span class="bp">+</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046594):
<p>So, that might not be even worth stating as a lemma.</p>

#### [ Kenny Lau (Aug 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046619):
<p>what's the use of this lemma if you could just <code>simp</code>?</p>

#### [ Johan Commelin (Aug 07 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046678):
<p>That's exactly my point.</p>


{% endraw %}
