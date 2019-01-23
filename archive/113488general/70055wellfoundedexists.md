---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70055wellfoundedexists.html
---

## Stream: [general](index.html)
### Topic: [well-founded exists](70055wellfoundedexists.html)

---

#### [Sean Leather (Sep 12 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793419):
Can I prove that a recursive definition `T → Prop` is well-founded if a clause wraps the recursive call with an exists (i.e. `f <pattern> := ∃ .., f <subpattern>`)? If so, how would I begin to do this?

#### [Sean Leather (Sep 12 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793458):
Oh, actually, it's not a strict subpattern, it's a function that uses a subpattern. Maybe that's my issue, not the exists.

#### [Sean Leather (Sep 12 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793554):
So, should I have something like `have sizeof (function-calling-subpattern) < sizeof pattern` here?

#### [Sean Leather (Sep 12 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793805):
Okay, never mind, I think I figured out what I need to solve.

#### [Sean Leather (Sep 12 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793811):
I always get confused with these well-founded proofs.

#### [Sean Leather (Sep 12 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133803135):
So I finally figured out how to prove that my recursion is well-founded. But I think it could be better.

```lean
def lc' : exp V → Prop
  | (var fb _)     := fb
  | (app ef ea)    :=  
    have depth ef < depth (app ef ea) := by simp,
    have depth ea < depth (app ef ea) := by simp,
    lc' ef ∧ lc' ea
  | (lam v eb)     :=  
    ∃ (L : finset (tagged V)),
    have depth (open_fresh v L eb) < depth (lam v eb) := by simp [nat.pos_iff_ne_zero'],
    lc' (open_fresh v L eb) 
  | (let_ v ed eb) :=
    have depth ed < depth (let_ v ed eb) := by simp,
    lc' ed ∧
    ∃ (L : finset (tagged V)),
    have depth (open_fresh v L eb) < depth (let_ v ed eb) := by simp,
    lc' (open_fresh v L eb) 
  using_well_founded {
    dec_tac := tactic.assumption,
    rel_tac := λ_ _, `[exact ⟨_, measure_wf depth⟩] }
```

It would be nice if I could, say, use `simp` for the well-founded condition instead of all of those `have ... := simp`s. Also, I tried `instance : has_sizeof (exp V) := ⟨depth⟩` so that I wouldn't need to specify ```rel_tac := λ_ _, `[exact ⟨_, measure_wf depth⟩]```, but that didn't seem to work. Any suggestions?

#### [Simon Hudon (Sep 12 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133803664):
For the `have`, what if you had:

```lean
 dec_tac := `[simp] >> tactic.assumption,
```

in your `  using_well_founded` clause?

#### [Sean Leather (Sep 12 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133812958):
@**Simon Hudon** Good idea, but, unfortunately, that doesn't work.

#### [Sean Leather (Sep 12 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815702):
@**Mario Carneiro** Do you have any thoughts on the above in this thread? Basically, I want to write `lc'` without `have`ing to redeclare all of these theorems locally. Ideally, I would like to avoid `using_well_founded` at all, but that's secondary.

#### [Mario Carneiro (Sep 12 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815806):
did Simon's suggestion work?

#### [Sean Leather (Sep 12 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815820):
No.

#### [Kenny Lau (Sep 12 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815841):
what is `exp`?

#### [Mario Carneiro (Sep 12 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815845):
Why not? If all your proofs are `by simp` then it should work as a discharger

#### [Sean Leather (Sep 12 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815909):
```lean
assumption tactic failed
state:
V : Type,
_inst_1 : decidable_eq V,
lc' : exp V → Prop,
lc' : Π (_x : exp V), (Π (_y : exp V), has_well_founded.r _y _x → Prop) → Prop,
ef ea : exp V,
_F : Π (_y : exp V), has_well_founded.r _y (app ef ea) → Prop
⊢ measure depth ef (app ef ea)
```

#### [Mario Carneiro (Sep 12 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815914):
actually you should just use `` `[simp]`` as the discharger

#### [Sean Leather (Sep 12 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815924):
That was what I initially tried, too. No luck.

#### [Mario Carneiro (Sep 12 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815936):
make that `simp [measure, inv_image]`

#### [Sean Leather (Sep 12 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815950):
```lean
assumption tactic failed
state:
V : Type,
_inst_1 : decidable_eq V,
lc' : exp V → Prop,
lc' : Π (_x : exp V), (Π (_y : exp V), has_well_founded.r _y _x → Prop) → Prop,
ef ea : exp V,
_F : Π (_y : exp V), has_well_founded.r _y (app ef ea) → Prop
⊢ inv_image has_lt.lt depth ef (app ef ea)
```

#### [Kenny Lau (Sep 12 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816009):
I searched `inductive.*exp` but nothing came up

#### [Mario Carneiro (Sep 12 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816016):
it's in sean's repo

#### [Sean Leather (Sep 12 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816032):
```lean
`[simp [measure, inv_image]] >> tactic.assumption,
```

```lean
assumption tactic failed
state:
no goals
```

#### [Mario Carneiro (Sep 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816043):
and drop the `asssumption`

#### [Sean Leather (Sep 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816047):
Kenny, it's an inductive. But it's not relevant to the issue.

#### [Sean Leather (Sep 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816056):
Ah ha!

#### [Sean Leather (Sep 12 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816138):
That works. Thanks! Any way to simplify away the `using_well_founded`?

#### [Sean Leather (Sep 12 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816244):
Can I define my own instance of...?

```lean
class has_well_founded (α : Sort u) : Type u :=
(r : α → α → Prop) (wf : well_founded r)
```

#### [Sean Leather (Sep 12 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816270):
I mean, will defining an instance of `has_well_founded` allow me to remove `using_well_founded`?

#### [Simon Hudon (Sep 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133886977):
I think so. You may also have to set the priority of `has_well_founded_of_has_sizeof` to 0

#### [Chris Hughes (Sep 13 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133887243):
I did this for polynomials. I had to write `dec_tac := tactic.assumption ` everywhere, but other than that it worked.

