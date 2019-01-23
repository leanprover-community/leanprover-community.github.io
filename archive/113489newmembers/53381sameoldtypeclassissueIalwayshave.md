---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/53381sameoldtypeclassissueIalwayshave.html
---

## Stream: [new members](index.html)
### Topic: [same old typeclass issue I always have](53381sameoldtypeclassissueIalwayshave.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401453):
I really should write these down at some point; I'm always having to ask. I still can't quite control `haveI` `exactI` etc.

I saw in the code of one of my first year students the comment `what's with rw mul_self_iff_eq_one? can't it be used to prove 0 = 1?`. I thought this was a great comment. I encouraged the student to formalise their question in Lean. And then I tried to knock this off myself.

```lean
import data.real.basic

#check @mul_self_iff_eq_one
/-
mul_self_iff_eq_one : ∀ {α : Type u_1} [_inst_1 : group α] {a : α}, a * a = a ↔ a = 1
-/
lemma lean_is_broken : (∀ {α : Type*} [_inst_1 : group α] {a : α}, a * a = a ↔ a = 1)
                          → (0 : ℝ) = 1 := sorry -- fails to synthesize has_mul and has_one
```

damnit is there a trick to get past type class inference issues? It would be nice if students could be taught to answer their own questions like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401601):
put `by exactI` between the group instance and the point of use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 08 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401606):
The only typeclass instances that are used by the elaborator are the ones before the colon:
```lean
lemma l_i_b [this_gets_used] : ∀ [this_not], foo := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401729):
```quote
put `by exactI` between the group instance and the point of use
```
I tried that and I got a second error :-/

```lean
failed to synthesize type class instance for
α : Type ?,
_inst_1 : group α,
a : α
⊢ has_one α
state:
α : Type ?,
_inst_1 : group α,
a : α
⊢ Sort ?
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401774):
I know they can just create the term with `let X := mul_self_iff_eq_one` in a tactic mode proof -- I was just trying to explictly put it into the question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401896):
this works fine for me:
```
lemma lean_is_broken : (∀ {α : Type*} [_inst_1 : group α] {a : α}, by exactI a * a = a ↔ a = 1)
                          → (0 : ℕ) = 1 := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401899):
Maybe that's actually a better answer because then they can see the term and not the type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401903):
```lean
lemma lean_is_broken : (0 : ℝ) = 1 :=
begin
  let X := @mul_self_iff_eq_one,
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402028):
```lean
lemma lean_is_broken' : (∀ {α : Type*} [group α] {a : α}, by exactI a * a = a ↔ a = 1)
                          → (0 : ℝ) = 1 := sorry
```
Yup you're right, I don't know what I did :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402105):
@**Abhimanyu Pallavi Sudhir** There are some ideas about how to formalise your question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402292):
The best questions on this forum are ones where people actually post MWEs -- completely working Lean code which people can just cut and paste -- and then ask a question about it. But when I began to learn to formulate my basic questions in this way, I realised that I was starting to be able to answer them myself without having to ask at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402362):
The biggest wins are when, in the process of formalising it, you remember that what you're stuck on is actually something you already asked about earlier :-) Then you go and search the forums and read what was said at the time.

