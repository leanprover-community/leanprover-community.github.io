---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44183heqquestion.html
---

## Stream: [general](index.html)
### Topic: [heq question](44183heqquestion.html)

---

#### [Kevin Buzzard (May 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126840954):
I wanted to get affine scheme = scheme finished today, but I have run into a problem whereby restricting to an open subset is not quite the same as restricting to the same not-defeq version of trhe open subset

#### [Kevin Buzzard (May 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126840994):
Here's a fairly minimised question

#### [Kevin Buzzard (May 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126840999):
```lean
import data.set
section oh_heq
parameters (α : Type) (U V W : set α)

lemma HU1 : U ∩ V ∩ W ⊆ U := set.subset.trans (set.inter_subset_left _ _) (set.inter_subset_left _ _)
lemma HV1 : U ∩ V ∩ W ⊆ V := set.subset.trans (set.inter_subset_left _ _) (set.inter_subset_right _ _)
lemma HW1 : U ∩ V ∩ W ⊆ W := set.inter_subset_right _ _
lemma HU2 : U ∩ (V ∩ W) ⊆ U := set.inter_subset_left _ _
lemma HV2 : U ∩ (V ∩ W) ⊆ V := set.subset.trans (set.inter_subset_right _ _) (set.inter_subset_left _ _)
lemma HW2 : U ∩ (V ∩ W) ⊆ W := set.subset.trans (set.inter_subset_right _ _) (set.inter_subset_right _ _)

example (F : set α → Type) [∀ Z : set α, group (F Z)]
(Fres : ∀ X Y : set α, X ⊆ Y → F Y → F X)
(i : F U) (j : F V) (k : F W) : 
Fres (U ∩ V ∩ W) U HU1 i * Fres (U ∩ V ∩ W) V HV1 j * Fres (U ∩ V ∩ W) W HW1 k 
== Fres (U ∩ (V ∩ W)) U HU2 i * Fres (U ∩ (V ∩ W)) V HV2 j * Fres (U ∩ (V ∩ W)) W HW2 k
:= sorry

end oh_heq 

```

#### [Kevin Buzzard (May 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841002):
Is that example true?

#### [Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841010):
What's going on is that I am constructing an element of F(U cap V cap W)

#### [Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841012):
and I'm constructing "the same" element of F(U cap (V cap W))

#### [Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841014):
and I want them to be equal

#### [Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841015):
or hequal

#### [Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841061):
I feel like I ran into this sort of problem once before

#### [Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841062):
and I tried some of the suggestions there

#### [Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841064):
(before minimising)

#### [Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841070):
`congr` turns the goal into 29 goals, not all of which are true

#### [Kevin Buzzard (May 20 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841079):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent.20congr_arg.3F

#### [Kevin Buzzard (May 20 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841081):
was the old thread

#### [Kevin Buzzard (May 20 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841123):
simp fails to simplify

#### [Kevin Buzzard (May 20 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841131):
cc fails

#### [Kevin Buzzard (May 20 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841142):
hmm maybe I should tell simp that the two intersections are equal

#### [Kevin Buzzard (May 20 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841143):
```lean
 begin
have Hinter : U ∩ V ∩ W = U ∩ (V ∩ W) := by cc,
simp [Hinter],
end
```

#### [Kevin Buzzard (May 20 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841144):
fails to simplify

#### [Kevin Buzzard (May 20 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841196):
Is what I have written provable?

#### [Kevin Buzzard (May 20 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841200):
I don't understand how to use `subst`

#### [Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841296):
Is there some crazy diamond thing going on?

#### [Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841297):
Is the issue that I have put a ring structure on F (U cap V cap W)

#### [Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841298):
and a ring structure on F(U cap (V cap W))

#### [Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841300):
sorry -- a group structure

#### [Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841301):
[in real life I have rings]

#### [Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841303):
and a proof that U cap V cap W = U cap (V cap W)

#### [Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841310):
but now there's the question as to whether the group structures get identified?

#### [Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841311):
aargh

