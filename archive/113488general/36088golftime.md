---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36088golftime.html
---

## Stream: [general](index.html)
### Topic: [golf time](36088golftime.html)

---

#### [Reid Barton (May 11 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126431532):
```lean
open finset
example {n : ℕ} : range (n+1) \ range n = {n} :=
```

#### [Chris Hughes (May 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126433149):
Not very pleased with my effort. I certainly lose points for stability
```lean
example {n : ℕ} : range (n+1) \ range n = {n} := 
ext.2 $ λ a, ⟨by simp [mem_sdiff, mem_range, le_iff_eq_or_lt.symm]; 
  simp [le_antisymm_iff] {contextual := tt},
    by simp {contextual := tt}⟩
```

#### [Chris Hughes (May 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126433411):
More stable version
```lean
example {n : ℕ} : range (n+1) \ range n = {n} := 
ext.2 $ λ a, ⟨by rw [mem_sdiff, mem_range, mem_range, singleton_eq_singleton, mem_singleton];
  exact λ h, le_antisymm (nat.le_of_lt_succ h.1) (le_of_not_gt h.2),
  by simp {contextual := tt}⟩
```

#### [Kevin Buzzard (May 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126435105):
It's this sort of question that gives Lean a bad name amongst mathematicians.

#### [Kevin Buzzard (May 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126435106):
"it's obvious"? ;-)

#### [Mario Carneiro (May 12 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126440450):
```
example {n : ℕ} : range (n+1) \ range n = {n} :=
ext.2 $ by simp [-range_succ, nat.lt_succ_iff, le_antisymm_iff]
```

#### [Mario Carneiro (May 12 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126440496):
i.e. "it's obvious"

#### [Kevin Buzzard (May 12 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126455763):
:-)

#### [Kevin Buzzard (May 12 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126455765):
I'm not so sure that one of my first year undergraduates would find that proof obvious to spot :-)

#### [Reid Barton (May 12 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126465086):
When do we get `omega` or a Presburger arithmetic solver?

#### [Andrew Ashworth (May 14 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126521067):
```quote
When do we get `omega` or a Presburger arithmetic solver?
```
You're not the first person to ask this in the chat, hah. The answer is: whenever a motivated contributer decides to port the Coq implementation to Lean. Leo and the other developers are not interested in doing this work as it is non-trivial and not academically interesting, so it can't lead to something publishable.

#### [Mario Carneiro (May 14 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126521751):
I think it also has dubious merit, I'm not sure that we actually have goals that fit the pattern very often to begin with

#### [Mario Carneiro (May 14 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126521812):
That said, I know that Seul Baek (my fellow CMU PhD) has implemented Cooper's algorithm for linear arithmetic over integers, and maybe he will pop in here someday to show it off

#### [Andrew Ashworth (May 14 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126523011):
Well, in defense of the people who really want omega, it's not so much that many goals may need a Presburger arith solver. However, when you do have a problem of that type, a tactic that solves them in one tactic invocation is convenient. It has a well-defined scope and application, and is not heuristics-based, so it will always succeed if the problem is appropriate.

#### [Andrew Ashworth (May 14 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126523100):
In Software Foundations Vol 3, which discusses verified data structures, the author uses omega quite frequently

#### [Kevin Buzzard (May 14 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126534010):
As @**Andrew Ashworth** points out, this question (porting omega) does come up again from time to time. Can someone give me an idea of how much work this would actually be? Obviously I am in no position to do it because I only know epsilon about tactics and have no time anyway, and perhaps one should at least wait until Lean 4 before embarking on such a project, but in the long term is it the sort of thing one can get a Masters student to do for a project, for example? I just have no  idea.

#### [Andrew Ashworth (May 14 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126546657):
Well, looking at the Coq source, it seems omega is around ~3500 lines of mixed ML and Ltac. For new work, you can probably estimate ~30 lines of finished, complete code / day, leading to a time estimate of ~120 days of full-time work. However, this isn't a completely new rewrite, but a translation of existing code, so maybe handwave and cut the time required in half... so about two months of work.

