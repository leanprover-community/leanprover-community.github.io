---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90698docssprint.html
---

## Stream: [general](index.html)
### Topic: [docs sprint](90698docssprint.html)

---


{% raw %}
#### [ Patrick Massot (Aug 10 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131844734):
There have been several additions to mathlib recently, many people asking what is there, and Mario's talk giving an overview. I think it's a good time to put some energy into that `docs` directory. Let's try out new community fork on this: https://github.com/leanprover-community/mathlib/commit/cc1f2c6a2a2c00c833d28023a63f9670f175d74d is a starting point. Note that I added links to several files which existed but were not reachable from the README. I also added new files in theory, but they don't contain much yet.

#### [ Patrick Massot (Aug 10 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131844818):
 I think it would also be useful to think of some common scheme for the `theories` directory. For instance: one short paragraph mentioning what is there and the main files. Then a highlights sections mentioning the main definitions and theorems (probably only the maths and Lean names, not copying the def). Then some maths discussion, as in the topological space doc (or Kevin's blog post), some more examples.

#### [ Kevin Buzzard (Aug 11 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131849561):
I agree. I've learnt a lot more about what is in mathlib recently. I feel like there should be a better way of documenting it.

#### [ Johan Commelin (Aug 11 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131937901):
Hey Patrick! Guess what I did just before I went to sleep yesterday: I wrote a two page todo-list of stuff that I wanted to see documented. I think a docs sprint is an awesome idea!

#### [ Johan Commelin (Aug 11 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131937950):
I'll see if I can find some time to add stuff. But it's holiday time over here. So I might not be very active the next few days.

#### [ Kevin Buzzard (Aug 11 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131945177):
I wrote my random blog posts because I was desperate at that time to find some way in to what was in mathlib, which at that time looked huge and daunting to me (and IIRC it might even have been before Mario went through and added docstrings to many of the major results). At that time, for example, I found `rat.lean` incomprehensible. Now things are very different -- for example I understand the "point" of a mathlib file now; to set up an API for the user so that someone like me can use multisets without having to worry about the fact that their definition is rather delicate so proving basic properties about them can be complicated. 

So what form should these docs take? How about using the Wiki feature of github? One wiki page per directory perhaps? Pages don't attempt to document everything, but instead flag the names of the main theorems and main definitions. I still don't know too much about lattices, but I note that when giving other things the structure of a lattice, "sometimes <= is defined to be >=", as it were (I forgot the specific example where this happened but I think it happens at least once). 

I don't think my approach with N,Z,Q etc of just writing down a bunch of random theorems and saying what their names are is a particularly good one. It helped me a lot at the time, but that was when I was struggling to work out the naming system.

What do people think about the Wiki idea? Perhaps I'll knock up a sample page and people can comment.

#### [ Patrick Massot (Aug 11 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131945951):
We already discuss the wiki option. The trouble is that Mario doesn't have enough power on the mathlib page to allow that. We could use the community account and link from official mathlib though. But using the public fork before PRing to mathlib is almost as easy. Remember you should have push access. So you can `git clone git@github.com:leanprover-community/mathlib.git`,`git checkout docs-theories`, commit there and push

#### [ Patrick Massot (Aug 11 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131946034):
While beginning this, I thought the file organization in mathlib probably needs some refactoring. In the mean time we cannot really use one page per directory. See the mess in https://github.com/leanprover-community/mathlib/blob/docs-theories/docs/theories/polynomials.md for instance

#### [ Patrick Massot (Aug 11 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131953188):
I feel my question may have disappeared among Ed's questions...

#### [ Johan Commelin (Aug 11 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131953712):
Patrick, I think all those questions by Ed and the answers by Mario contain a lot of raw data that could be used in a doc sprint on meta/tactics.

#### [ Edward Ayers (Aug 11 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131953811):
I'm writing up some personal notes based on the convo with Mario. its still quite idiosyncratic but I could spend some time making it a draft for some docs if that would be useful. But since I am still learning it might be best to let someone else who knows what they are doing make the first draft.

#### [ Patrick Massot (Aug 11 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131954117):
I'm not complaining, and I would love to read documentation by Ed. I'm only trying to get my answer (right now I'll go the beach, but I'd love to have an answer when I'll come back). Ed, you shouldn't wait for experts to write documentation if you can write some. All doc in mathlib was written by people who just learned it.

#### [ Kevin Buzzard (Aug 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131956176):
```quote
 All doc in mathlib was written by people who just learned it.
```
Ed this is absolutely true. For example the docs on `simp` were written by me precisely because I knew nothing about `simp`. I asked some questions here, wrote some basic first draft, PR'ed it, people told me about the noob mistakes I'd made, I edited it, it became a basic doc with some basic facts about `simp` which aren't mentioned in Theorem Proving In Lean (TPIL), and now I sometimes point people to it when they ask basic `simp` questions. We're not trying to be professional -- we're just trying to get basic facts down which are "known to the experts" but for which there is no reference. I would strongly encourage you to just post your personal docs as a PR to somewhere in the `docs` directory of mathlib. Anything you write would be appreciated, because, as you've probably seen, what is available in PIL is very limited, and you're already way ahead of most of us with your questions.

#### [ Kevin Buzzard (Aug 11 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/131956582):
```quote
So you can `git clone git@github.com:leanprover-community/mathlib.git`,`git checkout docs-theories`, commit there and push
```
So Patrick is suggesting that we just stick to writing `.md` files like before. Would a wiki not be a better way of organising the information? I guess the wiki stuff on github is just a bunch of `.md` files anyway...

#### [ Kevin Buzzard (Aug 12 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132008813):
I just sat down and binge-wrote an overview of what I think is in mathlib: https://github.com/leanprover-community/mathlib/blob/docs-theories/docs/mathlib-overview.md. Feel free to edit.

#### [ Kevin Buzzard (Aug 12 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132008925):
Oh I've just seen that to a certain extent I've duplicated what Patrick has done. Never mind, it's all about getting the facts down.

#### [ Patrick Massot (Aug 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132009193):
I think it's not a big problem to have several ways of documenting stuff. What you wrote is more narrative and less of a quick access list

#### [ Patrick Massot (Aug 12 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132009248):
I would add a link to your file either on top of https://github.com/leanprover-community/mathlib/blob/docs-theories/docs/theories.md or in https://github.com/leanprover-community/mathlib/blob/docs-theories/README.md on the same line linking to `theories.md`

#### [ Edward Ayers (Aug 21 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132520945):
I wrote a tutorial/docs for meta things:
https://github.com/EdAyers/mathlib/blob/doc/docs/meta_0.md
https://github.com/EdAyers/mathlib/blob/doc/docs/meta_1.md

Still some questions to be answered and I might write part 2 on elaboration if there is interest.

#### [ Edward Ayers (Aug 21 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132521463):
fixed some formatting issues on github

#### [ Kevin Buzzard (Aug 21 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132521684):
proof-irrelevance (in second doc, "Reduction in Lean" section) -- should that be `P : Prop` and `a b : P`?

#### [ Edward Ayers (Aug 21 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132521759):
```quote
proof-irrelevance (in second doc, "Reduction in Lean" section) -- should that be `P : Prop` and `a b : P`?
```
Yep!

#### [ Kevin Buzzard (Aug 21 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132521799):
`[TODO] find a paper giving the inference rules for CIC used in Lean.` -- is https://leanprover.github.io/reference/expressions.html#expression-syntax what you're looking for (or maybe something around there), or is that something else?

#### [ Kevin Buzzard (Aug 21 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132521851):
PS *thanks*!

#### [ Edward Ayers (Aug 21 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132522095):
```quote
`[TODO] find a paper giving the inference rules for CIC used in Lean.` -- is https://leanprover.github.io/reference/expressions.html#expression-syntax what you're looking for (or maybe something around there), or is that something else?
```
Expression syntax is different to inference rules. Inference rules tell you when a given expression is valid. I'm looking for these things: https://en.wikipedia.org/wiki/Type_rule

#### [ Edward Ayers (Aug 21 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132522183):
Specifications of functional programming languages usually come with a table of all of the type rules for that language.

#### [ Mario Carneiro (Aug 21 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132524892):
See https://github.com/digama0/lean-type-theory/releases/tag/v0.21 chapter 2 for the axioms of lean

#### [ Mario Carneiro (Aug 21 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132526104):
> Anything to do with the mathematics: proving a theorem, writing a definition, defining an inductive type ... is called object-level or theory-level ([TODO] what is the preferred nomenclature here?)

The usual term here is "object-level". But I think it is worth pointing out that `meta` in lean is a bit of a misnomer - it is more accurate to call this `unsafe`, because it enables a number of unsound mechanisms, and while it is useful for metaprogramming it is not exclusively used for this (not all metaprogramming things are `meta`, and not all `meta` things are used in metaprogramming)

#### [ Edward Ayers (Aug 21 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132526776):
Also @**Mario Carneiro** , some proportion of these documents are copy-and-pasted from answers in Zulip, mostly your answers. I hope you are ok with this.

#### [ Johan Commelin (Aug 21 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132535092):
@**Edward Ayers** Wow! I'm really impressed. This document is going to be massively useful. If you could lump on some exercises, I think you would have an insane tutorial!

#### [ Patrick Massot (Aug 21 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132539885):
Thanks Edward! I can't wait for the next episode.

#### [ Johan Commelin (Aug 22 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132559959):
Re the note on unification: so there are lots of different algorithms for unification. Does this mean that in principle one could have a conservative algorithm in the kernel, and other "user land" algorithms for unification as tactics or so?

#### [ Chris Hughes (Aug 22 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132562464):
I thought unification wasn't done in the kernel at all.

#### [ Johan Commelin (Aug 22 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132563611):
Maybe you're right. I still learning all these things, and I'm a complete novice... but I guess there is some sort of "default" algorithm. Anyway, if it's not in the kernel, then it is probably possible to have different unification algorithms that coexist.

#### [ Edward Ayers (Aug 22 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132571917):
Unification is not done in the kernel. It used to be in the kernel. Although I didn't find the precise C++ file that *is* doing unification.

#### [ Edward Ayers (Aug 22 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132572176):
The trouble is that there are lots of 'expansion packs' you can add to unification and they are all munged together in the literature. The most basic form of unification just does structural equality while assigning metavariables when it needs to. Then there is (undecidable in general) higher-order unification that tries to guess metavariables which are functions. There is also unification up to definitional equality and even unification where the unifier will perform rewrites using certain rules in the environment. I am not sure which of these Lean is doing, I find it hard to inspect in the source code. On top of this the unifier in Lean treats typeclass instances differently to other unification constraints.

#### [ Edward Ayers (Aug 22 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132572324):
I'm not sure if it is worth trying to figure this out because:
- Lean usually unifies/matches things sensibly anyway, so the implementation details can usually be ignored in practice.
- I would guess that the details of the unifier are going to change in Lean 4 anyway

#### [ Sebastian Ullrich (Aug 22 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132585914):
I didn't read everything, but two quick links:
- kernel unifier: https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/kernel/type_checker.cpp#L667 (but terms must be free of meta variables)
- elaborator unifier: https://github.com/leanprover/lean/blob/e6764047a14ce4383d29b2858fa9e2e246d4f13b/src/library/type_context.cpp#L3275 (uses approximation to higher-order unification and other heuristics)

#### [ Johan Commelin (Aug 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132681930):
Ok... so my TODO list for the docs sprint is now becoming very short... I wanted to push myself to write down some sort of summary of what I understood about `meta` and document everything that I learned from Ed's question barrage. But now he did that himself... I also wanted to document some of the maths in mathlib, but Kevin already wrote down a thorough overview. So, what is left is a small section on how to contribute to mathlib: https://github.com/leanprover-community/mathlib/blob/docs-theories/docs/howto-contribute.md

#### [ Johan Commelin (Aug 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132681938):
Another question: should we mention Zulip in `README.md`?

#### [ Scott Morrison (Aug 24 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132682171):
Yes, I think we should mention Zulip. Eventually we may want to divide into more streams, but for now I think it is working well.

#### [ Johan Commelin (Aug 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132682536):
Ok: should we also do that in the `docs_theories` branch, and then make a new PR?

#### [ Patrick Massot (Aug 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132688278):
Johan, there is still a lot to do in https://github.com/leanprover/mathlib/tree/master/docs/theories Many files are only stubs. You could also try to homogenize what's already there (I think I indicated one possible common scheme somewhere towards the beginning of this thread).

#### [ Kevin Buzzard (Aug 24 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132688786):
I think those early files I wrote are pretty rubbish and I think there's an argument which says that that whole part of the docs should be re-thought. I wrote those files when I was just figuring out what mathlib was, and my understanding was very superficial.

#### [ Kevin Buzzard (Aug 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132689064):
It seems to me that one of the most common questions about mathlib, from mathematicians at least, is "is X in mathlib?". But X is hardly ever "rings" (and I think that pointing someone who asks this to https://github.com/leanprover/mathlib/blob/master/docs/theories/rings_fields.md is a bit daft when we could just say "yes"), and it's never "commutative distribs" or whatever. More and more often it's things like "topological groups" or "Noetherian rings" or "fundamental groups" or "linear maps" or something -- and perhaps this part of the docs should be an attempt to answer such questions. Related questions are stuff like "how much number theory is in Lean"? Maybe we should be thinking more about writing really good answers to these questions.

#### [ Kevin Buzzard (Aug 24 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132689510):
I guess that writing these answers might also lead us towards finding missing theories which are a bottleneck for progress.

#### [ Edward Ayers (Aug 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132708979):
I wrote some docs on unicode in Lean:
https://github.com/EdAyers/mathlib/blob/doc/docs/unicode.md

#### [ Johan Commelin (Aug 24 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docs%20sprint/near/132710084):
:imp: After three years we will discover that Scott deceived everyone with his cool automation tactics: `obviously` is just `exact trivial` and the Yoneda lemma was pulling this Unicode trick. :rolling_on_the_floor_laughing:


{% endraw %}
