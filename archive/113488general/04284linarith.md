---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04284linarith.html
---

## Stream: [general](index.html)
### Topic: [linarith](04284linarith.html)

---


{% raw %}
#### [ Johan Commelin (Nov 21 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148096612):
Shouldn't `linarith` be able to take care of this?
```lean
n : ℕ,
i : fin (n + 1 + 1),
a b : fin (n + 1),
ha : ¬a.val < i.val,
h : b.val < i.val,
H : a.val ≤ b.val,
a_1 : nat.succ (a.val) > b.val
⊢ false
```

#### [ Kenny Lau (Nov 21 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148096896):
I thought it has been made clear that `linarith` doesn't deal with `nat`

#### [ Patrick Massot (Nov 21 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097084):
After `apply ha` it should be an easy target for `mono` but it doesn't work :sad:

#### [ Patrick Massot (Nov 21 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097138):
@**Simon Hudon** 
```
import tactic.monotonicity

example (n : ℕ)
(i : fin (n + 1 + 1))
(a b : fin (n + 1))
(ha : ¬a.val < i.val)
(h : b.val < i.val)
(H : a.val ≤ b.val) 
(a_1 : nat.succ (a.val) > b.val) : false :=
begin
  apply ha,
  mono*,  -- does nothing :-(
  exact calc a.val ≤ _ : H
  ... < _ : h,
end
```

#### [ Rob Lewis (Nov 21 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097160):
Change `nat.succ (a.val)` to `a.val + 1`.

#### [ Patrick Massot (Nov 21 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097178):
This is the first thing I tried, but it changes nothing

#### [ Kenny Lau (Nov 21 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097262):
maybe stop (over)relying on tactics

#### [ Rob Lewis (Nov 21 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097310):
Oh, change `ha` to `a.val ≥ i.val`.

#### [ Patrick Massot (Nov 21 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097329):
that works

#### [ Patrick Massot (Nov 21 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097395):
Kenny, the discussion is not really about how to prove that particular goal. It's about having a toolset which gets rid of hundred of stupid goals like this, that would otherwise break our proof flow and concentration

#### [ Rob Lewis (Nov 21 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097485):
There's something wrong with the routine that makes `linarith` work for `nat` and the part that deals with negated hypotheses, I'll look into it when I have a minute.

#### [ Patrick Massot (Nov 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097660):
Nice! In the mean time, Johan can use `replace ha := le_of_not_lt ha ; linarith` to close that goal

#### [ Rob Lewis (Nov 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097675):
Or `apply ha; linarith`.

#### [ Patrick Massot (Nov 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097682):
indeed

#### [ Sebastien Gouezel (Nov 21 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148099129):
Another `linarith`wishlist entry: if there is an assumption `abs x ≤ c`, convert it to `x ≤ c` and `-x ≤ c`.

#### [ Rob Lewis (Nov 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148101337):
There are various unfolding/preprocessing things like that, that `linarith` could do. Writing a separate tactic that unfolds `abs` would be very easy, and you could even add `meta def linarith' := unfold_abs; linarith` if you wanted. But I'm not sure that bundling all these things into the main tactic is a good idea.

#### [ Rob Lewis (Nov 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148101362):
There's now a PR open to fix Johan's problem, btw.

#### [ Sebastien Gouezel (Nov 21 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148101659):
OK, I understand. I can definitely unfold it by hand when needed. I am just motivated by the principle of maximal laziness.

#### [ Johan Commelin (Nov 21 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104169):
@**Rob Lewis** Cool! Thanks a lot.

#### [ Johan Commelin (Nov 21 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104182):
Now there is still the problem with `nat.succ _` vs `_ + 1`. Could that be fixed as well?

#### [ Johan Commelin (Nov 21 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104248):
Because then I could run `split_ifs with foo bar; {ext, simp, linarith}` and be done with it. Otherwise I need to explicitly `change` my goal for each goal. Or should I write a custom simp-lemma for this, that I use locally?

