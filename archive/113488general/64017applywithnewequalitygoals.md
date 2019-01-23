---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64017applywithnewequalitygoals.html
---

## Stream: [general](index.html)
### Topic: [apply with new equality goals](64017applywithnewequalitygoals.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558382):
Is there a tactic which works like `apply f` except that, if unifying the goal with the result type of `f` fails, it introduces new goals stating that the terms which don't unify are equal?
Example: I want to prove a statement like `f ⁻¹' (u ∩ v) = ∅`. Suppose I know I want to use `preimage_empty : f ⁻¹' ∅ = ∅`. I would like to obtain `u ∩ v = ∅` as a new goal without spelling it out explicitly (in a `have` or similar).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558494):
An interesting idea. You can effectively get the result by `refine cast _ f` and then `congr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558636):
I'm interested in this question but I don't understand the answer at all. @**Reid Barton** do your have a MWE so that Mario (or you) could be more explicit about to do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558645):
Let me try to cook one up and try out Mario's suggestion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558848):
OK, here's an example:
```lean
import data.set
open set

variables {α β : Type}
@[simp] lemma singleton_inter_singleton_eq_empty {x y : α} :
  ({x} ∩ {y} = (∅ : set α)) ↔ x ≠ y :=
by simp [singleton_inter_eq_empty]

example {f : β → α} {x y : α} (h : x ≠ y) : f ⁻¹' {x} ∩ f ⁻¹' {y} = ∅ :=
begin
  rw ←preimage_inter,
-- ⊢ f ⁻¹' ({x} ∩ {y}) = ∅
  have : {x} ∩ {y} = (∅ : set α) := by simpa using h,
  rw this, exact preimage_empty
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558894):
If `p` has type `f ⁻¹' ∅ = ∅` and the goal is `f ⁻¹' (u ∩ v) = ∅`, then `refine cast _ p` will give the goal `(f ⁻¹' (u ∩ v) = ∅) = (f ⁻¹' ∅ = ∅)` and `congr` will skip all the same stuff to get to `u ∩ v = ∅`. Of course this has the usual `congr` caveats about going too far, but it seems like the right idea for Reid's problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558946):
`refine cast _ preimage_empty` guessed to replace the wrong part, though, leaving `⊢ ?m_3 ⁻¹' ∅ = ∅ = (f ⁻¹' ({x} ∩ {y}) = ∅)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559023):
no that's correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559026):
what happens after `congr`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559043):
`congr` errors with "tactic failed, there are no goals to be solved" (even though there were 4 goals)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559090):
what is the first goal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559104):
the goals are `⊢ Type ?`, `⊢ Type ?`, `⊢ ?m_1 → ?m_2`, and what I wrote above

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559106):
I assume they are describing the type of `?m_3`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559107):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559109):
You don't want to run `congr` on those goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559159):
you have to cycle through them or set up the refine right, I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559169):
I'm confused though because I thought it was the `{x} ∩ {y}` part I wanted to replace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559218):
The goal is to do it in two stages. The first stage replaces your goal with an equality between the "apply" theorem and the goal, and the second stage simplifies the equality by congruence until you just have the part(s) that aren't defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559225):
`cast` has the type `A = B -> A -> B`, so `cast _ p` where `p : A` yields the goal `A = B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559234):
Oh I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559235):
I need to tell it to solve the third goal with `f`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559236):
You could also try specifying `f` for the sake of the example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559276):
i.e. `refine cast _ (@preimage_empty _ _ f)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559289):
I just did `exact β, exact α, exact f, congr,`, and that also works, and leaves me with `⊢ ∅ = {x} ∩ {y}` like I wanted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559306):
Well, I would have preferred `⊢ {x} ∩ {y} = ∅` :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559349):
I'm not sure if congr will automatically unify when it can, but that would fix these metavars without your intervention

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559353):
I think `eq.mp` and `eq.mpr` are the same as `cast` and allow you to get the orientation right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559421):
Yes, `refine cast _ preimage_empty, swap 4, congr` also worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559424):
and `eq.mpr` eliminates the need for `symmetry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559473):
Final version is to replace the last two lines with
```lean
  refine eq.mpr _ preimage_empty, swap 4, congr,
-- ⊢ {x} ∩ {y} = ∅
  simpa using h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559482):
This is helpful, I haven't used congr before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559542):
The `swap` business reminds me of those pairs of tactics which differ only in how the resulting goals get ordered; I guess `refine` has no such companion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559594):
no, it just creates all metavars in the order it finds them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559606):
There is enough going on here that it would not be unreasonable to have a tactic for it. Keep in mind though that it's not like apply in that it can't guess how many args to apply

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559612):
@**Simon Hudon** we need you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559657):
if you don't get the args right your equality will be some statement like (\forall x. ...) = (f 0 = 0) and congr will not do anything useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559662):
Right, I realized as I was asking the question that I don't really know how `apply` figures out how many args to insert

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559679):
I think it just applies as many as it can, or maybe counts how many nested pi are in the theorem type vs the target type and applies the difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125568801):
@**Patrick Massot** What would you imagine a tactic doing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125568812):
Ideally, the first message of this thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125572764):
Something like this?

```
meta def bridge_gap (r : parse texpr) : parse ("using" *> smallnat)? -> tactic unit
| none := refine ``(cast _ %%r) >> congr
| (some n) := refine ``(cast _ %%r) >> congr_n n
```

This way you can do `bridge_gap rule using n` to limit the depth of `congr` or just `bridge_gap rule`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125572815):
I'm not sure of the name though. Maybe something like `fit` or `adapt_to` would be better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125572849):
I don't get why you need `swap` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125573226):
Can you do the example with it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125573428):
I'm giving it a try. My computer is not helping today

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125575245):
Ok I think I see why `swap` was necessary. Here's a proof and a tactic that work:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125575289):
```lean
example {f : β → α} {x y : α} (h : x ≠ y) : f ⁻¹' {x} ∩ f ⁻¹' {y} = ∅ :=
begin
  have : {x} ∩ {y} = (∅ : set α) := by simpa using h,
  bridge_gap preimage_empty,
  rw [←preimage_inter,this],
