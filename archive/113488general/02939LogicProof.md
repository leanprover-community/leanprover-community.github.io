---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02939LogicProof.html
---

## [general](index.html)
### [Logic & Proof](02939LogicProof.html)

#### [Kaushik Chakraborty (Jun 07 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127707574):
Hi, I am going through the online course Logic and Proof. I am stuck in the exercises. Is this the right place to ask such questions?

#### [Chris Hughes (Jun 07 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127707694):
Yes

#### [Kaushik Chakraborty (Jun 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708058):
Thanks. So I'm stuck progressing with the last prob. of [Chapter 4's exercises](https://leanprover.github.io/logic_and_proof/propositional_logic_in_lean.html#exercises) i.e. prove `¬ (A ↔ ¬ A)`

#### [Kaushik Chakraborty (Jun 07 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708189):
I am thinking of following the rules mentioned in the book till now and start with the assumption that `(A ↔ ¬ A)`is true and then progress to show `false` so that I can prove the negation. But I can't figure out a way forward

#### [Kenny Lau (Jun 07 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708218):
hint: prove `¬ A` from your assumption

#### [Chris Hughes (Jun 07 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708555):
This actually came up in M1F, and I was annoyed with myself for assuming excluded middle.

#### [Kenny Lau (Jun 07 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708566):
not constructive enough, eh :P

#### [Kaushik Chakraborty (Jun 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708801):
am failing to get how can I get `¬ A` with just assuming `A ↔ ¬ A`. I can get it if I also assume `A` and apply left elimination to the iff to get `¬ A`. Is my understanding correct ?

#### [Kenny Lau (Jun 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708812):
no, you need to assume `A` and prove `false`

#### [Kenny Lau (Jun 07 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708823):
ok, which you get via deducing `¬ A`

#### [Chris Hughes (Jun 07 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708944):
Try `have h : ¬ A`

#### [Kaushik Chakraborty (Jun 07 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127708955):
I am trying to do something like that but I am getting a type mismatch error coz of the additional assumption. 
Could you please look at this [LEAN code](https://leanprover.github.io/live/3.4.1/#code=variables%20A%20:%20Prop%0A%0Aexample%20:%20¬%20(A%20↔%20¬%20A)%20:=%0Aassume%20h,%0Aassume%20a%20:%20A,%0Ahave%20h1%20:%20¬%20A,%20from%20h.mp%20a,%0Ashow%20false,%20from%20h1%20a)

#### [Chris Hughes (Jun 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709050):
You can only do `assume a : A` if your goal is `A → something`

#### [Chris Hughes (Jun 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709059):
Have you used `have` before?

#### [Kenny Lau (Jun 07 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709121):
```lean
variables A : Prop

example : ¬ (A ↔ ¬ A) :=
assume h,
have h1 : ¬ A, from _,
show false, from _
```

#### [Kenny Lau (Jun 07 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709126):
so your code should look like this

#### [Kaushik Chakraborty (Jun 07 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709348):
yeah that's what I am trying but could not think of any intro/elim rule to apply to get `¬ A` from `h`

#### [Moses Schönfinkel (Jun 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709518):
The biggest hint here was the innocuous sentence "...and I was annoyed with myself for assuming excluded middle" :). You can't conjure `not A` from thin air, but you *can* conjure something almost as good.

#### [Kaushik Chakraborty (Jun 07 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709738):
Ok I think I got it

```
variables A : Prop

example : ¬ (A ↔ ¬ A) :=
assume h,
have h1 : ¬ A, from 
    assume a : A,
    show false, from (h.mp a) a,
show false, from h1 (h.mpr h1)
```

#### [Kaushik Chakraborty (Jun 07 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/127709838):
thanks a lot for the guidance

#### [Kaushik Chakraborty (Jul 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129916601):
Hello again. I want to do the exercise 17.1 of the course on proving the equivalence of *principle of complete induction* to *principle of least element* in Lean. So in that regard does the following setup make sense? I still need to do the actual proof. 

```lean
variable P : ℕ → Prop

example : ∀ n, (∀ m, m < n ∧ P(m) →  P(n)) → ∀ x, P(x) ↔ 
                ∀ n, P(n) ∧ ∃ m x, m < n ∧ ¬ (x < m) → P(m) :=
sorry
```

#### [Mario Carneiro (Jul 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129917107):
the parentheses seem to be off in a few places

#### [Mario Carneiro (Jul 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129917793):
I think this is correct with minimal parentheses:
```lean
variable P : ℕ → Prop

example : ((∀ n, (∀ m, m < n → P m) → P n) → ∀ x, P x) ↔
            ∀ n, P n → ∃ m, P m ∧ ∀ x, x < m → ¬ P x :=
sorry
```

#### [Mario Carneiro (Jul 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129917947):
the statement of the principle of least element you gave looks really weird and is probably incorrect - I've changed the statement a bit

#### [Mario Carneiro (Jul 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129917995):
I expect it to say something like "if P(n) for some n, then there exists an m such that P(m), and ¬ P(x) for all smaller x"

#### [Johan Commelin (Jul 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918082):
The current statement reads to me as "I can prove `P` by induction iff the principle of least element holds for `P`"

#### [Mario Carneiro (Jul 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918311):
My point is that the right hand side doesn't look like the PLE to me

#### [Johan Commelin (Jul 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918399):
Oooh, you are completely right. The right hand side should start with `\exists`. As stated it is trivial: take `m = 0`.

#### [Mario Carneiro (Jul 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918405):
Also, I don't think this will actually work (unless you prove both sides individually), since the traditional reduction of induction to PLE and vice versa involves negating P

#### [Mario Carneiro (Jul 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918425):
this can be rectified by quantifying P individually on each side:
```lean
example : (∀ P : ℕ → Prop, (∀ n, (∀ m, m < n → P m) → P n) → ∀ x, P x) ↔
           ∀ (P : ℕ → Prop) n, P n → ∃ m, P m ∧ ∀ x, x < m → ¬ P x :=
sorry
```

#### [Kaushik Chakraborty (Jul 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918491):
Ok. I got the formalization of PLE. Thanks

#### [Kaushik Chakraborty (Jul 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918612):
although in your formalization of PLE, there is no relation between `n` and `m`. Shouldn't we mention that `m < n` ?

#### [Mario Carneiro (Jul 19 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129918986):
There is no need, in the same way that there is no relation between n and x in the statement of induction

#### [Mario Carneiro (Jul 19 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129919018):
You can prove, given the conclusion, that `m <= n`, but it is possible that `m = n` if `n` is already the minimal witness

#### [Mario Carneiro (Jul 19 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129919095):
another way to bracket it is `∀ (P : ℕ → Prop), (∃ n, P n) → ∃ m, P m ∧ ∀ x, x < m → ¬ P x`

#### [Kaushik Chakraborty (Jul 19 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/129919210):
Ok got it.

#### [Kaushik Chakraborty (Jul 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138371):
I'm stuck at this simple proof. how do I go from `n * n < m * m` to `n ^ 2 < m ^2`

```
open nat
variables n m : ℕ 

example : 0 < n ∧ n < m → n ^ 2 < m ^ 2 :=
assume h,
have n * n < n * m, from mul_lt_mul_of_pos_left h.right h.left,
have n * m < m * m, from mul_lt_mul_of_pos_right h.right (lt_trans h.left h.right),
have n * n < m * m, from lt_trans ‹ n * n < n * m › ‹ n * m < m * m ›,
sorry
```

#### [Kenny Lau (Jul 23 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138666):
```lean
open nat
variables n m : ℕ

example : 0 < n ∧ n < m → n ^ 2 < m ^ 2 :=
assume h,
calc  n ^ 2
    = nat.pow n 2 : by dsimp [(^)]; refl
... = 1 * (n * n) : nat.mul_assoc 1 n n
... = n * n : nat.one_mul _
... < n * m : mul_lt_mul_of_pos_left h.right h.left
... < m * m : mul_lt_mul_of_pos_right h.right (lt_trans h.left h.right)
... = m ^ 2 : by simp [(^), nat.pow]
```

#### [Kenny Lau (Jul 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138680):
@**Mario Carneiro** why can't I replace `by dsimp [(^)]; refl` with `rfl`?

#### [Chris Hughes (Jul 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138725):
Definitional equality is not transitive.

#### [Kenny Lau (Jul 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138729):
but then why does this work?

#### [Kenny Lau (Jul 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138731):
```lean
example : n ^ 2 = nat.pow n 2 := rfl
```

#### [Kenny Lau (Jul 23 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138738):
Definitional equality is not consistent either?

#### [Kaushik Chakraborty (Jul 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130138817):
thanks @**Kenny Lau** . I still don't understand tactics. Maybe the theorem proving in lean course will help. Logic and Proof course have few mentions of tactics.

#### [Johan Commelin (Jul 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130139007):
Kaushik, to answer your original question, there is `pow_two` which you can use to rewrite between `n * n` and `n^2`.

#### [Kenny Lau (Jul 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130139020):
it's not available without further import though

#### [Johan Commelin (Jul 23 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130139360):
Right, you need to import `algebra.group_power`, I think.

#### [Kaushik Chakraborty (Jul 23 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130140974):
thanks @**Johan Commelin**. but am still not sure how to use `pow_two` in my proof. I think I have to use `rewrite` tactic but not sure how. Here is how I've changed my earlier proof

```
import algebra.group_power
open nat
variables n m : ℕ

example : 0 < n ∧ n < m → n ^ 2 < m ^ 2 :=
assume h,
have n * n < n * m, from mul_lt_mul_of_pos_left h.right h.left,
have n ^ 2 < n * m, by sorry,
have n * m < m * m, from mul_lt_mul_of_pos_right h.right (lt_trans h.left h.right),
have n * m < m ^ 2, by sorry,
lt_trans ‹ n ^ 2 < n * m ›  ‹ n * m < m ^ 2 › 
```

#### [Johan Commelin (Jul 23 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130141157):
```lean
example (n : ℤ) : n ^ 2 = n * n :=
begin
  rewrite pow_two
end
```

#### [Kenny Lau (Jul 23 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130141225):
```lean
example (n : ℤ) : n ^ 2 = n * n := pow_two n
```

#### [Kaushik Chakraborty (Jul 23 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130141616):
yeah I got the function usage part but how do I use `pow_two` when I've the `lt` relation i.e. replace sorry in `have n ^ 2 <  n * m, by sorry` when I've established `n * n < n * m`. Or I'm approaching it wrong ?

#### [Kevin Buzzard (Jul 23 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130168976):
You should be able to do this with `rw`

#### [Kevin Buzzard (Jul 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169439):
```lean
import algebra.group_power

example (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m :=
begin
  have H : n ^ 2 = n * n := pow_two n,
  rw H,
  exact h
end 

```

#### [Kevin Buzzard (Jul 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169462):
You should also be able to do it with `eq.subst` but I can never ever ever for the life of me get it to work.

#### [Kenny Lau (Jul 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169478):
`\t`

#### [Kevin Buzzard (Jul 23 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169502):
```lean
import algebra.group_power

example (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m := (pow_two n).symm ▸ h
```

[doesn't work]

#### [Kevin Buzzard (Jul 23 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169525):
Can you fix it Kenny?

#### [Kenny Lau (Jul 23 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169559):
I think you would like `by convert h`

#### [Kenny Lau (Jul 23 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169633):
```lean
import algebra.group_power

example (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m :=
have H : n * n = n ^ 2, from eq.symm $ pow_two n,
H ▸ h
```

#### [Kenny Lau (Jul 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169668):
I'm not sure why your original version doesn't work

#### [Kenny Lau (Jul 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169677):
```lean
import algebra.group_power

example (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m :=
by convert h; from pow_two n
```

#### [Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169688):
```lean
example (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m := 
((((pow_two n).symm : n * n = n ^ 2) ▸ (h : n * n < n * m)) : n ^ 2 < n * m)
```

#### [Kenny Lau (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169727):
:o

#### [Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169729):
```
invalid 'eq.subst' application, elaborator has special support for this kind of application (it is handled as an "eliminator"), but expected type must not contain metavariables
  n ^ 2 < n * m
```

#### [Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169733):
I see no metavariables!

#### [Kenny Lau (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169743):
yeah I'm puzzled too

#### [Chris Hughes (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169747):
`example (m n : ℤ) (h : n * n < n * m) : n ^ (2 : ℕ) < n * m := (pow_two n).symm ▸ h`

#### [Kenny Lau (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169752):
...

#### [Chris Hughes (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169753):
works

#### [Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169755):
...

#### [Kevin Buzzard (Jul 23 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169775):
The well-known metavariable `2`

#### [Kevin Buzzard (Jul 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169932):
```
invalid 'eq.subst' application, elaborator has special support for this kind of application (it is handled as an "eliminator"), but expected type must not contain metavariables
  @has_lt.lt.{0} int int.has_lt
    (@has_pow.pow.{0 ?l_1} int ?m_2 ?m_3 n (@bit0.{?l_1} ?m_2 ?m_4 (@has_one.one.{?l_1} ?m_2 ?m_5)))
    (@has_mul.mul.{0} int int.has_mul n m)
```

#### [Kevin Buzzard (Jul 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169934):
Indeed there was a metavariable

#### [Chris Hughes (Jul 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169942):
This works `lemma thing (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m := (pow_two n).symm ▸ h`

#### [Kenny Lau (Jul 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169949):
?????????????????

#### [Chris Hughes (Jul 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130169960):
not this though `def thing (m n : ℤ) (h : n * n < n * m) : n ^ 2 < n * m := (pow_two n).symm ▸ h`

#### [Kevin Buzzard (Jul 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130170018):
I think this is a bug in `pow_two` -- the inbuilt `2` is a nat

#### [Kevin Buzzard (Jul 23 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130170049):
Clearly pow_two should be a definition not a theorem

#### [Kevin Buzzard (Jul 23 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130170055):
Or am I barking up the wrong tree ;-)

#### [Kenny Lau (Jul 23 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130170117):
I agree. Split the definition into more cases for easier definitional equality.

#### [Chris Hughes (Jul 23 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130170126):
I don't think it has anything to do with `pow_two`
```lean
lemma two_add_three : 2 + 3 = 5 := add_comm 0 5 ▸ rfl -- works

example : 2 + 3 = 5 := add_comm 0 5 ▸ rfl -- doesn't work
```

#### [Kevin Buzzard (Jul 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130171125):
`example : (2 : ℕ) + 3 = 5 := add_comm 0 5 ▸ rfl -- works`

#### [Kevin Buzzard (Jul 23 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130171160):
So the bit where it says "Ok I can't figure out the type of this `2` thing, let's let it be `nat` just so we can get on" is not occurring in the `example`s

#### [Kevin Buzzard (Jul 23 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130171165):
Maybe `pow_two` should have been an example. Wait...

#### [Mario Carneiro (Jul 24 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130180460):
The reason that `example` and `def` fail while `theorem` succeeds is due to the separation of statement and proof done with `theorem`

#### [Mario Carneiro (Jul 24 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130180493):
Remember how I mentioned a long time ago that `nat` is the default type for numerals but it occurs very late in the elaboration? It's basically the last resort if there is a numeral of indeterminate type

#### [Mario Carneiro (Jul 24 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130180615):
In regard to this example, what happens is that since `def`/`example` allows the statement and proof to be elaborated together, it checks the proof to see if that will give a hint what is alpha in `(2:alpha) + 3 = 5`. But that means that when it hits the `eq.subst` it will still have a lingering metavariable. In the `theorem` case, there is no information to be had, since the proof doesn't contribute to elaborating the statement, so it goes with the default `nat` type for numerals. Then when it elaborates the proof, there are no metavariables

#### [Kaushik Chakraborty (Jul 25 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130244645):
For this code in the LEAN live in-browser IDE

```lean
import algebra.group_power
theorem thing (m n : ℕ) (h : n * n < n * m) : (n ^ 2 < n * m) := (pow_two n).symm ▸ h
```

am getting following error

```lean
"eliminator" elaborator type mismatch, term
  h
has type
  n * n < n * m
but is expected to have type
  n ^ 2 < n * m
Additional information:
/test.lean:2:82: context: the inferred motive for the eliminator-like application is
  λ (_x : ℕ), n ^ 2 < n * m
```

#### [Kevin Buzzard (Jul 25 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130244817):
Join the `▸`-haters club!

#### [Kevin Buzzard (Jul 25 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130244863):
Sometimes the issue is that higher-order unification is undecidable, sometimes I've just made a silly mistake.

#### [Chris Hughes (Jul 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130244921):
The mistake here is that `pow_two` is a theorem about `monoid.pow` and not `nat.pow`

#### [Kevin Buzzard (Jul 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130244927):
yes, I just realised that when trying to solve without the triangle

#### [Kevin Buzzard (Jul 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130244928):
```
invalid type ascription, term has type
  @has_lt.lt nat nat.has_lt (@has_pow.pow nat nat (@monoid.has_pow nat nat.monoid) n 2)
    (@has_mul.mul nat nat.has_mul n m)
but is expected to have type
  @has_lt.lt nat nat.has_lt (@has_pow.pow nat nat nat.has_pow n 2) (@has_mul.mul nat nat.has_mul n m)
```

#### [Kevin Buzzard (Jul 25 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130245103):
```lean
theorem nat.pow_two (a : ℕ) : a ^ 2 = a * a := show (1 * a) * a = a * a, by rw one_mul

theorem thing (m n : ℕ) (h : n * n < n * m) : (n ^ 2 < n * m) := (nat.pow_two n).symm ▸ h

```

#### [Kaushik Chakraborty (Jul 25 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130246833):
thanks @**Kevin Buzzard**  this worked. however, I have some doubts about the `nat.pow_two` theorem. In your proof, you showed a different equality than what is in the sig. of the theorem. Is Lean somehow guessing the fact that `(1 * a) * a = a ^ 2`. Or how is the rewrite tactics working here?

#### [Nicholas Scheel (Jul 25 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130247804):
that’s obtained by unfolding the definition of `pow`, which basically is that `n^a = (((1*n)*n)*...)*n` (with `a` `n`s of course)

#### [Kaushik Chakraborty (Jul 25 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130261244):
got it. thanks, @**Nicholas Scheel**

#### [Kevin Buzzard (Jul 25 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/130263722):
Yes, there are two kinds of equality in Lean. There's "equal by definition" and "equal because of a theorem". `a^2=1*a*a` is true by definition of `^` (you can discover this sort of thing by continually unfolding everything -- switch off notation and just get unfolding in tactic mode and see where you go) but `1*a=a` is true because of a theorem. Things that are equal by definition you can just use interchangeably (I used `show` to change the goal to a goal which Lean thinks is the same goal by definition), but then I used a rewrite to apply the theorem.

#### [Kaushik Chakraborty (Aug 09 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131140816):
I am trying to attempt a Lean proof of quotient-remainder theorem shown [here](https://leanprover.github.io/logic_and_proof/elementary_number_theory.html#the-quotient-remainder-theorem) and, as usual, clueless on the approach. I've tried to chalk out a rough skeleton of the proof based on my understandings from an earlier chapter on doing induction in Lean & some exploration of Lean's types and functions. Does it make sense?

```
open int
open nat

 -- quotient / remainder theorem
theorem qt (n m q r : ℤ) : m > 0 → n = m * q + r ∧ (0 ≤ r ∧ r < m) :=
assume h,
show (n = m * q + r) ∧ (0 ≤ r ∧ r < m), from
  int.rec_on n
  (assume k,
  show (of_nat k = m * q + r) ∧ ( 0 ≤ r ∧ r < m ), from
    nat.rec_on k
      (show (of_nat 0 = m * q + r) ∧ (0 ≤ r ∧ r < m), from sorry)
      (assume k ih,
        show of_nat (succ k) = m * q + r ∧ (0 ≤ r ∧ r < m), from sorry)
  )
  (assume k,
    have h11 : -of_nat (k + 1) = m * q + r, from sorry,
    have h22 : 0 ≤ r ∧ r < m, from sorry,
    ⟨ h11 , h22 ⟩)
```

#### [Chris Hughes (Aug 09 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131141198):
The theorem isn't true. This says for all n m q r, ... Whereas you want `forall m n, exists q r,...`

#### [Chris Hughes (Aug 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131141265):
the proof of this theorem in the lean library is a combination of `int.mod_add_div`, `int.mod_lt`  and `int.mod_nonneg`.

#### [Kaushik Chakraborty (Aug 09 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131151108):
Oh, thanks for clarifying. Does this theorem statement make sense?

```
theorem qt : ∀ n m : ℤ, m > 0 → ∃ q r : ℤ, (n = m * q + r) ∧ (0 ≤ r ∧ r < m) :=
sorry
```

#### [Kaushik Chakraborty (Aug 09 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131155084):
I tried to solve the above statement with the functions you mentioned but I could not figure out how to come up with the existential terms `q` & `r` from `n` and  `m` and hence the proof does not type check. I must be formulating the theorem statement wrong or missing some approach in the proof.

```
theorem qt : ∀ n m : ℤ, m > 0 → ∃ q r : ℤ, n = m * q + r ∧ (0 ≤ r ∧ r < m) :=
assume n m h,

assume q r,
assume h2 : q = n / m,
assume h1 : r = n % m,

have HH:  n = m * q + r, from calc
  n = n % m + m * (n / m) : by rw [int.mod_add_div]
  ... = r + m * (n / m) : by rw h1
  ... = r + (m * q) : by rw h2
  ... = (m * q) + r : by rw add_comm,

have HH1: 0 ≤ r, from calc
  0 ≤ n % m : int.mod_nonneg n (ne_of_gt h)
  ... ≤ r : by rw h1,

have HH2: r < m, from calc
  r = n % m : by rw h1
  ... < abs m : int.mod_lt n (ne_of_gt h)
  ... = m : abs_of_pos h,

exists.intro q (exists.intro r (and.intro HH  (and.intro HH1 HH2) ))
```

#### [Mario Carneiro (Aug 09 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131155253):
This is an incorrect use of the `assume` keyword. `assume` is used *only* for proving a forall or pi or implication, and it introduces a variable with the type specified in the domain. To prove an existential, you use `exists.intro` and provide the witness you want

#### [Mario Carneiro (Aug 09 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131155369):
So after `assume n m h,` you should write `exists.intro (n / m) $ exists.intro (n % m) $` instead of `assume q r, assume h2 : q = n / m, assume h1 : r = n % m,`

#### [Mario Carneiro (Aug 09 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131155379):
(The dollar signs are to save on having to close parentheses at the end of the proof)

#### [Mario Carneiro (Aug 09 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131155394):
After that, `q` and `r` will no longer be present in the statement, so you won't need to rewrite with `h1` anymore

#### [Kaushik Chakraborty (Aug 09 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic & Proof/near/131157187):
I knew what was wrong with that *assume* but your tip on the `exists.intro` was helpful. Here's my updated proof which type checks

```
theorem qt : ∀ n m : ℤ, m > 0 → ∃ q r : ℤ, n = m * q + r ∧ (0 ≤ r ∧ r < m) :=
assume n m h,

exists.intro (n / m) $ exists.intro (n % m) $

  have HH:  n = m * (n / m)  + (n % m), from calc
    n = n % m + m * (n / m) : by rw [int.mod_add_div]
    ... = m * (n / m) + (n % m) : by rw add_comm,

  have HH1: 0 ≤ (n % m), from int.mod_nonneg n (ne_of_gt h),

  have HH2: (n % m) < m, from calc
    (n % m) < abs m : int.mod_lt n (ne_of_gt h)
    ... = m : abs_of_pos h,

  ⟨ HH , ⟨ HH1 , HH2 ⟩ ⟩

```

