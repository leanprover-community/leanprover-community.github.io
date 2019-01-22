---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20171rewriteoccs.html
---

## [general](index.html)
### [rewrite occs](20171rewriteoccs.html)

#### [Scott Morrison (Mar 10 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546271):
Can anyone help me understand why the 2nd example in the following doesn't work?
```lean
@[ematch] lemma baz (l : list ℕ) : 1 :: l = 2 :: l := sorry
example : [1, 1, 2] = [2, 1, 2] :=
begin 
rw [baz] {occs:=occurrences.pos [1]},
end
example : [1, 1, 2] = [1, 2, 2] :=
begin 
rw [baz] {occs:=occurrences.pos [2]},
end
```

#### [Scott Morrison (Mar 10 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546276):
I have been reading `replace_fn.cpp` and `kabstract.cpp`, to no avail: my understanding of what is going on there suggests the second example should still work.

#### [Scott Morrison (Mar 10 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546372):
A related confusion is why in
```lean
example : [1, 1, 2] = [1, 2, 2] :=
begin 
rw [baz],
end
```
the goal has become `[2, 1, 2] = [1, 2, 2]`, and not `[2, 1, 2] = [2, 2, 2]`. That is, why did rewrite give up on the rhs?

#### [Sebastian Ullrich (Mar 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546557):
`kabstract` does not backtrack from unification: once `l` has been assigned `[1, 2]`, it does not consider other values for it

#### [Sebastian Ullrich (Mar 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546564):
That is, it only finds occurrences of the same instantiation of the lhs

#### [Sebastian Ullrich (Mar 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546609):
(Don't ask me why :) )

#### [Scott Morrison (Mar 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546657):
oh...

#### [Scott Morrison (Mar 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546664):
I see, that `ctx.unify` call in `kabstract` is saving information about things it has seen before.

#### [Scott Morrison (Mar 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546667):
It hadn't occurred to me that there were side effects there.

#### [Scott Morrison (Mar 10 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546697):
That sucks (for my purposes)...

#### [Scott Morrison (Mar 10 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546756):
So... if I really really wanted be be able to generate a list of all the rewrites of some expression `e` by some rule `r` (where we just rewrite in one place), is there any hope?

#### [Scott Morrison (Mar 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546763):
It seems that just calling `rw [r] at e {occs := occurrences.pos n}` and gradually increasing `n` until it fails is doomed, because of this "feature" of `kabstract`.

#### [Simon Hudon (Mar 10 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547082):
if you want to hack a solution together, you might have to copy / paste the implementation of `rw` and reimplement `kabstract`. I think the key is to undo the assignment of meta variable. One way of to that is to traverse your expression and create new meta variables to replace the ones that you find.

#### [Sebastian Ullrich (Mar 10 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547088):
Yes. It just won't be very fast.

#### [Simon Hudon (Mar 10 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547146):
I assume with the new focus on Lean 4, that might be the one way to get the fixed tactic sooner than later.

#### [Scott Morrison (Mar 10 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547154):
I see: reimplement `kabstract` in Lean?

#### [Scott Morrison (Mar 10 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547198):
I was just trying to find the definition of `type_context_old`, and see if there was any hope of hacking on an extra option that would change this behaviour. But I agree it's exceedingly unlikely I could propose such a change.

#### [Simon Hudon (Mar 10 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547201):
yeah pretty much. Unless @**Sebastian Ullrich** agrees that the current semantics is wrong and is willing to fix it for you

#### [Scott Morrison (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547207):
@**Sebastian Ullrich** ? :-)

#### [Sebastian Ullrich (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547208):
It's been that way since Lean 2, where it was even documented afair :)

#### [Scott Morrison (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547209):
Okay!

#### [Scott Morrison (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547210):
Looks like I will think about a really slow version of kabstract!

#### [Scott Morrison (Mar 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547259):
(Context here is that I'm otherwise really happy with my `rewrite_search` tactic, based on greedily minimising edit distance. I have "real" examples where it successfully finds long (~10) chains of rewrites that complete a proof. Unfortunately sometimes it mysteriously fails, and this seems to be the issue.)

#### [Sebastian Ullrich (Mar 10 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547262):
It's not even clear to me what a different `kabstract` would look like. Would it introduce `n` lambdas and return `n` instantiated copies of `e`?

#### [Sebastian Ullrich (Mar 10 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547305):
@**Scott Morrison** I suppose repeatedly rewriting will not solve your problem? :)

#### [Scott Morrison (Mar 10 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547311):
No -- I have lots of examples where the rewrite rule needs to be applied "inside" a bigger expression where the rewrite rule also applies.

