---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64461unexpectedfunextreflbehaviour.html
---

## Stream: [general](index.html)
### Topic: [unexpected funext / refl behaviour](64461unexpectedfunextreflbehaviour.html)

---

#### [Kevin Buzzard (Apr 11 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946494):
```lean
set_option pp.universes true -- might help
example : -- phenomenon won't occur if you replace this with theorem T!
  (λ (X : Sort*) (f : X → X) , f) = (λ (X : Sort*) (f : X → X), f) :=
begin
  funext, -- only pulls off X, possibly because of universe issues
  -- two failed attempts to pull off f now:
  -- funext, -- does nothing
  -- apply funext, -- fails to unify
  refine funext _, -- Type of X now Sort (imax ? ?) and a type mismatch error reported **but goal changes anyway**
  intro f,
  -- goal now f = f
  -- refl, -- doesn't work! Fails to unify.
  exact rfl, -- does work
end
```

#### [Kevin Buzzard (Apr 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946536):
I am pleased to have confused tactic mode so much that `refl` won't work but `exact rfl` will.

#### [Kevin Buzzard (Apr 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946548):
I am not sure if my goal is true, as the sorts may or may not be in different universes initially. However the funext tactic seems to buy it, although after pulling off the X it gets confused and won't pull off the `f`.

#### [Kevin Buzzard (Apr 11 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946563):
`apply f` won't do it but I seem to be able to explicitly do it with `refine funext _` although now Lean is in a funny state -- the refine tactic does appear to do something, but reports an error anyway.

#### [Kevin Buzzard (Apr 11 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946610):
replacing `example` with `theorem T` makes all the problems go away, which is to me very surprising behaviour.

#### [Patrick Massot (Apr 11 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946682):
This Lean 3 is all broken. Let's have Lean 4.

#### [Patrick Massot (Apr 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946695):
(and hope Kevin stops trying to break everything)

#### [Chris Hughes (Apr 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946760):
Isn't it just because your X's are in different universes. And then if you put them in the same universe, it fails because the funext tactic gets rid of both lambdas.

#### [Kevin Buzzard (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946857):
I agree that if you put them in the same universe, all is well.

#### [Kevin Buzzard (Apr 11 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946864):
But if you leave them in different universes, Lean ends up in a weird state.

#### [Kevin Buzzard (Apr 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946940):
After the intro f, you have a goal `f = f` which refl won't close

#### [Kevin Buzzard (Apr 11 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946953):
but `exact rfl` will. However we are now passed a red squiggly line and I am not too sure how seriously to take Lean.

#### [Chris Hughes (Apr 11 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946954):
I'm beginning to see the problem. Is it something to do with, it let's you do funext the first time, so if you can prove their equal, it will deduce the universes are the same. So your proposition is a bit like an heq?

#### [Kevin Buzzard (Apr 11 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946958):
I was wondering if there was some implicit unification going on

#### [Kevin Buzzard (Apr 11 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947005):
Also it was very strange to see a line in tactic mode fail and yet see the goal change.

#### [Patrick Massot (Apr 11 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947019):
Looks a bit in the same spirit as your most recent issue on Lean github

#### [Chris Hughes (Apr 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947028):
And it automatically lifts the functions to a different universe to be able to state that they're equal.

#### [Patrick Massot (Apr 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947033):
Lean somehow fails to notice it's failing

#### [Chris Hughes (Apr 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947109):
Haven't ever done anything that really tests the universe system so I don't really know.

#### [Kevin Buzzard (Apr 11 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947173):
I just started playing with it recently. I'm just trying to get the hang of it :-)

#### [Kevin Buzzard (Apr 16 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162334):
I know there's something strange going on here but I've not explained it very well. How about this

#### [Kevin Buzzard (Apr 16 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162336):
```lean
example : 
  (λ (X : Sort*) (f : X → X) , f) = (λ (X : Sort*) (f : X → X), f) :=
begin
  funext, -- it's not very effective
  refine @funext (X → X) _ _ _ _, -- back on track
  intro f,
  refl,
end
```

#### [Kevin Buzzard (Apr 16 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162338):
That works fine.

#### [Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162340):
But now let me change `example` to `theorem strange`:

#### [Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162390):
```lean
theorem strange : 
  (λ (X : Sort*) (f : X → X) , f) = (λ (X : Sort*) (f : X → X), f) :=
begin
  funext, -- it's super effective!
  refine @funext (X → X) _ _ _ _, -- invalid type ascription
  intro f,
  refl,
end
```

#### [Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162393):
The proof no longer typechecks if I name the theorem

#### [Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162398):
because the behaviour of `funext` changes now the theorem has a name

#### [Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162401):
That's not right, is it?

#### [Kevin Buzzard (Apr 16 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162462):
I think this has something to do with screwy universes

#### [Johannes Hölzl (Apr 16 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162620):
Yes, it could be related to the fact that `example` (compared to `theorem`) does allow meta (universe) variables in its statement. So the type is not fully elaborated, it gets fully elaborated together with the value like `def`. So maybe `funext` has a problem with instantiating them.

#### [Kevin Buzzard (Apr 16 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162747):
Oh yes! If I set `pp.universes true` then I see that in the `theorem` the goal has `(X : Sort u_1)`

#### [Kevin Buzzard (Apr 16 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162780):
but in the `example` it has `(X : Sort ?l_1)`

#### [Kevin Buzzard (Apr 16 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125163009):
I see, so `definition strange` fixes the problem :-)

#### [Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166006):
here's some possibly related weird behaviour:

#### [Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166023):
```lean
example : 
  (λ (X : Sort*) (f : X → X) , f) = (λ (X : Sort*) (f : X → X), f) :=
begin
  funext, 
  refine funext _, 
  intro f,
  -- this proof isn't finished yet
end

```

#### [Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166031):
the goal now is `f = f`

#### [Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166037):
(at the point where the proof is not finished)

#### [Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166041):
or with `pp.all` on

#### [Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166054):
`⊢ @eq.{?l_2} (X → X) f f`

#### [Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166066):
and the red squiggle is under `end`

#### [Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166073):
because we wrote end before the proof was complete

#### [Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166079):
However if we write `admit` to finish the proof

#### [Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166087):
we get a new red squiggle

#### [Kevin Buzzard (Apr 16 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166137):
on the second funext :-)

#### [Kevin Buzzard (Apr 16 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166149):
Maybe the universe unification or whatever only takes place after the admit, and then Lean decides something was wrong all along

#### [Kevin Buzzard (Apr 16 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166164):
I guess this is the price I pay for the silly `Sort*` choices I made earlier

#### [Kevin Buzzard (Apr 16 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166182):
changing `example` to `theorem T` gives me the red squiggle on the second funext immediately

#### [Chris Hughes (Apr 16 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125168260):
I think it might be because the proof could give a clue about universes, but not if the proof is admit.

