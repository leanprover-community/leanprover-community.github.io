---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93377divneg.html
---

## Stream: [general](index.html)
### Topic: ["div_neg"](93377divneg.html)

---


{% raw %}
#### [ Kenny Lau (Sep 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134617532):
algebra/field.lean L95:
```
lemma div_neg (a : α) (hb : b ≠ 0) : a / -b = -(a / b) :=
by rw [← division_ring.neg_div_neg_eq _ (neg_ne_zero.2 hb), neg_neg, neg_div]
```

#### [ Kenny Lau (Sep 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134617540):
but `div_neg_eq_neg_div` is the exact same

#### [ Kevin Buzzard (Sep 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652104):
it's not the same, it's over twice as hard to type

#### [ Sean Leather (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652157):
Especially if you're using a [typewriter](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/caching.20proofs/near/134214831). :printer:

#### [ Mario Carneiro (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652158):
I imagine I was annoyed with the lean core name and duplicated it with a new name

#### [ Kenny Lau (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652162):
then why don't you prove it just using that?

#### [ Mario Carneiro (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652165):
probably the proof is shorter too?

#### [ Kenny Lau (Sep 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652234):
I think you're misunderstanding me. See [this edit of mine](https://github.com/leanprover-community/mathlib/commit/6b2ee1dd45fedc0d04a4c9df76b3d0ce1ec084ed#diff-6bbbc7fb99ee6d3f77c06e4b7ad403a1L97).

#### [ Mario Carneiro (Sep 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652262):
No, I know exactly what you mean. I am saying the proof is shorter than the original proof

#### [ Mario Carneiro (Sep 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652353):
you've also revealed to me that your compile times change is doing more than just improving compile times :}

#### [ Kenny Lau (Sep 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652412):
that's not true. my term mode proof is faster than `rw`

#### [ Mario Carneiro (Sep 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652426):
the point is not to be significantly refactoring the proofs while you do it though

#### [ Kenny Lau (Sep 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652431):
but that would reduce the time by like at least 90%

#### [ Mario Carneiro (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652435):
because that brings in more controversial aspects of the work

#### [ Kenny Lau (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652439):
I don't see why proofs are relevant

#### [ Mario Carneiro (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652447):
you aren't making it easy for me to merge this PR

#### [ Kenny Lau (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652449):
also don't you like shorter proofs?

#### [ Mario Carneiro (Sep 26 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652517):
yes, that's why I want the original proof there

#### [ Kenny Lau (Sep 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652528):
because the original proof `by rw [← division_ring.neg_div_neg_eq _ (neg_ne_zero.2 hb), neg_neg, neg_div]` is longer and slower?

#### [ Mario Carneiro (Sep 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652530):
I expect that the core theorem will disappear shortly, and I don't want to forget that it's already been minimized

#### [ Mario Carneiro (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652591):
Don't sweat the small stuff. I'm hoping that your work is focusing on the actual worst offenders

#### [ Mario Carneiro (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652604):
Did you test your proofs for actual time saved?

#### [ Kenny Lau (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652606):
of course

#### [ Mario Carneiro (Sep 26 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652621):
what method are you using?

#### [ Kenny Lau (Sep 26 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652623):
`set_option profiler true`

#### [ Mario Carneiro (Sep 26 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652671):
You should focus on proofs that take >1s to compile

#### [ Kenny Lau (Sep 26 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652679):
every `simp` proof takes >1s to compile

#### [ Mario Carneiro (Sep 26 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652720):
this is not my experience

#### [ Kevin Buzzard (Sep 26 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652779):
Maybe Kenny has a slower machine, which I guess in this context is in some weird sense quite helpful

#### [ Kevin Buzzard (Sep 26 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652792):
I remember Kenny complaining that some proof took 7 seconds to compile, and I tried it on my 1 year old laptop and it took 3 seconds

#### [ Kenny Lau (Sep 26 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652810):
[2018-09-26-5.png](/user_uploads/3121/OtOLeoaVolATyey-qF9KFNpx/2018-09-26-5.png)

#### [ Kevin Buzzard (Sep 26 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652815):
Kenny -- Mario is right. Attack the stuff which takes > 1 second for you. Don't worry about div_neg being 0.04 or 0.03

#### [ Kevin Buzzard (Sep 26 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652876):
Your screenshot is eye-opening by the way

#### [ Mario Carneiro (Sep 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652908):
it's also not good news at all