#### [Johan Commelin (May 15 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582480):
I would be interested in feedback on the definition of `\sigma`:
```lean
import data.fin order.basic

instance {n : ℕ} : linear_order (fin n) := {le := λ a b, nat.less_than_or_equal a.1 b.1,
  le_refl := λ a, @nat.le_refl a.1,
  le_trans := λ a b c, @nat.le_trans a.1 b.1 c.1,
  le_antisymm := λ a b H1 H2, fin.eq_of_veq $ @nat.le_antisymm a b H1 H2,
  le_total := λ a b, @nat.le_total a b,
  lt := λ a b, nat.lt a.1 b.1,
  lt_iff_le_not_le := λ a b, @nat.lt_iff_le_not_le a.1 b.1}

def σ {n : ℕ} (i : fin n) (a : fin (n+1)) : fin n :=
⟨if a ≤ raise_fin i then a else nat.pred a,
  begin
    by_cases (a ≤ raise_fin i),
    { rw [if_pos h], exact (lt_of_le_of_lt h i.2) },
    { rw [if_neg h], simp at *,
    have apos : a > 0 := begin
        show 0 < a,
        apply lt_of_le_of_lt (nat.zero_le _) h,
    end, 
    show nat.succ (nat.pred a.1) ≤ n,
    rw nat.succ_pred_eq_of_pos apos,
    exact nat.pred_le_pred a.2 }
  end⟩
```

#### [Mario Carneiro (May 15 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582865):
You could skip the whole `linear_order` business by writing the if condition as `a.1 <= i.1`

#### [Johan Commelin (May 15 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582980):
Yes, that is true... but I want to prove stuff about monotone functions `fin n \to fin m`

#### [Johan Commelin (May 15 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582982):
So I need it when I start using `\sigma`

#### [Mario Carneiro (May 15 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126583130):
golfed:
```
def σ {n : ℕ} (i : fin n) (a : fin (n+1)) : fin n :=
⟨if a.1 ≤ i.1 then a else nat.pred a,
  begin
    by_cases a.1 ≤ i.1; simp [h],
    { exact lt_of_le_of_lt h i.2 },
    { exact (nat.sub_lt_right_iff_lt_add
        (lt_of_le_of_lt (nat.zero_le i.1) (not_le.1 h))).2 a.2 },
  end⟩
```
what's with the mysterious name?

#### [Johan Commelin (May 15 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126583282):
Well, https://en.wikipedia.org/wiki/Simplicial_set#Face_and_degeneracy_maps

#### [Johan Commelin (May 15 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126583289):
And thanks for golfing!!

#### [Patrick Massot (May 15 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126584504):
Nice idea to do simplicial sets!

#### [Sean Leather (May 15 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126586836):
(deleted)

#### [Sean Leather (May 15 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126586921):
Oh, never mind.

#### [Sean Leather (May 15 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587382):
Here's my adaptation of Mario's version:

```lean
def σ {n : ℕ} (i : fin n) (a : fin (n+1)) : fin n :=
if h : a.val ≤ i.val then
  ⟨a.val, lt_of_le_of_lt h i.is_lt⟩
else
  ⟨a.val.pred, (nat.sub_lt_right_iff_lt_add (lt_of_le_of_lt i.val.zero_le (not_le.mp h))).mpr a.is_lt⟩
```

#### [Johan Commelin (May 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587558):
That doesn't parse, right? The `h` in the `then`-part is undefined.

#### [Sean Leather (May 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587563):
1. I find using the structure field names (`val`, `is_lt`) and `mpr` to be better documentation than `.1` and `.2`; I usually reserve the latter for “obvious” uses such as `and`,  `sigma`, etc.
2. The use of tactics in a definition momentarily confused me into thinking it was a theorem.
3. The duplicate casing with both `if` and `by_cases` seems redundant to me.

#### [Sean Leather (May 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587572):
```quote
That doesn't parse, right? The `h` in the `then`-part is undefined.
```
It does parse in my Lean. I don't think it's been changed.

#### [Johan Commelin (May 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587617):
Aah, sorry, I didn't copy your `h` from the line above...

#### [Sean Leather (May 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587624):
`if then else` is notation for `ite` and `if h : p then else` is notation for `dite`.

#### [Sean Leather (May 15 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587806):
Also, I could be wrong, but I think you might find it easier to work with the definition without tactics in it. At the very least, you know more clearly what you have to prove if you unfold it.

