---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96591proposalforbackwardsreasoning.html
---

## [general](index.html)
### [proposal for `backwards_reasoning`](96591proposalforbackwardsreasoning.html)

#### [Scott Morrison (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383465):
I'd like to propose an interactive partner for `solve_by_elim`. The idea is that it will be a tool for applying "backwards reasoning" (i.e. applying lemmas against the goal).

The idea is that we'll tag certain lemmas with an attribute, perhaps `back`, that are "safe" for backwards reasoning. A good example would be `min_fac_dvd : ∀ (n : ℕ), min_fac n ∣ n`. If you can unify that conclusion with the goal, you can't possibly be unhappy --- the only parameters are determined by unification, so no new goals can appear.

`backwards_reasoning [x, y, z]`, will apply all lemmas marked with `@[back]` against the goal, as well as applying x, y, z. It will then apply `solve_by_elim` afterwards (so also applying all hypotheses). The key difference from just using `solve_by_elim` is that `backwards_reasoning` will succeed even if it doesn't close the goal, as long as it manages to apply at least one of the specified lemmas.

Here's an example of it in action:

#### [Scott Morrison (Oct 08 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383576):
```
import data.nat.prime
import tactic.backwards_reasoning

open nat

-- These are all lemmas which it is sufficiently safe to `apply` 
-- that they can be automatically applied by backwards_reasoning.
attribute [back] succ_lt_succ
                 fact_pos dvd_fact
                 min_fac_prime min_fac_dvd 

theorem infinitude_of_primes (N : ℕ) : ∃ p ≥ N, prime p :=
begin
  let M := fact N + 1,
  let p := min_fac M,
  have pp : prime p, sorry,
  sorry,
```
Now we replace that first `sorry` with `backwards_reasoning`, and the goal `prime p` is replaced with `M \neq 1`.
(If we replace `backwards_reasoning` with `backwards_reasoning#`, it prints out what it did: `apply min_fac_prime`.)

We then realise that a good way to proceed is`apply ne_of_gt`, so we modify the tactic to `backwards_reasoning [ne_of_gt]`.
This succeeds, discharging the goal! If we replace the tactic with `backwards_reasoning# [ne_of_gt]`, it prints what it did:
`exact min_fac_prime (ne_of_gt (succ_lt_succ (fact_pos N)))`.

If you prefer you can then copy and paste that output, replacing entirely the call to `backwards_reasoning`.

#### [Scott Morrison (Oct 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383595):
(The rest of the proof of `infinitude_of_primes` can be proved in the same style.)

#### [Johan Commelin (Oct 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383599):
Looks really good @**Scott Morrison|110087**

#### [Kenny Lau (Oct 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383652):
looks like `inversion`™ in Coq

#### [Scott Morrison (Oct 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383661):
Having this be really useful requires some judicious tagging of lemmas with `back`. My suggestion to start off just by having a smattering of attributes added in the `tactics/backwards_reasoning.lean` file itself, and to consider later moving them to the point of definition if it seems useful.

#### [Scott Morrison (Oct 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383731):
@**Kenny Lau**, can you point me to some examples? The documentation I found for [inversion](https://coq.inria.fr/refman/proof-engine/tactics.html) is not super helpful. :-(

#### [Kenny Lau (Oct 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383778):
[you're looking at the wrong part](https://coq.inria.fr/refman/proof-engine/tactics.html#coq:tacn.inversion)

#### [Kenny Lau (Oct 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383783):
> `inversion ident`

> Let the type of ident in the local context be (I t), where I is a (co)inductive predicate. Then, inversion applied to ident derives for each possible constructor c i of (I t), all the necessary conditions that should hold for the instance (I t) to be proved by c i.

#### [Scott Morrison (Oct 08 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383795):
Glad you like it, @**Johan Commelin**. :-) I may wait until I hear something from @**Simon Hudon** or @**Mario Carneiro** before I bother cleaning it up for a PR.

#### [Scott Morrison (Oct 08 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383796):
But in any case I'll need some version of it before I'm willing to PR my work on limits in category theory. :-)

#### [Kenny Lau (Oct 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383836):
and in any case one should be noted that I do not know Coq at all.

#### [Scott Morrison (Oct 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383850):
Ok. It seems in any case `inversion` in Coq is quite different; whatever exactly it's doing, it's only doing one step, it's not something that chains together a whole sequence of applications.

#### [Mario Carneiro (Oct 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383862):
I don't see what `inversion` has to do with it - `inversion` is the equivalent of lean `cases`

