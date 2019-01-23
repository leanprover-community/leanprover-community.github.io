---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/82169inductionargument2notavariable.html
---

## Stream: [new members](index.html)
### Topic: [induction: "argument 2 not a variable"](82169inductionargument2notavariable.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 03 2019 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154266676):
Hi, I have an inductive predicate SN that takes a relation as argument (here eval), see the code snippet below. An induction over the statement ```SN eval st```gives me the error: induction tactic failed, argument #2 of major premise type SN eval st is not a variable. 

Is it a problem that SN takes eval as an argument? 

```
inductive tm  : nat -> Type 
  | app : Π {ntm : nat}, tm ntm -> tm ntm -> tm ntm
  /- ... -/

reserve infixl `≻`:40
inductive eval : Π {n}, tm n → tm n → Prop
infixl `≻` := eval
| eappl {n} {e₁ : tm n} {e₁' e₂} : e₁ ≻ e₁' →  tm.app e₁ e₂ ≻ tm.app e₁' e₂
  /- ... -/
infix `≻` := eval
open eval

inductive SN {n} : (tm n -> tm n -> Prop) → tm n -> Prop  
| sn_step (R: tm n → tm n → Prop) (e1 : tm n) : (forall e2, R e1 e2 -> SN R e2) -> SN R e1.

definition SNe {n} := @SN n eval.

theorem SN₁ {n} (s t : tm n) : SNe (tm.app s t) → SNe s ∧ SNe t := 
begin 
  intro h₁, split, 
  { generalize h₂ : (tm.app s t) = st, revert h₁, rw h₂, intro h₁, revert s t h₂, 
  induction h₁ with st hst ihst,  }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154268520):
I get a different error on this example, `generalize tactic failed, failed to find expression in the target`, which is solved by unfolding `SNe` at `h1`. Is this the right code snippet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 03 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154269026):
Oh, I still get the induction error (on the example alone)...
Unfolding ```SNe``` at ```h1``` makes the induction tactic work, but gives me this induction hypothesis:
```ih_1 :
  ∀ (e2 : tm n) (a_1 : R e1 e2),
    (λ (_x : tm n → tm n → Prop) (st : tm n) (h₁ : SN _x st), ∀ (s t : tm n), app s t = st → SNe s) R e2 _ ```

where R is added to the hypotheses, ```R : tm n → tm n → Prop```. I want  ```R```to be ```eval```, though. How can that be done?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154269337):
Can you make `R` a parameter to `SN`? (Move it to the left of the colon in the definition of `SN`, that is.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 03 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154269789):
That produces the same induction hypothesis (but unfolding ```SNe``` is not needed anymore)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 03 2019 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154269844):
I think we're either using different versions of Lean, or working on different examples.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 03 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154270131):
Ok, maybe my version is too old, I'm using 3-3-0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 04 2019 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154273397):
I guess most people here use 3.4.1.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 04 2019 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154274246):
Yeah sorry, I switched versions now and the tip with ```R```as parameter works for the induction tactic. But there are problems for ```cases``` and ```constructor```with this definiton, for example:

```
inductive tm  : nat -> Type
  | app : Π {ntm : nat}, tm ntm -> tm ntm -> tm ntm
  /- ... -/

reserve infixl `≻`:40
inductive eval : Π {n}, tm n → tm n → Prop
infixl `≻` := eval
| eappl {n} {e₁ : tm n} {e₁' e₂} : e₁ ≻ e₁' →  tm.app e₁ e₂ ≻ tm.app e₁' e₂
  /- ... -/
infix `≻` := eval
open eval
inductive star {n} (R : tm n → tm n → Prop) : tm n → (tm n → Prop)
| srefl {e} : star e e 
| sstep {e₁ e₂ e₃} :  (R e₁ e₂) → star e₂ e₃ → star e₁ e₃
open star
infix `≻*`:40 := star eval

inductive SN {n} (R : tm n -> tm n -> Prop ) : tm n -> Prop  
| sn_step (R: tm n → tm n → Prop) (e1 : tm n) : (forall e2, R e1 e2 -> SN e2) -> SN e1.

definition SNe {n} := @SN n eval.

lemma closed_star {n} (s t): s ≻* t -> SNe s -> @SNe n t :=
begin intros h1 h2,  induction h1 with s' s' t' e h3 h4 ih, 
      { assumption },
      { apply ih, cases h2,   }, 
end
```

Cases adds a hypothesis of type ```R : tm n → tm n → Prop``` (similar to what happened with induction before)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%3A%20%22argument%202%20not%20a%20variable%22/near/154386747):
you have `R` in the `sn_step` constructor even though it's already declared, so it's a different `R`

