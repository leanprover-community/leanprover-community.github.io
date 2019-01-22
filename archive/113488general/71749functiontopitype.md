---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71749functiontopitype.html
---

## [general](index.html)
### [function to pi type](71749functiontopitype.html)

#### [Johan Commelin (May 23 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967340):
Newbie alert! I can't find anything in PIL or TPIL on how to construct a function to a Pi type. If I have `Y : I \to Type` and `f : \Pi i, X \to Y i`, how do I turn this into `X \to (\Pi i, Y i)`?

#### [Johan Commelin (May 23 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967345):
Context: I want to prove that the latter function is continuous if all the `f i` are continuous.

#### [Kevin Buzzard (May 23 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967387):
use lambda?

#### [Johan Commelin (May 23 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967399):
O.o... lol

#### [Kevin Buzzard (May 23 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967416):
`example (I : Type) (X : Type) (Y : I → Type) (f : Π (i : I), X → Y i) : X → (Π i, Y i) := λ x, λ i, f i x`

#### [Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967457):
Pi and structures are the only way of defining types

#### [Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967458):
and then lambda and `{ }` are the only way of defining terms

#### [Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967459):
or something

#### [Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967461):
Pi and inductive types

#### [Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967463):
lambda and mk

#### [Kevin Buzzard (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967477):
Can one say that lambda is some sort of a constructor for Pi types?

#### [Kevin Buzzard (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967478):
Or is that abuse of language?

#### [Kevin Buzzard (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967530):
Come to think of it, I am not sure I used a single inductive type in the whole scheme thing which wasn't a structure

#### [Sebastian Ullrich (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967541):
Did you use `nat`? :stuck_out_tongue:

#### [Mario Carneiro (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967546):
no, in the type theory literature that's common

#### [Kevin Buzzard (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967549):
I mean

#### [Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967560):
actually I don't think I did use nat

#### [Mario Carneiro (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967561):
lambda is the intro rule for pi, and application is the elim form

#### [Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967567):
but what I meant to say was that I rolled my own structures many times

#### [Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967572):
but they were all structures

#### [Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967576):
Sebastian's comment is interesting

#### [Mario Carneiro (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967618):
There are tons of interesting inductive types beyond nat

#### [Kevin Buzzard (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967624):
because how can a mathematician be doing anything if they're not using the basic math type, namely nat

#### [Mario Carneiro (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967626):
the primitive recursive functions are obviously defined inductively

#### [Kevin Buzzard (May 23 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967639):
but I think this maybe shows some disconnect between what the CS people think maths is, and what the maths people think it is

#### [Kevin Buzzard (May 23 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967643):
e.g. Mario saying "w00t I did some more Matiyesevich" and Patrick responding "when will you get back to math"

#### [Mario Carneiro (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967687):
I'm mentioning that because it's fresh on my mind

#### [Patrick Massot (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967690):
That answer was mostly a joke

#### [Mario Carneiro (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967691):
your scheme stuff is a bit too category-theoretic so have good examples

#### [Patrick Massot (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967693):
I understand that Mario think Matiyesevich is math

#### [Kevin Buzzard (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967694):
My scheme stuff is central to what a mathematician thinks that mathematics is

#### [Mario Carneiro (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967696):
unless you consider freely generated stuff to be inductive

#### [Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967697):
and Patrick and I know well that most people in our departments would not have a clue about the Matiyesevich stuff

#### [Mario Carneiro (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967701):
it's obviously not all of math though

#### [Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967707):
"a bit too category-theoretic" -- this is a very weird thing to day

#### [Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967710):
Essentially nobody in my department is interested in categories

#### [Mario Carneiro (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967711):
it helps to look at more "concrete" areas, actual constructions and not constraints

#### [Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967712):
but many are interested in schemes

#### [Mario Carneiro (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967714):
constraints tend to be noninductive

#### [Kenny Lau (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967718):
```quote
Essentially nobody in my department is interested in categories
```
johannes nicaise is

#### [Mario Carneiro (May 23 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967720):
so not "definition of scheme" but "X is a scheme"

