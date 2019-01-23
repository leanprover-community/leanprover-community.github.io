---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22229tutorial.html
---

## Stream: [general](index.html)
### Topic: [tutorial](22229tutorial.html)

---


{% raw %}
#### [ Johan Commelin (Oct 04 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155789):
@**Patrick Massot** Would you mind pushing your demo to a new `tutorial` branch on community fork? Maybe as `docs/tutorial/demo.lean`.

#### [ Johan Commelin (Oct 04 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155799):
After that we could attempt answering Neil's questions in that branch as well.

#### [ Johan Commelin (Oct 04 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155804):
Q1 and Q2 have been done. They can easily be entered.

#### [ Johan Commelin (Oct 04 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155874):
Q3 shouldn't be hard either. Q4 needs work. Q5 should be rather easy again.

#### [ Johan Commelin (Oct 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155893):
The point is that we should write lots of comments in those files. So that people can actually learn a lot of Lean. Instead of learning only a tiny bit of maths (that they actually knew already).

#### [ Patrick Massot (Oct 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155894):
Ok, I'll do that

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156024):
If you're looking for help with this, I'd be happy to contribute. I think I should be able to do Q5.

#### [ Johan Commelin (Oct 04 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156040):
Sure! Please contribute!

#### [ Johan Commelin (Oct 04 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156234):
@**Patrick Massot** Do you have time to do this before the talks start? Otherwise I can start the branch... and you can dump your demo later (-;

#### [ Patrick Massot (Oct 04 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156333):
depends on the RER train. I'm leaving my house, let's see when I'll arrive in Orsay

#### [ Sean Leather (Oct 04 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156338):
I would recommend using a top-level `tutorial` directory instead of the subdirectory  under `docs`. First, it's more discoverable (easier to find). Second, I think many people expect `docs` to not be code, which could lead people to not look in there for code.

#### [ Johan Commelin (Oct 04 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156397):
I'm fine with that. It depends on what the powers that be prefer (-; @**Mario Carneiro** @**Johannes Hölzl**

#### [ Johannes Hölzl (Oct 04 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156595):
if we add tutorials, I would also prefer `tutorial` in the top level directory.

#### [ Johannes Hölzl (Oct 04 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156651):
But we could also have a separate repository in `leanprover-community` then its easier to contribute

#### [ Johan Commelin (Oct 04 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156668):
I think it is best to have this end up in mathlib. Because then we are forced to keep it working. Also: better discoverability

#### [ Kevin Buzzard (Oct 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135161048):
Stick it in the top level and it can be moved later

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240591):
I've made some progress on Q5. Is someone (Patrick? Johan?) planning to make a branch in leanprover-community I can PR to?

#### [ Johan Commelin (Oct 05 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240650):
Sorry, I have to do some other stuff now. Please go ahead and create the branch

#### [ Patrick Massot (Oct 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240799):
I'll create the branch if you want

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240813):
Sure, that'd be great.

#### [ Patrick Massot (Oct 05 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240831):
https://github.com/leanprover-community/mathlib/tree/tutorials

#### [ Patrick Massot (Oct 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240896):
wait

#### [ Patrick Massot (Oct 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240898):
I messed up

#### [ Patrick Massot (Oct 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240985):
now it's ok

#### [ Patrick Massot (Oct 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135241326):
Ok, I've pushed my demo file: https://github.com/leanprover-community/mathlib/commit/bf36dd1e66d373c53666ca4579649f767955ed42

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135241958):
OK, I've PR'd my file for review [here](https://github.com/leanprover-community/mathlib/pull/6).

#### [ Johan Commelin (Oct 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242037):
You don't have write access to the community fork?

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242038):
Oh, I guess not.

#### [ Johan Commelin (Oct 05 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242098):
@**Mario Carneiro** @**Simon Hudon** can one of you fix this?

#### [ Simon Hudon (Oct 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242854):
Done

#### [ Simon Hudon (Oct 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242861):
And now, I'm off. Good day!

#### [ Johan Commelin (Oct 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242909):
Sleep tight!

#### [ Simon Hudon (Oct 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242942):
Thanks :) :zzz:

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135254193):
Thanks Simon!

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135254614):
I've gone ahead and merged my PR. Here are two specific questions, and I would appreciate any other comments as well:

1) I'm not sure how to finish [this proof](https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96).

2) The forward and backward directions in the `iff.intro` [here](https://github.com/leanprover-community/mathlib/blob/4752d91c7e0781e275e6a14edafcbf1a73b8c8ae/tutorials/partitions.lean#L134) are identical except that the roles of ` s₁` and `s₂` are swapped. Is there a cleaner way to do this? I thought about using `wlog` but I couldn't figure out how to use it in this case.

#### [ Kevin Buzzard (Oct 05 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135259968):
```quote
1) I'm not sure how to finish [this proof](https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96).
```
Oh I love these questions. Mathematicians don't even give them a second thought. You have two finite types with the same cardinality and and you want to conclude that some operation on the type which only depends on the cardinality (e.g. the cardinality of the number of partitions) is the same for each. This is stupidly hard to do in Lean and it's coming up more and more. The general problem is that if you have two types which are equivalent (i.e. you are given inverse bijections between the types and proofs that the maps are inverse to each other on both sides) then a mathematician instantly identifies the types, and any reasonable theorem or definition constructed with one has an obvious counterpart for the other. Now someone will explain that yeah in theory this can all be done with `traversable` or `transportable` or something, but I can't do this because I don't really understand what needs to be done. We've just missed @**Simon Hudon** but he knows something about this sort of question. My guess is that you need to prove that if the cards are the same then there's an `equiv` (which might well be there), and then you want to prove that if `X equiv Y` then `partitions X equiv partitions Y` (which looks trivial but might involve some actual work) and then you want to prove that partitions X equiv partitions Y then the cards are the same, which might well be there.

#### [ Simon Hudon (Oct 05 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135260449):
Thanks for cueing me in @**Kevin Buzzard**! That is indeed a nice question!

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135260515):
> if the cards are the same then there's an equiv (which might well be there), 

Yeah, I was attempting to use `fintype.equiv_fin`for that but it gives me an equiv wrapped up in `trunc`... so I gave up and decided to ask for help.

#### [ Kevin Buzzard (Oct 05 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261258):
The example I ran into in around Feb/Mar time was that I had a complex of abelian groups `A -> B -> C` and an isomorphic (in the obvious sense) complex `A' -> B' -> C'` and wanted to deduce that these two complexes had isomorphic cohomology -- in fact I had several questions of this nature. I wanted the isomorphism to be explictly built for me by a tactic but in the end I don't think this ever happened.

#### [ Kevin Buzzard (Oct 05 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261330):
People ground out proofs very quickly -- "this is an isomorphism and this is an isomorphism so this map between kernels is an isomorphism, and now this map between images is an isomorphism, and..." but they really had to build them

#### [ Kevin Buzzard (Oct 05 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261383):
But I want proof by a tactic called `mathematical_intuition` or `transport_de_structure` or something

#### [ Kevin Buzzard (Oct 05 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261600):
and my understanding was that making a tactic would somehow involve having to go through a bunch of Lean theorems or definitions applying to abelian groups, and tagging them with an attribute which is a claim that this function some of whose inputs or outputs are abelian groups "naturally" descends to a function whose inputs and outputs are equivalence classes of abelian groups, where the equivalence is given by group isomorphism.

#### [ Kevin Buzzard (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261654):
And I think the idea was that some of the attribute-tagging could be done automatically.

#### [ Simon Hudon (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261659):
@**Kevin Buzzard** I did build some isomorphisms with a tactic but I got some push back because transport was seem as redundant with transfer and I didn't take it any further

#### [ Kevin Buzzard (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261668):
`transfer`, that's it.

#### [ Kevin Buzzard (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261673):
Thanks Simon.

#### [ Simon Hudon (Oct 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261691):
:+1:

#### [ Simon Hudon (Oct 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261724):
@**Bryan Gin-ge Chen** `trunc` should not deter you. You can unwrap it when you're proving a proposition.

#### [ Simon Hudon (Oct 05 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261750):
It just states that the object exists in a non constructive way

#### [ Kevin Buzzard (Oct 05 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261789):
This is an important tactic for mathematicians and it isn't there. Bryan's question is a great example of an EIMHIL questions (easy in maths, hard in Lean). The exciting thing about this community is that several times in the past I have explicitly flagged things which were easy in maths but hard in Lean, and other members of the community like Simon, Mario and Johannes sometimes step up and make them easy in Lean. The `ring` tactic is a great example of this.

