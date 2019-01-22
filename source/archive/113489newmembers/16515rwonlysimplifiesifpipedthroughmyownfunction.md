---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/16515rwonlysimplifiesifpipedthroughmyownfunction.html
---

## [new members](index.html)
### [rw only simplifies if piped through my own function](16515rwonlysimplifiesifpipedthroughmyownfunction.html)

#### [Tobias Grosser (Sep 07 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491472):
My first beginners question. I tampered with this since a while, but maybe somebody has a quick explanation for this:

https://gist.github.com/tobig/92b17c8cac76fd07e1537c9131a25260

#### [Tobias Grosser (Sep 07 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491484):
Rewriting with my own theorem works well, but if I directly use imp_iff_not_or things break

#### [Tobias Grosser (Sep 07 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491491):
with "function expected at"

#### [Tobias Grosser (Sep 07 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491541):
Probably a beginners mistake. It seems my declaration introduces some additional information which help the proof go through.

#### [Simon Hudon (Sep 07 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491641):
If you check the definition of `imp_iff_not_or`, (type `#check imp_iff_not_or` in your Lean buffer), you see that it does not take *explicit* arguments, only implicit ones

#### [Simon Hudon (Sep 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491663):
That means that they are meant to be inferred. But if you want to specify then, you can write `@imp_iff_not_or` and then you have to provide an argument for the implicit and explicit arguments.

#### [Simon Hudon (Sep 07 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491725):
For reference:

```lean
#check imp_iff_not_or
-- imp_iff_not_or : ?M_1 → ?M_2 ↔ ¬?M_1 ∨ ?M_2
#check @imp_iff_not_or
-- imp_iff_not_or : ∀ {a b : Prop} [_inst_1 : decidable a], a → b ↔ ¬a ∨ b
```

The curly brackets around `a` and `b` means that they are implicit arguments. The square brackets around `decidable a` means that it's a type class instance.

#### [Tobias Grosser (Sep 07 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491802):
https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments

#### [Tobias Grosser (Sep 07 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491841):
Works flawless. Need to read a little bit more on this.

#### [Tobias Grosser (Sep 07 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491845):
Thanks for the quick help.

#### [Simon Hudon (Sep 07 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491851):
No worries :)

#### [Tobias Grosser (Sep 07 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491931):
One last question:

#### [Tobias Grosser (Sep 07 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491932):
My proof looks now like this:

#### [Tobias Grosser (Sep 07 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491934):
            ((B → C) → (¬(A → C)     ∧ ¬(A ∨ B)))
          = ((B → C) → (¬(¬A ∨ C)    ∧ ¬(A ∨ B)))         : by rw @imp_iff_not_or A C
      ... = ((B → C) → ((¬(¬A) ∧ ¬C) ∧ ¬(A ∨ B)))         : by rw not_or_distrib
      ... = ((B → C) → ((¬(¬A) ∧ ¬C) ∧ (¬A ∧ ¬B)))        : by rw not_or_distrib
      ... = ((B → C) → ((A ∧ ¬C) ∧ (¬A ∧ ¬B)))            : by rw not_not
      ... = ((B → C) → ((A ∧ ¬C) ∧ ¬A ∧ ¬B))              : by rw and_assoc
      ... = ((B → C) → ((¬C ∧ A) ∧ ¬A ∧ ¬B))              : by rw and_comm (A) (¬C)
      ... = ((B → C) → (¬C ∧ A ∧ ¬A ∧ ¬B))                : by rw and_assoc
      ... = ((B → C) → (¬C ∧ (A ∧ ¬A) ∧ ¬B))              : by rw and_assoc
      ... = ((B → C) → (¬C ∧ ¬ B ∧ (A ∧ ¬A)))             : by rw and_comm (¬ B) (A ∧ ¬A)
      ... = ((B → C) → (¬C ∧ ¬ B ∧ false ))               : by rw and_not_self_iff A
      ... = ((B → C) → ((¬C) ∧ false ))                   : by rw and_false
      ... = ((B → C) → (false))                           : by rw and_false
      ... = (¬(B → C) ∨ false)                            : by rw imp_iff_not_or
      ... = ¬(B → C)                                      : by rw or_false
      ... = ¬(¬B ∨ C)                                     : by rw imp_iff_not_or 
      ... = ((¬¬B) ∧ (¬C))                                : by rw not_or_distrib
      ... = (B ∧ ¬C)                                      : by rw not_not

#### [Tobias Grosser (Sep 07 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491975):
It seems only imp_iff_not_or needs the '@'. All other functions are OK with explicit arguments (if given).

#### [Tobias Grosser (Sep 07 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491980):
Is there some schema when theorems take explicit arguments in mathlib?

#### [Mario Carneiro (Sep 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491999):
most iff theorems have implicit args

#### [Kenny Lau (Sep 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492001):
`rw ← imp_iff_not_or`

