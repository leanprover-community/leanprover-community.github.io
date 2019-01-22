---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39678LIVECHATStructuresformathematicians.html
---

## [maths](index.html)
### [LIVE CHAT: Structures for mathematicians](39678LIVECHATStructuresformathematicians.html)

#### [Kevin Buzzard (May 29 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127264270):
At 8pm UK time (2000 BST, so 1900 GMT) I am going to a live Lean explanation, in this thread, of a very simple mathlib file which defines a (non-inductive) structure. Mathematicians need to learn how to make structures, it's something we do very differently in mathematics. Here we need a far more formal kind of interface. I will hopefully do a few of these. It's like "talking people through mathlib files".

#### [Kenny Lau (May 29 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127264325):
youtube live?

#### [Johan Commelin (May 29 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127264635):
No, it seems "Zulip live"

#### [Kevin Buzzard (May 29 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127265656):
Johan, I was inspired to do it after looking at the structure you constructed, which reminded me of the terrible first structure I constructed.

#### [Kevin Buzzard (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267673):
Hello, this is just me talking through `pnat.lean`

#### [Kevin Buzzard (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267674):
It should be easy

#### [Kevin Buzzard (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267678):
and maybe people will find it later.

#### [Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267695):
Ok so mathematicians use a lot of structures, and one structure I was brought up on is "the UK mathematician's nat", namely {1,2,3,...}

#### [Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267698):
Ok so how do we define the UK mathematician's nat?

#### [Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267701):
Well pretty clearly we could define it like the computer scientist's nat := {0,1,2,3,...}

#### [Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267702):
we could just make a structure

#### [Kevin Buzzard (May 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267742):
hmm

#### [Kevin Buzzard (May 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267745):
let me fire up lean

#### [Kevin Buzzard (May 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267771):
that's better

#### [Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267796):
I am so rubbish at structures

#### [Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267810):
aah bingo

#### [Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267813):
it's not a structure

#### [Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267817):
it's an inductive type

#### [Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267819):
```lean
inductive pnat
| one : pnat 
| succ : pnat → pnat 

```

#### [Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267820):
So there's pnat

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267825):
and that would work

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267870):
and we could define addition and multiplication and prove addition is commutative

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267873):
and do all that stuff again

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267877):
and that's stuff we already did with nat

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267879):
and that's kind of a waste

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267889):
it would be nice to inherit all those theorems about nat and get them to pnat immediately

#### [Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267896):
so let's take a look at what they did in Lean or mathlib, wherever they defined pnat

#### [Kevin Buzzard (May 29 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267932):
Ok so it's in mathlib

#### [Kevin Buzzard (May 29 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267936):
which means that computer scientists are not interested in this structure

#### [Kevin Buzzard (May 29 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267939):
You can get to it with "import data.pnat"

#### [Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267943):
let's find it on github

#### [Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267993):
https://github.com/leanprover/mathlib/blob/master/data/pnat.lean

#### [Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267996):
There it is.

#### [Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267999):
Last modified two days ago!

#### [Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268002):
Things never stand still around here

#### [Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268022):
OK so I'm going to talk through this file, or at least what I understand of this file, which is pretty much all of it I hope

#### [Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268029):
and the first thing we notice

#### [Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268034):
is that on line 1

#### [Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268037):
they don't define it using an inductive structure like nat

#### [Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268039):
they define it as a _subtype_

#### [Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268041):
which is a bit more annoying to use in practice

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268066):
oh wait I skipped a line

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268093):
`import tactic.basic`

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268099):
let's come back to that line when I have figured out why it's there

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268104):
`def pnat := {n : ℕ // n > 0}`

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268105):
And there it is.

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268107):
There are sets `{x | blah}`

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268110):
and there are subtypes `{x // blah}`

#### [Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268112):
this one is a subtype

#### [Kevin Buzzard (May 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268135):
don't mind me I'm just editing mathlib

#### [Kevin Buzzard (May 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268138):
Ok so I was trying to work out what a subtype was

#### [Kevin Buzzard (May 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268140):
but I know the answer

#### [Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268197):
to make a pnat you have to give two pieces of data

#### [Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268200):
1) a nat

#### [Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268204):
2) a proof that it's positive

#### [Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268209):
(that's > 0 for you French speakers)

#### [Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268220):
so here's an example

#### [Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268230):
`definition x : pnat := ⟨59,oh crap⟩`

#### [Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268232):
that didn't go well

#### [Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268235):
I was in the middle of defining 59

#### [Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268238):
and all of a sudden I needed a proof.

#### [Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268240):
OK so let's try again but this time be prepared

#### [Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268288):
```lean
theorem H : 59 > 0 := sorry 
definition x : pnat := ⟨59,H⟩
```

#### [Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268289):
Ok that went better

#### [Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268295):
I cheated with my proof that 59 > 0 by saying the proof was sorry (which means "just assume it")

#### [Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268298):
and now I can finally make my pnat

#### [Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268311):
This is going to be pretty inconvenient having to prove that things are positive

#### [Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268316):
but actually in a couple of lines we're going to see a really good way of doing it

#### [Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268324):
```lean
notation `ℕ+` := pnat

instance coe_pnat_nat : has_coe ℕ+ ℕ := ⟨subtype.val⟩
```

#### [Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268325):
Those are the next couple of lines

#### [Kevin Buzzard (May 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268373):
The first one is easy: it sets up notation, and we're going to use the completely non-standard notation `ℕ+` for pnat

#### [Kevin Buzzard (May 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268376):
as opposed to a little plus or a little star or whatever the French use, maybe some sub zero or super zero

#### [Kevin Buzzard (May 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268383):
this sort of thing is a minefield

#### [Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268387):
`ℕ+` will do

#### [Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268413):
and now this incomprehensible coe line is where we start making the interface for our structure

#### [Patrick Massot (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268417):
ℕ^*

#### [Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268418):
because we are already finished with the structure

#### [Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268425):
Submit a PR Patrick

#### [Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268486):
The thing that mathematicians don't realise

#### [Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268490):
or at least that I didn't realise at all

#### [Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268492):
(I suspect Patrick knew full well)

#### [Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268493):
was that it's not just about making the structure

#### [Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268494):
the next thing you have to do is to say to yourself

#### [Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268502):
"what is every single basic thing that my users might want to do with this structure?"

#### [Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268515):
And the first basic thing is that given a positive natural, a mathematician might also want to think of it as a natural.

#### [Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268519):
And in fact it's such a natural (no pun intended) to move from pnat to nat

#### [Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268520):
that not only did they design a function for it

#### [Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268529):
but they made it into a coercion

#### [Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268532):
which means "it happens magically"

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268580):
Aah I see what to do

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268582):
I have mathlib pnat open

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268584):
and a copy of it

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268586):
and I edit the copy

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268587):
great

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268598):
so let's see if we can understand this coercion

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268602):
and then let's see it happen

