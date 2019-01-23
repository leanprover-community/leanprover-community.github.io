---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24978leanunresponsive.html
---

## Stream: [new members](index.html)
### Topic: [lean unresponsive](24978leanunresponsive.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 07 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154576468):
Hi, when I use 3.4.1, there are problems with displaying the goal if proofs get longer. In both Emacs and vscode, the goal is not displayed anymore and the message box just says 'updating'. If the proof is deleted and I restart it, it always happens again in some subcase as soon as the proof gets longer (it is not really that huge though, 20 lines maybe). Lean does not respond if something is typed  (if I type "end" I get the synthesize-placeholder error). Has anyone had this before?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 07 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154577042):
In VS code, are you seeing any indications that lean is still working (e.g. orange bars on the sides)? It might help if you post a minimum example, since slowness could be caused by a variety of things...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Uranus Testing (Jan 07 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154577401):
There are orange bars on the sides and indicator in status bar (“Lean [indicator] (checking visible lines)”).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 08 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154630892):
The orange bars are there for a moment but disappear directly.

The proof uses two other files of definitions, here are the types if that helps: 
```
variable Fin : nat -> Type
variable tm : nat -> Type 
variable neutral {n} : tm n → Prop
variable eval : Π {n}, tm n → tm n → Prop 
inductive type : Type
| tint : type
| tarrow : type → type → type
variable types : Π {m}, (Fin m → type) → tm m → type → Prop

variable R :  Π {n : nat}, (Fin n → type) → type → tm n → Prop 

variable SNe : Π {n}, tm n → Prop

theorem CR₁₃x {n} (Γ) (A : type) (s:tm n) : (R Γ A s → SNe s) ∧  
  (types Γ s A → neutral s → (∀ t, eval s t → R Γ A t)  → R Γ A s) :=   ... 
```

