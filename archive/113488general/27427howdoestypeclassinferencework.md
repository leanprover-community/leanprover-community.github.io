---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27427howdoestypeclassinferencework.html
---

## Stream: [general](index.html)
### Topic: [how does type class inference work?](27427howdoestypeclassinferencework.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151259224):
```lean
class foo (A : Type) :=
(blah : ℕ)

class bar (A : Type) extends foo A :=
(blah2 : bool)

class baz (A : Type) extends foo A .

instance : bar ℤ := {blah := 4, blah2 := tt}

example : bar ℤ := by apply_instance -- works

example : baz ℤ := by apply_instance -- fails
```

Why doesn't this work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151259885):
why would it work? You declared an instance of `bar` but not `baz`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260147):
I can figure out how to make an instance of `baz`, that's why I can believe it would work. All the fields are there. This is my problem -- I don't know what the type class inference system is _doing_.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260186):
Oh sorry there's a typo -- I meant to write

`example : foo ℤ := by apply_instance -- works`

I didn't declare an instance of `foo` but it found it anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260244):
I literally do not know what it can and cannot do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260256):
All I know is that it can do less than me, because I can solve `baz`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260277):
`class baz (A : Type) extends foo A .`
this creates an instance `baz.to_foo`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260291):
if you want to make `baz` from `foo` then you would need to use `{ .. infer_instance }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260308):
Well, maybe I should just create an instance `baz.from_foo`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260369):
or maybe `foo.to_baz` would be more appropriate.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260399):
congratulations, you've thrown yourself into a loop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260514):
```lean
class foo (A : Type) :=
(blah : ℕ)

class bar (A : Type) extends foo A :=
(blah2 : bool)

class baz (A : Type) extends foo A .

instance : bar ℤ := {blah := 4, blah2 := tt}

example : foo ℤ := by apply_instance -- works

-- type class inference is so stupid, why doesn't it just guess this.
instance foo.to_baz (A : Type) [foo A] : baz A := by refine {}

example : foo ℤ := by apply_instance -- fails? WTF?

example : baz ℤ := by apply_instance -- still fails
```

I broke everything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260535):
I don't understand why everything is broken. Everything is defeq, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260617):
you now have `foo.to_baz` and `baz.to_foo`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260621):
so the machine gets stuck forever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260645):
`example (A : Type) (H : foo A) : H = baz.to_foo A := rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260716):
I don't understand why it gets stuck forever. What is it doing? I am pretty convinced it's not playing the "let's see how many instances I can make from this instance, for no reason whatsoever" game. I ask the type class inference system to produce me a term of a typeclass, it should just try and try until it finds one and then stop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260728):
Of course I completely understand that I have made a loop. What I don't understand is why this even matters.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260734):
oh it *is* playing that game

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260737):
It is??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260742):
wait no it isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260756):
But your response makes me think that you can write some simple thing which will make it play this game.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260772):
well you want it to figure out `baz`. then it goes like "hey I can make this from `foo`". then it goes like "hey I can make this from `baz`". ad nauseam

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260775):
so maybe priority is the answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260823):
Do you know where it starts? At the top or the bottom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260859):
It says "Hmm, I want to make  an instance of `baz A`". Now does it say "OK so how do we make instances of `baz A`? or does it say "OK what other typeclasses can I make with `A`"? Hmm, I guess it must be the former.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260883):
it is the former

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260925):
So the type class system looks through *all instances* and tries to find one whose head term is `baz`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260929):
Say it finds ten such things. What does it do now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260970):
apply each one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260973):
(but mind you, it uses depth-first search)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260979):
"Head term" -- is that the right phrase? I mean "a term which is a function `baz [something]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260983):
What is depth-first search?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261002):
depth-first search = dig this hole as deep as possible until you find gold or you are blocked by a stone, and then move on to the next hole

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261014):
Is this the one where it finds the first instance of `baz A` and finds that it needs `moo A` and it checks for a term of type `moo A` and temporarily forgets all about the other nine ideas about `baz` and just looks for `moo` stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261087):
breadth-first search = dig this hole 1 cm, go to next hole and dig 1cm, and so on until you run out of holes, and then go back to the first hole and dig 1cm, etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261114):
```quote
Is this the one where it finds the first instance of `baz A` and finds that it needs `moo A` and it checks for a term of type `moo A` and if it can't find that it forgets all about the other nine ideas about `baz` and just looks for `moo` stuff?
```
 precisely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261125):