#### [Mario Carneiro (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383938):
How does `backwards_reasoning` select the lemmas to apply? Does it just go through the whole list every time?

#### [Mario Carneiro (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135383944):
also `backwards_reasoning` has way too many letters in it

#### [Scott Morrison (Oct 08 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384240):
Yes, it just runs through the whole list every time. I have not tested this at really big scale, but (a version of this) has been in my category theory library for a while, with maybe ~50 lemmas, and it never shows up in profiling. I think `apply` fails very fast.

#### [Mario Carneiro (Oct 08 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384254):
I think that if we used it in mathlib we would want to use it large scale, and then this would become a concern

#### [Scott Morrison (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384297):
```quote
also `backwards_reasoning` has way too many letters in it
```
I could rename it `br`, if you prefer. :-). How about just `back`?

#### [Mario Carneiro (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384308):
indeed I get the sense that it's not very useful unless it is marked everywhere

#### [Sebastien Gouezel (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384311):
If I understand correctly, you're creating a version of `apply_rules` on steroids, with additionally a set of default rules to be applied, right?

#### [Scott Morrison (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384317):
That sounds about right.

#### [Mario Carneiro (Oct 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384321):
I admit I don't understand `apply_rules` usage

#### [Scott Morrison (Oct 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384327):
(I have not used apply_rules, but I've seen the implementation.)

#### [Scott Morrison (Oct 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384338):
I guess we could have 'sub-attributes', to mark lemmas as relevant in certain domains.

#### [Scott Morrison (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384396):
The other solution is just to accept that `backwards_reasoning` is a slow tactic, and you're meant to switch to `backwards_reasoning#` once you've discovered the proof, and copy-paste the trace output.

#### [Scott Morrison (Oct 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384409):
(And just not worry about slow tactics, because we all have 30 cores, right?)

#### [Sebastien Gouezel (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384528):
If you want to go even further in this direction, let me mention the syntax of the Isabelle swiss army knife `auto`. Some rules in Isabelle are marked `[intro]`, or `[intro!]` (the first one would be unsafe rules to be applied in backward reasoning, the second one for safe rules). In the same way there are simp rules. And all of this can be combined with
```
auto (simp: foo_simp, bar_simp, intro:  foo_intro, bar_intro)
```
which will apply eagerly the rules `foo_intro` or `bar_intro` and the rules marked `[intro!]` in the library (and also the `[intro]` ones if their assumptions can be checked right away), simplify everything using the simplifier with the additional rules `foo_simp` and `bar_simp`, and go over again. All this with some amount of backtracking that can be controlled. 90% of Isabelle proofs are `auto`proofs...

#### [Scott Morrison (Oct 08 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384636):
Thanks for this description, @**Sebastien Gouezel**!

#### [Scott Morrison (Oct 08 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384708):
My version of `tidy` in the category theory library has been using `backwards_reasoning` all along, and the main loop of `tidy` causes it to bounce back and forth between `backwards_reasoning` and `simp`. :-) Good to know I was re-inventing `auto`.

#### [Johan Commelin (Oct 08 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384713):
@**Sebastien Gouezel** And do those proofs remain `auto`, or do they get replaced by some unreadable proof that `auto` found? In other words: is this fast, and how does Isabelle solve the speed issues that we are hitting now in Lean?

#### [Scott Morrison (Oct 08 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384719):
(Of course, `tidy` does many other things in the loop, for better or worse.)

#### [Scott Morrison (Oct 08 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384780):
My private `backwards_reasoning` also makes the distinction analogous to `[intro]` vs `[intro!]`, but I haven't reimplemented that completely in the new backwards_reasoning I've just been describing.

#### [Sebastien Gouezel (Oct 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135384964):
```quote
@**Sebastien Gouezel** And do those proofs remain `auto`, or do they get replaced by some unreadable proof that `auto` found? In other words: is this fast, and how does Isabelle solve the speed issues that we are hitting now in Lean?
```
There are no speed issues in Isabelle. `auto` is extremely fast, but this is certainly related to the lack of dependent types and unification, which makes everything much simpler.

#### [Kevin Buzzard (Oct 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135385652):
Anyone who watched @**Scott Morrison|110087** 's video of his Adelaide talk will have seen a pretty stunning application of `backwards_reasoning`. It was very well-delivered too. He was formalising proof of infinitely many primes and getting his hands dirty. "Oh we'll just skip this", "oh we'll come back to this later", "Oh Ok so now we've proved there are infinitely many primes modulo 5 sorries which clearly are going to be the hard work", "oh look, globally replacing `sorry` with `backwards_reasoning` closes the goal!"