#### [Kevin Buzzard (May 23 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967771):
Johannes knows what a category is, like most of us do

#### [Kevin Buzzard (May 23 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967777):
but Johannes does not study them in their own right, like most of us don't

#### [Kevin Buzzard (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967780):
For most of us it's just a language

#### [Patrick Massot (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967784):
Today's milestone is of type "X is a scheme"

#### [Mario Carneiro (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967791):
honestly I still have only the foggiest idea of what you guys actually do

#### [Kevin Buzzard (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967793):
I know

#### [Mario Carneiro (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967796):
I do all this math and you guys just say "oh that CS guy"

#### [Kevin Buzzard (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967799):
doing that CS stuff

#### [Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967843):
This is one of the big reasons why this stuff isn't more popular

#### [Patrick Massot (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967846):
So let's gather at the end of August and discuss that

#### [Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967848):
Mario, I honestly think that if we wrote the definition of a perfectoid space in Lean

#### [Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967850):
then some mathematicians would go "wooah"

#### [Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967854):
and your honest opinion might be "it's just a definition"

#### [Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967856):
but it is an extremely fashionable definition

#### [Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967859):
and a very delicate one

#### [Mario Carneiro (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967868):
I have no clue why I should care about perfectoid spaces, besides the societal stuff

#### [Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967870):
And people like me prove basic lemmas about perfectoid spaces

#### [Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967872):
and get them published in good journals

#### [Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967883):
If you want to get a post-doc

#### [Johan Commelin (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967884):
@**Mario Carneiro** That's a very long story... but people are interested in them because they help us make progress on the Langlands programme

#### [Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967921):
then you have to impress the right people

#### [Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967931):
but the right people in which discipline?

#### [Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967933):
And there is a big disconnect here

#### [Johan Commelin (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967935):
And people are interested in Langlands because... well, he just won the Abel prize for his impact on maths...

#### [Mario Carneiro (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967938):
 I want to see it develop more inline with the history - starting concrete and tending towards abstraction as things get more complicated

#### [Johan Commelin (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967940):
Langlands program pervades modern number theory and geometry

#### [Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967942):
The Langlands Philosophy is arguably one of the central problems in maths and definitely one of the central problems in number theory

#### [Johan Commelin (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967945):
It places Fermat's Last Theorem in a bigger picture

#### [Mario Carneiro (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967951):
So maybe we should start with fermat's last theorem

#### [Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967952):
And you CS guys have made 0 progress with it

#### [Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967955):
FLT is really old

#### [Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967957):
it's all been done

#### [Mario Carneiro (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967958):
not in lean

#### [Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967960):
it would take a decade to formalise

#### [Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967963):
by which time it would be even older

#### [Johan Commelin (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967968):
@**Mario Carneiro** Yes, but to do FLT, you have to define a scheme

#### [Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126967969):
and *nobody would care*

#### [Mario Carneiro (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968009):
but then it would be motivated

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968010):
Proof that nobody would care: I went around and asked a bunch of people if they would care

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968014):
and they said no

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968018):
_you_ would be motivated

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968019):
no mathematician would care

#### [Mario Carneiro (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968024):
I think everyone wants motivation

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968026):
Defining a perfectoid space in Lean is 1000 times easier

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968029):
and _some_ mathematicians would care

#### [Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968033):
I mean, a non-trivial percentage would notice

#### [Mario Carneiro (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968038):
Even just setting up a foundation for FLT would be tremendously satisfying for me

#### [Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968039):
Well, if FLT is formalised, then certainly lots of other modern stuff will be easily formalisable

#### [Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968044):
So it still would be a major milestone

#### [Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968046):
because Peter Scholze is probably going to get a Fields Medal

#### [Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968052):
```quote
Even just setting up a foundation for FLT would be tremendously satisfying for me
```
Well then you need to start caring about schemes

#### [Mario Carneiro (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968053):
I'm all about the library building, making impossible goals feasible

#### [Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968055):
```quote
Even just setting up a foundation for FLT would be tremendously satisfying for me
```
What do you mean with that?

#### [Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968057):
The reason FLT is impossible

#### [Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968060):
Formalising the statement of the modularity theorem?

