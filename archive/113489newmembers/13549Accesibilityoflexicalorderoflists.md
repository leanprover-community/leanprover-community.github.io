---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13549Accesibilityoflexicalorderoflists.html
---

## Stream: [new members](index.html)
### Topic: [Accesibility of lexical order of lists](13549Accesibilityoflexicalorderoflists.html)

---

#### [AHan (Nov 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148644364):
I've seen there are proofs for accessibility and well-founded for lexical order of product
And I also find out there is a definition for lexical order of list, but I can't find any proofs for it's accessibility and well-founded...
Are them provided in other names or just not yet proved?

And if I were going to prove the accessibility of lexical order of list, I'm not quite sure what the type of the lemma should be, and when to use functions like acc.rec_on, acc.intro....
( Is the type of the lemma like... this ?)
```lean
variables {α : Type*} (ra  : α → α → Prop)
def list_lex_acc : (ha : ∀ a : α, acc ra a) : ∀ a : list α, acc (list.lex ra) a := sorry
```

#### [Kevin Buzzard (Nov 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148646910):
Nice question! If you write ` ```lean ` when quoting code then you get syntax highlighting as well. Here's a version of your question which typechecks straight out the box:

```lean
import data.list.basic

variables {α : Type*} (ra : α → α → Prop)
theorem list_lex_acc (ha : ∀ a : α, acc ra a) :
∀ a : list α, acc (list.lex ra) a := sorry
```

#### [Kevin Buzzard (Nov 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647290):
Off the top of my head, I guess some useful lemmas would be to prove that there are no solutions to `x < []`, and then you could start proving that all lists of positive size were accessible by induction on first the length of the list, and secondly using well-founded induction on the first element of the list.

#### [AHan (Nov 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647442):
Thanks for the suggestion!
And are there any differences between using `def` and  `theorem` here ?
Because in mathlib they used `def` for well_founded and accessibility of lexical order of product

#### [AHan (Nov 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647627):
"well-founded induction" do you mean something like `well_founded.rec_on`?

#### [Reid Barton (Nov 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647639):
I think you mean in the Lean core library (`def lex_wf (ha : well_founded ra) (hb : well_founded rb) : well_founded (lex ra rb) := ...`)?

#### [Reid Barton (Nov 27 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647724):
There is a difference. I don't know why they used `def`, though

#### [Kevin Buzzard (Nov 27 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647756):
I just used theorem because the thing you want to prove has type Prop.

#### [AHan (Nov 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647839):
@**Reid Barton**  Yes!

#### [Kevin Buzzard (Nov 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648088):
```lean
lemma not_lt_empty (ra : α → α → Prop) (a : list α) :
¬ (list.lex ra a []) := by intro H; cases H
```
There will be shorter proofs :-) I'm doing induction on `list.lex` here.

#### [Kevin Buzzard (Nov 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648210):
got it:

```lean
lemma not_lt_empty (ra : α → α → Prop) (a : list α) :
¬ (list.lex ra a []) .
```

#### [Kevin Buzzard (Nov 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648277):
oh no wait, lean segfaulted :D

#### [AHan (Nov 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648310):
I can solve this case by
```lean
theorem list_lex_acc (ha : ∀ a : α, acc ra a) : ∀ a : list α, acc (list.lex ra) a := 
λ a, 
begin
    cases a, 
    apply acc.intro, intros, cases a,
...
end
```
but I'm stuck at the second part, doing well-founded induction on the first element of the list...

#### [Kevin Buzzard (Nov 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648514):
Yeah it's messy now. I am at work and need to think about other things :-/

This `.` proof works for me.

```lean
import data.list.basic

variables {α : Type*} (ra : α → α → Prop)

lemma not_lt_empty (ra : α → α → Prop) (a : list α) :
¬ (list.lex ra a []) .
```

#### [AHan (Nov 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648760):
Wow.... what's `.` proof ...

#### [Kevin Buzzard (Nov 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648767):
But this exact file gives me a segfault:

```lean
import data.list.basic

variables {α : Type*} (ra : α → α → Prop)
theorem list_lex_acc (ha : ∀ a : α, acc ra a) :
∀ a : list α, acc (list.lex ra) a := sorry

lemma not_lt_empty (ra : α → α → Prop) (a : list α) :
¬ (list.lex ra a []) .

