---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35885finsetsum.html
---

## [general](index.html)
### [finset.sum](35885finsetsum.html)

#### [Morenikeji Neri (Aug 06 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130977419):
I'm having some trouble proving this. Help would be much appreciated.
```lean lemma sum_keji {α β : Type*} [add_comm_monoid α] {f : β → α}
  (s : finset β) (g : Π a ∈ s, β) (h₁ : ∀ a ha, f a + f (g a ha) = 0)
  (h₂ : ∀ a ha, g a ha ≠ a) (h₂ : ∀ a₁ a₂ ha₁ ha₂, g a₁ ha₁ = g a₂ ha₂ → a₁ = a₂)
  (h₃ : ∀ a ha, ∃ b hb, g b hb = a) : s.sum f = 0 := sorry ```

#### [Mario Carneiro (Aug 06 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979862):
I guess you should first prove `g a ha ∈ s` using the pigeonhole principle

#### [Mario Carneiro (Aug 06 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979907):
then the assumptions say that `g : s -> s` is a bijection, so you can use `sum_bij` to shift things around and cancel using `h1`

#### [Mario Carneiro (Aug 06 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979982):
Oh wait, you only have that it is an `add_comm_monoid`, that's not enough to conclude

#### [Mario Carneiro (Aug 06 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979991):
you will be able to prove `s.sum f + s.sum f = 0`

#### [Mario Carneiro (Aug 06 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130980256):
So for example if `α = Z/2Z`, `β=Z/3Z`, `s={0,1,2}`, `f a = 1` and `g n = n+1` then we have a counterexample

#### [Morenikeji Neri (Aug 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982346):
sorry about that. I realized I missed out a few assumptions in the theorem.
It should read.

```lean lemma sum_keji {α β : Type*} [add_comm_monoid α] {f : β → α}
  (s : finset β) (g : Π a ∈ s, β) (h₁ : ∀ a ha, f a + f (g a ha) = 0)
  (h₂ : ∀ a ha, g a ha ≠ a) (h₂ : ∀ a₁ a₂ ha₁ ha₂, g a₁ ha₁ = g a₂ ha₂ → a₁ = a₂)
  (h₃ : ∀ a ha, ∃ b hb, g b hb = a) (h₄ : ∀ a ha, g a ha ∈ s) (h₅ : ∀ a ha, g (g a ha) (h₄ a ha) = a ) : s.sum f = 0 := sorry ```

#### [Mario Carneiro (Aug 06 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982614):
Oh I see, it's an involution

#### [Mario Carneiro (Aug 06 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982654):
You can prove this by complete induction on `s`. Just take out `a` and `g a ha` in one step of the induction

#### [Chris Hughes (Aug 06 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982680):
Is there a short proof using lemmas?

#### [Mario Carneiro (Aug 06 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982691):
not with those hypotheses

#### [Mario Carneiro (Aug 06 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982711):
half of the work will be unpacking them

#### [Mario Carneiro (Aug 06 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982788):
I mean, the stuff about `sum` is there but most of the work is showing that the reduced `g` function is still an involution

#### [Morenikeji Neri (Aug 06 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982854):
yep!

#### [Scott Morrison (Nov 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271569):
Okay... after way too many inequalities (thanks, everyone!), I now have "the right" proof that $\sum_m \binom n m = 2^n$, based on reindexing sums and splitting off and joining single terms. This uses the following four lemmas:
```
lemma finset.sum.interval_split_left (n m : ℕ) (h₁ : n < m) (f : ℕ → β) :
(interval n m).sum f = f n + (interval (n+1) m).sum f :=

lemma finset.sum.interval_split_right (n m : ℕ) (h : m > n) (f : ℕ → β) :
(interval n m).sum f = (interval n (m-1)).sum f + f (m-1) :=

lemma finset.sum.interval_reindex_left (k n m : ℕ) (h : k ≤ n) (f : ℕ → β) :
(interval n m).sum f = (interval (n-k) (m-k)).sum (λ x, f (x + k)) :=

lemma finset.sum.interval_reindex_right (k n m : ℕ) (f : ℕ → β) :
(interval n m).sum f = (interval (n+k) (m+k)).sum (λ x, f (x - k)) :=
```
which I've proved (and some infrastructure for `interval`).

