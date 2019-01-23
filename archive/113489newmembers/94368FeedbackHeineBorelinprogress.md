---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/94368FeedbackHeineBorelinprogress.html
---

## Stream: [new members](index.html)
### Topic: [Feedback (Heine Borel in progress)](94368FeedbackHeineBorelinprogress.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Guillermo Barajas Ayuso (Sep 16 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134030478):
Hi, I have uploaded some code in the link  https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Heine-Borel%20(incomplete) , I'll leave it here in case you want to give me some feedback. Thank you for your time! :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134045098):
```lean
theorem for_all_not_all {α : Type u} (P Q R: α → Prop):
(∀ x (H : R x), ¬ (P x ∧ Q x)) ↔  ∀ x (H : R x), P x → ¬ Q x := 
⟨λ Hnand x Hx, not_and.mp $ Hnand x Hx, λ Hton x Hx, not_and.mpr $ Hton x Hx⟩
```

Mathlib would prefer that kind of style to your tactic proof. I always suspect that such results are either in mathlib already or easily deducible. Looking at the proof I feel like it's one of those ones which could be shortened with some magic use of function.comp like in https://xenaproject.wordpress.com/2018/05/19/function-composition/ . 

Oh wait -- 

```lean
theorem for_all_not_all {α : Type u} (P Q R: α → Prop):
(∀ x (H : R x), ¬ (P x ∧ Q x)) ↔  ∀ x (H : R x), P x → ¬ Q x := by simp [not_and]
```
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134045185):
The simp proof -- the proof takes 50% longer to process but the parser takes far less time parsing :-) End result is that both versions run in about the same time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134045233):
I have an error at line 431 by the way, and there are 6 sorrys. Do you need help filling them in?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134046514):
Re the argument on line 431: there is already `nat.lt_pow_self`. 

```lean
theorem le_pow (n : ℕ) : (n : ℝ) ≤ (2 : ℝ) ^ n :=
begin
  show (n : ℝ) ≤ ((2 : ℕ) : ℝ) ^ n,
  rw ←nat.cast_pow,
  rw nat.cast_le,
  exact le_of_lt (nat.lt_pow_self (dec_trivial) n),
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134046673):
`notation ⟦a,b] := closed_interval a b `

This is a hilarious idea. Does it work? Re-using notation which is already used is a dangerous game, but given that as far as I know in Lean every use of `]` in notation comes with an `[` too, so avoiding the `[` in this case gives you better leeway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048119):
`theorem le_ε_to_le (Hle_ε : ∀ ε > 0, a ≤ b + ε) : a ≤ b := sorry` These things are really annoying if they're not there already. @**Kenny Lau** how is one supposed to prove stuff like this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048714):
```lean
theorem le_ε_to_le (Hle_ε : ∀ ε > 0, a ≤ b + ε) : a ≤ b :=
le_of_not_gt $ λ H, begin
  have H2 := Hle_ε ((a - b) / 2) _,
    revert H2, -- because it makes the rewriting easier
    rw [←(mul_le_mul_right (show (2 : ℝ) > 0, by norm_num)),add_mul,
    div_mul_cancel _ (show (2 : ℝ) ≠ 0, by norm_num),
   (show b * 2 + (a - b) = a + b, by ring),
    mul_two,add_le_add_iff_left],
    exact not_le_of_gt H,
  apply div_pos _ (show (0 : ℝ) < 2, by norm_num),
  exact sub_pos_of_lt H
end
```
This time last year there was no `norm_num` and no `ring` -- imagine how hard it was doing M1F example sheets!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048768):
```lean
theorem le_ε_to_le {α : Type*} [linear_ordered_field α] {a b : α}
  (Hle_ε : ∀ ε > 0, a ≤ b + ε) : a ≤ b :=
le_of_not_lt $ λ H, not_lt_of_le (Hle_ε ((a-b)/2) (half_pos $ sub_pos_of_lt H)) $
calc  b+(a-b)/2
    < b+(a-b) : add_lt_add_left (half_lt_self (sub_pos_of_lt H)) _
... = a : add_sub_cancel'_right b a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048808):
```lean
theorem between_shorter (H1 : b ≤ c) (H2 : c ≤ a) (H3 : b ≤ d) (H4 : d ≤ a) : 
abs (c - d) ≤ abs (a - b) :=
begin
  rw abs_of_nonneg (sub_nonneg_of_le $ le_trans H1 H2),
  rw abs_le, split,
    rw neg_sub,
    exact _root_.sub_le_sub H1 H4,
    exact _root_.sub_le_sub H2 H3,
end
```

This one wasn't too bad -- proof felt natural.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049053):
```lean
theorem between_shorter {α : Type*} [decidable_linear_ordered_comm_group α] {a b c d : α}
  (H1 : b ≤ c) (H2 : c ≤ a) (H3 : b ≤ d) (H4 : d ≤ a) :
  abs (c - d) ≤ abs (a - b) :=
calc  abs (c - d)
    ≤ a - b : abs_sub_le_iff.2 ⟨sub_le_sub H2 H3, sub_le_sub H4 H1⟩
... = abs (a - b) : (abs_of_nonneg $ sub_nonneg_of_le $ le_trans H1 H2).symm
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049054):
```lean
lemma half_le_self (H : 0 ≤ a) : a / 2 ≤ a := begin
  rw div_le_iff (show (2 : ℝ) > 0, by norm_num),
  rw mul_two,
  rwa le_add_iff_nonneg_left,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049259):
```lean
lemma half_le_self {α : Type*} [linear_ordered_field α] {a : α}
  (H : 0 ≤ a) : a / 2 ≤ a :=
div_le_of_le_mul two_pos $ (two_mul a).symm ▸ le_add_of_nonneg_left H
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049371):
Should there be training or exercises or something for people who need stuff like this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 16 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134050573):
```lean
import tactic.linarith

lemma half_le_self {α : Type*} [linear_ordered_field α] {a : α}
  (H : 0 ≤ a) : a / 2 ≤ a :=
by linarith

theorem between_shorter {α : Type*} [decidable_linear_ordered_comm_ring α] {a b c d : α}
  (H1 : b ≤ c) (H2 : c ≤ a) (H3 : b ≤ d) (H4 : d ≤ a) :
  abs (c - d) ≤ abs (a - b) :=
by unfold abs max; split_ifs; linarith
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134050865):
...or maybe even a tactic!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134050868):
Next we make a wrapper for linarith that unfolds stuff that is secretly arithmetic. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051134):
```quote
```lean
    < b+(a-b) : [blah]
