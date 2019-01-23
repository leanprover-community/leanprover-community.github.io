---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58237haveinmathlib.html
---

## Stream: [general](index.html)
### Topic: [have in mathlib](58237haveinmathlib.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 05 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154469705):
I am definitely very grateful to Mario for everything he does, but there is one question I want to raise on mathlib style. In general programming practice, comments are considered good, and even necessary. In lean, you can have lean-checked comments, in the form of `have`or `show`statements which, while unncessary to the compiler, increase a lot maintainability, readability, reusability (I mean, if you want to adapt a proof to suit your needs and you see what the proof is doing, then this is much easier), and make the learning curve less steep (by browsing through understandable code, one understands better what is going on). But this is at the price of compactness, or golfedness, which is very much valued in mathlib. 

Let me take a simple example, for the sake of the discussion. Suppose one wants to prove a statement by applying lemma `foo`, which gives rise to two subgoals `subgoal 1` and `subgoal 2`, whose proofs are both nontrivial. The mathlib canonical version (M) would be:
```lean
  refine foo _ _,
  { rather lengthy
    proof of subgoal 1 },
  { rather lengthy proof
    of subgoal 2 }
```
(or if you could even put some part of the proof in the first line, maybe go for it, for instance if the proof of `subgoal 1` starts with the introduction of variables `x` and `y` maybe write `refine foo (λ x y, _) _` in the first line)

But you could imagine more verbose versions such as (V1):
```lean
  refine foo _ _,
  show subgoal 1,
  { rather lengthy
    proof of subgoal 1 },
  show subgoal 2,
  { rather lengthy proof
    of subgoal 2 }
```
where the `show`lines are meant as completely unncessary comments. Or even (V2):
```lean
  have A : subgoal 1,
  { rather lengthy
    proof of subgoal 1 },
  have B : subgoal 2,
  { rather lengthy proof
    of subgoal 2 },
  exact foo A B
```
(M) is definitely more compact, but in my opinion (V1) or (V2) are preferable. And using (V1) or (V2) can depend on the intent: if the punchline is that one should use the lemma `foo`, I would put it at the beginning of the argument as in (V1), but if it is obvious that one should use `foo` and the hard part is checking the subgoals then I would rather go for (V2). Pros: more readable, maintainable, reusable. Cons: more verbose, slightly slower compilation time (?)

Anyway, I understand that the mathlib-ready version for now is (M), but I would really much like this to change. I am just starting the discussion, let me know what you think of it.

TLDR; I like code with a lot of `have` and `show` (at least one every sixth or seventh line?), and I would like to see more of them in mathlib. What do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 05 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470063):
My impression of these `show` lines is that they are mostly superfluous (there are ways to make a `show` do some work but I think we can agree that the question here is about the ones that are unnecessary for lean). Lean proofs (or at least mathlib proofs) aren't really intended to be read without the aid of lean in the background to give you side information. If we wanted to change that, a `show` line here and there wouldn't be nearly enough anyway. But assuming that the user has access to a lean server, comments about the current goal and the types of variables is quite redundant. It reminds me of the classic "bad C comment":
```
int i = 1; // set i to 1
```
There are much better uses for comments, like explaining *why* you are proving what you are. The Arzela-Ascoli theorem has several comments along these lines, and I think they are useful. But saying information that is already present seems like a waste of space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 05 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470079):
I like Sébastien's `show`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 05 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470250):
For very large proofs, it is helpful to mark the major landmarks with a `show`. But for sufficiently large proofs it is still better to just call these out as their own lemmas. Very long proofs don't work so great in lean; I would try to keep it to a page or less and break out lemmas if it gets longer than that (especially if the theorem takes a long time to compile).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 05 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470420):
```quote
Lean proofs (or at least mathlib proofs) aren't really intended to be read without the aid of lean in the background to give you side information.
```
Being able to read nontrivial proofs without starting a lean server looks important to me (I do it often in Isabelle). Maybe not all the tiny details of the proof, but the global structure, and what one is doing currently.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 05 2019 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470540):
also I much prefer (V1) style to (V2). When a proof breaks into a small piece and a large piece, the small piece should come first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 05 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470589):
this produces a more even distribution of complexity and minimizes nesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 05 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470960):
The question is whether one should be reading them at all. At the minute if you want to understand a lemma in mathlib you can usually just read a proof in an undergraduate textbook if it's "high level" and if it's a foundational lemma about multisets then who cares about the proof anyway, right? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 05 2019 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154471059):
My personal opinion is that mathlib is extremely hard to read for beginners and hence extremely intimidating. However the decisions about what it should like are entirely up to the maintainers who I'm sure have their reasons. I personally think that any reason of the form "makes compile time shorter" is spurious because we should be compiling every commit and dumping the olean files online so users don't have to compile ever and we should concentrate on solving this really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 05 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154471356):
I think the compilation time thing is currently crucial, and shouldn't be. Today I'm trying to bring Sébastien's metric namespace PR up to date with mathlib. I merged master, fix conflicts and pushed without building because it takes forever. And of course it failed to build. So I've tried to fix it, and now it takes forever to try to build. And this is not even touching basic files imported everywhere. But I needed to switch branch and everything is rebuilding. I think this is a major pain for maintainers, except if you can maintain without ever editing code...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 05 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154471838):
I have a separate copy of mathlib for each branch I am working on. So, I don't ever switch branches, as it is too painful otherwise. Clearly suboptimal, but efficient enough.

