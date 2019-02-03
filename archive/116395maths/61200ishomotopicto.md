---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61200ishomotopicto.html
---

## Stream: [maths](index.html)
### Topic: [is_homotopic_to](61200ishomotopicto.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 09 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131163659):
<p>I just saw this in <span class="user-mention" data-user-id="120726">@Luca Gerolla</span> 's code.</p>
<p><code>definition is_homotopic_to { x y : β } (f : path x y) ( g : path x y) : Prop := nonempty ( path_homotopy f g)</code></p>
<p>I feel like <code>is_homotopic_to</code> is an important concept and it sounds like a prop to me, but of course there might well be many homotopies between f and g. Is Luca unwise to use <code>nonempty</code> or is this exactly what he wants? I still feel very unsure about this kind of thing. Given an explicit homotopy from f to g and an explicit homotopy from g to h he will surely want an explicit homotopy from f to h, and of course he proves this, but...I think what I'm saying is that I am confused about both wanting a proposition and wanting to keep track of the homotopy at the same time.</p>

#### [ Reid Barton (Aug 09 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171197):
<p>You need both, I think. And here we do have both, since we also have <code>path_homotopy</code> itself.</p>

#### [ Reid Barton (Aug 09 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171234):
<p>What you don't want to do is define <code>is_homotopic_to</code> without <code>path_homotopy</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171736):
<p>I think you will want a quotient type over the is_homotopic_to relation</p>

#### [ Mario Carneiro (Aug 09 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171744):
<p>so the homotopy itself won't be in the structure</p>

#### [ Luca Gerolla (Aug 09 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172455):
<p>So you think this is the appropriate way to define the equivalence relation that I will define the quotient on? When needed to get an actual  <code>path_homotopy f g </code>  from <code> H : is_homotopic_to f g </code>  I use <code>cases </code>; while to show (for example) <code>is_homotopic_to f g</code> I construct an actual <code>F : path_homotopy f g </code> and feed this with <code>nonempty.intro </code>.  Would this be a good way to manage the homotopy binary relation? At first,  I just felt I was loosing some information with <code>nonempty </code> in later proofs.</p>

#### [ Kenny Lau (Aug 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172493):
<p>I think Kevin wants a <code>trunc</code> instead of a <code>nonempty</code></p>

#### [ Kenny Lau (Aug 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172500):
<p>but this will be to HoTT-like</p>

#### [ Mario Carneiro (Aug 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172508):
<p>To take a quotient you need a Prop</p>

#### [ Mario Carneiro (Aug 09 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172560):
<p>Consider the way <code>cardinal</code> is defined - it is a quotient over the relation <code>nonempty (A ≃ B)</code></p>

#### [ Luca Gerolla (Aug 09 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131174279):
<p>I see.. thank you! I will stick to <code>nonempty</code></p>


{% endraw %}