end
```

```lean
namespace tactic
namespace interactive

open interactive interactive.types lean.parser
local postfix `?`:9001 := optional
local postfix *:9001 := many

meta def bridge_gap (sym : parse (tk "←")?) (r : parse texpr) (n : parse (tk "using" *> small_nat)?) : tactic unit :=
do v ← mk_mvar,
   if sym.is_none
     then refine ``(eq.mp %%v %%r)
     else refine ``(eq.mpr %%v %%r),
   gs ← get_goals,
   set_goals [v],
   (option.cases_on n congr congr_n : tactic unit),
   gs' ← get_goals,
   set_goals $ gs' ++ gs

end interactive
end tactic
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125575597):
I added an option to allow `bridge_gap ← preimage_empty` but the parser doesn't seem to like it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576655):
Ok, it's now working. I put it here https://gist.github.com/cipher1024/0d3328135367269cc35f74f43ecbb302 if you want to use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576871):
Let's get to 20! (I mean 20, not 20!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576890):
noooo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576902):
my backlog is so long...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576905):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576908):
He'll go hermit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125577105):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125577350):
```quote
Let's get to 20! (I mean 20, not 20!)
```
20 what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125577366):
20 opened PR to mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125578498):
Ah! I didn't open a PR. I don't know if it's generally useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125578578):
Or rather, I don't know if there's interest for this tactic to be in mathlib rather than in one particular project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Apr 23 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125586345):
20 :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125595892):
@**Simon Hudon**  Is this really a problem to have too many tactics in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596043):
I think it's good to prioritize the tactics that will have the most positive impact for the users of `mathlib`. On one hand, that makes better use of Mario's time and on the other hand, it minimizes the effort required to understand `mathlib`'s features

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596052):
I have a new idea for you (which would simplify my current work). Assume `(*) : R → R → R` and `[is_associative (*))]`. I have an expression like `(a₁*(a₂*a₃)*a₄)*((a₅*a₆)*a₇)` (maybe I'm in conv mode so I only see this expression). I'd like to write `simon_new_magic_trick 4 5` and get an expression where parentheses are rearranged so that I see `(a₄*a₅)` in the middle.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596095):
And I'm going to sleep (2:33 am here)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596180):
We can talk about it some more tomorrow. Do you want it as a preparation for something in particular (e.g. `rw`) or do you foresee using it in combination with multiple other tactics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596233):
As for syntax, I could think of calling it `ac_zoom a₄*a₅` (in case we want to consider commutativity too) in `conv` mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596308):
that does seem useful. I guess the algebraic normalization functionality got put by the wayside for lean 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596313):
how about `ac_focus`? that sounds pretty neat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596321):
more generally being able to rewrite declaratively with wildcards like `_` would be sweet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596330):
> I guess the algebraic normalization functionality got put by the wayside for lean 4

