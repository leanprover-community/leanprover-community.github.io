---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48449provingltfromdecidability.html
---

## Stream: [general](index.html)
### Topic: [proving  lt from decidability](48449provingltfromdecidability.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661129):
I'd like to show the following lemma:

```
def  big_not_zero (a : nat) (P : 1  < a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  <  0, from eq.subst Pp P,
false.elim (nat.decidable_lt 1  0)
```

Concretely, I'd like to get a proof of false from `nat.decidable_lt 1 0`. But I don't understand how to use decidabilty in lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661254):
`example : 1  <  0  → false := dec_trivial`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661257):
I'm not saying these things are easy to use though :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661312):
```
def  big_not_zero (a : nat) (P : 1  < a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  <  0, from eq.subst Pp P,
(show  1  <  0  → false, by exact dec_trivial) olt0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661314):
and as you can see, I'm certainly no master of them myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661362):
```
def big_not_zero (a : nat) (P : 1 < a) : a ≠ 0 :=
λ h, nat.not_lt_zero 1 $ h ▸ P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661363):
\> implying I'm a master of them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661364):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661365):
Thank you! What is `exact`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661370):
`by` puts me into tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661371):
`exact` is a tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661372):
@**Adam Kurkiewicz** just do `from dec_trivial` instead of `by exact dec_trivial`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661373):
there's no need to go into tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661374):
I have trouble getting out of tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661415):
@**Kenny Lau** not working ` exact tactic failed, type mismatch, given expression has type `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661418):
```
def  big_not_zero (a : nat) (P : 1  < a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  <  0, from eq.subst Pp P,
(show  1  <  0  → false, from dec_trivial) olt0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661421):
works for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661422):
nevermind, that works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661436):
I'm surprised this is not working


```
def  big_not_zero (a : nat) (P : 1  < a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  <  0, from eq.subst Pp P,
dec_trivial olt0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661438):
```
def  big_not_zero (a : nat) (P : 1  < a) : a ≠  0  :=
begin
intro H,
rw H at P,
revert P,
exact dec_trivial
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661439):
aah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661441):
tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661481):
makes it all look so easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661486):
```quote
I'm surprised this is not working
```

```
def  big_not_zero (a : nat) (P : 1  < a) : a ≠  0  :=
λ Pp : a =  0, have olt0 : 1  <  0, from eq.subst Pp P,
dec_trivial olt0
```
`dec_trivial` takes no argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661492):
@**Kevin Buzzard**  Where did you learn tactic mode from? last few chapters of lean tutorial?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661494):
Tactic mode chapter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661499):
I have no idea why TPIL spends so long teaching people term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661500):
Fair enough, I didn't last that long :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661501):
For a beginner tactic mode is the bomb

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661504):
you can see what you're doing at all times

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661544):
what the goal is, what the hypotheses are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661547):
and you can try simp on every line in case it does the job

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661550):
I like term mode, at least I have an illusion I understand what's going on :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661553):
you have far more powerful tools available to you in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661555):
and then later on you can start figuring out what the tools are doing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661556):
and how they're doing it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661564):
You say "I don't understand decidability or how to use it"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661565):
I say "dec_trivial invokes a great tactic"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661605):
so your problems are solved in the short term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661612):
and then in the longer term you can start wondering about what it's doing and how it's doing it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661619):
My method is more robust than Kenny's

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661621):
```quote
My method is more robust than Kenny's
```
yeah right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661626):
because his solution relies on you knowing that there's a theorem in the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661629):
called ` nat.not_lt_zero `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661632):
implying one shouldn't know about theorems in the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661634):
whereas mine just relies on you being aware that stuff like this is decidable and there's a tactic which does it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661636):
I am saying mine is more robust.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661639):
I am not saying anything about whether it's a good idea to know the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661680):
What if tomorrow Adam wants to prove `2<1->false`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661689):
We all know it's decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661695):
and you and I know we can use no_confusion or all sorts of other tricks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661698):
but `dec_trivial` just does the job

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661700):
```
def big_not_zero' (a : nat) (P : 1 < a) : a ≠ 0 :=
λ h, (show ¬1 < 0, from dec_trivial) (h ▸ P)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661701):
satisfied?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661745):
It's good advice Kevin, I'll learn the tactic mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661748):
alright

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661753):
I think you should start with tactic mode and move on to term mode later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661754):
It's what they do in Software Foundations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661757):
and it's what I'm doing in the book I'm writing on doing maths in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661765):
but this is because my book is targetting mathematicians who have no idea what this lambda business is all about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661766):
because typically they will know no functional programming

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661767):
let's replace matlab with haskell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661768):
They do that next door

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661770):
in the computing department

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661771):
great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661772):
see you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661773):
:P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661812):
in the computing department?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661813):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661814):
Remember I'm on the curriculum review committee!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661815):
But I don't think I can push for Haskell for mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661819):
I am currently pushing for Python

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661820):
i'm just kidding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661822):
but python is already there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661823):
but not maths in python

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661825):
just general python

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661828):
i.e. teach them classes etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661833):
OOP python is the worst lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661834):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661835):
use java for OOP

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661837):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661840):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661841):
pee

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661843):
Should I push for java?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661848):
Why would a mathematician want to learn java?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661849):
heh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661850):
I think we should just teach them tactic mode ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661851):
push for lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661890):
problem solved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661891):
I think that some of them might want to compute something at some point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661892):
maybe they do that in the applied maths parts or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661893):
I have no idea what they do there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661895):
but I don't think it's theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 05 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661899):
Of couse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661905):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661906):
I think they figure out what f(10) is if they know some differential equation satisfied by f, and also they know f(0)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124661907):
@**Johannes Hölzl** wrong chat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662069):
@**Kevin Buzzard** I'd say teaching OOP is a bad idea. OOP is kind of dying at the moment anyway -- very few new languages actually have rich OOP features (rust, golang), and even in python very little new stuff gets written using OOP.

