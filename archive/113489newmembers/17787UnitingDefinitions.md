---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/17787UnitingDefinitions.html
---

## Stream: [new members](index.html)
### Topic: [Uniting Definitions](17787UnitingDefinitions.html)

---


{% raw %}
#### [ Ali Sever (Jul 28 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130457466):
Is there a way I can join perp, perp1 and perp2 into 1 definition? Same thing for perpx.  `l : point → point → set point`
```lean
def perpx (x : point) (A A' : set point) : Prop := line A ∧ line A' ∧ x ∈ A ∧ x ∈ A' ∧
∀ u v, u ∈ A → v ∈ A' → R u x v

def perpx1 (x a b : point) (A : set point) : Prop := a ≠ b ∧ perpx x A (l a b)

def perpx2 (x a b c d : point) : Prop := a ≠ b ∧ c ≠ d ∧ perpx x (l a b) (l c d)

def perp (A A' : set point) : Prop := ∃ x, perpx x A A'

def perp1 (a b : point) (A : set point) : Prop := a ≠ b ∧ perp A (l a b)

def perp2 (a b c d : point) : Prop := a ≠ b ∧ c ≠ d ∧ perp (l a b) (l c d)

notation A ⊥ B  := perp A B

notation A ⊥ B % x  := perpx x A B
```

#### [ Kevin Buzzard (Jul 28 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130457657):
I don't understand the question. What are you unhappy about with what you have?

#### [ Ali Sever (Jul 28 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130457768):
If I leave it like this, I'm going to have to prove everything three times.

#### [ Kevin Buzzard (Jul 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458494):
Are you likely to ever apply `perp` in a situation where `A` and `A'` are not lines?

#### [ Kevin Buzzard (Jul 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458495):
I mean, where you don't already know that they're lines?

#### [ Kevin Buzzard (Jul 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458535):
What I'm saying is that it sounds to me like the fact that `A` is a line should be a hypothesis rather than a conclusion of `perp`

#### [ Kevin Buzzard (Jul 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458612):
Presumably` R` is "these three points make a right angle"? Don't you want something like
`def perpx (x : point) {A A' : set point} (HLA : line A) (HLA' : line A') (HxA : x ∈ A) (HxA' : x ∈ A') :=
∀ u v, u ∈ A → v ∈ A' → R u x v`?

#### [ Kevin Buzzard (Jul 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458720):
`def perp {A A' : set point} (HLA : line A) (HLA' : line A') : Prop := ∃ x, perpx x A A'`

#### [ Kevin Buzzard (Jul 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458723):
I'm just guessing -- but it sounds like you want `perp` to be a predicate which applies only to lines, so you should demand only lines as input. Do you want to apply the idea in other situations?

#### [ Ali Sever (Jul 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459039):
What if I want to prove `perp A A' → something`? From the assumption I can obtain a proof of `line A` and `line A'`, but in your definition,  I have to add those to the hypotheses of every theorem.

#### [ Kevin Buzzard (Jul 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459044):
So you're telling me that you can envisage a situation where you have no idea that `A` and `A'` are lines, but you've managed to prove `perp A A'` anyway?

#### [ Johan Commelin (Jul 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459059):
Ali, that is where `variables` come in handy. Then you don't have to explicitly write them down in the statement of every theorem. You just write them once at the beginning of your section/file.

#### [ Johan Commelin (Jul 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459100):
Also, I can imagine that `line` can be a class, and then type class inference will (hopefully) keep track of which things are proven to be lines.

#### [ Kevin Buzzard (Jul 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459109):
I feel like you're saying the analogue of something like: "I want to define `a<b` for `a` and `b` arbitrary things, and I want it to mean "`a` and `b` are numbers, and `a<b`". And I'm saying "but we already have `a<b` for numbers -- why would you want to talk about arbitrary things which you don't even know are numbers and then start talking about whether one is less than the other? In all cases where it even makes sense to talk about this, you know `a` and `b` are numbers, so that assumption should be an input not an output."