#### [ Simon Hudon (Oct 05 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261791):
Look at `trunc.induction_on`

#### [ Kevin Buzzard (Oct 05 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261831):
Simon, do you know if is there a relatively easy way to patch up the sorry completely?

#### [ Simon Hudon (Oct 05 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261837):
:D Glad to be helpful. I think Lean won't be as easy as math (!) but there certainly are a lot of low hanging fruits to make it a lot easier to use.

#### [ Kevin Buzzard (Oct 05 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261924):
@**Jeremy Avigad** I would be really interested to hear your opinion on what a mathematician *means* when they say that two objects are "canonically isomorphic".

#### [ Kevin Buzzard (Oct 05 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261940):
This is notion which is somehow still missing in my Lean experience.

#### [ Kevin Buzzard (Oct 05 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261980):
I contributed to some mathoverflow chat about this once

#### [ Kevin Buzzard (Oct 05 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262053):
https://mathoverflow.net/questions/19644/what-is-the-definition-of-canonical/19663#19663

#### [ Simon Hudon (Oct 05 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262059):
```quote
Simon, do you know if is there a relatively easy way to patch up the sorry completely?
```
I'll look into it

#### [ Kevin Buzzard (Oct 05 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262100):
Oh I just wondered whether you knew immediately that this would be a relatively straightforward sorry to remove. Like when Patrick asks silly questions about subs on nats not working properly and I know I can prove every one because I just know how they work better than he does in some funny way.

#### [ Kevin Buzzard (Oct 05 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262150):
I think he can do them too, but they just annoy him too much :-)

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262174):
@**Simon Hudon** Ah, thanks! Up to now I've been getting away with just applying lemmas and not really thinking much about how things are actually set up using inductive types and such, but now I should probably turn my brain on.

#### [ Kevin Buzzard (Oct 05 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262176):
but I have no idea whether Bryan's sorry is easy to fill in or not. In some sense Neil Strickland is exhibiting a problem with doing mathematics in Lean here.

#### [ Kevin Buzzard (Oct 05 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262251):
And it's a problem I stumbled upon when doing schemes and so no doubt is looming when the perfectoid project gets really moving again

#### [ Kevin Buzzard (Oct 05 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262278):
We will need to be replacing complete topological rings with canonically isomorphic complete topological rings left right and centre.

#### [ Kevin Buzzard (Oct 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262354):
where by canonically isomorphic I mean an explicit `equiv` of morphisms in the appropriate category.

#### [ Simon Hudon (Oct 05 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262623):
@**Bryan Gin-ge Chen** It's a common experience I find. E. W. Dijkstra had a nice way to put it: just let the symbols do the work.

#### [ Simon Hudon (Oct 05 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262725):
It's taking me a little bit to boot up my brain but I have my coffee now so I should be able to understand a bit more. But Kevin had the right idea I think: you need a congruence lemma for `partition` with regards to `equiv`

#### [ Simon Hudon (Oct 05 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262743):
For the rest, let's see where the symbols take us

#### [ Kevin Buzzard (Oct 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264259):
@**Mario Carneiro** is that sorry above easy to fill in?

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264261):
OK, I think I have a rough idea of what to look at now.  It's rather hard to figure out how to use something new, e.g. `equiv` when there isn't a chapter of TPiL to fall back on. It doesn't help that core lean has `has_equiv` which is apparently just unrelated notation. At least mathlib itself provides plenty of example code to learn from. Anyways, hopefully these tutorials will help future users...

#### [ Kevin Buzzard (Oct 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264271):
https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96

#### [ Simon Hudon (Oct 05 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264295):
I'm almost done proving:

```lean
lemma card_eq_of_equiv {s : finset α} {t : finset β} (h : s.to_set ≃ t.to_set) :
  s.card = t.card :=  ...
```

if you want to wait a moment

#### [ Kevin Buzzard (Oct 05 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264308):
`equiv X Y` is the best kind of bijection between two types `X` and `Y`.

#### [ Kevin Buzzard (Oct 05 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264376):
It's an explicit map from `X` to `Y` and an explicit inverse.

#### [ Kevin Buzzard (Oct 05 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264419):
Just saying "there's a map and it's a bijection" is slightly less information in Lean, because they need the computer science version of the axiom of choice (getting data from proofs of existence), so `equiv` is the important one to focus on.

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264426):
@**Simon Hudon** Cool! I'm still digesting other code so you'll probably finish before I even get close to attempting my own version.

#### [ Kevin Buzzard (Oct 05 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264431):
The problem is that `equiv` is what mathematicians would think of as a canonical bijection between two sets.

#### [ Kevin Buzzard (Oct 05 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264494):
There are other equivs too -- group isomorphisms, topological space isomorphism etc.

#### [ Kevin Buzzard (Oct 05 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264510):
And then there is a whole bunch of stuff defined on types or groups or whatever, which descends to the equivalence classes under these various equivalence relations.

#### [ Kevin Buzzard (Oct 05 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264591):
And for mathematicians these are all "proof by obvious", so it's clear there's a tactic brewing. But we don't have that tactic yet.

#### [ Kevin Buzzard (Oct 05 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264690):
And without it, replacing a topological monoid with a canonically isomorphic topological monoid in a complex of topological monoids and then proving that the cohomology of the complex "hasn't changed" (when Lean actually can see that it _has_ changed in some sense) is going to be hard work I think.

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264916):
It's certainly eye-opening (in a good way, probably). I remember having vaguely similar feelings about all the calculus I thought I knew when I took analysis.

#### [ Simon Hudon (Oct 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266320):
@**Bryan Gin-ge Chen** The short answer to your question is: yes it's feasible. You need congruence of `partitions` with regards to `equiv` and congruence of `card` with regards to congruence as well. I'm completing the proof now if you want it. It you want to do it yourself, you can use these three hints:

1. prove congruence of partitions
2. prove congruence of card
3. use trunc.induction_on

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266793):
@**Simon Hudon** Great, thanks so much! Feel free to push your proofs into the tutorials branch if you'd like. I'll try to study them and add tutorial-style documentation later on.

#### [ Kevin Buzzard (Oct 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266877):
```quote
@**Simon Hudon** Great, thanks so much! Feel free to push your proofs into the tutorials branch if you'd like. I'll try to study them and add tutorial-style documentation later on.
```
This should not be being documented. This should be being hidden by tactics, no?

#### [ Kevin Buzzard (Oct 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266939):
"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)

#### [ Kevin Buzzard (Oct 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266952):
I think there's something missing here.

#### [ Kevin Buzzard (Oct 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266989):
It's rw for data somehow

#### [ Kevin Buzzard (Oct 05 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267068):
We want a rw that eats equivs, not equalities and iffs, and works for data in situations where we only care about the answer up to canonical isomorphism.

#### [ Simon Hudon (Oct 05 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267175):
That would be nice. It involves proving congruence about a ton of functions though. The nice thing about `=` is that every function preserves it.

#### [ Simon Hudon (Oct 05 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267222):
Such a tactic as you're describing is doable. We only need to decide how high it needs to be on the priority list

#### [ Kevin Buzzard (Oct 05 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267239):
I think we've had this discussion before. Wasn't there some hope that by proving some lemmas about the basic constructors in Lean one could then go on and get a machine to generate all the congruence lemmas automatically?

