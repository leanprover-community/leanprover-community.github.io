---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43357simpisamazing.html
---

## [general](index.html)
### [simp is amazing](43357simpisamazing.html)

#### [Chris Hughes (Mar 04 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123265688):
I was proving some lemmas about disjoint finsets, and I was amazed to find that this goal was solved by `simp {contextual := tt}`, when I previously had a 10 line proof.
```lean
α : Type u_1,
_inst_1 : decidable_eq α,
s : finset α
⊢ ∀ ⦃a : α⦄ {s : finset α},
    a ∉ s →
    (∀ (t : finset α), disjoint s t → card (s ∪ t) = card s + card t) →
    ∀ (t : finset α), disjoint (insert a s) t → card (insert a s ∪ t) = card (insert a s) + card t
```
To solve this goal before I noticed that `simp` did it, I had to rewrite `card (insert a s) + card t` to `card s + card (insert a t)` which involves using `rw ← card_insert_of_not_mem`, where card_insert_of_not_mem is a `simp` lemma, used in the wrong direction, so I'm wondering how simp managed it. The only `@[simp]` lemma it used which isn't already in the library is `disjoint_insert_left [decidable_eq α] {a : α} {s t : finset α} :  disjoint (insert a s) t ↔ a ∉ t ∧ disjoint s t`

#### [Kevin Buzzard (Mar 04 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123266504):
Chris -- you can find out how simp did it -- I ran into this when preparing my blog post on congruence being an equivalence relation

#### [Kevin Buzzard (Mar 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123266547):
and I wrote it up as something-which-might-be-useful-as-a-document at

#### [Kevin Buzzard (Mar 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123266550):
https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md

#### [Kevin Buzzard (Mar 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123266551):
Do you want to edit it and then we could submit it as a PR?

#### [Kevin Buzzard (Mar 04 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123266554):
I still have no idea how simp works in practice, all I know is that it randomly looks through its database and tries stuff. I have no idea about its strategy though.

#### [Chris Hughes (Mar 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123267383):
It's way more sophisticated than I previously thought. Another capability that I only discovered today is that if a simp lemma of the form `p → x = y` can be used if there is a proof of p in the context. Looking at the trace I can see that it didn't use the method I used, and instead rewrote `card (insert a s ∪ t)` to `card (insert a (s ∪ t))` and then must have somehow worked out that it should try to prove and prove `a ∉  s ∪ t`, from proofs of `a ∉ s` and `a ∉ t` in the context, so it could use card_insert_of_not_mem, which seems quite sophisticated to me. I can't add to the docs really, because I don't know what's going on.

#### [Andrew Ashworth (Mar 04 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123267882):
i like how you mention Prolog-like search in your simp.md

#### [Andrew Ashworth (Mar 04 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123267935):
I would amend that to backtracking search, as described in https://en.wikipedia.org/wiki/Backtracking, if you want to give a good description of it

#### [Andrew Ashworth (Mar 04 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268115):
I agree with you that these days, nobody has heard of Prolog

#### [Kevin Buzzard (Mar 04 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268168):
```quote
I agree with you that these days, nobody has heard of Prolog
```
Oh the reason I mention it is far more mundane! I have no CS background at all and had no idea what a Prolog-like search meant but the phrase is mentioned several times in the Lean docs so I just started using it as meaning "something I don't understand at all" because I had no idea how simp worked

#### [Gabriel Ebner (Mar 04 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268207):
I'm not sure I like the word backtracking here.  The only place where simp backtracks in any meaningful sense is when you have a conditional simp lemma (such as `p -> x = y` above), and simp fails to discharge the assumption.  Otherwise simp never goes back to a previous step.

#### [Andrew Ashworth (Mar 04 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268208):
i've been mislead

#### [Kevin Buzzard (Mar 04 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268209):
I am going to PR these simp docs in the hope that other people can actually make them correct and helpful.

#### [Andrew Ashworth (Mar 04 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268218):
tpil describes simp as a prolog-like search, which in my mind means backtracking

#### [Gabriel Ebner (Mar 04 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268263):
Where does TPIL say that?  I can't find either backtrack or prolog.

#### [Gabriel Ebner (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268267):
If you're looking for a short buzzwordy description, I'd use "simp applies a conditional term rewriting system".

#### [Andrew Ashworth (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268271):
hmm, looking at the current version, it mentions it when describing the type class instance resolution mechanism

#### [Kevin Buzzard (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268275):
I can quite believe I've conflated the two. As I say, I was using the entire phrase as a joke for a while

#### [Gabriel Ebner (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268276):
Indeed, type class inference is essentially a version of λProlog and uses backtracking.

#### [Kevin Buzzard (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268315):
I would just use it to describe anything I couldn't understand.

#### [Andrew Ashworth (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268316):
i'll just claim that i was bamboozled by kevin :)

#### [Kevin Buzzard (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268317):
I'll fix it

#### [Gabriel Ebner (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268318):
Prolog = try to `apply` all the theorems you know and repeat for the generated subgoals

#### [Kevin Buzzard (Mar 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268378):
https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md

#### [Gabriel Ebner (Mar 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268379):
With a bit of artistic license:
```lean
meta def prolog (lemmas : list name) : tactic unit :=
first $ lemmas.for $ λl, applyc l; prolog
```

#### [Gabriel Ebner (Mar 04 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268428):
Re: documentation.  If you mention congruence, you could show off simp's support for congruence relations.  If you show reflexivity and transitivity for `cong`, and have congruence lemmas for `+`, etc., then you can rewrite with congruences as if they were equations.

#### [Patrick Massot (Mar 04 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268470):
I think you should mention the `@[simp] lemma my_lemma : fact <-> true` trick

#### [Patrick Massot (Mar 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123268480):
especially since it could be confusing when reading existing Lean code

#### [Reid Barton (Mar 04 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123272385):
@**Chris Hughes**, if you just want to see what simp ended up doing (and not all the things that it didn't do), then I've found `set_option trace.simplify.rewrite true` to produce a more manageable amount of information.

#### [Kevin Buzzard (Mar 04 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123273896):
I've added Reid's comment. Patrick -- is this some trick for getting simp to know about facts which are not necessarily of the form `x=y` or `x iff y`? Assuming it is I've added it too. I am not sure I am competent enough to add Gabriel's comment so it's unedited at the bottom of https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md

#### [Patrick Massot (Mar 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123273963):
Yes. It's more a comment to your first bullet than a third one

#### [Patrick Massot (Mar 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp is amazing/near/123274002):
If you want a cheap way to document stuff about simp not in TPIL you can also search for simp in https://github.com/leanprover/lean/blob/master/doc/changes.md

