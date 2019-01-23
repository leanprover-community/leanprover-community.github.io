---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51017notationstointroduceproofs.html
---

## Stream: [general](index.html)
### Topic: [notations to introduce proofs](51017notationstointroduceproofs.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 15 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815299):
In the following snippet,
```lean
lemma foo : (0 : ℕ) = 0 :=
begin
  have : (0 : ℕ) = 0        := by simp,
  have B:= calc (0 : ℕ) = 0 : by simp,
  show (0 : ℕ) = 0          , by simp
end
```
you can see that a proof after `have` is introduced by `:=`, after `calc` by `:` and after `show` by `,`. And they can essentially not be used one for the other (the only allowed change is to use `,` instead of `:=` on the first line). I am plainly used to it, but I would like to understand the rationale behind it. Is it to ease parsing? Or just for historical reasons? Would it make sense to use, say, `:=` everywhere, to avoid confusing newcomers for no reason?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815435):
Certainly `calc` would make sense with `:=`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815449):
the commas in `show` and `have` are likely due to influence from Isar

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815458):
Of course you should be looking at term proofs not tactic proofs, which are at best an approximation of the term equivalents

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815503):
I'm not sure what notation Isar uses for `let`. Do you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 15 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815645):
There are no commas in Isar. The formula to be proved is enclosed in quotes, and then you give the proof. Either it is a direct proof, and then you just write something like `using foo by auto`. Or it is a complex proof, and it is enclosed in `proof ... qed`. The `let` equivalent is called `define`, and used like `define foo where "foo = 0"`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815713):
interesting. That's more different than I expected. Has it changed significantly in the past 10 years?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815726):
the base Isar syntax, I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815737):
Maybe it is Mizar influence then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 15 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815838):
The `define`syntax is a recent change, it used to be `def "foo  = 0"`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815881):
I was under the impression that the original term mode syntax of lean was basically lifted directly from the syntax of another language, probably Isar

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815886):
and it has since been simplified a bit but is otherwise unchanged

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815898):
like I think `and have` and `hence` used to exist and don't anymore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 15 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815958):
Since formulas to be proved are enclosed in quotes in Isar, you don't a separator as in Lean. The comma makes sense, as would `:=`, but having two or three different separators depending on the context might be misleading to newcomers. Will it be uniformized in Lean 4, or is the syntax expected not to change?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816033):
I think syntax changes like that are on the table

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816039):
I would be in support of using more `:=`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 15 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816055):
I agree.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816057):
and drop the `from`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816116):
i.e. `have A := proof in B` or `have A := by tac in B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816119):
`show A := proof`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816182):
`calc A = B := proof ... = C := proof`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816239):
although I guess `have in` has the problem that it won't look like the tactic version which is `have A := proof, tac`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816298):
I would prefer to get rid of the `in` in `let` and just write `let a := x, ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 15 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816310):
I don't mind the `from` so much, it makes things read slightly more naturally. Although I'm sure I wouldn't miss it for long if it disappeared. I get more annoyed with the difference between term and tactic `have`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816311):
and `have h : A, by tac, ...` or `have h : A := ..., ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816388):
I think that `have h : A := by tac, ...` is more uniform. Putting a comma in there doesn't seem to win much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816389):
it would also be nice to have parameters for `have` and `show`:
`have h (a : A) (b : B) : T := ..., ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816412):
short story: `let` and `have` should have the same parser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 15 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816422):
```quote
and `have h : A, by tac, ...` or `have h : A := ..., ...`
```
So you would still use `,` to introduce a proof, and to separate a statement from the next. I think I would favor `:=` to introduce proofs, and `,` to go to the next statement (removing `in`, as you say).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816434):
the comma would be just short form for tactic proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816502):
right, but I don't think that needs to be a thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816509):
like `have h : A := by tac, ...` and `have h : A := begin end, ...` are plenty short

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816534):
hm, yes its short enough. and nicely uniform

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816538):
what about `have h : A := { ... },`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816542):
preposterous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816584):
I guess it classes with set syntax

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816602):
Then we would still have inconsistency with the goal focussing {...}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816617):
just think of `begin end` as goal focussing brackets that work outside tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816618):
another dream: not only unify `let` and `have` but unify it also with `def`, i.e. allow to use the equation compiler in proofs, ala
```lean
have h : a \/ b -> c
| or.inl a := ...
| or.inr b := ...,
...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816700):
`mutual have ... with ... `?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816754):
yeah this makes a lot more sense than named `match`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Oct 15 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135819726):
Is there a general notation wishlist thread?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135851934):
there is now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Oct 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135852289):
I would really like all of the bells and whistles you get with `{!...!}` to work with `_` when it fails to fill in the proof. But I guess that's more of an editor feature.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 17 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135960094):
Lean 4 will most likely replace the hole syntax with `_`. Input to hole commands should be handled by the editor (which would've been basically impossible in Lean 3's infrastructure).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 04 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/150872739):
```quote
Is there a general notation wishlist thread?
```
 Another notation wish: as for `rw` I would like `simp [←foo]` to add reversed `foo` to the simpset. And possibly to remove `foo` if it is in the simpset. Currently, if `foo` has say two variables, I achieve this with `simp[-foo, (foo _ _).symm]`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 23 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152435172):
New notation wishlist item: be able to replace, say in a parameter list, `(n : { n : ℕ // 0 < n })` by `(n : ℕ // 0 < n)` (or, even better,  `(n : ℕ | 0 < n)`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 23 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152444089):
is there a reason you aren't uskng two arguments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152445176):
Also `(n > 0)` already does almost exactly what you are saying

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 24 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465051):
It's not exactly the same. I can indeed modify my example to:
```lean
def euclid : Π (m : ℕ) (n > 0), {p : ℕ × ℕ // m = n*p.1 + p.2 ∧ p.2 < n}
| m n := λ n_pos,
         if h : m < n then
           ⟨(0, m), by simp *⟩
         else
           have m - n < m, by apply nat.sub_lt ; linarith,
           let ⟨⟨q, r⟩, ⟨H, H'⟩⟩ := euclid (m-n) n n_pos in
             ⟨(q+1, r),
              ⟨begin
                rw nat.sub_eq_iff_eq_add (le_of_not_lt h) at H,
                simp [H], ring,
               end, H'⟩⟩
```
but I still think the notation `(n : nat | n > 0)` in a parameter list would be good to have (and they have it in Coq).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 24 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465176):
By the way, the context is given by https://www.college-de-france.fr/site/xavier-leroy/seminar-2018-12-12-11h30.htm which shows programming with recursion and dependent pattern matching in Coq. They have all sorts of cool tricks in this area, including deferring proof obligations after writing the program, you can have a look at minute 51 to see their version of the above function. And of course they also have `(q, r) : ℕ × ℕ` instead of our `p : ℕ × ℕ`, and a linear arithmetic tactic doing everything :sad:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465235):
You can defer proof obligations using `refine`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465353):
Isn't this just the definition of `div`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465356):
you can have a look at how it's defined in core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465432):
You can also write something with explicit binding for `q,r` but we try not to use it because it doesn't unfold as much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465552):
you can do something like this (the notation isn't there, but you get the idea)
```lean
def euclid (m : ℕ) (n > 0) : @subtype (ℕ × ℕ) (λ ⟨q, r⟩, m = n*q + r ∧ r < n) := sorry
```
Unfortunately I think lean has a bug with generating names for the auxiliary match and it clashes with the `let` statement in the body

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152483363):
```quote
You can defer proof obligations using `refine`
```
 It only defers a tiny bit. You need to close the goal before leaving the tactic block. DId you look at what `Program` does in this video? (you only have to look at the time I mentioned).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152483383):
```quote
you can have a look at how it's defined in core
```
 In core the output type does not assert correction. I'm not saying it should, I was doing an exercise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152483401):
```quote
you can do something like this (the notation isn't there, but you get the idea)
```lean
def euclid (m : ℕ) (n > 0) : @subtype (ℕ × ℕ) (λ ⟨q, r⟩, m = n*q + r ∧ r < n) := sorry
```
Unfortunately I think lean has a bug with generating names for the auxiliary match and it clashes with the `let` statement in the body
```
 Can you use well founded recursion if m and n are left of colon?

