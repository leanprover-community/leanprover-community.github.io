---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16100Strangeerrormessage.html
---

## Stream: [general](index.html)
### Topic: [Strange error message](16100Strangeerrormessage.html)

---


{% raw %}
#### [ Patrick Massot (Apr 24 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125639855):
<p><code>code generation failed, VM does not have code for 'classical.choice'</code> seems to be Lean trying to tell me to stop considering examples and go back to work</p>

#### [ Mario Carneiro (Apr 24 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125640036):
<p>you can't compute the <code>noncomputable</code></p>

#### [ Patrick Massot (Apr 24 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125640044):
<p>Yes I understand</p>

#### [ Patrick Massot (Apr 24 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125640337):
<p>funny part is I thought I wasn't using choice</p>

#### [ Patrick Massot (Apr 24 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125640531):
<p>Actually I used a small <code>#eval</code> to test something in the middle of a file I was working on. Of course this file begins the mathematical preamble, including <code>local attribute [instance] classical.prop_decidable</code></p>

#### [ Patrick Massot (Apr 24 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125640537):
<p>Removing that line makes eval to succeed</p>

#### [ Patrick Massot (Apr 24 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125640685):
<p>So the line can prevent computing even things which are actually computable. That's nice defense against constructivism</p>

#### [ Chris Hughes (Apr 24 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Strange%20error%20message/near/125642446):
<p>You can use <code>local attribute [instance, priority 0] classical.prop_decidable</code> to preserve computability when possible.</p>


{% endraw %}
