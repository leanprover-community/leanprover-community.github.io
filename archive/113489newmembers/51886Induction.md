---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/51886Induction.html
---

## Stream: [new members](index.html)
### Topic: [Induction](51886Induction.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Sep 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134579977):
Hello again! I'm still having a little trouble with my induction. In the example below the second dite gives me
```lean
term
  λ (h : card s ≠ n), sol.v s _
has type
  Π (h : card s ≠ n) (y : α), y ∈ sol.V s _ → β
but is expected to have type
  ¬card s = n → Π (y : α), y ∈ V s hs → β
```
But by the definition, V s hs should be the same as sol.V s (lt_of_ne s hs h)?
```lean
import data.finset
open nat finset

def names : finset string := {"BARC", "HSBC", "LLOY", "NATW", "RBSG", "SANT", "STDCH"}
def B : Type := {s : string // s ∈ names}

structure soln (α β : Type) (n : nat) :=
(V : Π (s : finset B), card s < n → set α)
(v : Π (s : finset B) (hs : card s < n) (y : α), y ∈ V s hs → β)

variable {find_domain (α β : Type) (n : nat) (s : finset B) : card s = n → soln α β n → set α}
variable {solve_pde (α β : Type) (n : nat) (s : finset B) : card s = n → soln α β n → Π (V : set α) (y : α), y ∈ V → β}

def solve_system {α β : Type} : Π (n : nat), soln α β n :=
nat.rec
    (let V (s : finset B) (hs : card s < 0) : set α := false.elim (not_lt_zero (card s) hs) in
        let v (s : finset B) (hs : card s < 0) : Π (y : α), y ∈ V s hs → β := false.elim (not_lt_zero (card s) hs) in
        @soln.mk α β 0 V v)
    (λ (n : nat) (sol : soln α β n),
        let lt_of_ne (s : finset B) (hs : card s < succ n) : card s ≠ n → card s < n :=
            have h1 : card s < n ∨ card s = n, from lt_succ_iff_lt_or_eq.mp hs,
            assume h2 : card s ≠ n, or.elim h1 id (λ h, absurd h h2) in
        let V (s : finset B) (hs : card s < succ n) : set α :=
            dite (card s = n)
                (λ (h : card s = n), find_domain α β n s h sol)
                (λ (h : card s ≠ n), sol.V s (lt_of_ne s hs h)) in
        let v (s : finset B) (hs : card s < succ n) : Π (y : α), y ∈ V s hs → β :=
            dite (card s = n)
                (λ (h : card s = n), solve_pde α β n s h sol (V s hs))
                (λ (h : card s ≠ n), sol.v s (lt_of_ne s hs h)) in
        @soln.mk α β (succ n) V v)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Sep 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134579994):
As you can probably tell by the names, I am attempting some applied mathematics :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134590793):
`V s hs` isn't equal to `sol.V s (lt_of_ne s hs h)` in general, only when you have the hypothesis `¬card s = n`, and even then it's not a definitional equality. You have to use `dif_neg` to simplify the `dite`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134590965):
I haven't looked carefully at what's going on here, but I wonder if there might be an easier way--it looks like you're constructing a "solution for all sets of size < n" by induction on n, where we just pass to the inductive hypothesis if the set is not of the new size--then why not just define a "solution for all sets of size = n", and then if you want to reproduce the type of `soln`, just provide `n = card s`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Sep 25 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592386):
Thanks! I have applied dif_neg but the final step eludes me...
```lean
let v (s : finset B) (hs : card s < succ n) : Π (y : α), y ∈ V s hs → β :=
    dite (card s = n)
        (λ (h : card s = n), solve_pde α β n s h sol (V s hs))
        (λ (h : card s ≠ n),
            have V s hs = sol.V s (lt_of_ne s hs h), from dif_neg h,
            sol.v s (lt_of_ne s hs h)) in
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Sep 25 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592520):
Your description of my intended algorithm is spot on. The reason I am trying to accumulate the Vs and vs in each successive soln is so that I can prove certain relations between them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592759):
Now there are two ways to proceed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592811):
The easier way is to change the last line to something like `by rw this; exact sol.v s (lt_of_ne s hs h)`, or the term-mode equivalent using `eq.rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Sep 25 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134593877):
Got it! Thank you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134594108):
The slightly more complicated way is to instead use the equality `this` to turn the hypothesis `y ∈ V s hs` into a proof of `y ∈ sol.V s _`--this will probably make things easier later if you want to prove things about the values of `v`, because the actual `β` value won't be wrapped inside a `rw`/`eq.rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250457):
Suppose I have the following:

```lean
namespace lambda

inductive exp : Type
| var : string → exp
| app : exp → exp → exp
| abs : string → exp → exp

inductive is_subterm : exp → exp → Prop
-- x ∈ Sub (x)
| var : ∀ (x : string), is_subterm (exp.var x) (exp.var x)

-- e1 ∈ Sub ((e1 e2))
| app_l : ∀ (e1 : exp) (e2 : exp), is_subterm e1 (exp.app e1 e2)

-- e2 ∈ Sub ((e1 e2))
| app_r : ∀ (e1 : exp) (e2 : exp), is_subterm e2 (exp.app e1 e2)

-- (e1 e2) ∈ Sub ((e1 e2))
| app_self : ∀ (e1 : exp) (e2 : exp), is_subterm (exp.app e1 e2) (exp.app e1 e2)

-- e ∈ Sub ((λ x . e))
| abs : ∀ (x : string) (e : exp), is_subterm e (exp.abs x e)

-- (λ x . e) ∈ Sub ((λ x . e))
| abs_self : ∀ (x : string) (e : exp), is_subterm (exp.abs x e) (exp.abs x e)
```

