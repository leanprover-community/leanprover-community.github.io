---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43130connectedcategories.html
---

## Stream: [maths](index.html)
### Topic: [connected categories](43130connectedcategories.html)

---


{% raw %}
#### [ Reid Barton (Sep 12 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133812119):
<p>I took a stab at defining an "interface" for what it means for a category to be connected and used it to prove a standard fact about cofinal functors. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm curious to hear whether you would suggest any improvements.<br>
<a href="https://gist.github.com/rwbarton/1ce6aabec33d47213ed11c5b7d907a4f" target="_blank" title="https://gist.github.com/rwbarton/1ce6aabec33d47213ed11c5b7d907a4f">https://gist.github.com/rwbarton/1ce6aabec33d47213ed11c5b7d907a4f</a></p>

#### [ Reid Barton (Sep 12 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133812190):
<p>I didn't bother actually defining <code>connected</code> as I figure it's easy once you have the interface right. So the interface is the three <code>axiom</code>s. <code>components</code> is not used directly, but the definition of <code>connected</code> should make proving <code>connected_iff_components_trivial</code> easy so it should probably be related to <code>components</code> in some way.</p>

#### [ Reid Barton (Sep 12 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133812479):
<p>I guess I didn't include any way to prove that a category is connected, but I feel like that side of things should be easier</p>

#### [ Reid Barton (Sep 12 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133814587):
<p>Actually I need the inv_fun direction of <code>connected_iff_components_trivial</code> elsewhere, so that can also be considered part of the interface</p>


{% endraw %}