#### [Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841312):
Am I in real trouble here??

#### [Kevin Buzzard (May 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841406):
```lean
begin
have Hinter : U ∩ V ∩ W = U ∩ (V ∩ W) := by cc,
refine eq.drec_on Hinter _,
congr,
-- now three goals:
-- ⊢ Fres (U ∩ V ∩ W) U HU1 i = Fres (U ∩ V ∩ W) U HU2 i
-- ⊢ Fres (U ∩ V ∩ W) V HV1 j = Fres (U ∩ V ∩ W) V HV2 j
-- ⊢ Fres (U ∩ V ∩ W) W HW1 k = Fres (U ∩ V ∩ W) W HW2 k
sorry,sorry,sorry
end
```

#### [Kevin Buzzard (May 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841408):
Possible progress

#### [Chris Hughes (May 20 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841482):
```lean
import data.set
section oh_heq
parameters (α : Type) (U V W : set α)

lemma HU1 : U ∩ V ∩ W ⊆ U := set.subset.trans (set.inter_subset_left _ _) (set.inter_subset_left _ _)
lemma HV1 : U ∩ V ∩ W ⊆ V := set.subset.trans (set.inter_subset_left _ _) (set.inter_subset_right _ _)
lemma HW1 : U ∩ V ∩ W ⊆ W := set.inter_subset_right _ _
lemma HU2 : U ∩ (V ∩ W) ⊆ U := set.inter_subset_left _ _
lemma HV2 : U ∩ (V ∩ W) ⊆ V := set.subset.trans (set.inter_subset_right _ _) (set.inter_subset_left _ _)
lemma HW2 : U ∩ (V ∩ W) ⊆ W := set.subset.trans (set.inter_subset_right _ _) (set.inter_subset_right _ _)

set_option trace.app_builder true

lemma T (F : set α → Type) [∀ Z : set α, group (F Z)]
(Fres : ∀ X Y : set α, X ⊆ Y → F Y → F X)
(i : F U) (j : F V) (k : F W) (s t : set α) 
(hst : s = t)
(hsU : s ⊆ U) (hsV : s ⊆ V) (hsW : s ⊆ W)
(htU : t ⊆ U) (htV : t ⊆ V) (htW : t ⊆ W) :
Fres s U hsU i * Fres s V hsV j * Fres s W hsW k
== Fres t U htU i * Fres t V htV j * Fres t W htW k := by subst hst

example (F : set α → Type) [∀ Z : set α, group (F Z)]
(Fres : ∀ X Y : set α, X ⊆ Y → F Y → F X)
(i : F U) (j : F V) (k : F W) :
Fres (U ∩ V ∩ W) U HU1 i * Fres (U ∩ V ∩ W) V HV1 j * Fres (U ∩ V ∩ W) W HW1 k
== Fres (U ∩ (V ∩ W)) U HU2 i * Fres (U ∩ (V ∩ W)) V HV2 j * Fres (U ∩ (V ∩ W)) W HW2 k :=
T _ _ _ _ _ _ _ (set.inter_assoc _ _ _) HU1 HV1 HW1 HU2 HV2 HW2
```

Trouble is `subst` doesn't work very well when the expression is more complicated than `s = t`

#### [Kevin Buzzard (May 20 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841531):
aah we're back with subst

#### [Kevin Buzzard (May 20 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841533):
I wrote `subst [random_thing]` and I get an error I don't understand

#### [Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841539):
so I gave up on subst very early

#### [Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841540):
you're suggesting I persevere

#### [Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841542):
My actual use case has rings and it's addition not multiplication

#### [Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841543):
but it's very close to this

#### [Chris Hughes (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841544):
I used to use `eq.drec_on` with an explicit motive for things like this. That's really messy.

#### [Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841547):
As you saw I tried eq.drec_on and made some progress

#### [Kevin Buzzard (May 20 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841561):
I perhaps need to learn how to use subst

#### [Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841592):
You saw I proved `Hinter : U ∩ V ∩ W = U ∩ (V ∩ W)`