#### [Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268616):
`instance coe_pnat_nat : has_coe ℕ+ ℕ := ⟨subtype.val⟩`

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268617):
instances are something I never understood

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268622):
coercions not really either

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268629):
and then those dreaded pointy brackets

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268633):
and then an incomprehensible `subtype.val`

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268636):
That's what I thought of that line in about January.

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268646):
But as Kenny once told me, Lean does not do magic

#### [Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268652):
so we can work out what this line does

#### [Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268719):
and I work it out by having this pnat file open in Lean and just right clicking on subtype.val

#### [Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268723):
and then selecting "go to definition"

#### [Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268728):
and then we find ourselves right in the heart of core lean

#### [Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268731):
and we see

#### [Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268733):
```lean
structure subtype {α : Sort u} (p : α → Prop) :=
(val : α) (property : p val)
```

#### [Kevin Buzzard (May 29 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268742):
and pnat, the positive naturals, was a subtype

#### [Kevin Buzzard (May 29 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268750):
in fact if we switch notation off and look at pnat

#### [Kevin Buzzard (May 29 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268765):
```lean
def pnat := {n : ℕ // n > 0}

set_option pp.notation false
#print pnat
```

#### [Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268803):
we see

#### [Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268808):
`def pnat : Type :=
subtype (λ (n : nat), gt n 0)`

#### [Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268814):
eew

#### [Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268816):
`gt` is `>`

#### [Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268824):
so indeed we see a function nat to Prop

#### [Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268827):
sending n to "n > 0"

#### [Kevin Buzzard (May 29 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268833):
and we get a subtype, consisting of the n such that we have a proof that n > 0

#### [Kevin Buzzard (May 29 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268846):
and we see from the definition of the subtype structure that the `n` is the `val` and the proof is the `property`

#### [Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268904):
so subtype.val sends the pnat `⟨59,H⟩`

#### [Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268905):
to its value

#### [Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268906):
which is 59

#### [Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268913):
and we made it a coercion using coercion instance magic

#### [Kevin Buzzard (May 29 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268920):
so that means it should happen naturally

#### [Kevin Buzzard (May 29 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268930):
Ok it works!

#### [Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268987):
```lean
theorem H : 59 > 0 := sorry 
definition x : pnat := ⟨59,H⟩
#check (x : pnat) -- x : pnat
#check (x : ℕ) 
```

#### [Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268991):
it would be better if you could see me typing

#### [Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268992):
that would save me having to cut and paste

#### [Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268993):
how do I do that?

#### [Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268994):
Did someone say youtube ?

#### [Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268996):
Does twitch take this sort of stuff?

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268997):
I have done all manner of weird things on twitch

#### [Patrick Massot (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269004):
Yes, I don't understand why you don't record that and put it on youtube

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269008):
because I'm just squeezing this in before I put the kids to bed

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269009):
so back to the point

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269011):
a miracle occurred!

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269012):
A contradiction in type theory!

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269015):
x had type pnat

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269016):
and type nat

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269019):
as well

#### [Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269021):
but actually what happened was that coercion kicked in

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269062):
The output of the second check was `↑x : ℕ`

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269074):
and that arrow (which you get with `\u`)

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269077):
means "I got coerced!"

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269084):
so that has solved our first fundamental problem

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269086):
which is that for a mathematician, pnat is a subset of nat

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269088):
and hence every pnat _is_ a nat

#### [Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269092):
They don't have it so easy in DTT

#### [Kevin Buzzard (May 29 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269100):
so we are stuck with the cute little arrows

#### [Kevin Buzzard (May 29 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269107):
let's press on

#### [Kevin Buzzard (May 29 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269120):
The next line is clever

#### [Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269146):
`def to_pnat (n : ℕ) (h : n > 0 . tactic.exact_dec_trivial) : ℕ+ := ⟨n, h⟩`

#### [Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269177):
That's using a really cool piece of Lean functionality

#### [Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269191):
...which breaks if I remove that `import` line

#### [Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269193):
so that's why the import is there

#### [Kevin Buzzard (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269213):
This is pretty much the rarest of ways to make a function input for Lean

#### [Patrick Massot (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269215):
you could still hide the  cute little arrows from pp display though

#### [Kevin Buzzard (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269225):
there's something in the manual about this

#### [Kevin Buzzard (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269228):
you can do pp.no_cute_arrows Patrick?

#### [Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269280):
here we are

#### [Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269281):
https://leanprover.github.io/reference/expressions.html#implicit-arguments

#### [Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269282):
`set_option pp.coercions false`

#### [Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269286):
does that mean Lean doesn't do them?

#### [Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269290):
or just doesn't print the arrows?

#### [Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269291):
doesn't print

#### [Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269293):
thought so :-)

#### [Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269297):
hence the pp

#### [Johan Commelin (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269299):
`pp` means "pretty print"

#### [Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269300):
meaning pretty print

#### [Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269305):
presumably no setting of options can change Lean's behaviour?

#### [Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269320):
in pnat we have the last of the ways that Lean can make an implicit argument

#### [Patrick Massot (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269324):
`class.instance_max_depth`

#### [Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269331):
"run a tactic to make the argument for you"

#### [Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269333):
Patrick: touch\'e

#### [Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269339):
`def to_pnat (n : ℕ) (h : n > 0 . tactic.exact_dec_trivial) : ℕ+ := ⟨n, h⟩`

#### [Kevin Buzzard (May 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269389):
means "take an input n, and then see if you can prove n > 0 by using the tactic `tactic.exact_dec_trivial`"

#### [Kevin Buzzard (May 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269394):
Let's see this tactic in action

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269414):
`theorem H : 59 > 0 := by tactic.exact_dec_trivial`

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269416):
It works!

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269420):
To find out what it does you can right click on it and it will be all tacticy stuff

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269422):
so I'm not going to do that

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269424):
but I know what is going on

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269425):
in fact there's a shorter way of doing it

#### [Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269430):
`theorem H : 59 > 0 := dec_trivial`

#### [Kevin Buzzard (May 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269432):
(not a tactic, so no `by` this time)

#### [Kevin Buzzard (May 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269485):
`dec_trivial` just means "> is decidable on nat so just please decide this for me by proving it's true"

#### [Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269505):
apparently you can't use it to prove things are false though

#### [Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269512):
`theorem H1 : 0 > 0 := dec_trivial`

#### [Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269514):
doesn't work

#### [Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269527):
so let's see `to_pnat` in action!

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269542):
`definition y : pnat := to_pnat 12 `

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269579):
that's much better than what we had before

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269595):
`definition z : pnat := to_pnat 0`

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269600):
you get some weird error

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269610):
OK so let's press on

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269612):
`def succ_pnat (n : ℕ) : ℕ+ := ⟨succ n, succ_pos n⟩`

#### [Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269616):
this one looks easy.

#### [Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269626):
Given n a nat, we are building a pnat called `succ_pnat n`

#### [Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269633):
and you can guess from the name that it will be n + 1

#### [Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269638):
so I reckon that succ_pos n is going to be the theorem that n + 1 > 0

#### [Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269644):
we can check that easily

#### [Mario Carneiro (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269659):
Obviously you can't prove false things using `dec_trivial`, they're false

