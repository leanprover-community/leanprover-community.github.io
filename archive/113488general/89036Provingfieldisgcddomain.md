---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89036Provingfieldisgcddomain.html
---

## Stream: [general](index.html)
### Topic: [Proving field is gcd domain](89036Provingfieldisgcddomain.html)

---


{% raw %}
#### [ AHan (Dec 19 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170274):
<p>While trying to prove a field is gcd domain, I found out that there seems like a conflict between two fields of class <code>gcd_domain</code> to me ...<br>
<code>lean norm_unit_coe_units : ∀(u : units α), norm_unit u = u⁻¹</code> and <br>
<code>lean norm_unit_gcd  : ∀a b, norm_unit (gcd a b) = 1</code><br>
Since every element in a  field, is a unit, and if <code>a ≠ 0 ∨ b ≠ 0</code>, then <code>1 =  norm_unit (gcd a b) = (gcd a b)⁻¹</code>...</p>

#### [ AHan (Dec 19 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170344):
<p>Do I misunderstand something?</p>

#### [ Kenny Lau (Dec 19 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170398):
<p>therefore <code>gcd a b = 1</code>!</p>

#### [ AHan (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170448):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  Yes... which sounds strange to me...</p>

#### [ Kenny Lau (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170452):
<p>why?</p>

#### [ Kenny Lau (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170453):
<p>who would say that <code>gcd 3 5 = -1</code>?</p>

#### [ Kenny Lau (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170458):
<p>or <code>gcd pi e = 3</code>?</p>

#### [ AHan (Dec 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170769):
<p>Why wouldn't <code>gcd 3 5 = 3</code> ?</p>

#### [ AHan (Dec 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170811):
<p>Oh I'm wrong...</p>

#### [ AHan (Dec 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170821):
<p>Yeah, you're right! It sould be 1!!</p>


{% endraw %}