#### [ Johan Commelin (Nov 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104284):
```lean
lemma δ_monotone (i : [n+1]) : monotone (δ i) :=
begin
  intros a b H,
  change a.val ≤ b.val at H,
  dsimp [fin.succ_above],
  split_ifs with ha hb;
  try { ext1, simp, linarith },
  { ext1, simp, change _ ≤ _ + 1, linarith },
  { ext1, simp, change _ + 1 ≤ _ + 1, linarith }
end
```

#### [ Rob Lewis (Nov 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104414):
@**Sebastien Gouezel** If you don't want to do it by hand, you can finish this and use it (or modify it to fit your purposes). Just use `unfold_abs; linarith` in place of `linarith`, or define an alias for that.
```lean
open tactic
lemma le_and_le_of_abs_le {α} [decidable_linear_ordered_comm_group α] {a b : α} (h : abs a ≤ b) : a ≤ b ∧ -a ≤ b :=
sorry

meta def unfold_abs : tactic unit :=
local_context >>= list.mmap' (λ e, try (mk_app `le_and_le_of_abs_le [e] >>= cases))

example (a b c : ℤ) (h : abs a ≤ b) (h2 : abs b ≤ c) : true :=
begin 
  unfold_abs
end 
```

#### [ Rob Lewis (Nov 21 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104502):
@**Johan Commelin** This falls into the same basket as Sebastien's request. There are lots of constants that can be unfolded or rewritten into a form that `linarith` will handle. I don't want to build them all in. You can just add `nat.succ_eq_add_one` to the `simp` call.

#### [ Johan Commelin (Nov 21 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104578):
Ok, thanks, will do.

#### [ Johan Commelin (Nov 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104774):
```quote
maybe stop (over)relying on tactics
```
 @**Kenny Lau** Can you golf this?
```lean
lemma δ_monotone (i : [n+1]) : monotone (δ i) :=
λ a b (H : a.val ≤ b.val),
by dsimp [fin.succ_above]; split_ifs with ha hb; { ext1, simp [nat.succ_eq_add_one], linarith }
```
You can find it here: https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L33-L35

#### [ Johan Commelin (Nov 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105362):
@**Rob Lewis** So presumably goals of this form are also outside the scope of `linarith`?
```lean
n : ℕ,
i j : fin (n + 1 + 1),
H : i ≤ j,
a : fin (n + 1),
h : a.val < i.val,
h_1 : (fin.cast_succ a).val < (fin.succ j).val,
h_2 : ¬a.val < j.val,
h_3 : ¬(fin.succ a).val < i.val
⊢ a.val = 1 + (1 + a.val)
```
I have 7 goals that are all of this form or another... I would like to kill them all in one go.

#### [ Johan Commelin (Nov 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105382):
Sorry, I should paste context...

#### [ Kevin Buzzard (Nov 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105384):
So these are nats?

#### [ Kevin Buzzard (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105470):
What is the argument in maths?

#### [ Rob Lewis (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105480):
Um, `linarith` doesn't know anything about the relation between `fin` and `fin.val`, or anything about `fin.succ` or `fin.cast_succ`.

#### [ Kevin Buzzard (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105484):
I am not sure you can ask `linarith` to start unfolding `fin.succ` or stuff like that

#### [ Kevin Buzzard (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105487):
There will be a never-ending list of things you want it to unfold.

#### [ Rob Lewis (Nov 21 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105530):
Basically, those are a bunch of random inequalities between distinct variables, not even all of the same type.

#### [ Rob Lewis (Nov 21 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105541):
The only thing `linarith` will learn is that `j.val < i.val`.

#### [ Kevin Buzzard (Nov 21 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105559):
What about `x ∈ {a : ℕ | a > 5}` ? That unfolds to an inequality, but it's surely not `linarith`'s job to figure that out.

#### [ Kenny Lau (Nov 21 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105571):
@**Johan Commelin** there must be such a function in mathlib

#### [ Kenny Lau (Nov 21 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105575):
(or not)

#### [ Kenny Lau (Nov 21 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105617):
(yes it’s decidable)

#### [ Rob Lewis (Nov 21 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105647):
@**Kevin Buzzard** right, see my last few comments. :slight_smile: Infinitely many things can unfold to linear inequalities. If `linarith` tries everything possible it will be unpredictable and slow.

#### [ Johan Commelin (Nov 21 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105717):
Cool, I'm getting the hang of this! @**Rob Lewis** Thanks for your help. I'm starting to understand how to play with `linarith`.
After:
```lean
lemma simplicial_identity₁ {i j : [n+1]} (H : i ≤ j) : δ j.succ ∘ δ i = δ i.cast_succ ∘ δ j :=
begin
  change i.val ≤ j.val at H,
  funext a,
  dsimp [fin.succ_above],
  split_ifs; { try {ext1}, try {simp [nat.succ_eq_add_one] at *}, try {linarith} },