#### [Mario Carneiro (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269708):
but you can prove the negation using `dec_trivial`

#### [Kevin Buzzard (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269733):
```lean
variable (n : ℕ)
#check succ_pos n 
```

#### [Kevin Buzzard (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269739):
`succ_pos n : 0 < succ n`

#### [Kevin Buzzard (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269750):
we could have right clicked and wandered back in to core lean or so, but this is another way

#### [Kevin Buzzard (May 29 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269767):
So that's two maps from nat to pnat and a map from pnat to nat

#### [Kevin Buzzard (May 29 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269774):
It's certainly the case that we could imagine using both those maps

#### [Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269818):
but what do we need to do next?

#### [Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269824):
This is the question that I as a mathematician find hard

#### [Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269825):
and I think that people like Mario just somehow know

#### [Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269828):
I'm just going to cheat and look at the code

#### [Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269831):
`@[simp] theorem succ_pnat_coe (n : ℕ) : (succ_pnat n : ℕ) = succ n := rfl`

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269845):
OK so this says that given a nat, if we compute its successor as a pnat then it equals its successor as a nat

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269852):
Notice the secret coercion! That equality is between a pnat and a nat

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269854):
and Lean coerces the left hand side

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269855):
so if you think about it

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269857):
when you unravel it

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269860):
that theorem just says `succ n = succ n`

#### [Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269865):
so the proof is `rfl`

#### [Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269928):
Ok now @**Mario Carneiro** told me that theorems whose proofs were rfl sometimes don't get names

#### [Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269932):
but this one got lucky

#### [Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269934):
it got a name

#### [Mario Carneiro (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269936):
it's a simp lemma, those need names

#### [Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269940):
and presumably that's because someone somewhere realised that this was a good simp lemma

#### [Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269944):
NOTE FOR BEGINNERS

#### [Mario Carneiro (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269946):
also I'm not sure that's a good rule of thumb

#### [Mario Carneiro (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269960):
rfl proofs are very common

#### [Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269963):
It's important that you get your simp lemma the right way round

#### [Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269971):
you don't want to prove that `succ n` equals `succ_pnat n`

#### [Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269975):
because that would be a comp lemma

#### [Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269984):
in maths it doesn't matter which order you put the things that are equal

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270022):
`x = y` and `y = x` mean the same thing

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270034):
but in Lean you might want to consider putting the more complicated thing on the left

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270042):
and then simp will simplify it to the right if it uses your lemma

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270046):
and even if simp does not use your lemma

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270053):
imagine when you're doing a rewrite

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270060):
you are trying to prove something

#### [Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270065):
so you're usally trying to make stuff easier

#### [Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270075):
and you don't want to have to put left arrows everywhere because they look weird

#### [Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270085):
so, mathematicians everywhere, remember that THIS WEIRD CS WORLD IS ASYMMETRIC

#### [Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270092):
and if you've proved x = y, make sure x takes more characters to type

#### [Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270097):
or else you should have proved y = x

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270142):
Next line

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270143):
`@[simp] theorem pos (n : ℕ+) : (n : ℕ) > 0 := n.2`

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270150):
that looks like really poor Lean to me

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270153):
who wrote this file anyway

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270156):
oh I heard of that guy

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270165):
Now everyone knows that simp is used to prove _equalities_

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270170):
so all your simp lemmas should be _equalities_

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270171):
or _iff_s

#### [Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270175):
and anything which is a random thing like >

#### [Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270180):
obviously should not be a simp lemma

#### [Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270196):
because simp, it turns out, does *not* stand for "this lemma is pretty simple"

#### [Mario Carneiro (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270200):
This is useful for fulfulling side conditions in algebraic rules, which sometimes need that things are nonzero or positive

#### [Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270203):
it stands for "this lemma is appropriate for the simplifier"

#### [Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270215):
and 9 times out of 10 it's because it's an equality

#### [Patrick Massot (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270221):
I disagree our equality is symmetric. Would you write some cohomological vanishing theorem as $$0 = H^i(X, F)$$?

#### [Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270268):
but apparently there are other times when it's not

#### [Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270285):
Interesting point Patrick I guess you're right

#### [Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270288):
Maybe 0 is a special case

#### [Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270303):
The conclusion of this is that working out if something is a simp lemma is still something which I haven't got the hang of

#### [Mario Carneiro (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270309):
most "let x = value" type statements have the variable on the left in math

#### [Patrick Massot (May 29 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270343):
What about $$\int_{-\infty}^\infty e^{-x^2} dx = \srqt\pi$$?

#### [Kevin Buzzard (May 29 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270345):
Now look at these

#### [Kevin Buzzard (May 29 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270348):
```lean
namespace pnat

open nat
@[simp] theorem pos (n : ℕ+) : (n : ℕ) > 0 := n.2

theorem eq {m n : ℕ+} : (m : ℕ) = n → m = n := subtype.eq

@[simp] theorem mk_coe (n h) : ((⟨n, h⟩ : ℕ+) : ℕ) = n := rfl

instance : has_add ℕ+ := ⟨λ m n, ⟨m + n, add_pos m.2 n.2⟩⟩

@[simp] theorem add_coe (m n : ℕ+) : ((m + n : ℕ+) : ℕ) = m + n := rfl

@[simp] theorem ne_zero (n : ℕ+) : (n : ℕ) ≠ 0 := ne_of_gt n.2
```

#### [Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270404):
The last thing we want to do is to define random theorems like `ne_zero` (the last one) and have its actual name be `ne_zero` in the root namespace

#### [Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270408):
I did that a lot when I started

#### [Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270416):
The statement that if n is a pnat then n isn't zero -- clearly ne_zero is a good name for it

#### [Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270417):
but its full name is `pnat.ne_zero`

#### [Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270423):
like all the other pnat things we're going to do now

#### [Johan Commelin (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270429):
So, why is `theorem eq` not a simp theorem?

#### [Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270430):
so that's why we opened the pnat namespace

#### [Kevin Buzzard (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270435):
we namespaced

#### [Kevin Buzzard (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270438):
and we opened nat for good measure

#### [Mario Carneiro (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270443):
because the RHS has a variable not on the LHS

#### [Kevin Buzzard (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270452):
So theorem `eq` says a fundamental thing about subtypes.

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270507):
Remember -- a subtype is a term and then a proof of something that depends only on the term

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270516):
so if we have two subtype things with the same term and different proofs, are they the same?

#### [Patrick Massot (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270520):
What RHS variable?

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270523):
And yes they are, because all proofs are the same

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270526):
so that's why pnat.eq is true

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270530):
and indeed the proof is subtype.eq and you can guess what that says

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270532):
or right click on ir

#### [Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270534):
it

#### [Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270536):
or #check it

#### [Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270549):
Oh I know why eq isn't a simp lemma

#### [Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270550):
it's not an equality

#### [Mario Carneiro (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270552):
`m = n` is not a simplification

#### [Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270555):
it's an implication

#### [Mario Carneiro (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270559):
and where is `n` coming from?

#### [Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270567):
aah