#### [Scott Morrison (Nov 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271613):
The proofs still need a lot of golfing, but I think it's progress.

#### [Scott Morrison (Nov 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271669):
I would like to write some tactics to help with this, so you can just write things like "reindex_sum +3" in tactic mode, and it will `conv` it's way to the first `(interval n m).sum f`, and replace it with `(interval (n+3) (m+3)).sum (\lambda x, f (x-3))`, etc.

#### [Kevin Buzzard (Nov 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271672):
Now on to multinomial coefficients!

#### [Scott Morrison (Nov 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271675):
I'd also like to write a `conv` tactic for rewriting inside the summand of a `finset.sum`, that gives you a hypothesis saying you're actually in the domain.

#### [Scott Morrison (Nov 24 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271831):
If I'm going to clean this up for a PR, where should it go? In `big_operators.lean`? Or start a new file for summations over intervals in `nat`?

#### [Mario Carneiro (Nov 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271914):
I think a file for summations over intervals is appropriate

#### [Mario Carneiro (Nov 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271960):
I think the name should be `finset.Icc` though

#### [Mario Carneiro (Nov 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271964):
thiat gives us plenty of room for future variation

#### [Mario Carneiro (Nov 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271969):
er, `Ico`?

#### [Scott Morrison (Nov 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271987):
does that stand for "interval closed open"?

#### [Scott Morrison (Nov 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271989):
okay

#### [Mario Carneiro (Nov 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271995):
yeah, for compatibility with `set.Ico`

#### [Scott Morrison (Nov 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272044):
how about when I define `Ico` as a list/multiset/finset? Should those go in those three files, or in the file about summations over intervals?

#### [Mario Carneiro (Nov 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272047):
they can all be in the same file, I think

#### [Scott Morrison (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272061):
excellent, that means I can safely use tactics :-)

#### [Mario Carneiro (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272065):
oh, you mean the definitions themselves

#### [Scott Morrison (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272069):
yes...

#### [Mario Carneiro (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272071):
I guess they could go near `finset.range`

#### [Mario Carneiro (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272079):
but the development should go in its own file

#### [Mario Carneiro (Nov 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272119):
especially stuff combining sums and these sets

#### [Scott Morrison (Nov 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272126):
okay, that's what I've done so far --- in fact put them next to `list.range'`, `multiset.range`, and `finset.range`, and then the actual lemmas about dealing with `(Ico n m).sum` are in their own file.

#### [Mario Carneiro (Nov 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272130):
great

#### [Scott Morrison (Nov 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272164):
a few lemmas about slicing and dicing intervals use `tidy` to blast through... those proofs will have to be rewritten if they are going to live in `finset.lean` or earlier.

#### [Scott Morrison (Nov 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272167):
oh well...

