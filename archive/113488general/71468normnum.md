---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71468normnum.html
---

## Stream: [general](index.html)
### Topic: [norm_num](71468normnum.html)

---


{% raw %}
#### [ Sebastien Gouezel (Dec 03 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797276):
<p>I was under the impression that <code>norm_num</code> was always successful in its range of expertise. Here is a real-life counterexample:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">crazy</span> <span class="o">(</span><span class="n">k</span> <span class="n">l</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">≤</span> <span class="n">k</span><span class="o">):</span> <span class="o">((</span><span class="mi">2</span><span class="o">:</span><span class="n">real</span><span class="o">)</span><span class="bp">⁻¹</span><span class="o">)</span><span class="err">^</span><span class="n">k</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">2</span><span class="bp">⁻¹</span><span class="o">)</span><span class="err">^</span><span class="n">l</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">pow_le_pow_of_le_one</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">norm_num</span><span class="o">,</span>
  <span class="c1">-- goal is 2⁻¹ ≤ 1</span>
  <span class="n">norm_num</span>
<span class="kn">end</span>
</pre></div>


<p>The last <code>norm_num</code> call gives rise to a deterministic timeout. Replacing it with <code>show 2⁻¹ ≤ (1 : real), by norm_num</code> works fine, so this is not really a problem for me, but still surprising.</p>

#### [ Kevin Buzzard (Dec 03 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797777):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>

<span class="kn">lemma</span> <span class="n">crazy</span> <span class="o">(</span><span class="n">k</span> <span class="n">l</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">≤</span> <span class="n">k</span><span class="o">):</span> <span class="o">((</span><span class="mi">2</span><span class="o">:</span><span class="n">real</span><span class="o">)</span><span class="bp">⁻¹</span><span class="o">)</span><span class="err">^</span><span class="n">k</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">2</span><span class="bp">⁻¹</span><span class="o">)</span><span class="err">^</span><span class="n">l</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">pow_le_pow_of_le_one</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">norm_num</span><span class="o">,</span>
  <span class="c1">-- goal is 2⁻¹ ≤ 1</span>
  <span class="k">show</span> <span class="o">(</span><span class="mi">2</span><span class="bp">⁻¹</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">norm_num</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I've seen this before, but don't remember why it's happening.</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797846):
<p><code>norm_num</code> is fighting with <code>simp</code>. Compare with <code>norm_num1, simp, norm_num1, simp,</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150797854):
<p>which is basically what <code>norm_num</code> does</p>

#### [ Sebastien Gouezel (Dec 03 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798112):
<p>Does it mean that it would be more safe for <code>norm_num</code> to call <code>simp [-one_div_eq_inv]</code>? By the way, I am not convinced that <code>one_div_eq_inv</code> is a good simp rule, what do you think?</p>

#### [ Patrick Massot (Dec 03 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798174):
<p>It's the same family that turns every <code>a-b</code> into <code>a+-b</code> that I hate</p>

