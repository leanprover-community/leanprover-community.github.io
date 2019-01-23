---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/52075noobquestions.html
---

## Stream: [new members](index.html)
### Topic: [noob question(s)](52075noobquestions.html)

---


{% raw %}
#### [ Wojciech Nawrocki (Nov 20 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148007940):
What's the command to make Lean automatically derive `decidable_eq` for some custom inductive type?

#### [ Chris Hughes (Nov 20 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148007958):
@[derive decidable_eq]

#### [ Wojciech Nawrocki (Nov 20 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148007972):
ah I should've thought of that, thanks! :)

#### [ Wojciech Nawrocki (Nov 20 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148013728):
Hm, when I add
```lean
open classical
local attribute [instance] prop_decidable
```
to a file, definitions below it which used to pass now fail with:
```lean
equation compiler failed to generate bytecode for 'subst._main'
nested exception message:
code generation failed, VM does not have code for 'classical.choice'
```

Why might this be?

Is it basically because `classical` makes things uncomputable? If so, maybe Lean should detect that `classical` is not used in a particular case and still compile the definition?

#### [ Chris Hughes (Nov 20 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148013848):
Try `[instance, priority 0]`. Otherwise it uses classical decidability even when there's proper decidability.

#### [ Wojciech Nawrocki (Nov 20 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148013915):
Ah indeed, thanks Chris!

#### [ Kevin Buzzard (Nov 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148024166):
This trips lots of people up! I wonder where people are learning this trick? Not putting priority 0 can trip you up later in quite a confusing way

#### [ Patrick Massot (Nov 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148024213):
@**Jeremy Avigad**  needs to fix the very bottom of https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html

#### [ Johan Commelin (Nov 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148024215):
I think Lean shows an error message when it can't find an instance for `decidable`, and that error message does not include setting the priority. It would be very helpful if it did.

#### [ Patrick Massot (Nov 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148024219):
and https://leanprover.github.io/theorem_proving_in_lean/type_classes.html

#### [ Jeremy Avigad (Nov 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148044684):
I'm on it -- I'll do it tomorrow.

#### [ Patrick Massot (Nov 20 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148049459):
Thanks!

#### [ Kenny Lau (Nov 20 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148049511):
how about *not* using `classical.dec`

#### [ Reid Barton (Nov 20 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148049651):
Let's just agree to not not use it

#### [ Kenny Lau (Nov 20 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148049677):
that doesn't mean we *use* it :P

#### [ Patrick Massot (Nov 20 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148049697):
You may have missed Reid's point

#### [ Reid Barton (Nov 20 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148049698):
It doesn't mean *you* use it

#### [ Wojciech Nawrocki (Nov 20 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148074938):
Is it possible to make Lean display the values of constant variables in the tactic state? E.g. if i have `lst: list nat` which is also empty, it would be nice to see that it's empty.

#### [ Kenny Lau (Nov 21 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148075021):
either this doesn't make sense, or `subst lst`

#### [ Wojciech Nawrocki (Nov 21 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148075182):
Hm I should elaborate, maybe I'm misunderstanding how `induction` works. Say I have a hypothesis `h: InductiveFoo list.nil`, where `InductiveFoo: list nat -> Prop`. So then running `induction h` creates cases for all the constructors of `InductiveFoo`, which take the list as an input, say `lst`. But the `lst` is empty, so it'd be nice to see that in the state.

#### [ Kenny Lau (Nov 21 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148075295):
you can't because it's forgotten

#### [ Kenny Lau (Nov 21 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148075309):
you might want to `generalize_hyp`

#### [ Wojciech Nawrocki (Nov 21 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148075886):
Thanks!

#### [ Wojciech Nawrocki (Nov 21 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148115433):
Perhaps it would be useful to have a reference sheet for translating from Coq to Lean tactics?

#### [ Mario Carneiro (Nov 21 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148115539):
I recall such a thing being made at one point. Maybe it's in mathlib docs?

#### [ Rob Lewis (Nov 21 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148115560):
https://github.com/jldodds/coq-lean-cheatsheet

#### [ Rob Lewis (Nov 21 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148115566):
Note the date though, it'll need updating.

#### [ Wojciech Nawrocki (Nov 21 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148115644):
Oh, nice!

#### [ Wojciech Nawrocki (Nov 21 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148119720):
Is there a general tactic for showing `false` by "this term could not have been constructed"? E.g.
```lean
inductive Foo: Prop → Prop → Prop
| FooT: Foo true true
| FooF: Foo false false

-- This term could not have been constructed
lemma impossible (h: Foo true false)
  : false := by sorry
```

