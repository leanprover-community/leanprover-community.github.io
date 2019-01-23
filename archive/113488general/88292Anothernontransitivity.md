---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88292Anothernontransitivity.html
---

## Stream: [general](index.html)
### Topic: [Another non-transitivity](88292Anothernontransitivity.html)

---


{% raw %}
#### [ Mario Carneiro (Mar 02 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123163815):
While trying to prove that lean doesn't have any other sources of definitional non-transitivity besides K-like eliminators, I discovered another one, quotients of propositions:
```
variables (α : Prop) (r : α → α → Prop) (β : Sort*)
  (f : α → β) (H : Π (a b : α), r a b → f a = f b) (a : α)
example : quot.lift f H (quot.mk r a) = f a := rfl
example (h : quot r) : quot.lift f H h = quot.lift f H (quot.mk r a) := congr rfl rfl
example (h : quot r) : quot.lift f H h = f a := sorry
```

#### [ Mario Carneiro (Mar 02 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123163882):
Note that a quotient of a proposition is always useless, because propositions are already subsingletons. Maybe we should just make `quot` always live in `Type`, even if the input is a `Prop`?

#### [ Simon Hudon (Mar 02 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164192):
What do we gain by doing that?

#### [ Mario Carneiro (Mar 02 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164194):
doing what

#### [ Simon Hudon (Mar 02 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164234):
Putting `quot` in `Type` even when the input is a `Prop`

#### [ Mario Carneiro (Mar 02 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164242):
The source of non-transitivity is when the major premise of an iota rule is a proof, while the resulting type is a `Type`

#### [ Mario Carneiro (Mar 02 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164248):
This happens exactly when the inductive type is a `Prop` but it "large eliminates"

#### [ Simon Hudon (Mar 02 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164293):
Is the kind of price that you pay only when you're in that situation?

#### [ Mario Carneiro (Mar 02 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164295):
And `quot p` acts like a large eliminator in this case because `lift` has target `Type`

#### [ Mario Carneiro (Mar 02 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164305):
The issue is that you can arbitrarily muck with the major premise and extract data from it even though it's a prop

#### [ Simon Hudon (Mar 02 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164351):
A bit as if your the `quot` framework acted as an axiom of choice?

#### [ Mario Carneiro (Mar 02 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164355):
Any other time it's not a problem - if the type itself is in `Type` then the major premise is not subject to proof irrelevance, and if it is a small eliminator then anything that results will also be subject to proof irrelevance

#### [ Mario Carneiro (Mar 02 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164375):
It's not quite axiom of choice level, because large elimination is only sound in the first place when there is exactly one thing that can be in the major premise... but that's only up to definitional equality and there are potentially many ways to write it

#### [ Mario Carneiro (Mar 02 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164377):
This is where undecidability of defeq arises

#### [ Simon Hudon (Mar 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164426):
The thing I'm worried about is if you build something on top of `quot` and you need functions of type `Sort u -> Sort u`, putting `quot` in `Type` may require you to have complicated universe expressions and force you to deal with types that live in different universes.

#### [ Mario Carneiro (Mar 02 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164432):
For example, consider the definitional equality `quot.lift f H h = f a` in the example above. Where would it get `a` from to perform that reduction?

#### [ Mario Carneiro (Mar 02 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164436):
It's a proof, so it is "unique"... but that doesn't make the problem easier

#### [ Mario Carneiro (Mar 02 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164477):
The other alternative, which was actually in use for a while, is to have `quot : Type u -> Type u` like so many other things

#### [ Mario Carneiro (Mar 02 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164479):
I think it was generalized to Sort because no one saw any harm in it

#### [ Simon Hudon (Mar 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164526):
Yeah I see. I find myself siding with `Type u -> Type u`. I wonder if that rules out anything useful

#### [ Mario Carneiro (Mar 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164532):
You can recover `quot` on `Sort`, without quite as many definitional rules, by simply using `quot (plift p)`

#### [ Simon Hudon (Mar 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164583):
Oh nice! I like that. In the general case, `quot` is cheap (from a design perspective) and you only pay a price for exotic uses

#### [ Mario Carneiro (Mar 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164591):
I think I would prefer `quot : Sort u -> Sort (max 1 u)` since it is the axiomatic one, and `quotient : Type u -> Type u`. This should avoid most universe unification problems

#### [ Simon Hudon (Mar 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164594):
Yeah, you're right

#### [ Simon Hudon (Mar 02 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164633):
Just to be sure. You're saying that this example demonstrate undecidability of defeq. Does that mean that the current type checker does not terminate on this example?

#### [ Mario Carneiro (Mar 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164639):
No, the current typechecker does not accept those definitional equalities

#### [ Mario Carneiro (Mar 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164640):
even though they are composed from acceptable definitional equalities

#### [ Simon Hudon (Mar 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164684):
Right but it is a known state of affair that definitional equalities are not transitive, no?

#### [ Mario Carneiro (Mar 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164690):
Right, hence "another non-transitivity"

#### [ Simon Hudon (Mar 02 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164732):
What I'm asking is why do we need to avoid this one?

#### [ Mario Carneiro (Mar 02 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164854):
Because it is preferable to have a reasonable story for how defeq works and to only break it with good reason. (Full disclosure: this is also going to add another page to my paper, for a dumb edge case that I am positive is currently completely unused)