#### [ Mario Carneiro (Sep 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652913):
we may need to rewrite simp

#### [ Kenny Lau (Sep 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652921):
so do I have the green light?

#### [ Mario Carneiro (Sep 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652999):
I am still a bit uncomfortable about this, like we should retain the original proofs

#### [ Mario Carneiro (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653015):
this is of course the same story as with `tidy`

#### [ Kenny Lau (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653018):
```quote
I expect that the core theorem will disappear shortly, and I don't want to forget that it's already been minimized
```
are you referring to Lean 4?

#### [ Mario Carneiro (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653024):
yes, basically

#### [ Kenny Lau (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653030):
but you can't copy the files to Lean 4 anyway

#### [ Kenny Lau (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653035):
why bother that this particular proof can't be copied to Lean 4

#### [ Mario Carneiro (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653047):
kenny, focus

#### [ Kenny Lau (Sep 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653097):
ok ok

#### [ Mario Carneiro (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653107):
suffice it to say that you have the green light to do changes expressly for the purpose of improving compile times by e.g. replacing `simp` with `simp only` or `rw`

#### [ Mario Carneiro (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653111):
If you want to do something else, put it in a different PR

#### [ Kevin Buzzard (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653113):
If you want to do two different things Kenny then you could do them in two different branches

#### [ Kenny Lau (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653114):
ok

#### [ Kenny Lau (Sep 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653168):
so I don't have the green light to change:
```lean
@[simp] lemma coe_singleton (a : α) : ↑(ι a) = ({a} : set α) :=
by simp [set.ext_iff]
```
to:
```lean
@[simp] lemma coe_singleton (a : α) : ↑(ι a) = ({a} : set α) :=
rfl
```
?

#### [ Kenny Lau (Sep 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653179):
just to confirm

#### [ Mario Carneiro (Sep 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653180):
I would accept that if it's actually much faster

#### [ Kenny Lau (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653190):
of course it's much faster

#### [ Mario Carneiro (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653193):
`refl` is also among the things you can replace `simp` with

#### [ Mario Carneiro (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653195):
definitional unfolding is not always fast

#### [ Mario Carneiro (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653199):
hint: `10 + 10 = 20 := rfl`

#### [ Kenny Lau (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653202):
alright

#### [ Kenny Lau (Sep 26 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653257):
[2018-09-26-6.png](/user_uploads/3121/12xknWSPMLmfvRnGOp0UDVj4/2018-09-26-6.png)

#### [ Mario Carneiro (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653280):
I would still prefer `simp` over `simp only` if it is not a significant improvement

#### [ Kenny Lau (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653292):
is 3 orders of magnitude significant enough?

#### [ Scott Morrison (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653294):
I wonder if it is worth writing a hole command for generating `simp only` tactics.

#### [ Mario Carneiro (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653298):
like if you can't improve by more than .1s then leave it

#### [ Mario Carneiro (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653303):
a hole command sounds like a great idea

#### [ Kenny Lau (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653304):
maybe you missed the unit

#### [ Mario Carneiro (Sep 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653356):
no, I saw, that's a phenomenal improvement and I don't doubt that you will find many such things

#### [ Scott Morrison (Sep 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653378):
or even just a wrapper for simp, that calls `simp`, looks at the result, and works out automatically a `simp only` command that will work, and outputs that as a trace message.

#### [ Kenny Lau (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653386):
```quote
or even just a wrapper for simp, that calls `simp`, looks at the result, and works out automatically a `simp only` command that will work, and outputs that as a trace message.
```
that's exaclty what's in my mind

#### [ Scott Morrison (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653392):
... and this all emphasises how much we need multiple levels of caching.

#### [ Kenny Lau (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653410):
I think caching is a bad idea

#### [ Mario Carneiro (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653420):
I think caching of the sort scott is talking about is a very good idea

#### [ Kenny Lau (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653438):
in terms of the trust of the correctness

#### [ Mario Carneiro (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653484):
?

#### [ Mario Carneiro (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653503):
a proof is a proof

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653515):
never mind

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653525):
also what Scott said is what I'm doing manually

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653537):
look at the output for `trace.simplify.rewrite` and write a correspondingly `simp only` or `rw`

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653539):
(or term mode proof)

#### [ Mario Carneiro (Sep 26 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653561):
Unfortunately I don't know if tactics can capture trace output

