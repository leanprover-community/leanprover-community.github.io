---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44061rewriteLHSisamvar.html
---

## [general](index.html)
### [rewrite LHS is a mvar](44061rewriteLHSisamvar.html)

#### [Mario Carneiro (Mar 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653459):
```
example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw h
-- rewrite tactic failed, lemma lhs is a metavariable
example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw ← h
-- rewrite tactic failed, lemma lhs is a metavariable
example (h : ∀ a : nat, 0 = a) : 0 = 2 := by rw h --ok
example (h : ∀ a : nat, 0 = a) : 0 = 2 := by rw ← h
-- rewrite tactic failed, did not find instance of the pattern in the target expression
--   ?m_1
```
rewrite talks about LHS but apparently it doesn't take into account symmetry

#### [Kevin Buzzard (Mar 13 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653641):
`example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw h 2 -- succeeds!`

#### [Kevin Buzzard (Mar 13 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653703):
oh this is more complicated than I thought. Of course that succeeds.

#### [Kevin Buzzard (Mar 13 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653754):
That first example is really hard. I can see why it fails. How should it have a clue what to set a?

#### [Mario Carneiro (Mar 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653809):
Actually, in my view none of them should fail. `rw` actually should not have any issues with the LHS being an arbitrary variable; it will just trigger very easily.

#### [Kevin Buzzard (Mar 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653812):
How is `rw` supposed to do the first one?

#### [Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653819):
It has a tool for showing an arbitrary thing is 0, but it has to match 0 = 2

#### [Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653820):
I think if I were rw I would let a be the first nat I found in the goal

#### [Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653822):
which is 0

#### [Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653827):
and then rewrite and get `0=2` and then decide I failed

#### [Kevin Buzzard (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653880):
Isn't that how it works? I just spent some time trying to figure this out.

#### [Mario Carneiro (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653883):
compare to when I wrap everything in `id`:
```
example (h : ∀ a : nat, id a = id 0) : id 0 = id 2 := by rw h -- ⊢ id 0 = id 2
example (h : ∀ a : nat, id a = id 0) : id 0 = id 2 := by rw ← h -- done
example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw h -- done
example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw ← h -- ⊢ id 0 = id 2
```

#### [Kevin Buzzard (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653892):
As I just said, I am unsurprised by the first one.

#### [Kevin Buzzard (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653895):
Why do you think it should work?

#### [Mario Carneiro (Mar 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653906):
`rw` should trigger on the first matching occurrence of the pattern. If the LHS is a metavar, that's just the first type correct subterm

#### [Kevin Buzzard (Mar 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653909):
and indeed this is a=0 for the first one

#### [Kevin Buzzard (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653951):
it matches `id 0` so sets a=0

#### [Kevin Buzzard (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653954):
and now you're doomed

#### [Mario Carneiro (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653958):
No, that's intended behavior

#### [Mario Carneiro (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653960):
I'm not expecting it to solve the goal, but it shouldn't fail

#### [Kevin Buzzard (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653962):
Aah I see.

#### [Mario Carneiro (Mar 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653975):
the question is why I get a bunch of weird and inconsistent failures when I remove the `id`

#### [Kevin Buzzard (Mar 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653981):
```
example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw ← h
-- rewrite tactic failed, lemma lhs is a metavariable
example (h' : ∀ a : nat, 0 = a) : 0 = 2 := by rw h'
-- succeeds
```

#### [Kevin Buzzard (Mar 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653983):
I had imagined these were synonymous

#### [Mario Carneiro (Mar 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654025):
exactly my point

#### [Mario Carneiro (Mar 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654032):
there's a funny lhs metavar check that literally checks *the left side* even if that's the destination, not the source

#### [Kevin Buzzard (Mar 13 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654035):
I see. The issue is not that they fail, it's how they fail. I understand your point now.

#### [Mario Carneiro (Mar 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654103):
and the final example is even stranger - `example (h : ∀ a : nat, 0 = a) : 0 = 2 := by rw ← h` is using backwards rewrite to circumvent the buggy lhs metavar check, and instead hits a search bug, probably what the lhs metavar check was trying to avoid

#### [Kevin Buzzard (Mar 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654110):
`example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw ← h -- ⊢ id 0 = id 2`

#### [Kevin Buzzard (Mar 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654115):
I have no idea what to do with this one. It seems there are two reasonable ways to behave?

#### [Mario Carneiro (Mar 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654120):
I would argue that all the `id` examples are consistent

#### [Kevin Buzzard (Mar 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654163):
First I could spot the id 0 on the LHS and just replace it with `id a`

#### [Mario Carneiro (Mar 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654169):
Here, just like the forward rewrite version, it is rewriting `id ?m` -> `id 0` and spots the first matching pattern `id 0`, so `?m := 0`

#### [Kevin Buzzard (Mar 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654178):
oh ha ha I missed the \l

#### [Kevin Buzzard (Mar 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654182):
It's this one that confuses me:

#### [Kevin Buzzard (Mar 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654183):
`example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw h -- done`

#### [Kevin Buzzard (Mar 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654234):
Presumably it doesn't spot the `id 0` in the goal and then announce that it's going to replace it with `id ?m`

#### [Sebastian Ullrich (Mar 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654238):
`kabstract` with a metavar will only match other metavars, it's probably trying to avoid that

#### [Kevin Buzzard (Mar 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654243):
instead it has to decide what to do with the `a` first

#### [Mario Carneiro (Mar 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654262):
why is that? As I said it seems inconsistent with the `id ?m` behavior. Is it being special cased? I feel like you would have to work hard to make that happen

#### [Mario Carneiro (Mar 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654329):
@**Kevin Buzzard** actually that's exactly what it does. It is rewriting `id 0` -> `id ?m`, and spots the first matching pattern `id 0`, but `?m` is unconstrained by this and the result is `id ?m = id 2`. The proof is finished with the automatic `refl` after `rw`

#### [Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654360):
ha ha

#### [Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654374):
yes I just noticed that this works too:

#### [Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654377):
`example (h : ∀ a : nat, 0 = a) : 2 = 0 := by rw h -- done`

#### [Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654386):
and here we really seem to have no option other than to leave the metavariable alone and make the match

#### [Sebastian Ullrich (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654477):
@**Mario Carneiro** It's using keyed matching, which uses structural equality for the head