```

with `Lean (version 3.4.1, commit 17fe3decaf8a, Release)`.

#### [Kevin Buzzard (Nov 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648809):
The `.` proof says "Check all the cases...actually, can't you see that there are no cases to check?". The equation compiler looks at all the constructors for `list.lex` and rules out `[]` appearing on the right hand side.

#### [Reid Barton (Nov 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648818):
Doesn't segfault for me with the same version of lean

#### [Kevin Buzzard (Nov 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648875):
I have a blank line 9

#### [Kevin Buzzard (Nov 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648906):
I can restart Lean and consistently get it to segfault. On linux.

#### [AHan (Nov 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148649005):
No segfault with the same version of lean either... (on windows

#### [Kevin Buzzard (Nov 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148649143):
I restarted VS Code and the problem has gone away *shrug*

#### [AHan (Nov 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148649741):
Oh I crashed on
```lean
import data.list.basic
variables {α : Type*} (ra  : α → α → Prop)

theorem list_lex_acc (ha : ∀ a : α, acc ra a) : ∀ a : list α, acc (list.lex ra) a := sorry

lemma not_lt_empty (ra : α → α → Prop) (a : list α) : ¬ (list.lex ra a []) .
```
but it works fine if I swap the lemma and the theorem...
```lean
import data.list.basic
variables {α : Type*} (ra  : α → α → Prop)

lemma not_lt_empty (ra : α → α → Prop) (a : list α) : ¬ (list.lex ra a []) .

theorem list_lex_acc (ha : ∀ a : α, acc ra a) : ∀ a : list α, acc (list.lex ra) a := sorry
```

#### [Kevin Buzzard (Nov 27 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148662338):
Hmm. I think I found an infinite decreasing sequence! `[1] > [0,1] > [0,0,1] > [0,0,0,1] > ...`. So that will be why it's not in the library.

#### [Mario Carneiro (Nov 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148664949):
Interesting. I think it's well founded if you reverse the order: `[] < x :: xs`, and `x :: xs < y :: ys` if `xs < ys` or `xs = ys` and `x < y`

#### [Kenny Lau (Nov 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148664978):
I don't recall having a "list" operation on ordinals...

#### [Kenny Lau (Nov 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665001):
it would be `list(x) = 1 + x + x^2 + x^3 + ...`

#### [Mario Carneiro (Nov 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665002):
I do: `CNF` (although I don't see the relevance)

#### [Kenny Lau (Nov 27 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665062):
but then it would be `list(x) = x^omega` but power in ordinal doesn't correspond to power in cardinal

#### [Mario Carneiro (Nov 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665114):
right, I think the list ordering I gave has order type `(type A)^omega`

#### [Kenny Lau (Nov 27 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665175):
so it wouldn't be correct

#### [Kenny Lau (Nov 27 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665189):
because there is no `x^cardinal.omega` in ordinals

#### [Mario Carneiro (Nov 27 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665327):
what are you talking about?

#### [Mario Carneiro (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665346):
`x^omega` is perfectly well defined

#### [Mario Carneiro (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665354):
it's an ordinal power

#### [Kenny Lau (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665377):
but is it in bijection with `x^cardinal.omega`?

#### [Mario Carneiro (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665384):
no... it's lists not infinite sequences

#### [Kenny Lau (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665391):
ah

#### [Kenny Lau (Nov 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665447):
```quote
Interesting. I think it's well founded if you reverse the order: `[] < x :: xs`, and `x :: xs < y :: ys` if `xs < ys` or `xs = ys` and `x < y`
```
 feels like hilbert basis theorem now

#### [AHan (Nov 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148693519):
So maybe we'll need a different definition for the lexical order of list in order to prove it's well-founded?

#### [AHan (Nov 29 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148780207):
I ‘ve modified the lex of list as below
```lean
import data.list.basic
import data.set.lattice
open lattice

variables {α : Type*} (ra  : α → α → Prop)

inductive lex (r : α → α → Prop) : list α → list α → Prop
| nil {} {a l} : lex [] (a :: l)
| rel {a₁ a₂} (l₁ l₂ : list α) (h₁ : r a₁ a₂) (h₂ : l₁.length ≤ l₂.length) : lex (a₁ :: l₁) (a₂ :: l₂)
| cons {a l₁ l₂} (h : lex l₁ l₂) : lex (a :: l₁) (a :: l₂)

lemma lex_acc_of_lex : ∀ a b : list α, lex ra a b → acc (lex ra) a
| _ [] h := by cases h
| [] _ h := by apply list_nil_acc
| (a :: l₁) (b :: l₂) h :=  sorry
```
But I don't know how to tell lean that the recursion application will decrease....

#### [Kenny Lau (Nov 29 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148782527):
prove it? lol