We've got a great new guy at Glasgow, who's teaching first year programming in python. He uses jupyter notebooks and shows applications of computation to multiple different problems (simulating fireworks, solving Travelling Salesman, etc.). I've done a guest lecture on Nim this year (https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material).

I think that's a more productive use of student's time than teaching them OOP.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662070):
I insisted to not use jupyter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662074):
even in the exam :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662077):
`python -m pip install numpy`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662120):
So I am in the maths department at Imperial College London and we're having a top-to-bottom curriculum review, and amongst the things that can change is that we can completely rethink what we teach to the undergraduates in terms of programming.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662121):
So I am definitely genuinely interested in hearing people's opinions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662123):
However we are definitely focussed on what mathematicians should need to know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662131):
in the sense of "what people who employ mathematicians want them to know"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662133):
You'd obviously want to modify the content a little bit to make it more mathsy,  but I think coding up an optimal algorithm to play Nim is definitely a worthy thing to teach first year mathematicians.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662136):
Your link doesn't work btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662189):
Ah, it's hidden from students cause it has solutions :D. one moment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662191):
don't worry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662192):
I don't want to disrupt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662360):
That's the task statement: [lab17-3.html](/user_uploads/3121/US_PO9-qzNBOQE1P_W4cNQ1C/lab17-3.html) 

There are ~7 specific python template files, which walk them through a solution, and they have to implement each one.

Each file gets automatically checked using something called "CMS", I believe stands  for "Contest Management System". Checking uses a regular test suite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662415):
Happy to share everything if you'd like, but at the moment I'm tethering and the internet is a bit slow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662419):
honestly don't worry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662424):
I can imagine what is there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662429):
I always imagine stuff like nim as being in the `recreational mathematics` box

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662430):
i.e. stuff they do outside of regular maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662469):
but I am not 100% sure whether I have this in the right box

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662479):
python has `^` -- do you let them use this or force them to code their own?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662645):
I let them use that after they've learned how it works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662704):
Just the opposite of what I did with my kids

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662708):
I asked them how to compute powers in python and let them be completely confused for 15 minutes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662709):
it's generally a problem with teaching python, it has everything and students sometimes just solve things with one-liners, without ever understanding it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662713):
just like tactic mode ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662721):
I don't normally use `numpy` and `sympy` :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662725):
Kenny, what do we teach the 1st years?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662726):
Currently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662729):
Do they import a lot of libraries?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662731):
`scipy`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662770):
`numpy` and `sympy`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662771):
I thought you're the head of curiculum reform

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662775):
curriculum

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662776):
words

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662841):
I'm just on the committee

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662843):
my job is to decide what to do in the future

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662844):
well you're the acting head of the department

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662846):
I don't want to pollute my understanding by knowing what we currently do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662857):
Maybe I should go and fill in forms :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662900):
how many goddam forms do you have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662901):
they come in at a rate faster than I can fill them in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662903):
what are those forms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662912):
I had to do a risk assessment form for Ana because she's pregnant. 6 pages of questions such as how much radioactive material there was in the department etc. Life is great when you're a manager.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662949):
OK I'm going to fill in more right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124662952):
life is always great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 05 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124664028):
I think between python, R, and Matlab, that's quite enough for a maths student... in a way I'm a little sad you can't get by without just pen, paper, and coffee pot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686378):
```quote
@**Kevin Buzzard** I'd say teaching OOP is a bad idea. OOP is kind of dying at the moment anyway -- very few new languages actually have rich OOP features (rust, golang), and even in python very little new stuff gets written using OOP.

We've got a great new guy at Glasgow, who's teaching first year programming in python. He uses jupyter notebooks and shows applications of computation to multiple different problems (simulating fireworks, solving Travelling Salesman, etc.). I've done a guest lecture on Nim this year (https://github.com/picrin/nim_game/tree/master/lab_material/lab17_student_material).

I think that's a more productive use of student's time than teaching them OOP.
```
What is this crazyness? Where did you see OOP dying?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686392):
I guess  this is what Haskell people say?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686402):
But what about the real world?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 05 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686651):
OOP is definitely not dying in the industry.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686878):
Yes, this very much sounds like functional programming academic fantasy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 05 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124686972):
To say that OOP is dying is certainly hyperbole, but none of the languages mentioned are particularly functional...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 05 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687127):
Go doesn't even have generics, speaking of modern design...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687187):
Go certainly looks awful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687309):
I never saw Rust but the wikipedia page features quite a occurrences of Haskell and ML

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687600):
Let's discuss something more productive: @**Sebastian Ullrich** am I correct in thinking that the nightly download link on  https://leanprover.github.io/download/ is no longer relevant and should not be used anymore?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687691):
```quote
Let's discuss something more productive: @**Sebastian Ullrich** am I correct in thinking that the nightly download link on  https://leanprover.github.io/download/ is no longer relevant and should not be used anymore?
```
Is there a new download link. It took me ages to update lean today, because MSYS didn't know where my c compiler was, and neither did I.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687706):
https://github.com/leanprover/lean-nightly/releases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687752):
You need to compare with https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687757):
(my understanding is it's not yet more automatic, but this is already great progress)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 05 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687777):
@**Patrick Massot** Correct. We're still waiting on AppVeyor enabling cron builds for us before we can make it official

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20%20lt%20from%20decidability/near/124687820):
Thanks