#### [Mario Carneiro (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270570):
that's what I mean, `n` doesn't show up on the LHS

#### [Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270575):
There's another simp rule of thumb

#### [Kevin Buzzard (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270620):
all the variables on the RHS should be in the LHS too

#### [Johan Commelin (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270625):
Whenever I have to subtype thingies in my goal, and I need to prove that they are equal, Lean should always apply `subtype.eq`. I can't think of any reason why you wouldn't want to do that.

#### [Patrick Massot (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270626):
why this rule?

#### [Kevin Buzzard (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270627):
I should mention that to the guy who wrote the simp docs

#### [Mario Carneiro (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270637):
It's an extensionality theorem

#### [Mario Carneiro (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270644):
you don't always want it applied, because it complicates the goal

#### [Patrick Massot (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270651):
should it be tagged as such?

#### [Mario Carneiro (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270655):
probably

#### [Kevin Buzzard (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270657):
More generally Johan, if you have two structures that are equal, you might want Lean to just decompose them and demand that you prove that all the bits you used to make them are equal

#### [Kevin Buzzard (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270666):
but I think it would be a bit confusing if you were just motoring along and all of a sudden you have 10 goals

#### [Johan Commelin (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270670):
```quote
you don't always want it applied, because it complicates the goal
```
Huh, the goal becomes easier, right? I just got rid of some irrelevant proofs...

#### [Kevin Buzzard (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270672):
because you wanted to prove complicated structures were equal

#### [Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270717):
I think this sort of thing is an art

#### [Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270731):
I'm not sure what the best answer is but clearly Mario will speak from experience

#### [Mario Carneiro (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270732):
you were trying to prove `m = n`, now you are proving `\u m = \u n`

#### [Mario Carneiro (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270740):
the goal got more complicated

#### [Mario Carneiro (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270744):
sometimes that's what you want, but it needs to be an explicit choice

#### [Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270745):
Aah -- Johan -- if you actually had variables m and n which were pnats

#### [Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270749):
then you might well not want it

#### [Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270756):
but if m was explicitly `<nat,proof>`

#### [Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270760):
and so was n

#### [Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270766):
then you might want it

#### [Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270767):
(but you might not)

#### [Johan Commelin (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270774):
Hmm, fair enough

#### [Mario Carneiro (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270775):
and that version is a simp lemma

#### [Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270789):
ooh my son's gone

#### [Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270791):
I just inherited a second screen

#### [Johan Commelin (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270796):
Ok, I have met subtypes where it was not a simp lemma, I think

#### [Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270801):
Ok so mk_coe

#### [Johan Commelin (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270811):
Or is it a simp lemma for general subtypes?

#### [Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270861):
that says "make the subtype and then coerce back to nat and you're back where you started"

#### [Johan Commelin (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270864):
Hmm, yes, let's move on with this chat

#### [Mario Carneiro (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270870):
`subtype.mk_eq_mk`

#### [Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270885):
`@[simp] theorem mk_coe (n h) : ((⟨n, h⟩ : ℕ+) : ℕ) = n := rfl`

#### [Mario Carneiro (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270888):
it's a general simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270901):
Actually there are several cool things about `mk_coe`

#### [Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270918):
first, it's something which I wanted for my structure and Mario said it didn't have a name

#### [Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270922):
hmm

#### [Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270924):
maybe that's not entirely true

#### [Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270933):
Mario -- why does this lemma use coercion instead of val?

#### [Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270937):
They're definitionally equal, right?

#### [Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270972):
Does it matter which one you choose when making your structure?

#### [Mario Carneiro (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270986):
it's a simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270995):
But what about `(⟨n, h⟩ : ℕ+).val = n`

#### [Mario Carneiro (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270999):
The val version is automatic, because simp knows about structures

#### [Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271006):
or `subtype.val (⟨n, h⟩ : ℕ+) = n`

#### [Mario Carneiro (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271010):
but when the val is hidden in a coercion simp misses it

#### [Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271014):
oh so simp doesn't need to be told that

#### [Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271017):
the thing I wrote

#### [Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271021):
but does need to be told the thing you put in the file

#### [Mario Carneiro (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271030):
right

#### [Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271036):
You see -- there is so much subtlety in this stuff

#### [Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271045):
I saw the definition of pnat in a maths lecture

#### [Mario Carneiro (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271048):
I mean you could have it as a simp lemma if you want

#### [Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271050):
it was "take nat and remove 0"

#### [Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271054):
and that was it

#### [Mario Carneiro (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271056):
but it probably won't trigger

#### [Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271059):
There is all this extra stuff here

#### [Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271068):
```lean

instance : has_add ℕ+ := ⟨λ m n, ⟨m + n, add_pos m.2 n.2⟩⟩

@[simp] theorem add_coe (m n : ℕ+) : ((m + n : ℕ+) : ℕ) = m + n := rfl
```

#### [Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271073):
We want add on pnat

#### [Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271116):
and here's something I only learnt recently

#### [Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271134):
the only purpose of `has_add` and the 20 or so other `has_notation` things

#### [Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271138):
is notation

#### [Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271143):
The instance is so unimportant that it doesn't even deserve a name

#### [Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271155):
although probably one could have called it `pnat.add`

#### [Mario Carneiro (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271162):
it gets an automatic name if you don't specify, in this case `pnat.has_add`

#### [Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271167):
The definition of add on pnat clearly needs a theorem -- it needs the theorem that if a>0 and b>0 then a+b>0

#### [Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271170):
Oh I didn't know that -- thanks

#### [Mario Carneiro (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271173):
`pnat.add` would be the name of the function itself

#### [Mario Carneiro (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271179):
if it had a name

#### [Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271181):
Oh of course

#### [Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271222):
The function is add

#### [Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271233):
and the proof that it has an add is something else

#### [Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271243):
actually it's not a proof

#### [Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271245):
it's data

#### [Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271253):
OK so we need to proev that if a>0 and b>0 then a+b>0

#### [Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271258):
and we cheat and look at what Mario did

#### [Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271277):
and why is the output from #check so ugly?

#### [Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271284):
`#check add_pos `

#### [Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271291):
`add_pos : 0 < ?M_3 → 0 < ?M_4 → 0 < ?M_3 + ?M_4`

#### [Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271293):
thanks Lean

#### [Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271299):
`#check @add_pos `

#### [Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271304):
`add_pos : ∀ {α : Type u_1} [_inst_1 : ordered_cancel_comm_monoid α] {a b : α}, 0 < a → 0 < b → 0 < a + b`

#### [Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271339):
not ideal either

#### [Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271358):
I would have preferred

#### [Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271364):
`0 < a → 0 < b → 0 < a + b`

#### [Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271371):
but unsurprisingly

#### [Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271376):
it's the lemma we need

#### [Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271395):
Now these should be straightforward