#### [Kenny Lau (Sep 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492009):
```lean
import logic.basic

local attribute [instance] classical.prop_decidable

example {A B C : Prop} : _ = _ :=
calc
        ((B → C) → (¬(A → C)     ∧ ¬(A ∨ B)))
      = ((B → C) → (¬(¬A ∨ C)    ∧ ¬(A ∨ B)))         : by rw ← imp_iff_not_or
  ... = ((B → C) → ((¬(¬A) ∧ ¬C) ∧ ¬(A ∨ B)))         : by rw not_or_distrib
  ... = ((B → C) → ((¬(¬A) ∧ ¬C) ∧ (¬A ∧ ¬B)))        : by rw not_or_distrib
  ... = ((B → C) → ((A ∧ ¬C) ∧ (¬A ∧ ¬B)))            : by rw not_not
  ... = ((B → C) → ((A ∧ ¬C) ∧ ¬A ∧ ¬B))              : by rw and_assoc
  ... = ((B → C) → ((¬C ∧ A) ∧ ¬A ∧ ¬B))              : by rw and_comm (A) (¬C)
  ... = ((B → C) → (¬C ∧ A ∧ ¬A ∧ ¬B))                : by rw and_assoc
  ... = ((B → C) → (¬C ∧ (A ∧ ¬A) ∧ ¬B))              : by rw and_assoc
  ... = ((B → C) → (¬C ∧ ¬ B ∧ (A ∧ ¬A)))             : by rw and_comm (¬ B) (A ∧ ¬A)
  ... = ((B → C) → (¬C ∧ ¬ B ∧ false ))               : by rw and_not_self_iff A
  ... = ((B → C) → ((¬C) ∧ false ))                   : by rw and_false
  ... = ((B → C) → (false))                           : by rw and_false
  ... = (¬(B → C) ∨ false)                            : by rw imp_iff_not_or
  ... = ¬(B → C)                                      : by rw or_false
  ... = ¬(¬B ∨ C)                                     : by rw imp_iff_not_or 
  ... = ((¬¬B) ∧ (¬C))                                : by rw not_or_distrib
  ... = (B ∧ ¬C)                                      : by rw not_not
```

#### [Tobias Grosser (Sep 07 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492210):
Is there a specific reason why 'iff' terms have implict  arguments and others not?

#### [Kenny Lau (Sep 07 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492230):
```lean
import logic.basic

local attribute [instance] classical.prop_decidable

example {A B C : Prop} : _ = _ :=
calc
        ((B → C) → (¬(A → C) ∧ ¬(A ∨ B)))
      = ((B → C) → ((A ∧ ¬C) ∧ ¬(A ∨ B)))  : by rw not_imp
  ... = ((B → C) → ((A ∧ ¬C) ∧ ¬A ∧ ¬B))   : by rw not_or_distrib
  ... = ((B → C) → ((¬C ∧ A) ∧ ¬A ∧ ¬B))   : by rw and_comm (A) (¬C)
  ... = ((B → C) → (¬C ∧ A ∧ ¬A ∧ ¬B))     : by rw and_assoc
  ... = ((B → C) → (¬C ∧ (A ∧ ¬A) ∧ ¬B))   : by rw and_assoc
  ... = ((B → C) → (¬C ∧ ¬ B ∧ (A ∧ ¬A)))  : by rw and_comm (¬ B) (A ∧ ¬A)
  ... = ((B → C) → (¬C ∧ ¬ B ∧ false ))    : by rw and_not_self_iff A
  ... = ((B → C) → ((¬C) ∧ false ))        : by rw and_false
  ... = ((B → C) → (false))                : by rw and_false
  ... = ¬(B → C)                           : rfl
  ... = (B ∧ ¬C)                           : by rw not_imp
```

#### [Tobias Grosser (Sep 07 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492326):
Nice

#### [Tobias Grosser (Sep 07 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492329):
Really helpful.

#### [Tobias Grosser (Sep 07 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492344):
Thank you!

#### [Kenny Lau (Sep 07 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492346):
```lean
import logic.basic

local attribute [instance] classical.prop_decidable

example {A B C : Prop} : _ = _ :=
calc
        ((B → C) → (¬(A → C) ∧ ¬(A ∨ B)))
      = ((B → C) → ((A ∧ ¬C) ∧ ¬(A ∨ B)))  : by rw not_imp
  ... = ((B → C) → ((A ∧ ¬C) ∧ ¬A ∧ ¬B))   : by rw not_or_distrib
  ... = ((B → C) → ((A ∧ ¬A ∧ ¬B) ∧ ¬C))   : by rw and.right_comm
  ... = ((B → C) → (((A ∧ ¬A) ∧ ¬B) ∧ ¬C)) : by rw ← and_assoc
  ... = ((B → C) → ((false ∧ ¬B) ∧ ¬C))    : by rw and_not_self_iff A
  ... = ((B → C) → (false ∧ ¬C))           : by rw false_and
  ... = ((B → C) → (false))                : by rw false_and
  ... = ¬(B → C)                           : rfl
  ... = (B ∧ ¬C)                           : by rw not_imp
```

#### [Simon Hudon (Sep 07 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492460):
I'm a bit vague on the rule for `iff` and other rewrite rules but in general, if an argument can be inferred from other arguments, it should be implicit. For rewrite rules, I think all the arguments that can be inferred from the lhs of the equation should be implicit.

