---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56063createalias.html
---

## Stream: [general](index.html)
### Topic: [create alias](56063createalias.html)

---

#### [Zesen Qian (Aug 17 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309111):
How can I create an alias to anther declaration? Say, in my namespace `foo` I want to create a `true` such that users can see `foo.true` and the prover treats it equally to `true` from core.

#### [Mario Carneiro (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309539):
equally is hard, but there are a few ways to get close

#### [Zesen Qian (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309551):
right now I'm thinking about `def` with `attribute [reducible]`

#### [Mario Carneiro (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309556):
`@[reducible] def` makes `rw` and `simp` see through the definition, as well as typeclass inference

#### [Zesen Qian (Aug 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309559):
I guess that should work, but really I'm looking for shorter path.

#### [Mario Carneiro (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309566):
`abbreviation` does something similar with kernel reduction, I'm not sure exactly

#### [Mario Carneiro (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309572):
what do you mean "shorter path"?

#### [Zesen Qian (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309578):
I mean, less characters to type.

#### [Zesen Qian (Aug 17 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309584):
alias true = true would be the best.

#### [Mario Carneiro (Aug 17 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309623):
mathlib has an `alias` tactic, but it doesn't set `reducible`

#### [Mario Carneiro (Aug 17 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309646):
what's wrong with just `def true := true`?

#### [Chris Hughes (Aug 17 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309652):
`notation`?

#### [Mario Carneiro (Aug 17 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309684):
also, what is your use case? I wrote `alias` to support alias constructions but it doesn't get much use since I specifically try to avoid aliases

#### [Zesen Qian (Aug 17 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309741):
I need something in my namespace that's definitionally equal to `true`

#### [Zesen Qian (Aug 17 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309775):
@**Chris Hughes** I haven't used notation before, can you give an example?

#### [Mario Carneiro (Aug 17 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309783):
`def true := true` is the easiest way to accomplish that

#### [Mario Carneiro (Aug 17 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309796):
``notation `true'` := true``

#### [Mario Carneiro (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309850):
but notation is not a def

#### [Mario Carneiro (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309857):
so there will be no `foo.true'` that way

#### [Zesen Qian (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309863):
yeah, I realize that.

#### [Zesen Qian (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309876):
ok, so the best way is `reducible` `def`.

#### [Mario Carneiro (Aug 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309877):
but you still haven't said why you need this

#### [Zesen Qian (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309894):
I'm doing some metaprogramming. A proof given by SMT solvers is mapped to a proof in lean.

#### [Zesen Qian (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309899):
so a `true` in source proof mapped to `true` in lean.

#### [Mario Carneiro (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309904):
then just map to the real `true`

#### [Zesen Qian (Aug 17 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309912):
I have a file containing all stuff that source proofs will refer.

#### [Zesen Qian (Aug 17 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309960):
so I don't need to write the mapping myself. The meta program will look it up itself.

#### [Mario Carneiro (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132309992):
but then your output statements will just be needlessly encoded with reducible defs

#### [Mario Carneiro (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310001):
you are writing the mapping just by giving these defs

#### [Zesen Qian (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310021):
yeah, but that's not big problem, no one is gonna read the proof as long as it's correct.

#### [Zesen Qian (Aug 17 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310024):
machine generated proofs are never intended for people.

#### [Mario Carneiro (Aug 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310070):
heh, you would be surprised

#### [Zesen Qian (Aug 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310081):
I hope I will never be suprised.

#### [Zesen Qian (Aug 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310090):
anyway, I'm going `reducible` `def`s.

#### [Mario Carneiro (Aug 17 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310128):
I don't think there is any point in using reducible here though. if it's in the proof term it's in the proof term

#### [Zesen Qian (Aug 17 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310183):
I don't know what you meant.

#### [Mario Carneiro (Aug 17 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310184):
you aren't using it with rw or anything so it won't be unfolded

#### [Mario Carneiro (Aug 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310330):
if you put together a proof using these variant definitions, it will make no difference to the type-correctness as long as it's defeq, and a regular def accomplishes that

#### [Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310459):
I think you are right.

#### [Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310460):
I can now get it work without reducible, but I will see it can keep working.

#### [Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310466):
yeah, but I'm thinking about if the user provides me with the "real" `true`.

#### [Zesen Qian (Aug 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310486):
and when a proof depends on the definitional equality between these two `true`, will that still work?

#### [Mario Carneiro (Aug 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310563):
yes, that's what defeq does

#### [Zesen Qian (Aug 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310571):
ok then!

#### [Mario Carneiro (Aug 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310576):
you can replace `true` with `true'` anywhere in the proof with no changes

#### [Zesen Qian (Aug 17 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/create%20alias/near/132310605):
ok. I guess I overlooked lean's ability of identifying equalities.