#### [ Kevin Buzzard (Sep 26 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653630):
```quote
```quote
or even just a wrapper for simp, that calls `simp`, looks at the result, and works out automatically a `simp only` command that will work, and outputs that as a trace message.
```
that's exaclty what's in my mind
```
Kenny why don't you look at how Scott got `tidy` to print out its proofs, and then write code which does what you're doing, or at least does part of it? It will make you a more powerful Lean programmer. Chris might be able to help you with this when you're back in London -- he knows some tactic stuff now.

#### [ Kenny Lau (Sep 26 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653667):
or you all can help me with my project so we can have a faster build sooner

#### [ Mario Carneiro (Sep 26 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653688):
maybe we can look at the proof term that is generated by `simp` to work out those lemmas

#### [ Kevin Buzzard (Sep 26 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653699):
I am not motivated to have a faster build because things build fast for me already :-/

#### [ Mario Carneiro (Sep 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653799):
do holes work inside interactive tactic mode?

#### [ Mario Carneiro (Sep 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653810):
like `begin {! !} end`

#### [ Kenny Lau (Sep 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653817):
```quote
I am not motivated to have a faster build because things build fast for me already :-/
```
remember the problems with mathlib that we talked about?

#### [ Johan Commelin (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653910):
```quote
do holes work inside interactive tactic mode?
```
It seems that they do.

#### [ Mario Carneiro (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653928):
there is a reason I recommended you focus on the worst offenders - not only is it a huge project to change every proof, but I'm not even sure that's a good idea

#### [ Mario Carneiro (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653953):
you will get most of the benefits with just working on 2 or 3 files in mathlib

#### [ Kenny Lau (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653956):
I understand

#### [ Kenny Lau (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653973):
do you know which 3 files those are?

#### [ Mario Carneiro (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654013):
no

#### [ Kenny Lau (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654023):
do you know how I can find out?

#### [ Mario Carneiro (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654028):
I'm hoping that you will find a way to use the profiler for this

#### [ Mario Carneiro (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654033):
and let me know what you do

#### [ Kenny Lau (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654071):
ok

#### [ Mario Carneiro (Sep 26 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654378):
kenny, have you found that `simp only` is faster or slower than `rw` when you have to give a list of rewrites?

#### [ Kenny Lau (Sep 26 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654429):
I think they're roughly the same

#### [ Mario Carneiro (Sep 26 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654607):
Also, if you come up with proof shortenings while you are doing this (and I expect you will), you should hold on to them and PR them separately. I'm not opposed to this, but the review is different

#### [ Kenny Lau (Oct 02 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019586):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.22div_neg.22/near/134653199
> Mario Carneiro: definitional unfolding is not always fast
> Mario Carneiro: hint: `10 + 10 = 20 := rfl`

[10+10=20](/user_uploads/3121/A-LPlvuMKGXmQM8fHPvu_LW8/2018-10-02.png)

#### [ Mario Carneiro (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019643):
it was a hint, not an answer

#### [ Kenny Lau (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019644):
I see

#### [ Chris Hughes (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019654):
Try `10000 * 10000`

#### [ Mario Carneiro (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019656):
obviously you should put a silly number of zeroes in random places, maybe a `^` for good measure

#### [ Kenny Lau (Oct 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020222):
I don't really think that's a good argument though. `10000 * 10000` would be a lot of layers of definitional unfolding, so what you really mean is that if you have a lot of layers of definitional unfolding then it would be slow. Of course, any fast process repeated 100000000 times will take a long time. That doesn't mean definitional unfolding itself is slow.

#### [ Mario Carneiro (Oct 02 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020288):
Okay, how about `nat.prime 5 := dec_trivial`?

#### [ Kenny Lau (Oct 02 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020346):
what do I need to import?

#### [ Mario Carneiro (Oct 02 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020415):
`data.nat.prime`

#### [ Kenny Lau (Oct 02 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020432):
and I also need an instance?

#### [ Mario Carneiro (Oct 02 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020435):
the default one

#### [ Kenny Lau (Oct 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020495):
well there are two of them

#### [ Mario Carneiro (Oct 02 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020524):
Actually the most convincing example is probably `ring2`. I wrote the same tactic twice, once via computational reflection, aka kernel evaluation, and once using the VM to produce proof terms. It wasn't significantly slower, but it was measurable, like 50% worse

#### [ Kenny Lau (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020551):
which one was worse?

#### [ Mario Carneiro (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020563):
`ring2` of course

