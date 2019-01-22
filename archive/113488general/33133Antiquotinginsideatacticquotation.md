---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33133Antiquotinginsideatacticquotation.html
---

## [general](index.html)
### [Antiquoting inside a tactic quotation](33133Antiquotinginsideatacticquotation.html)

#### [Nicholas Scheel (Sep 17 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134069500):
Hi!! So I'm trying to write my first tactic and I have something that looks like this:
```lean
meta def naturally (t : Type) : tactic unit :=
  iterate `[ rw [← @nat.cast_zero %%t] ]
```
but I get this error:
```
kernel failed to type check declaration 'naturally' this is usually due to a buggy tactic or a bug in the builtin elaborator
elaborated type:
  Type → tactic unit
elaborated value:
  λ (t : Type),
     .....................
```

I can write it without the antiquotation, but I realized I then have to have `t` in scope when I run `naturally` to get it to work that way :sweat_smile:

#### [Nicholas Scheel (Sep 17 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134069543):
Do you know what the issue is and how I could write it properly? :)

#### [Nicholas Scheel (Sep 17 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134069695):
Background: I'm basically trying to write a tactic that converts statements about \N embedded in \R into statements about \N, like the following:
```lean
example : ∀ n : ℕ, (0 : ℕ) < 2 + n := by intro n; simpa [nat.zero_lt_succ]

example : ∀ n : ℕ, (0 : ℝ) < 2 + n :=
  begin
  intro n,
  let t := ℝ,
  naturally ℝ,
  rw [add_comm _ n],
  apply nat.zero_lt_succ
  end
```

#### [Nicholas Scheel (Sep 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134069807):
Why I’m trying to restrict it to a certain type is to prevent infinite recursion (e.g. 0 with lots of coercions from nat to nat); it would be cool if there was a better way to do this but I have not explored tactics much

#### [Mario Carneiro (Sep 17 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134070948):
`t` should have type `expr` not `Type`

#### [Nicholas Scheel (Sep 17 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134072594):
Hm ... I believe you, but it still doesn't seem to compile:
```lean
meta def naturally' (t : expr) : tactic unit :=
  tactic.interactive.iterate none `[ rw [← @nat.cast_zero %%t] ]
```

#### [Nicholas Scheel (Sep 17 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134072699):
I'm using Lean v3.4.1 btw

#### [Nicholas Scheel (Sep 17 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134072755):
it looks like this term is failing: `rule := expr.subst (to_pexpr t)` (it's missing the second argument)
without the antiquotation it is: `rule := ``(@nat.cast_zero t)`

#### [Nicholas Scheel (Sep 17 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134072861):
I think it should be `rule := expr.subst ``(λ (_x_1 : _), @nat.cast_zero _x_1) (to_pexpr t)`

#### [Simon Hudon (Sep 17 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134077733):
`rw` is tricky to use this way. Try not quoting it. You'll see its argument list is not a list of expr (in which case your attempt should work); it's a list of `rw_rules`

#### [Nicholas Scheel (Sep 17 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134079385):
yeah, this is what I ended up with (forgive the messy code): https://github.com/MonoidMusician/MATH361/blob/56b6b5df40598bddade40e973a400a67cb79d184/src/hw/hw2.lean#L380-L407

#### [Nicholas Scheel (Sep 17 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134079431):
I wasn’t able to get it to parse an expression in interactive mode, so I just made an alias for applying it to reals haha

#### [Mario Carneiro (Sep 17 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134079528):
I suggest you use the noninteractive rw tactic outside interactive mode

#### [Nicholas Scheel (Sep 17 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134079539):
that would probably be a good idea :D

#### [Nicholas Scheel (Sep 17 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134079627):
would that be `rewrite_target`?

#### [Simon Hudon (Sep 17 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Antiquoting inside a tactic quotation/near/134108985):
I was about to suggest `rewrite_target` but it requires that you encode `<- ` by hand

