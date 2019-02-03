---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64685Normalsubmonoids.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Normal submonoids](https://leanprover-community.github.io/archive/116395maths/64685Normalsubmonoids.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131229964):
<p>Are these a thing? The natural definition of normal subgroup extends to the monoid case as <code>a + b \in S -&gt; b + a \in S</code></p>

#### [ Johan Commelin (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131229974):
<p>Do we need them anywhere?</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131229977):
<p>not particularly</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230045):
<p>Do we need normal subgroups?</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230056):
<p>I guess the answer is about the same</p>

#### [ Johan Commelin (Aug 10 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230120):
<p>Well... I think the will be used quite a lot.</p>

#### [ Johan Commelin (Aug 10 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230124):
<p>Isn't Kevin already using them?</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230139):
<p>I'm working on porting the add_subgroup stuff now... I don't really get why we care about noncommutative additive groups</p>

#### [ Johan Commelin (Aug 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230230):
<p>We don't care about those.</p>

#### [ Johan Commelin (Aug 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230284):
<p>We just want the additive subgroups, so that we can have subrings.</p>

#### [ Kenny Lau (Aug 10 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230305):
<p>subrings not</p>

#### [ Johan Commelin (Aug 10 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230317):
<p>And this seemed like a very straightforward translation exercise, which I performed without thinking about whether some lines could be removed...</p>

#### [ Kevin Buzzard (Aug 10 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131234329):
<p>Normal subgroups are used all over the place in maths, they're exactly the kernels of morphisms in the category of groups. I thought a bit recently about why we would care about noncommutative additive groups, and the only half-decent answer I could come up with is that there is at least one example in maths where people use addition as a standard notation and it's not commutative, namely addition of ordinals (not that anyone outside of logic ever uses ordinals anyway). These do not form a group though. In number theory there is an implicit assumption that addition is commutative.</p>
<p>I am only using normal subgroups in the additive case and only in the situation where addition is commutative, so they're the same as subgroups. My only use case was that I need some lemmas about quotient rings, and I thought that the "correct" way to prove that a map R -&gt; S whose kernel contains I induced a map R/I -&gt; S would be to first construct the map using some universal property of quotient abelian groups and then to show it's a ring homomorphism. But I don't know whether I'm fussing over nothing and should just prove it directly. </p>
<p>Didn't Chris make a quotient group PR recently? I was going to make one and then Chris told me he'd made one so I shouldn't PR because of potential conflicts.</p>
<p><a href="https://github.com/leanprover/mathlib/pull/212" target="_blank" title="https://github.com/leanprover/mathlib/pull/212">https://github.com/leanprover/mathlib/pull/212</a></p>

#### [ Mario Carneiro (Aug 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131234411):
<p>oops</p>

#### [ Andreas Swerdlow (Aug 10 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131842627):
<p>I did some basic subring and subfield stuff here <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean</a>. Is this useful at all, or should it be linked to existing stuff in mathlib?</p>

#### [ Reid Barton (Aug 11 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131849326):
<blockquote>
<p>Normal subgroups are used all over the place in maths, they're exactly the kernels of morphisms in the category of groups.</p>
</blockquote>
<p>And groups are special because the equivalence relation induced by a surjection (<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∼</mo><mi>y</mi></mrow><annotation encoding="application/x-tex">x \sim y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∼</span><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span> if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">f(x) = f(y)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span></span></span></span>) is determined by the equivalence class of 0, i.e., the kernel. For general monoids, knowing the kernel of a map doesn't tell you about the behavior of the map away from 0 (consider the quotient of <code>nat</code> which identifies all the numbers greater than or equal to 3).<br>
So, I don't think normal submonoids are of much interest.</p>

#### [ Scott Morrison (Aug 11 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852250):
<p><span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span>, looks useful to me. How about you PR it?</p>

#### [ Scott Morrison (Aug 11 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852257):
<p>It might be worth doing a little renaming to get the functions as close as possible to following the pattern in <code>mathlib/group_theory/subgroup.lean</code>.</p>

#### [ Scott Morrison (Aug 11 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852369):
<p>I'm not entirely certainly where to put what you've written. My suggestion would be to be ambitious, and split it into two parts, putting them in <code>ring_theory/subring.lean</code> and <code>field_theory/subfield.lean</code>, parallel to the group situation: eventually we're going to need a fair bit of other stuff in both those directories. (Although <code>field_theory</code> sounds very wrong...)</p>

#### [ Scott Morrison (Aug 11 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852441):
<p>Probably it's best to create a new branch at &lt;<a href="https://github.com/leanprover-community/mathlib" target="_blank" title="https://github.com/leanprover-community/mathlib">https://github.com/leanprover-community/mathlib</a>&gt;, so others can look at it first (announce here you want help?) and then once it's been tweaked a bit we can PR it to the official mathlib.</p>

#### [ Scott Morrison (Aug 11 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852498):
<p>(If you don't have commit access at leanprover-community, either ask here for it, or just do the work in your own fork of mathlib and send a PR to leanprover-community, and announce here and somewhere will merge it to a branch.)</p>

#### [ Johan Commelin (Aug 11 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131937828):
<blockquote>
<p>I did some basic subring and subfield stuff here <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean</a>. Is this useful at all, or should it be linked to existing stuff in mathlib?</p>
</blockquote>
<p>Hi <span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span> Additive subgroups have just been put into mathlib: <a href="https://github.com/leanprover/mathlib/blob/0f42b279865753eb3c79f3504783c7dbd81dfc7e/group_theory/subgroup.lean#L25" target="_blank" title="https://github.com/leanprover/mathlib/blob/0f42b279865753eb3c79f3504783c7dbd81dfc7e/group_theory/subgroup.lean#L25">https://github.com/leanprover/mathlib/blob/0f42b279865753eb3c79f3504783c7dbd81dfc7e/group_theory/subgroup.lean#L25</a>. I think that it is useful if Lean knows that every subring is also an additive subgroup. Some time ago I wrote <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean#L13" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean#L13">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean#L13</a>, but there is nothing about fields in that file. I think a merge of your and my approach would be best.</p>

#### [ Andreas Swerdlow (Aug 13 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/132038273):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span>  thanks for the help. I've rewritten the subfield part, so that it builds off of what Johan wrote for subrings, and created a fork of leanprover-community/mathlib with both Johan's subring file in ring_theory/subring.lean and the subfield stuff in field_theory/subfield.lean. The fork is here: <a href="https://github.com/amswerdlow/mathlib" target="_blank" title="https://github.com/amswerdlow/mathlib">https://github.com/amswerdlow/mathlib</a>. Any suggestions are welcome before I PR</p>


{% endraw %}
