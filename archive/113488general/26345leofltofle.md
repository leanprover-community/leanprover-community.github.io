---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26345leofltofle.html
---

## Stream: [general](index.html)
### Topic: [le_of_lt_of_le](26345leofltofle.html)

---


{% raw %}
#### [ Chris Hughes (Apr 25 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693526):
Should we prove `le_of_lt_of_le` so this stuff works?
```lean
example {a b c : ℕ} (h : a < b) (h₁ : b ≤ c) : a ≤ c :=
calc a < b : h 
   ... ≤ c : h₁ 

@[trans] lemma le_of_lt_of_le {a b c : ℕ} : a < b → b ≤ c → a ≤ c := sorry

example {a b c : ℕ} (h : a < b) (h₁ : b ≤ c) : a ≤ c :=
calc a < b : h 
   ... ≤ c : h₁ 
```

#### [ Kevin Buzzard (Apr 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693595):
I've run into that before

#### [ Kevin Buzzard (Apr 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693597):
You have to remember to apply le_of_lt before starting the calc :-)

#### [ Kevin Buzzard (Apr 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693605):
I like the idea.

#### [ Kevin Buzzard (Apr 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693695):
dammit I want the proof to be `le_of_lt $ lt_of_lt_of_le`

#### [ Kevin Buzzard (Apr 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693696):
:-)

#### [ Kevin Buzzard (Apr 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_of_lt_of_le/near/125693709):
`λ x y, le_of_lt $ lt_of_lt_of_le x y` looks like you're missing a trick


{% endraw %}