#### [Tobias Grosser (Sep 07 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492546):
I see. Thanks @**Simon Hudon**

#### [Mario Carneiro (Sep 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492706):
```
example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=
by apply classical.cases_on A;
   apply classical.cases_on B;
   apply classical.cases_on C; simp
```
The idea behind the rule for iff is that these are more often used as combined unidirectional rules, and in this case any argument present on both lhs and rhs are inferrable

#### [Simon Hudon (Sep 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492713):
Have you tried `tauto`?

#### [Mario Carneiro (Sep 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492719):
doesn't seem to do anything

#### [Mario Carneiro (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492758):
`propext $ by tauto` works though

#### [Simon Hudon (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492768):
Right! You need the propositions to be decidable

#### [Kenny Lau (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492774):
```quote
example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=
by apply classical.cases_on A;
   apply classical.cases_on B;
   apply classical.cases_on C; simp
```
that's the proof of completeness!

#### [Simon Hudon (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492780):
```quote
`propext $ by tauto` works though
```
Interesting! That should be worth adding to the tactic

#### [Mario Carneiro (Sep 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492790):
mathlib tries to avoid equality of propositions though

#### [Mario Carneiro (Sep 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492794):
it's always stated as an iff

#### [Kenny Lau (Sep 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492795):
```lean
example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=
by by_cases A; by_cases B; by_cases C; simp*
```

#### [Mario Carneiro (Sep 07 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492839):
oh, of course - `simp` will rewrite `A` to `true` or `false` given the `by_cases` assumption

#### [Tobias Grosser (Sep 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493165):
Nice. I am currently translating some student exercises, so I try to use the 'calc' mode to really show step-by-step how things evolve.

#### [Tobias Grosser (Sep 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493168):
This worked quite well so far. Nice to see that the tactics work so well too.

#### [Mario Carneiro (Sep 07 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493180):
you should be able to use `<->` in those calc blocks

#### [Tobias Grosser (Sep 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493249):
Yes, I can replace = with <->

#### [Tobias Grosser (Sep 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493250):
Does this have any benefits?

#### [Mario Carneiro (Sep 07 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493323):
only it's more idiomatic; `rw` and friends will work either way

#### [Tobias Grosser (Sep 07 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493366):
Why exactly is it more idiomatic?

#### [Mario Carneiro (Sep 07 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493378):
because it's easier to work with iff since you can destruct it, and you don't need the propext axiom to prove things about it

#### [Simon Hudon (Sep 07 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493381):
`=` has stronger precedence than `<->` and the other connectives so `<->` yields formulas with fewer brackets

#### [Tobias Grosser (Sep 07 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493395):
Great.

#### [Tobias Grosser (Sep 07 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493439):
Need to get back to normal life. Thanks for your help.

#### [Mario Carneiro (Sep 07 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493443):
But "idiomatic" really just means that it is used, like a convention - it doesn't need a reason per se, it's valuable because it is the convention

#### [Mario Carneiro (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493454):
i.e. it will make it easier to fit with and apply existing theorems

#### [Tobias Grosser (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493465):
I understand the meaning of idiomatic.

#### [Tobias Grosser (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493475):
Wanted understand the underlying motivation.

#### [Mario Carneiro (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493477):
so another answer is "there are two options, we picked one"

#### [Tobias Grosser (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493517):
If I want my proofs to be understood in the end, it helps to learn the choices you as a community have taken.

#### [Mario Carneiro (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493522):
I think logic textbooks usually use <->

#### [Mario Carneiro (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493526):
or sometimes ≡

#### [Tobias Grosser (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493527):
I can learn them easier if I can get an intuition where things come from.

#### [Keeley Hoek (Sep 11 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133708725):
Cool fact: `rewrite_search` solves this problem instantly:
````
local attribute [search] imp_iff_not_or not_or_distrib not_not and_assoc and_comm and_not_self_iff and_false not_not

example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=
  by rewrite_search_using [`search]
````

#### [Scott Morrison (Sep 11 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712079):
We really need to think about automatic lemma selection for rewrite_search.

#### [Scott Morrison (Sep 11 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712089):
Possible just finer attribute tagging (e.g. [search logic], [search list], [search category_theory]).

#### [Scott Morrison (Sep 11 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712100):
Perhaps even teach rewrite_search to automatically select from different bundles of lemmas depending on what it sees in the goal.

#### [Keeley Hoek (Sep 11 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712505):
At least for me, just printing out every definition in a modest real-ish maths environment takes 30 seconds, so I think some form of bundling will have to be the way to go. Maybe barring some emergency "show me the way" mode.

#### [Keeley Hoek (Sep 11 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712553):
Though "find me a lemma" mode could be a useful tactic in its own right I suppose

#### [Keeley Hoek (Sep 11 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712665):
I guess that's what I'll try next

#### [Patrick Massot (Sep 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133714529):
```quote
We really need to think about automatic lemma selection for rewrite_search.
```
This is all very nice, but don't forget that this is a whole research area. So don't expect this to be super easy, and maybe have a look at what already exists. I think the keyword is "relevance filter"

