---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84549idlytryingsoftwarefoundations.html
---

## Stream: [general](index.html)
### Topic: [idly trying software foundations](84549idlytryingsoftwarefoundations.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286568):
I am working through software foundations. I'm finding the first book relatively straightforward, which is a relief. I was trying to do the exercises in a golf-like way. Why doesn't this work:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286609):
```
inductive  ev : nat →  Prop
| ev_0 : ev 0
| ev_SS : ∀ n : nat, ev n → ev (n+2)
open ev
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286615):
`theorem  ev_plus4 : ∀ n, ev n → ev (n +  4) :=  λ _ _,ev_SS _ (ev_SS _ _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286618):
I thought there was every chance :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286636):
but I get

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286637):
```
don't know how to synthesize placeholder
context:
_x : ℕ,
_x : ev _x
⊢ ev _x 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286973):
what is software foundations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287015):
a book on the web

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287019):
https://softwarefoundations.cis.upenn.edu/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287026):
They have exercises like this:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287030):
You need to plug in the assumption for `ev n` somewhere.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287035):
```
definition  double (n : ℕ) := n + n
theorem  ev_double (n : ℕ) : ev (double n) := nat.rec_on n ev_0
(λ n H, have (n+1)+(n+1)=n+n+2,by simp,show ev((n+1)+(n+1)),by {rw this;exact ev_SS _ H})
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287047):
I wanted the elaborator to guess where. I have it as an underscore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 27 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287102):
The underscores won't find it because it is not determined by unification.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287111):
I know that `theorem  ev_plus4 : ∀ n, ev n → ev (n +  4) :=  λ _ H,ev_SS _ (ev_SS _ H)` works but I...basically I am trying to get a feeling for what I can get away with with underscores

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287122):
it's the same reason ` #check  λ n : nat, (rfl : _ +  4  = (_ +  2) +  2) ` fails, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287124):
(obviously it's `n`!!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287129):
It could also be 0, or 1, or...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287133):
Or `n!!` :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287178):
but `#check  λ n : nat, (rfl : _ +  4  = (_ +  4))` works...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287191):
But I hope you get a metavariable and not n, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287199):
Yes, because check allows unsolved metavars. Otherwise `#check f` where f takes implicit parameters would be pretty useless.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287278):
ha ha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287283):
`#check (rfl : _ = _ +  0)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287290):
didn't give what I expected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287304):
but probably did give what everyone else expected.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287415):
```quote
The underscores won't find it because it is not determined by unification.
```
unification says "this should be a proof of ev _x", and there is something in the local context which is a proof of ev _x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287449):
@**Kenny Lau** my proof of ev_double is lame. Can you do better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287472):
This one surely qualifies for the "this is mathematically obvious so it doesn't matter how obscure the proof is, just make it short"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287521):
```quote
@**Kenny Lau** my proof of ev_double is lame. Can you do better?
```
I should do that with my PhD student, and see what comes out of it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287523):
@**Patrick Massot**  "of course it's even, you just doubled it!"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287533):
I mean asking about real proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287541):
@**Kevin Buzzard** are you aiming for length?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287589):
brevity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287618):
By the way, we have a new nice example of a real world theorem built purely on trusting the big guys in the field: https://arxiv.org/abs/1803.07997 There are three ingredients: one was announced in 2001 and never written. One has a draft written in 2012 but the author doesn't want to make it into a publishable paper. The third one is published but none of the experts except the author understand the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287682):
One day, proof assistants will change all that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287685):
```
theorem  ev_double : ∀ (n : ℕ), ev (double n)
| 0  := ev_0
| (n+1) := (by simp [double] : double n +  2  = double (n+1)) ▸ ev_SS _ (ev_double n)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287687):
how is this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287704):
we all know there's so many things we need to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287705):
we need to prove the equality somehow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287707):
and we need to use recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287713):
```lean
lemma  ev_double (n : ℕ) : ev (2  * n) :=
nat.rec_on n ev.ev_0 (λ n hi, ev_SS _ hi)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287719):
well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287764):
Johannes has a bad influence on Chris

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287771):
changing the definition of `double` is called cheating :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287774):
I see an unused eta contraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287779):
What's the definition of double?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287783):
` definition  double (n : ℕ) := n + n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287804):
and by eta contraction he means
```
lemma ev_double (n : ℕ) : ev (2  * n) :=
nat.rec_on n ev.ev_0 (λ n, ev_SS _)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288271):
My best attempt for double. I saved three characters by using `rec` instead of `rec_on`
```lean
lemma  ev_double (n : ℕ) : ev (double n) :=
nat.rec ev_0 (λ n h, show ev (_ + _), by rw succ_add; from ev_SS _ h) n
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288275):
do we count brevity by characters?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288283):
or by tokens

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288286):
this is ridiculous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288319):
or by file size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288333):
if your goal is to save time, you should stick with what you have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288334):
(so then probably fancy unicode characters cost more)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288353):
and he opened nat! Is that allowed? you have to put `nat.succ_add`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 27 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288408):
I think there should be bonus points for term style. I would have used eq.subst but it was longer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288508):
I don't understand the syntax of Chris' answer! What is this ; from business? I've only ever seen ; in tactic mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288520):
oh we are in tactic mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288525):
Then my question is "what is this from in tactic mode?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288572):
and now I hover over it and find out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288575):
You can use from instead of exact, if you want to save one character.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288581):
I think that's the main reason they put it in.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288590):
Chris do you know about pyth? (as in "pithy")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288591):
https://esolangs.org/wiki/Pyth

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288595):
you bunch are ridiculous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288603):
ok to be fair I use pyth when I need to compute something quickly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288610):
and it's far more convenient than other programming languages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288663):
ha ha "you bunch are ridiculous" "actually I use it IRL"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288670):
The `;` there is actually in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288676):
yes it all dawned on me later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288680):
wait what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288681):
I hadn't seen from in tactic mode before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288695):
@**Kevin Buzzard** he's saying that `;` itself is in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288697):
it's just so you can write `have x, from y` in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288700):
I think we need "coz"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288702):
which is from but one fewer letter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288709):
I'll file an issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 27 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288726):
I prefer `exact` over `from` when it's not used after `show`, `have`, `suffices` or `let` tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 27 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288778):
As for the golfing, I won't enter the ring. I'd emphasize good lemmas in this instance so you can write each individual theorem very concisely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288843):
Aah I see. Perhaps double n = n * 2 or 2 * n would be worth proving before we launch into trying to prove stuff like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288849):
I hope the new parser will allow Kevin to define `coz` by adding one line near the top of his file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288871):
Do code-golf belong to the target of "domain specific language handling"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288932):
You can define `coz` in one line today

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288935):
@**Kevin Buzzard** I've been a member of PPCG for 3 years

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288936):
the people in the chat know me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288953):
```
meta def tactic.interactive.coz := tactic.interactive.from
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288975):
*message stared*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288983):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289032):
and a solution a la Mario:
```
lemma  double.aux (n : ℕ) : double (n+1) = double n +  2  :=
nat.succ_add _ _