#### [ Mario Carneiro (Nov 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148120085):
`cases`

#### [ Mario Carneiro (Nov 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148120091):
also empty match

#### [ Mario Carneiro (Nov 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148120098):
```
lemma impossible : Foo true false → false.
```

#### [ Rob Lewis (Nov 21 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148120175):
You have to make `Foo : bool -> bool -> Prop` for that.

#### [ Wojciech Nawrocki (Nov 21 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148120216):
Yeah, for `Prop -> Prop -> Prop` both of these fail, but that wasn't actually my problem, so thanks!

#### [ Patrick Massot (Nov 21 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148120406):
It seems that variations on this topic comes up again and again. We should really find a way to document that

#### [ Wojciech Nawrocki (Nov 21 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148134832):
That would be nice :) I was also surprised to see that more often than not `contradiction` fails when `cases h` works. Description: `The contradiction tactic attempts to find in the current local context an hypothesis that is equivalent to an empty inductive type (e.g. false)`. I thought a hypothesis that cannot be constructed is exactly that, but maybe I'm misunderstanding it?

#### [ Wojciech Nawrocki (Nov 22 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148147233):
Is it possible to reserve some notation for an inductive type and then use it while defining the type, like in Coq? I tried this,  but the parser seems to fail:
```lean
reserve infix `∋`:50

inductive Typeof: list Tp → Tp → Prop
| Z: ∀ (Γ: list Tp) A, Typeof (Γ.append [A]) A
| S_: ∀ (Γ: list Tp) A B, Typeof Γ A → Typeof (Γ.append [B]) A

inductive Typeof: list Tp → Tp → Prop
| Z: ∀ (Γ: list Tp) A, (Γ.append [A]) ∋ A -- fails
| S_: ∀ (Γ: list Tp) A B, Γ ∋ A → (Γ.append [B]) ∋ A

infix ∋ := Typeof
```

#### [ Mario Carneiro (Nov 22 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148150619):
Yes! You can just put a notation line between the inductive header and the first constructor
```lean
inductive Typeof{Tp}: list Tp → Tp → Prop
infix `∋`:50 := Typeof
| Z: ∀ (Γ: list Tp) A, (Γ.append [A]) ∋ A
| S_: ∀ (Γ: list Tp) A B, Γ ∋ A → (Γ.append [B]) ∋ A
```

#### [ Jeremy Avigad (Nov 23 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148238627):
@**Patrick Massot** I added a discussion of the `priority 0` trick to Section 10.4 of TPIL (search on "priority 0"):
https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#decidable-propositions
I also added a back reference in Section 11:
https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#the-law-of-the-excluded-middle

Finally, I fixed an old issue raised by @**Joseph Corneli** by changing all the examples in 6.4:
https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#attributes
https://github.com/leanprover/theorem_proving_in_lean/issues/62

Teaching my class next semester will give me a chance to review and expand TPIL. I am planning to add one more chapter on some of the fine points of dependent type theory, e.g. explaining how to work with equality and dependent types (the dark side of type theory), and explaining how Lean manages recursion on arbitrary well-founded relations. I'll also try to write a less ambitious but up-to-date version of Programming in Lean. But I am counting on the mathlib crew to continue documenting mathlib and all the new tactics, and to provide useful guidance on using the library and proving theorems.

#### [ Kevin Buzzard (Nov 23 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148238846):
I have not been using Lean seriously since term started; there are three weeks to go before it finishes. After that I fully intend to go back to the perfectoid project. But when I don't understand something, my instinct is to write docs about it, because if I work something out and don't write down what I learnt then I realise a month later that I've forgotten it all again!

#### [ Patrick Massot (Nov 23 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148247373):
Thank you very much Jeremy! Your documentation work is really crucial.

#### [ Patrick Massot (Nov 23 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148249579):
I'm now reading random pieces of TPIL, and I have a couple more suggestions about chapter 10:
* at several places, emacs is mentioned but not VScode. I guess this goes back to before the VScode extension was available, but it could be misleading
* in 10.5. Managing Type Class Inference, I think it would be nice to add the standard tricks to see what's the name of an instance Lean is finding, and sometimes what's the actual definition, as in
```lean
#check (by apply_instance : has_add ℕ) 
#reduce (infer_instance : has_add ℕ)
```
maybe find a better example for the second one since the answer is not super easy to read (every nice example coming to my mind are in mathlib...)

#### [ Patrick Massot (Nov 23 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148249664):
Oh, it seems `apply_instance` is never mentioned in TPIL :sad:

#### [ Patrick Massot (Nov 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148249726):
Another thing that would be very helpful, both because it can be puzzling and because it can be very helpful would be to discuss
```lean
def n : Type := ℕ

example : has_add ℕ := by apply_instance  -- ok
example : has_add n := by apply_instance  -- fails
example : has_add n := by unfold n ; apply_instance  -- ok
```

#### [ Jeremy Avigad (Nov 24 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/148277429):
Thanks for the input. Yes, TPIL evolved over time, and the last major rewrite was early in the days of Lean 3, before there was a VSCode extension. I'll do a global search and try to make the text less emacs-centric.

I'll discuss `apply_instance` and `infer_instance`. I am thinking of using these examples:
```lean
/- example 1: using apply_instance -/

def foo : has_add nat := by apply_instance
def bar : inhabited (nat → nat) := by apply_instance

/- example 2: using infer_instance -/

def baz : has_add nat := infer_instance
def bla : inhabited (nat → nat) := infer_instance

/- example 3: seeing them -/

#print foo    -- nat.has_add
#reduce foo   -- (unreadable)

#print bar    -- pi.inhabited ℕ
#reduce bar   -- {default := λ (a : ℕ), 0}

#print baz    -- infer_instance
#reduce baz   -- (same as for #reduce foo)

#print bla    -- infer_instance
#reduce bla   -- {default := λ (a : ℕ), 0}

/- example 4: tricks to be more concise -/

#check (by apply_instance : inhabited ℕ)
#print nat.inhabited

#reduce (infer_instance : inhabited ℕ)

/- examples 5: core Lean can't find an instance for inhabited set -/

-- fails
-- example {α : Type*} : inhabited (set α) := by apply_instance

/- example 6: supplying one manually -/

def inhabited.set (α : Type*) : inhabited (set α) := ⟨∅⟩
#print inhabited.set     -- λ {α : Type u}, {default := ∅}
#reduce inhabited.set ℕ  -- {default := λ (a : ℕ), false}

/- example 7: unfolding a definition so Lean can find it -/

def inhabited.set (α : Type*) : inhabited (set α) :=
by unfold set; apply_instance
#print inhabited.set     -- λ (α : Type u), eq.mpr _ (pi.inhabited α)
#reduce inhabited.set ℕ  -- {default := λ (a : ℕ), true}

/- example 8: using dunfold instead -/

def inhabited.set (α : Type*) : inhabited (set α) :=
by dunfold set; apply_instance
#print inhabited.set     -- λ (α : Type u), id (pi.inhabited α)
#reduce inhabited.set ℕ  -- {default := λ (a : ℕ), true}
```

#### [ Patrick Massot (Dec 11 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151432316):
```quote
Yes! You can just put a notation line between the inductive header and the first constructor
```lean
inductive Typeof{Tp}: list Tp → Tp → Prop
infix `∋`:50 := Typeof
| Z: ∀ (Γ: list Tp) A, (Γ.append [A]) ∋ A
| S_: ∀ (Γ: list Tp) A B, Γ ∋ A → (Γ.append [B]) ∋ A
```
```
 Is there something similar for dependant `structure`? If one field of my structure is a binary operator, can I define an infix notation usable in the remaining fields declaration?

#### [ Kevin Buzzard (Dec 11 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151432380):
I usually make the `structure` extend the notation typeclass in this situation.

#### [ Kevin Buzzard (Dec 11 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151432403):
In fact I have been known to make new notation typeclasses called things like `group_notation` extending `has_mul`, `has_one` and `has_inv`, and then extending these too so I get a bunch of notation at once.

#### [ Patrick Massot (Dec 11 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151432470):
Thanks Kevin. I know all this, but I'm still interested in an answer to my question.

#### [ Kevin Buzzard (Dec 11 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151432479):
Yes I understand. For example if the notation is not in the standard notation list then it would be nicer to add it directly in the definition of the structure.

#### [ Rob Lewis (Dec 11 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151440921):
You can define notation in structures that's used in the remaining fields. But I think it's just local to the structure declaration.
```lean
structure patrick :=
(α : Type)
(f : α → α → α)
(infix `^^^`:50 := f)
(h : ∀ a : α, a ^^^ a = a)

#check patrick.h
```

#### [ Patrick Massot (Dec 11 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/151445285):
Thanks!

#### [ Jeremy Avigad (Jan 03 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154258172):
I just crossed this item off my to do list. `apply_inference` and such are now discussed here: https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#managing-type-class-inference. And VS Code is now mentioned whenever Emacs is, with VS Code first.