#### [Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271401):
```lean

@[simp] theorem add_coe (m n : ℕ+) : ((m + n : ℕ+) : ℕ) = m + n := rfl

@[simp] theorem ne_zero (n : ℕ+) : (n : ℕ) ≠ 0 := ne_of_gt n.2

@[simp] theorem nat_coe_coe  {n : ℕ} : n > 0 → ((n : ℕ+) : ℕ) = n := succ_pred_eq_of_pos
@[simp] theorem to_pnat'_coe {n : ℕ} : n > 0 → (n.to_pnat' : ℕ) = n := succ_pred_eq_of_pos

@[simp] theorem coe_nat_coe (n : ℕ+) : ((n : ℕ) : ℕ+) = n := eq (nat_coe_coe n.pos)
```

#### [Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271414):
you see -- this is the advantage of making it a subtype

#### [Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271420):
we have to carry around all these proofs

#### [Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271425):
but `add_coe` says "adding the pnats is the same as adding the nats, by definition"

#### [Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271485):
and indeed if you look at the coercion you can see that this is just a statement of the form X = X

#### [Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271500):
ne_zero : we will need to prove n > 0 -> n ne 0

#### [Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271514):
and it would not surprise me if that were called ne_of_gt

#### [Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271517):
and note that

#### [Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271528):
`n.2` is the proof

#### [Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271531):
that n > 0

#### [Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271536):
it's `n.property`

#### [Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271546):
for kids who are too cool to write such a long thing

#### [Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271563):
`nat_coe_coe`

#### [Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271565):
I have no idea why this is a simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271571):
I guess I do know

#### [Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271573):
it's kind of "well there's only a minor precondition"

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271614):
"and then we get some serious simplification"

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271619):
I am kind of surprised this works

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271626):
we coerce a nat to a pnat

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271632):
that doesn't even make sense

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271635):
oh crap

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271642):
I am looking at an old version of pnat

#### [Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271645):
rofl

#### [Kevin Buzzard (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271669):
I'm now looking at the up to date version

#### [Kevin Buzzard (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271672):
and that line is gone :-)

#### [Kevin Buzzard (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271680):
```lean
@[simp] theorem add_coe (m n : ℕ+) : ((m + n : ℕ+) : ℕ) = m + n := rfl

@[simp] theorem ne_zero (n : ℕ+) : (n : ℕ) ≠ 0 := ne_of_gt n.2

@[simp] theorem to_pnat'_coe {n : ℕ} : n > 0 → (n.to_pnat' : ℕ) = n := succ_pred_eq_of_pos

@[simp] theorem coe_to_pnat' (n : ℕ+) : (n : ℕ).to_pnat' = n := eq (to_pnat'_coe n.pos)
```

#### [Mario Carneiro (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271682):
> Last modified two days ago!
> Things never stand still around here

#### [Kevin Buzzard (May 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271734):
Things stand still with my mathlib install I can assure you :-)

#### [Kevin Buzzard (May 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271747):
Ok great

#### [Kevin Buzzard (May 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271750):
`@[simp] theorem to_pnat'_coe {n : ℕ} : n > 0 → (n.to_pnat' : ℕ) = n := succ_pred_eq_of_pos`

#### [Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271766):
that starts with a nat, uses `to_pnat'` to get to a pnat and then coerces back to a nat and the claim is we're back where we started

#### [Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271777):
`def to_pnat' (n : ℕ) : ℕ+ := succ_pnat (pred n)`

#### [Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271778):
Ok so this looks good

#### [Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271785):
if you unravel then we're claiming that succ (pred n) = n

#### [Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271786):
and this is not rfl

#### [Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271789):
indeed it's not even true

#### [Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271816):
it's false for n=0

#### [Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271835):
but we have the hypo n > 0

#### [Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271843):
so we need a lemma that says n > 0 implies succ pred n = n

#### [Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271849):
and that would be called something like `succ_pred_eq_of_pos`

#### [Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271850):
which it indeed is

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271869):
Ok nearly there

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271876):
oh one more simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271882):
you see this is exactly what I don't get

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271885):
who decides (a) what to prove (b) what to make a simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271889):
We have just proved 10 trivial things

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271892):
`@[simp] theorem coe_to_pnat' (n : ℕ+) : (n : ℕ).to_pnat' = n := eq (to_pnat'_coe n.pos)`

#### [Mario Carneiro (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271896):
This is a very basic file, so it has almost nothing but simp lemmas

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271897):
look!

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271899):
We just proved `n = n` again

#### [Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271902):
let's make it a simp lemma!

#### [Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271950):
to_pnat' is a bit funny isn't it

#### [Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271959):
`def to_pnat' (n : ℕ) : ℕ+ := succ_pnat (pred n)`

#### [Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271964):
sends n to n if n is positive

#### [Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271967):
and 0 to 1

#### [Kevin Buzzard (May 29 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271974):
because nobody listens to me when I say it should be 37

#### [Mario Carneiro (May 29 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271991):
hey, the succ pred thing wouldn't work with 37

#### [Kevin Buzzard (May 29 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271992):
and perhaps in this particular case they're right

#### [Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272066):
Ok so we basically think of every possible way we can move between nats and pnats and then figure out what is true and make every simplification a simp lemma

#### [Mario Carneiro (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272079):
exactly

#### [Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272088):
Now here's a meaty bit of file

#### [Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272092):
```lean
instance : comm_monoid ℕ+ :=
{ mul       := λ m n, ⟨m.1 * n.1, mul_pos m.2 n.2⟩,
  mul_assoc := λ a b c, subtype.eq (mul_assoc _ _ _),
  one       := succ_pnat 0,
  one_mul   := λ a, subtype.eq (one_mul _),
  mul_one   := λ a, subtype.eq (mul_one _),
  mul_comm  := λ a b, subtype.eq (mul_comm _ _) }
```

#### [Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272101):
it's a commutative monoid!

#### [Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272109):
You can see what Lean thinks the axioms for a commutative monoid are, right there

#### [Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272133):
Now if I had been doing this I would have done `instance : has_mul pnat := <...>` first

#### [Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272135):
outside the monoid

#### [Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272142):
and I would have done `has_one pnat`

#### [Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272147):
Mario -- does your pnat have a mul?

#### [Mario Carneiro (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272150):
yes, it's right there

#### [Mario Carneiro (May 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272203):
`comm_monoid` implies `has_mul`

#### [Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272232):
If I type `#print comm_monoid`

#### [Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272243):
I can't see this

#### [Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272252):
Do I have to look at the source code to see that comm_monoid extends has_mul?

#### [Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272254):
Or have I misunderstood?

#### [Mario Carneiro (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272264):
`comm_monoid` extends `monoid` which extends `semigroup` which extends `has_mul`

#### [Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272268):
`class comm_monoid (α : Type u) extends monoid α, comm_semigroup α`

#### [Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272331):
but you had to know that

#### [Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272336):
I could have written comm_monoid in a different way

#### [Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272338):
and it would have _looked_ like there was a mul

#### [Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272339):
but you wouldn't have got the notation

#### [Kevin Buzzard (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272343):
so I have to look in the source code to check my mul is a mul?