#### [Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841596):
but `subst Hinter`, which somehow feels like what I want to do, gives me `subst tactic failed, hypothesis 'Hinter' is not of the form (x = t) or (t = x)`

#### [Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841597):
That error message is really unhelpful

#### [Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841598):
Does anyone know what it actually means?

#### [Kevin Buzzard (May 20 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841599):
Hinter looks like both of those forms to me :-)

#### [Kevin Buzzard (May 20 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841656):
```lean
begin
have Hinter : U ∩ V ∩ W = U ∩ (V ∩ W) := by cc,
subst Hinter, -- subst tactic failed, hypothesis 'Hinter' is not of the form (x = t) or (t = x)
sorry
end
```

#### [Kevin Buzzard (May 20 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841659):
How is that different to what you're doing?

#### [Chris Hughes (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841716):
I think it's basically that it has to be a really simple expression. `x = t` is fine, but anything like ` f x = t` is not. I might be wrong about that.

#### [Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841717):
You are telling me that subst won't work unless it literally is (one letter) = (one letter)?

#### [Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841719):
Well at the end of the day you apparently proved it and I definitely didn't

#### [Chris Hughes (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841721):
I think so.

#### [Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841722):
`set_option trace.app_builder true`

#### [Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841724):
What was that all about?

#### [Chris Hughes (May 20 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841775):
In this code your goal shouldn't typecheck
```lean
begin
have Hinter : U ∩ V ∩ W = U ∩ (V ∩ W) := by cc,
refine eq.drec_on Hinter _,
congr,
-- now three goals:
-- ⊢ Fres (U ∩ V ∩ W) U HU1 i = Fres (U ∩ V ∩ W) U HU2 i
-- ⊢ Fres (U ∩ V ∩ W) V HV1 j = Fres (U ∩ V ∩ W) V HV2 j
-- ⊢ Fres (U ∩ V ∩ W) W HW1 k = Fres (U ∩ V ∩ W) W HW2 k
sorry,sorry,sorry
end
```

#### [Chris Hughes (May 20 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841776):
but it does.

#### [Chris Hughes (May 20 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841792):
```quote
`set_option trace.app_builder true`
```
That was because something didn't work and the error message suggested I do that.

#### [Kevin Buzzard (May 20 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841794):
yeah that was a bit scary with the =

#### [Kevin Buzzard (May 20 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841797):
but if X = Y then F X = F Y

#### [Kevin Buzzard (May 20 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841855):
Thanks Chris

#### [Kevin Buzzard (May 20 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841858):
Indeed your proof works

#### [Kevin Buzzard (May 20 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841898):
I am currently mulling over having to translate it into the real life situation

#### [Chris Hughes (May 20 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126842102):
```lean
example (F : set α → Type) [∀ Z : set α, group (F Z)]
(Fres : ∀ X Y : set α, X ⊆ Y → F Y → F X)
(i : F U) (j : F V) (k : F W) :
Fres (U ∩ V ∩ W) U HU1 i * Fres (U ∩ V ∩ W) V HV1 j * Fres (U ∩ V ∩ W) W HW1 k
== Fres (U ∩ (V ∩ W)) U HU2 i * Fres (U ∩ (V ∩ W)) V HV2 j * Fres (U ∩ (V ∩ W)) W HW2 k :=
have Hinter : U ∩ V ∩ W = U ∩ (V ∩ W) := by cc,
@eq.drec_on _ (U ∩ V ∩ W) 
(λ s h, Fres (U ∩ V ∩ W) U HU1 i * Fres (U ∩ V ∩ W) V HV1 j * Fres (U ∩ V ∩ W) W HW1 k
== Fres s U (h ▸ HU1) i * Fres s V (h ▸ HV1) j * Fres s W (h ▸ HW1) k) _ Hinter (heq.refl _)
```

#### [Chris Hughes (May 20 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126842149):
Probably the best solution is to get `subst` to work properly. Might be a good after exams project.

