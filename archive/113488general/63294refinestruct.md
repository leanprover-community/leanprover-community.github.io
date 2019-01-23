---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63294refinestruct.html
---

## Stream: [general](index.html)
### Topic: [refine_struct](63294refinestruct.html)

---

#### [Simon Hudon (May 31 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127375963):
@**Patrick Massot** I finally got around to writing a `refine_struct` tactic to generalize and simplify the automation of the `indexed_product` proofs. 

You can see it in action here https://github.com/cipher1024/lean-differential-topology/blob/master/src/indexed_product.lean.

You can use it as:

```
refine_struct { some_field := foo, .. },
repeat 
{ intro x,
  have_field,
  apply (field x) }
```

In short, `refine_struct` acts a bit like `refine` but tags every goal it produces with the name of the field that requires it. Then you can use tactics such as `have_field` / `let_field` to add an assumption or a local definition that stands for the accessor of the current field. You can also use `apply_field` if you just want to use it as a rule.

Does it look useful in this state? My next step would be to PR it into `mathlib`.

#### [Patrick Massot (May 31 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127379709):
Do you examples of using `have_field`, `let_field` and `aply_field`? I can see in the indexed product that you don't need to provide any data, which is already really nice, but I don't understand how the other tactics can be used

#### [Simon Hudon (May 31 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380010):
I you were to write the proof of semigroup by hand, it would go like this:

```
instance semigroup [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
begin
  refine_struct { .. },
  { intros x y i, apply_field, apply (x i), apply (y i) },
  { have_field,
    intros, funext, simp!, apply field }
end
```

#### [Simon Hudon (May 31 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380073):
The first proof constructs the semigroup operator and the second proves associativity. While the first proof only works for binary functions, the second one is pretty much what the tactic does.

#### [Simon Hudon (May 31 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380096):
In the second proof, `apply_field` would work if `funext` didn't discard the goal's tags

#### [Patrick Massot (May 31 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380238):
it seems `have_field` already discards it

#### [Patrick Massot (May 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380289):
why `simp!` rather than `dsimp`?

#### [Simon Hudon (May 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380290):
Yeah, you're right. I'll fix that

#### [Simon Hudon (May 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380298):
No reasons, I hadn't thought of using `dsimp` that way

#### [Patrick Massot (May 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380361):
just trying to say more precisely what Lean shoud do (I also tend to use `exact` when it works, instead of `apply` like you did)

#### [Patrick Massot (May 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380365):
anyway, it looks very nice

#### [Patrick Massot (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380461):
can you also do Kevin's `instance : comm_monoid ℕ+ ` using it?

#### [Simon Hudon (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380471):
I see. I would only use one command in that case but I wanted to demonstrate `apply_field`.

#### [Simon Hudon (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380474):
Can you send me a link?

#### [Simon Hudon (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380480):
Is it the transport problem?

#### [Patrick Massot (May 31 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380570):
no, building this instance on pnat, given we already have it on nat

#### [Simon Hudon (May 31 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380583):
It should be doable

#### [Patrick Massot (May 31 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380585):
https://github.com/leanprover/mathlib/blob/ad92a9ba47f417916aab365d13db653fa8991a84/data/pnat.lean#L52

#### [Simon Hudon (May 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380629):
Thanks, I'll have a look after dinner :)

#### [Patrick Massot (May 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380638):
Kevin complained about Lean not being smart enough to do it by itself

#### [Patrick Massot (May 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380644):
Is it already dinner time in Quebec?

#### [Simon Hudon (May 31 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380864):
Here's my first attempt:

```
instance : comm_monoid ℕ+ :=
begin
  refine_struct
    { mul       := λ m n : ℕ+, (⟨m.1 * n.1, mul_pos m.2 n.2⟩ : ℕ+),
      one       := succ_pnat 0, .. },
  repeat
  { have_field,
    intros, refine subtype.eq _, apply field }
end
```

#### [Simon Hudon (May 31 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380877):
It's a mistake to expect Lean to be smart. Lean is effective.

#### [Simon Hudon (May 31 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380883):
It is a bit early for dinner but my sister just had a baby so I'm giving her a hand

#### [Simon Hudon (May 31 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380942):
Ok, I gotta run now

#### [Patrick Massot (May 31 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380952):
thanks!