#### [Scott Morrison (Nov 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272211):
(Not having `work_on_goal` available will make me cry, as it means I'll actually have to restructure the proofs `tidy` outputs.)

#### [Mario Carneiro (Nov 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272241):
oh no, structured proof

#### [Scott Morrison (Nov 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272346):
don't hold your breath :-) This PR is going to have some low-quality tactic proofs, that get the job done.

#### [Scott Morrison (Nov 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272542):
On the subject, if anyone wants to suggest to me some nice examples of proofs that rely on re-indexing and slicing and dicing sums, please do!

#### [Mario Carneiro (Nov 24 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272764):
you should look at `exp_add`

#### [Mario Carneiro (Nov 24 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272770):
and possibly quadratic reciprocity

#### [Patrick Massot (Nov 24 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273678):
Seriously guys, what's wrong with you? What the fuck is this thread?

#### [Patrick Massot (Nov 24 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273733):
I really think this proof assistant thing is going nowhere if we keep working like this, ignoring everything done by other people, including the ones who proved they can do much more than what we can currently do

#### [Patrick Massot (Nov 24 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273831):
I've pointed out repeatedly the existence of mathcomp's bigop library. They figured out all the issues, and they use it in linear algebra, in calculus, in finite group theory... I said it would very important to try to port that library to mathlib. Nobody cared. I started trying to do it, nobody cared. I struggled with nat substraction so I gave up for now. Then suddenly Scott asks many nat substraction questions, and, guess what, he is doing big operators again.

#### [Mario Carneiro (Nov 24 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273841):
The point is to see if our new techniques help with the proofs

#### [Patrick Massot (Nov 24 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273846):
I think the point is people thinking they are smarter than Gonthier and his friends

#### [Mario Carneiro (Nov 24 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273888):
if you get ahead of yourself writing theorems before the automation or appropriate structures and idioms come you get a load of unmaintainable hackery

#### [Mario Carneiro (Nov 24 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273891):
I'm afraid I can't read any of gonthier's proofs

#### [Patrick Massot (Nov 24 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273892):
Then why don't you ask?

#### [Mario Carneiro (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273899):
I highly respect him and I know he has a method to the madness but ssreflect style is not something I want to teach

#### [Patrick Massot (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273900):
We have Assia and Cyril who can read them, and explain everything

#### [Patrick Massot (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273905):
And they are really puzzled by our attitude

#### [Patrick Massot (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273906):
It has nothing to do with SSReflect crazyness

#### [Patrick Massot (Nov 24 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273981):
They thought about what are the right data structures, how to formulate the right induction principles for big operators, in what order to prove stuff

#### [Patrick Massot (Nov 24 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273983):
And it *works*

#### [Mario Carneiro (Nov 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273995):
sure, that's valuable

#### [Mario Carneiro (Nov 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274000):
it's the reason I periodically bring up metamath here, because many of our new problems are old problems somewhere else

#### [Mario Carneiro (Nov 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274002):
but I can't help that my experience is in metamath, not coq

#### [Mario Carneiro (Nov 24 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274061):
to get good information about how to do stuff in coq we would need Assia or Cyril guiding the path, and they have better things to do

#### [Patrick Massot (Nov 24 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274071):
What about letting them decide whether they have better things to do?

#### [Patrick Massot (Nov 24 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274078):
They both repeatedly offered to help us understand what's in mathcomp

#### [Mario Carneiro (Nov 24 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274122):
of course, if they actually think that's a good idea I'm all ears, that's not a rejection at all

#### [Mario Carneiro (Nov 24 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274127):
but in my view it's one more idea on the table, which can be considered equally among others

#### [Patrick Massot (Nov 24 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274133):
And what about trying to work together? @**Scott Morrison|110087** could you publicly write why you chose to restart from scratch instead of helping me in my attempt?

#### [Mario Carneiro (Nov 24 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274135):
I don't think we should blindly port any specific library

#### [Patrick Massot (Nov 24 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274179):
I'm not saying we should blindly do anything. Quite the contrary, I'm suggesting to open our eyes to the existing stuff

#### [Mario Carneiro (Nov 24 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274182):
are you referring to the notation for filtered sums of nats?

#### [Patrick Massot (Nov 24 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274195):
I don't think Lean would be there is Leo had the same attitude with existing software. And it doesn't mean Lean is "blindly ported"

#### [Patrick Massot (Nov 24 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274243):
It's not only about notations, I proved many lemmas in https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean. I know some stuff should be rethought, and everything could be improved, but why not starting there?

#### [Mario Carneiro (Nov 24 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274272):
one could ask the same of that approach... try it on `exp_sum`, try it on quadratic reciprocity, see if it helps

#### [Mario Carneiro (Nov 24 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274322):
this is not in any way a loaded question, it's a test bed for new ideas

#### [Mario Carneiro (Nov 24 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274332):
if it's a good approach, the proof will reflect that

#### [Mario Carneiro (Nov 24 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274352):
I don't know if scott's `Ico` will make things better than just using `range`, we need more data

#### [Patrick Massot (Nov 24 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274361):
It's lunch time, and this conversation is going nowhere anyway. Bye

#### [Kevin Buzzard (Nov 24 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275683):
@**Chris Hughes** do you have any comments on this? I remember a couple of times over the summer you saying you were having to battle with finite sums. What did you feel was missing from the library? Maybe it's time to compile a wishlist instead of all writing our own workarounds. Last year I wrote $$\sum_{i=1}^na_i=\sum_{j=1}^na_{n+1-j}$$ because I needed it for an example sheet question, and I remember it being a real pain.

#### [Mario Carneiro (Nov 24 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275731):
My impression of nat subtraction is it's best to avoid it appearing in lemmas to start with

#### [Kevin Buzzard (Nov 24 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275732):
Well it's in my lemma :-/

#### [Kevin Buzzard (Nov 24 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275737):
oh I see what you mean

#### [Mario Carneiro (Nov 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275776):
I wonder how much mileage you can get out of `finset.diag : finset (nat x nat) := {(0, n), ..., (n, 0)}`

#### [Kevin Buzzard (Nov 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275788):
you want me to prove that the function sending i to n+1-i is a bijection and then have some lemma about summing over a bijection, which actually might be in there already I guess. Is it?

#### [Chris Hughes (Nov 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275794):
I want to be able to sum between integers and naturals, and also do non commutative products over arbitrary lists. I think Patrick's approach seems to unify all these things nicely.

#### [Chris Hughes (Nov 24 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275801):
`sum_bij` is the lemma

#### [Mario Carneiro (Nov 24 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275810):
> the function sending i to n+1-i is

nope, you said minus

#### [Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275854):
the goal is to state the whole theorem without using minus

#### [Kevin Buzzard (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275855):
But I literally needed to prove that the sum of `F i` was equal to the sum of `F (n + 1 - i)`

#### [Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275856):
`finset.diag.map swap = finset.diag.reverse`

#### [Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275859):
no minus

#### [Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275861):
and `swap` is a bijection, etc etc

#### [Kevin Buzzard (Nov 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275873):
If I set as an example sheet question `binom n m = binom n (n - m)` you can't now avoid the minus. Are you suggesting that binom should take integer coefficients?

#### [Mario Carneiro (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275878):
if it's literally the input statement, then you should apply a lemma to get rid of it first, and work with that

#### [Kevin Buzzard (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275924):
so what lemma gets me rid of `n - m` in my input statement? :-/

#### [Mario Carneiro (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275926):
`binom n i = binom n j` when `i + j = n`

#### [Kevin Buzzard (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275927):
*boggle*

#### [Mario Carneiro (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275929):
aka `(i, j) in finset.diag`

#### [Mario Carneiro (Nov 24 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275990):
inductions go through so much more smoothly when there is no break in the function

#### [Kevin Buzzard (Nov 24 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275996):
My theorem isn't even true when `m > n`

#### [Mario Carneiro (Nov 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275999):
my theorem can't even have m > n

#### [Kevin Buzzard (Nov 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276005):
right

#### [Mario Carneiro (Nov 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276016):
of course you can substitute in `n` in that statement, and then it's an easy induction on i,j

#### [Mario Carneiro (Nov 24 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276062):
in general you might also want to generalize i,j and do induction on n, or something related

#### [Kevin Buzzard (Nov 24 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276073):
So one way of proving $$s : \mathbb{Z} :=\sum_{i=0}^{2n+1}(-1)^i\binom{2n+1}{i}$$ is 0 is to set $$j=2n+1-i$$ and note that this substitution proves that $$s=-s$$. You would do all this without any nat subtraction?

#### [Scott Morrison (Nov 24 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148287845):
> @Scott Morrison could you publicly write why you chose to restart from scratch instead of helping me in my attempt?

@**Patrick Massot**, my apologies if it appeared that I was intentionally ignoring your work at <https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean>. In fact I didn't even know that it existed. I remember looking at the top of `big_operators.lean` and thinking "huh, that's funny, Patrick's name isn't in the `Authors` line, I thought he helped write this file". But that was the extent of my memory of what you'd done. :-(

I'd be very happy to discuss what you wrote already and to make some plans about how to proceed.

Right now I need to go out for a while, but I'll look more closely at your repo soon. There is a lot there, and I see that working over `int` rather than `nat` index sets makes life easier. However I don't much like that you've "rolled your own" subsets built into your `bigop` notation, containing both a `list I` and an `I -> Prop`, rather than using existing technology (e.g. `multiset`, and `filter`). I think it's best if we decouple as much as possible here.

#### [Scott Morrison (Nov 25 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294592):
@**Patrick Massot**, moreover, I will attempt to read the big operators paper. :-)