#### [ Kevin Buzzard (Oct 05 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267426):
Can the `transfer` tactic be turned into this mega-rw tactic? Very often in mathematics people only care about the answer up to isomorphism or perhaps a well-defined notion of canonical isomorphism (maybe it's part of the story that the object is unique up to unique isomorphism, for example).

#### [ Kevin Buzzard (Oct 05 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267545):
we want to be able to rewrite isomorphic perfectoid spaces. Is Lean up to that?

#### [ Simon Hudon (Oct 05 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267731):
I remember building group isomorphism from their underlying type isomorphism but I don't remember the rest of the discussion that you're referring to.

#### [ Simon Hudon (Oct 05 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267823):
But in my libraries, I have some code to construct an isomorphism from an arbitrary type to sums and pairs. With Jeremy, we're talking about adding support for reasoning about W-types which should complete the picture to building isomorphism to canonical type representations

#### [ Simon Hudon (Oct 05 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267946):
Maybe that's what you're looking for?

#### [ Kevin Buzzard (Oct 05 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268845):
I'm looking for magic

#### [ Kevin Buzzard (Oct 05 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268851):
`example (X Y : Type) (f : Type → Type) (h : equiv X Y) : equiv (f X) (f Y) := by rw h`

#### [ Kevin Buzzard (Oct 05 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268880):
Mario sometimes tells me that this isn't always true, but I'm not sure I've ever seen a mathematical example of it going wrong.

#### [ Kevin Buzzard (Oct 05 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268942):
Here `equiv` could mean an `equiv` of structures, and then f is somehow known to preserve all the structure.

#### [ Kevin Buzzard (Oct 05 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268989):
Is that magic Simon?

#### [ Kevin Buzzard (Oct 05 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269044):
This time round I have a far more mature understanding of what I think is missing.

#### [ Simon Hudon (Oct 05 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269222):
What we probably need is a type class to tell us that `f` preserves `equiv`. Then `iso_rw h` (a tactic we want to build) would know how to build the proof. As it is, `rw` builds its proofs using `congr_arg` and `congr_fun` which needs no assumptions about `f`. We need basically the same tools for `equiv`.

#### [ Kevin Buzzard (Oct 05 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269351):
It would be interesting to find out when this is going to bite the perfectoid project and how badly it will bite it. With schemes it bit us when we were doing structure sheaves. Here we only have structure presheaves but who knows.

#### [ Kevin Buzzard (Oct 05 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269402):
In the schemes project I ended up writing some really weird code.

#### [ Kevin Buzzard (Oct 05 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269745):
 https://github.com/kbuzzard/lean-stacks-project/blob/53bea440dc519a1f6d023cbecc2dfe270499bbbf/src/tag01HR.lean#L210

#### [ Kevin Buzzard (Oct 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269818):
Over 350 (admittedly very inelegant and much commented) lines of code, to prove something which de Jong dismisses with one throwaway comment.

#### [ Kevin Buzzard (Oct 05 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269955):
"Thus we may apply Algebra, Lemma 10.23.1 to the module $$M_f$$ over $$R_f$$ and the elements $$g_1,\ldots,g_n$$." Note that Chris had already proved the lemma. The issue was applying it.

#### [ Kevin Buzzard (Oct 05 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135270021):
because $$R[1/f][1/g]$$ was only canonically isomorphic to $$R[1/fg]$$

#### [ Scott Morrison (Oct 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135284021):
```quote
"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)
```
@**Kevin Buzzard**, have you seen @**David Michael Roberts** attempt to summarise the latest disagreement between Mochizuki and Scholze? <https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf>. It's very much about whether such replacements were valid or not.

#### [ Kevin Buzzard (Oct 06 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135291222):
Wow I had not seen that. Thanks.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135298733):
Is there an easy proof of this (is it secretly in mathlib)? I did this the hard way with `ext` and lots of digging back and forth through exists statements:
```lean
def embedding_of_finset {β : Type*} (f : α ↪ β) : finset α ↪ finset β := 
⟨λ S, S.map f, by {
  unfold function.injective,
  intros a₁ a₂ h,
  simp [finset.ext] at h ⊢,
  intro x,
  split,
  { intro H,
    have hex := (h (f x)).mp (exists.intro x ⟨H, rfl⟩), 
    exact exists.elim hex (by { intros y hy,
      have : y = x := f.2 hy.2,
      exact this ▸ hy.1 }) },
  { intro H,
    have hex := (h (f x)).mpr (exists.intro x ⟨H, rfl⟩), 
    exact exists.elim hex (by { intros y hy,
      have : y = x := f.2 hy.2,
      exact this ▸ hy.1 }) } }⟩
```

#### [ Johan Commelin (Oct 06 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299119):
```quote
```quote
"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)
```
@**Kevin Buzzard**, have you seen @**David Michael Roberts** attempt to summarise the latest disagreement between Mochizuki and Scholze? <https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf>. It's very much about whether such replacements were valid or not.
```
@**David Michael Roberts** Thanks for writing these!

#### [ Mario Carneiro (Oct 06 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299259):
oops... I was too focused on the image properties and forgot about the fact that the function is injective

#### [ Simon Hudon (Oct 06 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299510):
I pushed something like that to `tutorial` and called it `map'`

#### [ Simon Hudon (Oct 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299600):
Also, I finished the proof of `card_partitions_eq_card_partitions_fin` in the partition tutorial. It needed much more work than I thought

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299601):
Ah, perfect! I was so engrossed in my attempt that I missed your commit.

#### [ Simon Hudon (Oct 06 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299610):
The big changes that I made was using `finset.sup` in the formulation of partition instead of using `multiset`s which required a few lemmas in `finset`

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300028):
Very nice! Using `sup` is much cleaner than the hack I was using with multiset.

[Here's what I had](https://gist.github.com/bryangingechen/4ba169f7db65711a07643cf213039049#file-partitions-lean-L282). Now that I've looked at what you did, I see there's still a ton of stuff needed to fill in the sorry at line 292. In particular I hadn't even started on something like `partitions_congr` yet and that was definitely also necessary.

#### [ David Michael Roberts (Oct 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300233):
```quote
```quote
```quote
"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)
```
@**Kevin Buzzard**, have you seen @**David Michael Roberts** attempt to summarise the latest disagreement between Mochizuki and Scholze? <https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf>. It's very much about whether such replacements were valid or not.
```
@**David Michael Roberts** Thanks for writing these!
```
You're welcome!

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300977):
@**Simon Hudon** Just a heads-up, I'm rebuilding tutorial and I think your changes to `ext` have broken the proofs of various things in category_theory and holor.

#### [ Simon Hudon (Oct 06 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300987):
Sorry about that. You can revert them for now.

#### [ Simon Hudon (Oct 06 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301074):
For the last `sorry`, do you need the lattice to be different from the lattice on finite sets?

#### [ Simon Hudon (Oct 06 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301119):
Ok, I see your definition of subset. I'll pick it up tomorrow if you haven't managed to solve it

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301126):
Yeah, I was thinking of implementing as a bonus [the lattice structure described here](https://en.wikipedia.org/wiki/Partition_of_a_set#Refinement_of_partitions).

#### [ Simon Hudon (Oct 06 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301169):
Ah! I see! You can somehow decrease a partition by taking one of its parts and splitting it, right?

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301174):
Exactly.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301305):
I think I could muddle my way through that eventually, though you're definitely welcome to work on it if you want to. I'd also appreciate comments on the other proofs / tutorial text that I've added if you've had a chance to look at them.

#### [ Mario Carneiro (Oct 06 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301647):
If you use equivalence relations instead of partitions, this follows from the fact that equivalence relations have a Moore structure (they are closed under arbitrary intersection), so they have a complete lattice structure

#### [ Johan Commelin (Oct 06 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301756):
@**Bryan Gin-ge Chen** https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109 Couldn't you just compare the `multiset.join` to the `multiset` that underlies our `finset`?

#### [ Johan Commelin (Oct 06 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301989):
@**Bryan Gin-ge Chen** Consider adding an example to https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L193 where the issue is multiplicity > 1.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302186):
```quote
@**Bryan Gin-ge Chen** https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109 Couldn't you just compare the `multiset.join` to the `multiset` that underlies our `finset`?
```
Thanks for pointing this out. In fact, Simon has created a better solution for this using `sup` which is used in `partition_of_disjoint_union` right below. I'll edit...

I've added this example:
```lean
#eval (is_partition ({{0}, {1}, {1,3}} : finset (finset (fin 4))) : bool) -- ff
```

#### [ Mario Carneiro (Oct 06 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302235):
I think this file could stand to be generalized quite a bit. I would want to see partitions defined as equivalence relations, forget the finiteness constraint, and forget the finset representatives

#### [ Mario Carneiro (Oct 06 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302244):
Then, given this, you can define the Bell numbers by a recurrence (so they compute fast), and prove that the number of partitions on a finite set is a bell number

#### [ Mario Carneiro (Oct 06 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302257):
At the same time, you can define an efficiently computable finset representation of a partition by recursion rather than filtering the universe

#### [ Mario Carneiro (Oct 06 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302304):
this both proves the recursion scheme for calculating its size, and also gives an efficiently computable partition function on finset

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302314):
That sounds cool. Is there a good place to read about this approach?

#### [ Mario Carneiro (Oct 06 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302320):
not particularly... basically finsets are bad for proving stuff when you don't need finiteness explicitly

#### [ Mario Carneiro (Oct 06 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302360):
you should use sets instead

#### [ Mario Carneiro (Oct 06 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302363):
especially since "partition" generalizes so nicely to the infinite case

