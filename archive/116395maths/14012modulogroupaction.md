---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14012modulogroupaction.html
---

## Stream: [maths](index.html)
### Topic: [modulo group action](14012modulogroupaction.html)

---


{% raw %}
#### [ Patrick Massot (Sep 13 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133907297):
Do I understand correctly that we have a file defining group action and a file defining left and right cosets in a group, but no link between those? And we don't have G\X if G acts on X?

#### [ Kenny Lau (Sep 13 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133907861):
we do have orbit-stabalizer theorem, if that's what you mean

#### [ Chris Hughes (Sep 13 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133907907):
I'm not sure exactly  what you mean, but it may well be part of my Sylow PR.

#### [ Patrick Massot (Sep 13 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908423):
No, I don't mean orbit stabilizer. I mean: if G acts on X, quotient X by "x equivalent to y if there exists g such that y = g x"

#### [ Patrick Massot (Sep 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908526):
This: https://github.com/leanprover/mathlib/pull/257/files#diff-a1c68f03014617e86345e35b6885b923R90

#### [ Patrick Massot (Sep 13 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908563):
What is the status of this PR?

#### [ Chris Hughes (Sep 13 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908650):
On hold because of the cardinals of finite sets issue.

#### [ Patrick Massot (Sep 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908941):
Is this something someone is working on?

#### [ Chris Hughes (Sep 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908971):
Not really.

#### [ Chris Hughes (Sep 13 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908998):
I'm playing with tactics, and hope to be able to write a tactic to deal with it at some point.

#### [ Chris Hughes (Sep 13 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909003):
But it could take a while

#### [ Chris Hughes (Sep 13 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909156):
I could separate out the bits that aren't about finite sets, and PR them first if you're desperate for it. Do you want the fact that G acts on the cosets of a subgroup as well?

#### [ Patrick Massot (Sep 13 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909216):
I'm not desperate, I wrote:
```lean
import group_theory.group_action

variables {X : Type*} {G : Type*} [group G] (ρ : G → X → X) [is_group_action ρ]

lemma is_group_action.inverse_left (g : G) : (ρ g⁻¹) ∘ ρ g = id :=
begin
  ext x,
  change ρ g⁻¹ (ρ g x) =  x,
  rw ← is_monoid_action.mul ρ g⁻¹ g x,
  simp [is_monoid_action.one ρ]
end

lemma is_group_action.inverse_right (g : G) : (ρ g) ∘ ρ g⁻¹ = id :=
by simpa using is_group_action.inverse_left ρ g⁻¹

def action_rel : setoid X :=
⟨λ x y, ∃ g, ρ g x = y, ⟨λ x, ⟨(1 : G),  is_monoid_action.one ρ x⟩,
  begin
  { split,
    { rintros x y ⟨g, h⟩,
      existsi g⁻¹,
      rw ←h,
      exact congr_fun (is_group_action.inverse_left ρ g) x },
    { rintros x y z ⟨g, h⟩ ⟨g', h'⟩,
      existsi g'*g,
      rw [is_monoid_action.mul ρ, h, h'] } }
  end⟩⟩
```

#### [ Patrick Massot (Sep 13 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909233):
So I have my setoid

#### [ Patrick Massot (Sep 13 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909249):
I don't think your PR contains much more in this direction

#### [ Patrick Massot (Sep 13 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133910622):
Does someone know where is the lemma saying that if a finite set surjects onto a type then this type is finite?

#### [ Reid Barton (Sep 13 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133910888):
`fintype.of_surjective` I guess

#### [ Patrick Massot (Sep 13 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133911324):
Thanks!


{% endraw %}
