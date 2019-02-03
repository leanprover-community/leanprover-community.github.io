---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18193extensions.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [extensions](https://leanprover-community.github.io/archive/116395maths/18193extensions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 16 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772133):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  At <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean#L841-L843" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean#L841-L843">https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean#L841-L843</a> do we really need that <code>[inhabited γ]</code>? It forces lots of other inhabited assumptions that seem unnecessary from a mathematical point of view. If γ is not inhabited then there shouldn't be that many <code>f : α → γ</code> to care about</p>

#### [ Mario Carneiro (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772434):
<p>the inhabited is needed for <code>lim</code></p>

#### [ Mario Carneiro (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772460):
<p>because it takes a default value when the limit is not defined</p>

#### [ Patrick Massot (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772463):
<p>I understand this</p>

#### [ Patrick Massot (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772485):
<p>But one could hope for a definition not using <code>lim</code> then</p>

#### [ Mario Carneiro (Jul 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772566):
<p>I recall puzzling over this definition a while ago; I also don't particularly like this style of definition</p>

#### [ Mario Carneiro (Jul 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772584):
<p>it seems like we should already know that the limit is defined at this point</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772750):
<p>I guess we need the assumption of <code>continuous_ext</code> to know the definition makes sense</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772839):
<blockquote>
<p>It forces lots of other inhabited assumptions that seem unnecessary from a mathematical point of view. </p>
</blockquote>
<p>Do you have any particular examples?</p>

#### [ Patrick Massot (Jul 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772871):
<p>Why? <code>ext de</code> is a function from <code>α → γ</code> to <code>β → γ</code>. Can't Lean be happy if both are uninhabited types and we don't write anything about the definition?</p>

#### [ Patrick Massot (Jul 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772922):
<p>Examples are in my work in progress in the perfectoid project. I'm working on Hausdorff completions of uniform spaces.</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772943):
<p>i mean maybe there is a way to pick an inhabitant in your setting</p>

#### [ Patrick Massot (Jul 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772945):
<p>The completion functor, which is left-adjoint to the inclusion of Hausdorff and complete uniform spaces into all uniform spaces, is constructed on homs by extension</p>

#### [ Patrick Massot (Jul 16 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772974):
<p>If I assume the starting uniform space is inhabited then its completion is also inhabited, no problem. But it mean I keep assuming spaces are inhabited</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773022):
<p>No, I mean somehow argue the empty case so it's not needed</p>

#### [ Patrick Massot (Jul 16 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773058):
<p>If this is possible there, why isn't possible right in the definition of <code>dense_embedding.ext</code></p>

#### [ Patrick Massot (Jul 16 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773067):
<p>(by the way, this name is confusion since it has nothing to do with extensionality)</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773120):
<p>Agreed. Do you have a suggestion?</p>

#### [ Patrick Massot (Jul 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773129):
<p>about the name?</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773131):
<p>yes</p>

#### [ Patrick Massot (Jul 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773136):
<p><code>dense_embedding.extension</code> maybe?</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773533):
<p>I managed this definition:</p>
<div class="codehilite"><pre><span></span>def extend (de : dense_embedding e) (f : α → γ) (b : β) : γ :=
have nonempty γ, from
let ⟨_, ⟨_, a, _⟩⟩ := exists_mem_of_ne_empty
  (mem_closure_iff.1 (de.dense b) _ is_open_univ trivial) in ⟨f a⟩,
@lim _ (classical.inhabited_of_nonempty this) _ (map f (vmap e (nhds b)))
</pre></div>

#### [ Patrick Massot (Jul 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773551):
<p>Scary! But I don't mind being scared by the definition: can you prove the expected properties?</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773631):
<p>It's mostly just a proof getting stuck into the <code>inhabited γ</code> slot - it doesn't change any of the proofs</p>

#### [ Mario Carneiro (Jul 16 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773686):
<p>all the proofs immediately after the definition still work, I may have to hunt down other uses</p>

#### [ Patrick Massot (Jul 16 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773914):
<p>and also hunt down the inhabited assumptions</p>


{% endraw %}