#### [ Mario Carneiro (Oct 06 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302371):
If you need more details about some part about that let me know

#### [ Mario Carneiro (Oct 06 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302418):
It would be nice to have the [Bell triangle](https://en.wikipedia.org/wiki/Bell_triangle) used for calculating and defining the bell numbers

#### [ Johan Commelin (Oct 06 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302637):
I guess Lean automatically memoizes computations? If I define `A n k = A (n-1) k + A n (k - 1)`, and I ask it to compute `A 10 5`, does that lead to combinatorial explosion? Or will it efficiently remember the terms it computed?

#### [ Johan Commelin (Oct 06 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302638):
@**Simon Hudon** Do you know this?

#### [ Mario Carneiro (Oct 06 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302991):
Just for fun:
```lean
def bell_aux₁ : ℕ → ℕ × list ℕ → ℕ × list ℕ
| n (r, l) := (r, n :: l)

def bell_triangle : ℕ → list ℕ → ℕ × list ℕ
| n [] := (n, [])
| n (m :: l) := let n' := n + m in bell_aux₁ n' (bell_triangle n' l)

def bell_aux : ℕ → ℕ × list ℕ
| 0     := (1, [])
| (k+1) := let (n, l) := bell_aux k in bell_aux₁ n (bell_triangle n l)

def bell (n : ℕ) : ℕ := (bell_aux n).1

#eval list.map bell (list.range 20)
```

#### [ Mario Carneiro (Oct 06 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303001):
lean does not memoize things unless you tell it to. This is one of the major shortcomings of lean 3

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303250):
Is the efficient partition function on finset that you had in mind one based on the "Combinatorial Interpretation" in the Bell triangle wiki page?

#### [ Johan Commelin (Oct 06 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303251):
Do we have a `memoize` monad that automagically does that for you?

#### [ Mario Carneiro (Oct 06 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303295):
I PR'd one to core back in the day, rejected

#### [ Mario Carneiro (Oct 06 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303301):
To do it in pure lean requires explicit maintenance of the accumulator data, in this case the `list nat` that forms the lines of the triangle as we progress

#### [ Johan Commelin (Oct 06 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303345):
Right, but a pure Lean version might already be nice.

#### [ Mario Carneiro (Oct 06 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303346):
@**Bryan Gin-ge Chen** Yes. That description of how to count partitions is exactly what you need to write a partition generating algorithm that obviously has length B_n

#### [ Mario Carneiro (Oct 06 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303357):
Lean can't figure out your accumulator data for you, at least not effectively

#### [ Mario Carneiro (Oct 06 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303361):
For example it's not completely obvious that you can calculate fibonacci numbers with a two number sliding window

#### [ Johan Commelin (Oct 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303406):
I was thinking about a naive cache that would just remember all Fibonacci numbers. Don't bother about two number sliding windows. Or am I missing something?

#### [ Mario Carneiro (Oct 06 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303459):
Well, yes that can be done, indeed that's how lean used to work

#### [ Mario Carneiro (Oct 06 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303498):
Leo decided that this causes unpredictable performance characteristics (since it depends on how the equation compiler compiles your code)

#### [ Mario Carneiro (Oct 06 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303500):
so now it just follows what you tell it, and if you use a bad algorithm then it's your fault

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135318182):
@**Simon Hudon** I've just pushed a commit that moves the more general lemmas you wrote in `partitions` to more appropriate places in `data.finset`, `data.fintype` and `data.equiv.basic`. Also, one of the `tactic.tfae` tests still fails, even after I reverted the `tactic.ext` change.

For now I think I'll leave the tutorial partitions file alone and see if I can make some progress working on Mario's idea in another file. If that turns out well that we can then decide whether we want to completely replace what we've done or perhaps include both approaches.

#### [ Simon Hudon (Oct 07 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135327337):
The `tfae` problem is separate. Maybe we should just remove it from master while I fix it

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333218):
@**Mario Carneiro** I'm stuck on something dumb:
```lean
import data.set.lattice

open function

variable (α : Type*)

/- We define a partition as a family of sets associated to an equivalence relation on a set -/

structure partition :=
(blocks : set (set α))
(empty_not_mem_blocks : blocks)
(blocks_partition : ∀ a, ∃ b, b ∈ blocks ∧ a ∈ b ∧ ∀ b' ∈ blocks, b ≠ b' → a ∉ b')

def coe_of_setoid [setoid α] : partition α := 
{ blocks := {t | ∀ (s₁ s₂), s₁ ∈ t → s₂ ∈ t → s₁ ≈ s₂ },
  empty_not_mem_blocks := sorry,
  blocks_partition := sorry }
```
I can't seem to prove that the empty set isn't contained in `blocks`. I also tried `blocks :=  {t | ∃ a, s ∈ t → a ≈ s}` without success.

#### [ Mario Carneiro (Oct 07 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333262):
`blocks := {t | ∃ a, {b | a ≈ b} = t}`

#### [ Mario Carneiro (Oct 07 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333265):
You can also write this as the range of a function

#### [ Mario Carneiro (Oct 07 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333318):
> `blocks :=  {t | ∃ a, s ∈ t → a ≈ s}`

This gives the set of subsets of some equivalence class

>  `blocks := {t | ∀ (s₁ s₂), s₁ ∈ t → s₂ ∈ t → s₁ ≈ s₂ }`

This gives the set of unions of equivalence classes

#### [ Mario Carneiro (Oct 07 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333360):
> `(empty_not_mem_blocks : blocks)`

The type on this isn't quite right...

#### [ Mario Carneiro (Oct 07 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333367):
But I don't think you should think much about this definition of partition. As far as possible you should just use equivalence relations

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333410):
Ah, thanks! I need to be more careful...

I do have `(empty_not_mem_blocks : ∅ ∉ blocks)`. I think I accidentally deleted it when I was  writing my previous message.

#### [ Mario Carneiro (Oct 07 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333420):
I would hope to be able to use `quot` to talk about equivalence classes, rather than sets

#### [ Mario Carneiro (Oct 07 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333422):
but that doesn't fit in this definition of partition

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333519):
OK, so I should just try to define poset / lattice instances on `setoid α`.

#### [ Mario Carneiro (Oct 07 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333682):
yes, that should work

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135335317):
This works:
```lean
instance : has_subset (setoid α) :=
⟨λ r₁ r₂, ∀ (a : α), let r1 := r₁.r in let r2 := r₂.r in {b | r1 a b} ⊆ {b | r2 a b}⟩
```
This fails:
```lean
instance a22 : has_subset (setoid α) :=
⟨λ r₁ r₂, ∀ (a : α), {b | r₁.r a b} ⊆ {b | r₂.r a b}⟩
/- invalid field notation, function 'setoid.r' does not have explicit argument with type (setoid ...) -/
```
Anyone know why?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135336689):
Usually the `simp` proves these equalities between structures, but not this time:
```lean
theorem setoid_eq_iff_r_eq : ∀ {r₁ r₂ : setoid α}, r₁ = r₂ ↔ r₁.r = r₂.r
| ⟨r1, e1⟩ ⟨r2, e2⟩
:= begin
  simp,
  sorry
end
```
What's the right way to do this? I don't know how to project out what I want from the equality `r₁ = r₂` between setoid structures.

#### [ Simon Hudon (Oct 07 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337108):
You can use `cases` on `r1`, `r2`, split the equivalence and use `cases` on the equality assumption in both cases.

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337309):
Thanks. Did you mean something like this?
```lean
theorem eq_iff_r_eq : ∀ {r₁ r₂ : setoid α}, r₁ = r₂ ↔ r₁.r = r₂.r
| ⟨r1, e1⟩ ⟨r2, e2⟩
:= begin
  intros,
  split,
  { intro h,
    cases h, },
  {  }
end
```
I'm getting a rather unhelpful error: `cases tactic failed, unexpected failure when introducing auxiliary equatilies`.

#### [ Simon Hudon (Oct 07 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337320):
That's odd. Try `injection h`, maybe that'll work

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337464):
Yep, that worked. I don't know how to use `cases` in the second case though, since now the equality between structures is now in the goal.

#### [ Simon Hudon (Oct 07 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337504):
you can do `subst h`

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337558):
`intro h, subst h` gives this error:
```lean
subst tactic failed, hypothesis 'h' is not of the form (x = t) or (t = x)
state:
α : Type u_1,
eq_iff_r_eq : ∀ {r₁ r₂ : setoid α}, r₁ = r₂ ↔ @r α r₁ = @r α r₂,
r1 : α → α → Prop,
e1 : @equivalence α r1,
r2 : α → α → Prop,
e2 : @equivalence α r2,
h : @r α (@mk α r1 e1) = @r α (@mk α r2 e2)
⊢ @mk α r1 e1 = @mk α r2 e2
```