#### [Kevin Buzzard (May 20 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126843676):
Thanks a lot for this Chris! I'll see if this method works in my actual file

#### [Mario Carneiro (May 21 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846183):
This works, but I'm not very happy with the result
```

theorem proof_irrel_heq {p q : Prop} (e : p = q) (hp : p) (hq : q) : hp == hq :=
by subst q; congr

example (F : set α → Type) [∀ Z : set α, group (F Z)]
(Fres : ∀ X Y : set α, X ⊆ Y → F Y → F X)
(i : F U) (j : F V) (k : F W) :
Fres (U ∩ V ∩ W) U HU1 i * Fres (U ∩ V ∩ W) V HV1 j * Fres (U ∩ V ∩ W) W HW1 k
== Fres (U ∩ (V ∩ W)) U HU2 i * Fres (U ∩ (V ∩ W)) V HV2 j * Fres (U ∩ (V ∩ W)) W HW2 k
:= 
by have := set.inter_assoc U V W;
   congr; try{assumption};
   { apply proof_irrel_heq, congr, assumption }
```

#### [Mario Carneiro (May 21 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846280):
Didn't I tell you partial functions give you headaches?

#### [Mario Carneiro (May 21 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846474):
Why do you have a `heq` goal in the first place?

#### [Kenny Lau (May 21 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846718):
because of bad interface

#### [Mario Carneiro (May 21 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846779):
oh, there's a bug in `congr`

#### [Mario Carneiro (May 21 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846874):
```
meta def congr' : parse small_nat? → tactic unit
| none         := focus1 (assumption <|> (congr_core >>
  all_goals (reflexivity <|> try (congr' none))))
| (some 0)     := failed
| (some (n+1)) := focus1 (assumption <|> (congr_core >>
  all_goals (reflexivity <|> try (congr' (some n)))))
```
now the following proof works:
```
by have := set.inter_assoc U V W;
   congr'; apply proof_irrel_heq; congr'
```

#### [Kenny Lau (May 21 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846883):
say what

#### [Mario Carneiro (May 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846933):
The congr tactic itself should read:
```
meta def congr : tactic unit :=
do focus1 (assumption <|> (congr_core >> all_goals (reflexivity <|> try congr)))
```
instead of 
```
meta def congr : tactic unit :=
do focus1 (try assumption >> congr_core >> all_goals (try reflexivity >> try congr))
```

#### [Mario Carneiro (May 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846934):
but I don't know if we are still doing bugfixes in 3.4.1

#### [Mario Carneiro (May 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846936):
so I made my own `congr` instead

#### [Mario Carneiro (May 21 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846990):
Not sure why those proof irrel goals appear though, they should also be taken care of by `congr`

#### [Kevin Buzzard (May 21 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860293):
```quote
Why do you have a `heq` goal in the first place?
```
I thought of a way around it, in this case.

#### [Kevin Buzzard (May 21 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860302):
The reason was that I wanted to prove two structures were equal, but one depended on (U cap V cap W) and one on (U cap (V cap W)), because of the way the structures were made (I was trying to prove addition on a quotient type was associative).

#### [Kevin Buzzard (May 21 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860350):
`congr` would go insane when presented with the problem (the first time I tried it, it turned my goal into 176 goals, no typo)

#### [Kevin Buzzard (May 21 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860351):
Kenny suggested a mk_inj solution and that led to the heqs

#### [Kevin Buzzard (May 21 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860352):
I remember Chris moaning about heqs before

#### [Kevin Buzzard (May 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860358):
But last night, 10 minutes after I switched my laptop off and started doing the dishes

#### [Kevin Buzzard (May 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860360):
I realised I could probably work around it on this occasion, by doing something a mathematican would never understand

#### [Kevin Buzzard (May 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860361):
I should restrict my section on U cap (V cap W) to a section on U cap V cap W :-)

#### [Kevin Buzzard (May 21 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860401):
This only changes it up to equivalence, which is OK for me

