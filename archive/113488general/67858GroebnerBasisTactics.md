---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67858GroebnerBasisTactics.html
---

## Stream: [general](index.html)
### Topic: [Groebner Basis Tactics](67858GroebnerBasisTactics.html)

---


{% raw %}
#### [ Syx Pek (Sep 09 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133625535):
Is there currently a way to do Groebner Basis in Lean?

#### [ Mario Carneiro (Sep 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133625670):
short answer is no. Long answer is what do you mean?

#### [ Syx Pek (Sep 09 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133625779):
Ive been thinking of trying to proving geometrical theorems via an algebraic approach. Obviously, I could generate a groebner basis externally and use it as a certificate for theorems, but was wondering is there already work done on making tactics do it directly.

#### [ Reid Barton (Sep 09 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133626122):
I think the answer is "not as far as anyone here knows".

#### [ Reid Barton (Sep 09 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133626235):
I'm guessing that doing the computations in Lean would be a lot slower (for now) and a lot more work and, if you can have an external tool give you a certificate that can be checked efficiently, doesn't really have any advantages besides not depending on an external tool.

#### [ Reid Barton (Sep 09 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133626301):
@**Syx Pek** on the other hand much of the work that would be required might be useful for implementing other tactics, as well.

#### [ Kevin Buzzard (Sep 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Groebner%20Basis%20Tactics/near/133641505):
We only got polynomials in one variable about a month ago, I think groebner bases are some time off yet.


{% endraw %}
