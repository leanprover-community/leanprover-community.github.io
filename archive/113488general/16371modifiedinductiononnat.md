---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16371modifiedinductiononnat.html
---

## Stream: [general](index.html)
### Topic: ["modified" induction on nat](16371modifiedinductiononnat.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147917777):
I am doing the homework I set my students. I seem to often want "induction on n >= 1" and in this question I even want "induction starting at n = 2". I have a family of propositions `P n` for `n : nat`, which are true for n >= 2 (and this can be proved by induction on n>=2), and I also have the hypothesis `Hn2 : n >= 2`. Currently (in tactic mode) I write

```lean
  -- hypotheses    n : ℕ
  --             Hn2 : n ≥ 2
  -- now replace n with m + 2 and then do induction on m >= 0
  cases n with n, cases Hn2, -- Hn2 : 0 ≥ 2 and cases kills it.
  cases n with m, revert Hn2, exact dec_trivial, -- here Hn2 : 1 ≥ 2 and cases doesn't kill it
  clear Hn2, -- and we're finally ready to go
  -- it would be nice to have 
  induction m with d Hd,
```
and off I go. But even then it's pretty meh because n is replaced by `nat.succ (nat.succ m)`. 

I don't think it would be too hard to knock up some kind of "modified principle of induction" which takes as input a hypothesis n>=2 and spits out two goals, one the case n = 2 and the other the goal `P (n + 1)` assuming both `P n` and `n >= 2` still. 

I might try to get a minion to do this. How would this work exactly?  I've just looked at the source code for meta induction and it looks intimidating, but I guess that's because it works on a general inductive type. Is this a feasible project for a student? What should it be called? What should the syntax be? `modified_induction n Hn2 with d Hd`?  It's just something that seems to come up a lot in my class, that's why I'm interested.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 18 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918117):
No need for a custom tactic, you can define that as a lemma, and maybe invoke it with `inducting ... using`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918290):
Hmm. What is this `using` of which you speak? Is that some keyword I don't know?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918299):
it comes out blue in VS code so I guess it means something...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 18 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918336):
It's one of the keywords that can be used by interactive tactics I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918435):
```lean
theorem Q0502' (n : ℕ) : n ≥ 2 → 4 ^ n > 3 ^ n + 2 ^ n :=
begin
  induction n with d Hd,
    exact dec_trivial,
  -- now pick up the pieces for modified induction
  intro Hs, cases Hs,
    exact dec_trivial, -- base case n = 2,
  replace Hd := Hd Hs_a, clear Hs_a,
  /-
  d : ℕ,
  Hd : 4 ^ d > 3 ^ d + 2 ^ d
  ⊢ 4 ^ nat.succ d > 3 ^ nat.succ d + 2 ^ nat.succ d
  -/
  -- exact calc blah
  sorry
end
```
This isn't so bad, although using induction twice does look weird. I think I still want it to be better though. I need to learn about `using` apparently...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918438):
Check out the docstring for `induction` (it's quite long)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918796):
this is not the easiest way to prove it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918968):
```lean
example (P : nat → Prop) (h0 : P 37) (h1 : ∀ n ≥ 37, P n → P (n + 1)) : ∀ n ≥ 37, P n :=
begin
  introv h,
  induction n with n IH, {cases h},
  cases lt_or_eq_of_le (nat.le_of_succ_le_succ h) with lt eq,
  { exact h1 _ lt (IH lt) },
  { subst eq, exact h0 }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918969):
this is what I usually do when I have an induction with a weird base case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919062):
But it makes it harder to see what's going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919065):
It's still better than both my ways though :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919070):
but that doesn't mean that I'm happy with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919113):
this is a bit more flexible with weird induction steps:
```lean
example (P : nat → Prop) {m} (h0 : P m) (h1 : ∀ n ≥ m, P n → P (n + 1)) : ∀ n ≥ m, P n :=
begin
  intro n,
  apply nat.strong_induction_on n, intros n IH h,
  cases lt_or_eq_of_le h with lt eq,
  { cases n with n, {cases lt},
    have := nat.le_of_lt_succ lt,
    exact h1 _ this (IH _ (nat.lt_succ_self _) this) },
  { subst n, exact h0 }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919124):
That's the optimal set-up I guess. So now I can do "induction n using ^^^" somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919125):
eh, it's not that great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919164):
`induction using` has little to offer over `refine` and it is much pickier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919174):
I just want to make it a one-liner for my students to go from goal `P n` and hypothesis `Hn : n >= 2` to goals `P 2` and `P (d + 1)`, the latter with hypotheses `P d` and `d >= 2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919216):
sure, just use this lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919218):
indeed!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919454):
Yes, this is better than anything I had. I've added modified induction to `xenalib` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919455):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 18 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147925201):
```quote
`induction using` has little to offer over `refine` and it is much pickier
```
 It may require Lean 4 but I hope we'll have something as powerfull as SSReflect `elim` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 01 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150688665):
```quote
this is a bit more flexible with weird induction steps:
```lean
example (P : nat → Prop) {m} (h0 : P m) (h1 : ∀ n ≥ m, P n → P (n + 1)) : ∀ n ≥ m, P n :=
begin
  intro n,
  apply nat.strong_induction_on n, intros n IH h,
  cases lt_or_eq_of_le h with lt eq,
  { cases n with n, {cases lt},
    have := nat.le_of_lt_succ lt,
    exact h1 _ this (IH _ (nat.lt_succ_self _) this) },
  { subst n, exact h0 }
end
```
```
 Has this been incorporated in mathlib? It turns out that I just need this lemma right now :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 01 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150689029):
In the middle of a proof, I need to define by induction a function from ℕ to some type α. I know how to do this with a top-level definition, but I could not figure out the syntax inside a proof. Is this possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 01 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150689418):
I don't think you can do it using the equation compiler

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 01 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150689522):
Yes, I have probably to use `nat.rec_on`, but this looks really arcane.


{% endraw %}
