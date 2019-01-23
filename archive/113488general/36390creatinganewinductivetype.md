---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36390creatinganewinductivetype.html
---

## Stream: [general](index.html)
### Topic: [creating a new inductive type](36390creatinganewinductivetype.html)

---

#### [Kevin Buzzard (Mar 16 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123817890):
What happens to the underlying system when a new inductive type `X` is created in Lean? A new axiom seems to appear, namely the eliminator for the type -- `X.rec`. Is that right? A new axiom appears? Is that the only new axiom that appears, and all of the other stuff I see when I type `#print prefix X` is always deducible from `X.rec`? I see that occasionally other stuff is used, like `and` or `eq.rec` or propext. Is it possible to list exactly which functions are used when creating these new facts? I am trying to get to the bottom of the difference between equality and definitional equality and I think one main difference is these random axioms that seem to appear every time to create a new type.

#### [Kevin Buzzard (Mar 16 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123817958):
For example I think a+(b+c)=(a+b)+c for nats isn't a defeq, it's a theorem, and the reason seems to be that the proof uses induction on c, which uses nat.rec, which seems to be a way of proving that things are equal other than by definitional equality.

#### [Kevin Buzzard (Mar 16 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123817965):
Have I got all this sort-of straight?

#### [Simon Hudon (Mar 16 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818103):
Something seems to be missing

#### [Simon Hudon (Mar 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818155):
I think `a + succ b = succ (a + b)` is a definitional equality despite relying on rec

#### [Kevin Buzzard (Mar 17 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818821):
Why does this rely on rec?

#### [Kevin Buzzard (Mar 17 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818829):
Isn't it just the definition of addition?

#### [Kevin Buzzard (Mar 17 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818876):
oh

#### [Kevin Buzzard (Mar 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818886):
`#print nat.add._main` was rather more complex than I had expected

#### [Kevin Buzzard (Mar 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818959):
This is funny because the definition of `nat.add` in `core.lean` seems to be the standard one

#### [Kevin Buzzard (Mar 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818963):
Oh it somehow relies on everything either being zero or a succ

#### [Kevin Buzzard (Mar 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819077):
Somehow this is OK. We are defining `nat.add` using what might be called the equation compiler, and internally Lean has to make sense of this definition. Hmm. Maybe what is going on is that I don't understand the definition of defeq that Lean uses in practice.

#### [Kevin Buzzard (Mar 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819159):
The definition of `nat.add_main` looks like a mess to me, but `nat.add.equations._eqn_2` is the assertion that `a+succ b = succ(a+b)`. The proof isn't rfl though.

#### [Simon Hudon (Mar 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819164):
If you use `nat.rec f (succ n)` it looks to me like Lean treats it as definitionally equal to `f n`

#### [Kevin Buzzard (Mar 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819208):
Is this just some weirdness with nat though, because it's such a primitive object?

#### [Simon Hudon (Mar 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819230):
```quote
The proof isn't rfl though.
```

I don't think that equations get labelled as `rfl`

#### [Andrew Ashworth (Mar 17 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819316):
you'd think `rec` wouldn't be part of defeq but it's common in type theory settings to include delta reduction as part of it

#### [Kevin Buzzard (Mar 17 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819329):
I just rolled my own nat and nat.add and the same happens, it's not something specific to nat

#### [Kevin Buzzard (Mar 17 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819396):
Maybe this is iota reduction

#### [Kevin Buzzard (Mar 17 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819400):
Why did you guys choose such weird names for all these reductions?

#### [Andrew Ashworth (Mar 17 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819467):
most people regard alonzo church as a mathematician :)

#### [Kevin Buzzard (Mar 17 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819516):
OK so I am going to say that the reason a + succ b = succ (a+b) is a defeq despite relying on nat.rec is that the entire definition of add relies on nat.rec, and nonetheless they're defeq because of iota reduction. I knew what none of this stuff meant a few months ago though so if this isn't right then I hope someone lets me know.

#### [Simon Hudon (Mar 17 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819519):
Funny ... and they regard Turing as a sort of computer scientist. They pretty much did the same things

#### [Simon Hudon (Mar 17 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819539):
```quote
you'd think `rec` wouldn't be part of defeq but it's common in type theory settings to include delta reduction as part of it
```
Isn't delta reduction about definitions? If `rec` is a constant, it doesn't have a definition ... what am I missing?

#### [Kevin Buzzard (Mar 17 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819601):
According to Wikipedia Church was a mathematician and logician, so maybe he was being a logician at that point

#### [Simon Hudon (Mar 17 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819615):
Haha! Your honor is safe then!

#### [Kevin Buzzard (Mar 17 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819618):
I am only going on the Lean reference manual, but delta reduction seems to say that if I define something without using matching then I can just substitute and I'm still defeq.

#### [Simon Hudon (Mar 17 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819623):
Do mathematicians regard logicians in a similar way in which they regard philosophers?