end
```
Before:
```lean
lemma simplicial_identity₁ {i j : [n+1]} (H : i ≤ j) : δ j.succ ∘ δ i = δ i.cast_succ ∘ δ j :=
begin
  funext a,
  dsimp [fin.succ_above],
  by_cases hja : (j.val < a.val),
  { have hja' : ((fin.succ j).val < (fin.succ a).val) :=
    begin
      simp,
      exact nat.succ_le_succ hja,
    end,
    have hia : ((i.cast_succ).val < (fin.succ a).val) :=
    begin
      simp,
      refine (lt_of_le_of_lt H _),
      exact (nat.le_trans hja (nat.le_succ a.val))
    end,
    rw [if_pos hja, if_pos (nat.le_trans H hja), if_pos hja', if_pos hia]},
  { rw [dif_neg hja],
    by_cases hia : (i.val ≤ a.val),
    { have hia' : ((fin.raise i).val ≤ (fin.raise a).val) := hia,

      have hja' : ¬(j.succ.val ≤ a.succ.val) :=
      begin
        simp at *,
        exact nat.succ_le_succ hja
      end,
      rw [dif_pos hia, dif_pos hia', dif_neg hja'],
      simp [fin.raise],
      apply fin.eq_of_veq,
      simp},
    { have hja' : ¬(j.succ.val ≤ a.raise.val) :=
      begin
        simp at *,
        exact nat.le_trans hja (nat.le_succ j.val)
      end,
      have hia' : ¬((fin.raise i).val ≤ (fin.raise a).val) :=
      begin
        unfold fin.raise, exact hia
      end,
      rw [dif_neg hia, dif_neg hja', dif_neg hia']}}
end
```

#### [ Johan Commelin (Nov 21 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148106009):
@**Kenny Lau** Do you mean it should be provable by `dec_trivial`?

#### [ Simon Hudon (Nov 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148122480):
@**Patrick Massot** @**Rob Lewis** Did the problem turn out to be `mono`?

#### [ Patrick Massot (Nov 21 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148122892):
`linarith` doesn't use `mono` so the bug in `linarith` had nothing to do with `mono` (and is now fixed). But I'm still disappointed I can't get `mono` to help here

#### [ Patrick Massot (Nov 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148123052):
You can try, what I posted right after pinging you is a MWE

#### [ Patrick Massot (Nov 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148123091):
search for "does nothing" in this thread

#### [ Simon Hudon (Nov 21 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148124879):
I wouldn't expect it to do anything in that case. What would you expect it to do?

#### [ Patrick Massot (Nov 21 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148125029):
I would expect it to close the goal

#### [ Simon Hudon (Nov 21 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148128435):
You mean using mixed transitivity? It doesn’t do that. What it does is identify a monotonic function on either side of a relation. < is that relation in your case but it doesn’t have a monotonic function on both sides.

#### [ Simon Hudon (Nov 21 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148128458):
If you want, you can treat < as the monotonic function and -> as the relation.

#### [ Simon Hudon (Nov 21 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148128569):
To do that, you need to do `revert h` before mono.

#### [ Patrick Massot (Nov 21 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131648):
This is sad. We need something like `cc` for inequality, working together with `mono`

#### [ Simon Hudon (Nov 21 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131680):
Maybe something like what I did for tfae would work for that

#### [ Patrick Massot (Nov 21 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131689):
Except `tfae` doesn't work :sad:

#### [ Patrick Massot (Nov 21 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131747):
The following is ridiculous but gives hope:
```lean
example (p q r : ℕ) (h : p ≤ q) (h' : q ≤ r) : p ≤ r :=
begin
  refine le_trans _ _,
  swap,
  tauto,
  tauto
end
```

#### [ Patrick Massot (Nov 21 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131762):
This is the kind goal I hope some "`cc` for inequalities" would solve

#### [ Simon Hudon (Nov 21 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131878):
What is tricky for this kind of tactic is that one would expect it to work in the case of mixed transitivity which makes selecting a relation a bit more difficult. I could do it specifically for `<` and `≤` to simplify things but it's a bit disappointing in terms of generality

#### [ Simon Hudon (Nov 21 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131995):
But in the situations that you're showing, it seems like the kind of stuff `linarith` should handle

#### [ Rob Lewis (Nov 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148135817):
Patrick, can you elaborate on what you mean by "cc for inequalities"?

#### [ Chris Hughes (Nov 21 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148135937):
I think he more or less means solvable using linear order axioms, without any algebra.

#### [ Chris Hughes (Nov 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148135954):
But I think linarith does those.

#### [ Rob Lewis (Nov 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136093):
Ah. Yeah, linarith does those. But I guess it requires some extra algebraic structure on the type that isn't always necessary.

#### [ Chris Hughes (Nov 21 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136290):
And maybe preorder axioms and partial order axioms would be nice as well.

#### [ Rob Lewis (Nov 21 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136993):
Indeed. A tactic for this kind of transitivity reasoning would be a nice project for someone who wants to learn about writing tactics. :wink:

#### [ Rob Lewis (Nov 21 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136997):
Note, I haven't really looked into `mono` yet, so I'm not sure how much overlap there is.

#### [ Simon Hudon (Nov 21 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148137165):
There isn't much overlap actually. To implement this tactic, tfae would be more helpful. It calculates the transitive closure of implication on the local assumptions.

#### [ Simon Hudon (Nov 21 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148137182):
You replace implication by a preorder and you'd get what Patrick is talking about with the additional difficulty of handling `<` properly

#### [ Rob Lewis (Nov 21 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148137301):
Ah, sure. Sounds reasonable enough.

#### [ Patrick Massot (Nov 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148140643):
I'd love to try to understand how to adapt `tfae` here, but again I don't think this would be reasonable before we get a deterministic behavior from `tfae`

#### [ Kenny Lau (Nov 22 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148181673):
@**Johan Commelin** I see someone has figured out the function in mathlib

#### [ Johan Commelin (Nov 22 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148187179):
@**Kenny Lau** Wait, which function in mathlib are you referring to?

#### [ Kenny Lau (Nov 22 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148190141):
@**Johan Commelin** `fin.succ_above`

#### [ Johan Commelin (Nov 22 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148191135):
Aah, yes, I'm using that one. Was that answering a question of mine?

#### [ Johan Commelin (Nov 22 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148191179):
Or maybe you just think it is confusing notation? It probably is...

#### [ Kenny Lau (Nov 22 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148191834):
never mind, ignore me

#### [ Scott Morrison (Nov 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148254707):
More requests: are these reasonable to expect from `linarith`?
```
n m : ℕ,
h₁ : n < m,
⊢ n + 1 ≤ m
```
and
```
n m l : ℕ,
a_left : n ≤ l,
a_right : l < n + (m - n)
⊢ l < m
```
and
```
a_left : n ≤ l,
a_right : l < m
⊢ l < n + (m - n)
```

#### [ Kenny Lau (Nov 24 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148256879):
```quote
The following is ridiculous but gives hope:
```lean
example (p q r : ℕ) (h : p ≤ q) (h' : q ≤ r) : p ≤ r :=
begin
  refine le_trans _ _,
  swap,
  tauto,
  tauto
end
```

This is the kind of goal I hope some "`cc` for inequalities" would solve
```
 
So like this?
```lean
import data.nat.basic

meta def tactic.interactive.cc_inequality : tactic unit :=
`[transitivity; tauto]

example (p q r : ℕ) (h : p ≤ q) (h' : q ≤ r) : p ≤ r :=
by cc_inequality
```

#### [ Johan Commelin (Nov 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148263754):
@**Scott Morrison|110087** Your first question is `exact h1`, so I would hope that `linarith` could do it.  The second and third are nasty because they use nat-subtraction. I think we still need a `num_cast` tactic that would lift it to `int`, and then `linarith` could do the job.

#### [ Andrew Ashworth (Nov 24 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148265222):
Cooper will kill these, if you're willing to use another dependency

#### [ Scott Morrison (Nov 24 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148265691):
Am I allowed to import `cooper` into `data.nat.basic`? :-)

#### [ Scott Morrison (Nov 24 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148265692):
Thanks for the suggestion, I will try out cooper!

#### [ Rob Lewis (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148270921):
`linarith` will not prove any of those. Think of it as a tactic for linear rational inequalities.  If a goal over `int` is still provable when you replace `int` with `rat`, it will still work. Inequalities over `nat` are cast to inequalities over `int`, with extra assumptions that all atoms are nonnegative. Applications of nat subtraction are treated as atoms.

#### [ Rob Lewis (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148270931):
The first one isn't true in a dense order. The second ones involve properties of nat subtraction beyond nonnegativity.

#### [ Rob Lewis (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148270979):
`cooper` isn't in mathlib, it's in Seul's repository. Use it, of course, but incorporating it into mathlib is a bigger discussion.

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148271514):
Would it be possible to edit `linarith` so that it automatically knows that variables coerced from nat are nonnegative? Compare:
```lean
example (a : ℚ) (h:a≥0) : (3:ℚ)/4 ≤ (4:ℚ) + a := by linarith --works
example (a : ℕ) : (3:ℚ)/4 ≤ (4:ℚ) + ↑a := by linarith -- fails
example (a : ℕ) (h:a≥0) : (3:ℚ)/4 ≤ (4:ℚ) + ↑a := by linarith -- even this fails
```

#### [ Rob Lewis (Nov 24 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273249):
`linarith` isn't a smart tactic. It does one thing (linear rational arithmetic) very well, and by coincidence, sometimes it can do things with `nat` and `int`. In your second example, it doesn't know any connection between `a` and `↑a`, and why should it? Instead of a cast, that could be `abs`, or `square`, or any nonnegative function. In the very special case when it sees an inequality over `nat`, it will cast it to `int` and add the nonnegativity hypotheses. But it won't go digging through the input looking for things it can learn are nonnegative. That's a kind of preprocessing that can be done separately.

#### [ Rob Lewis (Nov 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273254):
The third example is a little different. It sees the `a >= 0` hypothesis, and casts it to `int`. But the overall problem is in `rat`.

#### [ Rob Lewis (Nov 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273298):
In general, there's no well-defined type of the "overall problem," since you could have hypotheses over many different types.

#### [ Rob Lewis (Nov 24 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273305):
It could try to guess what type to cast to, or it could cast to every type that appears. This wouldn't be so unreasonable.

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148283001):
Thanks for explaining! As always, there was a lot of complexity lurking here that I didn't appreciate.


{% endraw %}