#### [Kevin Buzzard (May 21 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860409):
[terminology: a sheaf is, amongst other things, a map F : (open sets in a top space) -> (rings) together with restriction maps F(U) -> F(V) whenever V is a subset of U]

#### [Kevin Buzzard (May 21 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860447):
The concept of restricting to a subset which is non-definitionally-equal to the set you started with is alien to mathematics but it's exactly the crazy idea which will get me out of this hell

#### [Kevin Buzzard (May 21 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860467):
@**Mario Carneiro** Is Chris right when he suggests that subst could do with some work? His solution seemed to be "subst hst, where h : s = t, and then apply when s and t are more complicated"

#### [Kevin Buzzard (May 21 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860471):
as opposed to "subst [the thing we actually want to subst]"

#### [Kevin Buzzard (May 21 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860477):
I could imagine that Chris might want to learn something about tactics over the summer. He has two months of being paid to work for me and can do anything

#### [Kevin Buzzard (May 21 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860478):
as long as his boss OK's it

#### [Mario Carneiro (May 21 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860530):
I was thinking of suggesting that myself. I assume you have some composition axioms, so it might be easiest to work with the restriction from (U/\V)/\W to U/\V/\W

#### [Mario Carneiro (May 21 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860540):
It's not as crazy as it sounds; it's basically using (part of) the fact that (U/\V)/\W and U/\V/\W are "isomorphic but not equal" in the DTT sense

#### [Mario Carneiro (May 21 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860581):
it helps to think like in category theory here

#### [Mario Carneiro (May 21 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860586):
`subst` is a very basic tactic. It does one thing, and does it well

#### [Mario Carneiro (May 21 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860647):
you give it a hypothesis of the form `term = x` or `x = term`, and it will eliminate `x` in favor of `term` everywhere. This is rather restrictive, but the upside is that it *never* gets tripped up in dependencies like `rw` and `simp` can, because it is implemented purely using `eq.drec` and the variable restriction ensures that the motive is always type correct

#### [Kevin Buzzard (May 21 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860650):
Oh -- `x = t` means `x = term`? ;-)

#### [Mario Carneiro (May 21 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860680):
(you can also say `subst x` instead of `subst h` when you have `h : x = term` in the context)

#### [Kevin Buzzard (May 21 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860694):
isomorphic but not equal is something I know well in the context where the underlying sets are different, but I am only just coming to terms with generalising the idea to situations where the DTTist thinks they're isomorphic and the ZFCist is blinded by this because they think they're equal :-)

#### [Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860699):
Unrelated -- I see you wrote (U cap V) cap W v U cap V cap W

#### [Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860701):
I claim that you mean U cap (V cap W) vs U cap V cap W

#### [Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860702):
and actually this is minorly annoying

#### [Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860703):
because my proofs that x is in U cap V cap W

#### [Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860705):
all look like <<HU,HV>,HW>

#### [Mario Carneiro (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860744):
ah, cap is left assoc?

#### [Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860745):
Is this an oversight

#### [Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860746):
I assume it is

#### [Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860747):
and I already noticed that this was annoying

#### [Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860749):
but I wasn't confident enough to know whether there are other reasons for this

#### [Mario Carneiro (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860750):
I don't have any strong opinions on whether union and intersection are left or right assoc

#### [Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860751):
all I knew is that my proofs were two characters longer than I wanted them to be

#### [Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860758):
you would do if you had to keep writing <<HU,HV>,HW>

#### [Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860763):
heh

#### [Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860765):
maybe I should restrict to U cap (V cap W)

#### [Mario Carneiro (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860766):
also lost two chars there

#### [Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860768):
yeah but I only have to do that once

#### [Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860810):
Something else I noticed

#### [Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860811):
was that existsi is kind of dumb

#### [Mario Carneiro (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860812):
I never use it tbh

#### [Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860813):
existsi (<<HU,HV>,HW>)

#### [Mario Carneiro (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860814):
lol no

#### [Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860816):
"That doesn't make sense"

#### [Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860820):
"You have to tell me the type"

#### [Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860822):
"because I don't know the type"