#### [Mario Carneiro (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272353):
```
set_option pp.implicit true
#check (by apply_instance : has_mul ℕ+)
-- @semigroup.to_has_mul ℕ+ (@monoid.to_semigroup ℕ+ (@comm_monoid.to_monoid ℕ+ pnat.comm_monoid)) : has_mul ℕ+
```

#### [Kevin Buzzard (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272357):
The technical point here, for those wondering, is how I can get Lean to use the notation `*` for multiplication of pnats

#### [Mario Carneiro (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272369):
you already have the notation

#### [Mario Carneiro (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272370):
after that instance

#### [Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272409):
after making it a commutative monoid

#### [Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272416):
but you didn't know for sure that was going to happen

#### [Mario Carneiro (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272419):
proving it's a comm monoid a fortiori implies it's a monoid and a has_mul and all that

#### [Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272425):
you could only work it out by doing it and then checking that the multiplication notation stuck

#### [Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272430):
with your #check

#### [Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272434):
if you had wanted to know before writing the code

#### [Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272436):
you would have had to read Lean source code

#### [Mario Carneiro (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272444):
If you define something with a `mul := ` field it's in all likelihood extending `has_mul`

#### [Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272451):
you can't just work it out by querying the system

#### [Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272458):
exactly

#### [Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272469):
You had to rely on someone else being sensible

#### [Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272471):
```lean
instance : comm_monoid ℕ+ :=
{ mul       := λ m n, ⟨m.1 * n.1, mul_pos m.2 n.2⟩,
  mul_assoc := λ a b c, subtype.eq (mul_assoc _ _ _),
  one       := succ_pnat 0,
  one_mul   := λ a, subtype.eq (one_mul _),
  mul_one   := λ a, subtype.eq (mul_one _),
  mul_comm  := λ a b, subtype.eq (mul_comm _ _) }
```

#### [Mario Carneiro (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272473):
you can either read the code, the inheritance hierarchy, or get lean to tell you

#### [Kevin Buzzard (May 29 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272512):
But you didn't get Lean to tell you

#### [Mario Carneiro (May 29 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272523):
no because I knew that `comm_monoid` extends `has_mul` (and it wouldn't make sense any other way)

#### [Kevin Buzzard (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272538):
```lean
structure tricky1 (G : Type) :=
(mul : G → G → G)
(tricky_bit : 0 = 1)
```

#### [Mario Carneiro (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272539):
It is important that `has_mul` be declared only once though

#### [Kevin Buzzard (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272546):
```lean
structure tricky2 (G : Type) extends has_mul G :=
(tricky_bit : 0 = 1)
```

#### [Mario Carneiro (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272555):
only `tricky2` gets the notation, yes

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272596):
but your method for checking this fails

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272607):
because you can't make any instances

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272614):
`#check (by apply_instance : has_mul ℕ+)`

#### [Kenny Lau (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272615):
sorry, you can

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272620):
your method relied on pnat existing

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272625):
show me Kenny :-)

#### [Kenny Lau (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272628):
just `sorry` everything

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272630):
Fair enough

#### [Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272634):
even mul?

#### [Kevin Buzzard (May 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272638):
(deleted)

#### [Kevin Buzzard (May 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272649):
I seem to have wandered a bit

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272700):
OK so what do we need for mul -- clearly we need a proof that if a > 0 and b > 0 then a * b > 0, and we think of what a good name for this lemma would be, and we think "oh maybe `mul_pos_of_pos_of_pos`

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272706):
and then we think "wait a minute that's too long"

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272707):
why don't we just go with mul_pos

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272709):
and indeed that's what it is

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272710):
naming is an art

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272712):
and it's another thing mathematicians are bad at

#### [Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272713):
The only training we get

#### [Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272719):
is "Now by lemma 3.1 and 3.2 we see that Theorem A is proved!"

#### [Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272724):
from our teachers

#### [Mario Carneiro (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272729):
```

class tricky1 (G : Type) :=
(mul : G → G → G)
(tricky_bit : 0 = 1)

class tricky2 (G : Type) extends has_mul G :=
(tricky_bit : 0 = 1)

section
variables (G : Type) [tricky1 G]
#check (by apply_instance : has_mul G) --fail

instance tricky1.has_mul : has_mul G := ⟨tricky1.mul⟩

#check (by apply_instance : has_mul G) --fixed
end

section
variables (G : Type) [tricky2 G]
#check (by apply_instance : has_mul G) --success
end
```

#### [Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272739):
There you go

#### [Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272741):
couldn't be easier

#### [Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272779):
Now

#### [Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272783):
how are we going to prove all these stupid axioms?

#### [Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272786):
```lean
instance : comm_monoid ℕ+ :=
{ mul       := λ m n, ⟨m.1 * n.1, mul_pos m.2 n.2⟩,
  mul_assoc := λ a b c, subtype.eq (mul_assoc _ _ _),
  one       := succ_pnat 0,
  one_mul   := λ a, subtype.eq (one_mul _),
  mul_one   := λ a, subtype.eq (mul_one _),
  mul_comm  := λ a b, subtype.eq (mul_comm _ _) }
```

#### [Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272787):
mul_assoc -- that's already proved for nats

#### [Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272789):
as is mul_comm

#### [Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272795):
and the full proof of mul_comm is quite long if you have defined pnat as an inductive type with one and succ

#### [Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272804):
so here we see the benefits

#### [Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272821):
the proof of mul_comm is "to check a * b = b * a, all we have to do is to check the underlying nats are the same, which is true because that's mul_comm for nat"

#### [Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272827):
was subtype.eq a simp lemma?

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272867):
oh no

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272869):
of course not

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272871):
it has an implies

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272875):
so we can't hope to prove that with simp I guess

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272878):
all the proofs are the same

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272885):
on the other hand it still feels like a machine could have written those four proofs

#### [Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272888):
whereas I suspect Mario wrote them

#### [Kevin Buzzard (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272905):
Mario, why isn't there some weird tactic which deduces a bunch of lemmas for subtypes from the corresponding lemmas for the types?

#### [Patrick Massot (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272907):
We still have no conclusive proof that Mario is not a machine

#### [Kevin Buzzard (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272910):
true

#### [Patrick Massot (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272916):
This situation looks like what Simon solve for pi instances

#### [Kevin Buzzard (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272917):
People like Simon Hudon are good at writing that sort of thing

#### [Patrick Massot (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272921):
Where is Simon by the way?

#### [Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272956):
he's cool -- don't underestimate him

#### [Patrick Massot (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272960):
Haven't we lost him?

#### [Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272965):
All that's left is `one`

#### [Mario Carneiro (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272967):
because the proof is so short it's not worth automating

#### [Mario Carneiro (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272970):
there is a balance point there

#### [Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272976):
and Mario used succ_pnat, there were 5 other ways he could have done it, I am pretty sure that 1 > 0 is a named theorem, he could have used that

#### [Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272981):
I don't think it matters

#### [Mario Carneiro (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272982):
If I had to define a hundred more like that, sure

#### [Kevin Buzzard (May 29 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272985):
I think every method will produce basically the same term

#### [Kevin Buzzard (May 29 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272994):
All that's left is this:

#### [Kevin Buzzard (May 29 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272996):
```lean

@[simp] theorem one_coe : ((1 : ℕ+) : ℕ) = 1 := rfl

@[simp] theorem mul_coe (m n : ℕ+) : ((m * n : ℕ+) : ℕ) = m * n := rfl

/-- The power of a pnat and a nat is a pnat. -/
def pow (m : ℕ+) (n : ℕ) : ℕ+ :=
⟨m ^ n, nat.pos_pow_of_pos _ m.pos⟩

instance : has_pow ℕ+ ℕ := ⟨pow⟩

@[simp] theorem pow_coe (m : ℕ+) (n : ℕ) : (↑(m ^ n) : ℕ) = m ^ n := rfl

end pnat
```

#### [Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273053):
one_coe -- who knows why this is a simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273057):
Where does it end

#### [Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273060):
two_coe? Why is that not a simp lemma?

#### [Mario Carneiro (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273064):
because that's not an atomic term

#### [Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273068):
mul_coe -- proof is refl

#### [Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273072):
Oh I see

#### [Kevin Buzzard (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273075):
one just _became_ an atomic term

#### [Mario Carneiro (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273076):
the simp lemma would be about `\u bit0 n = bit0 \u n`

#### [Kevin Buzzard (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273084):
when you decided that the fact that it was a monoid was worth proving

#### [Kevin Buzzard (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273097):
and finally power

#### [Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273144):
There's a has_pow thing instance. That presumably is tied to the `^` notation

#### [Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273146):
how new-fangled and fancy

#### [Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273149):
it wasn't like this when I learnt it

#### [Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273154):
`#print notation ^`

#### [Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273157):
`_ `^`:80 _:79 := has_pow.pow #1 #0`

#### [Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273169):
Ok so the definition of pow is "work out pow in nats"

#### [Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273180):
but you now need to prove that if m>0 and n>=0 then m^n>0

#### [Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273182):
and if this was me 6 months ago

#### [Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273186):
I would think "oh I quite fancy this one"

#### [Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273188):
"induction on n should do it"

#### [Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273190):
and I'd prove it

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273229):
but that's not the way to think about Lean

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273230):
the way to think about it is

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273239):
"this looks pretty standard -- m > 0 implies m^n > 0"

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273245):
maybe the person who was implementing pow on nat thought of this

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273248):
and even if they didn't

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273253):
maybe some obsessive mathlib guy thought of it

#### [Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273259):
and maybe they gave it a name

#### [Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273273):
and maybe it's someething like `pos_pow_of_pos`

#### [Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273279):
This is the way to write Lean

#### [Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273282):
don't write the code because you can

#### [Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273287):
try and find the code someone else wrote already that does it

#### [Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273291):
write `nat.pos_pow` and hit ctrl-space

#### [Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273292):
and see if you get lucky

#### [Kevin Buzzard (May 29 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273351):
note that Mario used `m.pos` not `m.2`

#### [Kevin Buzzard (May 29 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273355):
That might just be for readability

#### [Kevin Buzzard (May 29 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273359):
The philosophy is that `m.2` is something Lean will always offer you

#### [Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273364):
but `m.pos` is basically better

#### [Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273371):
because it's more readable

#### [Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273375):
`@[simp] theorem pos (n : ℕ+) : (n : ℕ) > 0 := n.2`

#### [Mario Carneiro (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273376):
I'm sure it's just inconsistency

#### [Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273380):
But you are making an interface for pnat

#### [Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273388):
and that interface should involve a nice name for the assertion that a positive nat is positive

#### [Mario Carneiro (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273390):
of course it doesn't matter at all what gets used in the proof

#### [Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273425):
which you should encourage the users to use

#### [Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273442):
It literally makes no difference to anything?

#### [Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273449):
Doesn't it increase compile time by a zillisecond?

#### [Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273456):
you had to look up `pos` in some table

#### [Mario Carneiro (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273464):
It's not literally the same proof term, and who knows how compile time is affected, but whatever difference is extremely minimal

#### [Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273472):
Let me think epsilon more about poe

#### [Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273474):
pow

#### [Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273481):
What is going through the writer's mind when they write this

#### [Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273492):
```lean
/-- The power of a pnat and a nat is a pnat. -/
def pow (m : ℕ+) (n : ℕ) : ℕ+ :=
⟨m ^ n, nat.pos_pow_of_pos _ m.pos⟩
```

#### [Mario Carneiro (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273493):
note that projection notation in both cases only works if `n` has visible type pnat

#### [Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273503):
They are thinking "yay we now have pow"

#### [Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273548):
but then *immediately after*

#### [Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273555):
they think "OK I now have some obligations"

#### [Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273562):
There's the obvious one -- make an instance of has_pow, which is just an elaborate way of saying "let's enable `^` notation"

#### [Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273568):
but then there's the less obvious (to me) fact:

#### [Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273571):
which we've seen lots of times before

#### [Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273576):
we want to check that powers in pnat agree with powers in nat

#### [Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273578):
and even though the proof is refl

#### [Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273580):
this looks like it should be a simp lemma

#### [Kevin Buzzard (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273634):
It says "if we coerce m ^ n to nat we get what we expect"

#### [Kevin Buzzard (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273641):
That is a way of thinking which is not normally taught to the mathematician

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273650):
to define pow : pnat -> nat -> nat we just use induction

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273652):
to prove it lands in pnat we prove a lemma

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273653):
and that's the end

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273654):
We stop here:

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273655):
```lean
def pow (m : ℕ+) (n : ℕ) : ℕ+ :=
⟨m ^ n, nat.pos_pow_of_pos _ m.pos⟩

instance : has_pow ℕ+ ℕ := ⟨pow⟩
```

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273657):
We don't do this bit

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273659):
`@[simp] theorem pow_coe (m : ℕ+) (n : ℕ) : (↑(m ^ n) : ℕ) = m ^ n := rfl`

#### [Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273662):
but in CS if you don't do this

#### [Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273704):
then your users moan that they used a pnat 50 lines ago and it won't disappear

#### [Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273705):
even though we only care about nats now

#### [Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273710):
in fact did we prove all the coercions?

#### [Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273711):
`@[simp] theorem mul_coe (m n : ℕ+) : ((m * n : ℕ+) : ℕ) = m * n := rfl`

#### [Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273716):
`@[simp] theorem one_coe : ((1 : ℕ+) : ℕ) = 1 := rfl`

#### [Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273723):
`@[simp] theorem add_coe (m n : ℕ+) : ((m + n : ℕ+) : ℕ) = m + n := rfl`

#### [Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273733):
They all got proved

#### [Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273744):
Does that mean that if I have some complicated number made using lots of pnats and addition and multiplication etc

#### [Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273745):
and then I made it a nat

#### [Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273747):
then simp would remove all the pnats for me?

#### [Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273748):
I think it might!

#### [Kevin Buzzard (May 29 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273796):
```lean
variables (a b c : nat)
variables (ha : a > 0) (hb : b > 0) (hc : c > 0)
```