#### [ Simon Hudon (Oct 07 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337605):
What if you do `dsimp at h` first?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337610):
Ah, perfect! Thanks so much!

#### [ Simon Hudon (Oct 07 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337663):
:+1:

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135340678):
[Here's](https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean) the WIP complete lattice instance on setoids. I've completed the poset stuff and inf, top, bot but not much else, so a lot of the theorems are just broken skeletons from e.g. data.set.basic.

Is there a clean way of defining the sup / union / join operation? This boils down to something like two elements a z are equivalent in the transitive closure of r1 and r2 if there exists a finite chain of equivalences r1 a b, r2 b c, r1 c d, ... , r_ y z.

#### [ Simon Hudon (Oct 07 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135340789):
Aren't the relations in the setoid equivalences? They should be already transitive, symmetric and reflexive. sup and inf of `f : a -> b -> b -> Prop` should be `λ x y, ∃ i, f i x y` and `λ x y, ∀ i, f i x y` respectively

#### [ Mario Carneiro (Oct 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135340915):
Note that `eqv_gen` will allow you to take the "span" of an arbitrary relation, so you can just union up a bunch of things and take the span for the supremum

#### [ Simon Hudon (Oct 07 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341333):
What's the span of a relation?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341672):
@**Simon Hudon** I'm not sure I understand. I guess your `f` is a family of equivalence relations indexed by `a`? I think your inf agrees with [what I have](https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L87), but I don't think your sup is the correct one. Consider the following two equivalence relations r1 and r2 on the nats, the equivalence classes of r1 are {0,1}, {2,3}, {4,5}, ... and the equivalence classes of r2 are {0}, {1,2}, {3,4}, {5,6}, ....  The sup of r1 and r2 has only one equivalence class equal to nat, so in particular 0 is equivalent to 1000, but you need a very long chain of r1 and r2 relations to witness it.

#### [ Mario Carneiro (Oct 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341680):
`eqv_gen` is the equivalence closure of a relation, this is what Bryan wants

#### [ Mario Carneiro (Oct 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341740):
Because equivalence relations are closed under arbitrary intersection, you can construct a generic "span" function that gets the smallest equivalence relation including some specified relation, and `eqv_gen` is this

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341836):
Thanks Mario! `eqv_gen` looks promising. It will probably take me some time to figure out how to use it though.

#### [ Mario Carneiro (Oct 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341919):
In your case I think you want to take the `eqv_gen` of Simon's relation `λ x y, ∃ i, f i x y`

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342114):
OK great, I think I'm starting to get it. I think I would have never found this definition on my own.

#### [ Mario Carneiro (Oct 07 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342177):
Note that it's not required to use that definition, and indeed there is a more "abstract nonsense" definition that makes the proof obligations easier. Define the intersection of an arbitrary indexed family of equivalence relations using Simon's definition; it is straightforward to show this is an equivalence relation. From this, you can define every other element of the complete lattice structure, the inf, the sup, the Sup, the top and bot

#### [ Simon Hudon (Oct 07 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342226):
Do you use "abstract nonsense" interchangeably with category theory?

#### [ Mario Carneiro (Oct 07 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342301):
in this case it's lattice theory

#### [ Mario Carneiro (Oct 07 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342337):
but I guess posets are categories, so sure

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342344):
So I see that the intersection works, but how do I get the union from it? Would I have to define it using the finite chains of relations manually?

#### [ Simon Hudon (Oct 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342950):
I haven't looked at that function too closely but I think you could take the union as I defined it and take its transitive, symmetric, reflexive closure

#### [ Simon Hudon (Oct 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342951):
Does that make sense?

#### [ Kevin Buzzard (Oct 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342999):
```quote
Do you use "abstract nonsense" interchangeably with category theory?
```
This is the most common usage of the phrase "abstract nonsense" when you see it in the mathematical literature, but the category theory in question can range from a simple diagram chase to the adjoint functor theorem and possibly beyond.

#### [ Mario Carneiro (Oct 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343827):
You don't need to take any reflexive symmetric closures with the approach I suggested

#### [ Mario Carneiro (Oct 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343837):
Given an intersection construction, you can define the supremum as the intersection of all equivalence classes containing the inputs

#### [ Patrick Massot (Oct 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343843):
(deleted)

#### [ Simon Hudon (Oct 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343905):
But what about the union?

#### [ Mario Carneiro (Oct 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343945):
that is the union

#### [ Mario Carneiro (Oct 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343949):
i.e. `a \sqcup b = Inf {s | a <= s /\ b <= s}`

#### [ Mario Carneiro (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343955):
similarly for arbitrary union

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343958):
```quote
Given an intersection construction, you can define the supremum as the intersection of all equivalence classes containing the inputs
```
Typo here? Should the supremum be defined in terms of the union of [...]

#### [ Mario Carneiro (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343962):
no

#### [ Mario Carneiro (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343971):
Think of it as an approximation of the union "from above"

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344018):
Ah, OK.

#### [ Mario Carneiro (Oct 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344019):
the union is the LEAST upper bound, so you can just take the infimum of upper bounds

#### [ Kenny Lau (Oct 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344079):
are there any `sorry` that I can fill?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344146):
Feel free to consider any broken proof in my files as a sorry. I'm not actively working on it at the moment.

#### [ Kenny Lau (Oct 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344231):
do I need to compile for 1 hour to find out which proof is broken?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344301):
Ah, OK. Well `inter_subset_right`, `inter_subset_left`, `subset_inter` are broken but the statements should be right. You can just delete their proofs and fill them in. Let me see if there are others.

#### [ Kenny Lau (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344303):
again, I need to compile for 1 hour to build this branch

#### [ Kenny Lau (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344306):
so I don't really know what I can do

#### [ Kenny Lau (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344308):
how do other people work on this branch?

#### [ Kenny Lau (Oct 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344350):
how does @**Simon Hudon** work on this branch?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344402):
I guess we've all got faster computers? It takes my computer about 10 minutes to compile mathlib.

#### [ Kenny Lau (Oct 07 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344423):
do you have 24 threads?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344477):
The Activity monitor says lean is using 14 right now. I just started another build after switching branches. Let's see how long it takes.

#### [ Kenny Lau (Oct 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344480):
can't you see how many threads you have?

#### [ Kenny Lau (Oct 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344635):
[2018-10-07.png](/user_uploads/3121/8KeKjpR28C3y92LYg_XEHFbR/2018-10-07.png)

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344636):
Do you mean threads across all processes? It's something like 1800 threads and 360 processes. I'm on a 6 core macbook pro.

#### [ Kenny Lau (Oct 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344642):
I have 2 cores and 4 threads

#### [ Kenny Lau (Oct 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344643):
I'm on a windows surface

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344780):
That's really amazing. I'm sure the surface has its advantages. 

Oh yeah, you can now bind a key to toggle the infoview live updating in the VS code extension, in case you want to pause the tactic state while lean is busy. It's `lean.infoview.toggleUpdating` in the keyboard shortcuts.

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344793):
This branch seems to be all kinds of screwed up. There's something wrong in `data.finset` that I have to look at.

#### [ Kenny Lau (Oct 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344845):
```quote
That's really amazing. I'm sure the surface has its advantages. 
```
I guess it isn't designed to build lean