#### [ Mario Carneiro (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020570):
Otherwise it would be called `ring` now

#### [ Kenny Lau (Oct 02 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135048800):
not every term mode proof is fast

#### [ Kenny Lau (Oct 02 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135048803):
but every fast proof is in term mode

#### [ Kenny Lau (Oct 02 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135048809):
every proof that gets below 10 ms is done in term mode

#### [ Kenny Lau (Oct 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049451):
[case in point:](/user_uploads/3121/zqTn_dKHUTIKI1ujiLPrhKOR/2018-10-02-1.png)

#### [ Kenny Lau (Oct 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049466):
ok bad example, `rfl` is a special term

#### [ Kenny Lau (Oct 02 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049507):
[case in point:](/user_uploads/3121/8XdY6dp5U5mlaOPN-YFCkls_/2018-10-02-4.png)

#### [ Johan Commelin (Oct 02 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049582):
"All fast proofs are alike; each slow proof is slow in its own way" — Λeo Tolstoy

#### [ Kenny Lau (Oct 02 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049634):
is that a lambda?

#### [ Kevin Buzzard (Oct 02 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049689):
Do you get big speed-up if you tell Lean what the missing terms are instead of making it guess them?

#### [ Kenny Lau (Oct 02 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049731):
depends on the term

#### [ Kenny Lau (Oct 02 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049733):
mostly no.

#### [ Mario Carneiro (Oct 02 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050403):
You get a really big speedup if you just write olean files by hand

#### [ Chris Hughes (Oct 02 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050694):
It's not really a long term solution. The long term solution is to have an option to import files without proof checking, so that editing is easier. I've been using a ton of `linarith` when writing my stuff on exp, and it's great that when you have a goal like this, you don't have to think about it, and that's the way it should be, and I think it's hard to sell Lean if you say using these tactics is discouraged because they're slow.

#### [ Johan Commelin (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050710):
Right, so we are back to the caching that we have been talking about.

#### [ Johan Commelin (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050762):
We need readable (editable?) proofs. But we also need speed.

#### [ Johan Commelin (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050772):
So we need several layers of caches, I think.

#### [ Mario Carneiro (Oct 02 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050838):
This is one of the reasons I like metamath - there was a very clear middle layer that is easy to verify quickly and compiled-to by higher level IDEs

#### [ Mario Carneiro (Oct 02 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050849):
storing only proof scripts forces their reevaluation on a regular basis

#### [ Mario Carneiro (Oct 02 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050909):
In principle this should be the olean file, but the current design has these being far too ephemeral

#### [ Mario Carneiro (Oct 02 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051025):
Does anyone know how many definitions there are in mathlib? If we were to aim for 5 minutes compilation, how much time does that give each definition on average?

