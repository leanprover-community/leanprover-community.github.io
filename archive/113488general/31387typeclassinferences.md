---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31387typeclassinferences.html
---

## Stream: [general](index.html)
### Topic: [typeclass inferences](31387typeclassinferences.html)

---

#### [Kenny Lau (Apr 06 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695237):
https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72
In L72 of this, I needed to type `@linear_map R M (Hom_R_Q_div_Z R) _ _ (Hom_R_Q_div_Z.module R)`, i.e. I needed to manually provide the proof term `Hom_R_Q_div_Z.module R` that `Hom_R_Q_div_Z R` is a module, despite it being attributed as `instance`. Why is this the case?

#### [Scott Morrison (Apr 06 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695367):
When faced with this problem, I often try to write an example beforehand, which hopefully should summon the instance via `by apply_instance`, and see if I can get that working.

#### [Scott Morrison (Apr 06 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695372):
If I can't I start worrying about universe levels, which in my experience is a very common cause of typeclass inference failing.

#### [Scott Morrison (Apr 06 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695410):
(I haven't actually looked at your example.)

#### [Scott Morrison (Apr 06 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695678):
Having quickly looked at your example, I'd suggest trying to restrict to the case where the ring and the module live in the same universe.

#### [Kenny Lau (Apr 06 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695682):
hmm, would that break generality?

#### [Kenny Lau (Apr 06 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695722):
`linear_map` accepts three universes

#### [Scott Morrison (Apr 06 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695723):
Yeah... but that's maybe dangerous as well.

#### [Kenny Lau (Apr 06 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695729):
so other universes don't have enough injectives lol

#### [Scott Morrison (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695730):
at least check if this solves the inference problem

#### [Scott Morrison (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695735):
If it doesn't then it's irrelevant. If it does, it's probably time to consult Mario for advice.

#### [Scott Morrison (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695736):
(One can always `ulift` when you don't have enough universe polymorphism, and sometimes this is the better option.)

#### [Kenny Lau (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695738):
it doesn't

#### [Scott Morrison (Apr 06 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695782):
Oh well!

#### [Scott Morrison (Apr 06 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695794):
try replacing the points where you explicitly provide the instances with `by apply_instance`, and then set `pp.all`

#### [Kenny Lau (Apr 06 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695869):
wait what

#### [Kenny Lau (Apr 06 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695981):
@**Scott Morrison** once I removed L67-69, everything worked

#### [Kenny Lau (Apr 06 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695982):
except the fact that i of course need those lines

#### [Kenny Lau (Apr 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124697691):
@**Mario Carneiro** any idea? In [here](https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72), I need ` Hom_R_Q_div_Z.module R ` to tell Lean that ` Hom_R_Q_div_Z R ` is a module, but once I remove L67-69, it is no longer necessary

#### [Kenny Lau (Apr 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124697743):
I suspect it is because of the ` injective.to_module `

#### [Kenny Lau (Apr 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124697747):
interfering with the typeclass resolutions

