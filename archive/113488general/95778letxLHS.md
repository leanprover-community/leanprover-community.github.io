---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95778letxLHS.html
---

## Stream: [general](index.html)
### Topic: [let x = LHS](95778letxLHS.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756807):
As sometimes happens, my goal is currently `FPTB.res BU _ _ s = si i` and my proof that these two things are equal is going to involve showing that they're both the unique object with some property. I am in tactic mode. I need to hence feed both sides into a bunch of machinery (the proofs that each side has the property are quite different). The underscores are proofs. I want to write "now let x be the left hand side" just to make things easier to handle, but the proof terms are probably nightmares. I am hoping there's a cute one-liner which lets me do this, based on the fact that I sometimes use `to_lhs` in conv mode. But I don't think `to_lhs` exists in tactic mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756812):
does `let x := FPTB.res BU _ _ s` work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756868):
Here's a cute one-liner: `show let x := _ in x = si i, intro x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756914):
can you do the same sort of thing with generalize?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756961):
i don't have lean on this computer so i can't check myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757001):
It's not a bad idea, but no, `generalize` does not introduce let binders, only regular variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757008):
The best part about `generalize` with `let` is that it doesn't suffer the same problems with type incorrectness as `generalize` itself, since the replacement is definitional

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757409):
```quote
does `let x := FPTB.res BU _ _ s` work?
```
It works in the sense that no error appears, but all of a sudden I have 4 goals not 1.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757449):
```quote
Here's a cute one-liner: `show let x := _ in x = si i, intro x`
```
`show tactic failed`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757454):
and what if both sides had suppressed-proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757455):
This is hardly a serious issue, I mean I could turn proofs on and just copy what it said I guess...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757456):
What order are the goals? `let x := FPTB.res BU _ _ s, show x = si i` should kill most of the auxiliary goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757495):
you should be able to do this by unification, no need to copy down those proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757498):
does `change` give a better error message than `show` in the one-liner?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757505):
wooah one of my proofs is cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757506):
`sheaf_property._proof_6 U β Ui Hcover i`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757507):
```quote
you should be able to do this by unification, no need to copy down those proofs
```
I like your way of thinking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757596):
This seems to work in my mockup example:
```
example (LHS RHS : nat) : LHS = RHS :=
begin
  let x, show x = RHS,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757597):
`change let x := _ in x = si i` -> ` don't know how to synthesize placeholder [some term involving all the proofs = si i]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757642):
`let x := FPTB.res BU _ _ s, show x = si i` -- this is the answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757643):
The whole definition of the `let` is optional since it is inferred by the `show`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757644):
Sorry so slow, one of my monitors just died, so it's like I'm back in 2015 with only one screen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757650):
I might steal one of the kids' monitors, they're all still in bed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757690):
`let x := _, show x = si i` -- this is the best answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757691):
but it's a hack because what if the RHS had also been full of implicit proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757692):
but it'll do for now -- thanks :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757693):
I bet even `let x, show x =  _` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757698):
Indeed it does.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757699):
`let x,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757700):
wtf?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757701):
All parts of a `let` or `have` are optional

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757702):
you can even just `have,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757741):
It's the := being optional I didn't know about :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757742):
I'm sure you are familiar with omitting `:=` in a `have x : property,` tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757743):
I guess so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757750):
thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757751):
Note that this only works in tactic mode, in term mode it's not so flexible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757790):
I was tempted to go into conv mode and use to_lhs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757794):
but was scared that if I had to do anything at all in conv mode then I would fail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757795):
e.g. prove something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757796):
This way is a much better way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757797):
Show is *super* useful, don't underestimate the power of unification with `_`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757806):
Yes, that was the insight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757845):
That I could use unification to fill in the holes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757846):
I just wanted to copy them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757847):
Only thing missing is allowing metavariables instead of `_` that can be referenced afterwards :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757894):
You can still achieve most of this with unification

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757898):
Summary for casual readers: `let x, show x = _` works for me and answers the original question -- it lets `x` be the left hand side of a goal of the form `X = Y`. It looks powerful enough to work in great generality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757899):
Do you know why my `show let` solution failed? Looks like the type checking complained too early

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757985):
Hmm -- `change let x := _ in x = si i` actually gives ` don't know how to synthesize placeholder; context = blah blah blah, ⊢ ?m_1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 07 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124758074):
I think `let` checking the value independent from the body is a feature

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124758124):
fair enough - I forgot that `change` doesn't create metavariables but only unifies. `let x,` has the behavior I intended and also unifies properly in the `show` line, so I guess it's fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 11 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124940592):
```quote
I bet even `let x, show x =  _` works
```
Is there a version of this trick for term mode, when I want to rw something in a hypothesis and not my goal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 11 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124944250):
You can rw in a hypothesis in term mode by using `eqn ▸ h` in place of `h` wherever it gets used. (You may need `eqn` or `eqn.symm` depending on orientation of the equation.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 11 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947124):
This came up with me specifically because I could not use rw because I only wanted to rewrite a certain term on the LHS, and it showed up on both sides.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 11 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947190):
conv!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947296):
Actually I am lying, I remember now, it was because there were suppressed proofs everywhere.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 11 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947332):
Although in the unfolding carefully thread the issue is raised about what happens when conv mode doesn't have the tactics you want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 11 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947352):
Conversely, did you see the transitive trick?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 11 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947516):
Maybe you can let `y := RHS`, then rewrite in the hypothesis to get `LHS = y` and then just rw on the hypothesis (`rw ... at H` works)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 11 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947526):
(or the triangle business)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 11 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947837):
All this discussion is probably worth a new tips and tricks file in `mathlib/docs/extras/`