#### [Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968063):
is because you say that Cauchy Integral Formula is hard

#### [Mario Carneiro (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968080):
FLT is in a whole language of its own, let's get that theory

#### [Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968104):
But that is a drop in an ocean of analysis

#### [Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968109):
all of which needs to be done to prove the trace formula

#### [Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968112):
which in every known proof of FLT is an essential prerequisite

#### [Johan Commelin (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968113):
```quote
FLT is in a whole language of its own, let's get that theory
```
What do you mean with that?

#### [Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968118):
Mario -- like Johan I don't understand what you're saying

#### [Mario Carneiro (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968119):
I like to formalize "essential prerequisites"

#### [Johan Commelin (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968123):
Statements or proofs?

#### [Mario Carneiro (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968131):
both?

#### [Johan Commelin (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968133):
Great

#### [Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968134):
Well you can spend two years formalising Cauchy Integral Formula and then basic stuff about integration on complex manifolds

#### [Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968136):
and no mathematician will care

#### [Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968140):
and after all that

#### [Johan Commelin (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968141):
Schemes are epsilon-th prerequisite for FLT

#### [Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968147):
you will proudly be able to formalise the statement of the trace formula

#### [Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968149):
and no mathematician will care

#### [Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968196):
because we proved it in the 1960s for SL_2

#### [Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968199):
like the odd order theorem

#### [Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968208):
and that's what we need

#### [Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968212):
There is your major obstacle for proving FLT

#### [Mario Carneiro (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968215):
and then you will have a demo where you show people how to work with basic calculus and it won't be a barrier anymore

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968222):
And then 10 years later we have a proof of a 35-year-old theorem

#### [Mario Carneiro (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968224):
it's not about impressing people with the statements, it's about making regular stuff pain free

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968227):
and you have seen how this turns out

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968228):
*No*

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968230):
it is about impressing people

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968232):
because that's where the jobs are

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968237):
and that's where the money is

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968240):
that's where the funding is

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968243):
that's how you get promotions

#### [Mario Carneiro (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968247):
It's not what they want, it's what they need

#### [Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968248):
that's how you get money to support your family

#### [Andrew Ashworth (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968250):
i'm curious if MSR has any work on this; I know they want to prove certain properties of encryption protocols

#### [Mario Carneiro (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968293):
so you have to split your effort between flashy stuff and foundations

#### [Kevin Buzzard (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968298):
I absolutely agree that in a perfect world we should all just drop what we're doing and prove the trace formula and tell mathematicians to stop producing more maths

#### [Kevin Buzzard (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968301):
but that won't happen

#### [Mario Carneiro (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968308):
I don't think it need be so dichotomous

#### [Johan Commelin (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968309):
@**Mario Carneiro** FLT will never be formalised if it takes one of the leading number theorists of our time over 3 months to formalise the definition of the most basic gadget in the proof

#### [Kevin Buzzard (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968317):
or even me

#### [Johan Commelin (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968320):
Really, defining a scheme takes less then an hour in "Introduction to algebraic geometry"

#### [Mario Carneiro (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968322):
Right, so I will formalize the most basic gadgets and then leading number theorists won't have to

#### [Mario Carneiro (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968329):
or kevin

#### [Kevin Buzzard (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968332):
Why not take a break from your formalizing basic gadgets

#### [Johan Commelin (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968335):
@**Mario Carneiro** They will get hopelessly stuck on whatever comes after the basics

#### [Kevin Buzzard (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968336):
and formalize a fancy one with me

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968378):
and let's see the reaction

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968382):
Or

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968383):
if that's too fancy

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968385):
then formalize manifolds with Patrick

#### [Patrick Massot (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968386):
Kevin did formalize the basic gadget. Now you have the opportunity to do it right, and I'm sure that would be immensely instructive

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968387):
because at least that's an important object

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968390):
(manifolds)

#### [Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968394):
and people in maths departments use them

#### [Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968402):
as opposed to Diophantine sets

#### [Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968406):
which are just some niche thing

#### [Mario Carneiro (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968409):
which will get me publishing

#### [Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968412):
in your CS world

#### [Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968413):
That's the problem

