---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28785explodecommand.html
---

## [general](index.html)
### [explode command](28785explodecommand.html)

#### [Mario Carneiro (Aug 31 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133093714):
While on the flight home, I decided to actually write the wishlist tactic I've mentioned to a few people, which displays lean proofs in a line by line style heavily annotated with type ascriptions so it looks more like a Fitch style proof. I'm still tweaking the display options, but here's what it looks like right now:
```lean
import tactic.explode
section end
#explode iff_true
```
```
iff_true : ∀ (a : Prop), a ↔ true ↔ a
0│   │ a              ├ Prop
1│   │ h              │ ┌ a ↔ true
2│   │ trivial        │ │ true
3│1,2│ iff.mpr        │ │ a
4│3  │ ∀I             │ (a ↔ true) → a
5│   │ iff_true_intro │ a → (a ↔ true)
6│4,5│ iff.intro      │ a ↔ true ↔ a
```

#### [Johan Commelin (Aug 31 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103016):
Ok, I can parse this, and it looks really helpful... but why is line `0` at the top, instead of the bottom?

#### [Mario Carneiro (Aug 31 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103024):
it's numbered like lines of proof

#### [Johan Commelin (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103025):
It seems to me that `0` follows from `6`, but maybe I misunderstand `0`

#### [Johan Commelin (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103034):
Also, I'd rather read them upside down.

#### [Mario Carneiro (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103036):
lambdas are introduced with the intro variable on top of the bracket

#### [Johan Commelin (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103037):
First split the goal, then you get two subtrees... etc..

#### [Mario Carneiro (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103078):
Yes, I usually read metamath proofs bottom up as well

#### [Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103081):
Aaah, that is what `0` is doing, of course!

#### [Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103084):
Well... there is a solution to that: have `#explode` reverse the order...

#### [Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103085):
But now I see that `0` should remain at the top.

#### [Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103087):
So it's not that easy...

#### [Mario Carneiro (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103088):
I suppose, but that will get confusing to explain to people

#### [Mario Carneiro (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103099):
I would prefer a forward proof ordering on the page

#### [Mario Carneiro (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103103):
even if your interest is drawn from the bottom up

#### [Johan Commelin (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103114):
How far is this representation from writing a `begin end` proof?

#### [Johan Commelin (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103115):
Could you generate that as well?

#### [Mario Carneiro (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103152):
what do you mean?

#### [Mario Carneiro (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103157):
like you want the lines to correspond to `apply` and `intro`?

#### [Johan Commelin (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103162):
Right.

#### [Johan Commelin (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103166):
`#deobfuscate`

#### [Mario Carneiro (Aug 31 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103181):
it's pretty close, there are some edge cases where you see explicit `∀E` and `∀I` steps

#### [Johan Commelin (Aug 31 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103233):
Even if it isn't perfect, I'dd really like it.

#### [Mario Carneiro (Aug 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103257):
can you mockup?

#### [Johan Commelin (Aug 31 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103303):
What do you mean? This example? Or more general?

#### [Mario Carneiro (Aug 31 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103369):
either, something that shows off what you would like to see

#### [Johan Commelin (Aug 31 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103381):
Rob has this interface with mathematica... with certain terms corresponding to certain mathematica terms

#### [Johan Commelin (Aug 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103392):
So we could also have a dictionary `\lam <-> intros` etc...

#### [Johan Commelin (Aug 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103394):
But I don't have a clear picture how to actually implement this

#### [Mario Carneiro (Aug 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103440):
oh, there is a potential problem with making a real runnable proof script, as opposed to just a display like this... it has to parse as valid lean, and sometimes `pp` doesn't give good results

#### [Mario Carneiro (Aug 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103451):
I am currently hiding non proof terms in `#explode`, but probably this won't work in a proof script

#### [Johan Commelin (Aug 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103511):
```
iff_true : ∀ (a : Prop), a ↔ true ↔ a
0│   │ a              ├ Prop            | intro (intros?)
1│   │ h              │ ┌ a ↔ true      | intro (intros?)
2│   │ trivial        │ │ true          | exact trivial
3│1,2│ iff.mpr        │ │ a             | apply iff.mpr
4│3  │ ∀I             │ (a ↔ true) → a  | ???
5│   │ iff_true_intro │ a → (a ↔ true)  | exact iff_true_intro
6│4,5│ iff.intro      │ a ↔ true ↔ a    | apply iff.intro (split?)
```

#### [Johan Commelin (Aug 31 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103558):
I just added an extra column, and it totally wouldn't run.

#### [Mario Carneiro (Aug 31 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103567):
I guess part of the problem with line for line translating this display into a proof script is that forward proving is less natural

#### [Mario Carneiro (Aug 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103572):
you have to use lots of `have`

#### [Johan Commelin (Aug 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103577):
Right

#### [Mario Carneiro (Aug 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103584):
and the positioning of the `intro` is weird

#### [Mario Carneiro (Aug 31 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103676):
The hard stuff is when dealing with `eq.rec` though
```
iff_not_comm : ∀ {a b : Prop} [_inst_1 : decidable a] [_inst_2 : decidable b], a ↔ ¬b ↔ (b ↔ ¬a)
0 │     │ a            ├ Prop
1 │     │ b            ├ Prop
2 │     │ _inst_1      ├ decidable a
3 │     │ _inst_2      ├ decidable b
4 │     │ eq.refl      │ (a ↔ ¬b ↔ (b ↔ ¬a)) = (a ↔ ¬b ↔ (b ↔ ¬a))
5 │     │ iff_def      │ a ↔ ¬b ↔ (a → ¬b) ∧ (¬b → a)
6 │5    │ propext      │ (a ↔ ¬b) = ((a → ¬b) ∧ (¬b → a))
7 │4,6  │ eq.rec       │ (a ↔ ¬b ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a))
8 │7    │ id           │ (a ↔ ¬b ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a))
9 │     │ eq.refl      │ ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a))
10│     │ iff_def      │ b ↔ ¬a ↔ (b → ¬a) ∧ (¬a → b)
11│10   │ propext      │ (b ↔ ¬a) = ((b → ¬a) ∧ (¬a → b))
12│9,11 │ eq.rec       │ ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b → ¬a) ∧ (¬a → b))
13│12   │ id           │ ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b → ¬a) ∧ (¬a → b))
14│     │ imp_not_comm │ a → ¬b ↔ b → ¬a
15│     │ not_imp_comm │ ¬b → a ↔ ¬a → b
16│14,15│ and_congr    │ (a → ¬b) ∧ (¬b → a) ↔ (b → ¬a) ∧ (¬a → b)
17│13,16│ eq.mpr       │ (a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)
18│8,17 │ eq.mpr       │ a ↔ ¬b ↔ (b ↔ ¬a)
```

#### [Reid Barton (Aug 31 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133105985):
You should make a version which outputs those judgment tree things and outputs LaTeX

#### [Patrick Massot (Aug 31 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133108796):
Noooo! We triggered Mario's immune defenses. He spent three days with people who want Lean to prove everything by itself, he merged tidy and then, flying back, he wrote the Lean2metamath tactic!

#### [Kevin Buzzard (Aug 31 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133121291):
"On the flight home, I wrote an explode command" = "I just risked getting the plane diverted because the guy next to me panicked"

#### [Mario Carneiro (Aug 31 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133121314):
I originally called it `mmshow` but I decided against metamath branding it