#### [Kevin Buzzard (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819624):
Using matching is implicitly using what seems to be called iota reduction

#### [Simon Hudon (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819669):
That's what I'm going with as well

#### [Kevin Buzzard (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819674):
No, philosophers aren't doing maths at all. Logicians are doing stuff which some people would say was maths but most maths departments don't have any

#### [Andrew Ashworth (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819680):
```quote
```quote
you'd think `rec` wouldn't be part of defeq but it's common in type theory settings to include delta reduction as part of it
```
Isn't delta reduction about definitions? If `rec` is a constant, it doesn't have a definition ... what am I missing?
```
i'd have to check. i make no guarantees on whatever i remember about the lambda calculus

#### [Simon Hudon (Mar 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819693):
Let me compress the path for you: https://leanprover.github.io/reference/expressions.html#computation

#### [Kevin Buzzard (Mar 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819710):
I was suggesting that you can't use delta reduction to prove a + succ b = succ (a + b) because the definition of + depends on how the inductive type inputs were born

#### [Kevin Buzzard (Mar 17 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819773):
so I am not sure + is a "defined constant".

#### [Kevin Buzzard (Mar 17 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819781):
However + does sound a lot like a function defined by recursion on an inductive type

#### [Reid Barton (Mar 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819796):
`+` is a defined constant, its definition is going to be something like `nat.rec [...]` or possibly `lam a b, nat.rec [...]`

#### [Kevin Buzzard (Mar 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819797):
and a + succ b does sound a lot like the function "a +" being applied to an element given by an explicit constructor

#### [Kevin Buzzard (Mar 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819803):
Oh!

#### [Kevin Buzzard (Mar 17 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819850):
Right, this also makes sense.

#### [Reid Barton (Mar 17 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819859):
Then maybe (a) beta reduction(s) will apply to cancel the lambdas with the arguments, and then finally iota reduction will apply to `nat.rec`.

#### [Reid Barton (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819870):
(At least, this is my understanding without actually checking the definitions.)

#### [Kevin Buzzard (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819871):
What is the point of iota-reduction then?

#### [Simon Hudon (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819872):
That would be my thought as well. So the remaining question is: is iota reduction part of the def_eq definition?

#### [Kevin Buzzard (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819875):
`ι-reduction : When a function defined by recursion on an inductive type is applied to an element given by an explicit constructor, the result ι-reduces to the specified function value`

#### [Kevin Buzzard (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819877):
from the reference manual

#### [Reid Barton (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819920):
I think it's the rule that, after expanding the definition of `+` and then substituting the arguments, allows one to replace `nat.rec [...] (succ [...])` by something simpler.

#### [Kevin Buzzard (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819923):
Oh so it only explicitly applies to the recursor?

#### [Simon Hudon (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819924):
That sounds relevant doesn't it? I think here, "recursion" and "pattern matching" are synonymous

#### [Reid Barton (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819925):
And I think that has been paraphrased into a higher-level form in the lean documentation

#### [Reid Barton (Mar 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819928):
i.e. what Simon said.

