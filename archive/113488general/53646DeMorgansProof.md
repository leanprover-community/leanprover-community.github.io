---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53646DeMorgansProof.html
---

## Stream: [general](index.html)
### Topic: [De Morgan's Proof](53646DeMorgansProof.html)

---


{% raw %}
#### [ Stephanie Wang (Dec 13 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151734970):
I'm new to Lean, can someone help me out with this proof of this version of De Morgan's Law? I'm having trouble coming up with the forward proof
``` 
theorem demorgans_law : ¬(p ∨ q) ↔ ¬p ∧ ¬q := 
  iff.intro(
  -- 
  )
  (
  assume h : ¬p ∧ ¬q,
  not_or h.left h.right
  )
```

#### [ Kevin Buzzard (Dec 13 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735268):
I'd start like this:

```lean
theorem demorgans_law (p q : Prop) : ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
  iff.intro(
    λ h,⟨_,_⟩
  )
  (
  assume h : ¬p ∧ ¬q,
  not_or h.left h.right
  )
```

#### [ Kevin Buzzard (Dec 13 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735351):
and there is a red error on each of the _'s. I'd then try and figure out how to solve them. Actually, I'm a mathematician, so really I'd go straight into tactic mode...

#### [ Kevin Buzzard (Dec 13 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735412):
Ok so I can do it but it might look incomprehensible. Do you just want a solution or a hint?

#### [ Stephanie Wang (Dec 13 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735550):
a comprehensible solution would be nice!

#### [ Kevin Buzzard (Dec 13 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735667):
Then you want to use tactic mode!

#### [ Chris Hughes (Dec 13 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735761):
`assume h, and intro (assume hp, h (or.inl hp)) (assume hq, h (or.inr hq))`

#### [ Kevin Buzzard (Dec 13 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735780):
```lean
theorem demorgans_law' (p q : Prop) : ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
begin
  split,
  { intro hnpq,
    split,
    { intro hp,
      apply hnpq,
      left,
      assumption
    },
    { intro hq,
      apply hnpq,
      right,
      assumption
    }
  },
  sorry
end
```
half way there

#### [ Kevin Buzzard (Dec 13 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735899):
```lean
theorem demorgans_law' (p q : Prop) : ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
begin
  split,
  { intro hnpq,
    split,
    { intro hp,
      apply hnpq,
      left,
      assumption
    },
    { intro hq,
      apply hnpq,
      right,
      assumption
    }
  },
  intro hnpnq,
  intro hpq,
  cases hnpnq with hnp hnq,
  cases hpq,
    contradiction,
    contradiction
end
```

My impression is that computer scientists prefer these term mode things that you were writing, but I've been teaching mathematicians this stuff and tactic mode seems to be far easier for them.

#### [ Kevin Buzzard (Dec 13 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735933):
```lean
theorem demorgans_law (p q : Prop) : ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
⟨λ h, ⟨λ hp, h $ or.inl hp, λ hq, h $ or.inr hq⟩,
  λ ⟨hnp, hnq⟩ hn, or.elim hn hnp hnq⟩
```
Computer science proof, incomprehensibled to the max. Chris posted the perhaps happy medium you were looking for.

#### [ Kevin Buzzard (Dec 13 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151736068):
```lean
theorem demorgans_law'' (p q : Prop): ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
  iff.intro(
    assume h, and.intro (assume hp, h (or.inl hp)) (assume hq, h (or.inr hq))
  )
  (
  assume h : ¬p ∧ ¬q,
  not_or h.left h.right
  )
```

#### [ Stephanie Wang (Dec 13 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151736196):
Ok this makes a lot of sense to me, thanks so much.


{% endraw %}