lemma ev_double (n : ℕ) : ev (double n) :=
nat.rec ev_0 (λ n h, (double.aux n).symm ▸ ev_SS _ h) n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289273):
```quote
By the way, we have a new nice example of a real world theorem built purely on trusting the big guys in the field: https://arxiv.org/abs/1803.07997 There are three ingredients: one was announced in 2001 and never written. One has a draft written in 2012 but the author doesn't want to make it into a publishable paper. The third one is published but none of the experts except the author understand the proof.
```
@**Patrick Massot** as long as the experts are happy, we're all happy, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289337):
I would be most concerned about the third assumption I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289340):
Right. But there are not all happy about the third ingredient.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289351):
Because the third ingredient was proved by an obscure polish mathematician

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289357):
so you'll have to hope that the referees are either optimists or lazy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289375):
Who didn't even get the Crafoord prize.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289447):
We have two more elaborate plans actually. First we'd like to try to read the Polish proof. And we have a backup plan which is to use an earlier weaker result (about $$C^r$$ diffeomorphisms, $$r \leq 1+\dim(V)/2$$) to get a correspondingly weaker (but still new) result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289474):
How do you get LaTeX rendering on this website?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289523):
two $s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289529):
weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289531):
ooh Coq has an inversion tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289535):
inverting what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289536):
is there a subversion tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289545):
nooo subversion is dead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289553):
all cool kids use git nowadays

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289557):
```
Theorem evSS_ev : ∀ n,  
  ev (S (S n)) → ev n.  
Proof.  
  intros n E.  
  inversion E as [| n' E'].  
  (* We are in the E = ev_SS n' E' case now. *)  
  apply E'.  
Qed. 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289618):
induction n would not go down well here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289625):
Coq knows that the only way to prove ev (S S n) is to prove ev n and deduce ev (S S n)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289721):
is this the same as coinduction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289727):
The question in full:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289736):
```
inductive  ev : nat →  Prop
| ev_0 : ev 0
| ev_SS : ∀ n : nat, ev n → ev (n+2)

