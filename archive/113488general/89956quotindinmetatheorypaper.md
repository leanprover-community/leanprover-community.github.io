---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89956quotindinmetatheorypaper.html
---

## Stream: [general](index.html)
### Topic: [quot.ind in metatheory paper](89956quotindinmetatheorypaper.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136716513):
In Section 2.7 of Mario's metatheory of Lean paper, I'm missing the fact that `quot.ind` is a axiom in Lean. Is this an omission, or is there an implicit claim here that `quot.ind` is derivable from the other constants/axioms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 29 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136717438):
I'm pretty sure that `quot.ind` is only derivable if the underlying type α is empty.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136718421):
That is too strong. You can at least prove it for `unit` by using that `x = unit.star` for every `x : unit` (and therefore `quot.mk x = quot.mk unit.star`). And I suspect that (classically) you might be able to do something when `α` is `fin n`, for example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136718605):
oh wait, maybe I'm mentally already using `quot.ind`here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136718915):
Oh yes, you're right. If `α` is nonempty, say `z : α`, and `r : α -> α -> Prop` then I can define 
```
quot' α r := option (quot α r) 
quot'.mk r x := some (quot.mk r x)
quot'.lift β f h (some x) := quot.lift β f h x
quot'.lift β f h none := f z
```
and then `quot'` satisfies the same rules as `quot`, including the reduction rule, but excluding `quot.ind`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136720482):
Also, the paper claims/proves that using only the inductive types `empty psigma psum ulift nonempty W eq acc` we can construct all others. If we remove `acc` from this list, so we only have the other 7 inductive types, do we know whether the ("ideal") definitional equality in the resulting system decidable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136733168):
@**Floris van Doorn** The reasoning behind only considering `quot.sound` an axiom and ignoring the others is that the others taken together are conservative, because we can take `quot A = A` and then all the axioms are valid except `quot.sound`. `quot.ind` is valid because `id` is surjective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136733213):
That said, I don't think this is common practice in logic, I should probably just call them all axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136733320):
I don't know if removing `acc` makes defeq decidable, but my guess is yes. Of course the counterexample in the paper uses `acc` essentially

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736293):
@**Mario Carneiro** I don't care about which of them you call constants and which you call axioms, my point is that you forgot to mention `quot.ind` in the paper (in the latest release and on the master branch). You only mention `quot.lift` as elimination principle.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736324):
Now I forget if `quot.rec` or `quot.lift` + `quot.ind` were used internally by lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736397):
`quot.rec` is defined in terms of `quot.lift` + `quot.ind`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736414):
ok, I'll update the paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736688):
The issue with the nontransitivity of algorithmic definitional equality using `quot` is only because if `α : Sort u` then `@quot α r : Sort u`, right? If we alternatively defined `@quot α r` to be in `Sort (max u 1)` (which would make more sense, compared to inductive types), then the nontransitivity using quotients goes away, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736701):
thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736801):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136737064):
All of the known examples of failure of transitivity involve some kind of subsingleton elimination, where an inductive type in Prop recurses over Type. So it is reasonable to conjecture that without `acc` and with `quot` out of `Prop` the algorithmic equality becomes transitive, and so coincides with ideal defeq which becomes decidable.

