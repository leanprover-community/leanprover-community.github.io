---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/77548homeos.html
---

## Stream: [maths](index.html)
### Topic: [homeos](77548homeos.html)

---


{% raw %}
#### [ Patrick Massot (Sep 20 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeos/near/134333294):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> For the perfectoid project I had to get back to my old <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean</a> defining homeomorphisms. But now we have the category Top in mathlib, and isomorphisms. Can I throw away my file and use the category theory stuff? How would that work?</p>

#### [ Reid Barton (Sep 20 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeos/near/134333594):
<p>That's what I did in lean-homotopy-theory. My internet is acting up and I can't provide a direct link, but the filename is <code>src/homotopy_theory/topological_spaces/homeomorphism.lean</code></p>

#### [ Patrick Massot (Sep 20 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeos/near/134333849):
<p>great</p>

#### [ Patrick Massot (Sep 20 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeos/near/134333908):
<p>It looks nice, but I'd like to be able to plug this into the story we have in the separation thread</p>

#### [ Patrick Massot (Sep 20 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeos/near/134333938):
<p>Do you think it's possible, or does it mean everything must be rewritten in terms of Top instead of topological_space?</p>


{% endraw %}