#### [ Patrick Massot (Dec 03 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798199):
<p>and it's in core lib <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Mario Carneiro (Dec 03 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798795):
<p>a better question is why <code>norm_num1</code> isn't solving the goal</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798811):
<p>since it does solve the goal if you canonize the instances by restating the goal as you did</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798908):
<p>I think this one is a result of my relying on the C++ <code>norm_num</code> implementation, which lags behind the mathlib implementation quite a bit</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150798941):
<p>I use it for doing <code>+</code> <code>-</code> <code>*</code> <code>/</code> on rings and fields, and do everything else in lean</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150799067):
<p>but I have seen it get confused with weird instances before (i.e. <code>simp</code> wants to prove that <code>(0 : int) != (1 : multiplicative int)</code> even though it's false)</p>

#### [ Sebastien Gouezel (Dec 03 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150799423):
<p>It is definitely confused by the instances. With <code>pp.all</code>, the goal it can not solve is</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="n">has_le</span><span class="bp">.</span><span class="n">le</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">preorder</span><span class="bp">.</span><span class="n">to_has_le</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">partial_order</span><span class="bp">.</span><span class="n">to_preorder</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">ordered_comm_monoid</span><span class="bp">.</span><span class="n">to_partial_order</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">ordered_cancel_comm_monoid</span><span class="bp">.</span><span class="n">to_ordered_comm_monoid</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
                <span class="o">(</span><span class="bp">@</span><span class="n">ordered_semiring</span><span class="bp">.</span><span class="n">to_ordered_cancel_comm_monoid</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
                   <span class="o">(</span><span class="bp">@</span><span class="n">linear_ordered_semiring</span><span class="bp">.</span><span class="n">to_ordered_semiring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">linear_ordered_semiring</span><span class="o">))))))</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_inv</span><span class="bp">.</span><span class="n">inv</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">division_ring</span><span class="bp">.</span><span class="n">to_has_inv</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">division_ring</span><span class="o">)</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">bit0</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">distrib</span><span class="bp">.</span><span class="n">to_has_add</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">ring</span><span class="bp">.</span><span class="n">to_distrib</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
                <span class="o">(</span><span class="bp">@</span><span class="n">normed_ring</span><span class="bp">.</span><span class="n">to_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">normed_field</span><span class="bp">.</span><span class="n">to_normed_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span><span class="o">))))</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">has_one</span><span class="bp">.</span><span class="n">one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">zero_ne_one_class</span><span class="bp">.</span><span class="n">to_has_one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">domain</span><span class="bp">.</span><span class="n">to_zero_ne_one_class</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">domain</span><span class="o">)))))</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_one</span><span class="bp">.</span><span class="n">one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">monoid</span><span class="bp">.</span><span class="n">to_has_one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">semiring</span><span class="bp">.</span><span class="n">to_monoid</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">ordered_semiring</span><span class="bp">.</span><span class="n">to_semiring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
                <span class="o">(</span><span class="bp">@</span><span class="n">linear_ordered_semiring</span><span class="bp">.</span><span class="n">to_ordered_semiring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">linear_ordered_semiring</span><span class="o">)))))</span>
</pre></div>


<p>while the "right" instance is the much nicer </p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="n">has_le</span><span class="bp">.</span><span class="n">le</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">has_le</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_inv</span><span class="bp">.</span><span class="n">inv</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">division_ring</span><span class="bp">.</span><span class="n">to_has_inv</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">division_ring</span><span class="o">)</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">bit0</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">distrib</span><span class="bp">.</span><span class="n">to_has_add</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">ring</span><span class="bp">.</span><span class="n">to_distrib</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
                <span class="o">(</span><span class="bp">@</span><span class="n">normed_ring</span><span class="bp">.</span><span class="n">to_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">normed_field</span><span class="bp">.</span><span class="n">to_normed_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span><span class="o">))))</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">has_one</span><span class="bp">.</span><span class="n">one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">zero_ne_one_class</span><span class="bp">.</span><span class="n">to_has_one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">domain</span><span class="bp">.</span><span class="n">to_zero_ne_one_class</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">domain</span><span class="o">)))))</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_one</span><span class="bp">.</span><span class="n">one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">zero_ne_one_class</span><span class="bp">.</span><span class="n">to_has_one</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="o">(</span><span class="bp">@</span><span class="n">domain</span><span class="bp">.</span><span class="n">to_zero_ne_one_class</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">real</span> <span class="n">real</span><span class="bp">.</span><span class="n">domain</span><span class="o">)))</span>
</pre></div>

#### [ Rob Lewis (Dec 03 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150800863):
<p>Something in <code>norm_num</code>, either in C++ or in mathlib, is creating some metavars and leaving them uninstantiated. Adding <code>e₂ ← instantiate_mvars e₂,</code> before the <code>guard</code> at <a href="https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L162" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L162">https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L162</a> allows <code>norm_num1</code> to kill the goal.</p>

#### [ Rob Lewis (Dec 03 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150800903):
<p>I haven't tracked down where the uninstantiated metavar is coming from yet.</p>

#### [ Luca Gerolla (Dec 03 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802454):
<p><a href="/user_uploads/3121/ux1kBLQGexv8qc9xmddMHxrJ/20180814_193304.jpg" target="_blank" title="20180814_193304.jpg">20180814_193304.jpg</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/ux1kBLQGexv8qc9xmddMHxrJ/20180814_193304.jpg" target="_blank" title="20180814_193304.jpg"><img src="/user_uploads/3121/ux1kBLQGexv8qc9xmddMHxrJ/20180814_193304.jpg"></a></div>

#### [ Luca Gerolla (Dec 03 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802460):
<p>I also  bumped into deterministic timeout few times when solving various inequality; the common situation was that I had goals involving some "variable" real number (i.e. not explicit - like the 'k' and 'l' in the example) and norm_num got in a loop (often involving 'one_div_eq_inv')</p>

#### [ Rob Lewis (Dec 03 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802866):
<p>Hmm. I think the C++ <code>norm_num</code> instantiates mvars as a side effect, but only sometimes. It doesn't do it when it when the term is already in normal form.</p>

#### [ Rob Lewis (Dec 03 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150802905):
<p>Simple fix: <code>e ← instantiate_mvars e,</code> at <code>norm_num.lean:468</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804050):
<p>468?</p>

#### [ Mario Carneiro (Dec 03 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804058):
<p><a href="https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L468" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L468">https://github.com/leanprover/mathlib/blob/master/tactic/norm_num.lean#L468</a></p>

#### [ Mario Carneiro (Dec 03 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804070):
<p>you mean before the <code>ext_simplify_core</code>?</p>

#### [ Patrick Massot (Dec 03 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804122):
<p>Booooo! Rob is not running up to date mathlib</p>

#### [ Mario Carneiro (Dec 03 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804158):
<p>lol, you don't want to know what I'm running</p>

#### [ Rob Lewis (Dec 03 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804210):
<p>Nope, the argument to <code>derive</code> should be instantiated before you do anything with it.</p>

#### [ Rob Lewis (Dec 03 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804221):
<p>So make that the first line of the <code>do</code> block.</p>

#### [ Mario Carneiro (Dec 03 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804240):
<p>why not 471/472? that's the first place after calling C <code>norm_num</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804287):
<p>or is the problem uninstantiated metavars in the user input</p>

#### [ Rob Lewis (Dec 03 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804363):
<p>Yeah, exactly. At some point you compare the input with something that went through the C++ <code>norm_num</code>. The former has mvars, the latter doesn't.</p>

#### [ Mario Carneiro (Dec 03 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804500):
<p>we could just check for unify instead of alpha equivalent</p>

#### [ Mario Carneiro (Dec 03 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804591):
<p>eh, I guess that doesn't make sense here</p>

#### [ Mario Carneiro (Dec 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150804644):
<p>yeah okay, ship it</p>

#### [ Kenny Lau (Dec 03 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150805046):
<p>ship who?</p>

#### [ Mario Carneiro (Dec 04 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num/near/150809032):
<p>Not sure if this is a serious question, but this is an international forum, so... <a href="https://english.stackexchange.com/questions/48443/meaning-of-ship-it" target="_blank" title="https://english.stackexchange.com/questions/48443/meaning-of-ship-it">ship it</a></p>


{% endraw %}
