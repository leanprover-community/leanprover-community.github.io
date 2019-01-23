---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49946wheredidIgoclassical.html
---

## Stream: [general](index.html)
### Topic: [where did I go classical?](49946wheredidIgoclassical.html)

---


{% raw %}
#### [ Kenny Lau (Mar 29 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368857):
```
theorem aux3 (n : nat) (H1 : ¬n < 3) (H2 : even n) : aux (n - 2) < aux n :=
begin
  have H3 := le_of_not_gt H1,
  rw [aux, aux, if_neg H1, if_pos H2],
  let m := n - 3,
  have H4 : n = m + 3,
  { dsimp [m], rw [nat.sub_add_cancel H3] },
  rw H4 at *,
  rw nat.add_sub_assoc,
  rw nat.add_sub_assoc,
  rw nat.add_sub_assoc,
  { simp,
    by_cases m + 1 < 3,
    { simp [h],
      apply add_lt_add_left,
      exact dec_trivial },
    { simp [h, even_of_even_add_two _ H2],
      apply nat.lt_add_of_pos_right,
      exact dec_trivial } },
  exact dec_trivial,
  exact dec_trivial,
  exact dec_trivial
end

#### [ Kenny Lau (Mar 29 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368864):
this isn't MWE. I would understand if you can't read it off the lines

#### [ Kenny Lau (Mar 29 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368909):
(it matters in this context, not because I'm a constructivist, it has nothing to do with my constructivism, I really need this to be constructive)

#### [ Kenny Lau (Mar 29 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368916):
I suspect it's the `dec_trivial`, but natural inequality should be decidable

#### [ Kenny Lau (Mar 29 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368998):
update: I removed every `dec_trivial` and proved the inequalities using `constructor`, it's still classical

#### [ Gabriel Ebner (Mar 29 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369007):
It's `le_of_not_gt`, of course.

#### [ Kenny Lau (Mar 29 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369050):
oh, how do I fix it?

#### [ Gabriel Ebner (Mar 29 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369100):
If you really, really don't want classical logic, then you should probably prove a specialized version of `le_of_not_gt` for decidable linear orders.

#### [ Kenny Lau (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369109):
is there no simple fix for naturals

#### [ Johannes Hölzl (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369153):
Why do you need this as a constructive proof? There is no computable content.
You can constructively prove `le_of_not_gt` for `nat` using the decidability of `lt` on natural numbers.

#### [ Kenny Lau (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369161):
because the content is outside

#### [ Kenny Lau (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369163):
this is just a part

#### [ Johannes Hölzl (Mar 29 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369331):
But rewriting ` ¬n < 3 ` to `n <= 3` is not a problem for decidability in Lean. You are fine as long as only your proofs are classical.

#### [ Kenny Lau (Mar 29 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124380166):
oh and for the sake of completeness, the final product is here https://github.com/kckennylau/Lean/blob/master/recursion.lean


{% endraw %}