open ev

example : ∀ n, ev (n+2) → ev n :=  sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289957):
oh no way, intros n H, cases H works!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289966):
Yay, we have an inversion tactic!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289980):
I still don't understand what this inversion tactic is meant to do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289984):
```
example : ¬ (ev 1) :=  begin
intro H,
cases H,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289987):
(but I'm writing lecture notes on convex integration without integration in parallel of reading Zulip)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290030):
@**Kevin Buzzard** I have a solution: do you want to see it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290031):
inversion says "You are assuming ev (n+2) and the only way to prove this would be by proving ev(n) and tehen applying ev_SS

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290037):
btw what you call "inversion" is just induction on the inductive predicate "ev"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290045):
(it's called `inductive` because you can do `induction`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290047):
it's what software foundations calls inversion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290129):
"rule inversion" is what computer scientists say when they mean "case analysis"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290139):
@**Kevin Buzzard** for a second I thought this is something Lean doesn't have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290140):
(well, it's specific to inductive definitions usually)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290152):
So did I, that's why I mentioned it here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290244):
case (hah) in point
```
example : ∀ n, ev (n+2) → ev n
| n (ev_SS _ h) := h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290266):
Kevin and Kenny, have you managed to prove an affine scheme is a scheme?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290273):
if we're allowed to assume `false`, then we've proved it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290323):
@**Sebastian Ullrich** hmm, I still have much to learn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290326):
you gave a 2-line solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290328):
mine had 10 lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290333):
I considered formatting it as one line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290711):
@**Kevin Buzzard** do you have a link?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290779):
For schemes? I think we're in the wrong topic. We are plenty of lemmas short of proving that an affine scheme is a scheme.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290787):
Tom Hales told me he was going to mention it in his talk at AITP today

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290788):
so Kenny and I and Chris were hard at work trying to get it done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290796):
and then Tom broke his toe and couldn't go to the conference :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290799):
so I decided to leave the undergraduates alone so they can revise for their exams!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290804):
as if they would really do so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290806):
Are you not revising mechanics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290850):
I'm building the function X -> T

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290851):
There are not revising and you are code golfing...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290852):
Go back to schemes!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290853):
:wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290874):
> Are you not revising mechanics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290876):
Let's look at my latest test scores

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290882):
M1M2 100%

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290885):
M1P2 100%

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290886):
M1A1 100%

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290891):
conclusion: continue building the map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290934):
are you arguing by induction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290936):
This is a dangerous technique :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290941):
The final exam is worth 18 times more than the tests so you need to work 18 times as hard, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290944):
This AITP looks interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290948):
what is AITP?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290949):
why did nobody mentioned that when we discussed ITP?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290959):
http://aitp-conference.org/2017/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290960):
a conference on the top of a mountain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290964):
That link might be last year's...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290968):
That where @**Sebastian Ullrich** must be then!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290969):
just at a guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290970):
conferences are always best when they are in a desireable location

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290972):
I never think that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290973):
My favourite conferences are in big cities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290975):
that way I don't miss home so much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291024):
I have been asked to go to exotic conferences in exotic places like Hawaii and have declined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291028):
think of your graduate students who attend who can't afford holidays abroad without work kicking in a bit :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291029):
because I was not sure I could handle a week there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291039):
Last three conferences I went to were in Boston, Berkeley and LA

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291041):
Indeed I was probably looking for http://aitp-conference.org/2018/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291057):
@**Patrick Massot** wait what

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291119):
Oh, it's in Aussois!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291122):
I try to avoid going skiing in March, February is way better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291146):
I could have gone there easily (except that I'm teaching this week)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291153):
I read "Robert Lewis: Toward AI for Lean, via metaprogramming"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291197):
Looks like some people got proper training in grant proposal writing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291199):
I would fund that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Matt Wilson (Mar 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291269):
is that paper available publicly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291282):
I also like the spirit of the schedule:
> **March 25**
> 19:30 dinner
> **March 26**
> ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291443):
Oh, I didn't know Rob had a new paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291449):
I love that the conference page concludes with ski rental prices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291509):
Does talking in this conference imply new paper?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291514):
(I'm trying to learn CS academic life)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291520):
you have to hope that your labmates ski though; not one of mine in graduate school did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291626):
There is http://aitp-conference.org/2018/aitp18-proceedings.pdf but it contains only one page by Rob

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291637):
But it contains question relevant to Lean 4 (stuff about the VM)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291904):
I'd be curious to know what Hales intended to say

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291922):
He was probably going to let out the secret.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291938):
Which one? There are so many secrets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291942):
He just got a big grant to fund formal abstracts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291952):
Oooh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291997):
and talking of secrets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292004):
Fund what exactly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292007):
today I heard i'd been awarded a rather smaller grant to find my 13 undergraduates this summer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292017):
I think Hales is going to pay people to type in statements of theorems in the Annals or whatever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292023):
into Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292034):
Where will he find those people?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292043):
If he's sitting at home with a broken toe he should come here and tell us the details :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292550):
Hah, I guessed from the email I just got that I was mentioned here. There's no new paper, just a talk about some experiments that Minchao and I have been doing in our free time. Nothing very deep.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292584):
The slides will eventually be online. The wifi here barely works, it took me ten minutes to email a picture of the scenery so I'm not gonna try to upload them now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292586):
Is this hammer thing the same as the stuff Isabelle users always talk  about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292639):
Yeah. There's a recent paper that translates the idea to Coq.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292663):
Great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292716):
Do you have a public demo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292728):
And, while you're here: are you considering have your Mathematica stuff turned into a Sage stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292865):
We've only worked out the relevance filter component, and it isn't quite fast enough for practical use yet. This is really just experimenting right now. There's some messy jumble of code on github but nothing you want to look at. Johannes and I have been talking to a masters student who is interested in this kind of automation though, so with some luck, the three of us will make some progress soon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292868):
The ideas behind the link will transfer easily enough. The engineering is another story, and I've never actually used Sage.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292906):
It could happen, particularly with an application in mind, but it isn't at the top of my to-do list.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292975):
I don't have any specific application in mind. But I was surprised by your paper because I know no Mathematica user, everybody uses Sage around me, and teaches Sage to students

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293020):
And Lean is open source software so it looks strange to choose Mathematica as a partner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293023):
(well Lean 4 development is not yet open source, but let's hope for the best)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293079):
But I should be sleeping. Tomorrow I need to teach old fashioned algebraic geometry in Sage (computing projections of algebraic sets using resultants).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293084):
Bye

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293097):
I had the opposite experience as an undergrad, they taught us Mathematica and nothing else. Most of the people I asked said similar, but it was definitely a biased sample. And there were people at Wolfram who were already interested in Lean, so it made sense at the time, heh.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Mar 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293105):
I should also call it a night!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293282):
I'm still sitting here idly trying software foundations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293292):
```
namespace hidden

inductive  le : nat → nat →  Prop
| le_n : ∀ n, le n n
| le_S : ∀ n m, (le n m) → (le n (nat.succ m))

local  infix ` lq ` :50  :=  λ m n, le m n

open le

lemma n_le_m__Sn_le_Sm : ∀ n m,
  n lq m → nat.succ n lq nat.succ m :=
begin
  intros n m H,
  cases H with NOT_USED NOT_USED_EITHER q Hnq,
  repeat {admit},  
end 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293348):
cases is throwing away my variable names

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293359):
(I called it lq to avoid confusion with already-defined-things)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295500):
I proved 2+2 isn't 6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295506):
```
definition  S (n : ℕ) := nat.succ n