#### [Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968415):
we seem to live in two different worlds

#### [Mario Carneiro (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968418):
well we've all got mouths to feed

#### [Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968419):
You need your papers

#### [Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968460):
and if the CS guys like the Diophantine set stuff

#### [Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968464):
than that's what they're going to get

#### [Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968467):
but the problem with this approach

#### [Johan Commelin (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968469):
@**Mario Carneiro** You have incredible skills. But atm mathematicians are really unable to use Lean, (except for a couple weirdo nerds like Kevin, Patrick, Scott and me). We really hope that you will help us build the bridge that the regular mathematicians need.

#### [Patrick Massot (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968470):
How is it possible that formalizing Diophantine sets could give you a paper but formalize schemes couldn't?

#### [Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968472):
is that the mathematicians will continue to not give a shit

#### [Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968476):
Patrick, I was going to write something very short

#### [Mario Carneiro (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968479):
I can't publish in a math journal, unless I stop formalizing

#### [Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968480):
but honestly let's face it

#### [Mario Carneiro (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968486):
math journals don't care about that

#### [Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968487):
whatever would I do with a two page paper saying "I wrote down a trivial definition, it took three months, here are some of the interesting problems I ran into"

#### [Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968488):
for sure maths journals don't care

#### [Patrick Massot (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968490):
Why not publishing about formalization of schemes in a CS journal?

#### [Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968491):
and from a CS point of view all I did was formalise a definition

#### [Mario Carneiro (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968493):
CS journals care, but they also care about CS things

#### [Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968495):
I am in a privileged position that I can just do what I like

#### [Kevin Buzzard (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968535):
so I did something I thought was important

#### [Johan Commelin (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968536):
Right, so we need a new journal "Formalisations in Geometry and Number Theory"

#### [Kevin Buzzard (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968537):
That can happen

#### [Kevin Buzzard (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968538):
journals are not hard to start

#### [Patrick Massot (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968543):
As I wrote earlier, I think the really interesting thing to write about would be the whole process starting with an optimistic mathematician knowing nothing about DTT and ending with a usable formalization

#### [Kevin Buzzard (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968548):
That was the story I was going to write

#### [Kevin Buzzard (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968551):
except I can't imagine it's usable yet

#### [Patrick Massot (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968553):
Yes, because it's not done yet

#### [Kevin Buzzard (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968554):
Mario -- I hope you understand that none of this is an implicit criticism of what you do

#### [Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968596):
it is general frustration

#### [Patrick Massot (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968597):
It lacks the stage where Mario or Johannes enters the game seriously

#### [Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968603):
about the state of things

#### [Patrick Massot (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968613):
It's not only frustration, it's also excitement about what could be

#### [Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968617):
that too

#### [Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968618):
but somehow the right people don't exist yet

#### [Patrick Massot (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968619):
If you would accept to play this game

#### [Mario Carneiro (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968622):
The thing is, the things I enjoy are useful to others, but not really publishable results for the most part

#### [Mario Carneiro (May 23 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968637):
I just have to make sure to stay somewhat on task

#### [Patrick Massot (May 23 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968640):
How did Assia got her job then? I think she always formalized math

#### [Mario Carneiro (May 23 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968646):
I think she's my hero

#### [Johan Commelin (May 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968698):
Well, and there is Tom Hales of course. He knows everything about FLT and about formalisation.

#### [Patrick Massot (May 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968702):
Then why don't you start reading that scheme repository?

#### [Johan Commelin (May 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968703):
Still he did not formalise any algebraic geometry or anything in the direction of Langlands yet

#### [Patrick Massot (May 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968746):
I guess Hales knows too much, this prevents him from enjoying Kevin's optimism

#### [Patrick Massot (May 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968748):
Naive optimism is a very important math skill

#### [Patrick Massot (May 23 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968758):
I don't think I was ever able to prove anything without first hugely underestimating the difficulty

#### [Mario Carneiro (May 23 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968822):
Also Johannes and I will be working at the university of Hanoi with Tom on a lean summer school

#### [Patrick Massot (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968829):
I think your hero would write "Scheme theory done right in Lean"

