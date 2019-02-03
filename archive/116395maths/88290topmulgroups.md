---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88290topmulgroups.html
---

## Stream: [maths](index.html)
### Topic: [top mul groups](88290topmulgroups.html)

---


{% raw %}
#### [ Patrick Massot (Oct 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135306917):
<p>Am I blind or is the definition of multiplicative topological groups is missing in mathlib?</p>

#### [ Patrick Massot (Oct 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135306924):
<p>And nothing about topological groups uses the <code>to_additive</code> machine?</p>

#### [ Kevin Buzzard (Oct 06 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135307033):
<p>Maybe edit core Lean and redefine the notation for <code>+</code> to be <code>mul</code>?</p>

#### [ Kevin Buzzard (Oct 06 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135307076):
<p>You might well be right though. With groups I went through a phase of confusing <code>group</code> and <code>add_group</code> but I've never had the same confusion for topological groups.</p>

#### [ Patrick Massot (Oct 06 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135307084):
<p>I think I'll stick to additive group, and try to make progress on rings. Then someone will have to do a huge refactor of all this mess</p>

#### [ Patrick Massot (Oct 06 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135312988):
<p>Also, as I suspected, Lean doesn't want to hear that a ring quotiented by an ideal has anything to do with a add_comm_group quotiented by a subgroup. After proving addition is continuous when you quotient a commutative topological group by a subgroup, you cannot get continuity of addition when you quotient a ring by an ideal. This is a bit sad</p>

#### [ Patrick Massot (Oct 06 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135312998):
<p>Even after I wrote:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">module</span> <span class="n">α</span> <span class="n">M</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_submodule</span> <span class="n">N</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">submodule_is_add_subgroup</span> <span class="o">:</span> <span class="n">is_add_subgroup</span> <span class="n">N</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">zero_mem</span> <span class="o">:=</span>  <span class="n">is_submodule</span><span class="bp">.</span><span class="n">zero</span><span class="o">,</span>
  <span class="n">add_mem</span> <span class="o">:=</span>  <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">is_submodule</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="n">neg_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span>  <span class="n">is_submodule</span><span class="bp">.</span><span class="n">neg</span><span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 06 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313204):
<p>Is that because quotients of modules is not done via quotients of add_groups?</p>

#### [ Patrick Massot (Oct 06 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313213):
<p>yes</p>

#### [ Patrick Massot (Oct 06 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313269):
<p><a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L22" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L22">https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L22</a><br>
<a href="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L145" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L145">https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L145</a><br>
No link</p>

#### [ Johan Commelin (Oct 06 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313316):
<p>I've heard rumors that there are plans to fix this in mathlib 5.2</p>

#### [ Patrick Massot (Oct 06 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135313425):
<p><span class="emoji emoji-1f615" title="oh no">:oh_no:</span> I try to copy-paste proofs but <a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L49" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L49">https://github.com/leanprover/mathlib/blob/master/linear_algebra/quotient_module.lean#L49</a> and <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L193" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L193">https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L193</a> are not compatible <span class="emoji emoji-2639" title="sad">:sad:</span> <span class="emoji emoji-2639" title="sad">:sad:</span> <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Patrick Massot (Oct 06 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135314044):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I just pushed <a href="https://github.com/leanprover-community/mathlib/commit/981ed82f657f49b4f276457de398b9c33af05d54" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/981ed82f657f49b4f276457de398b9c33af05d54">https://github.com/leanprover-community/mathlib/commit/981ed82f657f49b4f276457de398b9c33af05d54</a> It's a mess with a lot of duplication and brute force but it should allow me to continue working on completions of topological rings. Of course I'd be grateful if you can refactor it, but I expect it would be quite a bit of work because <code>topological_structures.lean</code> does not use at all the <code>to_additive</code> machine, and module quotients are unrelated to additive group quotients.</p>

#### [ Patrick Massot (Oct 06 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135314056):
<p>To be clear: currently I need only the ring part of that commit (and the open map things of course) but I let the group and add_comm_group part in order to highlight the refactoring issue</p>

#### [ Patrick Massot (Oct 06 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135318258):
<p>And again it fails because we have multiple instances on the same type, see <a href="https://github.com/leanprover-community/mathlib/commit/125efed6aac2f44d8d466b001c655dd04ebd5fb0" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/125efed6aac2f44d8d466b001c655dd04ebd5fb0">https://github.com/leanprover-community/mathlib/commit/125efed6aac2f44d8d466b001c655dd04ebd5fb0</a> I give up for today since I won't be there after dinner. <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> you can have a look if you want. The issue is go back and forth between the separation quotient of a topological ring seen from the purely uniform space point of view and from the quotient ring point of view. It seems Lean doesn't accept they correspond to the same topology, although both are defeq to a quotient topology and I have a lemma stating the two setoid are equals.</p>

#### [ Johannes Hölzl (Oct 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135619845):
<p>I added a commit in <code>lc\completions</code> s.t. <code>topological_structures</code> uses <code>to_additive</code> (at least for <code>topological_add_monoid</code> and <code>topological_add_group</code>)</p>

#### [ Patrick Massot (Oct 11 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135625411):
<p>Thanks!</p>

#### [ Patrick Massot (Oct 11 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top%20mul%20groups/near/135625428):
<p>And thanks for working on this branch again</p>


{% endraw %}