#### [Scott Morrison (Mar 10 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547312):
But after you do the outer rewrite the inner rewrite is no longer available.

#### [Scott Morrison (Mar 10 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547354):
(`rewrite_search` is already trying repeated rewrites itself: I only discovered this problem because it was mysteriously failing.)

#### [Kevin Buzzard (Mar 10 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547355):
Scott -- has Mario made any suggestions on how to deal with your issues?

#### [Scott Morrison (Mar 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547357):
Kevin -- I only raised this about 5 minutes ago, perhaps Mario is sleeping. :-)

#### [Scott Morrison (Mar 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547414):
@**Sebastian Ullrich**, I guess I was thinking not actually to reimplement `kabstract`, but reimplement all of `rewrite_core`.

#### [Scott Morrison (Mar 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547416):
(Reimplementing `kabstract` in Lean would not be helpful, because no tactics actually call it from Lean: only things in c++.)

#### [Sebastian Ullrich (Mar 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547458):
I'm not sure how you want to solve your issue with the current kabstract

#### [Scott Morrison (Mar 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547464):
Or rather, to write something called `all_rewrites`, that takes an expr, and a list of lemmas, and returns `list (expr \times expr)`, where the pairs are the result of using the lemma in one place, and the proof.

#### [Scott Morrison (Mar 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547505):
It would work by recursively going down into the expr, and repeatedly calling unify ... oh, I see your point.

#### [Scott Morrison (Mar 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547509):
Those calls to unify are _also_ going to be cached. :-(

#### [Scott Morrison (Mar 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547511):
This is terrible. :-)

#### [Sebastian Ullrich (Mar 10 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547518):
Well, not if you create new mvars like Simon suggested

#### [Scott Morrison (Mar 10 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547524):
I see; after every time you successfully find a match, you throw out the mvar you were passing to unify and make a new one.

#### [Scott Morrison (Mar 10 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547566):
(Thanks, Simon, sorry I was slow to understand exactly what you meant.)

#### [Simon Hudon (Mar 10 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547580):
No worries

#### [Kevin Buzzard (Mar 10 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547635):
```quote
Kevin -- I only raised this about 5 minutes ago, perhaps Mario is sleeping. :-)
```
Oh -- I knew that you had been discussing with Mario about what looked like a major refactoring job on the category theory library and I was just kind of assumed this might be something to do with the refactoring

#### [Simon Hudon (Mar 10 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547638):
I believe in rewrite, when you use `∀ x, f x = g x` as your rewrite rule, you generate one mvar to instantiate x and you start matching. What you can do instead is create a unique local constant to instantiate x with (or as many as you have bound variable) and you create a table mapping those constants to mvars every time you attempt a match

#### [Sebastian Ullrich (Mar 10 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547691):
Btw, it might be easier to build something on top of `tactic.ext_simplify_core`. You basically get a very configurable term DFS where you can return subterm equality proofs pre or post visit and the tactic takes care of composing them into the complete proof.

#### [Scott Morrison (Mar 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547692):
Hmm... okay, on the 3rd reading I still don't understand that. :-) (Simon's comment about local constants.)

#### [Mario Carneiro (Mar 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547704):
I don't have any good suggestions for your rewrite issue. One possibility is to use `conv` or `ext_simplify_core` to recurse into all subterms and try `rw` on each of them

#### [Kevin Buzzard (Mar 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547744):
How do I do a rw in conv, by the way?

#### [Scott Morrison (Mar 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547745):
I don't actually know how `conv` is implemented under the hood: is it using `ext_simplify_core` anyway?

#### [Kevin Buzzard (Mar 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547746):
I don't mean a rw, I mean I want to replace something with something defeq

#### [Kevin Buzzard (Mar 10 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547750):
do I have to use whnf?

#### [Scott Morrison (Mar 10 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547756):
I really like these ideas. It hadn't occurred to me that I could think of `conv` as letting me recurse into all subterms in tactic mode.

#### [Kevin Buzzard (Mar 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547798):
I only just learnt how it worked really, it's all because of this push by Patrick to get some informal docs written.

#### [Kevin Buzzard (Mar 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547799):
I find them really enlightening

#### [Scott Morrison (Mar 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547800):
Is there any hope that I could build a pattern corresponding to the lhs of my rewrite rule, and pass that to `conv`, and thereby only visit the places where `rw` would work anyway? Or would this run into exactly the same unification caching problem?

#### [Scott Morrison (Mar 10 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547916):
Okay, answering my own question: no, you can't pass patterns to conv, it does indeed run into this same problem.