#### [Scott Morrison (Nov 25 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294612):
I see already that your `list I` and `I -> Prop` is imitating what they do, although my limited understanding so far is that they do something more general than `list I`.

#### [Patrick Massot (Nov 25 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294656):
I just came back from the hospital after some climbing session, so I didn't see your message earlier

#### [Patrick Massot (Nov 25 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294663):
I'm sorry I was so upset this morning, but I'm really tired of these problems.

#### [Patrick Massot (Nov 25 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294712):
I didn't "roll my own subset" rather using filter, everything is based on filter. The question is the interface question, and this is precisely the kind of question where I think it makes sense to have a look at what mathcomp successfully used

#### [Patrick Massot (Nov 25 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294783):
I moved from nat to int mostly because of nat substraction hell, but also because sums indexed by integers do arise, for instance with Fourier series

#### [Scott Morrison (Nov 25 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148302363):
Okay, a few disorganised thoughts post bike-ride:
1) While I absolutely agree that we want "generic operation" big operations, I mostly wanted to explore writing useful tactics for manipulating big operations, and thought that testing this out more narrowly (just with `finset.sum` at first) would be helpful.

2) The sort of tactics I have in mind are: `shift 5` (and `shift -2`, and `shift_left`, etc.), `split_first`, `split_at`, etc, and very importantly making it possible to `conv` your way inside the summand, and be given a hypothesis that you're in the domain, so you can perform appropriate conditional rewrites. There are many more tactics suitable for multivariable big operations, changing between int and nat, etc. (Does the Coq library provide tactic level support?)

