---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97486trolledbyundergrad.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [trolled by undergrad](https://leanprover-community.github.io/archive/113488general/97486trolledbyundergrad.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 20 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130014811):
<p>It took me 20 minutes to diagnose this deterministic time-out:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="kn">theorem</span> <span class="n">infinite_cover</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">ℝ</span><span class="o">)}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="n">k</span> <span class="bp">≤</span> <span class="n">n</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">c&#39;</span> <span class="err">⊆</span> <span class="n">c</span><span class="o">,</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">a</span><span class="bp">+</span><span class="o">(</span><span class="n">k</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="bp">/</span><span class="n">n</span> <span class="bp">≤</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">a</span><span class="bp">+</span><span class="n">k</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="bp">/</span><span class="n">n</span><span class="o">}</span> <span class="err">⊆</span> <span class="err">⋃₀</span> <span class="n">c&#39;</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">c&#39;</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>In my defence, the code was far longer to begin with, and probably about 15 were spent reducing it to this.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015487):
<p>I'm about to set off for home and I'll spill the beans if nobody has spotted it by the time I get in</p>

#### [ Patrick Massot (Jul 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015541):
<p>I don't understand what you are asking for</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015604):
<p>Cut and paste that code -- it times out</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015613):
<p>deterministic time-out</p>

#### [ Chris Hughes (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015615):
<p><code>1 ≤ k ≤ n</code></p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015618):
<p>:-)</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015625):
<p>I spotted it when I changed <code>n</code> to <code>1</code></p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015658):
<p>I was quite surprised that the statement managed to parse</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015659):
<p>in retrospect</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015677):
<p>because obviously <code>k ≤ n</code> is also a nat</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015719):
<p>bigger than one no less</p>

#### [ Chris Hughes (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015737):
<p>is <code>≤</code> left or right associative?</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016247):
<p>left assoc, my bad</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016271):
<div class="codehilite"><pre><span></span>infix ≤        := has_le.le
</pre></div>


<p><code>infix</code> means <code>infixl</code></p>

#### [ Mario Carneiro (Jul 20 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016335):
<p>oh I see so it tried to find a Prop coercion for <code>n</code></p>

#### [ Mario Carneiro (Jul 20 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016351):
<p>and then it means "if <code>1 &lt;= k</code> then <code>n</code>"</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016440):
<p><code>1 ≤ k ≤ (n ≤ 1)</code> parses just fine</p>

#### [ Chris Hughes (Jul 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016450):
<p>Because Prop has an order structure for some reason.</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016464):
<p>because Prop has a natural order structure...</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016479):
<p>which we use funky notation for</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016545):
<p>In fact I'm pretty sure boolean algebras are basically generalized Prop</p>

#### [ Mario Carneiro (Jul 21 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130035267):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I just noticed that this error is a bit subtler than expected. It doesn't give a instance overflow error, it times out and produces no output in the trace. Do you know how the typeclass instance mechanism could run out of time without overflowing?</p>