#### [ Ali Sever (Jul 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459201):
So if I change it, does that mean `perp A A'` also implies that they are lines?

#### [ Kevin Buzzard (Jul 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459206):
I'm suggesting that `perp A A'` *doesn't even make sense* unless `A` and `A'` are lines.

#### [ Kevin Buzzard (Jul 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459209):
And there are two ways to do this.

#### [ Kevin Buzzard (Jul 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459223):
One is to ask that `perp` takes as an input not the *sets* `A` and `A'` but *proofs* `HA : line A` and `HA' : line A`

#### [ Kevin Buzzard (Jul 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459263):
(it would also need `A` and `A'` as inputs but they can be guessed from `HA` and `HA'`, so you can put them in squiggly brackets `{}` like I did above)

#### [ Kevin Buzzard (Jul 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459266):
and the other way is that you use type class inference.

#### [ Johan Commelin (Jul 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459274):
I would say that type class inference feels more natural, but sometimes comes with unexpected challenges of its own. (I'm sure Kevin can tell you more about that (-; ....)

#### [ Kevin Buzzard (Jul 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459275):
Then your function looks like `def perpx (x : point) (A A' : set point) [HLA : line A] [HLA' : line A'] (HxA : x ∈ A) (HxA' : x ∈ A') := ...` or even `def perpx (x : point) (A A' : set point) [line A] [line A'] (HxA : x ∈ A) (HxA' : x ∈ A') := ...`, and the proofs that `A` and `A'` are lines are supplied not by you but by the type class inference machine.

#### [ Johan Commelin (Jul 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459333):
And you would have to tell Lean that `l a b` is a line by adding an instance for it to the type class system.

#### [ Johan Commelin (Jul 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459334):
(If I inferred correctly that `l a b` is the line through points `a` and `b`.)

#### [ Kevin Buzzard (Jul 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459335):
Right: if you do it with type class inference then you change some of your `theorem`s and `definitions` to `instance`s, which adds them into the system.

#### [ Kevin Buzzard (Jul 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459376):
and you change your definition of `line` into a `class`

#### [ Kevin Buzzard (Jul 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459441):
Then you just feed the sets into your function and Lean checks in every case that it can construct a proof behind the scene that they're lines, typically by looking at the definition of `A` and noticing that it was defined using a function which it knows produces things which it can prove are lines.

#### [ Ali Sever (Jul 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459453):
I think this means I have a lot of tidying to do, and even more reading before that.

#### [ Johan Commelin (Jul 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459466):
But otoh, this creates a bit of a snowball effect. Because now you also want `point`s to be a type class, so that Lean can figure out itself that the intersection of two lines is a point.... (if the lines are not parallel)

#### [ Kevin Buzzard (Jul 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459504):
If Lean can't find a proof, then it gives up with a "failed to synthesize type class instance" error:

```lean
import data.complex.basic 

example : (1 : ℂ) < (2 : ℂ) := sorry 
```

->

```
failed to synthesize type class instance for
⊢ has_lt ℂ
```

#### [ Kevin Buzzard (Jul 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459572):
Of course `<` is just notation. If you type `#print notation <` you see it just means the function `has_lt.lt` and if you `#check @has_lt.lt` you find

```
has_lt.lt : Π {α : Type u_1} [c : has_lt α], α → α → Prop
```

which says "if the user asks me to make sense of `x<y` with `x y: α` then I'm going to ask the type class inference system to check for me that it makes sense to talk about terms of type alpha being less than each other " -- that's what the square brackets means.

#### [ Kevin Buzzard (Jul 28 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459676):
And lo and behold, in `data/real/basic.lean` we have `instance : has_lt ℝ := (some definition)` which is where Lean is told not just the definition of what it means for a real to be less than another real, but that this should be an "instance", which means "a definition but one which the type class inference system knows about".

#### [ Kevin Buzzard (Jul 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459694):
So `#check (1 : ℝ) < (2 : ℝ)` works fine, but `#check (1 : ℂ) < (2 : ℂ)` doesn't -- you get the "failed to synthesize type class instance" error.

#### [ Kevin Buzzard (Jul 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459738):
I guess `line A` will be a `Prop` so it sounds like an ideal candidate for type class inference.

#### [ Ali Sever (Jul 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459748):
So I can get rid of the defintion `perp a b c d` and use `perp (l a b) (l c d)`, which automatically knows that  `a ≠ b ∧ line (l a b)`.

#### [ Kevin Buzzard (Jul 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459889):
If you define something like `instance line_through_two_points_is_a_line (a b : point) (Hne : a \ne b) : is_line (line_through_two_points a b) := (proof it's a line)` then...hmm...this somehow doesn't look too good, because how will Lean guess that a isn't equal to b?

#### [ Johan Commelin (Jul 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459890):
Hmm, the `a \ne b` bit seems non-trivial.

#### [ Johan Commelin (Jul 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459892):
That might have to be supplied...

#### [ Kevin Buzzard (Jul 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459945):
I guess you'll be carrying round a proof of that anyway. But feeding it into the system might be hard. Why don't you adopt the other approach for now? Then at least you'll get the logic straight. Just feed in the proofs that everything is a line. That's what I did with schemes. I couldn't figure out how type class inference worked so several of my functions were taking proofs as inputs.

#### [ Ali Sever (Jul 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459947):
I mean `l a b` is only defined for `a \ne b`

#### [ Kevin Buzzard (Jul 28 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460105):
Lean doesn't like that kind of idea. You know `1/0=0` right?

#### [ Kevin Buzzard (Jul 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460118):
Only defining it for `a \ne b` is pretty much the same as carrying round a proof of this, in some sense.

#### [ Kevin Buzzard (Jul 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460192):
Why not go with `def perpx (x : point) {A A' : set point} (HLA : line A) (HLA' : line A') (HxA : x ∈ A) (HxA' : x ∈ A') :=
∀ u v, u ∈ A → v ∈ A' → R u x v`?

#### [ Kevin Buzzard (Jul 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460193):
We can worry about type class inference later.

#### [ Ali Sever (Jul 28 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460198):
If I adopt the other approach, won't it be harder in the future to switch to the more sophisticated method?

#### [ Kevin Buzzard (Jul 28 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460199):
I'm not sure that this is what an expert would do. But this is what I did for schemes, when I wasn't ready to launch into type class inference, and when I decided I wanted to change it was surprisingly easy.

#### [ Kevin Buzzard (Jul 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460241):
I just had to change a bunch of function inputs from `HU` to `U`

#### [ Mario Carneiro (Jul 28 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130465493):
> If you define something like instance line_through_two_points_is_a_line (a b : point) (Hne : a \ne b) : is_line (line_through_two_points a b) := (proof it's a line) then...hmm...this somehow doesn't look too good, because how will Lean guess that a isn't equal to b?

I often use partial functions for this. My general recommendation against partial functions notwithstanding, when you have typeclasses that depend on it this is usually a good reason to push the assumption into the arguments somehow, either by having an additional proof argument or using a more structured argument space (i.e. a subtype or sigma)

#### [ Kevin Buzzard (Jul 28 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130465623):
@**Ali Sever** so Mario is suggesting that you could use typeclasses. It might be easier to show you how to do all this on e.g. Monday if you're coming in, where I can explain face to face.

#### [ Ali Sever (Jul 28 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130472981):
Now that I have VS Code back up, I'll use your suggestion until Monday, and then we can do some CS.

#### [ Patrick Massot (Jul 29 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130493666):
Seriously, as far as choosing how to represent things, you could really use fifteen years of work gathered at http://geocoq.github.io/GeoCoq/ Definitions in Coq should be easy to read if you have the maths translation explained in the paper, eg https://hal.inria.fr/hal-00727117/file/adg2012_braun_narboux_postproc.pdf You would still have fun I think


{% endraw %}
