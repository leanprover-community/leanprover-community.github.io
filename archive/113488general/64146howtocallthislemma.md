---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64146howtocallthislemma.html
---

## Stream: [general](index.html)
### Topic: [how to call this lemma](64146howtocallthislemma.html)

---


{% raw %}
#### [ Johan Commelin (Aug 07 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131039906):
```lean
lemma quux {A : Type*} [add_comm_group A] {n : ℕ} (f : fin (n+1) → A) : sum univ f = f n + sum univ (λ i : fin n, f i.raise) :=
begin
  sorry
end
```

#### [ Johan Commelin (Aug 07 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040023):
Ooh, and if you don't know a name, but you know a *proof*... that's fine too.

#### [ Kevin Buzzard (Aug 07 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040821):
Johan, I think Kenny might have generated a proof of this once, when I was trying to figure out induction.

#### [ Kevin Buzzard (Aug 07 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040877):
https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/

#### [ Kevin Buzzard (Aug 07 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040889):
check out def4 in https://github.com/kckennylau/Lean/blob/master/proofs_by_induction.lean

#### [ Kevin Buzzard (Aug 07 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131040899):
Apparently it uses a lemma called `chris`. I'm not sure if this is the official mathlib-sanctioned name.

#### [ Johan Commelin (Aug 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131041195):
Ok, thanks. I'll take a look in a minute!

#### [ Chris Hughes (Aug 07 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042444):
I proved a slightly weaker version
```lean
lemma quux {A : Type*} [add_comm_group A] {n : ℕ} (f : fin (n+1) → A) :
  sum univ f = f ⟨n, nat.lt_succ_self _⟩  + sum univ (λ i : fin n, f i.raise) :=
by rw [← insert_erase (mem_univ (⟨n, nat.lt_succ_self _⟩ : fin (n + 1))), 
    sum_insert (not_mem_erase _ _), add_left_inj]; exact
sum_bij (λ a ha, ⟨a, lt_of_le_of_ne (nat.le_of_lt_succ a.2) 
  (fin.vne_of_ne (mem_erase.1 ha).1)⟩ ) (λ _ _, mem_univ _) 
  (λ ⟨_, _⟩ _, rfl) (λ ⟨a, _⟩ ⟨b, _⟩ _ _ h, fin.eq_of_veq (fin.veq_of_eq h : _)) 
  (λ b hb, ⟨⟨b.1, nat.lt_succ_of_lt b.2⟩, mem_erase.2 ⟨fin.ne_of_vne (ne_of_lt b.2), mem_univ _⟩, 
    by cases b; refl⟩)
```

#### [ Johan Commelin (Aug 07 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042466):
Why is it weaker?

#### [ Johan Commelin (Aug 07 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042478):
Also, apparently I ought to be using `finset.range`...

#### [ Chris Hughes (Aug 07 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042484):
I used `⟨n, nat.lt_succ_self _⟩` instead of `\u n`

#### [ Johan Commelin (Aug 07 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042536):
Aaah, but that is better.

#### [ Johan Commelin (Aug 07 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042543):
Silly me didn't understand that `\u n` is difficult.

#### [ Johan Commelin (Aug 07 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042561):
I think you can use `nat.le_refl _` for some golfing.

#### [ Johan Commelin (Aug 07 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131042583):
But I will first think about the `finset.range` version. Maybe it becomes a whole lot easier.

#### [ Johan Commelin (Aug 07 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046567):
```lean
lemma quux {A : Type*} [add_comm_group A] (n : ℕ) (f : ℕ → A)
: (finset.range (n+1)).sum f = f n + (finset.range n).sum f := by simp

```

#### [ Johan Commelin (Aug 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046594):
So, that might not be even worth stating as a lemma.

#### [ Kenny Lau (Aug 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046619):
what's the use of this lemma if you could just `simp`?

#### [ Johan Commelin (Aug 07 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20call%20this%20lemma/near/131046678):
That's exactly my point.


{% endraw %}