#### [ Patrick Massot (Jan 03 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154258563):
> If you add this to your file in Emacs mode and use C-c C-x to run an independent Lean process on your file, the output buffer will show a trace every time the type class resolution procedure is subsequently triggered.

This paragraph (in the section your referred to) is still Emacs centric

#### [ Jeremy Avigad (Jan 03 2019 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154260198):
Yes, that is the only one, because I don't know how to start an independent Lean process from within VS Code. I guess I'll remind people that they can run Lean from the VS Code terminal.

#### [ Patrick Massot (Jan 03 2019 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154260213):
Why would you do that?

#### [ Patrick Massot (Jan 03 2019 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154260222):
The trace is printed in the info view

#### [ Jeremy Avigad (Jan 03 2019 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154260439):
Oh! I forgot. Good point. I'll fix that.

#### [ Patrick Massot (Jan 03 2019 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154260510):
Great!

#### [ Jeremy Avigad (Jan 03 2019 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/154261167):
Fixed. Thanks for catching it.
https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#managing-type-class-inference

#### [ Wojciech Nawrocki (Jan 16 2019 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155250652):
Hello! Is there anything special I need to do to make Lean recognise my `instance : has_zero Foo` as being equivalent to `0`? I got this state while trying to use `rw [this]`:
```lean
rewrite tactic failed, did not find instance of the pattern in the target expression
  0 + π₂
state:
3 goals
π₂ : mult,
this : 0 + π₂ = π₂
⊢ mult.Zero + π₂ = π₂ + mult.Zero
```
even though I have
```lean
instance : has_zero mult :=
  ⟨mult.Zero⟩
```
above

#### [ Kevin Buzzard (Jan 16 2019 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155250968):
rewrites don't recognise definitional equality, only syntactic equality.

#### [ Kevin Buzzard (Jan 16 2019 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155250980):
So you could try "show 0 + pi2 = _" before the rewrite

#### [ Kevin Buzzard (Jan 16 2019 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251052):
or "change mult.Zero + _ = _ at this". Maybe it will work after one of these changes. But not after both ;-)

#### [ Reid Barton (Jan 16 2019 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251072):
`convert this` should also work

#### [ Kevin Buzzard (Jan 16 2019 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251096):
but `this` isn't the goal

#### [ Kevin Buzzard (Jan 16 2019 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251103):
Oh!

#### [ Kevin Buzzard (Jan 16 2019 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251182):
This `convert` trick works when the thing you're rewriting is precisely one side of the equality I guess.

#### [ Reid Barton (Jan 16 2019 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251188):
or `erw this` would also work but it's not as nice