#### [Reid Barton (Mar 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819938):
(But I've never encountered the phrase "iota reduction" outside the context of lean, so I am guessing a bit.)

#### [Kevin Buzzard (Mar 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819941):
At the end of the day it all adds up to the same thing -- a + succ b = succ (a + b) is defeq despite relying on nat.rec

#### [Kevin Buzzard (Mar 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819999):
Google led me to some pages about CIC:

#### [Kevin Buzzard (Mar 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820002):
" A specific conversion rule is associated to the inductive objects in the environment. We shall give later on (section 4.5.4) the precise rules but it just says that a destructor applied to an object built from a constructor behaves as expected. This reduction is called iota-reduction and is more precisely studied in [103, 117]."

#### [Kevin Buzzard (Mar 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820012):
This seems to say more explicitly that iota reduction is exactly how you prove that `blah.rec` is defeq to something else

#### [Kevin Buzzard (Mar 17 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820089):
On the other hand, the manual doesn't seem to give a definition of "what Lean uses for defeq" other than observing that (a) it's not the actual definition of defeq (proof: Lean's defeq isn't transitive) and (b) I think they're saying it's decidable (and actual defeq isn't).

#### [Kevin Buzzard (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820142):
So some of these reductions are from lambda calculus and iota reduction has just been tagged on afterwards as something coming from CIC it seems to me.

#### [Andrew Ashworth (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820143):
yes, lean and coq are CIC + extras

#### [Kevin Buzzard (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820144):
and we don't know what Lean is doing.

#### [Reid Barton (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820145):
Yes--specifically `blah.rec` applied to a constructor.
This will also go by names like "the elimination rule for the constructor"

#### [Simon Hudon (Mar 17 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820214):
```quote
Yes--specifically `blah.rec` applied to a constructor.
This will also go by names like "the elimination rule for the constructor"
```
I don't get what you're responding to

#### [Reid Barton (Mar 17 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820230):
To 

>  iota reduction is exactly how you prove that blah.rec is defeq to something else

#### [Andrew Ashworth (Mar 17 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820232):
the extras that are added to CIC make defeq not transitive

#### [Andrew Ashworth (Mar 17 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820296):
and it has something something to do with how you can go from an inductively defined proposition to a Type

#### [Andrew Ashworth (Mar 17 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820300):
but we don't want to do without because classical reasoning is so convenient

#### [Andrew Ashworth (Mar 17 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820304):
so little bits are stuck on here and there and we sort of politely ignore it

#### [Andrew Ashworth (Mar 17 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820344):
is my terrible understanding of the base theory

#### [Andrew Ashworth (Mar 17 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820351):
if you go completely constructive you get HoTT and you may then hop on voevodsky's bandwagon

#### [Kevin Buzzard (Mar 17 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820406):
```quote
the extras that are added to CIC make defeq not transitive
```
My reading of section 3.7 of the manual is that "true defeq" is transitive by definition, and "Lean defeq" is not.

#### [Andrew Ashworth (Mar 17 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820407):
yup, that's my understanding as well

#### [Kevin Buzzard (Mar 17 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820577):
So implicit in the reference manual is a description of two terms which have different weak head normal forms but which can be proved equal using rfl.

#### [Kevin Buzzard (Mar 17 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820591):
```
def R (x y : unit) := false
def accrec := @acc.rec unit R (λ_, unit) (λ _ a ih, ()) ()
example (h) : accrec h = accrec (acc.intro _ (λ y, acc.inv h)) := rfl
example (h) : accrec h = accrec (acc.intro _ (λ y, acc.inv h)) :=
begin
conv begin
to_rhs,
whnf,
end,
conv begin
to_lhs,
whnf,
end,
admit,
end
```

#### [Kevin Buzzard (Mar 17 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820594):
rfl works, but if you reduce both terms to weak head normal form then you see they are different.

#### [Kevin Buzzard (Mar 17 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820760):
So I am at a loss as to what Lean's definition of defeq is, but I understand it a lot better after this chat.

#### [Kevin Buzzard (Mar 17 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820768):
Looking back at the proof of associativity of nat.add it's interesting to actually try and point at exactly what stops the argument being rfl.

#### [Kevin Buzzard (Mar 17 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820807):
You prove it by induction on c; the zero case is rfl

#### [Kevin Buzzard (Mar 17 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820815):
and the inductive step is a bunch of rfls up to `a+(b+c)=(a+b)+c -> nat.succ (a+(b+c))=nat.succ((a+b)+c)`

#### [Kevin Buzzard (Mar 17 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820823):
but the inductive hypothesis isn't rfl, it's an assumption because we're using nat.rec

#### [Kevin Buzzard (Mar 17 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820867):
and in particular we can't deduce associativity from this iota-reduction thing because even though c is either zero or a succ, in the succ case we need more than a case split, we need induction.

#### [Kevin Buzzard (Mar 17 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820872):
It seems to me that it's this one point which stops associativity being defeq

#### [Kevin Buzzard (Mar 17 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820994):
On the other hand you can chase this back to congr_arg and hence to eq.subst and eq.rec

#### [Kevin Buzzard (Mar 17 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123821066):
Somehow this is not relevant.

#### [Reid Barton (Mar 17 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123821246):
More simply, you might consider the relationship between `(p.1, p.2)` and `p`

#### [Kevin Buzzard (Mar 17 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822140):
Also the coq page I was looking at seems to be saying that iota reduction says that a definition by cases can be reduced to its value for a given constructor when applied to a term constructed using this constructor.

#### [Kevin Buzzard (Mar 17 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822158):
This seems to be weaker than what it says in the Lean reference manual, which seems to imply that general definitions by recursion (like the definition of nat.add) can be iota-reduced.

#### [Kevin Buzzard (Mar 17 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822746):
So looking at what the manual says about inductive types, it seems that the answer to my original question is that what is added is the type, the constructors, and the recursor, and then everything else is worked out from this. And it also seems to say that iota reduction is fine for eliminating `X.rec`.

#### [Kevin Buzzard (Mar 17 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822757):
For example I think `(a,b).1=a` is rfl

#### [Kevin Buzzard (Mar 17 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822798):
but is @**Reid Barton** suggesting that `p=(p.1,p.2)` is not? It doesn't seem to be.

#### [Reid Barton (Mar 17 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822800):
Yes and yes (the latter is not definitionally equal)

#### [Kevin Buzzard (Mar 17 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822801):
Do you know Lean's definition of definitionally equal?

#### [Reid Barton (Mar 17 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822807):
Not really, no.

#### [Reid Barton (Mar 17 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123823460):
I just have some bits of type theory knowledge cobbled together from various sources.

#### [Mario Carneiro (Mar 17 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123825965):
Aah, you really should see this paper I'm working on

#### [Mario Carneiro (Mar 17 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123825973):
I basically lay all of this out in precise (too precise, probably) detail