What are you referring to?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596372):
```quote
more generally being able to rewrite declaratively with wildcards like `_` would be sweet
```
Can you elaborate a bit on what that would look like?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596379):
Alternatively, the syntax could be an expression like `ac_zoom _*a₄*a₅` and this is ac-unified with the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596441):
you have `(a1 * (a2 * (a3 * (a4 * (a5 * a6)))))`, you want `a1 * a2 * (a3 * a4) * a5 * a6`, hmm, maybe something like `mytactic _ * _ * (a3 * a4) * _ * _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596444):
perhaps you could allow less `_` than variables and that would make the constraint search easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596455):
I remember hearing awhile back that there was going to be a lot of algebra machinery going in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596459):
you could get by with only one `_` on left and right with assoc only, and just one `_` on left or right with ac

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596503):
if there are too many holes you can just fill them eagerly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596506):
and fail if there aren't enough terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596511):
commutativity only reasoning seems trickier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596583):
You mean without associativity? Why is it trickier?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596671):
:( too bad floating point math is non-associative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 24 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596776):
@**Simon Hudon** Thanks, this `bridge_gap` worked in my real project too.
Only I can't seem to get the ← feature to actually work (I tried `bridge_gap ←preimage_empty` with all combinations of space or no space around the arrow). But it works fine if I change ← to - for some reason.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 24 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596793):
With ←, I get a parse error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 24 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596811):
"error: expression expected", and then it continues in a confused state

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596814):
I had a hard time too with that notation. I don't understand why. It works fine with `rw`. Have you tried `<-`? That worked better for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 24 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596825):
Yes, that works... something about the arrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596872):
I decided not to spend more time investigating that issue because `<-` works. It's still annoying

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597061):
You have to use `tk "<-"` instead of `tk "←"`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597070):
by some weird setup on lean's part, the token that lean knows as `<-` is parsed from both `<-` and `←`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597074):
so if you write `tk "←"` it doesn't work at all, and `tk "<-"` works with both `<-` and `←`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597075):
Ah! I bet that was a fun lesson for you to learn!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597116):
Btw, can you think of a better name than `bridge_gap`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597120):
I expect this is in part because this is a built in notation (like the forward arrow for functions), since it shows up in `do` notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597133):
That makes sense. I'm actually glad that notation is built in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597137):
Also I think that the polarity of `<-` should be reversed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597139):
`eq.mpr` is the forward one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597186):
I'm not, if I had my way all notation would be declared in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597187):
maybe I'll get it in lean 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597189):
but it does seem like a really hard one to do generically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597202):
`convert`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597243):
That's a bit too close to `conv`, no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597245):
to be fair it's actually doing a very similar thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597248):
That's true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597254):
every time i see `conv` i think it's talking about convolution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597256):
Is it something you'd like to have in `mathlib` btw?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597260):
little tactics like this are not a big deal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597312):
go right ahead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597315):
Cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597328):
I've been busy with my other obligations this past week, but I promise I'll finish updating mathlib and get on those PRs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597577):
I think the amount of work you've put on `mathlib` is actually amazing. I think you shouldn't feel like you have to apologize

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 24 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125605769):
[22](/user_uploads/3121/bGfjZkmMdvJegOrpJ6MnVKEB/22.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 24 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125605781):
... for anyone keeping count.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 24 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606413):
@**Mario Carneiro** wishing you luck. I just want to thank you for everything you're doing. Please don't feel any pressure from the game these guys are playing...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 24 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606414):
/me wouldn't want another hermit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 24 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606808):
I haven't followed the entire conversation, but, to be clear, I think the PR count should not be taken as a backlog waiting to be completed but rather as a sign of interest in the growth of mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 24 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606862):
Personally, I have my own backlog of things I want to contribute, but I'm waiting (patiently, mind you) for stabilization of mathlib wrt Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609412):
I absolutely agree. I put in a couple of PR's for docs recently and once I did that I felt my job was done -- people can even see the docs if they want. There was no need at all to pester anyone to accept the PR's and I had plenty of other things to worry about. The fact that Lean doesn't keep changing at the minute is also really nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609414):
because I am not typing `leanpkg upgrade` all the time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609417):
so if I really wanted something in mathlib that wasn't there yet, I could just edit the mathlib in `_target` in my project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609536):
Yes, this is what I did in https://github.com/PatrickMassot/mathlib/tree/wlog_ext  (which is upstream + 2 PR)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 24 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125616698):
I like `bridge_gap` (or whatever it ends up called). I had a primitive version that I was calling `its`. That is, I'd write `its X` as a generalised version of `exact X`, and I would be left with whatever goals were required to unify `X` with the actual goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 24 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125616701):
(of course, apostrophe man would probably complain)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 24 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125616706):
I'm certainly planning in discarding `its` in favour of this one once it's in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125619917):
how about `itis`? Signed, Apostrophe man.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125620284):
What a cool super hero name :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125620361):
I submitted as `convert`. I'm not sure why `itis` works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 24 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125620365):
I'm wondering if `refine_congr` would be a good name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125631877):
[23](/user_uploads/3121/QoX4a9GPQ88G78zBt2MfjLzX/2018-04-25.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125631910):
Now I need to sleep

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125632009):
it would be less than 23 if you finished all your [WIPs] :)