#### [Mario Carneiro (Oct 08 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135385811):
what do you mean lack of unification?

#### [Scott Morrison (Oct 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386143):
Okay, that demo in Adelaide was a bit misleading. Way too many things were marked `@[back]`, that in practice we couldn't avoid.

#### [Scott Morrison (Oct 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386148):
It's going to be a little while before `backwards_reasoning` or friends really does what it appeared to do there...

#### [Kevin Buzzard (Oct 08 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386584):
That doesn't matter. The point was made.

#### [Kevin Buzzard (Oct 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386607):
I will be doing the same thing in Sheffield; showing the audience how proving $$(x+y)^3=x^3+3x^2y+...$$ is really hard from the axioms and then solving it using automation

#### [Kevin Buzzard (Oct 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386652):
Mathematicians need to understand that doing simple maths might be simple in Lean.

#### [Kevin Buzzard (Oct 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386668):
The more we say it's true and the more we work on cases where it is not true (like $$A\cong B\to Spec(A)\cong Spec(B)$$) the more it will become true

#### [Kevin Buzzard (Oct 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135386691):
If it's easy in maths, we need to try and make it easy in Lean.

#### [Patrick Massot (Oct 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135388213):
I also liked the backward reasoning demo in Adelaide, but I struggled with the name. Of course I'm not a native English speaker but, to me, `backward_reasoning` sounds like we are doing something wrong (like using `P -> Q` to prove `P` from `Q`).

#### [Johan Commelin (Oct 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135394086):
How far are we from this turning into a PR?

#### [Scott Morrison (Oct 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135394249):
Close.

#### [Scott Morrison (Oct 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135394254):
But I have grumpy coauthors back in the real world. :-)

#### [Simon Hudon (Oct 08 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135406314):
Hi @**Scott Morrison|110087**! Sorry I got distracted by this sleeping thing. This looks really cool! I think we can do things much faster than going through the whole list of lemmas and we may not hit the performance wall that we did with simp. 

A bit like `simp`, we can index `back` lemmas using the head symbol of the rhs of its pi type. Then, the number of candidate at each step should be much smaller. I'd have to think some more about further optimizations but I think Isabelle suggests it must be possible to do things really fast

#### [Scott Morrison (Oct 09 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135436974):
Hi @**Simon Hudon**, indexing sounds great. How hard do you think this would be? I'm not confident I could implement it efficiently, but especially if you can give me a pointer to something similar I can give it a try. If I pushed a branch, I'd be very happy if you wanted to look at doing this.

#### [Scott Morrison (Oct 09 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135436986):
I also want to implement two attributes, analogous to [intro] and [intro!] in Isabelle, for lemmas that it's always safe to apply, vs lemmas that should only be applied if their hypotheses can immediately be solved. I already had this in my original implementation of `back`, but it's not in the current one. Perhaps I should do this first, and then we can think about indexing?

#### [Simon Hudon (Oct 09 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135437029):
Sure, no problems. You can also have a look at the user attribute for extensionality if you want to try it before I get into it

#### [Simon Hudon (Oct 09 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135437035):
Sure

#### [Simon Hudon (Oct 09 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135437056):
You can do one `intro` attribute and use `!` as a parameter

#### [Scott Morrison (Oct 10 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519236):
@**Simon Hudon** , can you point me to examples of using a token like `!` as a parameter to an attribute?

#### [Mario Carneiro (Oct 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519868):
`intro!` is an attribute

#### [Mario Carneiro (Oct 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519872):
but I think the parsing for that is in core

#### [Mario Carneiro (Oct 10 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519888):
The parsing for an attribute is just a regular `lean.parser` monad thing, so you can use `tk "!"?` to get a possible `!` token

#### [Mario Carneiro (Oct 10 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135519943):
If you want an example of an attribute with arguments, look at `to_additive_attr` in `algebra.group`. You specify the type of the parsed result in one of the optional arguments to `user_attribute`, and you give the parser itself in the `parser := ` field

#### [Scott Morrison (Oct 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal%20for%20%60backwards_reasoning%60/near/135520477):
Thanks. I've just made a PR at https://leanprover.zulipchat.com/#narrow/stream/144837-PR-reviews/subject/.23410.20backwards.20reasoning, so perhaps anything further on this thread can go there.

