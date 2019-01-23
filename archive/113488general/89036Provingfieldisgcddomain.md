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
While trying to prove a field is gcd domain, I found out that there seems like a conflict between two fields of class `gcd_domain` to me ...
```lean norm_unit_coe_units : ∀(u : units α), norm_unit u = u⁻¹``` and 
```lean norm_unit_gcd  : ∀a b, norm_unit (gcd a b) = 1```
Since every element in a  field, is a unit, and if `a ≠ 0 ∨ b ≠ 0`, then `1 =  norm_unit (gcd a b) = (gcd a b)⁻¹`...

#### [ AHan (Dec 19 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170344):
Do I misunderstand something?

#### [ Kenny Lau (Dec 19 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170398):
therefore `gcd a b = 1`!

#### [ AHan (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170448):
@**Kenny Lau**  Yes... which sounds strange to me...

#### [ Kenny Lau (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170452):
why?

#### [ Kenny Lau (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170453):
who would say that `gcd 3 5 = -1`?

#### [ Kenny Lau (Dec 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170458):
or `gcd pi e = 3`?

#### [ AHan (Dec 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170769):
Why wouldn't `gcd 3 5 = 3` ?

#### [ AHan (Dec 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170811):
Oh I'm wrong...

#### [ AHan (Dec 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20field%20is%20gcd%20domain/near/152170821):
Yeah, you're right! It sould be 1!!


{% endraw %}
