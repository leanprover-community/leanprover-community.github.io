---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/30835symmetryofcongruencemod37.html
---

## [new members](index.html)
### [symmetry of congruence mod 37](30835symmetryofcongruencemod37.html)

#### [Nicholas Siedlaczek (Dec 06 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151046285):
I know what I am trying to achieve, however not sure about how to actually execute it in Lean.

```lean
import tactic.ring

definition R (a b : ℤ) := ∃ (k : ℤ), k * 37 = a - b

theorem R_is_symmetric : symmetric R :=
begin
  unfold symmetric,
  intro x,
  intro y,
  unfold R,
  intro H,
  existsi((-k) : ℤ),

end
```
As you can see I have the hypothesis the k * 37 = x - y, however want to show existence of -k to show -k * 37 = y - x which will show that it is symmetric.
Thanks

#### [Chris Hughes (Dec 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151046398):
This should help. Use cases.
```lean
theorem R_is_symmetric : symmetric R :=
begin
  unfold symmetric,
  intro x,
  intro y,
  unfold R,
  intro H,
  cases H with k hk,
  existsi( -k : ℤ),

end
```

#### [Nicholas Siedlaczek (Dec 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151046671):
Thanks Chris

#### [Kevin Buzzard (Dec 06 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151050131):
Are you an Imperial undergraduate doing my equivalence relation challenge @**Nicholas Siedlaczek** ?

#### [Mario Carneiro (Dec 06 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151050456):
I'm sure the 37 was a coincidence

#### [Patrick Massot (Dec 07 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052405):
@**Nicholas Siedlaczek** , after you're done with this, it will be useful to realize that all those `unfold` are only psychological comfort for you, but Lean doesn't need them. The tactic proof of your lemma needs no more than three lines, one for introductions (using tactic `rintros`), one for instanciating the existential (using tactic `use`, or `existsi` but you should get used to `use` which is newer and more powerful), and one for the tiny computation (using tactic `simp`).

#### [Nicholas Siedlaczek (Dec 07 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052641):
@**Patrick Massot** Thanks so what you're saying is all ```unfold``` does is display to the user what it actually means and shows you what to prove while lean basically 'ignores' them and is of no consequences to it?

#### [Patrick Massot (Dec 07 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052874):
Sometimes it's useful also to Lean, eg for type class instance resolution but, in my experience, almost every unfold that I type is unnecessary.

#### [Patrick Massot (Dec 07 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052898):
In your case, the full proof is
```lean
definition R (a b : ℤ) := ∃ (k : ℤ), k * 37 = a - b

theorem R_is_symmetric : symmetric R :=
begin
  rintros x y ⟨k, H⟩,
  use -k,
  simp[H]
end
```

#### [Patrick Massot (Dec 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151053009):
If you want to emphasize which part really uses tactics seriously, you can also write it as:
```lean
theorem R_is_symmetric : symmetric R := λ x y ⟨k, H⟩, ⟨-k, by simp[H]⟩
```

#### [Patrick Massot (Dec 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151053075):
It shows clearly that, in this proof, the only tactic which actually does work for you is the simplifier