#### [ Mario Carneiro (Oct 02 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051061):
(this ignores multithreading, but I'm not sure if travis is even multithreaded)

#### [ Johan Commelin (Oct 02 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051179):
I don't really care about the Travis compile time. I care about the compile time on my laptop, and that of Chris, and yours.

#### [ Johan Commelin (Oct 02 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051188):
For me it currently takes more than an hour...

#### [ Johan Commelin (Oct 02 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051239):
Concerning number of statements: I think this was somewhere in the statistics of Patrick.

#### [ Chris Hughes (Oct 02 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051275):
I don't even care about that. I care about the 10 minute - 1 hour wait for the yellow bar to move whenever I change some library file with quite a few dependencies.

#### [ Johan Commelin (Oct 02 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051385):
```
for i in def lemma theorem; do git grep "^$i" | wc -l; done
1301
2511
3942
```

#### [ Johan Commelin (Oct 02 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051432):
That's a rough approximation, because it doesn't match simp-lemmas etc

#### [ Mario Carneiro (Oct 02 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051491):
that is 40ms each, sounds tough

#### [ Johan Commelin (Oct 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051527):
```
for i in def lemma theorem "\\@\\["; do git grep "^$i" | wc -l; done
1301
2511
3942
3457
```

#### [ Mario Carneiro (Oct 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051565):
There could be some overcounting there though

#### [ Johan Commelin (Oct 02 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051615):
Right. To do this properly one should use one of the statistics tools

#### [ Johan Commelin (Oct 02 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051628):
But I don't care if I have to compile for 8 hours, once a month.

#### [ Johan Commelin (Oct 02 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051634):
I'll just leave my laptop running overnight.

#### [ Johan Commelin (Oct 02 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051641):
The rest of the month, some sort of intermediate layer should be sufficient.

#### [ Johan Commelin (Oct 02 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051718):
But I guess it doesn't make sense to discuss this all over again. I hope Lean 4 will bring some nice features. The issue about memoisation of tactic blocks sounded good. I hope something like that will be realised.

#### [ Mario Carneiro (Oct 02 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051826):
What about "unsafe caching"? In the sense, if A changes and you are modifying C and B is in the dependency path, then A is updated and rechecked, B remains untouched and all its theorems continue to hold in the old A environment, and C uses both, with conflicts resolved in favor of the new A environment

#### [ Mario Carneiro (Oct 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051870):
This is not sound, but it would be pretty hard to notice the inconsistency unless you are specifically trying to foil it

#### [ Mario Carneiro (Oct 02 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051923):
And it would only be for editor interaction anyway

#### [ Johan Commelin (Oct 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051971):
Right... it is completely fine if the stuff is opportunistic

#### [ Johan Commelin (Oct 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052005):
If it trips on some edge case you just flag it to rebuild some caches

#### [ Johan Commelin (Oct 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052022):
But again... this is not something we can currently do, right?

#### [ Mario Carneiro (Oct 02 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052070):
no, this requires lean support as does any caching modification

#### [ Johan Commelin (Oct 02 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052336):
I should say that even "readable term-mode proofs" (what most people here would call readable) are really bad for showing to newcomers. There was a PhD student who showed quite a bit of interest over lunch. He asked me if I could show him some files on ring theory. So we browsed mathlib a bit. He really liked the interactive proofs. But as soon as a term-mode proof was more than a simple lambda-expression he was completely lost and disappointed.

#### [ Johan Commelin (Oct 02 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052346):
Especially some 15-line term-mode proofs that were impossible to explain

#### [ Andrew Ashworth (Oct 02 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052510):
What do you think of TPIL's term mode style?

#### [ Johan Commelin (Oct 02 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052669):
Can you point me to a specific page?

#### [ Johan Commelin (Oct 02 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052770):
@**Andrew Ashworth** Do you mean something like p34?

#### [ Johan Commelin (Oct 02 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052778):
I would say that is readable, but it is also extremely long-winded for a really simple goal.

#### [ Johan Commelin (Oct 02 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052886):
It helps that the write a lot of types and `show` that are not strictly necessary.

#### [ Andrew Ashworth (Oct 02 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052918):
yes, in general, TPIL's style of using lots of explicit `show`, `have`, and `calc` mode

#### [ Johan Commelin (Oct 02 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052991):
But what is the benefit over tactic mode?

#### [ Johan Commelin (Oct 02 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053034):
Those proofs have a pretty straight forward analogue in tactic mode. With the benefit that you get interaction, and you can see how the proof state changes.

#### [ Andrew Ashworth (Oct 02 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053048):
hmm, well, 1) you may read it without using the Lean editor, 2) organizing proofs around key `have` statements instead of long chains of `apply` or `rewrite` is good practice

#### [ Johan Commelin (Oct 02 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053097):
But both of those can be done in tactic mode

#### [ Andrew Ashworth (Oct 02 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053159):
sure! and that's great for tactic mode. also I don't want to deny using tactics and advocate for 100% terms

#### [ Johan Commelin (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053221):
```
git grep "^begin" | wc -l
800
```

#### [ Johan Commelin (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053238):
It is clear that tactic mode proofs are a minority in mathlib

#### [ Johan Commelin (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053247):
And it is not clear to me why.

#### [ Andrew Ashworth (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053264):
Just like in Coq most people write tactic mode proofs, but they could also write them in C-Zar style

#### [ Andrew Ashworth (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053266):
https://www-verimag.imag.fr/~corbinea/ftp/programs/sqrt2.v

#### [ Andrew Ashworth (Oct 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053275):
and I prefer to read those kinds of proofs

#### [ Johan Commelin (Oct 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053306):
Sure, there are expensive tactics... we can try to use those for proof discovery, and remove them later (or have good caching :stuck_out_tongue_wink:). But just a bunch of `have` and `show`, `convert`, `cases`, `split`, etc...

#### [ Johan Commelin (Oct 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053323):
That shouldn't be much more expensive then term mode, I hope.

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053366):
it's really not about tactics, I think, just that tactics encourage what I think is a kind of sloppy proof writing

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053378):
with not much care about reading and understanding the proof later

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053380):
of course you can do the same thing in term mode