#### [Patrick Massot (May 31 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381384):
Ok, so obvisouly I can add 
```lean
meta def derive_field' : tactic unit :=
do b ← target >>= is_prop,
  if b then do
     field ← get_current_field,
     intros,
     `[refine subtype.eq _],
     applyc field
  else do skip
```
And the instance becomes
```lean
instance : comm_monoid ℕ+ :=
begin
  refine_struct
    { mul       := λ m n : ℕ+, (⟨m.1 * n.1, mul_pos m.2 n.2⟩ : ℕ+),
      one       := succ_pnat 0, .. } ; derive_field'
end
```

#### [Patrick Massot (May 31 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381392):
Question: can we start `derive_field` by some testing whether the target type is a pi type of a sub-type?

#### [Patrick Massot (May 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381462):
@**Kevin Buzzard** did you see that?

#### [Patrick Massot (May 31 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381491):
It's a mistake to expect Lean to be smart. Expect Simon to be smart.

#### [Simon Hudon (Jun 01 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391159):
Haha! That was not quite my point ...

#### [Mario Carneiro (Jun 01 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391298):
I think there is a good lesson in there though... "Computers don't prove theorems, people prove theorems"

#### [Simon Hudon (Jun 01 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391350):
Is this the slogan for the new National Reasoning Association?

#### [Mario Carneiro (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391370):
the Bot Lobby

#### [Simon Hudon (Jun 01 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391558):
Are you trying to emphasize the "people prove theorems" or the "computers are innocent"?

#### [Mario Carneiro (Jun 01 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391639):
In all seriousness, I would say it's important not to lose sight of the fact that computers do nothing more than what you tell them to

#### [Mario Carneiro (Jun 01 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391646):
so if you want magical tactics, you need magical people to support them

#### [Simon Hudon (Jun 01 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391662):
Yeah, my point exactly

#### [Kevin Buzzard (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391818):
or just sufficiently advanced technology

#### [Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391825):
No

#### [Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391826):
that's the point

#### [Mario Carneiro (Jun 01 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391868):
the sufficiently advanced tech has to come from us

#### [Simon Hudon (Jun 01 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391890):
The difference is that, from magic, you expect all your wildest dreams to be fulfilled while with effective technology, you expect a specific task to be handled. The technology is more useful because it's easier to know when it will work and when it won't

#### [Mario Carneiro (Jun 01 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391891):
it's one thing to expect miracles of "the CS community" in general, but that seems much less reasonable when you restrict scope to the <=10 people who are actually involved in writing tactics that you will see

#### [Kevin Buzzard (Jun 01 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127392976):
That's why I have to learn. But I have so many other things I want to do :-/

#### [Kevin Buzzard (Jun 01 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127392977):
It's wonderful being busy isn't it

#### [Simon Hudon (Jun 01 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127393040):
It sounds like a sarcastic comment but I have found that since my schedule has been filling up, I've been able to get things done quicker

#### [Patrick Massot (Jun 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127403167):
```quote
Question: can we start `derive_field` by some testing whether the target type is a pi type of a sub-type?
```
What about this question?

#### [Simon Hudon (Jun 01 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127412218):
Yes that can be done. Are those the only two situations where you'd like to use `derive_field`?

#### [Simon Hudon (Jun 01 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127419299):
I'm not sure what the best way to generalize `derive_field` is. I'm thinking of breaking it into `derive_method` and `derive_proof_of_law`. You could use them  as `refine_struct { .. } ; try { derive_field <|> derive_proof_of_law`. Then, we can add a tactic argument to `derive_proof_of_law` and use it as `derive_proof_of_law { intro }` or `derive_proof_of_law { refine subtype.eq _ }`. I don't know if that's simpler than having separate tactics for pi instances and for subtypes.

#### [Patrick Massot (Jun 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127424663):
maybe two separate tactics make more sense actually (one for pi and one for subtypes)

#### [Simon Hudon (Jun 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127424840):
The benefit over the previous automation is, even if you do need specialized code, the simplified code is much simpler than in the current version of `pi_instance`

#### [Mario Carneiro (Jun 01 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127425124):
I like this approach for exactly this reason. I wasn't a fan of `pi_instance` originally because it was a lot of code for a specialized problem; this puts most of the code in an obviously general setting and now `pi_instance` is both simpler and requires less input