#### [ Mario Carneiro (Oct 07 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135345229):
Yes, an ultrabook is not intended for heavy workstation programming

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135345608):
tutorial should now build properly. `order.partitions` is also filled out with sorries, so it should be more clear what's missing.

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135359879):
[Here's my definition for union using `eqv_gen`](https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L68) (is this right?).  Now this is what I need to show `union_subset` (forgive any typos introduced by my manual prettifying...):
```lean
α : Type u_1,
r₁ r₂ r₃ : setoid α,
a : α,
r1 : α → α → Prop :=
  @eqv_gen α (λ (s₁ s₂ : α), @r α r₁ s₁ s₂ ∨ @r α r₂ s₁ s₂),
r2 : α → α → Prop := @r α r₃,
x : α,
a_1 : r1 a x,
h23 : ∀ (y : α), @r α r₂ a y → r2 a y,
h13 : ∀ (y : α), @r α r₁ a y → r2 a y
⊢ r2 a x
```
Here's a very informal argument: `a_1` tells us that there's some finite chain of r₁  and r₂ equivalences between a and x, and and we then repeatedly apply h13 and h23 to each of the links of that chain to win. How do I do this?

#### [ Kevin Buzzard (Oct 07 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365476):
I have only half-been paying attention to this thread (and indeed Zulip) but I have a little time before bed. You're trying to prove that if r,s,t are three equivalence relations on a set, and both s and t are subsets of r, then the equivalence relation generated by s and t is a subset of r, right? Do you have that if x is a random relation contained in an equivalence relation r then the equivalence relation generated by x is also contained in r? It's trivial from this, right?

#### [ Kevin Buzzard (Oct 07 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365488):
I'm asking if we have the universal property of "equivalence relation generated by".

#### [ Kenny Lau (Oct 07 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365545):
you mean `rec_on`

#### [ Kevin Buzzard (Oct 07 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365546):
This would be trivial if you knew that the equivalence relation generated by an arbitrary relation was equal to the intersection of all the equivalence relations containing this relation. Sorry I'm late to the party; there's a lot of other noise in this thread too.

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365653):
I think I can do what I want with [`relation.eqv_gen_mono`](https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L367). That might be the same thing that you're saying.

#### [ Kevin Buzzard (Oct 07 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365655):
Kenny you're right

#### [ Kevin Buzzard (Oct 07 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365667):
Is the question "how do I fill in the sorry here: https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean#L110 "?

#### [ Kevin Buzzard (Oct 07 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365716):
If so, I am suggesting that you first prove that for an arbitrary relation x and an equiv reln r, x is a subset of r iff the equiv reln generated by x is a subset of r

#### [ Kevin Buzzard (Oct 07 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365717):
and then the union thing is a triviality

#### [ Kevin Buzzard (Oct 07 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365728):
and Kenny is suggesting that that the universal property of the relation is just the recursor

#### [ Kevin Buzzard (Oct 07 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365730):
so this should be hopefully straightforward.

#### [ Kevin Buzzard (Oct 07 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365733):
Do you want me to try or am I answering the wrong question @**Bryan Gin-ge Chen** ?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365828):
Yes, that was the question. I think I've solved it just now though:
```lean
theorem union_subset {r₁ r₂ r₃ : setoid α} (h13 : r₁ ⊆ r₃) (h23 : r₂ ⊆ r₃) : r₁ ∪ r₂ ⊆ r₃ :=
begin
  rw [subset_def] at h13 h23 ⊢,
  simp only [set.subset_def, set.mem_set_of_eq] at h13 h23 ⊢,
  rw [union_def, rel_union],
  intros,
  have hor : ∀ a x, @r α r₁ a x ∨ @r α r₂ a x → @r α r₃ a x := by { intros a x h,
    exact or.elim h (h13 a x) (h23 a x) },
  have H := relation.eqv_gen_mono hor a_1,
  have h := (@relation.eqv_gen_iff_of_equivalence _ r₃.r a x r₃.2).mp,
  exact h H
end
```

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365891):
I think `relation.eqv_gen_mono` is this property you are describing. And it does appear to me to be proved in the way you guys are suggesting. Thanks for the explanation though, without it, I was probably just going to go on not really understanding what was happening under the hood here!

#### [ Kevin Buzzard (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366475):
@**Kenny Lau** why did this come out so horrible:

```lean
lemma sub_of_gen_sub (x : α → α → Prop) (s : setoid α) (H : ∀ a b : α, x a b → @setoid.r _ s a b) :
∀ a b : α, (eqv_gen x) a b → @setoid.r _ s a b := 
λ a b H2, eqv_gen.rec_on H2 H 
  (@setoid.iseqv α s).1 
  (λ x y _ H3, (@setoid.iseqv α s).2.1 H3) 
  (λ x y z _ _ H4 H5,(@setoid.iseqv α s).2.2 H4 H5)
```

#### [ Kevin Buzzard (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366478):
Oh it's because I should be using a typeclass

#### [ Kenny Lau (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366479):
what do you mean by terrible?

#### [ Kenny Lau (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366480):
oh

#### [ Kevin Buzzard (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366518):
I didn't use typeclasses because I could see I'd have two equiv relns on alpha

#### [ Kenny Lau (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366530):
well it's a lemma

#### [ Kenny Lau (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366531):
the typeclass is local

#### [ Kenny Lau (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366578):
```lean
lemma sub_of_gen_sub {α : Type*} (x : α → α → Prop) [setoid α] (H : ∀ a b : α, x a b → a ≈ b) :
∀ a b : α, (eqv_gen x) a b → a ≈ b :=
λ a b H2, eqv_gen.rec_on H2 H
  setoid.refl
  (λ _ _ _, setoid.symm)
  (λ _ _ _ _ _, setoid.trans)
```

#### [ Kevin Buzzard (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366588):
@**Bryan Gin-ge Chen** it's not mono, this is a slightly longer way around isn't it? Mono says if x sub y then the equiv reln gen by x is a subset of the equiv reln generated by y. To get the universal property from that you also need that the equiv reln generated by an equiv reln is itself, which is another lemma

#### [ Kenny Lau (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366590):
inb4 *galois insertion*

#### [ Kevin Buzzard (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366594):
rofl

#### [ Kevin Buzzard (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366599):
I can quite believe it.

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366600):
Right, you can see I had to use `relation.eqv_gen_iff_of_equivalence`.

#### [ Kevin Buzzard (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366601):
although it might be a coinsertion

#### [ Kevin Buzzard (Oct 07 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366602):
With `sub_of_gen_sub` (which is a relatively straightforward consequence of the recursor) the proof is simpler.

#### [ Kevin Buzzard (Oct 07 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366644):
The lemma reduces you to checking that if X and Y are subsets of Z then so is X union Y, which will be in the library

#### [ Kenny Lau (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366692):
I don't really understand

#### [ Kevin Buzzard (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366694):
It wouldn't surprise me if `sub_of_gen_sub` is already in the library, perhaps under a better name.

#### [ Kenny Lau (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366695):
this is just the preimage of the canonical embedding from the set of equivalence relations on A to P(A x A)

#### [ Kevin Buzzard (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366698):
yes

#### [ Kevin Buzzard (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366704):
Bryan is using subset notation in exactly this way

#### [ Kenny Lau (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366705):
but he's not proving things this way

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366706):
I did a search for `eqv_gen` in mathlib and it only showed up in `logic.relation` and Kenny's free group file.

#### [ Kevin Buzzard (Oct 07 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366750):
Kenny I'm sure both Bryan and I would be interested if you were to blow his code out of the water using a more high-powered way of thinking about this question.

#### [ Kenny Lau (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366765):
blow his code out of the water?

#### [ Kevin Buzzard (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366766):
Bryan, do you know what a Galois insertion is?

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366782):
I'm about to have dinner, so I'll push what I have. Feel free to make arbitrary changes if you're willing to deal with the compile times.

I was just about to ask whether I ought to know about Galois (co)insertions...

#### [ Kevin Buzzard (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366814):
So the idea is that the construction sending a random relation to an equivalence relation is an adjoint to the forgetful functor sending an equivalence relation to the underlying relation

#### [ Kenny Lau (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366817):
```quote
Kenny I'm sure both Bryan and I would be interested if you were to blow his code out of the water using a more high-powered way of thinking about this question.
```
I still don't know what the question is

#### [ Kevin Buzzard (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366820):
https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean

#### [ Kevin Buzzard (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366822):
Prove all the lemmas there but in a much better way

#### [ Kevin Buzzard (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366825):
That's the question

#### [ Kevin Buzzard (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366826):
I think

#### [ Kevin Buzzard (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366884):
But the point is that you have something else here too -- these aren't just a pair of adjoint functors, because these are on posets (ordered by inclusion) and not just categories.

#### [ Kenny Lau (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366890):
well give me an hour to compile the mathlib first...

#### [ Kenny Lau (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366891):
I've changed some of the files

#### [ Kevin Buzzard (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366893):
So there's a special name for this situation, called a Galois insertion.

#### [ Kenny Lau (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366901):
so every time I change some files I need to spend one hour compiling the files

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366903):
And there's a bunch of lemmas proved about Galois insertions which might make these sorts of arguments easier.

#### [ Kenny Lau (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366910):
and in this hour my CPU will be fully used

