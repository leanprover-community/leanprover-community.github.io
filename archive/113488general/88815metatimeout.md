---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88815metatimeout.html
---

## Stream: [general](index.html)
### Topic: [meta timeout](88815metatimeout.html)

---


{% raw %}
#### [ Patrick Massot (Aug 13 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015530):
<p>I'm still playing with Lean introspection, but I can't sort declarations in order to print first axioms, then constants, then definition, and then theorems. I try</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">declaration_kind_nb</span> <span class="o">:</span> <span class="n">declaration</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ax</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnst</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">2</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">defn</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">3</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">thm</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">4</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">declaration_compare</span> <span class="o">(</span><span class="n">d</span> <span class="n">d&#39;</span> <span class="o">:</span> <span class="n">declaration</span><span class="o">)</span> <span class="o">:=</span> <span class="n">declaration_kind_nb</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">declaration_kind_nb</span> <span class="n">d&#39;</span>

<span class="n">meta</span> <span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_rel</span> <span class="n">declaration_compare</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">tauto</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">sort_env</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span>
   <span class="n">trace</span> <span class="o">((</span><span class="n">list</span><span class="bp">.</span><span class="n">merge_sort</span> <span class="n">declaration_compare</span> <span class="n">decls</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">to_string</span> <span class="err">∘</span> <span class="n">to_name</span><span class="o">))</span>
</pre></div>


<p>and get either determistic timeout or worse (excessive memory consumption, segfault...)</p>

#### [ Simon Hudon (Aug 13 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015764):
<p>What if you print only the length of the resulting list?</p>

#### [ Mario Carneiro (Aug 13 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015805):
<p>this works for me:</p>
<div class="codehilite"><pre><span></span>meta instance : decidable_rel declaration_compare :=
λ _ _, nat.decidable_le _ _

meta def sort_env : tactic unit :=
do curr_env ← get_env,
   let decls := curr_env.fold [] list.cons,
   (list.merge_sort declaration_compare decls).mmap&#39; (trace ∘ to_name)

run_cmd sort_env
</pre></div>

#### [ Mario Carneiro (Aug 13 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015812):
<p>the problem is that the format instance for <code>list string</code> involves a recursion, so it is very deeply nested and hits the recursion limit</p>

#### [ Mario Carneiro (Aug 13 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015817):
<p>(this is why TCO is important in functional programming languages)</p>

#### [ Patrick Massot (Aug 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015861):
<p>Thanks!</p>

#### [ Patrick Massot (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132015934):
<p>Is there a more natural way to do define that comparison function?</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132016013):
<p>Not particularly; you could do a cases on both and return true or false in each case</p>

#### [ Patrick Massot (Aug 13 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132016054):
<p>This was my original plan, but I decided there were too many cases</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132016068):
<p>this is a legitimate way to cut down the number of cases from O(n^2) to O(n)</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132016119):
<p>I wish there was a built in (autogenerated) <code>T.discr</code> function that returns the discriminant of the type, which is basically this</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20timeout/near/132016126):
<p>it has an O(1) implementation, since this is the tag on the vm object</p>


{% endraw %}