#### [Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860828):
"even though the goal is "there exists a proof that x is in U cap V cap W"

#### [Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860829):
"

#### [Mario Carneiro (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860830):
just use refine instead

#### [Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860833):
What are your views on "existsi _,tactic.swap"

#### [Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860834):
I think you once told me to avoid it

#### [Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860835):
but it does exactly what I want sometimes

#### [Kevin Buzzard (May 21 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860878):
"let's just remove the bloody exists symbol and make it a goal"

#### [Mario Carneiro (May 21 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860880):
For exploratory tactic writing it's fine I guess

#### [Kevin Buzzard (May 21 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860881):
what about definitive scheme writing?

#### [Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860884):
:-)

#### [Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860890):
I guess it's all exploratory as far as I am concerned

#### [Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860892):
OK back to work

#### [Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860893):
Thanks for the comments as ever

#### [Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861159):
rofl

#### [Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861161):
I proved associativity

#### [Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861163):
end of proof looks like this

#### [Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861164):
```lean
  existsi (Ua ∩ Ub ∩ Uc), -- brainwave
  existsi (⟨⟨Hxa,Hxb⟩,Hxc⟩ : x ∈ Ua ∩ Ub ∩ Uc),
  existsi (Hstandard _ _ (Hstandard _ _ BUa BUb) BUc),
  existsi (set.subset.refl (Ua ∩ Ub ∩ Uc)),
  existsi ((set.inter_assoc Ua Ub Uc ▸ set.subset.refl _) : Ua ∩ Ub ∩ Uc ⊆ Ua ∩ (Ub ∩ Uc)),
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←(presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw ←presheaf_of_types_on_basis.Hcomp',
  rw add_assoc,
```

#### [Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861165):
restrict to isomorphic set

#### [Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861171):
prove some trivialities

#### [Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861173):
a bit of rewriting

#### [Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861174):
and apply associativity

#### [Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861177):
not sure that proof is mathlib-ready

#### [Mario Carneiro (May 21 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861289):
have you tried using `simp` instead of `rw`?

#### [Kevin Buzzard (May 21 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861295):
simp insists on rewriting a+b+c as c+a+b

#### [Kevin Buzzard (May 21 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861296):
on exactly one side

#### [Kevin Buzzard (May 21 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861298):
so I never got it to do anything useful

#### [Kevin Buzzard (May 21 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861347):
anyway, this is a breakthrough because if I can prove add_assoc I can prove all the ring axioms

#### [Kevin Buzzard (May 21 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861403):
simp [add_assoc,more stuff] doesn't even do it when we're on the last line

#### [Kevin Buzzard (May 21 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861404):
My goal is too messy for simp

#### [Kevin Buzzard (May 21 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861405):
I need comp

#### [Kevin Buzzard (May 21 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861413):
lol

#### [Kevin Buzzard (May 21 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861419):
`    simp [add_assoc,add_comm,(presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,presheaf_of_types_on_basis.Hcomp']` turns a goal which is closed by `rw add_assoc` to a goal which is closed by `rw add_comm`

#### [Kevin Buzzard (May 21 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861421):
thanks simp

#### [Kevin Buzzard (May 21 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861481):
goal is `(FPRB.to_presheaf_of_types_on_basis).res _ _ _ sa + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb +
      (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc =
    (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sa +
      ((FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc)`

#### [Kevin Buzzard (May 21 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861483):
`    simp [add_assoc,add_comm],`

#### [Kevin Buzzard (May 21 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861525):
goal becomes `(FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb =
    (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc`

#### [Kevin Buzzard (May 21 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861527):
Unless my eyes are deceiving me simp just turned add_assoc into add_comm

#### [Kevin Buzzard (May 21 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861532):
terms are in a comm_ring

#### [Kevin Buzzard (May 21 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861601):
obviously-minimised version doesn't exhibit the problem

#### [Kevin Buzzard (May 21 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861645):
sa,sb,sc all in different rings, the FPRB...res is mapping them down all into the same ring