3) I feel pretty dubious about the Coq model where there is apparently a multiset, and a filter, being carried around in the notation. It then seems there are two places we can add an extra filter: on the actual multiset, and composed with the filter. There's then an extra dimension worth of rewriting to move the filters back on forth. Why cause yourself that trouble? (I still haven't read the Coq paper -- so this question is perhaps an invitation for someone to point me to a relevant comment.)

4) In Patrick's prototype, I think there's a real semantic problem with using a `list I` and a `I -> Prop`. What is the meaning of repeated elements in the list? Presumably that we're summing with multiplicity. What is the meaning of the order of the list? It's strange that the filter removes all copies of some element --- surely you want to be able to control multiplicities directly if you're summing with multiplicity? I suspect here that the answer is just to change from `list I` to `finset I`.

5) A more fundamental objection to following the Coq approach is indexing by the binary operation, rather than the carrier type, is completely alien to the rest of the design in Lean. Pursuing this for a big operators library seems likely to cause of lot of friction. In their paper (okay, I've now read the first 3 pages) they say they don't want to index by the carrier type because of course there is more than one relevant operation we want bigops for, for a single type (their example is nat, with +,*, max, min, lcm, gcd, and so on). I think this is actually an easy problem to solve, that we've solved elsewhere in mathlib by "wrapper types", and providing alternative instances for the wrapper. For example we might define 

```
def as_gcd_monoid (X : Type) := X
```

and then
```
instance [has_gcd X] : has_mul (as_gcd_monoid X) := ...
```
and finally 
```
def finset.gcd (t : finset X) (f : X -> Y) [has_gcd Y] := @finset.big_op X (as_gcd_monoid Y) t (\lambda x, f x)
```
(or something like that... )

#### [Kenny Lau (Nov 25 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148302414):
don't drive and derive...

#### [Scott Morrison (Nov 25 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148302765):
Also, if we're going to make some progress on big ops, I think it would be great if we can ask Assia and Cyril for some advice. I'd like to do a few experiments perhaps first (actually try writing some of the `conv` style tactics for manipulating sums, and seeing if it really is okay to index by carrier type), but maybe we could even schedule a skype call with whoever is interested so we can ask them some questions.

#### [Patrick Massot (Nov 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148314025):
Scott, I think you completely missed the point that we want to handle non-commutative operations

#### [Patrick Massot (Nov 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148314037):
Next, I think the list + predicate is there to handle the very common case of summing on a range of integers subjects to conditions, like "sum for n from 1 to N, with n odd"

#### [Patrick Massot (Nov 25 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148314038):
I'm not sure I understand what you'd like your tactic to do that a rewriting lemma couldn't

#### [Scott Morrison (Nov 25 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335113):
I did miss the intention to also do noncommutative things. What do you have in mind? (And in any case, while we're writing prototypes, I'd prefer to work in simpler special cases, so I suspect I'll propose we ignore the noncommutative stuff for now anyway.)

#### [Scott Morrison (Nov 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335286):
It might be good to at some point list all the things that conceivably could count as "big operations". Here's a sampling of things that could conceivably be in scope:
* sums, 
* products, 
* unions, 
* maxs, 
* gcds, 
* convergent sums, 
* integrals, 
* limits (e.g. as x goes to a), 
* limits (of a functor over a diagram).

#### [Scott Morrison (Nov 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335293):
But Patrick, why not just filter the list, if you want to sum over odd integers? I really don't understand why you want to carry around an "unapplied" filter.

#### [Scott Morrison (Nov 25 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335464):
And I think my point stands, even if we're going to do noncommutative operations: a list is a bad way to model a ordered set. Using a list commits us to dealing with multiplicities, and I don't think that's what you intend.

#### [Scott Morrison (Nov 25 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335685):
Regarding tactics: at the moment, rewriting inside the summand is a royal pain. As far as I can see, you need to use `rw sum_congr`, having carefully prepared the equation you want to rewrite along ahead of time in the form `\forall x \in t, f x  = g x`. `conv` completely fails to enter the summand giving you appropriate hypotheses, and this could easily be fixed.

#### [Scott Morrison (Nov 25 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335754):
Going back to my "big list of big operations"... I think it would be a bad idea to try to write a framework so general it encompasses all of these.

#### [Chris Hughes (Nov 25 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335806):
So for non commutative stuff, might it be better to use a finset with `linear_order` on the indexing type? I like that idea.

#### [Scott Morrison (Nov 26 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335959):
It's possible. I'm not sure though how to make the commutative case a specialisation of the non-commutative case.

#### [Scott Morrison (Nov 26 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335976):
Another possibility is to have the range of the big operation be a "list without duplicates" (a new type?), and then have extra lemmas that apply when the operation is known to be commutative, and that list comes from a finset.

#### [Scott Morrison (Nov 26 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335979):
That design would mean lemmas proved about the noncommutative case would specialise.

#### [Chris Hughes (Nov 26 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336031):
Are there any concrete examples of where a list with duplicates is annoying?

#### [Chris Hughes (Nov 26 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336037):
I don't want to ask for that proof obligation without a good reason.

#### [Scott Morrison (Nov 26 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336105):
I ... guess not.

#### [Scott Morrison (Nov 26 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336148):
One problem is perhaps getting a list back out of a finset in the first place.

#### [Scott Morrison (Nov 26 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336160):
I'm still unhappy about carrying along unapplied predicates, but I'm now open to the idea of using a list to represent the range.

#### [Scott Morrison (Nov 26 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148337035):
Just thinking out loud for a moment here: I wonder about really embracing the typeclass system here. What if we did big operations over arbitrary types A, and require an extra piece of evidence, possibly depending on the summand function `f : A -> X` that the big operation makes sense. There could be lots of mechanisms here:
* `[fintype A] [ordered A] [monoid X]` (summing over an ordered finite set)
* `[fintype A] [comm_monoid X]` (summing over a unordered finite set)
* with `f : (near a) -> X`, where `def near {A : Type} (a : A) := A`, the evidence for `lim_{a : near A} f` could be computed from something like `[topological_space A] [continuous_at f a]`
* `[normed_space X]  [absolute_convergence f]`,
* `[category A] [category X] [is_functorial f] [has_limits_of_shape A]` (computing a limit)
Could one prove enough of the needed lemmas in this ridiculous generality that it would be worth doing?

#### [Chris Hughes (Nov 26 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148337512):
distributivity of multiplication is true for lots of types of sums. Not sure how you'd state or prove that though. Unless you made a new class for more or less every lemma.

#### [Johan Commelin (Nov 26 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148345914):
@**Scott Morrison|110087** I think that limits (in topology or category theory) are a completely different kind of big operators from the others. All the others have some sort of iterative or recursive aspect to them. (Btw, we could add tensor products to your big list.) For those iterative instances I think it will probably be very useful to also have `product L` if `L` is a list of matrices. So we do care about the non-commutative case, I think.
About tactics vs rewrites: I completely agree that it is crucial that we have slick rewriting of the summand, and currently this is a pain. I also agree with @**Patrick Massot** That most of the "slicing and dicing" probably doesn't need tactics, but could be done with regular rewrite lemmas, because that doesn't touch the summand.
But making `conv` access the summand would be get you a major hooray from my side! I just recently reexperienced how awful it is, when I tried to prove that `boundary_boundary` lemma in the simplicial branch. You get nested sums over finsets, and manipulating them is a silly gamble where you just hope that `simp` and `erw` drill down far enough to make a bit of progress.

#### [Scott Morrison (Nov 26 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148351986):
The other tactic support I realised we can do is unrolling sums of "explicit length". Just like my `fin_cases` command, we can have a single tactic that takes for example $\sum_{n=k}^{k+3} f(n)$ and replaces it with $f(k) + f(k+1) + f(k+2) + f(k+3)$. This is quite a pain to achieve with pure rewriting, and is not so bad to automate in tactic mode.

#### [Scott Morrison (Nov 26 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352070):
I'm not sure sure that limits (in category theory or in topology) are completely different big operators. If you just categorify your natural numbers as finite sets, a sum of natural numbers is just the colimit of the discrete diagram of those sets (and a product is just the colimit)! Nevertheless, I wasn't seriously suggested we do this --- in fact I was setting up a straw man to try to argue we should not go for maximum generality. :-)

#### [Johan Commelin (Nov 26 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352123):
```quote
The other tactic support I realised we can do is unrolling sums of "explicit length". Just like my `fin_cases` command, we can have a single tactic that takes for example $\sum_{n=k}^{k+3} f(n)$ and replaces it with $f(k) + f(k+1) + f(k+2) + f(k+3)$. This is quite a pain to achieve with pure rewriting, and is not so bad to automate in tactic mode.
```
 I suppose this could be done with `repeat { rw split_last }, simp`.

#### [Johan Commelin (Nov 26 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352148):
But I agree that an `unroll_bigop` tactic might make sense.

#### [Scott Morrison (Nov 26 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352194):
I'm not quite convinced it's that easy, but perhaps I'm thinking about the `fin_cases` situation, which was quite a bit more painful.

#### [Patrick Massot (Nov 26 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148356624):
I agree it seems to make sense to drop the predicate part, at least until we see a need for it, although I'll try to ask Cyril and Assia before doing so. But non-commutative operators are crucial. I started this project because I wanted to do group theory. And I still hope that one day we will be able to handle differential forms as well.  Now that I think about it, I'm not sure I could find any big operator in one of my papers that uses a commutative operation.

#### [Patrick Massot (Nov 26 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148367393):
I worked on my bigop attempt today, reaching a new sorry-free equilibrium point. I did find a use for the predicate thing as a convenient way to prove stuff, keeping track of information.

#### [Patrick Massot (Nov 26 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148371544):
Ok, I pushed https://github.com/leanprover-community/mathlib/tree/bigop Any contributor is very welcome. In particular, cleaning up https://github.com/leanprover-community/mathlib/blob/bigop/pending_lemmas.lean  requires no big operators skills, only knowing mathlib (or searching efficiently), or being good at either list or nat vs int bashing.

