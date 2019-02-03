---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10577nonpersistentattributes.html
---

## Stream: [general](index.html)
### Topic: [non-persistent attributes](10577nonpersistentattributes.html)

---


{% raw %}
#### [ Simon Hudon (Jan 26 2019 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-persistent%20attributes/near/156944210):
<p>I'm trying to set an attribute inside a proof script and as soon as the proof is done, the attribute seems to disappear. Is this the desired behavior? Is there a way to make the attribute persistent?</p>

#### [ Mario Carneiro (Jan 27 2019 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-persistent%20attributes/near/156945139):
<p>Theorems can't make permanent modifications to the environment, because they are executed out of order</p>

#### [ Simon Hudon (Jan 27 2019 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-persistent%20attributes/near/156945256):
<p>Arrrrgh! I'm trying to generate unique file names for caching proof witnesses</p>

#### [ Simon Hudon (Jan 27 2019 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-persistent%20attributes/near/156945302):
<p>Maybe I should just hash the goal</p>


{% endraw %}