#### [ Kenny Lau (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366914):
and the computer will be mostly unusable

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366917):
Kenny if you are only working on one branch which isn't master

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366920):
then you should just commit the olean files to master :P

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366924):
then whenever you checkout master again, the olean files will reappear

#### [ Patrick Massot (Oct 07 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366967):
Kenny and Kevin, you should pay attention to what Simon is writing in the nextdoor thread

#### [ Kevin Buzzard (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366974):
Kenny should -- I can compile mathlib in 10 minutes and I never fiddle with it anyway ;-)

#### [ Kevin Buzzard (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366981):
well...hardly ever

#### [ Kenny Lau (Oct 07 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135367165):
do all of you have like 30 cores?

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368008):
```quote
And there's a bunch of lemmas proved about Galois insertions which might make these sorts of arguments easier.
```
Are these lemmas in mathlib? There doesn't seem to be anything named `galois*`.

#### [ Kenny Lau (Oct 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368009):
`galois.*`?

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368011):
Oh oops, I was trying to search  the community fork.

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368163):
I remember reading about Galois connections whenever I learned about covering spaces. I don't remember insertions and coinsertions but the lean file seems clear enough.

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369030):
OK, I see the point now! The smart way to do all of this is to just use `lift_complete_lattice` on the complete lattice instance on subsets. Presumably that's what Kenny is up to now that an hour has passed. :)

#### [ Kenny Lau (Oct 08 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369082):
oh well I proved this

#### [ Kenny Lau (Oct 08 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369083):
```lean
import order.complete_lattice data.fintype

open lattice

instance bounded_lattice.of_fintype_inhabited_lattice
  (α : Type*) [fintype α] [inhabited α] [lattice α] :
  bounded_lattice α :=
{ top := finset.fold (⊔) (default α) id finset.univ,
  le_top := begin
    suffices : ∀ a ∈ finset.univ, a ≤ finset.fold (⊔) (default α) id finset.univ,
      from λ x, this x (finset.mem_univ x),
    generalize : finset.univ = U,
    cases U with U hu1,
    induction U using quot.ind with L,
    induction L with hd tl ih,
    { exact λ _, false.elim },
    intros x hx,
    rcases hx with rfl | hx,
    { exact le_sup_left },
    transitivity,
    { exact ih (list.nodup_of_nodup_cons hu1) x hx },
    { exact le_sup_right }
  end,
  bot := finset.fold (⊓) (default α) id finset.univ,
  bot_le := begin
    suffices : ∀ a ∈ finset.univ, finset.fold (⊓) (default α) id finset.univ ≤ a,
      from λ x, this x (finset.mem_univ x),
    generalize : finset.univ = U,
    cases U with U hu1,
    induction U using quot.ind with L,
    induction L with hd tl ih,
    { exact λ _, false.elim },
    intros x hx,
    rcases hx with rfl | hx,
    { exact inf_le_left },
    transitivity,
    { exact inf_le_right },
    { exact ih (list.nodup_of_nodup_cons hu1) x hx }
  end,
  .. (infer_instance : lattice α) }
```

#### [ Kenny Lau (Oct 08 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369135):
and realized that proving it is a complete lattice is impossible

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369151):
Oh are you working on `tutorial/partitions.lean` or `order/partitions.lean`?

#### [ Kenny Lau (Oct 08 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369193):
what is the difference?

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369199):
`tutorial/partitions.lean` was my first try on finite sets. Mario told me I should do stuff with general sets and then specialize, so I made `order/partitions.lean`.

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369238):
Is the issue with finite partitions that `Sup` and `Inf` need to use `set`?

#### [ Kenny Lau (Oct 08 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369296):
I think we should have an instance of `\Pi [fintype \a], bounded_lattice (finset \a)`

#### [ Kenny Lau (Oct 08 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369504):
```quote
Is the issue with finite partitions that `Sup` and `Inf` need to use `set`?
```
yes

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369556):
That's unfortunate. There should be a version of `complete_lattice` that works for finsets. Is that what your instance above does?

#### [ Kenny Lau (Oct 08 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369571):
no, that's `bounded_lattice`

#### [ Kenny Lau (Oct 08 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369573):
I don't think you can prove `complete_lattice`.

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369687):
Partitions of finite sets have a complete lattice structure just as much as partitions of arbitrary sets do, so we should add `complete_lattice_finset`.

#### [ Kenny Lau (Oct 08 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369731):
I don't think so.

#### [ Jeremy Avigad (Oct 08 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369738):
@**Kevin Buzzard** I am sorry to be slow to respond to your ping, but I have thought about it and I don't have any great insights here. I don't think the notion of a canonical isomorphism is a sharp concept, and your post gives as good a working definition as any. It would be nice to have automation the finds/constructs them for you.

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369842):
@**Kenny Lau** Why not?

#### [ Kenny Lau (Oct 08 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369846):
because given an arbitrary set of partitions I don't see how you can find its supremum.

#### [ Kenny Lau (Oct 08 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369850):
let's just say our set is A = {0,1}

#### [ Kenny Lau (Oct 08 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369856):
I give you a set S of partitions of A

#### [ Kenny Lau (Oct 08 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369857):
how do you find the supremum of S?

#### [ Kenny Lau (Oct 08 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369902):
let's say S is {{{0},{1}}} if Goldbach conjecture is true and and {} otherwise.

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369979):
OK, but for finite partitions I only care about finsets of partitions which can't be that gross, right?

#### [ Kenny Lau (Oct 08 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369992):
but if you want to have a `complete_lattice` instance then you need to find the supremum for arbitrary sets

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370045):
So you're saying that there's not even `complete_lattice` on `setoid`, as I was aiming to prove in `order/partitions.lean`...

#### [ Kenny Lau (Oct 08 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370047):
you can always make a `noncomputable def` :)

#### [ Kenny Lau (Oct 08 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370048):
(don't make it an instance!)

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370296):
I think I'm starting to get it. Do you happen to know which part of the galois insertion between the partial order on equivalence relations and that on subsets of $$\alpha \times \alpha$$ is noncomputable?

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370318):
@**Mario Carneiro** What do you think about having a `complete_lattice_finset`?

#### [ Kenny Lau (Oct 08 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370319):
none of the parts

#### [ Mario Carneiro (Oct 08 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371718):
@**Kenny Lau** `Sup` and `Inf` are inherently noncomputable, just from their types: `set A -> A`

#### [ Mario Carneiro (Oct 08 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371721):
This means that they take in no data and produce data

#### [ Kenny Lau (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371723):
well `set (set A) -> set A` is computable though

#### [ Mario Carneiro (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371731):
pointlessly so

#### [ Mario Carneiro (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371734):
you can computabilize any definition of that type

#### [ Kenny Lau (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371738):
aha

#### [ Kenny Lau (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371739):
thanks

#### [ Johan Commelin (Oct 09 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448580):
@**Scott Morrison|110087** Do you know if Neil got Lean working in the end?

#### [ Johan Commelin (Oct 09 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448584):
@**Neil Strickland** Aah, you're on this Zulip. Can you confirm?

#### [ Johan Commelin (Oct 09 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448697):
I'm looking at the first "challenge", namely: prove `2 + 2 = 4`. Your goal with this challenge is
```quote
Key points: basic boilerplate at the top of the file, basic grammar of stating and proving, how to interact with the proof assistant.
```
But in Lean you won't learn that from `2 + 2 = 4`. In idiomatic Lean, a file dedicated to that lemma would contain 1 line:
```lean
lemma two_add_two : 2 + 2 = 4 := rfl
```
No imports, no boiler plate, no interactions, no nothing.

#### [ Scott Morrison (Oct 09 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448700):
I'm not really sure what state we left him in. At Dagstuhl he definitely had a working copy on the laptop he had with him, but that might not still be the case.

#### [ Johan Commelin (Oct 09 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448712):
I think the "Key points" deserve to be in a dedicated tutorial file. But I'm not sure if `2 + 2 = 4` is the right "goal" of that file.

#### [ Scott Morrison (Oct 09 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448758):
Well -- even that file teaches you a few things: the lemma keyword, colon, colon-equals. You could also explain the red and green underlines, and the fact that the absence of these shows Lean approves. (Or ... is just not even running...)

#### [ Tobias Grosser (Oct 09 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450223):
(deleted)

#### [ Tobias Grosser (Oct 09 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450243):
```quote
do all of you have like 30 cores?
```
@**Kenny Lau** , any reason you don't compile on a proper server?

#### [ Tobias Grosser (Oct 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450297):
If you don't have one available, I suggest you get an account at the GCC compile farm: "https://cfarm.tetaneutral.net"

