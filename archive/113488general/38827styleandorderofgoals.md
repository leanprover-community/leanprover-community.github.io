---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38827styleandorderofgoals.html
---

## [general](index.html)
### [`_` style and order of goals](38827styleandorderofgoals.html)

#### [Kevin Buzzard (Apr 15 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125107491):
I was proving a goal yesterday which was a rather complex maze of essentially trivial things -- everything was either a relatively easy argument or a relatively easy consequence of an already-proved result, and it was very much a case of following my nose. I was in tactic mode. Occasionally there were branches, where I would write something like `refine _ H _` because H was to hand but the two other goals needed a three-line argument, or I had a goal of the form `exists x, exists H, ...` and I would write `existsi _` and move on.

I noticed during this procedure that I would always just work on "the next available goal". Lines like `existsi _` would usually create an extra goal and I would just use `{}`s to focus down to one goal again. I didn't really care what the next goal was, I had a good notation system going so it was easy to keep track of which trivial thing I was proving, and the arguments were all independent.

However if someone made a one-line change to Lean which changed the order that the goals appeared in after a line like `existsi _` then my proof would break and it would be pretty horrible to fix it.

I know that whenever there is more than one goal I can just write `show [blah]` to make sure Lean is working on the goal I expect it to be working on, but I was doing classical mathematics with proofs on and many of the goals were of the form `|- x in classical.some [very long thing]`.

Would it be considered good style to actually put all these `show [blah]` lines in? Is there any conceivable reason that the devs might choose, in Lean 4 say, to reorder the way goals appear, and really break a lot of the work I did yesterday? The goals were long in my case and I felt they would clutter my code, but on the other hand I can see an argument for stating precisely what I'm working on at any given time.

#### [Andrew Ashworth (Apr 15 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125111068):
it's an option for readability

#### [Andrew Ashworth (Apr 15 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125111071):
i know i've linked this file before, but https://github.com/leanprover/mathlib/blob/master/order/conditionally_complete_lattice.lean demonstrates usage of lots of `show` for goals

#### [Andrew Ashworth (Apr 15 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125111114):
and also breaking down a problem so there isn't a single large proof that discharges many goals

#### [Andrew Ashworth (Apr 15 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125111154):
hm, in coq it's pretty easy to match based on the goal type

#### [Andrew Ashworth (Apr 15 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125111161):
doing different things based on the 'shape' of the proof may be even more resilient to changes than `show` too

#### [Sebastian Ullrich (Apr 15 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125111209):
```quote
I know that whenever there is more than one goal I can just write `show [blah]` to make sure Lean is working on the goal I expect it to be working on, but I was doing classical mathematics with proofs on and many of the goals were of the form `|- x in classical.some [very long thing]`.
```
`show` selects goal by unification, no need to write down the entire goal.

#### [Mario Carneiro (Apr 15 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125119384):
> goals were of the form `|- x in classical.some [very long thing]`.

You should not be facing a theorem like this. There are two ways this can come up:
* You have a definition that uses `classical.some`, that you unfolded. If you make such a definition, you should *always* state the corresponding `some_spec` theorem (or some consequences of it) as the "interface" to the definition. This has much better behavior wrt simp and rw, and it makes it clear what important properties you need the definition to have that caused you to use `classical.some` in the first place.
* If you introduce a `classical.some` in the middle of a proof, I suggest you use `axiom_of_choice` instead, which is essentially just `some` and `some_spec` together and wrapped in an exists. That way, when you open the exists in your context, it adds a variable f and a fact about it to your context without getting some irrelevant complex term `classical.some <big thing>` that shouldn't be unfolded anyway.

#### [Mario Carneiro (Apr 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60_%60%20style%20and%20order%20of%20goals/near/125119646):
> However if someone made a one-line change to Lean which changed the order that the goals appeared in after a line like existsi _ then my proof would break and it would be pretty horrible to fix it.

Your proof style sounds like a good way to find a proof in the first place, but it definitely requires post-processing once the proof is complete, because if you just leave it like that it will be very brittle since you give very little information about what you are proving. One easy thing to do is never use `existsi _`; once you find out what term goes there (when you finish the proof) you should go back to this line and insert the term. This should also suppress the superfluous branching. (You can get away with `<_, proof>` to prove an exists more often in term mode, since the type of `proof` will often give the term by unification.)