#### [Mario Carneiro (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968832):
As I understand it many of the folks involved in Flyspeck are there, so it should be interesting

#### [Patrick Massot (May 23 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126968887):
I fear Hanoi is a bit too far for me

#### [Andrew Ashworth (May 23 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969103):
ooh, Flyspeck looks interesting! So they proved the optimal packing of balls in 3d space

#### [Andrew Ashworth (May 23 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969117):
Please don't pressure Mario too hard :) For his future career prospects, all the money in formal verification comes from the large software companies

#### [Patrick Massot (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969185):
It's not 100% true

#### [Patrick Massot (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969194):
Since Assia is a counter-example for instance

#### [Andrew Ashworth (May 23 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969264):
I'm not aware of very many other mathematicians outside of Assia who get to work on computer formalized math... whereas, Intel, Amazon, Microsoft, Facebook etc. all have teams of people who do this. Not to mention the smaller companies like Galois and others who do contract work in the field

#### [Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969378):
I want to bring computer formalized maths to mathematics departments

#### [Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969384):
because I think mathematicians don't know what they're missing

#### [Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969386):
both in terms of it making their lives better

#### [Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969387):
and in terms of the fact that some of their arguments are incomplete and they need to be told

#### [Patrick Massot (May 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969392):
I know what they are missing: a - b + b may or may not be equal to a

#### [Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969434):
They are not missing that

#### [Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969439):
that - sign is not a mathematician's minus

#### [Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969440):
I see it and I see "-^*"

#### [Patrick Massot (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969442):
Formalized math in maths departments may be a dream too far away. But we only need two INRIA positions: one for Mario and one for Johannes

#### [Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969443):
with the footnote "this is a different minus, don't expect it to be sensible"

#### [Mario Carneiro (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969446):
actually it's a dot over, not a star

#### [Andrew Ashworth (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969453):
Not even a Field's medalist in Vovoedsky could get mathematicians interested in DTT...

#### [Johan Commelin (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969457):
Because he didn't formalise any AG (= Algebraic Geometry)

#### [Johan Commelin (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969458):
He completely changed fields

#### [Kevin Buzzard (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969462):
In fact you could see this in his Cambridge talk

#### [Johan Commelin (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969463):
I don't think he even formalised the definition of a scheme in all those years

#### [Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969510):
He got interested in formal proof verification because he was worried about bugs in his proofs

#### [Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969516):
but then he decided that DTT or whatever wasn't right for him

#### [Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969518):
so he invented a new thing

#### [Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969519):
with yet another bloody definition of =

#### [Mario Carneiro (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969520):
When you do HoTT though, everything is "more" than what's written

#### [Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969522):
and then all of a sudden there were lots of interesting questions

#### [Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969524):
and then oops

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969525):
who cares about Bloch-Kato any more

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969530):
and he explicitly said this in his Cambridge talk

#### [Mario Carneiro (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969531):
and you get distracted by all the homotopy implications of your definition and never get around to the original goal

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969532):
"So how is Bloch-Kato doing?"

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969534):
"Well, not very well"

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969535):
"I'm pretty sure it's right"

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969536):
"and nobody is working on that right now"

#### [Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969538):
exactly

#### [Mario Carneiro (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969541):
formalizing a scheme in HoTT feels like the wrong application of a tool

#### [Mario Carneiro (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969584):
because you have no interest in the HoTT stuff, it's just a classical definition

#### [Patrick Massot (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969586):
Recently I heard someone claiming a proof of this Simpson conjecture that was missing in order to fix that broken Voevodsky paper that started it all

#### [Johan Commelin (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969588):
True

#### [Patrick Massot (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969596):
https://ncatlab.org/nlab/show/Simpson%27s+conjecture

#### [Johan Commelin (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969597):
@**Mario Carneiro** Unless HoTT helps you to turn *math*-trivial stuff into *formally*-trivial stuff.

#### [Mario Carneiro (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969602):
I like lean because it's not trying to be "more" like this, it's exactly what you are trying to say

#### [Johan Commelin (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function to pi type/near/126969603):
I think Voevodsky thought very hard about transport of structure. And that led him to HoTT