#### [ Mario Carneiro (Mar 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164894):
In fact, I've even had conversations discussing putting `acc` in Type to avoid exactly this problem, and that's a much bigger deal

#### [ Simon Hudon (Mar 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164895):
(About the disclosure: are you telling me that you're being paid by the big definitional equality industry?)

#### [ Mario Carneiro (Mar 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164902):
I guess I am, in a way...

#### [ Simon Hudon (Mar 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123164904):
What's the consequence of putting `acc` in Type?

#### [ Mario Carneiro (Mar 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123169571):
Again, it eliminates issues caused by large elimination. If `acc` was in Type and `quot` was in type, then definitional equality would be decidable, transitive, all that good stuff

#### [ Gabriel Ebner (Mar 02 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123174245):
I had already submitted a PR to move `acc` into `Type` once: https://github.com/leanprover/lean/pull/1803  But of course it got rejected.  The comments on the PR are an interesting read, though.

#### [ Gabriel Ebner (Mar 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123174616):
Just if anybody else wondered, `congr rfl rfl` in the original post is definitionally equal to `rfl`.  And if I see this correctly, my PR would not fix this issue.

#### [ Sean Leather (Mar 02 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175304):
https://github.com/leanprover/lean/pull/1803#issuecomment-325014390 :

> If "several people" == @digama0, then it doesn't count :)

Ouch! :open_mouth:

#### [ Patrick Massot (Mar 02 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175720):
Yes, I'm very worried by that paper @**Mario Carneiro** is writing. I don't  understand anything about type theory but, to me, it sounds like Mario is scientifically documenting some weakness of Lean (which is irrelevant to end users and doesn't allow to prove false). In principle this is fair. But is it a smart diplomatic move? How could that improve the little "communication issue"?

#### [ Patrick Massot (Mar 02 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175872):
I have a recurrent question: should I learn what "subsingleton" means? If yes, where?

#### [ Chris Hughes (Mar 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175881):
Subsingleton just means a type with 0 or 1 elements

#### [ Patrick Massot (Mar 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175888):
I understand that bit. It doesn't explain why it comes up all the time, always with "elimination" in the same neighborhood

#### [ Simon Hudon (Mar 02 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175932):
In the context of Lean, that includes any `Prop`. I believe it's a generalization of proof irrelevance.

#### [ Simon Hudon (Mar 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175944):
When checking if two terms are the same, you ignore proof terms and you can ignore subsingleton types.

#### [ Patrick Massot (Mar 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175985):
I see

#### [ Patrick Massot (Mar 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123175987):
Thanks

#### [ Gabriel Ebner (Mar 02 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178245):
@**Simon Hudon** That's just proof irrelevance.  @**Patrick Massot** Subsingleton is a type with at most one element (we have the subsingleton type class for that).  Subsingleton elimination is something slightly different: usually, inductive data types in Prop only allow you to eliminate into Prop.  For example, the recursor for ∃ only allows you to obtain propositions, if you could eliminate into Type, then you could extract the witness and thereby prove choice.  Subsingleton elimination is now a relaxation of this restriction: in some cases it is perfectly sound for the recursor of an inductive proposition to eliminate into Type: intuitively, if you don't get any additional "data" when eliminating (such as constructor arguments that are in Type, or which constructor of the inductive proposition is used).  For example, ∧, false, true, all eliminate into Type.

#### [ Patrick Massot (Mar 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178735):
Thanks for your explanation but I'm afraid I'm missing too much background. Can you explain what "∧  eliminate into Type" means? Maybe with an example? I know about `and.elim` but I don't see any Type here, only Prop.

#### [ Kevin Buzzard (Mar 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178810):
```quote
Thanks for your explanation but I'm afraid I'm missing too much background. Can you explain what "∧  eliminate into Type" means? Maybe with an example? I know about `and.elim` but I don't see any Type here, only Prop.
```
look at `and.rec`

#### [ Kevin Buzzard (Mar 02 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123178860):
Compare with `Exists.rec` [sorry, typo fixed]

#### [ Gabriel Ebner (Mar 02 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123179178):
Example:
```lean
-- and eliminates into Type, this means that in the
-- recursor we can return values e.g. of type nat : Type
#check @and.rec true true ℕ (λ h₁ h₂, 5) ⟨⟨⟩,⟨⟩⟩

-- however Exists does not eliminate into Type (just 
-- into Prop), we cannot return values of type nat : Type,
-- just propositions
#check @Exists.rec _ (λ x : ℤ, true) ℕ (λ witness h, 5) ⟨1, trivial⟩
             -- could use witness here, so forbidden ^
```
The second example fails, since nat is not in Prop.

#### [ Patrick Massot (Mar 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123180791):
Thank you very much. I was confused by the type of `and.elim`. Since it only wraps `and.rec`, why do we have a different type here?

#### [ Gabriel Ebner (Mar 02 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123182111):
The `.rec` one is the one generated by the kernel, and is the only one that matters (for foundational purposes).  I don't know the reason behind the `.elim` redefinitions, my best guess is that they correspond to the inference rules in natural deduction (which obviously only talk about Prop).

#### [ Simon Hudon (Mar 02 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Another%20non-transitivity/near/123194465):
Thanks for correcting my mistake


{% endraw %}
