---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08268noncomputabletheorem.html
---

## Stream: [general](index.html)
### Topic: [noncomputable theorem](08268noncomputabletheorem.html)

---


{% raw %}
#### [ Reid Barton (Oct 19 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136123067):
<p>Is there any sense in writing <code>noncomputable theorem</code>, as in mathlib <code>logic.basic</code> lines 516-519?</p>

#### [ Simon Hudon (Oct 19 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136124051):
<p>What happens if you remove <code>noncomputable</code>?</p>

#### [ Reid Barton (Oct 19 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136124347):
<p>Probably I wait a long time for mathlib to rebuild and then nothing interesting happens--I've written lots of <code>theorem</code>s that use noncomputable things before.</p>

#### [ Reid Barton (Oct 19 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136124359):
<p>I wonder whether they should be <code>noncomputable def</code>, or just <code>theorem</code>, or maybe none of this matters</p>

#### [ Reid Barton (Oct 19 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136124519):
<p>Actually I could be wrong--these <code>theorem</code>s are special because their result types are not Props (that's why I'm looking at them), and maybe that is what triggers the <code>noncomputable</code> check</p>

#### [ Reid Barton (Oct 19 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136124688):
<p>Okay yes, that seems to be the case.</p>

#### [ Reid Barton (Oct 19 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136125141):
<p>I never thought about exactly what is going on with <code>def</code> and <code>theorem</code>. I guess the difference is like <code>let</code> vs <code>have</code>, that is, something defined with <code>def</code> can be replaced by its definition by one of the reduction rules, while something defined with <code>theorem</code> can't be replaced by, well, its proof?</p>

#### [ Reid Barton (Oct 19 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136125354):
<p>The VM can't reduce a <code>theorem</code> either, right? So why bother with the <code>noncomputable</code> check for theorems?</p>

#### [ Reid Barton (Oct 19 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136125488):
<p>In the case of <code>classical.dec</code> I guess someone decided that it was useless to allow it to be unfolded because it's essentially just an application of an axiom, and it's uniquely determined up to propositional equality, anyways?</p>

#### [ Reid Barton (Oct 19 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136125590):
<p>This all seems to make sense, I'm just not sure my mental picture is actually correct.</p>

#### [ Simon Hudon (Oct 19 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136129728):
<p>I'm wondering if it's about generating byte code for the VM. If the theorem's type is in <code>Prop</code>, then, it doesn't matter.</p>

#### [ Simon Hudon (Oct 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136129843):
<p>But otherwise, you may have to say explicitly "Don't generate code" with <code>noncomputable</code></p>

#### [ Mario Carneiro (Oct 20 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136143543):
<p>If you mark something as <em>either</em> <code>noncomputable</code> or <code>theorem</code>, then the VM does not generate code for the definition. This is why sometimes you get those errors about bytecode generation failed when you accidentally mark something as a <code>theorem</code></p>

#### [ Mario Carneiro (Oct 20 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136143755):
<p><code>noncomputable theorem</code> is almost always not needed, but it is used in a few specialized instances. One other consequence of defining something as a <code>theorem</code> is that it is "definition irrelevant", that is, lean will not generate or use the definitional equation for this definition. This is almost never appropriate for a <code>Type</code> valued expression, since it provides relations between definiendum and definiens that we can't otherwise recover. So the place where it makes sense is when the definition is already ambiguous, as in <code>classical.some</code> - unfolding it will not tell us any more about its value - and it is also using the axiom of choice so it should not have any code generation.</p>

#### [ Mario Carneiro (Oct 20 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable%20theorem/near/136143757):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span></p>


{% endraw %}