#### [ Mario Carneiro (Jul 21 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130035317):
<p>example without trolling:</p>
<div class="codehilite"><pre><span></span>import analysis.real
example (n : ℕ) : Prop := n
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130036027):
<p>Ah, I finally got an instance trace, and it does something I didn't think the typeclass inference engine does: it repeatedly does the same search, at the same depth level, which is why it timeouts from iteration rather than recursion. Here's the beginning, with the depth shown using indentation:</p>
<div class="codehilite"><pre><span></span>(0) ?x_3 : has_coe_to_sort ℕ := @coe_sort_trans ?x_5 ?x_6 ?x_7 ?x_8
 (1) ?x_7 : has_coe_t_aux ℕ ?x_6 := @coe_base_aux ?x_9 ?x_10 ?x_11
  (2) ?x_11 : has_coe ℕ ?x_10 := int.has_coe
 (1) ?x_8 : has_coe_to_sort ℤ := @coe_sort_trans ?x_22 ?x_23 ?x_24 ?x_25
  (2) ?x_24 : has_coe_t_aux ℤ ?x_23 := @coe_base_aux ?x_26 ?x_27 ?x_28
   (3) ?x_28 : has_coe ℤ ?x_27 := @int.cast_coe ?x_49 ?x_50 ?x_51 ?x_52 ?x_53
    (4) ?x_50 : has_zero ?x_49 := real.has_zero
    (4) ?x_51 : has_one ℝ := real.has_one
    (4) ?x_52 : has_add ℝ := real.has_add
    (4) ?x_53 : has_neg ℝ := real.has_neg
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_55 ?x_56 ?x_57 ?x_58
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_base_aux ?x_59 ?x_60 ?x_61
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_trans_aux ?x_59 ?x_60 ?x_61 ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @lattice.boolean_algebra.to_has_neg ?x_60 ?x_61
     (5) ?x_61 : lattice.boolean_algebra ℝ := @lattice.complete_boolean_algebra.to_boolean_algebra ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @add_group.to_has_neg ?x_55 ?x_56
     (5) ?x_56 : add_group ℝ := real.add_group
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_58 ?x_59 ?x_60 ?x_61
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_base_aux ?x_62 ?x_63 ?x_64
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_trans_aux ?x_62 ?x_63 ?x_64 ?x_65 ?x_66
     (5) ?x_56 : add_group ℝ := @add_comm_group.to_add_group ?x_59 ?x_60
      (6) ?x_60 : add_comm_group ℝ := real.add_comm_group
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_62 ?x_63 ?x_64 ?x_65
   (3) ?x_64 : has_coe_t_aux ℝ ?x_63 := @coe_base_aux ?x_66 ?x_67 ?x_68
   (3) ?x_64 : has_coe_t_aux ℝ ?x_63 := @coe_trans_aux ?x_66 ?x_67 ?x_68 ?x_69 ?x_70
      (6) ?x_60 : add_comm_group ℝ := @nonneg_comm_group.to_add_comm_group ?x_61 ?x_62
       (7) ?x_62 : nonneg_comm_group ℝ := @linear_nonneg_ring.to_nonneg_comm_group ?x_63 ?x_64
       (7) ?x_62 : nonneg_comm_group ℝ := @nonneg_ring.to_nonneg_comm_group ?x_63 ?x_64
        (8) ?x_64 : nonneg_ring ℝ := @linear_nonneg_ring.to_nonneg_ring ?x_65 ?x_66
      (6) ?x_60 : add_comm_group ℝ := @ring.to_add_comm_group ?x_63 ?x_64
       (7) ?x_64 : ring ℝ := real.ring
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_66 ?x_67 ?x_68 ?x_69
   (3) ?x_68 : has_coe_t_aux ℝ ?x_67 := @coe_base_aux ?x_70 ?x_71 ?x_72
   (3) ?x_68 : has_coe_t_aux ℝ ?x_67 := @coe_trans_aux ?x_70 ?x_71 ?x_72 ?x_73 ?x_74
       (7) ?x_64 : ring ℝ := @nonneg_ring.to_ring ?x_71 ?x_72
        (8) ?x_72 : nonneg_ring ℝ := @linear_nonneg_ring.to_nonneg_ring ?x_73 ?x_74
       (7) ?x_64 : ring ℝ := @domain.to_ring ?x_65 ?x_66
        (8) ?x_66 : domain ℝ := real.domain
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130036032):
<p>notice that <code>(2) ?x_25 : has_coe_to_sort ℝ</code> keeps coming up; this continues for all 38000 lines of output before it times out</p>

#### [ Mario Carneiro (Jul 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130037002):
<p>Oh whoa I just figured out why this is happening, and why it's called a "prolog-like search" - nota bene <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  :)</p>
<p>Whenever it tries something which doesn't work, it reverts all the metavariable assignments up to that point and then tries again. Like here around the newline:</p>
<div class="codehilite"><pre><span></span>  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_55 ?x_56 ?x_57 ?x_58
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_base_aux ?x_59 ?x_60 ?x_61
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_trans_aux ?x_59 ?x_60 ?x_61 ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @lattice.boolean_algebra.to_has_neg ?x_60 ?x_61
     (5) ?x_61 : lattice.boolean_algebra ℝ := @lattice.complete_boolean_algebra.to_boolean_algebra ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @add_group.to_has_neg ?x_55 ?x_56
     (5) ?x_56 : add_group ℝ := real.add_group

  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_58 ?x_59 ?x_60 ?x_61
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_base_aux ?x_62 ?x_63 ?x_64
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_trans_aux ?x_62 ?x_63 ?x_64 ?x_65 ?x_66
     (5) ?x_56 : add_group ℝ := @add_comm_group.to_add_group ?x_59 ?x_60
      (6) ?x_60 : add_comm_group ℝ := real.add_comm_group
</pre></div>


<p>The line <code>(5) ?x_56 : add_group ℝ := real.add_group</code> is a failure, but it assigns a value to <code>?x_56</code> from the (2) line. So it rolls all the way back to the (2) line and replays the same assignments until it gets to the bad choice <code>real.add_group</code>, and tries something different, in this case <code>@add_comm_group.to_add_group ?x_59 ?x_60</code>.</p>

#### [ Mario Carneiro (Jul 21 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130037108):
<p>I wonder if typeclass search will change in lean 4. This seems like such a poor strategy I'm surprised it works as well as it does in mathlib. I know Leo thinks many things about lean 3 are fundamentally broken, and I wouldn't be surprised if this was on the list</p>

