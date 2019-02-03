---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05553Finitemaps.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Finite maps](https://leanprover-community.github.io/archive/113488general/05553Finitemaps.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ben Sherman (Nov 06 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146891105):
<p>Is there a Lean (3) library for finite maps (i.e., key-value maps where finitely many keys are mapped to values)? I don't need performance, just reasoning really. But I'd also be fine if the key type requires decidable ordering (I would assume it would require at least decidable equality). Should I use this <a href="https://github.com/spl/lean-finmap" target="_blank" title="https://github.com/spl/lean-finmap">https://github.com/spl/lean-finmap</a>?</p>

#### [ Reid Barton (Nov 06 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146891398):
<p>There's <code>data.rbmap</code> in the Lean standard library, does that meet your needs?</p>

#### [ Mario Carneiro (Nov 06 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146891483):
<p>There is also the <code>finmap</code> branch of leanprover-community which is porting Sean's work to mathlib</p>

#### [ Mario Carneiro (Nov 06 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146891514):
<p>and <code>hash_map</code> is also a finite map type</p>

#### [ Mario Carneiro (Nov 06 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146891603):
<p>on the non-computational side, <code>finsupp</code> is basically the type of finite maps (mapping everything out of domain to 0)</p>

#### [ Ben Sherman (Nov 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146892020):
<p>I'm looking for something that has unions and theorems about them. In this regard, both <code>data.rbmap</code> and <code>data.hash_map</code> are incomplete. And I do want to write programs, so <code>finsupp</code> is not what I'm looking for either. So it sounds like <code>finmap</code> is the way to go! Thanks for pointing me to the <code>finmap</code> branch of mathlib - I guess I'll use that. Thanks for the pointers, everyone!</p>

#### [ Mario Carneiro (Nov 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Finite%20maps/near/146892405):
<p>Ah, that's good to know. I'll work on adding unions to rbmap and hash_map</p>


{% endraw %}