#### [Scott Morrison (Mar 10 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548005):
@**Kevin Buzzard**, here are two examples of using `rw` inside `conv`, solving the problem I started this thread with:
```lean
example : [1, 1, 2] = [2, 1, 2] :=
begin 
conv { congr, rw [baz] },
end
example : [1, 1, 2] = [1, 2, 2] :=
begin 
conv { congr, congr, skip, rw [baz] },
end
```

#### [Scott Morrison (Mar 10 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548103):
I think in the end `ext_simplify_core` is going to be the right solution. Since I want to build up a list of all the possible rewrites, I think it makes sense to build it up during the run of `ext_simplify_core`, rather than making multiple calls into conv, each one looking at a different piece of the expression.

#### [Scott Morrison (Mar 10 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548109):
(Please tell me if that doesn't make sense!)

#### [Scott Morrison (Mar 10 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548158):
Thank you, everyone, for the extremely helpful suggestions, as usual!

#### [Simon Hudon (Mar 10 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548204):
Thanks for the interesting challenges :smile:

#### [Kevin Buzzard (Mar 10 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548272):
I don't even understand what this thread is about. What is ematch? Did someone write some informal docs yet?

#### [Kevin Buzzard (Mar 10 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548304):
I really find life easier with docs. Then I have to ask fewer questions.

#### [Mario Carneiro (Mar 10 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548319):
I don't think the ematch attribute is relevant to simon's example

#### [Andrew Ashworth (Mar 10 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548415):
ematch: you can try reading Leo's paper.... https://link.springer.com/chapter/10.1007/978-3-540-73595-3_13

#### [Andrew Ashworth (Mar 10 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548456):
it's a little arcane unless you're really into the theory though

#### [Andrew Ashworth (Mar 10 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548570):
aha! something better: http://yices.csl.sri.com/papers/cav2007.pdf

#### [Andrew Ashworth (Mar 10 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548609):
seems the root paper at the bottom of all this is something from the 80s: https://people.eecs.berkeley.edu/~necula/Papers/nelson-thesis.pdf

#### [Andrew Ashworth (Mar 10 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548657):
that said, i'm not volunteering to read everything, digest it, and then write a simple introduction to ematch :)

#### [Kevin Buzzard (Mar 11 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123567801):
Oh thanks! I honestly behave like a computer. I looked at what Scott had posted, didn't understand the first word (ematch) and then just crashed and stopped reading (I was trying to get three kids to bed as well as reading chat). I see that this thread is well within my grasp now. Sorry for earlier noise.

#### [Kevin Buzzard (Mar 11 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123567891):
So Scott what are you actually trying to do in the long run here? What is the problem with just writing a tactic which tries every possible rw on some term using some set of terms which are equalities but with metavariables? Is that what you want? Isn't that exactly the sort of thing one can write a tactic for? Or is the point that you want to do it without writing a tactic?

#### [Kevin Buzzard (Mar 11 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568038):
And a related question. Is Sebastian saying "there is something written in C++ which doesn't do what you want, but you could write a version in Lean which does do what you want but it would be slow"? And how does this contrast with Leo's Lean 4 plan -- goal #1 in fact -- of taking some stuff out of C++ and implementing it in Lean?

#### [Kevin Buzzard (Mar 11 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568039):
How can this ever be a good idea? I don't understand the ramifications of this idea

#### [Kevin Buzzard (Mar 11 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568138):
(deleted)

#### [Gabriel Ebner (Mar 11 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568224):
In Lean 4 it would be fast because you could compile it to C++ that runs as fast as the current kabstract code.

#### [Simon Hudon (Mar 11 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123579238):
How will that work? Will Lean run the definitions of the current file in the VM and at the end compile the whole file to C++ to accelerate the verification of the next files?

#### [Kevin Buzzard (Mar 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580122):
```quote
I don't mean a rw, I mean I want to replace something with something defeq
```
ooh I can use change.

#### [Kevin Buzzard (Mar 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580123):
```
theorem H3 : 3 + 2 = 1 + 4 := begin
conv begin
to_lhs,
change 1 + 4,
end
end
```

#### [Patrick Massot (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580178):
Great! Do you have a slightly more realistic example?

#### [Kevin Buzzard (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580181):
I did have the other day!

#### [Patrick Massot (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580183):
(not necessarily super realistic, like the ones I put in the conv doc)

#### [Kevin Buzzard (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580184):
I had a goal of the form `X=Y` but `Y` had terms in it of the form `\<a,_\>`

#### [Kevin Buzzard (Mar 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580228):
so I couldn't use show to replace X on LHS with something defeq because cut and paste wouldn't work for RHS. So I used conv and then realised I didn't know how to do show in conv mode and ended proving some auxiliary lemma with rfl and doing a rw. This way is much cooler :-)

#### [Kevin Buzzard (Mar 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580229):
I was going to update the conv doc myself but then I realised you owned it rather than mathlib

#### [Patrick Massot (Mar 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580231):
What?

#### [Patrick Massot (Mar 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580236):
I don't own anything here

#### [Patrick Massot (Mar 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580237):
My PR was merged into mathlib

#### [Patrick Massot (Mar 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580238):
Please feel super free to update it

#### [Kevin Buzzard (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580277):
wait I can't find it anywhere

#### [Patrick Massot (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580279):
https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md

#### [Patrick Massot (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580280):
or follow links from the main README

#### [Patrick Massot (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580282):
Starting with link "extra Lean documentation"

#### [Kevin Buzzard (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580283):
maybe I don't understand git. I thought I just pulled

#### [Kevin Buzzard (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580290):
oh maybe I really don't understand git. I am pulling from my own fork not from mathlib

#### [Patrick Massot (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580291):
(because it's no about mathlib)

#### [Patrick Massot (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580294):
Do you have a git remote pointing to the main repo?

#### [Patrick Massot (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580295):
`git add remote upstream https://github.com/leanprover/mathlib.git`

#### [Kevin Buzzard (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580296):
```
$ git remote -v
leanprover	https://github.com/leanprover/mathlib.git (fetch)
leanprover	https://github.com/leanprover/mathlib.git (push)
origin	git@github.com:kbuzzard/mathlib.git (fetch)
origin	git@github.com:kbuzzard/mathlib.git (push)
```

#### [Kevin Buzzard (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580338):
I need to pull harder somehow

#### [Kevin Buzzard (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580342):
I am only pulling from origin

#### [Patrick Massot (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580343):
Then `git pull leanprover master`

#### [Patrick Massot (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580344):
you called leanprover what is traditionnaly called "upstream"

#### [Kevin Buzzard (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580347):
great, I now have extras.

#### [Patrick Massot (Mar 11 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580358):
Now `git checkout -b docs-conv-change`

#### [Patrick Massot (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580399):
Do your modifications, `git commit -a`, `git push`. Then git will complain and tell you what to type instead of `git push`

#### [Patrick Massot (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580400):
(with `git push set-upstream` in it)

#### [Kevin Buzzard (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580401):
why won't it just push to my fork?

#### [Patrick Massot (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580404):
then go to either upstream mathlib or your fork on Github and you'll be invited to open a PR

#### [Patrick Massot (Mar 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580410):
Because it's a new branch

#### [Patrick Massot (Mar 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580411):
a branch that is not on github yet

#### [Patrick Massot (Mar 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580412):
(yeah, the word upstream is used in a slightly different sense in `set-upstream`)

#### [Kevin Buzzard (Mar 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580639):
git push just pushed to my fork

#### [Patrick Massot (Mar 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580640):
yes

#### [Patrick Massot (Mar 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580642):
now you can PR

#### [Patrick Massot (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580648):
except that you skipped creating a new branch...

#### [Kevin Buzzard (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580649):
yeah :-/

#### [Patrick Massot (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580650):
This is bad

#### [Kevin Buzzard (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580651):
oh :-)

#### [Patrick Massot (Mar 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580701):
You can't have several open PR with this non-branching strategy

#### [Kevin Buzzard (Mar 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580702):
I have loads of my own WIPs all with no branch either.

#### [Kevin Buzzard (Mar 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580704):
I will google and sort it out. Let's not spam here.

#### [Patrick Massot (Mar 11 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580712):
Then you can't even PR since it would PR the WIP at the same time

#### [Kevin Buzzard (Mar 12 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123597942):
Hmm. I can't deal with Mario's comments on my docs because travis hasn't finished building.

#### [Mario Carneiro (Mar 12 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598291):
I think you can more or less ignore travis builds for a doc change

#### [Patrick Massot (Mar 12 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598331):
Quoting Mario for @**Kevin Buzzard** 
```quote
Re: PRs, I'm okay with docs of any kind. My recommendation is to try to write them with an authoritative locution style; I will let you know if you say false things. If you don't know something, leave it out, say you don't know in the doc, or ask about it here and then put in whatever you find out.
```

#### [Mario Carneiro (Mar 12 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598341):
(Of course, there is no guarantee that your PR won't (apparently) "break the build", since our current peculiar setup that pulls from a moving target lean nightly means that if Leo decides to break mathlib at the same time your PR will get the blame.)

#### [Patrick Massot (Mar 12 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598348):
I think you could edit a few sentences to conform to this recommendation

#### [Mario Carneiro (Mar 12 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598385):
I tried to respond to Kevin's parentheticals in the PR comments, so hopefully they will be addressed in the next revision

