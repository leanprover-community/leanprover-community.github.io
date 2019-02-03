---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35423explicitimplicitswitch.html
---

## Stream: [general](index.html)
### Topic: [explicit/implicit switch](35423explicitimplicitswitch.html)

---


{% raw %}
#### [ Patrick Massot (Jun 09 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explicit/implicit%20switch/near/127814721):
<p>We have a section where all definitions and lemmas start with either <code>(A : type) [class1 A] [class2 A] [class3 A] [class4 A]</code> or <code>{A : type} [class1 A] [class2 A] [class3 A] [class4 A]</code> ( only difference is <code>()</code> vs <code>{}</code> in first argument). Is there any way we could tell Lean which one we want for each def/lemma without having to copy the whole line or use a different variable name? Of course simply writing <code>(A : Type)</code> or <code>{A : Type}</code> at the beginning of a def doesn't work since it shadows the variable and loses the instance implicit stuff</p>

#### [ Sebastian Ullrich (Jun 09 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explicit/implicit%20switch/near/127819085):
<p><code>variable {A}</code> changes the binder of an existing variable <code>A</code></p>

#### [ Patrick Massot (Jun 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explicit/implicit%20switch/near/127819892):
<p>Thanks!</p>


{% endraw %}
