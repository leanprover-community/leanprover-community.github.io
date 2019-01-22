---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/2111785monotonicity.html
---

## [PR reviews](index.html)
### [#85 monotonicity](2111785monotonicity.html)

#### [Simon Hudon (Oct 07 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135362082):
@**Mario Carneiro** @**Johannes Hölzl**: what is missing on this PR?

#### [Johan Commelin (Oct 08 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135399492):
Is it correct that there is some overlap with `linarith` in use cases? (I'm just trying to get a feel for what this is doing.)

#### [Simon Hudon (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135407173):
In the cases where no arithmetic or little arithmetic is involved, yes, that's true. It also works with any relation you want

#### [Simon Hudon (Oct 08 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135407285):
The overlap is just enough that if you have a long chain of monotonicity, you don't have to drop `mono` in the middle to use `linarith`

#### [Johannes Hölzl (Oct 15 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135827830):
what I like is that it works with different relations. But I think we want a more general rewrite. Where congruence rules are added in a database for arbitrary relations. And then I just say `grw [r1, r2, r3]`. maybe even trying to match modulo AC?

#### [Simon Hudon (Oct 15 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135839710):
I like the idea but I'm hesitant. One benefit of calling `mono` directly is that, unlike with rewrite, with orderings, only one direction works.

#### [Johannes Hölzl (Oct 15 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135841066):
yes, the relation may not be symmetric, or reflexive or even transitive. And with symmetry for rewrite its only a special case for `<- r`. For rewriting its more important that the relation is reflexive, and for `simp` that it is transitive.

#### [Simon Hudon (Oct 15 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135841718):
In terms of usability I think it goes further. If you have `h : x ≤ y` and you want to rewrite `a ≤ b - x`, only `rw <- h` is available.

#### [Johannes Hölzl (Oct 15 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135843736):
This works with generalized rewriting. The congruence rules would be:
```
((≥) ⇒ (≤) ⇒ (→)) (≤) (≤)
i.e. a' ≥ a → b' ≤ b → (a' ≤ b' → a ≤ b)

((≤) ⇒ (≥) ⇒ (≤)) (-) (-)
i.e. a' ≤ a → b' ≥ b → (a' - b' ≤ a - b)
```

#### [Johannes Hölzl (Oct 15 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135843793):
So the `<- h` translates to a flip of the actual relation.

#### [Johannes Hölzl (Oct 15 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135843955):
This is by the way how `transfer` works, just that it doesn't apply a rewrite step, but tries to build up the relation proof exhaustively (hoping that it has rules for all constants and variables)

#### [Simon Hudon (Oct 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135852211):
I like the idea. It is quite a bit different from what I implemented and I would rather do it as a separate project

#### [Simon Hudon (Oct 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135925544):
Survery: do you (the reviewers) prefer for the attribute to be named `monotonic` or `mono`?

#### [Scott Morrison (Oct 17 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135949962):
`monotonic` (on the unpopular principle that abbreviations are always a bad idea)

#### [Simon Hudon (Oct 17 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135950021):
The tactic's name is `mono` though so do you think it's also a bad idea?

#### [Johannes Hölzl (Oct 17 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/135953945):
if possible the tactic and attribute should have the same name. I prefer `mono` over `monotonicity` due to its length, and for me `mono` is clearly `monotonicity`

#### [Scott Morrison (Oct 17 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001257):
monotone, monomorphism, monoid, monomial, monopole

#### [Mario Carneiro (Oct 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001322):
I vote `mono`. The shorter the name of a tactic is, the more awesome it sounds

#### [Scott Morrison (Oct 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001332):
... but I have never understood the desire to abbreviate (or rather, I think I understand the stated desire, to require fewer keystrokes and to fit more content per pixel, but don't think it's a valuable outcome)

#### [Scott Morrison (Oct 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001335):
I'd prefer things to be clear, rather than just clear from context.

#### [Mario Carneiro (Oct 17 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001366):
tactics with short and cryptic names like `omega` and `auto` seem to be quite popular

#### [Mario Carneiro (Oct 17 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001385):
it makes them more "name-like" rather than "decription-like"

#### [Scott Morrison (Oct 17 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001433):
but that is because they are useful!

#### [Mario Carneiro (Oct 17 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001437):
as in "use the mono tactic" rather than "use the tactic that does monotonicity reasoning"

#### [Scott Morrison (Oct 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001470):
`/- the result now follows -/ by monotonicity`

#### [Scott Morrison (Oct 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001492):
But again, I understand that no one is interested at this point in writing literate proofs.

#### [Simon Hudon (Oct 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001539):
```quote
But again, I understand that no one is interested at this point in writing literate proofs.
```
Why do you believe that?

#### [Mario Carneiro (Oct 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001545):
No, I mean literally name like, as in Joe or Sue

#### [Mario Carneiro (Oct 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001560):
I think it makes the language more colourful

#### [Mario Carneiro (Oct 17 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001613):
because I don't think you should take too seriously the "description-like" aspect of a tactic name anyway

#### [Mario Carneiro (Oct 17 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001690):
for a given tactic you will usually want to know exactly what it does and the description itself always falls short

#### [Scott Morrison (Oct 17 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001694):
I do appreciate this point.

#### [Mario Carneiro (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001707):
if it's just a name, then you just get used to the foibles of that tactic

#### [Scott Morrison (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001725):
```quote
```quote
But again, I understand that no one is interested at this point in writing literate proofs.
```
Why do you believe that?
```
Because I've never seen anyone try to write one? I considered trying to make the proof of the infinitude of primes in mathlib 'literate', but went on to other things.

#### [Mario Carneiro (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001734):
looks like Neil beat you to it

#### [Scott Morrison (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001739):
Oh, I didn't see.

#### [Mario Carneiro (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001741):
http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/

#### [Mario Carneiro (Oct 17 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001789):
I would like to see what you would add or change, you've done a few presentations with this proof now

#### [Scott Morrison (Oct 17 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001827):
Well, I think it's important to have everything in a single text file, even if there are tools to extract "human" and "cryptic Lean" available.

#### [Mario Carneiro (Oct 17 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136001994):
it looks like neil invented his own version of coqdoc, with popout text

#### [Scott Morrison (Oct 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002240):
I would hope that from same text file that we produce the `olean` file, we can also extract the following text:

>We take p to be the smallest prime factor of N!+1.

>First, we need to show that p is prime; this is immediate from the definition of the smallest prime factor, as long as we know that N!+1 is greater than one. (This follows since N! is at least one, so N!+1 is greater than one.)

>Next we show that p > N. We prove this by contradiction, so we assume p <= N. We observe that p | N! + 1, and p | N!. The first follows since p was chosen as a prime factor of N!+1. The second follows as 1 <= p <= N, and any such number divides N!. Combining these two facts, we have that p | 1. (This is just the fact that if n | a and n | a+b, then n | b.) We showed earlier that a prime cannot divide one, giving the desired contradiction.

I think this text very faithfully follows the proof given in mathlib.

#### [Scott Morrison (Oct 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002251):
Now, it is unclear to me whether that text should appear in the `lean` file.

#### [Scott Morrison (Oct 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002261):
But if it doesn't, that's only because we'd have written some tool that could _generate_ that text from the Lean source.

#### [Scott Morrison (Oct 17 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002307):
Generating an approximation of that text is not at all crazy, I think.

#### [Mario Carneiro (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002407):
that text is in the lean file

#### [Scott Morrison (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002413):
Even better would be that that text is what appears in the Lean file, and the "lean source" is extracted from it ...

#### [Scott Morrison (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002421):
What do you mean?

#### [Mario Carneiro (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002434):
click on the show raw text button

#### [Scott Morrison (Oct 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002577):
Okay, yes, I understand. It's great that Neil has written a prototype tool for `leandoc`. Now we need to think about what lean sources should look like with `leandoc` available.

#### [Scott Morrison (Oct 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002593):
Obviously they should not have html in the comments, but markdown.

#### [Scott Morrison (Oct 17 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136002614):
But maybe what Neil has written is an excellent start.

#### [Simon Hudon (Oct 18 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#85 monotonicity/near/136045229):
On the subject of `mono`, do we agree that if the tactic is called `mono`, `mono` is also a good name for the attribute?