... = a : add_sub_cancel'_right b a
```
```
Kenny -- you misspelt "by ring". 

Why should mathematican end users have to know that the triviality `b + (a - b) = a` is called `add_sub_cancel'_right`? Surely we should just be able to write something which generates this proof for us, and then internally replaces what we wrote with this add_sub_cancel' nonsense?  I'm assuming that using `ring` to do this is not recommended because it might take about 10 times as long. It's all well and good people writing clever tactics which solve all goals of this nature, but then we end up in this situation where people are encouraged not to use them and instead get an encyclopedic knowledge of all this `add_sub_cancel'_right` nonsense, or learn how to look it up. I guess what I'm asking for is a tactic which does `by ring` but only takes a long time the first time -- like Scott's `tidy` trick. Can this be done in other cases somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051186):
@**Guillermo Barajas Ayuso** -- `linarith` is a brand new tactic which Rob wrote. You might find it useful in other situations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051860):
@**Rob Lewis** re `between_shorter`, my version works for objects without multiplication

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 16 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051971):
```quote
Can this be done in other cases somehow?
```
It can in principle. But things like `ring` often don't try to produce short or pretty output, because it's way harder to write something that does that and works generally. And the output will probably still look messy on anything more complicated than that basic example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 16 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052060):
I wouldn't expect `ring` to be unreasonably slow for examples like that, either.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 16 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052895):
Hi @**Rob Lewis**, in the interest in making `linarith` even easier to use, what would you think of having it automatically try `exfalso` if the goal doesn't look like linear arithmetic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 16 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052931):
It's of course possible to achieve this by: `linarith <|> (exfalso >> linarith)`, but I worry that this is inefficient.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 16 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052956):
(Actually maybe it isn't --- if the goal is something else, linarith I guess fails before doing any work already...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 16 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134053111):
That's completely reasonable. I actually thought it did that already, but apparently I added a check for a `false` goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 16 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134053146):
If there are no inequality hypotheses, it'll fail immediately. If there are hypotheses it can work with, it will try, but failure is a lot quicker than success.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 16 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134053210):
I'll add a config option for trying to prove arbitrary goals by `exfalso`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 16 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134054291):
This sort of follows-up what Kevin was saying before: it seems to me that it'd be really great if Lean had a facility for tactics to opt-in to cache what they did on invocation, not just in the interactive lean session (memoizing there), but statically in a file in the repository.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 16 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134054292):
The (my?) dream is that mathlib (or just mathematics) could be filled with tactic proofs which call shiny-new maybe-expensive tactics which do all of your dirty-work for you in one line (e.g `by super_ring`), without any detrimental performance impact; if you change the first line of a file, the expensive tactic proofs in the file below instantly recompile; and if you change the statement of a lemma the cached proof will just silently fail to typecheck and the tactic proof will be re-run. mathlib can be distributed with these cache-files, or they could just be built the first time mathlib is built, and everyone is happy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 16 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134054295):
Instead it seems like in many places people have to steer clear of the "big guns", or at least only use them to get a term/tactic-mode proof which they will replace them with. To me, this seems just like a manual way of doing the same sort of static caching, but the tools which helped generate your easy proof (e.g. `ring` → `add_sub_cancel'_right`) are lost forever (and don't auto-fix your proof when you e.g. tinker with your lemma).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134058680):
```quote
```quote
```lean
    < b+(a-b) : [blah]
... = a : add_sub_cancel'_right b a
```
```
Kenny -- you misspelt "by ring". 
```
Or "by abel"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134104742):
Or even `by simp`. Grr. What is the point of this `abel` tactic? I still haven't found an example which `simp` can't do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134106299):
Hopefully `abel` is a step towards the `module` tactic which should be more useful