#### [Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273811):
```lean
def A : pnat := ⟨a,ha⟩
def B : pnat := ⟨b,hb⟩
def C : pnat := ⟨c,hc⟩
```

#### [Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273818):
One thing I learnt a while ago was that instead of asking "can Lean do this"

#### [Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273822):
it's not hard to just make Lean try to do it yourself

#### [Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273827):
you just use variables to make stuff

#### [Kevin Buzzard (May 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273890):
rofl

#### [Kevin Buzzard (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273906):
I need to work harder

#### [Kevin Buzzard (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273925):
dammit

#### [Kevin Buzzard (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273937):
```lean
variables {a b c : nat}
variables {ha : a > 0} {hb : b > 0} {hc : c > 0}
def A : pnat := ⟨a,ha⟩
def B : pnat := ⟨b,hb⟩
def C : pnat := ⟨c,hc⟩


example : A * (A + B) * (C + (A + B)) = a * (a + b) * (c + (a + b)) := sorry 
```

#### [Kevin Buzzard (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273974):
doesn't typecheck yet

#### [Mario Carneiro (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273996):
Note that `A` and `B` are the same

#### [Mario Carneiro (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274000):
You should use `parameters` instead

#### [Kevin Buzzard (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274008):
for a b c

#### [Kevin Buzzard (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274009):
what about the proofs?

#### [Mario Carneiro (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274010):
all six

#### [Kevin Buzzard (May 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274039):
Parameters can only be used in a section

#### [Kevin Buzzard (May 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274043):
```lean
section
parameters {a b c : nat}
parameters {ha : a > 0} {hb : b > 0} {hc : c > 0}
def A : pnat := ⟨a,ha⟩
def B : pnat := ⟨b,hb⟩
def C : pnat := ⟨c,hc⟩

example : (A * (A + B) * (C + (A + B)) : ℕ) = a * (a + b) * (c + (a + b)) := sorry 

end section 

```

#### [Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274085):
and this typechecks

#### [Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274092):
now let's remove the sorry (which I put there for typechecky reasons)

#### [Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274093):
maybe that's something I could mention

#### [Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274098):
I like my lean files to have no red squiggly underlines ever

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274102):
but I am happy with plenty of sorrys

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274108):
green squiggly underlines ftw

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274111):
the reason for this

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274113):
is that if you make an error

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274116):
then sometimes your new red squiggly underline appears in a weird place

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274118):
and you might not notice it if they're everywhere

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274121):
so every time I split in tactic mode

#### [Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274123):
I always put in two sorrys

#### [Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274162):
etc etc

#### [Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274174):
`example : (A * (A + B) * (C + (A + B)) : ℕ) = a * (a + b) * (c + (a + b)) := rfl `

#### [Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274181):
that's not surprising

#### [Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274188):
`example : ↑(A * (A + B) * (C + (A + B))) = a * (a + b) * (c + (a + b)) := rfl `

#### [Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274193):
that's not surprising

#### [Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274201):
why did he make all these rfl things simp lemmas?

#### [Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274217):
`example : ↑(A * (A + B) * (C + (A + B))) = a * (a + b) * (c + (a + b)) := by simp  `

#### [Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274218):
fails :-)

#### [Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274222):
*doh*

#### [Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274232):
aah well so it was probably for another reason

#### [Kevin Buzzard (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274284):
but at least we made it to the end, even if I'm still not 100% sure what makes a good simp lemma. Maybe I'm beginning to get the hang of it.

#### [Mario Carneiro (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274294):
You have to unfold your new definitions

#### [Kevin Buzzard (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274295):
But it's interesting to see the way of thinking -- put new structure on pnat, now immediately ask yourself if we need some lemmas

#### [Mario Carneiro (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274299):
try `by simp [A, B, C]`

#### [Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274314):
```lean
section
parameters {a b c : nat}
parameters {ha : a > 0} {hb : b > 0} {hc : c > 0}
@[reducible] def A : pnat := ⟨a,ha⟩
@[reducible] def B : pnat := ⟨b,hb⟩
@[reducible] def C : pnat := ⟨c,hc⟩

example : (A * (A + B) * (C + (A + B)) : ℕ) = a * (a + b) * (c + (a + b)) := by simp  

end section
```

#### [Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274321):
That works because I told Lean to unfold A B and C eagerly

#### [Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274333):
`simp [A,B,C]`?

#### [Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274336):
Is `A` a good simp lemma??

#### [Kevin Buzzard (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274383):
Normally when you start putting `simp [random thing]` it complains that the random thing isn't a good simp lemma

#### [Kevin Buzzard (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274392):
```lean

section
parameters {a b c : nat}
parameters {ha : a > 0} {hb : b > 0} {hc : c > 0}
def A : pnat := ⟨a,ha⟩
def B : pnat := ⟨b,hb⟩
def C : pnat := ⟨c,hc⟩

example : (A * (A + B) * (C + (A + B)) : ℕ) = a * (a + b) * (c + (a + b)) := by simp [A,B,C]


end section 
```

#### [Kevin Buzzard (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274396):
well blow me down it works

#### [Mario Carneiro (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274400):
`simp [my_def]` where `my_def` is a `def` means `simp [my_def.<equation lemmas>]`

#### [Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274405):
ooh

#### [Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274411):
How do I see A's equation lemmas?

#### [Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274420):
`#print prefix A `

#### [Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274428):
```lean
A : Π {a : ℕ} {ha : a > 0}, ℕ+
A.equations._eqn_1 : ∀ {a : ℕ} {ha : a > 0}, A = ⟨a, ha⟩
```

#### [Kevin Buzzard (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274479):
That doesn't look like a good simp lemma to me

#### [Mario Carneiro (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274482):
not by default, no

#### [Kevin Buzzard (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274486):
there are variables on the RHS which don't appear on the LHS

#### [Mario Carneiro (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274492):
Actually they appear on the left too

#### [Kevin Buzzard (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274498):
and a wise person once told me not to put these into simp

#### [Mario Carneiro (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274501):
they are hidden because of the parameter thing

#### [Mario Carneiro (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274521):
or possibly because you have `{a} {ha}`

#### [Kevin Buzzard (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274523):
heh

#### [Kevin Buzzard (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274524):
I think the latter

#### [Kevin Buzzard (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274531):
Ok so we got there

#### [Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274569):
and that's pnat.

#### [Mario Carneiro (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274572):
if they didn't appear on the left, you could use this theorem to prove 1 = 2

#### [Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274578):
Oh that would be a cool application of pnat

#### [Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274586):
I need to go to tend to the family

#### [Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274589):
but there's a random thing

#### [Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274593):
which people will be able to link to and look at later on

#### [Kevin Buzzard (May 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274605):
and in particular in a couple of weeks when I am supposed to be teaching a bunch of mathematicians Lean and they don't know how to make structures

#### [Kevin Buzzard (May 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274610):
and it was much easier to write than a proper document

#### [Kevin Buzzard (May 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274613):
Thanks for the help Mario and Patrick and Johan and others

