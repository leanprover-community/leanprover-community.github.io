---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78790typeclassresolutionorunification.html
---

## Stream: [general](index.html)
### Topic: [type class resolution or unification?](78790typeclassresolutionorunification.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265237):
This question might be too vague to answer. I have a fixed type `X` and I am doing a lot of work with functions from `{U : set X // P U}` to `Type*` (for example, `X` might be a topological space and the functions might assign a type to each open set in `X`, but I also consider more general possibilities for `P`, e.g. `P` might say "`U` is in a fixed basis for the topological space"). I seem to have three different ways to set up such functions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265251):
1) I could look at functions on subtypes, as I wrote above. I don't do this. I think subtypes are messy and would be forever taking them apart.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265280):
2) I could define my functions as `lam {U} (H : P U), ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265322):
3) I could define my functions as `lam U [H : P U], ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265336):
I don't like (3) because it relies on the type class inference system and for my own types P it would rely on my getting the system to work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265360):
I used to be using (4) `lam U (H : P U)` but I just got sick of constantly writing U when it could be inferred from HU, so I just switched to (2).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265371):
I am now looking at (2) thinking "ugh, my functions are supposed to be eating open sets and they're now eating proofs, that looks a bit weird"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 18 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265469):
I like (2). Same number of arguments, but you don't have to rely on type classes. So long as you always have a proof of `P U` to hand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265532):
Are there any arguments for or against any of (1) to (4)? I am 99.9% convinced that I could get any of (1), (2) or (4) working. I simply don't know whether I could get (3) working; in my mind it would be by far the "riskiest" approach. These functions are everywhere in my code and I am constantly coming up with proofs that various sets have property `P`; in the case `P` is "I am an open set" then some of these are in mathlib. I would probably have to go around making a whole bunch of things instances, and even then I'm not convinced that I would be able to cover everything (e.g. these functions might show up as part of structures, where the proof of `P U` is somewhere else in the structure and I am not 100 percent convinced that type class inference can get me to it).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265593):
I used (4) for open sets and (2) for bases of open sets, and both worked fine, so I switched to (2) because it made my code shorter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265703):
...and possibly slightly less readable -- e.g. open sets like $$f^{-1}(V)$$ (which was easy to read) have now been removed and replaced by hypotheses like "I am a lemma in mathlib saying the pre-image of an open set under a continuous function is open".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265721):
On the other hand I am using type class inference for rings (the functions map open sets to rings) and sometimes it just doesn't work and it's easier to do the `@` dance than try to figure out why it didn't work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 18 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265734):
(1) has no advantages other than proving things like injectivity where the function has to be `α → β`, but I don't think you want to do that. (4) does have the advantage of readability. `some _` is a nightmare in this regard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265779):
@**Kevin Buzzard** it's amazing how we went from knowing nothing about type theory to having an opinion on them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265780):
yes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265784):
I've learnt so much this year.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265795):
the best way to learn maths is indeed to play with them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265805):
people just learn symbols without the meanings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265810):
(x+y)^2 = x^2+2xy+y^2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265811):
I am very much in two minds about whether I want my code to be readable though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265812):
means nothing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265819):
but whenever you are told to expand it, you go from left to right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265829):
here it means "about 6 invocations of the axioms of a ring" :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265831):
i think you should not worry too much about your code being readable in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265888):
i don't think there's any way to understand tactic mode without going through the proofs line by line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 18 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265901):
Technically Coq is all tactic mode and you can write readable proofs just fine :).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265962):
chlipala disagrees :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265965):
I think I read some quote by Paulson arguing that readability was super-important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265968):
and that's the biggest difference between the isabelle style and the coq style

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265970):
I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265972):
Adam Disagrees and then writes CPDT, which has yet to be deciphered :).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266045):
well, readability is definitely important, but do you want to make a second pass over all your proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266060):
you can write out many of the intermediate steps with show, have, and give many comments, and that is certainly great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266138):
The last big proof I wrote (compactness of a certain topological space), every few lines I wrote down what the goal was (in mathematical language) and what I was going to do next.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266142):
So "unreadable" proof but readable comments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266222):
in isabelle some authors go so far as to write a latex proof in the comments next to the formal derivation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266226):
in isabelle one forgets computability

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266580):
In the future there will be files which humans read which will look like beautifully typeset mathematics and which will unfold into computer-checked proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266586):
I hope to see it before I die.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266609):
perhaps... you have to wonder why coq and isabelle never took off. well, maybe people just need to be exposed to it more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Apr 18 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266776):
Speaking of readability, I just wrote a proof like that:
```lean
lemma eventually_bdd_above_iff_exists_eventually_le {F : filter α} {u : α → β} :
(eventually_bdd_above F u) ↔ (∃t, eventually (λn, u n ≤ t) F) :=
have A: eventually_bdd_above F u → (∃t, eventually (λn, u n ≤ t) F) :=
  assume ⟨su, suF, tu, tuH⟩,
  have eventually (λn, u n ≤ tu) F :=
  begin
    apply filter.upwards_sets F suF,
    assume (y) (Hy),
    apply tuH _ (mem_image_of_mem _ Hy)
  end,
  ⟨tu, by assumption⟩,
have B: (∃t, eventually (λn, u n ≤ t) F) → eventually_bdd_above F u :=
  assume ⟨t, Ht⟩,
  have bdd_above (u '' {y : α | u y ≤ t}) :=
  begin
    apply bdd_above.mk t,
    assume (y) (Hy),
    induction Hy with x Hx,
    simpa [Hx.2] using Hx,
  end,
  ⟨{y | u y ≤ t}, by assumption, by assumption⟩,
⟨A, B⟩
```
and then I compacted it to
```lean
⟨λ ⟨su, suF, tu, tuH⟩, ⟨tu, filter.upwards_sets F suF (λ y Hy, tuH _ (mem_image_of_mem _ Hy))⟩,
 λ ⟨t, Ht⟩, ⟨{y | u y ≤ t}, Ht, t, (λy Hy, let ⟨x, Hx⟩ := Hy in by simpa [Hx.2] using Hx)⟩⟩
```
Do you have an opinion on the readability of both, and which one I should keep?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266974):
@**Andrew Ashworth** They're reasonably well established in a few specific areas, almost exclusively related to software verification. Are you talking widespread adoption by mathematicians and in general, people who use formal apparatus of any kind?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267209):
i like non-compacted proofs, although the mathlib developers disagree with me :grinning:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267224):
I think it depends on your audience.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267229):
If you want to get it into mathlib then if you wrote the long one they would squish it down to the short one themselves

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267240):
If you want to explain to a bunch of undergraduates how Lean works then I would definitely not recommend the short one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267303):
there is plenty of space for big proofs in TPIL and similar works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267345):
@**Moses Schönfinkel** yes. it doesn't even have that many inroads into high-assurance software, which is all written in things like MISRA C

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267350):
For simple statements like this I prefer the later proof (btw: you can even reduce it more: `λy Hy, let ⟨x, Hx⟩ := Hy in  ~> λy ⟨x, Hx⟩,`). But the more complicated the proof itself is, especially when the proof goes over a couple of lines, I prefer the more elaborate one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267433):
In fact Johannes taught me a valuable lesson regarding this sort of thing (which you already know Sebastian) -- it's a very good exercise, at some point in your Lean career, to start trying to write the shortest proofs you possibly can.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267442):
because this game just teaches you stuff, or perhaps teaches you to appreciate certain things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267448):
which you might otherwise miss.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Apr 18 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267549):
Agreed. To be able to compactify the proof, I needed to understand much more of what is going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267682):
The problem with compact proofs is of course, that it is hard to ever change the definition of constants. As the often rely on definitional equality. There using automation has a big advantage, as it is often configurable like the simplifier.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267683):
compact proofs / programs are painful to me. as someone who was tasked with fixing an old scientific c program from the 80s for several months, terseness is the great enemy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267849):
What about having the goal that people could learn stuff from reading proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267852):
In ordinary maths this is a pretty important idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267932):
Of course we could completely separate the explanation of a theorem from its proof using Lean. But that wouldn't help people learning how to convince Lean that something is true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269848):
What about having the goal that in between the incomprehensible lines of Lean code there are comments explaining what is going on, so people can learn from the comments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269853):
I think readability is extremely important for people to have confidence in formalisations. I am sure you all know the paper by Pollack, "How to believe a machine-checked proof": http://www.brics.dk/RS/97/18/BRICS-RS-97-18.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269859):
I think he has very good points

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269962):
For example, if the statement of Ramanujan's conjecture uses modular forms, then I need to understand the formalisation of the definition of modular forms as well. And if they are defined as sections of some line bundle on a modular curve, then I need to understand those as well...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269972):
If there is one typo in those definitions... then the proof of Ramanujan's conjecture might not actually be a proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125270026):
That is why theorems with simple statements should have extremely readable and simple formalisations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125270044):
And afterwards, there might be theorems that say the statement is equivalent to some other statement using involved definitions, which you then go on to prove...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 18 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125270068):
On the other hand, maybe my rant does not have much bearing on readability of *proofs*...


{% endraw %}
