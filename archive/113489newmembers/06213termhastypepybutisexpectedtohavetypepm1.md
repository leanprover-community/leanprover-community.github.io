---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/06213termhastypepybutisexpectedtohavetypepm1.html
---

## [new members](index.html)
### [term has type p y but is expected to have type p ?m_1[_]](06213termhastypepybutisexpectedtohavetypepm1.html)

#### [Alistair Tucker (Dec 02 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150728969):
Am I trying to do something impossible?
```lean
theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  apply exists.intro,
  cases h with y hy,
  exact hy,
end
```

#### [Kevin Buzzard (Dec 02 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729021):
```lean
theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y := h

```

So the theorem is true, at least :-)

#### [Kevin Buzzard (Dec 02 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729038):
```lean
theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  cases h with y hy,
  apply exists.intro,
  exact hy,  
end
```

#### [Kenny Lau (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729091):
```lean
meta def tactic.interactive.result : tactic unit :=
tactic.result >>= tactic.trace

theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  apply exists.intro,
  cases h with y hy,
  result,
/-
exists.intro ?m_1 (Exists.dcases_on h (λ (y : α) (hy : p y), ?m_2[h, y, hy]))
-/
  exact hy,
end
```

#### [Alistair Tucker (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729095):
Yes :)  But there is some reason it's in that order. I think...

#### [Kenny Lau (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729096):
(`result` is the proof term constructed at that particular moment)

#### [Kenny Lau (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729099):
and you can see why this is impossible

#### [Kevin Buzzard (Dec 02 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729154):
After your application of `exists.intro` one of your goals has a metavariable, which is not at all ideal. I would recommend not using `apply exists.intro` for this sort of reason.

#### [Kevin Buzzard (Dec 02 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729224):
```lean
theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  apply exists.intro,
  -- you now have two goals, and one contains a metavariable.
  -- this is not recommended.
  -- Your next line only applies to the first goal.
    cases h with y hy,
    -- your metavariable just got uglier.
    -- This is even less recommended.
    tactic.swap,
    -- we are now working with a sensible goal
    -- but now we need to get data from a proposition.
    exact classical.some h, -- I just used a noncomputable axiom
  -- one goal now
  exact classical.some_spec ⟨y,hy⟩, -- I just undid your "cases h" line.
end
```

That's a way to dig yourself out of the hole.

#### [Kevin Buzzard (Dec 02 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729230):
`#print axioms mwe -- classical.choice`

#### [Kenny Lau (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729285):
```lean
theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  apply exists.intro,
  cases h with y hy,
  exact classical.some_spec _
end

#print mwe
/-
exists.intro (classical.some h) (Exists.dcases_on h (λ (y : α) (hy : p y), classical.some_spec (Exists.intro y hy)))
-/
```

#### [Alistair Tucker (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729286):
Ha!  it turns out there was no good reason for putting it in that order :)
What do you recommend instead of apply exists.intro?

#### [Kevin Buzzard (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729289):
`use`

#### [Reid Barton (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729290):
It would probably be better to do the `cases` first

#### [Rob Lewis (Dec 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729347):
It's not always bad to `apply exists.intro` and have a metavar for one goal. Sometimes you want to just show the body of the exists, and let Lean figure out what the witness was by unification. (Like in Kenny's example.)

#### [Kenny Lau (Dec 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729348):
I'm surprised the `_` worked

#### [Kevin Buzzard (Dec 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729351):
```lean
import tactic.interactive

theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  cases h with y hy,
  use y,
  assumption
end

#print axioms mwe -- no axioms
```

#### [Alistair Tucker (Dec 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729362):
"use" is a tactic?

#### [Kevin Buzzard (Dec 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729365):
As of about a week ago

#### [Kevin Buzzard (Dec 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729375):
`existsi` is an older one, it's a bit less robust but it would work here

#### [Kevin Buzzard (Dec 02 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729418):
```lean
theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  cases h with y hy,
  existsi y,
  assumption
end
```

#### [Kevin Buzzard (Dec 02 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729420):
no import needed

#### [Alistair Tucker (Dec 02 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729424):
Thank you all

#### [Reid Barton (Dec 02 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729433):
Your original one didn't work because you wanted `exact hy` to also solve the other goal with `y`, but `y` was not in scope for the other goal!

#### [Kevin Buzzard (Dec 02 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729480):
Yes! And it's hard to get access to it too, because `\exists` only eliminates to `Prop`.

#### [Kenny Lau (Dec 02 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729501):
again, you can see it using this:
```lean
meta def tactic.interactive.result : tactic unit :=
tactic.result >>= tactic.trace

theorem mwe {α : Type*} {p : α → Prop} (h : ∃ (y : α), p y) : ∃ (y : α), p y :=
begin
  apply exists.intro,
  cases h with y hy,
  result,
/-
exists.intro ?m_1 (Exists.dcases_on h (λ (y : α) (hy : p y), ?m_2[h, y, hy]))
-/
  exact hy,
end
```

#### [Kenny Lau (Dec 02 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729503):
there's no way to unify `?m_1` with `y` because `y` doesn't even exist in the scope of `?m_1`

#### [Kevin Buzzard (Dec 02 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729543):
[just to be clear -- Kenny's code doesn't run]