#### [Kevin Buzzard (May 21 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861663):
```lean
example (R : Type) [comm_ring R] (α β γ : Type) (a : α) (b : β) (c : γ)
(f : α → R) (g : β → R) (h : γ → R) : f a + g b + h c = f a + (g b + h c) := begin
simp [add_assoc,add_comm],
end
```

#### [Kevin Buzzard (May 21 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861664):
works fine

#### [Kevin Buzzard (May 21 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861705):
so it's something in my `_`s

#### [Kevin Buzzard (May 21 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861768):
but at the end of the day I have a goal which can be cleared (without errors) either with `rw add_assoc` or `simp [add_assoc,add_comm],rw add_comm`

#### [Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861886):
hey stupid comm_ring, why are you asking me to prove a+0=a and 0+a=a and a+b=b+a?

#### [Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861889):
well, I know why

#### [Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861891):
but wouldn't it be nice if you didn't

#### [Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861896):
I need a better comm_ring constructor I guess

#### [Chris Hughes (May 21 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863336):
`simp only` might help

#### [Mario Carneiro (May 21 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863815):
you can always add `-add_comm` to your simp set to fix superfluous rewriting

#### [Kevin Buzzard (May 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863881):
`existsi (Ua ∩ Ua)`

#### [Kevin Buzzard (May 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863882):
I can't believe I just wrote that

#### [Kevin Buzzard (May 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863883):
proving add_neg

#### [Kevin Buzzard (May 21 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863923):
just restrict everything down to there and it will be fine

#### [Patrick Massot (May 21 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864002):
Just to be sure: Kevin, do you know you can write `repeat { rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add, },`?

#### [Kevin Buzzard (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864156):
yeah, but I like watching the goal slowly decay

#### [Kevin Buzzard (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864162):
I just had to write ` rw is_ring_hom.map_neg (FPRB.res _ _ _);try {apply_instance},`

#### [Kevin Buzzard (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864164):
that surprised me.

#### [Patrick Massot (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864168):
I'm still puzzled each time I need to write `apply_instance`.

#### [Patrick Massot (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864171):
I don't understand why Lean doesn't do that for me

#### [Patrick Massot (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864177):
sometimes

#### [Kevin Buzzard (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864179):
I applied map_neg (the statement that a morphism of rings satisfies f(-x)=-f(x))

#### [Kevin Buzzard (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864185):
and all of a sudden it asked me if f was a ring hom and was the source a ring?

#### [Kevin Buzzard (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864191):
and apply_instance said yes

#### [Patrick Massot (May 21 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864254):
Exactly the kind of situation where I'm puzzled

#### [Patrick Massot (May 21 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864257):
Why isn't this automatic?

#### [Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864259):
I dunno

#### [Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864298):
I have two choices today

#### [Patrick Massot (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864301):
Is it a bug in the `apply` tactic?

#### [Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864305):
I could spend a pleasant day verifying the axioms of a ring

#### [Patrick Massot (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864306):
(Or simp, refine,...)

#### [Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864307):
or I could mark 100 proofs of various trivial lemmas about sup of a set of reals

#### [Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864309):
and I am currently at home doing the former

#### [Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864312):
and I'm already on add_comm

#### [Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864318):
but I really should be doing the latter...

#### [Patrick Massot (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864323):
Too bad you can't quite hire Kenny or Chris to mark these exams for you...

#### [Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864324):
I knew that once I managed add_assoc the rest would be trivial

#### [Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864326):
but it takes time

#### [Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864327):
rofl

#### [Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864330):
I'm not sure if the university would be keen on students marking their own scripts

#### [Patrick Massot (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864384):
yep, universities tend to have all kind of stupid administrative rules like that

#### [Kevin Buzzard (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864386):
I am much keener on Lean marking their scripts

#### [Kevin Buzzard (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864391):
When they're done I might well write a blog post about how Lean does the question

#### [Patrick Massot (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864393):
Do you know which ones are from Kenny and Chris or are there anonymous?

