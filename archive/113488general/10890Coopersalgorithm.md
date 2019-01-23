---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10890Coopersalgorithm.html
---

## Stream: [general](index.html)
### Topic: [Cooper's algorithm](10890Coopersalgorithm.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 20 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126812643):
I've implemented Cooper's algorithm for linear integer arithmetic as a Lean tactic (https://github.com/skbaek/qelim). It's still quite limited, but it should work for simple goals.
* `cooper` is the completely verified tactic that is proof-producing all the way. Unfortunately, it is unusably slow.
* `cooper_vm` is the partially verified tactic whose first step (replacing the original goal with the new quantifier-eliminated goal) is proof-producing. The second step (evaluating the new goal to a tautology) is trusted.
* The tactics assume sentential goals, so you'll have to generalize variables and hypotheses before calling it.
* The implementation is based on Tobias Nipkow's paper (http://www21.in.tum.de/~nipkow/pubs/jar10.pdf).
* I've added a few test cases (qelim/lia/cooper/tests.lean) from John Harrison's book.
* Right now I'm having trouble making absolute paths work. All references to mathlib are relative.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126812751):
Hey! Seul's here! And he brings gifts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 20 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126813048):
I notice that your `atom` type uses `int`. This will kill your efficiency, if you are doing kernel evaluation. You should use `znum` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126813108):
Re: paths, do you have a `leanpkg.toml` file in your project? I don't see one, but it's important for making file resolution work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 20 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126813252):
For others who may not be aware: this is basically the `omega` tactic everyone's been talking about, although Cooper's is a slightly different algorithm for the same problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 20 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126817604):
Thanks for releasing this! It looks like it was quite a substantial effort, with the first commit being a few months ago. I definitely want to spend some time looking over it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 20 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844501):
```quote
I notice that your `atom` type uses `int`. This will kill your efficiency, if you are doing kernel evaluation. You should use `znum` instead
```
Thanks for the suggestion! Maybe this is what's making `cooper` so much slower than `cooper_vm`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 20 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844596):
```quote
Re: paths, do you have a `leanpkg.toml` file in your project? I don't see one, but it's important for making file resolution work
```
I'm actually having problems with mathlib itself—when I clone mathlib it won't work as is, because Lean doesn't like its absolute paths for some reason. It works after I manually relativize them.  This is strange because mathlib does have a `leanpkg.toml` file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 20 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844646):
You want to make mathlib a dependency for your project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 20 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844687):
if you use leanpkg and add mathlib as a dependency then it should sort out everything for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 20 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844697):
see section 1.4.3 of the reference manual

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 20 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844698):
https://leanprover.github.io/reference/using_lean.html#using-the-package-manager

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 20 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844748):
I am really grateful for your work by the way, and maybe @**Patrick Massot** will be even more grateful -- Patrick maybe this solves some of your nat woes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126864044):
I hope it can help me. I need to find some time to try it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126864048):
Maybe I'm not trying very hard to find this time because I'm afraid I'll be disappointed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865859):
Any hint about how to actually import that cooper thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865899):
I tried `leanpkg add skbaek/qelim` and then import

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865902):
I tried adding a `leanpkg.toml` to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865905):
But `import lia.cooper.main` doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866474):
@**Mario Carneiro** Did you manage to import this tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866481):
I haven't attempted it, no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866527):
You could just copy the files into your project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866593):
Then all mathlib imports fail...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866594):
I guess we need to wait a bit more until this can be tested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 28 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127217640):
I figured out what was wrong and added a .toml file. Now you can install and use the repo using leanpkg.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127218789):
This is cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127218832):
Is it planned to merge this into mathlib? Or will it remain a separate lib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127218837):
I'm not sure what the planning is in general: a monolithic lib, or distributed libs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127219807):
@**Seul Baek**  Do you have any example of use? I can now import the lib, but haven't yet managed to proved anything using Cooper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220285):
actually I can prove stuff about integers (that `ring` also proves),  so maybe I misunderstood the scope of this tactic. I thought it would work on natural numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220332):
With nat I always get `type error at eval_expr, argument has type  ℕ but is expected to have type  ℤ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220429):
The core tactic is designed to work on `int`. There are some missing preprocessing steps to prove natural number theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220432):
Of course a nat quantifier is the same as an int quantifier with the additional assumption 0 <= n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220439):
What do you get in addition to `ring` then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220443):
I think Seul's tactic is still more of a backend thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220482):
it needs a front end to generalize and revert quantifiers, and convert nats to ints

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220487):
Do you know whether he's working on this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220488):
`ring` will not be able to prove that `\forall n : int, n <= 0 \/ n >= 1` for example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220495):
Or `3 | n -> 5 | n -> 15 | n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220537):
or `3 | n -> n > 0 -> n*n - n > 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220544):
oh wait actually that last one might not work because of the square

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220546):
This sounds pretty nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220587):
but more importantly, it allows full quantifier alternation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220588):
But Lean doesn't let me state the divisibility stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220590):
type `3 \| n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220601):
Oh, Johan will like this unicode trickery

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220609):
```lean
example  : ∀ (n : ℤ), (3 ∣ n) → (5 ∣ n) → (15 ∣ n) :=
by cooper
```
doesn't work though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221407):
looking at the code, it's pretty sparse on extended syntax

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221412):
you have to use exists ~~and forall~~ and times and le

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221417):
I'm not even sure equality is supported

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221426):
so you would have to write `\ex k, 3 * k <= n /\ n <= 3 * k` instead of `3 | n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221537):
I thought everything is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221538):
@**Johan Commelin** I'm not sure what'd be the best way to integrate this to other libraries in the long term.  It'll stay separate for the short term for convenience of further development.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221553):
actually I take it back, forall is also not supported

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221555):
you have to use negation and exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 28 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221653):
@**Patrick Massot**  It should definitely be possible to write a preprocessor for nat, although I'm not working on it at the moment. I'm trying to first replace `int` with `znum` to improve efficiency.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221777):
@**Mario Carneiro** forall and equality are indirectly supported by the rewriting step before calling the main quantifier elimination tactic. E.g., `cooper_vm` works for `forall (x: int), exists (y : int), x = 1 + y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221833):
oh, I see it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221835):
I guess you should add the definition of dvd in that list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 28 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221944):
You mean the list of indirectly supported relations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221945):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221947):
as a simp lemma in the preprocessing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221959):
something like `a | b <-> ∃ c, b = a * c`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221977):
surprisingly not stated as a theorem that I can see, but easy to prove by refl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Seul Baek (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127222107):
Yes, I think it should be possible to do this even more directly (w/o preprocessing), since the internal syntax already includes dvd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 29 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127241177):
Thanks Seul and Mario. I'll wait a bit more then (a tactic handling ℕ crazyness is what I really need).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246452):
```quote
surprisingly not stated as a theorem that I can see, but easy to prove by refl
```
Hey wait a minute! I asked for the name of a theorem recently (if a structure is made with a : A and b : B then  (structure.mk a b).a = a) and you said "oh that's true by refl so it doesn't have a name"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246465):
What's the algorithm for determining whether an equality whose proofs is rfl gets blessed with a name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246748):
It doesn't usually matter, Seul is writing a tactic so he needs to have names for his automation. It's fine even if he just declares a local theorem with a particular statement he can rely on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246755):
For example there are lots of theorems in `tactic.ring` that are like this - they have very particular statements to make it easy for the automation, but no one would ever use those theorems otherwise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246826):
But the other day I said "I want to do this rewrite and it's refl but I want to know the name anyway" and your response was "use show"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246833):
and I bought this at the time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246834):
but this response stinks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246876):
But it's also common for definitional expansions to have a name, particularly when the definition is hidden in a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246878):
because I have to keep changing things to definitionally equal things in my head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246879):
and I am sitting at a computer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246885):
for example `finset.subset_iff`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246889):
can I do targetted dsimp?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246896):
This is a new thread. Hang on