Is it possible to prove that is_subterm does not hold for something? For example, could one prove that if ```x``` is a lambda variable, then the only subterm of ```x``` is ```x``` itself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 03 2019 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250562):
Doesn't it contradict `is_subterm.abs`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250752):
Are you saying that the statement "if ```x``` is a lambda variable, then the only subterm of ```x``` is ```x``` itself", does not hold because of ```is_subterm.abs```? I'm not sure I see why that would be the case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 03 2019 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250754):
This is provable (hint: try the `cases` tactic):
```lean
example (y x) : is_subterm y (exp.var x) → y = exp.var x
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250765):
You may need to be a little careful about how you state it, but this is a good place to take advantage of the equation compiler. It will discharge the structurally impossible cases for you.
```lean
example (s : string) : ∀ (e : exp), is_subterm e (exp.var s) → e = exp.var s
| _ (is_subterm.var _) := rfl
```
(As Gabriel points out, `cases` will do the same thing.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 03 2019 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250796):
oh I missed "variable" in "lambda variable", it's on the next line here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154251107):
Thank you. I will have to do some reading on tactics and the equation compiler.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154251985):
I'm still learning how induction is handled in Lean. Does the inductive definition create theorems related to what is not an object of the defined type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154252289):
The only objects of the defined type are the ones that can be defined using the constructors. This is a "theorem" that's captured by the type's induction principle. In your case, look at `#check is_subterm.cases_on `.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154253410):
should we use `nat` instead of `string`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154254942):
Is the following what Gabriel means by the ```cases``` tactic?
```lean
example (e : exp) (x : string) : is_subterm e (exp.var x) → e = exp.var x :=
	exp.cases_on e
	(show ∀ (y : string), is_subterm (exp.var y) (exp.var x) → (exp.var y) = (exp.var x), from
	assume y : string,
```
I'm not sure how to proceed from here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154254968):
well by the `cases` tactic he means `by cases e`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154254973):
but I don't know if you're familiar with using tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154255034):
Oh. No, I'm not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 03 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154255194):
Actually I mean by cases on the `is_subterm` proof:
`begin intro h, cases h, end`  (you can easily solve the remaining goal)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154265785):
why bother making `is_subterm` inductive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154265902):
I thought it would have to be. What is the alternative?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154266764):
well it isn't inductive (i.e. recursive) so maybe just make it a def or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267466):
Hmm. I was trying to formalize the recursive definition of the set of all subterms of a lambda expression given by definition 1.3.5 here: https://play.google.com/books/reader?id=orsrBQAAQBAJ&hl=en_US&pg=GBS.PA5.w.4.0.36
Did I do this wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267703):
You're missing the recursive calls. The set of subterms of (M N) is the union of the subterms of M, the subterms of N, and the singleton set {(M N)}.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267747):
In your definition, (M N) only has three subterms: M, N, and (M N).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267858):
This is a perfectly good situation to use an inductive predicate, but the one you wrote isn't the one you wanted.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154269430):
Does adding the following fix it?
```lean
| app_l' : ∀ (e : exp) (e1 : exp) (e2 : exp), (is_subterm e e1) → is_subterm e (exp.app e1 e2)
| app_r' : ∀ (e : exp) (e1 : exp) (e2 : exp), (is_subterm e e2) → is_subterm e (exp.app e1 e2)
| abs' : ∀ (e : exp) (x : string) (e1 : exp), (is_subterm e e1) → is_subterm e (exp.abs x e1)
```
Also, is there a way to formalize this as a set, similar to the definition in the book?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 03 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154269672):
Sure, you can just write a recursive function:
```lean
def subterms : exp → multiset exp
| (exp.var x) := {exp.var x}
-- ...
```
I'm not sure why they use multisets instead of sets though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154269810):
You could add those, and you can also reduce some of the others into one case.
```lean
inductive is_subterm : exp → exp → Prop
| self : ∀ x, is_subterm x x
| app_l : ∀ e₁ e₂ x, is_subterm x e₁ → is_subterm x (exp.app e₁ e₂)
| app_r : ∀ e₁ e₂ x, is_subterm x e₂ → is_subterm x (exp.app e₁ e₂)
| abs : ∀ e s x, is_subterm x e → is_subterm x (exp.abs s e)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270313):
and rename `self` into `refl`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270442):
```lean
def is_subterm : exp → exp → bool
| e (exp.var s) := e = exp.var s
| e (exp.app e₁ e₂) := (e = exp.app e₁ e₂) || is_subterm e e₁ || is_subterm e e₂
| e (exp.abs s e') := (e = exp.abs s e') || is_subterm e e'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 03 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270505):
```lean
def is_subterm (e : exp) : exp → bool
| (exp.var s) := e = exp.var s
| (exp.app e₁ e₂) := (e = exp.app e₁ e₂) || is_subterm e₁ || is_subterm e₂
| (exp.abs s e') := (e = exp.abs s e') || is_subterm e'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Thomas (Jan 03 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270926):
@**Gabriel Ebner** Cool. Could something similar be done for the set of all lambda terms?