#### [ Sebastian Ullrich (Jul 21 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130044916):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> This is not how class inference should work, nor have I seen such a trace before. Class inference uses temporary mvars that can be unassigned individually. <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/type_context.cpp#L1405" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/type_context.cpp#L1405">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/type_context.cpp#L1405</a></p>

#### [ Mario Carneiro (Jul 21 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130044978):
<p>If you like I can make a mathlib-free example</p>

#### [ Sebastian Ullrich (Jul 21 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045083):
<p>That would be great, thanks</p>

#### [ Mario Carneiro (Jul 21 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045431):
<p>I think this should do the trick (WARNING: this brings VSCode to its knees due to quantity of output)</p>
<div class="codehilite"><pre><span></span>@[priority 0] instance cast_coe {α} [has_zero α] [has_one α] [has_add α] : has_coe ℕ α := ⟨λ _, 0⟩
constant R : Type
instance : has_zero R := sorry

set_option trace.class_instances true
example (n : ℕ) : Prop := n
</pre></div>


<p>The <code>constant R</code> is optional but gives the typeclass system something to fixate on rather than whatever random thing it finds first (usually <code>unsigned</code> for me on the init library and <code>real</code> when it is imported)</p>

#### [ Sebastian Ullrich (Jul 21 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045547):
<p>hmm</p>
<div class="codehilite"><pre><span></span>$ lean +3.4.1 scratch.lean |&amp; wc -l
381659
 $ lean +master scratch.lean |&amp; wc -l
3342
</pre></div>


<p>I guess Leo fixed it already :D</p>

#### [ Mario Carneiro (Jul 21 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045637):
<p>well... I'm glad it was fixed, although I'm still puzzled over the cause...</p>

#### [ Mario Carneiro (Jul 21 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046079):
<p>Oh, looking at the trace from that version, I noticed that it searches for <code>(1) ?x_7 : has_coe_to_sort ℤ</code> 2826 times (with 26000 lines in between, not counting failures) before finally getting to <code>(1) ?x_7 : has_coe_to_sort ℕ</code>, which is the same typeclass search it started with. So I think if I let it run long enough it <em>would</em> hit the recursion limit, it would just take an extremely long time to do so.</p>

#### [ Patrick Massot (Jul 21 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046129):
<p>Maybe it would be worth checking that it was not fixed by accident (since another modification could reinstate the bug), or at least add it to the test suite?</p>

#### [ Patrick Massot (Jul 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046199):
<p>Do you think the type class search could become more programmable for users? For instance we already saw that it would be nice to be able to tell it: whenever you're looking for <code>ring ?x_i</code> then you should give up on that branch.</p>

#### [ Mario Carneiro (Jul 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046200):
<p>I'm not sure how much I should care about this bug, since it has to do with lean performance on an unsuccessful typeclass search anyway</p>

#### [ Mario Carneiro (Jul 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046222):
<p>I think "negative instances" would be great, they could probably speed up the search a lot. I.e. <code>unsigned</code> is not a field, stop looking there</p>

#### [ Patrick Massot (Jul 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046225):
<p>Obviously I don't know either, this is far above my competences. My reaction is only triggered by Sebastian not knowing something has been fixed</p>

#### [ Mario Carneiro (Jul 21 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046264):
<p>but there is a lot of planning necessary to get a feature like that right</p>

#### [ Mario Carneiro (Jul 21 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046266):
<p>and obviously it's up to Sebastian and Leo to make that happen</p>

#### [ Mario Carneiro (Jul 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046275):
<p>so I will just let them ponder and figure out whatever works</p>

#### [ Patrick Massot (Jul 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046291):
<p>and soon Gabriel, according to Leo's talk</p>

#### [ Sebastian Ullrich (Jul 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046296):
<p>The type context will remain in C++, so it will not be arbitrarily configurable like other parts (hopefully will)</p>

#### [ Mario Carneiro (Jul 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046340):
<p>is typeclass search done in the type context?</p>

#### [ Patrick Massot (Jul 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046344):
<p>You could still let users pass options to the C++ code, couldn't you?</p>

#### [ Sebastian Ullrich (Jul 22 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103015):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Yes, it uses many type context internals. Still, reimplementing it on top of the new type context monad may be an interesting idea, now that I think about it.</p>

#### [ Sebastian Ullrich (Jul 22 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103045):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Sure, that's what I meant by "not arbitrarily". For the parts reimplemented in Lean, I'd like users to be able to completely replace the default implementations if they want to.</p>

#### [ Mario Carneiro (Jul 22 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103086):
<p>it would certainly be good if at least potential writing of the typeclass search could guide what of the type context gets exposed to lean</p>

#### [ Sebastian Ullrich (Jul 22 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103093):
<p>Yes, exactly</p>


{% endraw %}
