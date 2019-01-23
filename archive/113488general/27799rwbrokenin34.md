---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27799rwbrokenin34.html
---

## Stream: [general](index.html)
### Topic: [rw broken in 3.4](27799rwbrokenin34.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 20 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125331297):
@**Sebastian Ullrich** Help! I'm looking at upgrading to 3.4.0, but one of the recent commits introduced a bug that breaks a lot of mathlib stuff. I'm a bit worried I will have to abandon 3.4 and stick to nightlies unless it is fixed.
```
def f : ℕ → ℕ := λ _, 0

theorem A (x : ℕ) : f x = 0 := rfl
theorem B (x : ℕ) : (f : _) x = 0 := rfl
theorem C (x : ℕ) : (f : ℕ → ℕ) x = 0 := rfl

example (x) : f x = 0 := by simp [A] --ok
example (x) : f x = 0 := by have := A x; rw this --ok
example (x) : f x = 0 := by simp [B] --fails
example (x) : f x = 0 := by have := B x; rw this --fails
example (x) : f x = 0 := by simp [C] --fails
example (x) : f x = 0 := by have := C x; rw this --fails
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 20 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125331546):
Oh, it's not a bug, it's `typed_expr`. What is the purpose of this thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 20 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125331596):
and how do I get my type ascriptions back?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125432803):
@**Mario Carneiro** `typed_expr` [*is* the new type ascription](https://github.com/leanprover/lean/commit/bcaa0b2/). I'm investigating what's happening here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 20 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125434269):
I am very relieved to see this answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 20 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125434333):
because there was always the fear that something had to be changed to make the monad stuff work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 20 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125434488):
and that it couldn't be changed back and Mario's observation was supposed to be the new normal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125437568):
I found the issue, it's certainly not intended behavior. I'll talk to Leo about it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125471033):
@**Sebastian Ullrich**  I have some additional information about what is happening, although you may already know:
* When you type `(e : t)`, the resulting pexpr contains a constant `typed_expr t e`, to record the existence of the type ascription. (I am not sure what it used to be, probably a macro of some kind.)
* It used to be the case that the corresponding expr was just `e`, i.e. type ascriptions leave no trace in the resulting term. This property is super important for me. Now, the resulting expr is `typed_expr t e`, which breaks many simp lemmas which used type ascriptions to silently correct some intermediate types, since simp doesn't unfold reducibles in simp lemma LHS for matching. (And it probably shouldn't, otherwise this would make it hard to actually get rid of a reducible via a simp lemma.)
* I have a workaround tactic `clean` which is like `by exact` but removes all identity functions from the given pexpr after elaboration. I am using this on all simp lemmas that use type ascription. But this is probably not the best solution, and I hope you have luck fixing this. What about just stripping `typed_expr` during pexpr -> expr translation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 21 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125486104):
@**Mario Carneiro** I tried to @ you in the RSS feed, did that not work? https://leanprover.zulipchat.com/#narrow/stream/116290-rss/subject/Recent.20Commits.20to.20lean.3Amaster/near/125451078

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125487371):
Will there be a Lean 3.4.1 then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125487416):
Yes. I'll wait a while to make sure you're not digging up any other obscure issues :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125487420):
Sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125487421):
There's one more, I need to minimize

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125487422):
It seems Lean could use a rather large test project to test such things...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125487427):
Like... a math library say

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 25 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125653376):
@**Sebastian Ullrich** Here's problem number 2 from the mathlib update, reasonably minimized:
```
universe u
variables {α : Type u}

def X (α : Type u) : Type u := sorry
instance {α} : has_mem α (X α) := sorry
def ID [decidable_eq α] (s : X α) : X α := sorry
theorem mem_ID [decidable_eq α] (a : α) (s : X α) : a ∈ ID s ↔ a ∈ s := sorry

def T (m : X α) : Type u := sorry
instance decidable_eq_T {m : X α} : decidable_eq (T m) := sorry

def F (m : X α) : X (T m) := sorry
example {s : X α} {f : T s} : f ∈ ID (F (id s)) ↔ f ∈ F (id s) :=
by rw [mem_ID]; admit
```
It derives from `finset.mem_pi`, which no longer typechecks in the latest nightly. If anyone is running the 04-06 nightly, could you check that this code typechecks?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 25 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125653432):
Yes, typechecks in nightly-2018-04-06.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 25 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125653489):
It was not a huge problem as far as updating mathlib, it only affected two proofs in mathlib relating to `finset.pi` which I just rewrote to be shorter anyway :) but it's still a mystery why this broke since there is nothing obviously related to this in the intervening commits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 25 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125653560):
Here is the pp all error output:
```
rewrite tactic failed, did not find instance of the pattern in the target expression
  @has_mem.mem.{?l_1 ?l_1} ?m_2 (X.{?l_1} ?m_2) (@X.has_mem.{?l_1} ?m_2) ?m_3
    (@ID.{?l_1} ?m_2 (λ (a b : ?m_2), ?m_4 a b) ?m_5)
state:
α : Type u,
s : X.{u} α,
f : @T.{u} α s,
m : X.{u} (@T.{u} α s)
⊢ iff
    (@has_mem.mem.{u u} (@T.{u} α s) (X.{u} (@T.{u} α (@id.{u+1} (X.{u} α) s)))
       (@X.has_mem.{u} (@T.{u} α (@id.{u+1} (X.{u} α) s)))
       f
       (@ID.{u} (@T.{u} α (@id.{u+1} (X.{u} α) s))
          (λ (a b : @T.{u} α (@id.{u+1} (X.{u} α) s)), @decidable_eq_T.{u} α (@id.{u+1} (X.{u} α) s) a b)
          (@F.{u} α (@id.{u+1} (X.{u} α) s))))
    (@has_mem.mem.{u u} (@T.{u} α s) (X.{u} (@T.{u} α (@id.{u+1} (X.{u} α) s)))
       (@X.has_mem.{u} (@T.{u} α (@id.{u+1} (X.{u} α) s)))
       f
       (@F.{u} α (@id.{u+1} (X.{u} α) s)))
```
The `decidable_eq` argument seems important, and the `id s` can be any composite term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 25 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125653656):
oh, I just noticed that `f` has the wrong type; if it has type `T (id s)` instead of `T s` it works. Maybe I minimized too much...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 25 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20broken%20in%203.4/near/125653815):
No, that's exactly the issue. The pattern involves two occurrences of `?m_2` in types, which are defeq but not syntactically equal in the target


{% endraw %}
