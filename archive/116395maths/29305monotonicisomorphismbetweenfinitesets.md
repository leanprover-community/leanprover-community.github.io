---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29305monotonicisomorphismbetweenfinitesets.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [monotonic isomorphism between finite sets](https://leanprover-community.github.io/archive/116395maths/29305monotonicisomorphismbetweenfinitesets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Aug 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132370926):
<p>I'm looking for a lexicographic total order on <code>fin a × fin b</code> and a proof that's it's isomorphic to the lexicographic total order on <code>fin b × fin a</code>. Is this easy in lean?</p>

#### [ Chris Hughes (Aug 18 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132372379):
<p>No longer needed</p>

#### [ Chris Hughes (Aug 21 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132508918):
<p>Turns out I do need it after all. I need a linear order isomorphism between any two totally ordered types of the same size. Is that anywhere in lean? Seems like the sort of thing that might have come up doing ordinals.</p>

#### [ Johan Commelin (Aug 21 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132509200):
<p>I have no idea whether this is in Lean. Also, I'm not a master of finsets, like you are. But my initial attempt would be to prove this by induction. Construct a map to <code>fin n</code>. If the cardinality is <code>0</code>, then it's easy. If it is <code>k+1</code> construct a map to <code>fin k+1</code> by sending the largest element to <code>k</code>.</p>

#### [ Johan Commelin (Aug 21 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132509490):
<p>Do you in fact also want to prove that the linear order isom is unique?</p>

#### [ Chris Hughes (Aug 21 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132509662):
<p>I don't care if it's unique I don't think.</p>

#### [ Mario Carneiro (Aug 21 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512403):
<blockquote>
<p>I need a linear order isomorphism between any two totally ordered types of the same size</p>
</blockquote>
<p>This isn't true for all types, e.g. nat and int are not order isomorphic</p>

#### [ Mario Carneiro (Aug 21 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512417):
<p>This fact for finite linear orders is a special case of the uniqueness of well orders in the finite case</p>

#### [ Kevin Buzzard (Aug 21 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512622):
<p>He's only interested in finite types surely</p>

#### [ Chris Hughes (Aug 21 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512913):
<p>I do mean finite</p>

#### [ Kevin Buzzard (Aug 21 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513119):
<p>So the question is "is existence and uniqueness (up to permutation) of a total order on a finite type in Lean"?</p>

#### [ Mario Carneiro (Aug 21 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513204):
<p><code>ord n</code> essentially imposes a well order on any set (or the well order theorem directly), which gives you the existence part</p>

#### [ Chris Hughes (Aug 21 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513255):
<p>The uniqueness is what I care about.</p>

#### [ Mario Carneiro (Aug 21 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513564):
<p>A linear order of a finite set is a well order, so you get an embedding of each order into <code>ordinal</code>; the cardinals for these orders is equal so you have uniqueness by <code>ord_nat</code> and hence an order isomorphism</p>

#### [ Mario Carneiro (Aug 21 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513571):
<p>(this is probably an excessively high powered proof)</p>

#### [ Kenny Lau (Aug 21 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514251):
<p>I'm still struggling with something like</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">something</span> <span class="o">:</span> <span class="bp">@</span><span class="n">order_iso</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="err">$</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="err">$</span> <span class="n">ordinal</span><span class="bp">.</span><span class="n">type_eq</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="o">(</span><span class="n">ordinal</span><span class="bp">.</span><span class="n">fintype_card</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">))</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">ordinal</span><span class="bp">.</span><span class="n">lift_type_fin</span> <span class="err">$</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>

#### [ Kenny Lau (Aug 21 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514255):
<p>(I hadn't read the messages by Mario)</p>

#### [ Kenny Lau (Aug 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514599):
<p>oh and my incomplete code (posting here because I don't want to work with it now):</p>

#### [ Kenny Lau (Aug 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514602):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">ordinal</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">linear_order</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">has_lt</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">is_well_order</span> <span class="n">β</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">is_well_order_of_fintype</span> <span class="o">:</span> <span class="n">is_well_order</span> <span class="n">α</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">wf</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">ulift_up_eq</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ulift</span><span class="bp">.</span><span class="n">up</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">ulift</span><span class="bp">.</span><span class="n">up</span> <span class="n">y</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">ulift</span><span class="bp">.</span><span class="n">up</span><span class="bp">.</span><span class="n">inj</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="bp">_⟩</span>

<span class="kn">instance</span> <span class="n">ulift</span><span class="bp">.</span><span class="n">is_well_order</span> <span class="o">:</span> <span class="n">is_well_order</span> <span class="o">(</span><span class="n">ulift</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">to_fun</span> <span class="bp">⁻¹</span><span class="err">&#39;</span><span class="n">o</span> <span class="n">has_lt</span><span class="bp">.</span><span class="n">lt</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">z</span><span class="bp">⟩</span> <span class="n">Hxy</span> <span class="n">Hyz</span><span class="o">,</span> <span class="bp">@</span><span class="n">is_trans</span><span class="bp">.</span><span class="n">trans</span> <span class="n">β</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="bp">_</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">Hxy</span> <span class="n">Hyz</span><span class="o">,</span>
  <span class="n">irrefl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">⟩</span> <span class="n">H</span><span class="o">,</span> <span class="n">is_irrefl</span><span class="bp">.</span><span class="n">irrefl</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">trichotomous</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">is_trichotomous</span><span class="bp">.</span><span class="n">trichotomous</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">wf</span> <span class="o">:=</span> <span class="n">inv_image</span><span class="bp">.</span><span class="n">wf</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">is_well_order</span><span class="bp">.</span><span class="n">wf</span> <span class="bp">_</span> <span class="o">}</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">something</span> <span class="o">:</span> <span class="bp">@</span><span class="n">order_iso</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="err">$</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="err">$</span> <span class="n">ordinal</span><span class="bp">.</span><span class="n">type_eq</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="o">(</span><span class="n">ordinal</span><span class="bp">.</span><span class="n">fintype_card</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">))</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">ordinal</span><span class="bp">.</span><span class="n">lift_type_fin</span> <span class="err">$</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">ord_nat</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">something</span>
</pre></div>


{% endraw %}