#### [ Reid Barton (Jan 16 2019 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155251370):
In fact you can use `a' = b'` to prove `a = b` with neither side matching definitionally (you'll get two new goals `a = a'` and `b = b'`), but then you run the risk that the new goals are not actually true :smile:

#### [ Wojciech Nawrocki (Jan 16 2019 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155252212):
Ah, I see, thanks! And related, I'm proving that an object with three elements and custom add/mult tables is a semiring, how ugly is it to do all my proofs like this?
```lean
  lemma add_assoc (π₁ π₂ π₃: mult)
    : π₁ + π₂ + π₃ = π₁ + (π₂ + π₃) := by { cases π₁; cases π₂; cases π₃; refl }
```

#### [ Mario Carneiro (Jan 16 2019 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155252434):
it will work, although there are simpler proofs where you ony case on one of them, I think

#### [ Wojciech Nawrocki (Jan 16 2019 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155252646):
Hm, I found that without expanding every case, I had to do a bit more work by using other lemmas and so on. The definition of `add` is:
```lean
inductive mult: Type
| Zero: mult
| One: mult
| Omega: mult

instance : has_zero mult :=
  ⟨mult.Zero⟩

instance : has_one mult :=
  ⟨mult.One⟩

notation `ω` := mult.Omega

def add: mult → mult → mult
| 0 π := π
| π 0 := π
| 1 1 := ω
| ω _ := ω
| _ ω := ω

instance : has_add mult :=
  ⟨add⟩
```

#### [ Mario Carneiro (Jan 16 2019 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155252763):
right

#### [ Mario Carneiro (Jan 16 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155252890):
you should have lemmas like `x + ω = ω` as simp lemmas which should simplify most of the cases

#### [ Mario Carneiro (Jan 16 2019 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155252915):
or you could just split into 27 cases if you want

#### [ Wojciech Nawrocki (Jan 16 2019 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155253007):
Ah ok, i'll try it with simp as well, thanks!

#### [ Johan Commelin (Jan 16 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155254705):
Scott Morrison's case-bashing tactic would probably be useful here. But I don't know where that tactic lives at the moment...

#### [ Mario Carneiro (Jan 16 2019 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155255138):
if you want to do a case bashing proof, another approach is to prove `fintype mult` and `decidable_eq mult` (you can `derive` this), and then you can just revert everything and use `dec_trivial`

#### [ Johan Commelin (Jan 16 2019 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155255210):
Should even be reasonably fast, I guess.

#### [ Mario Carneiro (Jan 16 2019 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155255232):
as long as you don't have too many variables; it is still 27 cases

#### [ Kevin Buzzard (Jan 16 2019 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155256347):
Kind of a stupid question, but when I'm using other computer algebra systems I would expect checking a million cases to be very quick. Mario's comments suggest that 27 is rather large for Lean. What is happening here?

#### [ Mario Carneiro (Jan 16 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155257947):
There is a large overhead of the expression that is generated, elaboration for it, and typechecking

#### [ Mario Carneiro (Jan 16 2019 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258030):
I don't think 27 is that large in this context, I guess it's probably less than a second to check

#### [ Mario Carneiro (Jan 16 2019 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258059):
I just think it's better to have more "human" proofs with fewer cases

#### [ Kevin Buzzard (Jan 16 2019 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258070):
This is what I don't understand. We have to check that 27 things of the form add a (add b c) = add (add a b) c hold and in each case this is by refl.

#### [ Kevin Buzzard (Jan 16 2019 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258119):
How long does it take Lean to prove (0 + 1) + 1 = 0 + (1 + 1) in this type?

#### [ Mario Carneiro (Jan 16 2019 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258201):
there is also all the intermediate steps, the generation of motives, lots of abstraction and substitution going on, and large terms being built up behind the scenes before you even attack those 27 cases

#### [ Kevin Buzzard (Jan 16 2019 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258224):
So the bottleneck is elsewhere?

#### [ Mario Carneiro (Jan 16 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258252):
I have heard it repeatedly asserted that the kernel is not a bottleneck

#### [ Kevin Buzzard (Jan 16 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258265):
Again the idea of a "large" term is confusing to me. In python I could happily manipulate a list with 1000 elements.

#### [ Mario Carneiro (Jan 16 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258275):
this term has way more than 1000 subterms

#### [ Kevin Buzzard (Jan 16 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258304):
One of my kids has been learning about algorithms over the last few months and I realise now that I am far more aware of these things than I used to be.

#### [ Mario Carneiro (Jan 16 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258379):
all in all it makes lean just look a lot slower to do "simple" things

#### [ Mario Carneiro (Jan 16 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258393):
because there is a lot of bookkeeping in the background

#### [ Mario Carneiro (Jan 16 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155258552):
I would like to figure out ways to minimize the overhead, but that runs close to work on the lean compiler

#### [ Kevin Buzzard (Jan 16 2019 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155261902):
```quote
this term has way more than 1000 subterms
```
 In the same way that a set with 10 elements has more than 1000 subsets, or in a more serious "we really need to work with way more than 1000 things" way?

#### [ Mario Carneiro (Jan 16 2019 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155263745):
in the more serious way. (It's tricky to count the "size" of an expression but number of subterms is a good proxy)

#### [ Mario Carneiro (Jan 16 2019 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/155263817):
there is no exponential growth because subterms can't overlap, they are either disjoint or in a containment relationship

#### [ Wojciech Nawrocki (Jan 18 2019 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156331129):
Is it possible to define a custom synthesis strategy for an implicit argument? I would like to define a function which extracts concrete values from concrete lists, like so:
```lean
def get': ∀ (l: list ℕ) (n: ℕ) {h: n < l.length}, ℕ
| (x::xs) 0 _ := x
| (x::xs) (n+1) h := @get' xs n (nat.lt_of_succ_lt_succ h)
| [] n h := by { exfalso, simp at h, exact (nat.not_lt_zero n)
```
and for concrete args, `h` is always derivable with a custom tactic. I'd like Lean to use that tactic to synthesise it.
OR am I doing this completely wrong and there is a much simpler way?

#### [ Chris Hughes (Jan 18 2019 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156331279):
unification hints! I don't know much about them though.

#### [ Mario Carneiro (Jan 18 2019 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156334847):
This function is `list.nth_le` btw

#### [ Mario Carneiro (Jan 18 2019 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156334971):
you can synthesize the argument using typeclasses, but `exact_dec_trivial` is another easy way to do it

#### [ Mario Carneiro (Jan 18 2019 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156335048):
```lean
def get' (l : list ℕ) (n : ℕ) (h : n < l.length . exact_dec_trivial) : ℕ := l.nth_le n h

example : get' [1, 2, 3] 1 = 2 := rfl
```

#### [ Wojciech Nawrocki (Jan 18 2019 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156335623):
Ah indeed, thanks Mario! Can I use something like this in a Pi-type (to make the equation compiler work)? The `foo . tactic` syntax doesn't seem to work:
```lean
def debrujin_of_nat: Π {Γ: Env} (n: ℕ) (h: n < Γ.length . tactic.exact_dec_trivial), (Γ ∋ Γ.nth_le n h) -- ill-formed declaration
```

#### [ Mario Carneiro (Jan 18 2019 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156335911):
If you can put it left of the colon, the dot notation should work. But if you can't write it that way, it's sugar for `auto_param`:
```lean
def get' : Π (l : list ℕ) (n : ℕ), auto_param (n < l.length) ``exact_dec_trivial → ℕ := list.nth_le

example : get' [1, 2, 3] 1 = 2 := rfl
```

#### [ Wojciech Nawrocki (Jan 18 2019 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336087):
Can I have a _named_ `auto_param` :sweat_smile:? I need to use the hypothesis in the type signature itself, more specifically in the return type.

#### [ Mario Carneiro (Jan 18 2019 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336185):
sure, just use a pi instead of an arrow

#### [ Mario Carneiro (Jan 18 2019 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336193):
`auto_param T n` is defeq to `T` so it doesn't cause any problems

#### [ Wojciech Nawrocki (Jan 18 2019 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336460):
Oh, I was sure I'd tried that but apparently not, thanks! Doesn't seem to work under `#eval` unfortunately:
```lean
don't know how to synthesize placeholder
context:
⊢ auto_param (0 < list.length [Tp.Nat]) (name.mk_string "exact_dec_trivial" (name.mk_string "tactic" name.anonymous))
```

#### [ Mario Carneiro (Jan 18 2019 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336541):
what did you write?

#### [ Mario Carneiro (Jan 18 2019 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336637):
it's not really related to the context you write it in, but rather the expected type during elaboration

#### [ Wojciech Nawrocki (Jan 18 2019 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336845):
Apologies for the length, but this is the full context:
```lean
import tactic.find
import tactic.interactive
import tactic
import tactic.auto_cases
import tactic.tidy

@[derive decidable_eq]
inductive Tp
| Nat: Tp
| Bool: Tp
| Fn: Tp → Tp → Tp

local infixr ` ⇒ `:50 := Tp.Fn

def Env := list Tp

inductive TypeIn: Env → Tp → Type
infix ` ∋ `:40 := TypeIn
| ZVar: Π {Γ T}, T::Γ ∋ T
| SVar: Π {Γ T U}, Γ ∋ T → U::Γ ∋ T

local infix ` ∋ `:40 := TypeIn

open TypeIn

inductive Term: Env → Tp → Type
| Nat (n: ℕ): Π {Γ}, Term Γ Tp.Nat -- in all environments, nat literals have type Nat
| Bool (b: bool): Π {Γ}, Term Γ Tp.Bool -- and booleans have type Bool
| Var: Π {Γ T}, Γ ∋ T → Term Γ T -- A variable has type T given its de Brujin index
                                 -- is in the environment.
| Abs: Π {Γ T U}, Term (T::Γ) U → Term Γ (T ⇒ U)
| App: Π {Γ T U}, Term Γ (T ⇒ U) → Term Γ T → Term Γ U

open Term

def debrujin_of_nat: Π {Γ: Env} (n: ℕ) {h: auto_param (n < Γ.length) ``tactic.exact_dec_trivial}, (Γ ∋ Γ.nth_le n h)
| (T::Γ) 0 _ := ZVar
| (T::Γ) (n+1) h := SVar (@debrujin_of_nat Γ n (nat.lt_of_succ_lt_succ h))
| [] n h := by { exfalso, simp at h, exact (nat.not_lt_zero n) h }

local notation `#` n := Var (debrujin_of_nat n)

#eval (@App [] Tp.Nat Tp.Nat (@Abs [] Tp.Nat Tp.Nat (@Var [Tp.Nat] Tp.Nat (debrujin_of_nat 0))) (@Nat 3 []))
```

#### [ Wojciech Nawrocki (Jan 18 2019 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156336955):
Basically given a concrete `list Tp` and a concrete `n`, I'd like it to figure out that `n` is within bounds and include the result of `lst.nth_le n _` in the return type.

#### [ Wojciech Nawrocki (Jan 18 2019 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156337127):
This does work: `#eval (@App [] Tp.Nat Tp.Nat (@Abs [] Tp.Nat Tp.Nat (@Var [Tp.Nat] Tp.Nat (@debrujin_of_nat [Tp.Nat] 0 (by tactic.exact_dec_trivial)))) (@Nat 3 []))` (notice the explicit proof I put in)

#### [ Mario Carneiro (Jan 18 2019 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156338055):
so what did you write?

#### [ Wojciech Nawrocki (Jan 18 2019 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156338116):
Well, the `#eval` at the bottom of that long snippet is what fails synthesis. The `#eval` with an explicit proof works

#### [ Mario Carneiro (Jan 18 2019 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156338117):
aha, you made the arg implicit

#### [ Mario Carneiro (Jan 18 2019 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156338118):
auto params should be explicit

#### [ Mario Carneiro (Jan 18 2019 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156338120):
```
def debrujin_of_nat: Π {Γ: Env} (n: ℕ) (h: auto_param (n < Γ.length) ``tactic.exact_dec_trivial), (Γ ∋ Γ.nth_le n h)
```

#### [ Wojciech Nawrocki (Jan 18 2019 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156338198):
Oh thanks, now it does work, but still behaves as if it were implicit :thinking: is this currying at work, meaning I have to place `auto_param` last, s.t. given `foo: nat -> auto_param blah -> nat`, `(foo n): nat` (and `foo n _` still fails)?

#### [ Wojciech Nawrocki (Jan 19 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156408748):
(unrelated to above)
I'm seeing a wierd error in an inductive type: `invalid occurrence of recursive arg#3 of 'context.cons', the body of the functional type depends on it.`. The type definition is below, and as far as I know it's a perfectly legit defn, so what's wrong?
```lean
inductive context: list ℕ → Type
| nil: context []
| cons {ns: list ℕ} (_: context ns) (n: ℕ) (m: ℕ): context (n::ns)
```
EDIT: swapping two arguments makes it compile, but why?
```lean
inductive context: list ℕ → Type
| nil: context []
| cons: Π {ns: list ℕ} (n: ℕ) (_: context ns) (m: ℕ), context (n::ns)
```

#### [ Mario Carneiro (Jan 19 2019 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156409198):
I think Gabriel recently pointed out an example similar to this. You have a dependent pi (`n`) after a recursive arg (`_ : context ns`) and lean doesn't like this

#### [ Wojciech Nawrocki (Jan 19 2019 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156411833):
Ah ok, maybe this could be fixed in Lean 4? :)

#### [ Wojciech Nawrocki (Jan 19 2019 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156414862):
Do I need to do something special to make the semiring-ness of my custom type available to the `ring` tactic? I have a state like this:
```lean
π π' : mult,
π_1 : mult,
⊢ π * π' * π_1 = π * (π' * π_1)
```
which is provable by `exact mult.monoid.mul_assoc π π' π_1`, but `ring` fails. I have `instance : semiring mult` shown a few lines above.

#### [ Mario Carneiro (Jan 19 2019 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156415302):
you need to prove `comm_semiring mult`

#### [ Wojciech Nawrocki (Jan 21 2019 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554174):
Given `def add (a b: foo): foo := blah`, what's the difference between `infix ` ++ ` := add` and `instance : has_add foo := ⟨add⟩`? If i switch from the former to the latter and replace `++` with `+`, my proofs break at the simplification stage, namely addition seems to not be `unfold`able anymore

#### [ Kevin Buzzard (Jan 21 2019 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554210):
They're very different in the sense that they're using different machinery to figure out what's going on.

#### [ Kevin Buzzard (Jan 21 2019 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554280):
I guess the `infix` trick is just syntax sugar, whereas the `instance` approach is using type class inference. Can you give an example of something which breaks?

#### [ Kevin Buzzard (Jan 21 2019 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554315):
I guess if you go via the instance approach then you have an extra layer of unfolding to do. `+` is `has_add.add`, which unfolds to your add.

#### [ Kevin Buzzard (Jan 21 2019 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554337):
Maybe that's the answer to your question. If you're trying to unfold things explicitly in the middle of a proof, maybe you have to insert some `unfold has_add.add`'s

#### [ Kevin Buzzard (Jan 21 2019 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554416):
`++` unfolds directly to your `add`, whereas `+` unfolds to `has_add.add` which unfolds to your add.

#### [ Kevin Buzzard (Jan 21 2019 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554455):
[NB I'm a bit of a CS noob, I don't know if "unfolds" is the right terminology for notation turning into its underlying definition]

#### [ Kevin Buzzard (Jan 21 2019 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156554512):
[they might well be syntactically equal rather than just definitionally equal]

#### [ Wojciech Nawrocki (Jan 21 2019 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156556743):
Ah indeed, `unfold`ing twice does make it work - thanks!

#### [ Wojciech Nawrocki (Jan 22 2019 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156571293):
Does there exist a general tactic for proving `f a0 .. an = f b0 .. bn` from `a0 = b0 .. an = bn`?

#### [ Mario Carneiro (Jan 22 2019 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156571984):
`congr`

#### [ Wojciech Nawrocki (Jan 22 2019 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156572109):
Hm, I tried `congr` but it seems to iterate the congruence, which gives me unprovable goals. Namely, I have a goal `f (g x) = f (g y)` and `congr` gives me `x = y` but I just want `g x = g y`. EDIT: `congr' 1` works, thx!

#### [ Mario Carneiro (Jan 22 2019 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156574364):
use `congr' 1` and increase the number until you get a good result

#### [ Wojciech Nawrocki (Jan 22 2019 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156647038):
The issue of `has_add.add` and its actual value not being definitionally equal makes a lot of my proofs quite ugly - I have to expand definitions first so that the expressions can simplify and then fold them back into the `has_add.add` version (or `has_mul.mul`, etc), because all the ring/module/whatever laws only work on those. For example:
```lean
  { /-
    case context.cons
    δ γ γ₁ : precontext,
    π₁ : mult,
    T₁ : tp,
    Γ₁ : context γ₁,
    ih₁ : ∀ {Γ₂ : context γ₁} {Ξ : matrix γ₁ δ}, vmul (Γ₁ + Γ₂) Ξ = vmul Γ₁ Ξ + vmul Γ₂ Ξ,
    Γ₂ : context (T₁ :: γ₁),
    Ξ : matrix (T₁ :: γ₁) δ
    ⊢ vmul (cons π₁ T₁ Γ₁ + Γ₂) Ξ = vmul (cons π₁ T₁ Γ₁) Ξ + vmul Γ₂ Ξ
    -/
    cases Γ₂ with _ π₂ _ Γ₂,
    -- unfold
    unfold vmul has_add.add context.add has_scalar.smul context.smul at *,
    simp *,
    -- fold back
    let a := vmul Γ₁ (λ (U : tp) (x : γ₁ ∋ U), Ξ U (SVar x)),
    let b := vmul Γ₂ (λ (U : tp) (x : γ₁ ∋ U), Ξ U (SVar x)),
    change
      (π₁ + π₂) • (Ξ T₁ ZVar) + (a + b)
      =
      (π₁•(Ξ T₁ ZVar) + a) + (π₂•(Ξ T₁ ZVar) + b),
    -- simplify using monoid laws
    simp [context.add_smul, context.add_assoc] },
```
is there some tactic or such that I could apply to do this automatically?

#### [ Mario Carneiro (Jan 22 2019 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156647545):
This is what simp lemmas are for

#### [ Mario Carneiro (Jan 22 2019 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156647677):
If you define `add x (y :: z) := y :: add x z`, for example, and then install `add` as a `has_add` instance, then you can prove `x + (y :: z) = y :: (x + z)` by rfl, and you should state this as a simp lemma

#### [ Mario Carneiro (Jan 22 2019 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156647754):
You should not ever have to unfold `has_add.add`

#### [ Wojciech Nawrocki (Jan 22 2019 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156647865):
Hm okay, so basically I need to "lift" the behaviour of my functions from the custom definition to one using `has_op.op`? I'll try

#### [ Wojciech Nawrocki (Jan 23 2019 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156648686):
Is it fine to unfold `has_zero.zero` though? My definition of `0` for this type is
```lean
def zeros: Π γ, context γ
| [] := nil
| (T::δ) := cons 0 T (zeros δ)
```
and I need the `cons` to prove `0+Γ=Γ`

#### [ Wojciech Nawrocki (Jan 23 2019 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156649254):
In any case this is pretty awesome, all my proofs have shortened by half now without the unfolding, thanks a lot!

#### [ Mario Carneiro (Jan 23 2019 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%28s%29/near/156653719):
For this, you should decide whether you prefer to write the empty context as `0` or `[]`, and write a simp lemma like `0 = []` if you want to get rid of the 0 everywhere. In this case you should also make sure that all your other simp lemmas use the "preferred form" of this element on the LHS


{% endraw %}
