---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96855definingapredicate.html
---

## Stream: [new members](index.html)
### Topic: [defining a predicate](96855definingapredicate.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Nov 26 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148346494):
Hi,

I do not have a lot of experience using computer theorem provers, and I have just started trying to learn Lean. As practice I am attempting to formalize and prove that the Principle of Induction implies the Principle of Induction from a Starting Point. So far I have:

```
open nat

-- Principle of Induction -> Principle of Induction from a Starting Point
example : ( forall P : nat -> Prop, ( ( P 0 /\ ( forall n, ( P n -> P (n + 1) ) ) ) -> ( forall n, P n ) ) ) -> ( forall Q : nat -> Prop, forall m, ( ( Q m /\ ( forall n, ( ( n >= m ) -> ( Q n -> Q (n + 1) ) ) ) ) -> ( forall n, ( ( n >= m ) -> Q n ) ) ) ) :=
	assume a1 : forall P : nat -> Prop, ( ( P 0 /\ ( forall n, ( P n -> P (n + 1) ) ) ) -> ( forall n, P n ) ),
		assume Q : nat -> Prop,
			assume m : nat,
				assume a2 : ( Q m /\ ( forall n, ( ( n >= m ) -> ( Q n -> Q (n + 1) ) ) ) ),
				have s1 : Q m, from and.left a2,
				have s2 : forall n, ( ( n >= m ) -> ( Q n -> Q (n + 1) ) ), from and.right a2,
				have s3 : forall n, ( Q (n + m) -> Q ((n + m) + 1) ), from
					assume n : nat,
					have s4 : ( ( (n + m) >= m ) -> ( Q (n + m) -> Q ((n + m) + 1) ) ), from s2 (n + m),
					have s5 : (n + m) >= m, from sorry,
					show ( Q (n + m) -> Q ((n + m) + 1) ), from s4 s5,

				-- define P' n to hold if and only if Q (m + n) holds
				-- then P' 0 holds by s1, and forall n, ( P' n -> P' (n + 1) ) holds by s3
				-- then forall n, P' n holds by a1
				-- then Q (m + n) holds for all n
				-- then Q holds for all n >= m
```

I am currently trying to define a predicate P' n : nat -> Prop that holds if and only if the predicate Q holds for m + n. Is there any chance that someone could show me how this can be done?

Thank you very much for your time,
Patrick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347104):
Hi @**Patrick Thomas** Welcome to Lean (and Zulip).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347120):
This is certainly possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347174):
By the way (depending on taste) you can make your code a bit more readable by using unicode.
For example, you can type `\and` or `\to` to get nice symbols for `/\` and `->`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Nov 26 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347184):
Thank you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347204):
Are you using mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347211):
Because there must be some lemma in `data/nat/basic.lean` that will tell you that `(n - m) + m = n` if `n ≥ m`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Nov 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347271):
No. I just read about it a couple of minutes ago actually.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347275):
Aah, it will be very helpful. There's tons of useful little facts in there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347279):
Do you have a CS or a maths background, or both?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Nov 26 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347497):
I did an undergraduate degree in CS and physics, and have a strong interest in math. I started studying mathematical logic about a year ago in an attempt to understand computer proof assistants.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347559):
Ok, cool. There's a nice mix of CS and math in this community.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Nov 26 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148348284):
```quote
Because there must be some lemma in `data/nat/basic.lean` that will tell you that `(n - m) + m = n` if `n ≥ m`.
```
I'm sorry, I'm not certain how I would use this in the proof. Is this in relation to step s5?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148349209):
@**Patrick Thomas** I would first state something like `let P' : Prop := foobar,`
and then `have quux : Q \iff P' := xyzzy,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 26 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148349216):
In that latter proof you will need some lemma from mathlib, I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 26 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148353577):
To define something in a proof, you can use `let`. In this case `let P' := λ n, Q (m + n)` will do. Here is a short proof following mathlib style. This is probably too dense for a first cut but I'm sure someone around here can unpack this a bit.
```lean
example
  (H : ∀ P : nat → Prop, P 0 → (∀ n, P n → P (n + 1)) → ∀ n, P n)
  (Q : nat → Prop) (m)
  (h₁ : Q m) (h₂ : ∀ n ≥ m, Q n → Q (n + 1)) (n) (mn : n ≥ m) : Q n :=
let P' := λ n, Q (m + n) in
have P' (n - m), from H P' h₁ (λ n, h₂ _ (nat.le_add_right m n)) (n - m),
by simp [P'] at this; rwa nat.add_sub_cancel' mn at this
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148353667):
`simp [P'] at this` is using Lean's inbuilt simplifier to do a lot of dirty work involving equalities; `rwa` means "rewrite, then use an assumption". Both `simp` and `rw` are talked about in Theorem Proving in Lean, in the chapter on tactics: https://leanprover.github.io/theorem_proving_in_lean/tactics.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Nov 28 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148691325):
Thank you! This has helped.


{% endraw %}