I do an induction on the type A, but the proof always crashes somewhere in the tarrow-case ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 08 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631244):
more code would help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Uranus Testing (Jan 08 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631733):
What if run file from command line ($ lean /path/to/proof.lean)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 08 2019 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631799):
```lean

open nat
inductive Fin : ℕ → Type
| fz {n} : Fin (succ n)
| fs {n} : Fin n → Fin (succ n)
open Fin 
attribute reducible Fin 

inductive tm  : nat -> Type 
  | var_tm : Π {ntm : nat}, Fin ntm -> tm ntm
  | app : Π {ntm : nat}, tm ntm -> tm ntm -> tm ntm
  | lam : Π {ntm : nat}, tm (nat.succ ntm) -> tm ntm
  | const : Π {ntm : nat}, nat  -> tm ntm
  | plus : Π {ntm : nat}, tm ntm -> tm ntm -> tm ntm
open tm 

reserve infixl `≻`:40
inductive eval : Π {n}, tm n → tm n → Prop
infixl `≻` := eval
| eappl {n} {e₁ : tm n} {e₁' e₂} : e₁ ≻ e₁' →  app e₁ e₂ ≻ app e₁' e₂
| eappr {n} {e₁ : tm n} {e₂ e₂'} : e₂ ≻ e₂' → app e₁ e₂ ≻ app e₁ e₂'
| elam {n} {e1 : tm (nat.succ n)} {e2} : e1 ≻ e2 → lam e1 ≻ lam e2
| eplusl {n} {e₁ : tm n}{e₁' e₂} : e₁ ≻ e₁' → plus e₁ e₂ ≻ plus e₁' e₂
| eplusr {n} {e₁ : tm n} {e₂ e₂'} : e₂ ≻ e₂' → plus e₁ e₂ ≻ plus e₁ e₂'
| econst {n} {n₁ n₂} : @eval n (plus (const n₁) (const n₂)) (const (n₁+n₂))
--| ebeta {n} {e₁ : tm (nat.succ n)} {e₂} : app (lam e₁) e₂ ≻ (subst_tm (scons e₂ var_tm ) (e₁))
infix `≻` := eval
open eval

inductive type : Type
  | tint : type
  | tarrow : type → type → type
open type
infixl `⤏`:50 := tarrow

definition ctx (m) := Fin m → type

inductive types : Π {m}, (Fin m → type) → tm m → type → Prop
  | tvar {m} Γ (x : Fin m) : types Γ (var_tm x) (Γ x)
  | tapp {m} Γ (e₁ : tm m) e₂ (A B) : types Γ e₁ (tarrow A B) → types Γ e₂ A → types Γ (app e₁ e₂) B
  | tplus {m} Γ (e₁ : tm m) (e₂) : types Γ e₁ tint → types Γ e₂ tint → types Γ (plus e₁ e₂) tint 
 -- | tlam {m} Γ (e : tm (nat.succ m)) (A B) : types (@scons _ m  A Γ) e B → types Γ (lam e) (A ⤏ B) 
  | tconst {m n} (Γ : ctx m) : types Γ (const n) tint
notation Γ ` ⊢ `:50 x ` : ` A:50 := types Γ x A. 
open types

definition agree_ren {n m} (Γ : ctx n) (Γ' : ctx m) (ξ : Fin m → Fin n) := 
    forall x, (Γ (ξ x)) = Γ' x. 

notation Γ `≼`:50 Δ `:`:50 ξ := agree_ren Δ Γ ξ.

definition neutral {n} : tm n → Prop
| (lam s) := ff
| _ := tt 


inductive SN {n} (R : tm n -> tm n -> Prop ) : tm n -> Prop  
| sn_step (e1 : tm n) : (forall e2, R e1 e2 -> SN e2) -> SN e1.

definition SNe {n} := @SN n eval.

constant ren_tm : Π { mtm : nat } { ntm : nat } (xitm : Fin mtm -> Fin ntm) (s : tm mtm), tm ntm --...

definition R : Π {n}, (ctx n) → type → tm n → Prop 
| n Γ tint s :=  (Γ ⊢ s : tint) ∧ SNe s
| n Γ (tarrow A B) s := Γ ⊢ s : tarrow A B ∧ forall {m : nat} ξ Δ t,
    (Γ ≼ Δ : ξ) → @R m Δ A t -> R Δ B (app (ren_tm ξ s) t)

theorem CR₁₃ {n} (Γ) (A) (s: tm n) : (R Γ A s → SNe s) ∧ 
  (Γ ⊢ s : A → neutral s → (∀ t, s ≻ t → R Γ A t) → R Γ A s) :=  
begin 
  revert s Γ n, induction A; intros,
  { split, 
    { intro h, apply h.right,}, 
    { intros, split, admit,
     constructor, intros,
    apply (a_2 _ _).right, admit,
    },
  },
  { split, 
    { intro h, apply SN_appzero, 
    have p:= (A_ih_a_1 (A_a.;Γ) (app (ren_tm shift s) (var_tm var_zero))),  
    apply p.left, apply h.right, 
      { intro x,  refl, },
      { apply (A_ih_a _ _).right, 
        { constructor, },
        { simp [neutral], },
        { intros t q, cases q, },
      },
    },
    { intros h₁ h₂ h₃, split, aauto,
    intros m ξ Δ t p₁ p₂,
    have p₃ : SNe t, 
      from begin 
        apply (A_ih_a _ _).left, aauto 
      end,
    induction p₃, 
```
There are some more definitions about properties of tm n, though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 08 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631854):
It compiles if I run it from the command line but I can't finish the proof in interactive mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 08 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631855):
you still aren't showing us the exact part of your code that crashes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Uranus Testing (Jan 08 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632041):
Look at “Lean: Server Errors” log in Visual Studio Code, it may be useful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 08 2019 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632221):
It added the induction where it crashed, but right now I can't even edit something at the beginning of the proof...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 08 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632274):
you are advised to put `end` immediately after you put `begin` (and then add stuff between), etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Jan 08 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632415):
Oh that solved it! Thanks a lot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 08 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632772):
This may be a good time to start using VScode code snippets. In menu File/Preferences/User code snippet (or slight variation on this, I'm making up translation from French) and select `lean.json`. Then put in:
```json
{
	"Proof": {
        "prefix": "proof",
        "body": [
		  "begin",
		  "  $0",
		  "  sorry",
		  "end",
        ],
        "description": "Proof tactic block"
	}
```
Then you can (start to) type  proof and auto-completion will suggests using the snippet. After accepting that suggestion VScode will write "begin", "sorry", "end" and put the cursor at the right position

