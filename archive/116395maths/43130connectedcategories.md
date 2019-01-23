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
I took a stab at defining an "interface" for what it means for a category to be connected and used it to prove a standard fact about cofinal functors. @**Mario Carneiro** I'm curious to hear whether you would suggest any improvements.
https://gist.github.com/rwbarton/1ce6aabec33d47213ed11c5b7d907a4f

#### [ Reid Barton (Sep 12 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133812190):
I didn't bother actually defining `connected` as I figure it's easy once you have the interface right. So the interface is the three `axiom`s. `components` is not used directly, but the definition of `connected` should make proving `connected_iff_components_trivial` easy so it should probably be related to `components` in some way.

#### [ Reid Barton (Sep 12 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133812479):
I guess I didn't include any way to prove that a category is connected, but I feel like that side of things should be easier

#### [ Reid Barton (Sep 12 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/connected%20categories/near/133814587):
Actually I need the inv_fun direction of `connected_iff_components_trivial` elsewhere, so that can also be considered part of the interface


{% endraw %}