#### [Kevin Buzzard (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864395):
yes and yes

#### [Patrick Massot (May 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864410):
Do you mean two out of 100 gave answer in Lean written on paper, and you guessed?

#### [Kevin Buzzard (May 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864414):
I recognise their handwriting and I know enough about where they were sitting in the room to be able to work it out

#### [Kevin Buzzard (May 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864474):
In fact I missed Chris' script for Q1

#### [Kevin Buzzard (May 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864480):
so I don't really know

#### [Kevin Buzzard (May 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864487):
but I did notice Kenny's, a combination of the handwriting, the way he presented the arguments, and the fact that I did unfortunately know that his script would be "around this point in the pile"

#### [Kevin Buzzard (May 21 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864489):
I could be wrong though

#### [Kevin Buzzard (May 21 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864497):
I have no formal proof that it was Kenny's

#### [Kevin Buzzard (May 21 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864505):
In fact it was the fact that I recognised Kenny's handwriting that I realised I must have missed Chris' script

#### [Kenny Lau (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864552):
where did you get my handwriting sample from?

#### [Kevin Buzzard (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864557):
You have sent me lots of handwriting in private zulip chats

#### [Kevin Buzzard (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864558):
and I am sort of a bit weird about handwriting for some reason

#### [Kevin Buzzard (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864561):
I am quite good at recognising it

#### [Kenny Lau (May 21 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864564):
very interesting

#### [Kevin Buzzard (May 21 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864580):
I guess I should be clear: I have no way of verifying that the script I strongly suspected was Kenny's, was Kenny's

#### [Kevin Buzzard (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864629):
which of course is a good thing

#### [Kenny Lau (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864633):
how many questions have you marked?

#### [Kevin Buzzard (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864634):
1.3

#### [Kenny Lau (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864638):
did you mark the sup(A+B)=sup(A)+sup(B)?

#### [Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864644):
doing that one today

#### [Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864647):
or more of it

#### [Kenny Lau (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864648):
I see

#### [Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864650):
Hope to get another 0.3 of it done

#### [Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864661):
indeed I am just off now

#### [Mario Carneiro (May 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864704):
Sometimes you get those `apply_instance` goals when you use `apply` with underscores, due to some strange elaboration order stuff. Essentially those goals are unknown at the time when instance resolution normally happens

#### [Mario Carneiro (May 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864707):
using `refine` instead may help

#### [Patrick Massot (May 21 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865634):
Do you get a student teacher collusion law suit if some other student realize Kenny answered "This function is continuous because it goes from R to R" as a signal to trigger special marking?

#### [Andrew Ashworth (May 21 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865906):
I always appreciated automated marking, which you can do for programming assignments (and Lean, too!). Instant feedback if the grader is set up correctly, less need to attend office hours in order to discover that "one special trick professors want you to know about"

#### [Patrick Massot (May 21 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865914):
What do you use for automated marking?

#### [Andrew Ashworth (May 21 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865978):
Our CS department cobbled together a web server and a bunch of Python scripts

#### [Patrick Massot (May 21 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865979):
Is there anything public?

#### [Andrew Ashworth (May 21 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126866043):
hmm, doubt it. shell scripts aren't the sort of thing that people would even think to release

#### [Andrew Ashworth (May 21 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126866277):
they all tend to be custom solutions based on whatever your institution's favorite content management system is... for example, this one links with Canvas: https://github.com/arthuraa/sf-grader

#### [Kevin Buzzard (May 25 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/127092646):
```quote
Do you know which ones are from Kenny and Chris or are there anonymous?
```
OK so I asked some question about sups. I got about 80 correct solutions, of which 79 were a proof by contradiction, and one was constructive. And in Kenny's handwriting. And using the kind of pen he uses. But really -- it is anonymous!

#### [Andrew Ashworth (May 25 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/127092713):
You can tell the difference between pens? Does he have a fountain pen?

#### [Moses Schönfinkel (May 25 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/127092857):
Perhaps Kenny uses one of those rainbow pencils.

