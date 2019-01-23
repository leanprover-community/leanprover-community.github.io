---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48024simplemmas.html
---

## Stream: [general](index.html)
### Topic: [simp_lemmas](48024simplemmas.html)

---

#### [Edward Ayers (Oct 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135532880):
What is the difference between a 'simp' and a 'congr' below?
```lean
meta constant simp_lemmas.add_simp : simp_lemmas → name → tactic simp_lemmas
meta constant simp_lemmas.add_congr : simp_lemmas → name → tactic simp_lemmas
```

#### [Edward Ayers (Oct 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135533034):
My guess is that anything of the form `lhs = rhs` goes in `add_congr` so `simp` knows its a congruence relation.

In the C++, I can see that there is a pair of tables for each equivalence relation we have simp lemmas for. One table contains congruences and the other contains simps. So I guess for `=` and `<->` the simps table would be empty? What would be an example of a relation where both the congr and simps table would be occupied?

 I remember hearing somewhere that simp can support arbitrary congruence relations.

#### [Edward Ayers (Oct 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135533129):
I'm interested in expanding on this from `simp.md` in mathlib's docs.
```quote
### Something that could be added later on:

"Re: documentation. If you mention congruence, you could show off simp's support for congruence relations. If you show reflexivity and transitivity for cong, and have congruence lemmas for +, etc., then you can rewrite with congruences as if they were equations."
```

#### [Edward Ayers (Oct 10 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135533645):
What is on the lhs and rhs for the simp lemma made from this:
```lean
@[simp] theorem ne_zero (u : units α) : (u : α) ≠ 0 
:= ...
```

#### [Edward Ayers (Oct 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135535720):
Ok now that I've printed out the congruence rules and simp rules for the default set of simp_lemmas I am just confused.

#### [Edward Ayers (Oct 10 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135536015):
Ah ok, congruence lemmas let you move between different relations:
```lean
[if_simp_congr] #11 (?x_1 ↔ ?x_2) (?x_4 = ?x_6) (?x_5 = ?x_7), ite ?x_1 ?x_4 ?x_5 = ite ?x_2 ?x_6 ?x_7
```
Whereas simps  don't. I am now curious about whether simp lemmas can be defined for other relations. They have to be transitive and reflexive, but I don't know if it has to be congruent `x = y -> f x = f y`. Would it be possible to define simp lemmas for  the relation`<`? What about integer conguence mod n?

#### [Gabriel Ebner (Oct 10 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135536879):
Simp lemmas and congruence lemmas are very different.  1) They have different variable constraints: for simp lemmas, all variables of the rhs must occur on the lhs.  E.g. `g x y = f x` is a simp lemma, but `f x = g x y` is not.  Congruence lemmas on the hand impose a requirement on the hypotheses: e.g. `x = y -> f x = f y` is a congruence lemma, but `x = h x -> f x = f x` is not (because the rhs of `x = h x` is just wrong).

#### [Gabriel Ebner (Oct 10 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135536979):
2) Their purpose is different.  You use congruence lemmas to specify where to rewrite, and simp lemmas tell you the result of the rewriting.

#### [Gabriel Ebner (Oct 10 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537089):
Ideally you could use simp to rewrite modulo integer congruence.  As far as I remember there was a technical problem preventing this though.  But there's no fundamental reason why this can't work.

#### [Gabriel Ebner (Oct 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537137):
I think the most interesting example of a simp relation other than `eq` is `equiv` at the moment.  Look at `data/equiv.lean`.

#### [Edward Ayers (Oct 10 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537396):
Thanks! As far as I can tell, `x = y -> f x = f y` is not explicitly in simp_lemmas. simp is assuming the relation is congruent. Is this right?

#### [Gabriel Ebner (Oct 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537459):
That's a congruence lemma.  And yes, it is generated on-demand using the same tool that powers the `congr` tactic.

#### [Edward Ayers (Oct 10 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135537491):
So you couldn't do simp with the `<` relation?

#### [Gabriel Ebner (Oct 10 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_lemmas/near/135542107):
No, because 1) `<` is not reflexive and 2) `has_lt.lt` is not transitive in general.  I think you can turn `nat.le` into a simplification relation though.