#### [Sean Leather (May 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587819):
Along the same lines, having just `if` instead of `if` and `by_cases` should make it easier to work with.

#### [Johan Commelin (May 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587929):
Well... until you try to prove anything about the composition of two such maps...

#### [Johan Commelin (May 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587930):
Like I am trying now

#### [Johan Commelin (May 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587934):
If you unfold, you suddenly have a page-filling goal (-;

#### [Kevin Buzzard (May 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587975):
```quote
Also, I could be wrong, but I think you might find it easier to work with the definition without tactics in it. At the very least, you know more clearly what you have to prove if you unfold it.
```
It's only the proof part of the def that involves tactics, so maybe this is OK?

#### [Sean Leather (May 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587984):
That may be true.

#### [Kevin Buzzard (May 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588029):
OTOH I am a bit wary of Johan's unfolding comment above...

#### [Sean Leather (May 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588087):
```quote
If you unfold, you suddenly have a page-filling goal (-;
```
Is there a difference between the goals using the different definitions of `σ`?

#### [Johan Commelin (May 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588091):
Not too much

#### [Johan Commelin (May 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588102):
But you get stuff of the form `(\lambda h, ...)` where you first didn't have the `\lambda`. I think this has to do with `ite` vs `dite`

#### [Kevin Buzzard (May 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588107):
Johan, let me echo other people's comments that it's a great idea to do whatever it is that you're doing, which might be simplicial homology of a topological space as far as I can see. I definitely learnt the most about how Lean works at times when I was engaged in actually writing non-trivial amounts of non-trivial code, and even if I look back at my schemes work and perhaps regret some earlier design decisions (e.g. a cheap definition of the structure presheaf on an affine scheme which now has to be seriously reworked) I still learnt masses of stuff. You might well end up with a canonical "bad lecture" -- some definition of cohomology, plus not one single example worked out :-)

#### [Johan Commelin (May 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588149):
Hehe

#### [Kevin Buzzard (May 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588151):
But this raises the question of whether lean code is supposed to be used to teach people mathematics, and I have pretty much decided that the answer should be "no, at least for the code I write".

#### [Kevin Buzzard (May 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588153):
I'm going to see Larry Paulson on Tuesday who I think has very different ideas about this.

#### [Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588160):
At some point in the future we need readable code, I think

#### [Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588166):
Why?

#### [Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588170):
Why can't we have unreadable code with readable documentation and comments instead?

#### [Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588173):
Ok, sure

#### [Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588174):
"This is what is going on here"

#### [Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588177):
But so far I haven't seen much comments in Lean code

#### [Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588181):
`simp;cc;finish`

#### [Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588183):
I know you have some comments,...

#### [Johan Commelin (May 15 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588233):
but the ratio of comments/code in mathlib is pretty low

#### [Kevin Buzzard (May 15 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588234):
But that's because most code you've seen has probably been written by Mario, and he's not a big commenter

#### [Johan Commelin (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588243):
That's what you get when you speak Lean faster then anyone else (-;

#### [Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588247):
OTOH one might argue that much of the mathlib code is "elementary" in the sense that it is proving lemmas which are trivial to a mathematician

#### [Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588250):
so one might argue that this code does not need comments.

#### [Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588253):
"I am proving this by induction"

#### [Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588254):
"as any mathematician would"

#### [Johan Commelin (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588258):
Well, I often have quite a hard time figuring out *which* lemma is being proven

#### [Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588259):
"it's just that mathematicians can't read the argument without training"

#### [Johan Commelin (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588262):
Because the type signatures can be pretty unreadable as well

#### [Johan Commelin (May 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588306):
And I think that we should at least make sure that type signatures are readable

#### [Johan Commelin (May 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588315):
That's why I really loved Reid's improvement of my statement of the five lemma... He just put everything into a diagram!

#### [Kevin Buzzard (May 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588320):
Yeah that was great :-)

#### [Patrick Massot (May 15 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588394):
At some point Mario added a lot of comments on top of unreadable definitions and statements

#### [Patrick Massot (May 15 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588398):
But I don't know if this was continued with new stuff in mathlib

#### [Mario Carneiro (May 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126609677):
More precisely, I added comments on every `def` and `class` and `structure` and `inductive`. I think that is still mostly the case, I can do another pass to make sure