inductive  R : nat → nat → nat →  Prop
| c1 : R 0  0  0
| c2 : ∀ m n o, R m n o → R (S m) n (S o)
| c3 : ∀ m n o, R m n o → R m (S n) (S o)

open R

example : R 1  1  2  := c3 _ _ _ (c2 _ _ _ c1)

example : ¬ (R 2  2  6) :=  begin
intro H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295555):
Cases eats far too many variables which makes the proof look even more ridiculous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 28 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295607):
Cut and paste from VS Code into zulipchat (ubuntu, firefox) isn't great. I get extra spaces, extra carriage returns

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 28 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295722):
I'm not sure what's up with zulip paste. I don't think it was doing that when we first moved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 28 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295724):
Here's a shorter way to write that proof:
```
example : ¬ (R 2 2 6) | H := by casesm * [R _ _ _]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 28 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295739):
but if you look at the resulting proof, it's rather involved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 28 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295788):
You can simplify the proof if you define `R` to avoid having both `c2` and `c3`; the proof length here increases exponentially

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 28 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295898):
> cases is throwing away my variable names

I tried once to make a version of cases that doesn't throw away names, but it's tough. What happens is that the names are allotted first, in the case splits, and then some cases are eliminated outright by inversion so you never see those names. I just put `_` for those

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359326):
@**Kevin Buzzard** did you do the 4-star exercise proving that the two notions of evenness are equivalent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359329):
Three notions :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359330):
I must be ahead of you ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359338):
Link?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359397):
Use cases or induction on the inductive prop, if that's the issue. This blew my mind.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359405):
https://softwarefoundations.cis.upenn.edu/lf-current/IndProp.html#lab206

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359407):
Yes I did that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359416):
I did the exercise before that one as well, which IIRC I used.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359594):
Here's what I think Kenny is asking:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359603):
All I'm asking is " did you do the 4-star exercise proving that the two notions of evenness are equivalent? "

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359604):
```
def  S  := nat.succ

