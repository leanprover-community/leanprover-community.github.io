---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/58787428BanachContraction.html
---

## Stream: [PR reviews](index.html)
### Topic: [#428 Banach Contraction](58787428BanachContraction.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 11 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151452941):
PR by @**Rohan Mitta**.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Dec 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151607136):
I edited this PR based on feedback from Patrick, I think it's ready now but any other feedback would be appreciated!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 13 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151618862):
I think there is still overlap with existing stuff, eg https://github.com/leanprover/mathlib/blob/master/data/real/cau_seq_filter.lean#L164

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 13 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151618877):
And I'm sure you can extract lemmas from the Banach contraction proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 15 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151834889):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 15 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151834942):
In fact I don't think I found a use for anything in cau_seq_filter.lean
   (Edit : I see this was because I didn't go beyond the first half of metric_sequences.lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 15 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151835097):
We've got `sequentially_complete.tendsto_div`used in metric_sequences.lean, in
```lean
theorem lim_sequence_of_mem_closure {Y : set α} {a : α} (H : a ∈ closure Y) :
∃ (f : ℕ → α) (H1 : ∀ (n : ℕ), f n ∈ Y), filter.tendsto f at_top (nhds a)
```
But nothing from metric_sequences.lean is actually used in banach_contraction.lean any more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036009):
Isn't this basically constructive? It's a shame I that we have to mark as noncomputable the function to return the fixed point because the definition of completeness uses an exists.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036085):
It looks very non-computable to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036140):
This is what we keep repeating to our students: compactness and completeness give you elements for free! Constructive maths don't give anything for free, they want you to suffer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036161):
Why is that? If I have a cauchy sequence of, say, reals then I have constructed a real

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036192):
This is a very special case, because you constructed real like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036251):
And it's breaking an abstraction barrier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036288):
We want to use this theorem for many complete spaces which are not constructed as completions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036327):
OK. Can you give me an example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036342):
Differentiable functions for instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036376):
Say you want to prove Cauchy-Lipschitz theorem about existence and uniqueness of solutions to nice ordinary differential equations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152044239):
I think @Rohan Mitta will probably want to kill me because I put Mario off reviewing this :oh_no:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152044258):
I panicked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045032):
if you want some more tips: the style of tactic indentation isn't quite standard, there are some funny names like `Banach's_fixed_point` and generally nonconforming names (they should be more or less strictly based on reading the symbols), `fixed_point_of_iteration_limit'` and `fixed_point_of_iteration_limit` are the same, the main theorem is far too long (I think it can be shorter, and this should also be lemma'd if not)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045161):
I wrote that last remark many times, so I guess they'll need more help there. But I really want to finish completions (before the end of July 2018...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045274):
We do have a much shorter one here https://github.com/agjftucker/mathlib/blob/Banach/analysis/topology/banach_contraction.lean#L253

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045404):
That's much better!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045488):
What's the difference with the next statement?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045558):
Why can't you get rid of `0 ≤ K →`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045561):
The statement is much the same but the method is different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045676):
I think because otherwise you need inhabiteds ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045720):
In fact you need at least two distinct points

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045730):
the space is already inhabited

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045736):
why two points?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045796):
Oh I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045799):
crazy computers...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045811):
To prove that K >=0 I think you need two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045947):
yeah, but if the space has only one point then it's a fixed point :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045958):
Yeah!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045970):
Let's begin with this very natural case disjunction!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045977):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045995):
I would suggest putting `K >= 0` in the definition of lipschitz

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152046020):
OK I can change that in the main theorem :) But I might still need some `0 \leq K` in the preceding lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 17 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152054653):
```quote
I would suggest putting `K >= 0` in the definition of lipschitz
```
 Yes, definitely -- I played a lot with this in Isabelle, and it turned out to be much more manageable once I enforced `K >= 0`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152054798):
will do. Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 17 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152056937):
```quote
Let's begin with this very natural case disjunction!
```
 That's pretty much how the proof I was taught as an undergraduate began!


{% endraw %}