#### [ Tobias Grosser (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450314):
They give accounts to open source contributors and have some servers that are commonly not too busy

#### [ Tobias Grosser (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450320):
gcc20	22, 443	Dual Xeon	x86_64	Intel(R) Xeon(R) CPU X5670 @ 2.93GHz	2 CPU
12 cores 24 threads	24105 MB	825.0 GB	Debian 7.11 wheezy
3.2.0-4-amd64	1090 days	INRIA Rocquencourt	France

#### [ Tobias Grosser (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450325):
Is mostly idle today.

#### [ Tobias Grosser (Oct 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450381):
If you can get lean compiled on powerpc hardware you can run on IBM Power8 with 160 CPUs

#### [ Tobias Grosser (Oct 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450385):
It's also at 99% idle ATM.

#### [ Mario Carneiro (Oct 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450516):
I've never heard of this option

#### [ Mario Carneiro (Oct 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450564):
Maybe there is a possibility we can set up Jenkins on it as an alternative to Travis?

#### [ Johan Commelin (Oct 09 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450973):
Here is what I just pushed for Challenge 1.
https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/two_add_two.lean

#### [ Johan Commelin (Oct 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451044):
I didn't do any tactics yet. So that should be done in Challenge 2 "Infinitude of primes".

#### [ Johan Commelin (Oct 09 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451447):
@**Neil Strickland** Would you mind adding a link to https://github.com/leanprover-community/mathlib/tree/tutorials/tutorials in you post on MO? Or is it ok with you if we edit the post while writing tutorials on the 5 challenges that you suggested?

#### [ Johan Commelin (Oct 09 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451645):
General question @**Mario Carneiro** @**Bryan Gin-ge Chen** should we leave active `#eval` and `#print` statements in these tutorials? Or should they be commented out, so that they don't spam ordinary mathlib-builds. I suppose it is easy enough for the user to uncomment them.

#### [ Mario Carneiro (Oct 09 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451694):
I'm not sure mathlib is the best place for them

#### [ Johan Commelin (Oct 09 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451700):
them what?

#### [ Mario Carneiro (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451706):
the tutorials

#### [ Johan Commelin (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451713):
I think it is

#### [ Mario Carneiro (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451716):
Especially if it is an interactive walkthrough

#### [ Johan Commelin (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451717):
Because it forces us to make sure they compile

#### [ Mario Carneiro (Oct 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451773):
I don't know, I mean TPIL has code snippets and they only break occasionally, and it is reported and fixed

#### [ Mario Carneiro (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451785):
It's not like they are going to be based on really complicated things

#### [ Johan Commelin (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451801):
```quote
It's not like they are going to be based on really complicated things
```
One of the challenges is on nilpotent ideals... it would break helplessly by your module refactor.

#### [ Mario Carneiro (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451848):
They could just as easily be in a separate project. Even better, if a user downloads the tutorial project depending on mathlib then they are already in the right place to do work of their own

#### [ Kenny Lau (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451861):
```quote
One of the challenges is on nilpotent ideals... it would break helplessly by your module refactor.
```
what do you mean?

#### [ Mario Carneiro (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451871):
I'm not saying they never change, but they won't change often

#### [ Johan Commelin (Oct 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451884):
@**Kenny Lau** https://mathoverflow.net/a/311159/21815

#### [ Kenny Lau (Oct 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451939):
yes?

#### [ Johan Commelin (Oct 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451954):
That's homework for us (-;

#### [ Scott Morrison (Oct 09 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135454675):
I'd be pretty happy to see tutorials embedded in mathlib for now. Anything to avoid useful stuff bit-rotting away. :-)

#### [ Sean Leather (Oct 09 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455291):
I agree that tutorials should go into in mathlib. I think that, as long as the plan is to keep mathlib monolithic (which seems to be working out for the most part), it should include tutorials. A reasonable alternative is to build a tutorial repository during mathlib's CI test phase.

#### [ Mario Carneiro (Oct 09 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455714):
I still think it is a good idea to have a "scratch" repo that newbies can get to have a working setup in vscode with mathlib already hooked in, since this is the recommended use

#### [ Johan Commelin (Oct 09 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455740):
What do you mean with "recommended use"?

#### [ Mario Carneiro (Oct 09 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455751):
I mean this is the way third parties use mathlib

#### [ Mario Carneiro (Oct 09 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455802):
you have a project, and this project imports mathlib

#### [ Mario Carneiro (Oct 09 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455809):
this is the format vscode is expecting

#### [ Mario Carneiro (Oct 09 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455831):
You can have mathlib as a global install and work with loose files, but I think this approach is less robust

#### [ Johan Commelin (Oct 09 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455852):
Right, but I'm more thinking about mathematicians that want to contribute to mathlib

#### [ Mario Carneiro (Oct 09 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455859):
contributing to mathlib is another thing altogether

#### [ Johan Commelin (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455901):
So they will end up hacking on the community fork asap

#### [ Mario Carneiro (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455909):
sure, in that case they are working on mathlib itself so there is already a project

#### [ Mario Carneiro (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455916):
I mean for new leaners, like the kids in Kevin's classes

#### [ Johan Commelin (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455917):
Right, and they get to know that project by looking in `tutorials/`

#### [ Scott Morrison (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455933):
A scratch project is a good idea.

#### [ Johan Commelin (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455938):
I see. Well, I was more thinking about people like Neil.

#### [ Mario Carneiro (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455947):
I don't think Neil was ready to be a contributor

#### [ Scott Morrison (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455951):
Just the bare minimum setup, with perhaps a file that reminds them where to go for more help.

#### [ Mario Carneiro (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455966):
I assume people start out with projects on their own for a while, and then move to contribution if they are so inclined

#### [ Johan Commelin (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455967):
https://github.com/leanprover-community/hello-world

#### [ Scott Morrison (Oct 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456022):
And as Lean/mathlib improves, we actually hope a larger and larger fraction of the community are _not_ hacking on mathlib!

#### [ Johan Commelin (Oct 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456026):
Why?

#### [ Johan Commelin (Oct 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456031):
I thought we wanted to be a massive monolith

#### [ Scott Morrison (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456033):
(because they're actually doing maths, rather than filling in all the gaps before they can actually get started)

#### [ Sean Leather (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456040):
There's ambiguity in the word “tutorial.” I was thinking of something more like a walkthrough of various features of mathlib. But a scratch/hello-world repository would also be useful.

#### [ Johan Commelin (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456045):
@**Scott Morrison|110087** But why not do maths inside mathlib?

#### [ Scott Morrison (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456047):
If I'm going to formalise a bunch of the boring-but-technical lemmas in my research paper, they don't belong in mathlib.

#### [ Mario Carneiro (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456049):
@**Sean Leather**  I guess Kevin's mathlib docs pages already do that?

#### [ Scott Morrison (Oct 09 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456127):
or because they're working out the lemmas for their research project. They don't belong in mathlib because they've got no idea if they're the right lemmas yet. But this is all dreaming. For the next couple of decades, I agree, all in mathlib. :-)

#### [ Sean Leather (Oct 09 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456195):
```quote
I guess Kevin's mathlib docs pages already do that?
```
Not in the sense that you can see examples in Lean of what is provable and how with mathlib.

#### [ Sean Leather (Oct 09 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456299):
Perhaps I'm off-topic here with my own definition of tutorial — I'm not sure — but I was thinking of something that demonstrated usage of mathlib with proofs and words, not *just* words.

#### [ Johan Commelin (Oct 09 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135457779):
@**Sean Leather** I think we can have both

#### [ Sean Leather (Oct 09 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135457873):
@**Johan Commelin** Yep, we probably should.

#### [ Kevin Buzzard (Oct 09 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135482607):
The Xena.zip file which I was going to use with my 1st years this year (until ICT delivered something much better) -- that was precisely what Mario was describing above. The way this seems to work is that once a year I am allowed to update what the Imperial College undergraduates see by default when they open up VS Code. This year they see a project with one file `test.lean` containing `import data.int.basic theorem 2+2=4:=rfl` and then all the lean and olean files for mathlib and lean (with mathlib as a dependency). This is what I would now call "the bare minimum for mathematicians who are interested". But it sounds like the community might be able to make a much better variant of this, which we could just generally advertise on GH. I think it's worth stressing that win10 users have no git and no command line, and I've met plenty of people who just want to get going. We make a better repo, and we replace Xena.zip with this repo and I document it on the installation page and people will be happier.


{% endraw %}