inductive  ev : nat →  Prop
| ev_0 : ev 0
| ev_SS : ∀ n : nat, ev n → ev (S (S n))

inductive  ev' : nat →  Prop
| ev'_0 : ev' 0
| ev'_2 : ev' 2
| ev'_sum : ∀ n m, ev' n → ev' m → ev' (n + m)

theorem  ev'_ev : ∀ n, ev' n ↔ ev n :=  sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359607):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359609):
and the answer is "yes, I did it whilst watching the football on Tuesday"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359650):
did you use term mode or tactic mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359652):
tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359656):
why am i not surprised

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359657):
I really like Software Foundations, because I can do the exercises no matter how many stars they have, which is a good confidence boost :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359665):
The first time I saw a 5-star one I thought "oh gosh", and then I just sat down and did it, and thought "maybe I already know what they're trying to teach me here"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359670):
maybe they're teaching you to quit using tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359672):
rofl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359722):
Coq is big on tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359727):
Term mode is favored by mathematicians who work in isabelle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359734):
Ish. Obviously there are exceptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359737):
Lean docs seem to push term mode a lot at the start.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359740):
I did notice that Software foundations instantly starts with "OK so here are some easy things, let's prove them in tactic mode".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359742):
You mean Jeremy pushes term mode in TIPL 🙂

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359743):
As did a Coq tutorial I did before I came to Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359782):
I think that mathematicians should start with tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359785):
because they typically have no idea what a functional language is or what a lambda is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359787):
mathematicians should start with formal proofs...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359790):
fitch, hilbert, whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359791):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359792):
via tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359793):
via writing it down on pen and paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359841):
You can get pretty far writing everything out with assume, show, and calc in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359857):
as far as Zeno got?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359906):
whenever I do a tactic proof I don't indent the line after `begin` and I can hear Johannes' voice in my head telling me that I can't get it PR'ed to mathlib that way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359907):
Not familiar with his proofs, unfortunately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359915):
Haha, best fix your style or else you'll get another nasty email asking you to teach your students the mathlib style

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359917):
It's the voices in my head I have to deal with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359966):
be the compiler, be the journal editor... these voices are quite talented

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359971):
yeah I have some pretty high-class voices in my head.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360082):
Did you skip over the 5 star pumping lemma? That was quite an exercise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360115):
Actually even the one on palindromes in the same chapter was involved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360123):
I looked at that when I didn't have access to a computer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360126):
and decided that mathematicians didn't care about pumping lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360128):
I did do the 5 star constructive mathematics exercise even though the first time I saw it I figured mathematicians didn't care about that either.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360137):
@**Kevin Buzzard** try doing regex :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360138):
I did the 4 star even question again just now, because I couldnt' find my original solution and Kenny asking it made me concerned I'd missed something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360139):
I saw that regex stuff. I am not convinced I need to learn this sort of skill. I'm sure I'd find it a lot of fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360140):
but I need to focus on other things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360189):
Kenny, my evenness proof is just `repeat {induction *, exact *}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360191):
well, perhaps not quite that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381653):
I have a 4-line 223-character solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381654):
```
inductive ev : nat → Prop
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)

inductive ev' : nat → Prop
| ev'_0 : ev' 0
| ev'_2 : ev' 2
| ev'_sum : ∀ n m, ev' n → ev' m → ev' (n + m)

open ev
open ev'

theorem ev'_ev.standalone : ∀ n, ev' n ↔ ev n :=
Line 1
Line 2
Line 3
Line 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381656):
Let's see who can beat me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381658):
(I used appropriate spacings and I counted them in)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382012):
i'm surprised there's so much interest in the "three different definitions of even" exercise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382023):
@**Andrew Ashworth** beat me :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382029):
i thought the most interesting ones in that chapter were the subseq and palindrome problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382078):
i would give it a shot except i'm currently supposedly doing work at the moment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382173):
and i think the nodup and nostutter predicates are interesting since they are related to how finite sets are implemented in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ching-Tsun Chou (Mar 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124383111):
I would be interested to know if anyone can prove the pigeonhole principle (last exercise of the IndProp chapter) without excluded_middle.


{% endraw %}
