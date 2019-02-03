---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02642implicitparametersofstructureclassfields.html
---

## Stream: [general](index.html)
### Topic: [implicit parameters of structure/class fields](02642implicitparametersofstructureclassfields.html)

---


{% raw %}
#### [ Reid Barton (Nov 26 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20parameters%20of%20structure/class%20fields/near/148375439):
<p>Are the rules for the types of the field accessors (in particular, whether arguments are explicit or implicit) written out somewhere (not in C++)?</p>

#### [ Keeley Hoek (Nov 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20parameters%20of%20structure/class%20fields/near/148408330):
<p>I don't fully know what you mean Reid, so sorry if this stuff you already know, but given <code>struct : name</code> and <code>field : name</code> you can infer the type of the honest function named <code>struct</code> and of the projection <code>struct ++ field</code>, then unwind the Pi binders off the projection which just correspond to the type arguments passed to <code>struct</code>. That's how I've figured out what all the arguments are and what their <code>binder_info</code> is in the past.</p>


{% endraw %}
