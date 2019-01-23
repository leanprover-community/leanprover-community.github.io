---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19171builtintactics.html
---

## Stream: [new members](index.html)
### Topic: [builtin tactics](19171builtintactics.html)

---

#### [Olli (Sep 15 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134011488):
is there an even simpler way to write `{ left, assumption} <|> { right, assumption }` ?

#### [Kenny Lau (Sep 15 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134011636):
`simp*`

#### [Olli (Sep 15 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134011708):
thanks

#### [Olli (Sep 15 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134012389):
is there a way to do pattern matching in tactic mode?

#### [Olli (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134012448):
if there was I would think it'd be with the `let` tactic, but I can't seem to get it to work

#### [Chris Hughes (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134012572):
rcases

#### [Olli (Sep 15 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134023310):
how come I can't just repeat `constructor` here:
```lean
example {p q} : ¬(p ∨ q) → ¬p ∧ ¬q := 
begin
  intro h,
  constructor;
  intro hpq;
  apply h,
  constructor, assumption,
  constructor, assumption
  -- Doesn't work because before `assumption` state is:
  -- p q : Prop,
  -- h : ¬(p ∨ q),
  -- hpq : q
  -- ⊢ p
end
```

but yet this works:
```lean
example {p q} : ¬(p ∨ q) → ¬p ∧ ¬q := 
begin
  intro h,
  constructor;
  intro hpq;
  apply h,
  constructor, assumption,
  apply or.inr hpq
end
```

#### [Kenny Lau (Sep 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134023364):
Lean can't possibly know which constructor to use

#### [Olli (Sep 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134023405):
hmm I see, I was originally trying to write it as `repeat { constructor, assumption }`, but yeah I think I understand how this is ambigious

#### [Kevin Buzzard (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134025252):
Some symmetries in maths are lost in computer science. Or and And are different types of things. And only has one constructor (to prove `and p q` you have to supply both a proof of `p` and a proof of `q` all in one go) but Or has two (to prove `or p q` you have two choices). If you look at the definitions as inductive types by right clicking on `and` or `or` in a working Lean session and peeking at the definition you will see this. For inductive types with one constructor like `and` or `subtype` or `group` the `constructor` tactic does a predictable thing. For types like `or` with more than one constructor the tactic just, I think, chooses the first one, so for `or` I think `constructor` does the same as `left`.

#### [Olli (Sep 15 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134025625):
yeah it's probably a good idea to avoid using `constructor` with types having more than one constructor then?

so far my strategy for solving these exercises has been just staring at the tactic state while trying to make progress and not giving too much thought to what is happening in the bigger picture, and this is working surprisingly well, but there are some traps like this that lead to dead-ends

#### [Mario Carneiro (Sep 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134025763):
you can use constructor as long as only one of the constructors is applicable

