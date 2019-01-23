---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50979Dagstuhltasks.html
---

## Stream: [general](index.html)
### Topic: [Dagstuhl tasks](50979Dagstuhltasks.html)

---

#### [Neil Strickland (Oct 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135961777):
Some of you will have seen my post on Mathoverflow (https://mathoverflow.net/q/311159) where I described some tasks that I would like to see formalised for expository purposes, with extensive annotation.  I have carried out two of the tasks, and attempted to write useful annotations,  as shown on these pages:

http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/ (infinitely many primes)
http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/nilpotents/ (the ideal of nilpotents)

These are part of a larger set of pages that are under construction.  I would be interested to hear comments.
My annotations include a number of confessions of confusion or ignorance, and I would be happy for
people to enlighten me.  There are doubtless other misunderstandings as well that I have not flagged.

Note that these formalisations are designed to optimise comprehensibility for users who know a lot
of mathematics but are new to proof assistants; I am not aiming for efficiency, or for consistency 
with standard Lean style in cases where that conflicts with comprehensibility.

#### [Johan Commelin (Oct 17 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135963881):
@**Neil Strickland** Cool display mode! In the past there has been discussion here on Zulip on how  to generate html docs. This looks really nice. I suppose you could steel a syntax highlighter from somewhere (maybe VScode?) and use that as well.

#### [Johan Commelin (Oct 17 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964031):
Also, if you don't care about Lean/mathlib style guides, I would suggest calling the type underlying your `comm_ring` just `R` instead of `α`.

#### [Johan Commelin (Oct 17 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964166):
You write
```quote
 (There is no obvious way to supply an alternative name; Lean rejects `variable [R : comm_ring α]`, for reasons that are not clear to me.)
```
That is very weird, because Scott is doing this all the time in his category libs. Do you get an actual error?
Maybe you should write `include R` afterwards. That will include the instance in all your local contexts. Does that help?

#### [Johan Commelin (Oct 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964326):
You also write
```quote
 The resulting heuristics are often effective, but it is also fairly common for the simplifier to apply rules in a way that is unhelpful. In those cases one can instead use the `rewrite` tactic (which can be abbreviated as `rw`) to give finer control over what rules are applied in what order. 
```
You might want to mention `simp only` and `simp [-rule]` that can be used to avoid bad simplification steps.

#### [Johan Commelin (Oct 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964342):
By the way, I must say that I really like these files! You wrote really extensive comments. Thanks a lot!

#### [Neil Strickland (Oct 17 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964796):
I hadn't noticed the ```simp only``` thing, thanks for pointing that out.  I will have a look and see whether that makes some steps easier.

#### [Johan Commelin (Oct 17 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964801):
@**Neil Strickland** Do you just want us to spam all our feedback into this thread? Or how should we organise this?

#### [Neil Strickland (Oct 17 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964958):
That's a good question.  I was thinking of putting the whole set of pages and associated code (including Coq and Isabelle stuff) on GitHub, but that will require some organisation, and I haven't really decided on the right structure.  So we should probably just use this thread for the time being.

#### [Kevin Buzzard (Oct 17 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964963):
Yes I already have some comments about your nilpotent proof

#### [Kevin Buzzard (Oct 17 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135964985):
(although I am currently on a tram in Sheffield -- are you coming to lunch with me?)

#### [Kevin Buzzard (Oct 17 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135965059):
Lines 520-620 or so -- these are of no interest to mathematicians and you never need all these intermediate lemmas. You can prove what you want in a couple of lines but it's incomprehensible in some sense. Proving these fiddly things is hard for beginners

#### [Floris van Doorn (Oct 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135973624):
> The definition comes from the file mathlib/data/nat/basic.lean (but I do not know a completely automatic way to obtain that information).

You can go to the location where the definition was defined either by ctrl+click, or by clicking on it, and then pressing F12. That will in particular give you the file in which it was defined.

#### [Bryan Gin-ge Chen (Oct 17 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135974877):
A few minor typos in the annotations to "primes": 

- line 10, "The declaration of `min_fac_prime` has the shape:" the declaration that follows is missing `<span class="code></span>` around it.

- line 13, "the implicit arguments 𝑝 and 𝑛 are deduced from the context." However, the code uses `@dvd_fact`.

- line 15, "The syntax `(...).mpr` extracts the left-to-right half of this equivalence," should be "right-to-left".

#### [Bryan Gin-ge Chen (Oct 17 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135975155):
Have you seen [the work in the "tutorials" branch in leanprover-community](https://github.com/leanprover-community/mathlib/tree/tutorials/tutorials)? The files `two_add_two.lean` and `partitions.lean` tackle tasks 1 and 5 from your MO post, respectively.

#### [Floris van Doorn (Oct 17 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135975455):
> Maybe you should write `include R` afterwards.

This is correct. Lean doesn't automatically inserts variables, unless they are **explicitly** mentioned in the definition. For example, if I write
```
variables {α β : Type} 
def my_id (a : α) : α := a
```
Then the definition `my_id` does *not* have `β` as an argument. If you want to explicitly add a variable/parameter `x` to all following definitions, you can write `include x` (and stop doing it with `omit x`). Because type-class variables are almost never *explicitly* mentioned, the (quite arbitrary) convention was added that if you don't give a type-class variable a name, it is automatically included if all variables in its type are included (so the variable `[comm_ring α]` is included when `α` is included).

#### [Kevin Buzzard (Oct 17 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135983921):
(deleted)

#### [Kevin Buzzard (Oct 17 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135983922):
PS `data.nat.binomial` was written by @**Chris Hughes**  -- an Imperial maths undergraduate :-)

#### [Neil Strickland (Oct 17 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135984404):
@**Bryan Gin-ge Chen**  and @**Johan Commelin** : are you happy for me to steal ```two_add_two.lean``` and ```partitions.lean``` and adapt them to the same framework that I have used for primes and nilpotents?

#### [Johan Commelin (Oct 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135984428):
I'm completely fine with that.

#### [Kevin Buzzard (Oct 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135984549):
@**Neil Strickland**  At line 528 you have `p := n + m + 1` and `Sn_gt_k : n + 1 > k` and you want `m < p - k`. Here's a relatively painless proof which avoids a bunch of intermediate steps.

```lean
import data.nat.basic
--lines 516-624
example (n m k : ℕ) (Sn_gt_k : k < n + 1):
let p := n + m + 1 in m < p - k := 
begin
  apply nat.lt_sub_right_of_add_lt,
  apply lt_of_lt_of_le (add_lt_add_left Sn_gt_k m),
  simp,
end
```

#### [Kevin Buzzard (Oct 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135984621):
I think it's hard for learners to prove these things -- I have to a certain extent got a nose for which way to go now, but it wouldn't surprise me if Chris, Kenny or Mario could pull off a one-liner. However the real point should be that this is trivial to a mathematician so ideally should be done with a tactic. I tried `linarith` (as did you) and I couldn't get it to work. Should it work?

#### [Bryan Gin-ge Chen (Oct 17 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135985306):
I'm fine with that too.

#### [Kevin Buzzard (Oct 17 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135986207):
```lean
 lemma npz_mul_right (x y : α) (n : ℕ) (xR : next_pow_zero x n) :
  (next_pow_zero (x * y) n) := 
  begin
    rw mul_comm,
    exact npz_mul_left y x n xR
  end
```

#### [Kevin Buzzard (Oct 17 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135986423):
Computer scientists like writing their proofs backwards because then they don't get extra hypotheses cluttering up the context ("things that used to be the goal" are not remembered, whereas old hypotheses are)

#### [Kevin Buzzard (Oct 17 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135986424):
```lean
have Z2 : (n * m + n + m) + 1 = (n + 1) * (m + 1),
    by simp[add_mul,mul_add,mul_one,one_mul,add_assoc],
```
I would just put `by ring` because why not.

#### [Johan Commelin (Oct 17 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135986431):
@**Neil Strickland** In the post by Kevin (above this one) you can see that `x` and `n` can be determined from `xR`. So you can make them implicit, by wrapping them in `{}` instead of `()`.

#### [Kevin Buzzard (Oct 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135987203):
The reason it's not dealt with automatically by `simp` is I believe that Leo removed `add_mul` and `mul_add` from the list of simp rules because of some CS reasons.

#### [Kevin Buzzard (Oct 17 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135987623):
Do you ever use `nilpotent_mul_right`and `npz_mul_right` ?

#### [Mario Carneiro (Oct 17 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135992615):
> because of some CS reasons

aka exponential blowup

#### [Kevin Buzzard (Oct 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135992675):
Like I said

#### [Mario Carneiro (Oct 17 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135992862):
>  There are mechanisms that allow Lean to obtain a commutative ring structure automatically from a field structure where necessary, but the resulting commutative ring structure is anonymous. It has been found convenient to include the line
>
> `instance : comm_ring ℚ          := by apply_instance`
>
> in data/rat.lean, which allows us to use the notation rat.comm_ring to refer to the standard commutative ring structure on $\mathbb{Q}$. 

Actually this is just to make it faster for lean to discover that Q has a comm_ring instance. Not sure if you want to mention that though.

#### [Mario Carneiro (Oct 17 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135993054):
> There is no obvious way to supply an alternative name; Lean rejects variable [R : comm_ring α], for reasons that are not clear to me.

Johan already mentioned this a bit, but unnamed instance variables are automatically included whenever the variable they reference is included, while a named variable is only included if it is used directly. So if you want to name an instance variable you have to put `include R` so it gets included even when it is not referenced.

#### [Mario Carneiro (Oct 17 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135993577):
>  We are given a proof (denoted n_le_m) that $n\leq m$. We now apply the theorem nat.succ_le_succ to convert it to a proof that $n+1\leq m+1$. Note that the conclusion of nat.succ_le_succ is actually that succ n ≤ succ m, where succ is the successor function as in Peano arithmetic. One needs to unwind the definitions of $1$ and $+$ to see that n + 1 is the same as succ n. It is not clear to me under what circumstances this unwinding happens automatically, but it seems to work here. 

Unfolding of definitions like this happens, quite aggressively, when lean expects something of type T and you give it something of type T', and it tries to figure out why T and T' are the same (definitionally equal). Most tactics, on the other hand, are sensitive to the exact way you write an expression, so for example `rw` would not work on a term of type `next_pow_zero` even though it is an equality after some unfolding. You can also obtain the result of line 18 in a more automatic way by using `unfold next_pow_zero at xR`.

#### [Mario Carneiro (Oct 17 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135993697):
L19:
>  Note that we have given the name Sn_le_Sm to our conclusion. The Lean documentation says that one can use the keyword have with no label, and use the keyword this to refer to the most recently proved statement. However, this does not seem to work here. I think that this is because we are in tactic mode, and anonymous have only works outside that mode. But the full story is not clear to me. 

Anonymous have should work here. You can put `have : n + 1 ≤ m + 1 := (succ_le_succ n_le_m),` on this line and use `this` instead of `Sn_le_Sm` in L21, and it should work. If not, let me know what error you get

#### [Mario Carneiro (Oct 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/135998372):
Unless you specifically want to focus on nat subtraction and how annoying it is to work with for pedagogical reasons, I would suggest using `le.dest` to avoid it altogether. This also gives you a chance to use `rcases` which I think is worth calling out.
```lean
lemma npz_shift
  (x : α) (n m : ℕ) (xR : next_pow_zero x n) (n_le_m : n ≤ m) : 
    next_pow_zero x m := 
begin
  unfold next_pow_zero at xR,
  have : n + 1 ≤ m + 1 := succ_le_succ n_le_m,
  have : ∃ k, (n + 1) + k = (m + 1) := le.dest this,
  rcases this with ⟨k, SnkSm⟩,
  show x^(m + 1) = 0,
  rw [← SnkSm, _root_.pow_add, xR, zero_mul],
end
```

#### [Mario Carneiro (Oct 17 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136000972):
Here's a proof of `npz_add` with a few comments of my own. I tried not to over-optimize it and keep it pedagogical:
```lean
-- The first few parameters are implicit because they follow from the types of xR and yR
lemma npz_add {x y : α} {n m : ℕ}
  (xR : next_pow_zero x n) (yR : next_pow_zero y m) :
  next_pow_zero (x + y) (n + m) := 
begin
  unfold next_pow_zero at xR yR ⊢,
  -- we want to unfold this definition everywhere so it doesn't get in the way
  let p := n + m + 1,
  suffices : ∀ (k : ℕ) (h : k ∈ (range (succ p))),
    x ^ k * y ^ (p - k) * ↑(choose p k) = 0,
  -- Let us use suffices so that we know why we are proving this
  { exact calc (x + y)^p
        = (range (succ p)).sum (λ k, x ^ k * y ^ (p - k) * ↑(choose p k))
        : add_pow x y p -- use binomial theorem
    ... = (range (succ p)).sum (λ k, (0 : α))
        : finset.sum_congr rfl this -- use the assumption
    ... = 0 : sum_const_zero },
  -- note for Neil: use {} instead of begin end to make it clearer that syntax
  -- in tactic mode is different than term mode.
  -- Similarly 'by' is unnecessary in tactic mode
  intros k h,
  have k_lt_Sp : k < p + 1 := mem_range.mp h,
  have k_le_p : k ≤ p := le_of_lt_succ k_lt_Sp,
  -- note the name of the theorem is derivable from the statement (very important!)
  rcases le_or_gt (n + 1) k with Sn_le_k | Sn_gt_k,
  { rcases le.dest Sn_le_k with ⟨j, Z0⟩, -- note Z0 : (n + 1) + j = k
    have Z1 : x ^ (n + 1) = 0 := xR,
    -- Note at this point that theorem Z2 is actually a special case
    -- of npz_shift, so maybe we should go back and generalize it? Exercise for the reader
    have Z2 : x ^ k = 0,
    { rw [← Z0, -- x ^ (n + 1 + j) = 0
        _root_.pow_add, -- x ^ (n + 1) * x ^ j = 0
        Z1, -- 0 * x ^ j = 0
        zero_mul] },
    simp [Z2] },
  { have k_le_n : k ≤ n := lt_succ_iff.mp Sn_gt_k,
    rcases le.dest k_le_n with ⟨j, Z0⟩, -- Z0 : k + j = n
    have Z4 : p - k = (m + 1) + j,
    { apply nat.sub_eq_of_eq_add,
      -- get rid of the subtraction because nat subtraction sucks
      simp [p, Z0.symm] },
      -- After unfolding p and using Z0.symm : n = k + j, the goal is
      -- (k + j) + m + 1 = k + (m + 1 + j) which simp can handle
      -- (just associativity and commutativity of addition)
    have Z6 : y ^ (p - k) = 0,
    { rw [Z4, _root_.pow_add, yR, zero_mul] },
    simp [Z6] }
end
```

#### [Alex J. Best (Oct 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136009280):
Hi @**Neil Strickland**  the viewer is really cool! The tex doesn't load for me though but if I add ```MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
``` to viewer.js line 102 above  ```this.show_comment(0);``` it does.

#### [Neil Strickland (Oct 18 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136015026):
Thanks to everyone for your feedback.  I am working on incorporating it and also improving my infrastructure in various ways; I will report back in a day or two.

#### [Scott Morrison (Oct 18 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136016513):
I'd love to see your infrastructure turn into `leandoc`. :-)

#### [Scott Morrison (Oct 18 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136016580):
Can I suggest that you don't embed html in the source code, but use markdown instead? I don't think we're ever going to want to include html in source files, but markdown ($ ... $ for math is of course fine) is great.

#### [David Michael Roberts (Oct 18 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136026586):
@**Neil Strickland** I am using the latest version of Chrome (69.0.3497.100 (Official Build) (64-bit)) on OS X 10.10.5 and I see this: [Code from "There are infinitely many primes"](/user_uploads/3121/Cb0AG3O7WFQGsv-jamxweKyi/Screen-Shot-2018-10-18-at-6.25.03-pm.png)

#### [Bryan Gin-ge Chen (Oct 18 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136053537):
Line 145 in `nilpotents`:
```lean 
def is_reduced (α : Type*) [comm_ring α] : Prop :=
```
>I am not completely clear about the mechanism for handling implicit and explicit arguments here. At the beginning of this file we opened a section and had the declaration `variable {α : Type u}`. [...] It seems that the declaration here overrides the default behaviour and converts `𝛼` to an explicit argument. The ring structure on `𝛼` remains an implicit argument handled by typeclass inference, however. 

It's my understanding that when you explicitly include in a `def` some variable `𝛼` with the same name as one in an earlier `variable` declaration, lean locally creates a new variable which is unrelated to the other `𝛼`; in particular, previous typeclass assignments won't apply to the new `𝛼`, and that's why you had to put in `[comm_ring 𝛼]` here again. 

To convert an existing variable from implicit to explicit, write `variable (𝛼)` on the line before this definition. Then when you want to let `𝛼` be implicit again (presumably after 158), you can write `variable {𝛼}`.

#### [Bryan Gin-ge Chen (Oct 18 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dagstuhl%20tasks/near/136055004):
Typo in the comments to line 153-154 in `nilpotents`: there's a missing space in "`init/data/setoid.lean`in".

Including the types explicitly in lines 153 and 159 would make things more readable to me: ` def reduced_quotient (α : Type*) [comm_ring α] : Type* :=` and `instance reduced_quotient_mk_is_ring_hom : is_ring_hom quotient_ring.mk :=`.

I'm not sure what "further problems related to implicit arguments" occurred that required you to write lines 168-178 but if you say more perhaps we can figure it out.