How does it conclude that it is blocked by a stone?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261151):
Can this only happen when there are literally no instances which have the right head term or whatever the phrase is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261160):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261214):
so for example there is no instance that produces `ordered_canonical_discrete_ordered_field` or whatever the flying that is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261221):
because it's the highest structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261260):
```lean
class H1 (A : Type) .

class H11 (A : Type) extends H1 A .

class H12 (A : Type) extends H1 A .

```

Does this segfault for you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261317):
I am trying to do some simple experiments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261336):
no it doesn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261421):
```quote
Can this only happen when there are literally no instances which have the right head term or whatever the phrase is?
```
 No, it's sufficient that no instance of the target class can be unified with the target

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261476):
Hmm, thanks, I'll restart VS Code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261537):
@**Sebastian Ullrich** what's the difference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261551):
The head symbol could match but not the rest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261571):
```lean
class H1 (A : Type) .

class H11 (A : Type) extends H1 A .

class H12 (A : Type) extends H1 A .

class H111 (A : Type) extends H11 A .

class H121 (A : Type) extends H12 A .

instance H1.to_H11 (A : Type) [H1 A] : H11 A := by refine {}

instance H11.to_H111 (A : Type) [H11 A] : H111 A := by refine {}

instance : H121 unit := by refine {}

instance : H111 unit := by apply_instance


```

That seems to have gone really well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261646):
I am trying to get into trouble. I am trying to get max class inference thingy error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261672):
but you didn't create any loop...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261675):
oh wait you did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261679):
Right, H1 and H11 loop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261682):
but I managed to get past the loop and up to H111

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262058):
Kevin, in your case there exactly one instance to try at each step, and it clearly succeeds without ever risking a loop:
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : H111 unit := @H11.to_H111 ?x_1 ?x_2
[class_instances] (1) ?x_2 : H11 unit := @H1.to_H11 ?x_3 ?x_4
[class_instances] (2) ?x_4 : H1 unit := @H12.to_H1 ?x_5 ?x_6
[class_instances] (3) ?x_6 : H12 unit := @H121.to_H12 ?x_7 ?x_8
[class_instances] (4) ?x_8 : H121 unit := unit.H121
```
You can simply draw the instance graph and see it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262747):
I want to make it get stuck in a loop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262764):
To find `H111` it suffices to find `H1`. Can I make it look for `H1` by going back to `H12`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262817):
Oh I see, that instance is not even there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262875):
```lean
class H1 (A : Type) .

class H11 (A : Type) extends H1 A .

class H12 (A : Type) extends H1 A .

class H111 (A : Type) extends H11 A .

class H121 (A : Type) extends H12 A .

instance H1.to_H11 (A : Type) [H1 A] : H11 A := by refine {}

instance H11.to_H111 (A : Type) [H11 A] : H111 A := by refine {}

instance H1.to_H12 (A : Type) [H1 A] : H12 A := by refine {}

instance H12.to_H121 (A : Type) [H12 A] : H121 A := by refine {}

instance : H121 unit := by refine {}

instance : H111 unit := by apply_instance -- max depth reached

```

Bingo.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262890):
So whatever is type class inference thinking here? Why go back to `H12` when we have been there already?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263019):
```lean
set_option trace.class_instances true
instance : H111 unit := by apply_instance -- max depth reached

```

gives random stuff such as

```
[class_instances] (0) ?x_0 : has_one ℕ := unsigned.has_one
```

Who said anything about nat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263079):
I'm glad the type class inference system's job isn't finding its way out of mazes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263165):
usually one writes a depth first search with a search stack to prevent loops like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263180):
The nat thing is related to my question to Sebastian about shortcut. It has nothing to do with your problem, it's something Lean solves for itself in its meta-work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263184):
I'm not sure why typeclass inference doesn't have one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263234):
then again, this wouldn't prevent problems with loops that look different the second time around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263243):
i.e. the same instances are being used but the instantiations are different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151264966):
OK this is great. I have to interview a bunch of people now but I will probably be back later on with more dumb questions. This has been a great start. Thanks to all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 10 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151390897):
Conceptually, Lean could require one to prove instance backchaining is well-founded.  Haskell has static checks to ensure this, but those can be bypassed via language pragma.


{% endraw %}