#### [ Johan Commelin (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053383):
Huh?

#### [ Johan Commelin (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053397):
With every term mode proof I have trouble "reading and understanding the proof later"

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053398):
I think I jokingly complained about this many months ago to Mario when I was going through Mathlib's analysis section

#### [ Johan Commelin (Oct 02 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053404):
It is the tactic proofs that I find easy to follow

#### [ Johan Commelin (Oct 02 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053415):
Btw, link is broken over here.

#### [ Andrew Ashworth (Oct 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053511):
https://gist.github.com/alashworth/0f1446b5b322427cfd42a6ccb5a9df83

#### [ Johan Commelin (Oct 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053534):
Maybe tactic mode makes me sloppy. But I'm sure that I can come back and pretty quickly edit some proof or make little changes. With term mode I just have to start all over again.

#### [ Johan Commelin (Oct 02 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053588):
Those proofs in that link are very readable!

#### [ Andrew Ashworth (Oct 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053659):
yes, I imagine anybody could understand them, even if they don't know any Coq

#### [ Johan Commelin (Oct 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053773):
In Orsay we spoke about a VScode button that would transform a term-mode proof into a tactic block. Just by silly regex transformations you could get pretty far...

#### [ Johan Commelin (Oct 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053807):
I haven't figured out how to contribute to the VScode extensions, but I think it would be really helpful for me...

#### [ Andrew Ashworth (Oct 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053919):
if people wrote their term mode proofs with care, in the style of TPIL or the gist I linked, then you wouldn't need to step through it with Lean :) I guess that's the point I wanted to make

#### [ Andrew Ashworth (Oct 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053942):
I agree with your friend that most proofs in mathlib, term mode or tactic mode, are impossible to understand without taking them apart by hand...

#### [ Andrew Ashworth (Oct 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054129):
but as it turns out the concise style seems to be popular no matter the language. In Coq nobody uses C-Zar, but instead SSReflect, which is famously terse

#### [ Andrew Ashworth (Oct 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054137):
(for math anyway)

#### [ Johan Commelin (Oct 02 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054197):
hmmm... is it also faster?

#### [ Andrew Ashworth (Oct 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054335):
I don't know enough about SSReflect to compare the two

#### [ Andrew Ashworth (Oct 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054356):
Actually I found out about Lean after struggling with SSReflect in an IRC chatroom... and then I switched

#### [ Johan Commelin (Oct 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054371):
Lol

#### [ Kenny Lau (Oct 02 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135055543):
```quote
It is clear that tactic mode proofs are a minority in mathlib
```
maybe you forgot `by`

#### [ Kenny Lau (Oct 02 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135055706):
```quote
that is 40ms each, sounds tough
```
20% of the theorems take 80% of the time to compile (Pareto principle)

#### [ Kenny Lau (Oct 02 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135055715):
many theorems take less than 40ms to compile

#### [ Kevin Buzzard (Oct 03 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135086345):
Everyone seems to have different opinions about readability. People like Larry Paulson in Cambridge seem to believe it is a fundamental principle which should be adhered to at all costs. I had always assumed that Mario's attitude was "hang readability, just get it done in as few characters as possible" -- but then later on I realised that Mario was writing code which he could actually read, it was just that I couldn't read it. No doubt this will come with practice.

My opinion is that actually I don't think anyone reads Bourbaki, people read books which are written to be read so that people could learn the material, and Bourbaki was written to be foundational. There is one Bourbaki that people read -- the stuff on algebraic groups -- because it's a really good refrence for e.g. all the facts and figures for the exceptional groups like E_8, G_2 etc -- but in general my experience is that people only read Bourbaki if they're desperate or if they for some reason want to see the theory built up from scratch (and most mathematicians don't). I've come to the conclusion that when it comes to mathlib I don't care whether the proofs are readable or not, because that is not the point of mathlib. I have occasionally in the past written instructive proofs, and actually this term I will be writing a whole bunch of instructive proofs of basic mathematics, with Lean tactic proofs littered with comments. But that's because I'm concentrating on teaching. In my mind the main criteria for a mathlib proof should be "is it easily maintainable?". I am hoping that compilation times are something which can be solved by technology (code to make it so I only have to compile once a month, speed-ups, better hardware) in the long term.


{% endraw %}
