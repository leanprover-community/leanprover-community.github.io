---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08987Freshofftheboat.html
---

## Stream: [general](index.html)
### Topic: [Fresh off the boat](08987Freshofftheboat.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351061):
Anyone is willing to prove this example for me? It seems too obvious, but I have not luck doing it within the past hour.

```
universe u

variable {α : Type u}

structure constraint (α:Type u) :=
  cnstr::
  (trv:bool) -- is trivial
  (stt:bool) -- is strict
  (low:bool) -- is lower-bound
  (bnd:α)
open constraint

def setof : constraint α → α → Prop 
| (cnstr tt _  _   _  ) _ := tt
| (cnstr _  tt low bnd) a := tt --if low then bnd < a else a < bnd
| (cnstr _  ff low bnd) a := tt --if low then bnd ≤ a else a ≤ bnd

example (c: constraint α) (a:α) : setof c a := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351110):
It doesn't even typecheck @**Nima**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351152):
@**Kenny Lau** Sorry, I  added "open constraint". Now it is typed checked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 29 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351206):
you can prove it as:

```
example (c: constraint α) (a:α) : setof c a := 
by cases c ; trivial
```

I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351263):
@**Simon Hudon** internal.lean:21:59: error
trivial tactic failed
state:
α : Type u,
a : α,
trv stt low : bool,
bnd : α
⊢ setof {trv := trv, stt := stt, low := low, bnd := bnd} a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351376):
You probably want `true` instead of `tt` in the definition of `setof`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 29 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351484):
And you may find it easier to use this definition rather than yours:

```
inductive constraint (a : Type u)
| trivial : constraint
| strict_upper (x : a) : constraint
| strict_lower (x : a) : constraint
| nonstrict_upper (x : a) : constraint
| nonstrict_lower (x : a) : constraint
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351488):
@**Mario Carneiro** 
The following gives me the same error
```
def  setof : constraint α → α →  Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr _ tt low bnd) a := true --if low then bnd < a else a < bnd
| (cnstr _ ff low bnd) a := true --if low then bnd ≤ a else a ≤ bnd
```
The following is not typechecked
```
def  setof : constraint α → α →  Prop
| (cnstr true _ _ _ ) _ := true
| (cnstr _ true low bnd) a := true --if low then bnd < a else a < bnd
| (cnstr _ false low bnd) a := true --if low then bnd ≤ a else a ≤ bnd
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351496):
The first one is what I mean. FYI you can code block with triple backquote before and after

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351539):
```
def setof : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr ff tt low bnd) a := true --if low then bnd < a else a < bnd
| (cnstr ff ff low bnd) a := true --if low then bnd ≤ a else a ≤ bnd

example : ∀ (c : constraint α) (a:α), setof c a
| (cnstr tt _ _ _) _ := trivial
| (cnstr ff tt low bnd) a := trivial
| (cnstr ff ff low bnd) a := trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351545):
@**Mario Carneiro** you don't need after :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351546):
Are you one of those people who leaves off `</html>`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351547):
YOU RUINED THE INTERNET

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351592):
@**Mario Carneiro** Not sure what you mean!?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351593):
About what? The example shows how to prove the theorem by cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351594):
my quip about the internet was for kenny's benefit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351633):
Note that you need to explicitly specify `ff` for the latter two cases in the definition of `setof` for the proof to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351638):
@**Mario Carneiro** Thanks a lot, it worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351677):
Also, if you want to use `<` you will need an appropriate typeclass, e.g.
```
def setof [linear_order α] : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr ff tt low bnd) a := if low then bnd < a else a < bnd
| (cnstr ff ff low bnd) a := if low then bnd ≤ a else a ≤ bnd
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351684):
@**Mario Carneiro** too soon for those lessons ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351726):
I agree with simon though about your encoding; having a bunch of `bool` flags will make things harder than just having a single inductive case split

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351776):
You can also replace `α → Prop` with `set α` in the definition of `setof` (they are the same, but `set α` has more associated notations)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351777):
@**Mario Carneiro** Is there any easy explanation for why do I need "to explicitly specify `ff` for the latter two cases in the definition of `setof` for the proof to work "

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351821):
And if you want to avoid type classes, you should pick a specific type (e.g. `ℕ`, `ℤ`, `ℚ`, `ℝ`) and the order will come from there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 29 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351866):
```quote
@**Mario Carneiro** Is there any easy explanation for why do I need "to explicitly specify `ff` for the latter two cases in the definition of `setof` for the proof to work "
```
Because your definition has three equations and you can't match against the bools unless you know their values because you use their exact values in the equations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 29 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351867):
E.g.:

```
| (cnstr tt _ _ _ ) _ := true 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351870):
```
def setof : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr ff tt low bnd) a := true
| (cnstr ff ff low bnd) a := true
#print prefix setof.equations
-- setof.equations._eqn_1 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := ff, low := low, bnd := bnd} a = true
-- setof.equations._eqn_2 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := tt, low := low, bnd := bnd} a = true
-- setof.equations._eqn_3 : ∀ {α : Type u} (_x _x_1 : bool) (_x_2 _x_3 : α), setof {trv := tt, stt := _x, low := _x_1, bnd := _x_2} _x_3 = true

def setof : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr _ tt low bnd) a := true
| (cnstr _ ff low bnd) a := true
#print prefix setof.equations
-- setof.equations._eqn_1 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := ff, low := low, bnd := bnd} a = true
-- setof.equations._eqn_2 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := tt, low := low, bnd := bnd} a = true
-- setof.equations._eqn_3 : ∀ {α : Type u} (_x : bool) (_x_1 _x_2 : α), setof {trv := tt, stt := ff, low := _x, bnd := _x_1} _x_2 = true
-- setof.equations._eqn_4 : ∀ {α : Type u} (_x : bool) (_x_1 _x_2 : α), setof {trv := tt, stt := tt, low := _x, bnd := _x_1} _x_2 = true
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351918):
Actually, the problem is that without specifying that the last two cases are `ff`, it does its first case split on the second bool, leading to four cases overall (with a superfluous case split on `stt` in the trivial case). This means that later you will need to case on it in the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351924):
@**Mario Carneiro** So the following from "8.2. Wildcards and Overlapping Patterns" is not that useful " But Lean handles the ambiguity by using the first applicable equation, so the net result is the same "

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351972):
This has more to do with internals of the heuristics for what to case split when you aren't being explicit about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351976):
@**Mario Carneiro** Got it! Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351979):
There's really no need to use a variable in the latter cases, you know it's `ff` and by writing it you tell lean to split there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124369160):
Have I defined `has_coe_to_sort` correctly? If so, how do I fix the `admit`s in my proof?
```
inductive constraint
| trv                    : constraint
| stt (bnd:ℕ) (low:Prop) : constraint
| nst (bnd:ℕ) (low:Prop) : constraint

namespace constraint

def setof : constraint → ℕ → Prop := 
begin
  intros c a,
  cases c with bnd lft bnd lft,
    case trv         {exact true},
    case stt bnd lft {exact lft ∧ bnd<a ∨ a < bnd},
    case nst bnd lft {exact lft ∧ bnd≤a ∨ a ≤ bnd},
end

instance constraint_to_sort : has_coe_to_sort constraint :=
  {S := Type, coe := λ S, {x // setof S x}}

example : ∀ (c:constraint) (n:c), setof c n :=
begin
  intros c n,
  cases c,
    trivial,
    begin
      admit
    end,
    begin
      admit
    end
end

end constraint 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371359):
This doesn't typecheck for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371371):
```
invalid `case`, there is no goal tagged with prefix [constraint.stt, bnd, lft]
state:
2 goals
case constraint.stt
a bnd : ℕ,
lft : Prop
⊢ Prop

case constraint.nst
a bnd : ℕ,
lft : Prop
⊢ Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371375):
line 13

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371556):
fixed it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371576):
```
def setof : constraint → ℕ → Prop :=
begin
  intros c a,
  cases c with bnd lft bnd lft,
    case trv         {exact true},
    case stt {exact lft ∧ bnd<a ∨ a < bnd},
    case nst {exact lft ∧ bnd≤a ∨ a ≤ bnd},
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371579):
I'm using a recent lean nightly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371678):
@**Kevin Buzzard** 
The following two lines fixed it (replace `admit`s)
`exact @subtype.property nat (setof (stt bnd low)) n`
`exact @subtype.property nat (setof (nst bnd low)) n`
In fact I can solve the example in the following way
```
example : ∀ (c:constraint) (n:c), setof c n :=
begin
  intros c n,
  exact @subtype.property nat (setof c) n
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371841):
I am confused about what's going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371847):
`setof c` wants a nat, and you give it `n`, which is a `c`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124375020):
Why the following is invalid? 
Error Message " invalid universe declaration, 'u_1' shadows a local universe"
If I use `variable α : Type u` then everything will be fine
```
universe u
constant  α : Type u
variables x y : α
```
The following gives me no error (why?):
```
universe u
constant α : Type u
variable x : α 
variable y : α 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376097):
I know the following example can be solve by replacing the last line with `exact hm`. But why I receive a this error:
```
universe u
variable {α : Type u}
constant le : α → α → Prop
example : 
∀ (α : Type u) 
  (hm : ∃ (m : α), ∀ (m' : α), le m m'),
  (∃ (m : α), ∀ (a : α) , le m a) := 
begin
  intros α hm,
  match hm with ⟨m,hh⟩ := sorry
end
```
It gives me
```
tmp.lean:12:2: error
don't know how to synthesize placeholder
context:
⊢ Type ?

tmp.lean:12:2: error
equation compiler failed (use 'set_option trace.eqn_compiler.elim_match true' for additional details)

tmp.lean:12:8: error
unknown identifier 'hm'

tmp.lean:12:8: error
don't know how to synthesize placeholder
context:
⊢ Sort ?

tmp.lean:12:16: error
invalid constructor ⟨...⟩, expected type is not an inductive type
  ?m_1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376139):
That is funny. Generally I never use constants at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376145):
right, you shouldn't use constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376163):
@**Kevin Buzzard** You mean constant for types, right? Otherwise, how do you assume a relation is given to you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376512):
I never ever use constants. I would write something like `example (le : X -> X -> Prop) : blah`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376522):
@**Nima** you use variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376538):
Or `variable` yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376552):
I would use variables or the trick above for an abstract relation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376596):
For a "well-known" one like `le` I would use the type class system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376626):
Like this:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376674):
```
variables (X : Type) [has_le X]
variables (x y : X)
#check has_le.le x y
#check x ≤ y 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376689):
Making X an instance of class `has_le` enables me to use the notation `\leq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376695):
`\le` :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376696):
no way!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376706):
You'll be telling me I don't have to type `\forall` next

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376707):
I know the shortest code for the symbols I use :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376709):
`\fo`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376760):
I discovered that one because I once typed something like `\fo4all` followed by a space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376772):
and was like "wooah, it's magic"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376783):
"it worked anyway"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376817):
Back to the point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376872):
you can write `[H : has_le X]` if you want to give the construction a name. Otherwise it ends up being called something like `_inst_1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376882):
but most of the time you don't want to do that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376920):
Right, most of the time you want Lean to figure it out for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124377820):
Thanks, 
Would you please answer this one as well?
```quote
I know the following example can be solve by replacing the last line with `exact hm`. But why I receive a this error:
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124377930):
match is not a tactic. If you want to use it you have to say `exact match ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124377984):
When you write it there lean gets all sorts of confused in the parsing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378010):
also `match` requires `end` after it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378069):
@**Mario Carneiro** Awesome!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378075):
The tactic equivalent of `match` is `cases`, but I think you have already discovered this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 29 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378087):
so you could use `cases hm with m hh,` in place of the match line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124379367):
@**Mario Carneiro** Thanks a lot, I finally finished a proof! (super simple one, yet 65 lines!!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383712):
This is about ** coercions **
The first example in the following code works perfectly fine.
However, the second example cannot be type-checked. I know this direction in general is not possible. But this example, `trv α` contains all elements of `α`. So how should I prove the second example?
```
universe u
variables {α : Type u} [linear_order α]

inductive constraint (α:Type u) 
| trv                    : constraint
| stt (bnd:α) (low:Prop) : constraint
| nst (bnd:α) (low:Prop) : constraint

namespace constraint

def setof : constraint α → α → Prop := 
begin
  intros c a,
  cases c with bnd low bnd low,
    case trv         {exact true},
    case stt bnd low {exact low ∧ bnd<a ∨ ¬ low ∧ a < bnd},
    case nst bnd low {exact low ∧ bnd≤a ∨ ¬ low ∧ a ≤ bnd},
end

instance constraint_to_sort : has_coe_to_sort (constraint α) :=
  {S := Type u, coe := λ S, {x // setof S x}}

example : ∀ (c:constraint α) (a:c), setof c a := 
begin 
  intros c a,
  exact @subtype.property α (setof c) a
end

example : (∀ (a : (trv α)), ff) → ∀ a:α, ff :=
begin
  intros h a,
  exact h a
end

end constraint
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383739):
what is the intuition behind all these?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383794):
Using coercion we can say every natural number is a real number. But what if we know `r` is a real number `2`. How we can use it as a natural number.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383804):
what is trv stt nst?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383989):
Constructors of `constraint`. The code defines coercion from `constraint  α` to `α`. I am trying to go back from `α` to `constraint α`.  In the second example, `trv α` is a trivial constraint that is satisfied by every element of type `α`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384111):
btw `setof` doesn't type check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384152):
I copy pasted it from VSCode, it type checks perfectly fine.
Someone else told me if they remove `bnd` and `low` right after `case stt` and `case nst` they can compile it as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384192):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384196):
```
universe u
variables {α : Type u} [linear_order α]

inductive constraint (α:Type u)
| trv                    : constraint
| stt (bnd:α) (low:Prop) : constraint
| nst (bnd:α) (low:Prop) : constraint

namespace constraint

def setof : constraint α → α → Prop :=
begin
  intros c a,
  cases c with bnd low bnd low,
    case trv {exact true},
    case stt {exact low ∧ bnd<a ∨ ¬ low ∧ a < bnd},
    case nst {exact low ∧ bnd≤a ∨ ¬ low ∧ a ≤ bnd},
end

instance constraint_to_sort : has_coe_to_sort (constraint α) :=
  {S := Type u, coe := λ S, {x // setof S x}}

example : ∀ (c:constraint α) (a:c), setof c a :=
begin
  intros c a,
  exact @subtype.property α (setof c) a
end

example : (∀ (a : (trv α)), ff) → ∀ a:α, ff :=
begin
  intros h a,
  exact h ⟨a, trivial⟩
end

end constraint

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384198):
solution ^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384222):
also, I would avoid using any tactics in definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384230):
Thanks, so `trivial` is basically a proof that `a` is satisfied by `trv α`. Right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384300):
```quote
also, I would avoid using any tactics in definitions
```
"Fresh off the boat", so no idea what best practices are. Just trying to survive ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384333):
oh, ok, sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384399):
```
def setof : constraint α → α → Prop
| (trv α)       a := true
| (stt bnd low) a := low ∧ bnd<a ∨ ¬ low ∧ a < bnd
| (nst bnd low) a := low ∧ bnd≤a ∨ ¬ low ∧ a ≤ bnd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384477):
Cool, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 30 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124387596):
Is there any tactic that can push the negation inside quantifiers?
For example `¬  ∀ x,∃ y, p x y` should become `∃ x,∀ y, ¬ p x y`.
Using `classical` is fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124388893):
no. use a lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 30 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124389077):
@**Andrew Ashworth** You mean some lemma (probably two) twice. Right? I was looking for some tactic to push the negation all the way inside. Not sure how difficult it is to write such a tactic. I don't think writing a lemma is the solution, or at least I don't know how that can be done using a lemma such that one invocation of it will do the job.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124389453):
i mean, literally write a lemma stating ` ¬ ∀ x,∃ y, p x y ` iff ` ∃ x,∀ y, ¬ p x y `. Then rewrite with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 30 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124394062):
How do I find Lean version that is running online? I am using 3.3.0 (re-downloaded 5 minutes ago) and cannot typecheck the following code from Programming in Lean (the online Lean typechecks it):
```
import system.io
variable [io.interface]
open nat io

def print_squares : ℕ → io unit
| 0        := return ()
| (succ n) := print_squares n >>
              put_str (nat.to_string n ++ "^2 = " ++ 
                       nat.to_string (n * n) ++ "\n")

#eval print_squares 100
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124394417):
The latest version of lean doesn't use `io.interface`. Try removing that line and the rest should work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 30 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124394471):
Removing that adds to error.  The current error I am receiving is ` unknown identifier 'nat.to_string' `.
If it is of any help, I am on Mac and downloaded the binary version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124395469):
Looks like it's just `to_string` now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124395480):
what did I just see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124395481):
is Lean basically python now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396126):
i think there's room to add more handy programming gadgets once lean 4 rolls around and we can extend the parser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396196):
`map (fun x -> x * x) [0 .. 10] = [0, 1, 4, 9, 16, 25, 36, 49, 56, 64, 81, 100]` would be sweet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396199):
we already have list.map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396203):
you can't write `[0 .. 10]` right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396204):
list.range

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396214):
or more generally `[0 .. 2 .. 10]` where you can supply a step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396257):
aha, that's not quite so simple to declare with a `notation` command

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396269):
```
import system.io

open nat io

def print_fib_core : ℕ → ℕ × ℕ × io unit
| 0        := (0, 1, return ())
| (succ n) := let (a, b, c) := print_fib_core n in
              (b, a+b, c >>
                  put_str ("fib " ++ to_string n ++ " = " ++
                       to_string a ++ "\n"))

def print_fib : ℕ → io unit :=
λ n, (print_fib_core n).2.2

#eval print_fib 100

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396274):
```
fib 0 = 0
fib 1 = 1
fib 2 = 1
fib 3 = 2
fib 4 = 3
fib 5 = 5
fib 6 = 8
fib 7 = 13
fib 8 = 21
fib 9 = 34
fib 10 = 55
[...]
fib 90 = 2880067194370816120
fib 91 = 4660046610375530309
fib 92 = 7540113804746346429
fib 93 = 12200160415121876738
fib 94 = 19740274219868223167
fib 95 = 31940434634990099905
fib 96 = 51680708854858323072
fib 97 = 83621143489848422977
fib 98 = 135301852344706746049
fib 99 = 218922995834555169026

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396276):
cool, now I can do Project Euler with it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396325):
this is ridiculous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396360):
project euler in a functional language is painful, but that's probably because i don't speak monad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396406):
you only need `io unit` :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 30 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396431):
@**Kenny Lau** Thank you, it worked (I still need ` variable [io.interface]`, but it works)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396472):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396942):
I get ` VM does not have code for 'unsafe_monad_from_pure_bind' ` when I try to run that code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396946):
which code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396991):
your fib code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396992):
what is your lean version?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396995):
```
Lean (version 3.3.1, commit 28f4143be31b, RELEASE)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396996):
28f414

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396998):
wow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397036):
what does that mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397039):
same as yours, evidently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397111):
I can't even find`unsafe_monad_from_pure_bind` in the lean repo, it's a mystery where that comes from

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397117):
meh, restart and it's fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397125):
what is the intended use for bit0 and bit1?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397127):
can I use them in recursion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397368):
Here's my version of the fib printer:
```  
def fib_core : ℕ → ℕ × ℕ
| 0        := (0, 1)
| (succ n) := let (a, b) := fib_core n in (b, a+b)

def fib (n) := (fib_core n).1

def print_fib (n : ℕ) : io unit :=
(list.range 100).mmap' (λ n,
  put_str ("fib " ++ to_string n ++ " = " ++
    to_string (fib n) ++ "\n"))

#eval print_fib 100
```
It's asymptotically slower than Kenny's version since it recomputes `fib` rather than calculating as it goes, but this is a bit closer to what you would expect in another programming language without any fancy tricks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397445):
`bit0` and `bit1` are used by the parser to construct natural number literals and other number literals like `7`, which is actually `bit1 (bit1 (bit1 1)))` in whatever type (it must have typeclasses for `has_add` and `has_one`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397459):
If you want to define a function by binary recursion over `nat`, use `nat.binary_rec_on`, which uses `bit b n` which generalizes `bit0` and `bit1` with a boolean bit parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397505):
```
def list.update {α : Type*} : list α → list nat → α → list α
| L []     x := L
| L (h::t) x := (L.update t x).update_nth h x

namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) > sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 < n then
         (aux1 n (isqrt (n / 4) * 2))
       else n

def aux2 : list bool → nat → nat → list bool :=
λ L len n, L.update (list.map (λ z, (z + n) * n) (list.range $ len / n)) ff

def aux3 : list bool → nat → nat → list bool
| L len 0     := L
| L len 1     := L
| L len (n+1) := aux2 (aux3 L len n) len (n+1)

def aux4 : nat → list bool :=
λ n, aux3 (list.repeat tt n) n (isqrt n)

def aux5 : list bool → nat → list nat :=
λ L n, (list.range n).filter $ λ z, L.nth z = tt

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, (eratosthenes.aux5 (eratosthenes.aux4 n) n).drop 2

#eval eratosthenes 1000

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397508):
why is this so slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397558):
geez, name your stuff better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397560):
well I don't intend to PR it :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397565):
it's like reading decompiled sources

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397566):
oh, sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397567):
aux1 is for isqrt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397568):
heh, sieve of e

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397569):
aux2 does one sieve

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397570):
https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397571):
What's the anticipated order?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397611):
of what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397613):
of the code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397615):
it sieves sqrt(n) times

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397616):
each time taking n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397619):
I think it's O(n^1.5) then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397620):
I see several quadratic passes at least

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397621):
where is the quadratic pass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397628):
`(list.range n).filter $ λ z, L.nth z = tt` passes over `L` for each `n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397638):
oh, how should I fix that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397639):
ah, I should deconstruct the list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397640):
paper i linked discusses the sieve in a functional setting exhaustively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397681):
You should put comments or something, it's not obvious what the auxes do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397689):
should I implement the code form your paper?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397730):
i mean, if you want a functional Sieve of Eratosthenes , that is also pretty fast, yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397735):
does it use data structures that I don't have?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397738):
PriorityQ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397777):
this is getting a bit out of hand, but you could implement one from okasaki's "purely functional data structures"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397780):
Yeah, we don't have that, maybe `rb_map` will work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397784):
Beware, Okasaki assumes a `susp` type (aka memoization), but we don't have one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397828):
hm. then i'd use the red-black tree in lean core for everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397833):
You actually could make your original code a lot faster simply by using arrays instead of lists. You are using them like arrays anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397834):
and that will make `L.nth` asymptotically fast

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397874):
I've never used array :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397875):
I don't even know arrays exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397896):
`array` is like `vector`, it's a list with a fixed (in the type) size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397938):
and importantly, it's implemented as an C++ array, meaning that updates and nth are fast

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397993):
can I trace the function calls? i.e. debugging?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397996):
is vector a dynamically growing array under the hood?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398049):
... i wonder how much work it would take to use a dynamically growing array for lean's list impl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398148):
`vector` is literally just a subtype of `list`. `array` is isomorphic to `vector`, and is implemented as the `parray` type in C++, which is a C++ array with some added support for end extension and persistent usage

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398220):
ahh, i see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398431):
```
def list.update {α : Type*} : list α → list nat → α → list α
| L []     x := L
| L (h::t) x := (L.update t x).update_nth h x

def list.extract {α : Type*} [decidable_eq α] : list α → nat → α → list nat
| L      0     x := []
| []     (n+1) x := []
| (h::t) (n+1) x := if h = x then n :: t.extract n x else t.extract n x

namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) > sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 < n then aux1 n (isqrt (n / 4) * 2) else n

-- from L, make every n-th item false
def step : list bool → nat → nat → list bool :=
λ L len n, L.update (list.map (λ z, (z + n) * n) (list.range $ len / n)) ff

-- do "step" for every integer from 2 to n
def sieve : list bool → nat → nat → list bool
| L len 0     := L
| L len 1     := L
| L len (n+1) := if L.nth (n+1) = tt then step (sieve L len n) len (n+1) else sieve L len n

-- invoke sieve with sqrt(n)
def prime.bool : nat → list bool :=
λ n, sieve (list.repeat tt n) n (isqrt n)

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, ((eratosthenes.prime.bool n).reverse.extract n tt).reverse.drop 2

#eval eratosthenes 1000

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398434):
@**Mario Carneiro** what do you think is the complexity of this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398474):
ah, I see a quadratic pass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398480):
`L.update` is quadratic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398481):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398484):
I think you should define `step` by recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398494):
it shouldn't be hard to make every `n`th item false by keeping an accumulator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398539):
You can't do `step` in less than O(n) time with this data structure, so `sieve` is necessarily O(n^2)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398540):
what do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398547):
`step` has to walk down the entire list to change stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398551):
but I only need to call step `sqrt(n)` times

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398592):
Ah, that's true. So n^1.5 seems likely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398597):
As that paper will tell you though, this isn't "true" eratosthenes since you have to visit all the skipped entries multiple times

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398599):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398639):
well that paper is too technical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398687):
it's O(n^1.5) now, empirically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398688):
because I can do 10000 now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398691):
(how pathetic)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398692):
```
def list.extract {α : Type*} [decidable_eq α] : list α → nat → α → list nat
| L      0     x := []
| []     (n+1) x := []
| (h::t) (n+1) x := if h = x then n :: t.extract n x else t.extract n x

namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) > sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 < n then aux1 n (isqrt (n / 4) * 2) else n

-- from L, make every n-th item false
def step : list bool → nat → nat → list bool :=
λ L n start, L.enum.map (λ z, if z.1 % n = 0 ∧ start ≤ z.1 then ff else z.2)

-- do "step" for every integer from 2 to n
def sieve : list bool → nat →list bool
| L 0     := L
| L 1     := L
| L (n+1) := if L.nth (n+1) = tt then step (sieve L n) (n+1) ((n+1)*(n+1)) else sieve L n

-- invoke sieve with sqrt(n)
def prime.bool : nat → list bool :=
λ n, sieve (list.repeat tt n) (isqrt n)

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, ((eratosthenes.prime.bool n).reverse.extract n tt).reverse.drop 2

#eval eratosthenes 10000

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398695):
now I'm going to redo it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398698):
i.e. use `list nat` instead of `list bool`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398701):
and use accumulator instead of mod

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398704):
well, that paper has a list based implementation on page 11

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398743):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398745):
but, you'll need a lazy sequence type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398746):
coinduction is coming soon, I hope :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398747):
i don't know if lean supports lazy semantics right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398749):
we already have stream

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398750):
but I don't know how computable it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398751):
Seriously, use `array`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398757):
if you care about speed, use `array`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398760):
linked lists are known horrible in almost all cases in CS theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398802):
`stream` exists and is computable, but is not remotely efficient as a stream

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398808):
the hard part about making that paper applicable in lean is all the tricks used to take advantage of laziness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398847):
AFAIK there are no plans to make lean lazy. You can manually add laziness using `thunk`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398849):
yeah, it's unfortunate that the most popular pure functional language emphasizes laziness so much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398853):
it's really hard to move code snippets and ideas over

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398857):
ML is a good functional strict language, but I find it often does too much impure stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398859):
that's a benefit :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398860):
(i use f# when i can)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398899):
In the sense that it makes it difficult to transfer ideas over

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398907):
i haven't tried to do much imperative programming in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 30 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398909):
is it hard to emulate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399059):
now it's much faster!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399060):
```
namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) > sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 < n then aux1 n (isqrt (n / 4) * 2) else n

-- from L, remove every item divisible by n
def step : list nat → nat → list nat
| []     n := []
| (h::t) n := if h%n = 0 then step t n else h::step t n

-- each time : remove one element, do step on that element
def sieve : nat → list nat → list nat
| hi []     := []
| hi (h::t) := if h ≤ hi then (h::step t h) else (h::t)

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, eratosthenes.sieve (eratosthenes.isqrt n) ((list.range n).drop 2)

#eval eratosthenes 10000

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399219):
I think `step` can be expressed as a `list.filter` without a performance hit with this approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399222):
Isn't `sieve` recursive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399244):
yes, I just discovered the bug xd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399282):
now Lean doesn't trust that my recursion is well-founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399283):
I can't be bothered to prove that to Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399284):
so, see you :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399694):
```
namespace eratosthenes

-- O(1)
def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) > sq then lo else lo+1

-- O(log n)
def isqrt : nat → nat
| n := if H : n / 4 < n then aux1 n (isqrt (n / 4) * 2) else n

-- O(n)
-- from L, remove every item divisible by n
def step : list nat → nat → list nat
| []     n := []
| (h::t) n := if h%n = 0 then step t n else h::step t n

theorem aux (t : list nat) (h : nat) : list.sizeof (step t h) ≤ list.sizeof t :=
begin
  induction t with h1 t1 ih,
  { dsimp [step],
    refl },
  { dsimp [step],
    by_cases H : h1 % h = 0,
    { simp [H, list.sizeof],
      apply le_trans ih,
      apply le_trans (nat.le_add_right _ (sizeof h1)),
      exact nat.le_add_left _ _ },
    { simp [H, list.sizeof],
      apply nat.add_le_add_left,
      rw add_comm,
      apply nat.add_le_add_right,
      exact ih } }
end

theorem aux2 (t : list nat) (h : nat) : has_well_founded.r (step t h) (h :: t) :=
begin
  dsimp [has_well_founded.r, sizeof_measure, measure, inv_image, sizeof, has_sizeof.sizeof, list.sizeof],
  apply lt_of_le_of_lt (aux t h),
  apply nat.lt_add_of_pos_left,
  rw add_comm,
  exact nat.zero_lt_succ _
end

-- O(n^1.5)
-- each time : remove one element, do step on that element
def sieve (hi : nat) : list nat → list nat
| []     := []
| (h::t) := if h ≤ hi then (h::(sieve $ step t h)) else (h::t)
using_well_founded { dec_tac := `[exact aux2 t h] }

end eratosthenes

-- O(n^1.5)
def eratosthenes : nat → list nat :=
λ n, eratosthenes.sieve (eratosthenes.isqrt n) ((list.range n).drop 2)

#eval eratosthenes 10000

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399696):
@**Mario Carneiro** I lied

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399751):
If you used `filter` for `step`, the lemma would be easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400262):
btw it can handle `100000` now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400366):
@**Mario Carneiro** I don't see what difference it makes. It isn't a lemma that L.filter p has size at most L

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400386):
It's a sublist from `filter_sublist`, and sublist implies length less equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400388):
so how exactly would I prove its well-foundedness?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124401268):
```
def step (L : list nat) (n : nat) : list nat :=
L.filter (λ a, a%n ≠ 0)

def sieve (hi : nat) : list nat → list nat
| []     := []
| (h::t) :=
  have (step t h).length < (h :: t).length, from
  lt_succ_of_le $ list.length_le_of_sublist $ list.filter_sublist _,
  if h ≤ hi then h::sieve (step t h) else h::t
using_well_founded {
  rel_tac := λ _ _, `[exact ⟨_, measure_wf list.length⟩],
  dec_tac := `[exact this] }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124401276):
oh, changing the relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 30 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124401277):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436819):
The following is from Programming in Lean and works perfectly fine in the online Lean. Any idea how I should make it also work in version 3.3.0?
```
open expr tactic classical

meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do try (simp_at hyp lemmas)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436867):
what errors are you encountering?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436869):
```
sandbox3.lean:6:3: error

don't know how to synthesize placeholder
context:
lemmas : list expr,
hyp : expr,
normalize_hyp : tactic unit
⊢ Type ?


sandbox3.lean:6:8: error

unknown identifier 'simp_at'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436964):
Yes, those errors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437019):
Can you try `simp_hyp` instead of `simp_at`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437022):
```
type mismatch at application
  simp_hyp hyp
term
  hyp
has type
  expr
but is expected to have type
  simp_lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437257):
ok, first, swap the order of the arguments: ` simp_hyp lemmas hyp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437259):
second, let's construct a `simp_lemmas`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437309):
```
meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s <- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_at s hyp) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437406):
`simp_at`(`unknown identifier`)?
If I use `simp_hyp` give me the same error
```
type mismatch at application
  simp_hyp hyp
term
  hyp
has type
  expr
but is expected to have type
  simp_lemmas 
Additional information:
/Users/nima/Dropbox/Codes/Lean/Interval/tmp.lean:5:8: context: switched to simple application elaboration procedure because failed to use expected type to elaborate it, error message
  type mismatch, term
    (simp_hyp ?m_1 ?m_2 h
       {max_steps := simp.default_max_steps,
        contextual := ff,
        lift_eq := tt,
        canonize_instances := tt,
        canonize_proofs := ff,
        use_axioms := tt,
        zeta := tt,
        beta := tt,
        eta := tt,
        proj := tt,
        iota := tt,
        single_pass := ff,
        fail_if_unchanged := tt,
        memoize := tt})
  has type
    expr → tactic expr : Type
  but is expected to have type
    tactic ?m_1 : Type ? 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437425):
Sorry, the second version was wrong. I fixed it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437594):
Is there any lean file that I can download from github to have the fix?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437603):
I mean, this is what it should be:

```
meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s <- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_at s hyp) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437655):
but `simp_at` gives me `unknown identifier 'simp_at' ` error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437699):
Sorry I keep making the same typo:

```
meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s <- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_hyp s hyp) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437706):
This gives me the following error:
```
type mismatch at application
  simp_hyp s hyp
term
  hyp
has type
  expr
but is expected to have type
  opt_param (list name) list.nil
Additional information:
/Users/nima/Dropbox/Codes/Lean/Interval/tmp.lean:5:8: context: switched to simple application elaboration procedure because failed to use expected type to elaborate it, error message
  type mismatch, term
    (simp_hyp ?m_1 ?m_2 h
       {max_steps := simp.default_max_steps,
        contextual := ff,
        lift_eq := tt,
        canonize_instances := tt,
        canonize_proofs := ff,
        use_axioms := tt,
        zeta := tt,
        beta := tt,
        eta := tt,
        proj := tt,
        iota := tt,
        single_pass := ff,
        fail_if_unchanged := tt,
        memoize := tt})
  has type
    expr → tactic expr : Type
  but is expected to have type
    tactic ?m_1 : Type ? 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437753):
that's progress

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437795):
How about

```
meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s <- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_hyp s [] hyp) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437842):
Wow! Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437851):
No problems. Sorry for the excessive back and forth.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437890):
I don't see `simp_at` in the lean web editor either. Is it in 3.3.0?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437950):
No problem at all.
I don't know how to check Lean version, mine is supposed to be 3.3.0.
The same chapter gives me error. 
Last line ` unknown identifier 'monad.for''`
Is there a magic fix for this one as well?
```quote
The for' tactic, like the for tactic, applies the second argument to each element of the first, but it returns unit rather than accumulate the results in a list. 
```

```
open expr tactic classical monad

meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s <- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_hyp s [] hyp)

meta def normalize_hyps : tactic unit :=
do hyps ← local_context,
   lemmas ← monad.mapm mk_const [``not_not_intro],
   monad.for' hyps (normalize_hyp lemmas)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437965):
```quote
I don't see `simp_at` in the lean web editor either. Is it in 3.3.0?
```
It disappeared in https://github.com/leanprover/lean/commit/69ed291aab8493a7fb33b52dc2982e2db417761f
in July

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437997):
@**Nima** you can check your version with `lean --version`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438043):
Instead of ` monad.for' hyps (normalize_hyp lemmas) ` try `hyps.mmap' (normalize_hyp lemmas)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438094):
Fantastic!
Thanks a lot,
Also, my version is `Lean (version 3.3.0, commit fa9c868ed2bb, Release)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438145):
Yeah, that's exactly 3.3.0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438148):
Programming in Lean seems to be working with a pretty old version of Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442486):
Sorry if this is too stupid, but why the following does not type-checks (I don't care the example itself) :
```
universe u
variable {α : Type u}
example (p:α → Prop) : (¬(∃ (a:α), ¬ p a)) → (∀ (a:α), p a) :=
begin
  intros h a,
  have h' : (p a) → p a,
  from admit,
  admit
end
```
I get the following error at `have`
```
type mismatch at application
  p a
term
  a
has type
  p a : Prop
but is expected to have type
  α : Type u
state:
α : Type u,
p : α → Prop,
h : ¬∃ (a : α), ¬p a,
a : α
⊢ p a 
```
This is Tactic State right before `have`
```
α : Type u,
p : α → Prop,
h : ¬∃ (a : α), ¬p a,
a : α
⊢ p a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442534):
That's puzzling

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442585):
You can't `from admit`, `admit` is a tactic not a term. Use `from sorry` or just `admit`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442624):
Dang! I completely missed that!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442625):
But the error is actually an issue with the variable `a` together with `p -> q` instead of `\forall (_ : p), q`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442632):
So the following change gives me the same error:
```
have h' : (p a) → (p a),
  admit,
  admit
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442672):
https://github.com/leanprover/lean/issues/1822

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442673):
Oooooooh! I had to stare a it for a while. I almost bore a whole through my monitor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442681):
You can work around the issue by writing `∀_:p a, p a` instead of `p a -> p a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442682):
or use a variable other than `a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442723):
Is there any plan to change that horrible convention to name that bound variable `a`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442724):
I think? There are two separate autonaming approaches, one produces `a_n` and the other produces `_x_n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442729):
The underscore trick switches to the other naming convention

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442731):
But it's never as simple as it seems for this stuff. See the issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442770):
also https://github.com/leanprover/lean/pull/1844

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442778):
Yeah, don't I know it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442779):
Looks like Leo wanted to postpone a fix because of the new parser (sigh...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442780):
Thanks for the link

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442822):
I've heard that song before :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442823):
Here's hoping that the new parser also cures cancer :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442824):
but don't bother with any medicine or chemotherapy in the meantime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442829):
oh, what does double colon mean? as in, `{x : : p a}` something like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442830):
that's malformed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442869):
https://github.com/leanprover/mathlib/pull/88#discussion_r178095763

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442871):
```quote
what about `def next.fixed_point {x : : α} (H : x ≤ f x) : fixed_point` (in similar for previous) then you can shorten some proofs below.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442872):
looks like a typo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442874):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443018):
> But the error is actually an issue with the ...

@**Mario Carneiro** I only understood that part, but it worked. So thank you  :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443076):
Basically, `have h' : (p a) → p a,` is the same as `have h' : ∀ a : p a, p a,` so the first `a` has type ` α` and the second one has type `p a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443709):
Thanks for the clarification,
Some of the discussion on those links were about how Lean should choose name of the bounded variable in `∀ a : p ...`. Right? (I mean is it always `a` or starts with `a`, so if I don't start names with `a` then I will never see this problem again?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443809):
Yes. Ideally it should be chosen to be distinct from the variables on the RHS, but for some reason this is complicated, so it just uses a name generator and you the user are responsible for not choosing the same name. You should beware of naming your variables `a`, `a_1`, `a_2` etc. as well as `_x`, `_x_1`, `_x_2` etc. Also `_inst` and `_match` and other underscore names are taken, so you should avoid starting your variables with an underscore.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447155):
```
has type
  α → α → Prop : Type u
but is expected to have type
  α → α → Type ? : Type (max u (?+1))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447156):
is Prop not a type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447161):
btw `plift` seems to have resolved the error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447207):
Prop is a Type, but Prop is not Type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447211):
Prop is Type 0, no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447214):
Prop is Sort 0, Type u is Sort (u+1)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447215):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447258):
```
don't know how to synthesize placeholder
context:
α : Type u,
_inst_1 : partial_order α,
x y : α,
hxy : plift (x ≤ y)
⊢ {down := le_trans (hxy.down) ({down := le_refl y}.down)} = hxy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447262):
proof irrelevance after plift...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447269):
you have to case on `hxy` first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447308):
or rewrite with `plift.up_down`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447315):
`congr_arg plift.up rfl` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447316):
after casing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447317):
` λ x y ⟨hxy⟩, congr_arg plift.up rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447318):
but `rfl` doesn't?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447354):
I'm stupid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447355):
it does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447362):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447363):
it goes assertion error without the casing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447364):
but I've been getting too many assertion errors I decided to stop caring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447372):
hm, that's not a place I've seen an assertion error before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447461):
is there polymorphic empty type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447507):
```
def empty : category empty :=
{ Mor := empty.rec _,
  Comp := empty.rec _,
  Id := empty.rec _,
  Hid_left := empty.rec _,
  Hid_right := empty.rec _,
  Hassoc := empty.rec _ }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447508):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447548):
Surprisingly no. You can use `ulift empty` in a pinch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447555):
and yes, I'm doing category theory again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447600):
`λ x y z, unit.cases_on z rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447601):
is there a way to case on `z` in the lambda part?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447641):
```
def one : category unit :=
{ Mor := λ _ _, unit,
  Comp := λ _ _ _ _ _, unit.star,
  Id := λ _, unit.star,
  Hid_left := λ _ _, unit.rec rfl,
  Hid_right := λ _ _, unit.rec rfl,
  Hassoc := λ _ _ _ _ _ _ _, rfl }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447688):
you can write `()` in the lambda I think, or `⟨⟩`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447693):
the latter works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447782):
```
def of_monoid (α : Type u) [monoid α] : category unit :=
{ Mor := λ _ _, α,
  Comp := λ _ _ _, (*),
  Id := λ _, 1,
  Hid_left := λ _ _, one_mul,
  Hid_right := λ _ _, mul_one,
  Hassoc := λ _ _ _ _, mul_assoc }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447783):
how beautifully the structures are compatible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447841):
```
def of_monoid (α : Type u) [monoid α] : category unit :=
{ Mor := λ _ _, α,
  Comp := λ _ _ _, (*),
  Id := λ _, 1,
  Hid_left := λ _ _, one_mul,
  Hid_right := λ _ _, mul_one,
  Hassoc := λ _ _ _ _, mul_assoc }

def to_monoid (C: category unit) : monoid (C.Mor () ()) :=
{ mul := C.Comp _ _ _,
  mul_assoc := C.Hassoc () () () (),
  one := C.Id (),
  one_mul := C.Hid_left () (),
  mul_one := C.Hid_right () () }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447878):
this is very beautiful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447888):
I think you can do better in that last one... in any category, the homs from an object to itself forms a monoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447931):
```
def to_monoid {α : Type u} (C: category α) (x : α) : monoid (C.Mor x x) :=
{ mul := C.Comp _ _ _,
  mul_assoc := C.Hassoc x x x x,
  one := C.Id x,
  one_mul := C.Hid_left x x,
  mul_one := C.Hid_right x x }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447932):
done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447974):
I just realized the forgetful functor and its adjoint exists in Cat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448020):
now `one` is a special case of `discrete`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448021):
```
def discrete (α : Type u) : category α :=
{ Mor := λ _ _, unit,
  Comp := λ _ _ _ _ _, (),
  Id := λ _, (),
  Hid_left := λ _ _ ⟨⟩, rfl,
  Hid_right := λ _ _ ⟨⟩, rfl,
  Hassoc := λ _ _ _ _ _ _ _, rfl }

def one : category unit :=
discrete unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448022):
ok technically zero also, but...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448023):
```
def discrete (α : Type u) : category α :=
{ Mor := λ _ _, unit,
  Comp := λ _ _ _ _ _, (),
  Id := λ _, (),
  Hid_left := λ _ _ ⟨⟩, rfl,
  Hid_right := λ _ _ ⟨⟩, rfl,
  Hassoc := λ _ _ _ _ _ _ _, rfl }

def zero : category empty :=
discrete empty

def one : category unit :=
discrete unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448158):
@**Mario Carneiro**  how would you call the category `* -> *` and the category `* => *`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448159):
(one arrow, two arrows)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448161):
what do they mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448162):
the former is the category with 2 objects and 3 morphisms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448202):
that's `two`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448203):
and the latter is with 4 morphisms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448205):
`two'`? `two_eq` (since it's the equalizer diagram)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448210):
so it doesn't have a name in convention?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448212):
I've never seen it have an official name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448213):
yes, I meant official. words.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448250):
maybe `equalizer_diagram` lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448259):
Alternatively `two_mor` since it's the canonical two morphism diagram

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448260):
what do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448261):
and how are you going to name the pullback diagram

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448300):
`three_in` and `three_out`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448301):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448302):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448348):
```
def Mor : bool → bool → Type
| ff ff := unit
| ff tt := bool
| tt ff := empty
| tt tt := unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448349):
do you want to switch `bool` and `empty`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448398):
Hm, that seems a bit painful to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448400):
how would you do it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448441):
```
def Mor : bool → bool → Type
| ff ff := unit
| ff tt := bool
| tt ff := empty
| tt tt := unit

def Comp : Π x y z : bool, Mor y z → Mor x y → Mor x z
| ff ff ff _ g := g
| ff ff tt f _ := f
| ff tt tt _ g := g
| tt tt tt _ _ := ()

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448446):
```
inductive Mor : bool → bool → Type
| id : ∀ b, Mor b b
| par : bool → Mor ff tt
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448452):
heh...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448454):
what does `par` stand for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448455):
parallel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448456):
making up names is hard...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448496):
eu entendo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448540):
It might be worth generalizing this example to a whole bouquet of parallel arrows indexed by `A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448542):
fair enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448543):
would you like to do the hard job of naming it for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448544):
`par` :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448545):
wonderful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448546):
```
inductive Mor : bool → bool → Type
| id : ∀ b, Mor b b
| par : bool → Mor ff tt

def Comp : Π x y z : bool, Mor y z → Mor x y → Mor x z
| ff ff _  f _ := f
| _  tt tt _ g := g

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448549):
two cases!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448782):
```
namespace par

variable α : Type u

inductive Mor : bool → bool → Type u
| id : ∀ b, Mor b b
| par : α → Mor ff tt

def Comp : Π x y z, Mor α y z → Mor α x y → Mor α x z
| ff ff _  f _ := f
| _  tt tt _ g := g

def Hid_left : ∀ x y f, Comp α x y y (Mor.id α y) f = f
| ff ff (Mor.id α b) := rfl
| ff tt _ := rfl
| tt tt (Mor.id α b) := rfl

def Hid_right : ∀ x y f, Comp α x x y f (Mor.id α x) = f
| ff ff (Mor.id α b) := rfl
| ff tt _ := rfl
| tt tt (Mor.id α b) := rfl

def Hassoc : ∀ x y z w f g h, Comp α x y w (Comp α y z w f g) h = Comp α x z w f (Comp α x y z g h)
| ff ff _  _  _ _ _ := rfl
| ff tt tt tt _ _ _ := rfl
| tt tt tt tt _ _ _ := rfl

end par

def par (α : Type u) : category bool :=
{ Mor := par.Mor α,
  Comp := par.Comp α,
  Id := par.Mor.id α,
  Hid_left := par.Hid_left α,
  Hid_right := par.Hid_right α,
  Hassoc := par.Hassoc α }

def two_mor : category bool :=
par bool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448783):
@**Mario Carneiro** do you see any possible golf on the casings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448833):
I sometimes use secondary cases when a bunch of cases are the same; there isn't too much of that in this example but you could write `Hassoc` as
```
def Hassoc : ∀ x y z w f g h, Comp α x y w (Comp α y z w f g) h = Comp α x z w f (Comp α x y z g h)
| ff ff _  _  _ _ _ := rfl
| b tt tt tt _ _ _ := by cases b; refl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448872):
well...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448874):
that tactic was |unnecessary|

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448879):
The advantage really shows itself when you need to deal with a wildcard case which abbreviates five identical cases with five identical proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448880):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448921):
it doesn't make the generated proof any shorter, but it's a slightly neater arrangement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448922):
```
structure category (α : Type u) : Type (max u v + 1) :=
(Mor : Π x y : α, Type v)
(Comp : Π x y z, Mor y z → Mor x y → Mor x z)
(Id : Π x, Mor x x)
(Hid_left : ∀ x y (f : Mor x y), Comp _ _ _ (Id _) f = f)
(Hid_right : ∀ x y (f : Mor x y), Comp _ _ _ f (Id _) = f)
(Hassoc : ∀ x y z w (f : Mor z w) (g : Mor y z) (h : Mor x y), Comp _ _ _ (Comp _ _ _ f g) h = Comp _ _ _ f (Comp _ _ _ g h))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448923):
I run into type problem when I try to define a cone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448924):
namely, option

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448929):
the problem is the type of the morphism...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448930):
I was thinking about doing the same for the `Mor.id` cases in `Hid_left` and such but you need the cases there so that the `ff tt` case works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448973):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448974):
```
def Mor : option α → option α → Type u_1
| none none := punit
| none (some y) := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448975):
how the hell does this work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448977):
```
variables {α : Type u} (C : category α)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448978):
what's the problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448979):
this is amazing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448980):
I never defined `u_1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448982):
it comes with `C`, but I never gave it a name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448987):
yeah, it's a really thin abstraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448988):
how does it work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448990):
also why `variables A B : Sort*` doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448991):
it's unprecedented, the ability to have an unnamed name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449030):
Whenever you have a free universe variable in a `variable` declaration, it adds a `universe u_n` definition to the file and uses that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449031):
it's not magically named or a metavariable or anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449049):
```
inductive Mor : option α → option α → Type (max u u_1)
| id : ∀ y, Mor none y
| mor : ∀ x y (f : C.Mor x y), Mor (some x) (some y)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449050):
why do I need `max` here but not that one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449052):
```
def Mor : option α → option α → Type u_1
| none none := punit
| none (some y) := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449108):
I don't recommend using `u_1`, you should name your variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449109):
how would I do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449111):
`universes u v`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449150):
no...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449153):
```
structure category (α : Type u) : Type (max u v + 1) :=
(Mor : Π x y : α, Type v)
(Comp : Π x y z, Mor y z → Mor x y → Mor x z)
(Id : Π x, Mor x x)
(Hid_left : ∀ x y (f : Mor x y), Comp _ _ _ (Id _) f = f)
(Hid_right : ∀ x y (f : Mor x y), Comp _ _ _ f (Id _) = f)
(Hassoc : ∀ x y z w (f : Mor z w) (g : Mor y z) (h : Mor x y), Comp _ _ _ (Comp _ _ _ f g) h = Comp _ _ _ f (Comp _ _ _ g h))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449154):
I can't name it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449155):
it comes with the `Mor` of the category variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449156):
```
variables {α : Type u} (C : category α)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449157):
You can write universe arguments of a constant explicitly with `category.{u v}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449162):
oh worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449215):
```
inductive Mor : option α → option α → Type (max u v)
| id : ∀ y, Mor none y
| mor : ∀ x y (f : C.Mor x y), Mor x y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449216):
@**Mario Carneiro** the name `id` is morally wrong; how would you name it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449217):
maybe `proj`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449258):
you should use `some` instead of the coercion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449259):
like you were before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449262):
```
inductive Mor : option α → option α → Type (max u v)
| proj : ∀ y, Mor none y
| mor : ∀ x y (f : C.Mor x y), Mor (some x) (some y)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449263):
this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449266):
komu eesu?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449267):
maybe just `none_le` or something like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449268):
i don't like thinking it in a poset-manner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449269):
about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449314):
I think this one should be defined with a `def`; that will fix the universe `max` thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449315):
what do you mean by "fix", is it a bug?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449355):
The problem is that lean isn't smart enough to notice that the `∀ y` in proj only fills out one morphism per type in the family

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449360):
If you just try to push it all in a single inductive type, it overestimates the best universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449489):
```
def Mor : option α → option α → Type v
| none none := punit
| none (some y) := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y

def Comp : Π x y z, Mor C y z → Mor C x y → Mor C x z
| none none _ f _ := f
| none _ (some z) _ _ := punit.star
| (some x) (some y) (some z) f g := C.Comp x y z f g

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449490):
the sky is blue again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449496):
@**Mario Carneiro** what next, are you going to tell me that you can generalize `option` to `sum`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449536):
```
def Mor : option α → option α → Type v
| none     y        := punit
| _        none     := ulift empty
| (some x) (some y) := C.Mor x y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449537):
ok thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449543):
ok it's really 3 equations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449544):
You can generalize option to sum, there are two interesting structures there - disjoint union and union where the left objects have morphisms to the right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449586):
but `option` is nicer to use than `sum punit`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449587):
```
def Mor : option α → option α → Type v
| none y := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y

/-
._eqn_1 : ∀ {α : Type u} (C : category α) (y : option α), Mor C none y = punit
._eqn_2 : ∀ {α : Type u} (C : category α) (x : α), Mor C (some x) none = ulift empty
._eqn_3 : ∀ {α : Type u} (C : category α) (x y : α), Mor C (some x) (some y) = C.Mor x y
-/

def Mor : option α → option α → Type v
| none y := punit
| _ none := ulift empty
| (some x) (some y) := C.Mor x y

/-
._eqn_1 : ∀ {α : Type u} (C : category α), Mor C none none = punit
._eqn_2 : ∀ {α : Type u} (C : category α) (val : α), Mor C none (some val) = punit
._eqn_3 : ∀ {α : Type u} (C : category α) (val : α), Mor C (some val) none = ulift empty
._eqn_4 : ∀ {α : Type u} (C : category α) (x y : α), Mor C (some x) (some y) = C.Mor x y
-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449592):
por que pasa isso

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449594):
ok I know why I'm just exclaiming

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449633):
¡

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449678):
pojish einteindeh si eu falu assii?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449685):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449722):
your portuguese is getting harder to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449725):
:P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449727):
"podes entender se eu falo assim"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449736):
I think Nima had a similar issue the other day

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449737):
not understanding my portuguese?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449774):
something about the order of case splits causing superfluous splitting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449778):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449780):
I could do disjoint union

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449782):
but I don't think there's this notion in the category theory community?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449789):
Have you coordinated with Scott?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449790):
I mean, it is probably some universal objects in the category of categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449791):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449792):
The disjoint union is certainly the coproduct in Cat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449793):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449876):
is there a shorthand for `punit.star`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450072):
why does `#check  Type  1000000` crash?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450073):
no, although you could open `punit`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450110):
lol stop breaking lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450113):
I mean, it should be just a construct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450114):
unless you're telling me that it creates an array with a million entries

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450115):
but most of them should be just empty?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450116):
I think it does something by recursion a million times and busts the stack

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450118):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450123):
Is there a general construction that abstracts "from set to pointed set"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450186):
oh, it's just the coslice category isn't it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124451065):
```
def Cat : category Σ α : Type u, category.{u v} α :=
{ Mor := λ C D, functor C.2 D.2,
  Comp := λ C D E, functor.comp C.2 D.2 E.2,
  Id := λ C, functor.id C.2,
  Hid_left := λ C D F, by cases F; refl,
  Hid_right := λ C D F, by cases F; refl,
  Hassoc := λ _ _ _ _ _ _ _, rfl, }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124451066):
my life is now complete

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124452180):
```
def comma {α : Type u} (C : category.{u v} α)
  {β : Type u₁} (D : category.{u₁ v₁} β)
  {γ : Type u₂} (E : category.{u₂ v₂} γ)
  (F : functor C E) (G : functor D E) :
  category Σ c d, E.Mor (F.F c) (G.F d) :=
{ Mor := λ x y, { P : C.Mor x.1 y.1 × D.Mor x.2.1 y.2.1 //
      E.Comp (F.F x.1) (F.F y.1) (G.F y.2.1) y.2.2 (F.mor x.1 y.1 P.1)
    = E.Comp (F.F x.1) (G.F x.2.1) (G.F y.2.1) (G.mor x.2.1 y.2.1 P.2) x.2.2 },
  Comp := λ x y z P Q, ⟨(C.Comp x.1 y.1 z.1 P.1.1 Q.1.1, D.Comp x.2.1 y.2.1 z.2.1 P.1.2 Q.1.2),
    by rw [← F.Hcomp, ← G.Hcomp, E.Hassoc, ← Q.2, ← E.Hassoc, P.2, E.Hassoc]⟩,
  Id := λ x, ⟨(C.Id x.1, D.Id x.2.1), by rw [F.Hid, G.Hid, E.Hid_left, E.Hid_right]⟩,
  Hid_left := λ x y P, subtype.eq $ by dsimp; rw [C.Hid_left, D.Hid_left]; cases P.1; refl,
  Hid_right := λ x y P, subtype.eq $ by dsimp; rw [C.Hid_right, D.Hid_right]; cases P.1; refl,
  Hassoc := λ x y z w P Q R, subtype.eq $ by dsimp; rw [C.Hassoc, D.Hassoc] }
```
Now I can have pointed sets :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464151):
How do we pass arguments to meta definition?
The following does not typecheck
```
universe u
open tactic monad expr classical

meta def inst {α: Type u} (p:α → Prop) (h:∀ (n:α), p n) (a:α) : tactic unit :=
do skip

example {α:Type u} (b:α) (p:α → Prop) : (∀ (a:α), p a) → p b :=
begin
  intro h,
  have h' : p b, from h b, -- I want the next line have does the same thing
  inst p h b, -- error: unknown identifier 'p' 'h' 'b'
end
```
Tactic State:
```
α : Type u,
b : α,
p : α → Prop,
h : ∀ (a : α), p a,
h' : p b
⊢ p b 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464196):
I believe there exists a tactic for what you're trying to do. I'm still going to assume that you want an answer to the question you actually asked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464258):
I don't know such tactic, but sure, I would like to know an answer to what I asked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464348):
It is called `specialize`. It is pretty nice. 

Let's put your tactic in its section because we need to open a bunch of namespaces:

```lean
section
open tactic interactive interactive.types lean.parser

meta def inst (fa : parse texpr) (x : parse texpr) : tactic unit :=
do trace fa,
   trace x

end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464361):
When you're given information to a tactic, you're basically giving them syntactic objects and you need provide a way for Lean to parse it. That's because you can invent a lot of different notations for your tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464414):
When I write `inst h b`, I still get the same error(?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464460):
I'm not sure it will solve anything but let's see if it does. Add the following between your tactic and your lemma:

```lean
run_cmd add_interactive [`inst]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464516):
Instead of the previous error, this gives me  error `expression expected `, error is below `b` in `inst h b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464668):
Also, is there anyway I can use `specialize` on a **goal**  like `∃ (b : α), p b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464676):
To your second question: no, you need `existsi` and you feel it your witness or a list of witnesses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464723):
What if you erase `b` in `inst h b`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464777):
Here is the status:
```
universe u

section
open tactic interactive interactive.types lean.parser
meta def inst (fa : parse texpr) (x : parse texpr) : tactic unit :=
do trace fa,
   trace x
end
run_cmd add_interactive [`inst]

example {α:Type u} (b:α) (p:α → Prop) : (∀ (a:α), p a) → p b :=
begin
  intro h,
  inst h,  -- error: expression expected
  admit
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464788):
Ok, I get it. Sorry it took me a while. Lean seems `h b` as one expression in `inst h b` so we need a separator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464829):
We could require the user to enter `inst (h, b)`, how does that look to you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464839):
Fine by me, but does that mean we should change definition of `inst`? (right now I am getting the same error)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464843):
In that case, you'd define your tactic as:

```
meta def inst (fa : parse $ tk "(" *> texpr <* tk ",") 
              (x : parse $ texpr <* tk ")") : tactic unit :=
do trace fa,
   trace x

end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464845):
wow! this is scary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464886):
`tk` and `texpr` are commands for the parser: literally "parse a parenthesis" and "parse an expression"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464934):
`<*` and `*>` is just to get them to be executed one after the other. `a <* b` runs `a` first, then `b` and returns whatever `a` returns. `a *> b` runs `a` first as well and then runs `b` and returns the result of `b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464941):
I see, and `$` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464990):
It's a way of making function application nicer by using fewer parentheses. If you'd write `f (g (h x))` instead you can write `f $ g $ h x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465039):
So, instead of ` parse $ tk "(" *> texpr <* tk "," `, one could write:

```lean
parse 
   (do tk "(",
       e ← texpr,
       tk ",",
       return e)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465047):
We can only use `$` in meta world. Right?
The following gives me error
```
def f (n:ℕ) := n+1
example : f $ f $ 1 = 3 := sorry
```
Error is:
```
type mismatch at application
  f (1 = 3)
term
  1 = 3
has type
  Prop
but is expected to have type
  ℕ
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465095):
No actually, it works everywhere. The problem with your expression is `f $ f 1` is of type `ℕ ` but you're using it to specify the type of `example` it should have type `Sort u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465142):
Now the problem is precedence: `$` has lower precedence than `=` and Lean reads your expression as `f (f (1 = 3))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465144):
Nice, thanks a lot,
Also, `existsi` you mentioned worked as a charm.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465151):
`$` won't make your expression nicer but if you applied `f` once more, you could write `f (f $ f 1) = 3` where you use `(` and `)` to "protect" `=` from `$`, in a sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Mar 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465245):
I see, it is good to have an alternative to parenthesis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 31 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465259):
to be fair I would then do `example : (f ∘ f ∘ f) 1 = 4 := sorry` :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 31 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465306):
it's an eternal Haskell bikeshed as to how to mix parens, composition, flip and low priority application :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465522):
I agree on second point, not on first. I prefer ` f ∘ f ∘ f $ 1` if we're going to use `∘` to avoid parenthesis ... but in this case, it doesn't help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 31 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465562):
oh, you're absolutely right in this regard, it doesn't avoid the parens :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 31 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465563):
in general I do prefer composition over anything else tho

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784334):
I know `exact fact p` finishes the proof, but how can I break it into the following two steps:
1. add `fact` to my set of hypotheses (named `fa`)
1. use `fa` to finish the proof
```
constant fact : ∀ (p:Prop), ¬p
example (p:Prop) : ¬p :=
begin
  exact fact p
end
```
Also, I used `constant` to define an axiom. Is this the usual method?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784341):
we don't usually use `constant/axiom`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784342):
`have fa := fact, exact fa p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784382):
The usual method is not to add axioms at all. Usually it suffices to use `variable` instead, which adds the "axiom" as a precondition of the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784383):
You can also use `apply fa` instead of `exact fa p` to finish the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784427):
as a useless and obvious remark, your axiom is inconsistent:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784428):
```
constant fact : ∀ (p:Prop), ¬p
example : false :=
begin
  apply fact (fact = fact),
  exact rfl
end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784429):
If I have many axioms, isn't it going to be a problem?
Suppose I define a lot of axioms to use in a project.
But I am sure I am not going to use all of them in all of theorems.
Isn't it considered a problem that I see all of them in my proof status?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784434):
what are your axioms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784480):
One way to manage a large collection of axioms is to bundle them all in a typeclass like `field A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784487):
If you use `variable` to declare your axioms, only the ones you actually use in a given theorem will be added as preconditions to the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784530):
```quote
If you use `variable` to declare your axioms, only the ones you actually use in a given theorem will be added as preconditions to the theorem
```
So in that case, what is the difference between constant and variable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784578):
`constant` is global, in the sense that it is true once and for all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784587):
whereas, e.g. `example : P -> Q := sorry` is the same as
```
variable (h : P)
example : Q := sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784588):
`variable` is more like a local assumption

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784629):
I have not written any large collection of axioms, I am thinking of a `C++` type with a lot of constraints.
If all these constraints are satisfied then the operations that I will define on this type make sense.
So how should I define all type constraints so I can easily use them later? (obviously I am going to have more than one type)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784640):
```
class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
(smul_add : ∀r (x y : β), r • (x + y) = r • x + r • y)
(add_smul : ∀r s (x : β), (r + s) • x = r • x + s • x)
(mul_smul : ∀r s (x : β), (r * s) • x = r • s • x)
(one_smul : ∀x : β, (1 : α) • x = x)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784641):
make it a structure / class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784749):
A `constant` / `axiom` (they're the same) is like you gained knowledge for free. With `variables`, `class` and `structure`, you get to assume certain properties but whatever you assume eventually has to be proved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784821):
If you have `variable h : false`, you can prove any theorem statement you want but using that theorem will be much more demanding. If you have `constant h : false`, you'll be able to prove all the theorems that you want and you'll never have to "pay" for such a strong assumption. That means that you may be building a bunch of nonsense. Especially if you have two or more axioms and you don't realize that they contradict each other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784910):
(actually, I can't think of a use for a theorem that assumes false (with `variable`), it's probably useless but also harmless)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784913):
you can never prove false, so you can never use that theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784914):
oh wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784918):
So would you finish this example (if I use `constant` then I can do it):
```
variable h : false
example : ∀ (p:Prop), ¬ p :=  sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784919):
that theorem is exactly `false.elim`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784922):
I use `false.elim` all the time...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784923):
`false.elim h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784924):
```quote
I use `false.elim` all the time...
```
Yes, me too but you only need one of those

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784961):
What is true is that you don't really need anything other than `false.elim` in an inconsistent context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784964):
I see, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784965):
since it's like `sorry`, it's the best theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784972):
You can also write `h.elim` if `h : false` btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785013):
When I wasn't using `class`, I defined a constant for an operator and then define notation for it. How can I do the same for class?
```
universe u
class number(α : Type u) [linear_order α] :=
(neg₀ : α     → option α)

prefix `-₀`:40 := neg₀ -- won't type check
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785015):
`number.neg_o`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785021):
not sure what you're trying to do though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785022):
neg maps alpha to option alpha?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785023):
optional negation, I assume

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785024):
something like `nat.ppred`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785063):
Excellent,
Suppose I have a value of type `int` (in `C++`). Just because negation is defined it does not mean that I can take negation of every value. So I defined it to be something like this!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785065):
but shouldn't that not be a field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785066):
I mean, you don't want to permit any map from alpha to option alpha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785071):
Who said anything about it being a field?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785072):
by field I mean a field of the class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785073):
i.e. the things after `:=`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785074):
what's wrong with specifying a negation operation like this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785113):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785114):
I thought it's like making int from nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785115):
misinterpreted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785258):
Section 6.6 of Theorem Proving in Lean says
```quote
They can also include subscripts, which can be entered by typing `\_` followed by the desired subscripted character
```
I can only use single digits as subscript in VS Code. Am I missing something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785259):
`\_m\_g`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785260):
you need to do it twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785311):
I type `m` then `\` then `_` them `m` then `\` then `_` then `g`then space 
I got: `m` followed by a box followed by a dash followed by `g`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785350):
`\_m \_g `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785351):
space after `m`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785358):
I typed `m` then `\` then `_` them `m` then space then `\` then `_` then `g`then space  
I got: `m` followed by a box followed by a space followed by dash followed by `g`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785399):
maybe `m` doesn't work then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785400):
`\_r \_g`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785401):
not every letter has subscript

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785408):
the point being, make each letter separately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785448):
Thank, `r` worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785544):
Would you let me know why the following won't type check
```
universe u
class number(α : Type u) [linear_order α] :=
(neg₀ : α     → option α)
prefix `-₀`:40 := number.neg₀
example (α : Type u) [linear_order α] : ∀ (n:number α), (-₀ n) = (neg₀ n) := sorry 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785546):
`number.neg_0 n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785547):
or `n.neg_0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785599):
oops!
When I defined everything in terms of a class, then type of my operators don't make any sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785603):
how so?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785644):
Ok, here is two errors I still receive
```
failed to synthesize type class instance for
α : Type u,
_inst_1 : linear_order α,
n : number α
⊢ linear_order (number α)
```
```
invalid field notation, function 'number.neg₀' does not have explicit argument with type (number ...)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785645):
right\

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785646):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785647):
you should have `[number \alpha]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785654):
and then `\forall n:\alpha, -\_o n = number.neg\_o n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785696):
but I would use `extends`:
```
universe u

class number (α : Type u) extends linear_order α :=
(neg₀ : α → option α)

prefix `-₀`:40 := number.neg₀

example (α : Type u) [number α] : ∀ (n:α), (-₀ n) = (number.neg₀ n) := λ _, rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785697):
When going from an OO-ish language (like C++) to a functional language (like Lean and Haskell), one pitfall is that `class` don't mean the same thing anymore. In C++, a class defines a type while in Lean, a class is a sort of packet of information that can be inferred about your types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785789):
Thanks, without `[linear_order α]` --> `extends linear_order α` it would not type checked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785790):
there's a way to do it without `extends`:
```
universe u

class number (α : Type u) [linear_order α] :=
(neg₀ : α → option α)

prefix `-₀`:40 := number.neg₀

example (α : Type u) [linear_order α] [number α] : ∀ (n:α), (-₀ n) = (number.neg₀ n) := λ _, rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785792):
but I prefer the version with `extends`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785807):
Also, can I do something so instead of ` _inst_1 : number α ` I will get something like `hn : number α`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785847):
if you want to do that, you can, but you should also make it a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785851):
```
universe u

class number (α : Type u) [linear_order α] :=
(neg₀ : α → option α)

prefix `-₀`:40 := number.neg₀

example (α : Type u) [linear_order α] [hn : number α] : ∀ (n:α), (-₀ n) = (number.neg₀ n) := λ _, rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785895):
Awesome, thank you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786746):
Sorry if it is too obvious, but how do you finish this example:
```
universe u
class  number(α : Type u) extends linear_order α := unit
example (α : Type u) [nn:number α] (a:α) (b:α) : (a<b) → (a≤ b) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786752):
`le_of_lt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786753):
`and.left` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786755):
eww

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786756):
actually that won't work now that I come to think of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786805):
Thanks, but I was thinking of how I can directly use `preorder.lt`?
When I say `have hh:=nn.lt` all I get is ` hh : α → α → Prop `. But `preorder.lt` is defined to be ` (lt := λ a b, a ≤ b ∧ ¬ b ≤ a) `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786844):
use `let` instead of `have`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786845):
`have` forgets definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786846):
This was also kenny's mistake - `preorder.lt` is not defined as that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786847):
that's only the default value

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786850):
there is a second field that says that `preorder.lt` is equivalent to that, from which `le_of_lt` is proven

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786896):
Perhaps you are oversimplifying your problem, but `le_of_lt` is certainly the way to solve the original question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786999):
sure, I am trying to see how I can directly use all those properties defined for a class.
I used `let hh := nn.lt` and got ` hh : α → α → Prop := linear_order.lt `.
Why does it say `linear_order` and not `preorder`?
```
class preorder (α : Type u) extends has_le α, has_lt α :=
(le_refl : ∀ a : α, a ≤ a)
(le_trans : ∀ a b c : α, a ≤ b → b ≤ c → a ≤ c)
(lt := λ a b, a ≤ b ∧ ¬ b ≤ a)
(lt_iff_le_not_le : ∀ a b : α, a < b ↔ (a ≤ b ∧ ¬ b ≤ a) . order_laws_tac)

class partial_order (α : Type u) extends preorder α :=
(le_antisymm : ∀ a b : α, a ≤ b → b ≤ a → a = b)

class linear_order (α : Type u) extends partial_order α :=
(le_total : ∀ a b : α, a ≤ b ∨ b ≤ a)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787296):
`linear_order.lt` extracts the `lt` field of a `linear_order`. It is defined in terms of `preorder.lt`, just composing with the parent structure conversions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787337):
When `lt_iff_le_not_le` is defined for `preorder`, why do we need a lemma with same name for `preorder`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787343):
If you know ` number α`, then you can write `number.lt a b` where `a b : α` (you don't need to refer to `nn`) and it will refer to the `lt` field inherited from `preorder`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787383):
The lemmas of a structure are often restated as separate theorems in order to get the notations and implicitness of arguments right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787393):
so for instance you can write `a < b` where `a b : α` and it will find the `number` instance and work it back to the `preorder` that supplies the implementation of `<`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787434):
but this is not the same term as `number.lt a b` (it is definitionally equal), which can affect rewrites and things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787435):
`let hh := number.lt a b` gives me error: ` unknown identifier 'number.lt' `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787444):
The new structure command doesn't create `number.lt` type fields, it just has parent structure fields

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787446):
the preferred way to refer to it is `a < b` of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787486):
but should be able to write `preorder.lt a b` or `linear_order.lt a b`.. they are all the same, definitionally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787575):
I have no problem with `a<b`. My problem is that I still don't know how to finish this example (how do I expand definition `nn.lt` or  `preorder.lt a b`,  I failed to do it using `rw`)? I don't care about the full proof, just how do I bring definition or the lemma itself into my hypotheses?
```
universe u
class number(α : Type u) extends linear_order α := unit
example (α : Type u) [nn:number α] (a:α) (b:α) : (a<b) → (a≤ b) := 
begin
  intro less,
  let hh := nn.lt,
  admit
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787720):
The relevant lemma is `lt_iff_le_not_le`, which you can refer to directly by `preorder.lt_iff_le_not_le` or through the restated version (which uses notation for le and lt). So the proof would be something like `(preorder.lt_iff_le_not_le _ _).1 less`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787762):
Again, `nn.lt` *is not a definition*, despite the `:=`. It is a default value for a field, which is allowed to be anything. The reason we know it is in fact equivalent to that default value is because of `lt_iff_le_not_le`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124788049):
```quote
Again, `nn.lt` *is not a definition*, despite t...
```
Very helpful, thank you.
How can I  expand/replace ` ≤ ` to/with ` preorder.le `?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124788056):
`dsimp [( ≤ )]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124788059):
Nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124802900):
How should I write the `match` so the whole thing will type-check?
```
universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(min_prop : match min with
            | none := true -- some predicate
            | sime m := true -- some predicate
            end)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124802998):
Some not sime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124802999):
still does not typecheck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803001):
And brackets round some m

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803003):
That should do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803004):
nope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803007):
I don't think you can do funny things inside that particular position

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803012):
Then we need the big guns to save us

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803051):
```
universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(min_prop : match min with
            | none := true -- some predicate
            | (some m) := true -- some predicate
            end)
```
gives me ` invalid match/convoy expression, expected type is not known `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803052):
min might also mean something else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803053):
```
universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(min_prop : @option.rec_on α (λ x, Prop) min true (λ x, true))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803054):
this worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803055):
He is just rewriting the match into what lean expands it to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803063):
Given the error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803065):
To me `match` or `cases` are a lot more readable that `rec_on`.
Is there any way to fix this and use `match`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803106):
Is the issue that lean needs to be told the type earlier on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803107):
I think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124804468):
Any way I can fix the error message ` failed to register private name '_match_2', prefix has not been registered ` for this:
```
universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(max_prop : Prop := match min with
                    | none := true
                    | (some _) := true 
                    end)) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124804999):
Interesting. I'm not sure you can use `match` this way because it requires the creation of auxiliary definitions. You can try `option.cases_on min true (λ _, true)` instead or create a definition yourself that you refer to in that expression.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805183):
I know `option.cases_on min true (λ _, true)` works, but to me `match` and `cases` are a lot more readable.
I am just trying to define some property to my `class` and it seems impossible without using `cases_on` or `rec_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805272):
You can also do:

```
def max_prop_def (α : Type*) : option α -> Prop
  | none := true
  | (some _) := true
```

And use `max_prop_def min` as your default value.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805367):
Fantastic, thanks a lot!
`Type*` means Type at some universe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805679):
Exactly! And Lean infers that universe for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805978):
you can also write `universe u` at the top and then `(alpha : Type u)`. It's like variables -- you are implicitly quantifying over universes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 08 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124806249):
I strongly recommend Simon's solution over inlining the match (even assuming you can get it to work). It might look nice up front, but as soon as you start using these properties in proofs, you will have to reference those internals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124806595):
Would you please tell me how I should change this, so it will type check?
```
inductive constraint (α:Type*)
| trv                                        : constraint
| stt (bnd:α) (low:Prop) (d : decidable low) : constraint

namespace constraint
def setof {α : Type*} [linear_order α] : constraint α → α → Prop 
| (trv α)         a := true
| (stt bnd low d) a := if low then bnd<a else a<bnd -- ERROR: failed to synthesize type class instance for
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124806903):
I'm not sure what @**Mario Carneiro** will think of it but I propose:

```lean
inductive bound (α:Type*)
| upper  (bnd:α) : bound
| lower  (bnd:α) : bound

def check {α:Type*} [decidable_linear_order  α] : bound α → α → bool
| (bound.lower x) y := x < y
| (bound.upper x) y := x > y

inductive constraint (α:Type*)
| trv                     : constraint
| stt (bnd:bound α) : constraint

namespace constraint
def setof {α : Type*} [decidable_linear_order α] : constraint α → α → bool
| (trv α)         a := true
| (stt bnd) a := check bnd a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807220):
Thanks for showing `lean` :)
I have to think about/learn/understand your solution.
In a meantime, is there a way to merge similar cases?
Consider the following example
```lean
inductive constraint (α:Type*)
| trv        : constraint
| lt (bnd:α) : constraint
| le (bnd:α) : constraint
| gt (bnd:α) : constraint
| ge (bnd:α) : constraint

open constraint
def prop (α:Type*) : constraint α → Prop
| (trv α):= true -- short term
| (lt _) := true -- very long term 1
| (le _) := true -- very long term 1
| (gt _) := true -- very long term 2
| (ge _) := true -- very long term 2
```
Is there any way I use pattern matching and merge those cases where the right hand side is going to be the same?
I know it is a long shot, but even better: may be cases for `lt` and `le` have a lot in common, `very_long ∧p1` and `very_long∧p2`.  Is there a way to effectively write something like 
```lean
def prop (α:Type*) : constraint α → Prop
| (trv α):= true -- short term
| x:(lt _) or x:(le _) := very_long ∧ match x with |(lt _):= p1 | (le _):=p2 end
| (gt _) := true -- very long term 2
| (ge _) := true -- very long term 2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807668):
```quote
Thanks for showing `lean`
```
My pleasure! I love sharing my excitement for Lean.

I would go back to the separation of `constraint` and `bound` and define `prop` as:

```lean
inductive strictness
| strict | non_strict

inductive bound (α:Type*)
| upper  (bnd:α) : strictness → bound
| lower  (bnd:α) : strictness → bound

open bound strictness
-- ...

def prop (α:Type*) : constraint α → Prop
| (trv α):= true -- short term
| (stt (lower b str)) := very_long ∧ match str with | strict:= p1 | non_strict :=p2 end
| (stt (upper b str)) := -- very long term 2 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807713):
So the short answer is that you can't combine pattern matching and propositional notation. You can, however, try to get a bit closer and define functions like `is_strict` or `is_le` and use them in `if _ then _ else _`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807940):
Thanks a lot,
About `[decidable_linear_order ℕ]`
At the intuitive level, does this mean if you give me two natural numbers, I can tell you which one is larger?
I think the answer yes, but it should be no.
For example, if you give me two natural number in **binary format** then comparing them is decidable. But who said you are going to always give them in binary format?
So if I use `[decidable_linear_order ℕ]` in a definition, and use `classical` to find two numbers inside that definition, does that mean comparing them is decidable? (I think the answer should be no, but I don't know why)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808142):
```quote
At the intuitive level, does this mean if you give me two natural numbers, I can tell you which one is larger?
```

Yes that's correct. 

```quote

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808241):
```quote
I think the answer yes, but it should be no.
```

In Lean, no set of numbers are postulated (i.e. we say "let there be natural numbers" and they appear). Instead, each set of numbers is constructed as an inductive type. In particular, natural numbers are defined as follows:

```lean
inductive nat 
| zero : nat
| succ : nat -> nat
```

You may recognize the structure of Peano's axiomatization of natural numbers. The big difference is that the above is a valid definition. Whenever you are given two natural numbers, they are given to you in unary notation (e.g. 11111 for 5, 111 for 3 and so on). This makes comparison decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808252):
For the sake of performances however, the virtual machine and some tactics use binary representations (in the case of the vm, it's implemented by gmp, I believe)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 08 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808255):
Is this what you were getting at?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 08 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808675):
That makes sense, thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124812752):
How can I finish the last definition?
```lean
open nat

inductive ind
| emt : ind
| val (a:ℕ) :ind
open ind

def is_nonempty : ind → Prop
| emt     := false
| (val _) := true

def valof (i : ind) (h : is_nonempty i) : ℕ := match i with
| (val n) := n
| _ := begin admit end
end
```
Status is 
```
i : ind,
h : is_nonempty i,
_match : ind → ℕ,
_x : ind
⊢ ℕ	 
```
It seems `lean` forgot about the first case!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813315):
I don't understand what the difference is, but it could be done using the following definition:
```lean
def valof (i : ind) (h : is_nonempty i) : ℕ := 
begin
  cases i,
  rw is_nonempty at h,
  contradiction,
  exact a
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813425):
Here's how to avoid the `a`:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813433):
```lean
def valof (i : ind) (h : is_nonempty i) : ℕ :=
begin
  cases i with n,
  { exact false.elim h },
  { exact n }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813486):
After `cases` you have two goals, and it's encouraged to wrap them in curly brackets so you can deal with them one at a time (it helps with debugging later on when Leo changes everything and stuff stops working)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813493):
what is wrong with `a`? 
Is it because `a` is used internally?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813835):
the fact that Lean randomly calls variables a is considered a bug ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813836):
Not least because you might already have another variable called a!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813884):
https://github.com/leanprover/lean/issues/1822

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813925):
In Lean 4 your code will stop working but mine should be OK. In fact your code does not work for me -- which version of Lean are you using?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813927):
I am on the nightly from 6th April.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813932):
All my code does, of course, is explicitly names the variable when we do the case split.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813984):
Lean (version 3.3.0, commit fa9c868ed2bb, Release)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814034):
v3.4 is coming soon. A lot has happened since 3.3.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814079):
Oh, this works for me:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814083):
```lean
def  valof' : Π (i : ind), is_nonempty i → ℕ
| (val n) h := n
| emt h := false.elim h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814089):
The equation compiler is apparently more clever than match

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814129):
that can't be right because they are the same thing. The difference is that I am getting h involved in the matching process here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814192):
```lean
def  valof (i : ind) (h : is_nonempty i) : ℕ :=  match i,h with
| (val n), h := n
| emt, h := false.elim h
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814194):
You need to tell the equation compiler about h explicitly, so it seems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814735):
Thanks, your solution worked for me,
But I did not understand why I should use `h` in the match (I know it won't type-check without it, but I don't know why)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815048):
How can I mark result Prop decidable?
```lean
def func(p:Prop)[decidable p] : Prop := p
example (p:Prop)[decidable p] : if (func p) then true else false := sorry -- won't type check
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815254):
```lean
def func (p:Prop) : Prop := p

instance func_of_decidable_is_decidable (p : Prop) [H : decidable p] : decidable (func p) := H

example (p:Prop) [decidable p] : if (func p) then true else false := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815294):
I explain to the type class inference system that it should spot that if p is decidable then func p is too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815298):
Great, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815365):
As for the equation compiler question (why it's not smart enough to make deductions about h) -- I'm afraid that's beyond my pay grade. You can see in your begin/end attempt that by the time we've got to the right of the colon-equals, Lean doesn't even seem to know that i is emt -- even if you explicitly write that it is -- so it can't make any deductions about h.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815524):
I think that when you match on both `i` and `h`, it allows Lean to change the type of `h` (or rather, its patterns) to reflect that you're matching on `i`. In the first branch, `h : is_empty (val n)` and in the second, `h : is_empty emt`. After that, we have definitional equality with `false` (resp. `true`) by simply unfolding `is_empty`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815579):
With regards to decidable, when a function returns `true` or `false` and then that you need it to be decidable, you can use `bool` instead and it will be automatically decidable because there is an implicit conversion from `bool` to `Prop` and the resulting `Prop` is decidable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815709):
How do I prove `decidable true`?
Regarding using `bool`, it works, but then either I have write `p=tt` or I will see the left symbol `↥p` everywhere (not sure how comfortable I am with that, or how much trouble it is going to cause me later).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815760):
`decidable true` has type `Type`so I'm not sure you can prove it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815761):
Here's the definition of decidable -- it's an inductive type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815801):
```
class inductive decidable (p : Prop)
| is_false (h : ¬p) : decidable
| is_true  (h : p) : decidable
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815802):
So you have two constructors, `is_true` and `is_false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815813):
`#check is_true trivial -- decidable true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815856):
`true` is a Prop and `trivial` is a proof of `true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815867):
So if output of a function is either `true` or `false`, how do I say this output is decidable (without going to `bool`)? From what you just said, what I am trying to write in `lean` does not even make sense. Right?
```lean
def func(p:Prop)[decidable p] : Prop := true
example (p:Prop)[decidable p] : if (func p) then true else false := sorry -- won't type check
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815916):
Well you have to prove that the output is either true or false, and then you can make an instance of the decidable class by using is_false if it's false and is_true if it's true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815978):
Take a look at how core Lean proves that less than or equal to is decidable on nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815981):
```lean
instance decidable_le : ∀ a b : ℕ, decidable (a ≤ b)
| 0     b     := is_true (zero_le b)
| (a+1) 0     := is_false (not_succ_le_zero a)
| (a+1) (b+1) :=
  match decidable_le a b with
  | is_true h  := is_true (succ_le_succ h)
  | is_false h := is_false (λ a, h (le_of_succ_le_succ a))
  end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816022):
Given the statement `a <= b` it either proves that it's true or proves that it's false, and in each case it creates an instance of `decidable (a <= b)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816028):
using the `is_true` or `is_false` constructors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816073):
things like `nat.zero_le` are lemmas in Lean (that one says "forall n, 0 <= n")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816076):
Earlier in the file they must have written "open nat" so you don't have to keep writing "nat."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816172):
Sorry, but I still cannot figure out how to make this example work without going to `bool`
```lean
def func(p:Prop) : Prop := true
instance func_of_decidable_is_decidable (p : Prop) : 
decidable (func p) := 
begin
  simp [func],
  -- I have to prove decidable true
  admit
end

example (p:Prop) : if (func p) then true else false := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816222):
```lean
def func(p:Prop) : Prop := true
instance func_of_decidable_is_decidable (p : Prop) :
decidable (func p) := is_true trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816227):
I just use the constructor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816265):
in tactic mode you can write `exact is_true trivial`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816270):
Thanks, now I got it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816272):
The only way you can ever prove decidable anything is to use a constructor. decidable is an inductive type with two constructors and the only way to make an instance of it is to use one of the constructors.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816379):
`decidable.true` proves `decidable true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816479):
```
instance (i) : decidable (is_nonempty i) :=
by cases i; unfold is_nonempty; apply_instance
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816490):
`valof` can also be defined without the `emt` case at all:
```
def valof : Π (i : ind), is_nonempty i → ℕ
| (val n) h := n
```
This is because lean does cases on `h` there and needs no cases since it's `false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816533):
I don't recommend using `bool` in this case if you can help it; it's possible but the coercions will get in your way sooner or later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816581):
what is the difference between `unfold` and `rw`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816582):
Also, you can prove `decidable T` for any expression `T` that is already known to be decidable from earlier stuff (like ands of ors of true and natural number equality and other things like that) by `apply_instance`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816591):
`unfold` does definitional unfolding; the syntax is `unfold X` where `X` is a definition will rewrite with the equation lemmas for `X`. `rw` does arbitrary (non-definitional) rewriting with any equations you give it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816634):
However, `rw X` also works as a shorthand for "rewrite with the equation lemmas for `X`" which makes it very similar to `unfold` in this instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817111):
Thank you,
After all these helps and more than an hour I wrote **6 lines** as a proof  :scream:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817178):
"perfection is when there is nothing left to take away" - Antoine de Saint-Exupery

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817309):
Just to be clear, that was just survival; no perfection was involved!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817314):
I also like to quote Adventure Time when it comes to learning functional programming and proving: sucking is the first step towards being kind of good at something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817408):
The fun thing about Haskell and Lean is that ugly code is still very much usable. As you learn more, you see it improve over time. My ugly Haskell and Lean code is still easier to refactor and evolve than anything I wrote in any language. Just to say: starting with bad code is not too much of a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819331):
When I use `cases ` on an inductive type, how can I specify the first case that I would like to consider?
When I am in tactic mode, how can I have pattern matching on two inductive types at the same time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819379):
nested cases?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819382):
```quote
When I use `cases ` on an inductive type, how can I specify the first case that I would like to consider?
```
in tactic mode you can write
```
case list.nil
{ simp },
case list.cons
{ simp }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819491):
Thanks for `case`
By "nested cases" you mean writing multiple `cases`?
I meant something like `match a,b with`? Is there anything like that available?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819500):
`exact match a,b with`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819501):
you can always use `exact` to go into term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819502):
and `by` to go into tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819503):
no, I don't think there's a tactic for nested cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 09 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819545):
`exact match a,b with` is exactly what I was looking for. Thank you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124820994):
`rcases`, from the mathlib tactics, does multiple cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124821038):
but it only works with one input expression. In fact regular cases will automatically generalize dependent hypotheses like `match i, h with` in your earlier example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124863817):
Does it make any sense if I use `classical` to prove something like ` decidable (number.choose α = none) `?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124864641):
You can, but `option.is_none` is already decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865269):
There's also something contradictory to using classical reasoning to prove decidability: decidability is preferable to `classical.em` (excluded middle) especially to preserve computability. If you bring in classical reasoning, you lose computability so you might as well go all the way and just use `classical.prop_decidable` to make every proposition decidable:

```lean
local attribute [instance] classical.prop_decidable
```

This is useful to use `if _ then _ else _` without proving decidability.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865624):
So if I want to use `decidable` as what it is intended to be then I should not use `classical`. Right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865732):
but `classical.prop_decidable` just says that every `prop` is `decidable`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865767):
`decidable` is a proof obligation that is trivial if you are being classical. Most conventional math in lean is classical, so you usually don't have to worry about this. You should think about decidability if you are writing an executable program (if you have to mark your program `noncomputable` it won't run).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865820):
You can attempt to avoid LEM even when proving theorems, like Kenny, but the library won't really help you in this quest so it's an uphill battle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865830):
Please look at the last two lines, as I am not sure if anything else there is relevant
```lean
α : Type u_1,
_inst_1 : number α,
c : constraint α,
d₁ : decidable (is_trivial c),
d₂ : decidable_linear_order α,
_match : Π (_a : decidable (is_trivial c)), decidable (is_satisfiable c),
hnt : ¬is_trivial c,
d₃ : decidable (is_lower_bound c),
_match :
  decidable (is_lower_bound c) →
  decidable
    (ite (is_lower_bound c) (is_satisfiable._match_3 c hnt (number.max α))
       (is_satisfiable._match_4 c hnt (number.min α))),
hl : is_lower_bound c,
_match : Π (_a : option α), decidable (is_satisfiable._match_3 c hnt _a),
m : α,
aa : decidable (get_bound c hnt < m)
⊢ decidable (get_bound c hnt < m)
```
If I do ` exact aa,` I receive this cryptic error message.
```lean
invalid type ascription, term has type
  decidable
    (@has_lt.lt α
       (@preorder.to_has_lt α
          (@partial_order.to_preorder α
             (@linear_order.to_partial_order α
                (@linear_order.mk α (@decidable_linear_order.le α d₂) (@decidable_linear_order.lt α d₂) _ _ _ _
                   _))))
       (@constraint.get_bound α _inst_1 c hnt)
       m)
but is expected to have type
  decidable
    (@has_lt.lt α
       (@preorder.to_has_lt α
          (@partial_order.to_preorder α
             (@linear_order.to_partial_order α (@number.number.to_linear_order α _inst_1))))
       (@constraint.get_bound α _inst_1 c hnt)
       m)
state:
α : Type u_1,
...
```
I know I might not gave enough information to receive an exact answer, but is there any clue you can share about why this might happen?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865882):
You have `decidable (is_trivial c)` as an assumption, which is probably a bad sign. How is `is_trivial` and `constraint` defined?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865889):
diamond of death?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865935):
I think ` decidable_linear_order α` is more problematic because it is already subsumed by `number α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865937):
yes, ` number α` and ` decidable_linear_order α` both supply a less-equal relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865947):
you should replace `decidable_linear_order α` with `@decidable_rel α (<)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865948):
```lean
def is_trivial : constraint α → Prop
| (cnstr  ktrv        _ _ _ _) := true
| (cnstr (kdyn trv _) _ _ _ _) := true
| _                            := false
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865950):
or define `decidable_number`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865991):
You should be able to prove `decidable (is_trivial c)` for all `c` as an instance, so it shouldn't need to be an assumption

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865997):
I make **no claim** of writing in the best or even a good way. Just trying to find my way through.

```lean
inductive triviality
| trv
| ntr

inductive direction
| lower
| upper

inductive strictness
| stt
| nst

inductive triviality_kind {α:Type*}
| ktrv                             : triviality_kind
| kntr                   (bnd : α) : triviality_kind
| kdyn (tr : triviality) (bnd : α) : triviality_kind

inductive direction_kind
| none
| klower
| kupper
| kdynam (dir : direction)

inductive strictness_kind
| none
| kstt
| knst
| kdyn (st : strictness)

structure constraint (α : Type*) :=
cnstr ::
  (trvk : @triviality_kind α)
  (dirk : direction_kind )
  (strk : strictness_kind)
  (ndir : dirk = direction_kind.none  ↔ trvk = triviality_kind.ktrv)
  (nstr : strk = strictness_kind.none ↔ trvk = triviality_kind.ktrv)
```

```lean
instance  is_trivial_is_decidable (c : constraint α) : 
decidable (is_trivial c) := 
begin
  cases c; cases trvk; 
  try { unfold is_trivial };
  try { cases tr };
  try { exact decidable.true };
  try { exact decidable.false},
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866049):
You seem to already have the proof I mention there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866094):
What produced the `d₁ : decidable (is_trivial c)` in the theorem you are proving?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866108):
I am trying to prove  the following is decidable
```lean
def is_satisfiable (c : constraint α) [d : decidable (is_trivial c)] : Prop :=
  match d with
  | is_true  _  := number.choose α ≠ none
  | is_false ht :=
    match get_strictness c ht with
    | nst :=  true
    | stt :=  if is_lower_bound c then
                match number.max α with
                | none   := true
                | some m := get_bound c ht < m
                end
              else 
                match number.min α with
                | none   := true
                | some m := m < get_bound c ht
                end
    end
  end
```
Second line:
```lean
instance  is_satisfiable_is_decidable (c : constraint α)
          [d₁ : decidable (is_trivial c)] 
          [d₂ : decidable_linear_order α] :
decidable (is_satisfiable c) := 
match d₁ with
| is_true  ht  := by unfold is_satisfiable; simp; apply_instance
| is_false hnt := 
  begin
    unfold is_satisfiable,
    cases get_strictness c hnt; unfold is_satisfiable._match_2,
    begin
      have d₃ : decidable (is_lower_bound c), by apply_instance,
      exact match d₃ with
      | is_true  hl  := 
        begin 
          simp [hl],
          exact match number.max α with
          | none   := by unfold is_satisfiable._match_3; exact decidable.true 
          | some m := begin 
                      unfold is_satisfiable._match_3,
                      have aa := decidable_linear_order.decidable_lt α (get_bound c hnt) m,
                      exact aa,
                      end
          -- by unfold is_satisfiable._match_3; apply_instance
          end
        end
      | is_false hnl := begin simp [hnl], admit end
      end,
    end,
    exact decidable.true
  end
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866109):
drop the line `           [d₁ : decidable (is_trivial c)] `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866111):
You can do the match by writing `if ht : is_trivial c then ... else ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866223):
Should I drop ` [d : decidable (is_trivial c)] ` from definition of `is_satisfiable` as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866253):
Given the complexity of your definition, I think you would do better to change `is_satisfiable` to type `def is_satisfiable (c : constraint α) : bool :=`. Same for `is_trivial`, since it's just a bunch of `true` and `false` branches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866261):
Then decidability will be trivial, and you can prove the unfolding of the individual branches as (much easier) lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866476):
I don't have all your definitions so I don't know if this typechecks, but something like this:
```
def is_trivial : constraint α → bool
| (cnstr  ktrv        _ _ _ _) := tt
| (cnstr (kdyn trv _) _ _ _ _) := tt
| _                            := ff

def is_satisfiable (c : constraint α) : bool :=
if ht : is_trivial c then
  (number.choose α).is_some
else
  match get_strictness c ht with
  | nst := tt
  | stt :=
    if is_lower_bound c then
      match number.max α with
      | none   := tt
      | some m := get_bound c ht < m
      end
    else
      match number.min α with
      | none   := tt
      | some m := m < get_bound c ht
      end
  end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866687):
Would you please tell me why I should have dropped `[d₁ : decidable (is_trivial c)]`?
Shouldn't I have one of these for every property I put in `if then else`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866740):
When you look at `(get_bound c hnt < m)` you should see that `<` is generic, i.e. it is inferred from instances. Because of that you should see that it takes four parameters, not two:

- `α `
- some instance of `has_lt α`
- `get_bound c hnt`
- `m`

This means that if different instances of `has_lt` are inferred for two `<` propositions, they are not syntactically the same so you can't use one to prove the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866786):
That means that you have to consciously try to have a unique path to any instance that you're going to use. If the instances are conceptually the same, it might still be hard to prove and the effort is usually not worth it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866904):
When you say `[d₁ : decidable (is_trivial c)]` , you are defining a function parametric over proofs that triviality is decidable. There's no need to do this, you already have such a proof/function and want to call it whenever you want to decide if a constraint is trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866963):
If you say `if ht : is_trivial c then ...`, it automatically infers the `decidable (is_trivial c)` argument (using the environment, not just the local context), which is what you want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124867141):
Thank you both,
I need time to take these in ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124867357):
Sure :) it's a slow process. You can have Lean's pretty printer show more information and, among others, show the implicit and type class arguments by using `set_option pp.all true` before your theorem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124869749):
OK, after I changed something and I will get back to it later, I managed to rewrote the whole proof in the following nicer way.
As you can see something is almost duplicated. Is there anyway I can make this even shorter (ie remove those duplications)?
```lean
instance  is_satisfiable_is_decidable (c : constraint α) :
decidable (is_satisfiable c) := 
  if ht : is_trivial     c then by { unfold is_satisfiable, simp [ht], apply_instance } else
  if hs : is_nonstrict   c then by { unfold is_satisfiable, simp [hs], apply_instance } else 
  if hl : is_lower_bound c then by
    unfold is_satisfiable;
    cases number.max α with m;
    simp [ht,hs,hl,is_satisfiable]; 
    apply_instance
  else by
    unfold is_satisfiable;
    cases number.min α with m;
    simp [ht,hs,hl,is_satisfiable]; 
    apply_instance
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124869940):
Can you reproduce the definitions of `is_satisfiable`, `constraint`, `is_trivial`, `is_nonstrict` and `is_lower_bound` please?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870028):
I did not mean shorter proof using all these definitions. I thought just because those lines look a lot like each other, one should be able to merge them using something like `try`. But if I write `if ht : is_trivial c ∨ is_nonstrict c then` then I cannot even write `cases ht`, and I did not understand why.
```lean
structure constraint (α : Type*) :=
cnstr ::
  (trvk : @triviality_kind α)
  (dirk : direction_kind )
  (strk : strictness_kind)
  (ndir : dirk = direction_kind.none  ↔ trvk = triviality_kind.ktrv)
  (nstr : strk = strictness_kind.none ↔ trvk = triviality_kind.ktrv)

def is_trivial : constraint α → Prop
| (cnstr  ktrv        _ _ _ _) := true
| (cnstr (kdyn trv _) _ _ _ _) := true
| _                            := false

def is_lower_bound : constraint α → Prop 
| (cnstr _  klower        _ _ _) := true
| (cnstr _ (kdynam lower) _ _ _) := true
| _                              := false

def is_nonstrict : constraint α → Prop 
| (cnstr _ _  knst      _ _) := true
| (cnstr _ _ (kdyn nst) _ _) := true
| _                          := false

def is_satisfiable (c : constraint α) : Prop :=
  if ht : is_trivial     c then number.choose α ≠ none else
  if      is_nonstrict   c then true else 
  if      is_lower_bound c then
    match number.max α with
    | none   := true
    | some m := get_bound c ht < m
    end
  else 
    match number.min α with
    | none   := true
    | some m := m < get_bound c ht
    end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870217):
I'd like to replace your big `if _ then _ else _ ` with a `match` but I can't think of a nice way to do it. Instead, let's try this:

```lean
begin
   refine ( if ht : is_trivial     c then _ 
            else if      is_nonstrict   c then _ 
            else if      is_lower_bound c then 
                match number.max α with
                 | none   := _
                 | some m := _
                end
            else 
                match number.min α with
                 | none   := _
                 | some m := _
                end ) 
   ; simp [*, is_satisfiable] ; apply_instance
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870219):
Not very concise but less repetitive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870361):
As a side note: I suggest you pick more obvious names -- that is, names whose meaning is obvious rather than names that are easy to pick -- that names such as `knst`. I feel overly short names pose a puzzle to the reader.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870419):
Thanks a lot, seems something I can use often.
Regarding `refine`, I found this:
```quote
The refine tactic applies the expression in question to the goal, but leaves any remaining metavariables for us to fill
```
Is that what you are trying to do?
How does `refine` knows inside `(..)` is supposed to be definition of `is_satisfiable` and so it can fill all the `_`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870519):
```quote
As a side note: I suggest you pick more ...
```
Sometimes I think I might be sick, since I prefer `stt` and `nst` over `strict` and `non_strict`, mainly because when you write them in two consecutive lines, they are nicely aligned! :upside_down_face:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870612):
Yes that's what I'm trying to do. Think of refine as applying type inference to `(if ... then _ else ... :  decidable (is_satisfiable c))`. Before we start, we don't know the type of `_` but then, we use the type of `dite` (the `if _ then _ else _` function) and we can figure out that `_` has type `decidable (is_satisfiable c)`. When we're done with type inference / type checking, we still don't know a term (or proof) to assign to `_` so building such a term becomes the goal of a subproof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870621):
Symbols that line up do look nice! As a compromise, you may consider padding with spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870724):
OK, I copy-pasted your suggestion and I am receiving the following error (highlighted below the first `;`), is this a version issue? (I am on 3.3.0)
```lean
Tactic State
α : Type u_1,
_inst_1 : number α,
c : constraint α
⊢ decidable (is_satisfiable c)


don't know how to synthesize placeholder
context:
α : Type u_1,
_inst_1 : number α,
c : constraint α,
ht : ¬is_trivial c,
_match : option α → decidable (is_satisfiable c)
⊢ decidable (is_satisfiable c)
state:
α : Type u_1,
_inst_1 : number α,
c : constraint α
⊢ decidable (is_satisfiable c)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870774):
I don't think your approach will work, Simon. First of all, `match` and `let match` have a tendency to be insulated from pexpr metavariable generation, so that they end up being immediate (term) goals even if they appear in a `refine`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870822):
Second, it is important for Nima's proof approach that the ` number.max α ` argument be exposed at the point of the `match`/`cases`, otherwise it won't be generalized. That means that the `unfold is_satisfiable` command has to come *before* the match attempt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870826):
@**Mario Carneiro** I think you're right.

@**Nima** Would you mind using https://gist.github.com/ to share all the definitions needed to make the example work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870878):
I'll try to make a proof work on my side and get back to you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124871580):
Here is a link
**[lets-learn-some-lean](https://github.com/nima-roohi/lets-learn-some-lean)**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124871630):
In `number.lean`, you almost certainly want `:` instead of `:=` in the fields ` neg₀` etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124871678):
Sure,  thanks,

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872748):
Here's my next suggestion:

```lean
instance  is_satisfiable_is_decidable (c : constraint α) :
decidable (is_satisfiable c) :=
begin
  refine ( if ht : is_trivial     c then _
            else if hs : is_nonstrict   c then _
            else if hl : is_lower_bound c then
                _
            else
                _ )
   ; simp [*, is_satisfiable]
   ; try { generalize : number.max α = x, cases x, }
   ; try { generalize : number.min α = x, cases x, }
   ; try { simp [*, is_satisfiable] }
   ; apply_instance,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872756):
It could work without the `generalize`s but it would produce many more cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872798):
why is that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872799):
also isn't the first `simp` redundant?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872801):
Yeah, I just noticed that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872807):
also the parens around the `refine` should be unnecessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872808):
I mean: which first `simp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872859):
```quote
also the parens around the `refine` should be unnecessary
```
I think it might create a precedence problem with `;`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872982):
To answer your first question: it generates many more cases because we only need `cases number.max α` (resp. `cases number.min α`) in one branch out of four so, at the first `try`, without the `generalize`, we end up with `8` cases instead of `5` and, at the second try, we end up with `16` cases instead of `6`. We don't see all those cases but somehow knowing that they're there would give me nightmares

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873026):
does `generalize` fail if the target expression is not present?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873080):
`generalize : number.max α = x` does but not `generalize h : number.max α = x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873185):
I kind of like this use of `refine`. Maybe a tactic such as `if_then_else [is_trivial c,is_nonstrict c,is_lower_bound c]` would be nicer though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873190):
A remark on theorems like this, where you have to go through all the cases in your original definition: You have to do this every time you want to prove anything about `is_satisfiable`, which is why I prefer to write a custom recursor that does the match splits for you. You can then use it to define `is_satisfiable` itself, as well as theorems proving properties about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873193):
That make sense. Do you also write a tactic to apply the recursor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873194):
`by_cases` is the tactic version of `if then else`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873237):
Can you give it multiple conditions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873238):
Not usually, I will either write it explicitly as a term or use `apply is_satisfiable.rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873239):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873246):
I'm not convinced you will always have this structure anyway; it seems like it's best just to nest the `by_cases` applications

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873287):
you could also have `if h1 then if h2 then e1 else e2 else e3`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873419):
Thank you for the solution.
By actually doing it, I can see `cases number.max α` creates a lot more cases than `generalize : number.max α = x, cases x`. But why (aren't they both cases on `none` and `some _`)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873477):
In `generalize : number.max α = x, cases x`, `generalize : number.max α = x` fails if `number.max α` is not used in the goal and therefore `cases x` doesn't get executed. It's a complicated way of saying `cases number.max α` but only if I actually use `number.max α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873546):
I see,
Also, is this **recuroser** a concept in lean or Haskell?
```quote
... which is why I prefer to write a custom recursor that does the match splits for you. ...
```
Theorem Proving in Lean, Section 7.1
```quote
... It is also known as a recursor, and it is what makes the type “inductive” ...
```
??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873547):
By the time it is used, `number.max α` has disappeared from all but one goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873636):
The recursor is a Lean and dependent type theory concept

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873689):
In Lean, an inductive type definition is not a first class citizen. It is translated into a bunch of constants and definitions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873691):
Let's take a look at:

```lean
inductive my_option (α : Type*)
 | none : my_option
 | some : α → my_option
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873696):
It's not limited to dependent types, of course. :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873741):
Thanks for the precision!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873747):
Gotta keep you on your toes. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873752):
If we type in 

```lean
#print prefix my_option
```

we see the constants and definitions that `my_option` is translated into

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873906):
Sean will correct me if I'm wrong but I think only three of them are constants: two constructors

```
my_option.none : Π (α : Type u_1), my_option α
my_option.some : Π {α : Type u_1}, α → my_option α
```

and one recursor

```
my_option.cases_on : Π {α : Type u_1} {C : my_option α → Sort l} (n : my_option α),
  C (my_option.none α) → (Π (a : α), C (my_option.some a)) → C n
```

(I just realized that `no_confusion` is actually a definition)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873964):
The recursor basically tells you how to pattern match on `my_option`. When you pattern match on `opt : my_option α`, you're constructing a value of `C opt` (for some `C`) and you have to provide a way to construct `C opt` in the case where `opt` is `none` and in the case where `opt` is `some a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874009):
Actually the constant is `my_option.rec_on`, and of course `my_option` itself is also a constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874019):
`rec_on` should be a definition as well.  `rec` is the recursor constant.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874021):
Aren't `rec_on` and `cases_on` defined in term of each other?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874026):
`rec_on` and `cases_on` are the same for a nonrecursive inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874078):
What I mean is, for recursive inductive types, do we actually have two separate constants for `cases` and `rec`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874127):
there is no `cases` for some reason, just `cases_on`, and no, `rec` is the only elimination-like constant, `cases_on` just ignores the inductive hypotheses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874175):
@**Simon Hudon** https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/ -- `no_confusion` is defined in terms of the eliminator, but I always found the definition rather obscure. I wrote some notes about it in the link.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874176):
Ok, that's what I thought. So I cut some cornets in my explanation by making it about `cases_on` instead of `rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874189):
@**Kevin Buzzard** Thanks! I was sure it had to be postulated too. I guess i got confused :stuck_out_tongue_closed_eyes:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874229):
Just for the sake of completeness and posterity, is this what everybody is seeing after `#print prefix my_option`?

```lean
my_option : Type u_1 → Type u_1
my_option.cases_on : Π {α : Type u_1} {C : my_option α → Sort l} (n : my_option α),
  C (my_option.none α) → (Π (a : α), C (my_option.some a)) → C n
my_option.has_sizeof_inst : Π (α : Type u_1) [α_inst : has_sizeof α], has_sizeof (my_option α)
my_option.no_confusion : Π {α : Type u_1} {P : Sort l} {v1 v2 : my_option α}, v1 = v2 → my_option.no_confusion_type P v1 v2
my_option.no_confusion_type : Π {α : Type u_1}, Sort l → my_option α → my_option α → Sort l
my_option.none : Π (α : Type u_1), my_option α
my_option.none.inj : ∀ {α : Type u_1}, my_option.none α = my_option.none α → true
my_option.none.inj_arrow : Π {α : Type u_1}, my_option.none α = my_option.none α → Π ⦃P : Sort l⦄, (true → P) → P
my_option.none.inj_eq : ∀ {α : Type u_1}, my_option.none α = my_option.none α = true
my_option.none.sizeof_spec : ∀ (α : Type u_1) [α_inst : has_sizeof α], my_option.sizeof α (my_option.none α) = 1
my_option.rec : Π {α : Type u_1} {C : my_option α → Sort l},
  C (my_option.none α) → (Π (a : α), C (my_option.some a)) → Π (n : my_option α), C n
my_option.rec_on : Π {α : Type u_1} {C : my_option α → Sort l} (n : my_option α),
  C (my_option.none α) → (Π (a : α), C (my_option.some a)) → C n
my_option.sizeof : Π (α : Type u_1) [α_inst : has_sizeof α], my_option α → ℕ
my_option.some : Π {α : Type u_1}, α → my_option α
my_option.some.inj : ∀ {α : Type u_1} {a a_1 : α}, my_option.some a = my_option.some a_1 → a = a_1
my_option.some.inj_arrow : Π {α : Type u_1} {a a_1 : α}, my_option.some a = my_option.some a_1 → Π ⦃P : Sort l⦄, (a = a_1 → P) → P
my_option.some.inj_eq : ∀ {α : Type u_1} {a a_1 : α}, my_option.some a = my_option.some a_1 = (a = a_1)
my_option.some.sizeof_spec : ∀ (α : Type u_1) [α_inst : has_sizeof α] (a : α), my_option.sizeof α (my_option.some a) = 1 + sizeof a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874240):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874243):
Awesome. I haven't upgraded Lean in a while, so some things may have changed. :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874244):
Or rather, until other people answer: I don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874245):
@**Simon Hudon** here's an indication that it doesn't have to be postulated -- once you have `cases` for `nat` you can define `is_zero` by `is_zero 0 = tt` and `is_zero (succ n) = ff` and then prove that zero can't be a successor that way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874287):
Is this what _everybody_ is seeing??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874290):
I don't know either.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874297):
One response was enough for me, it seems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874298):
[i.e. it's what I am seeing]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874302):
```quote
Is this what _everybody_ is seeing??
```
we all know you teach m1f

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874311):
I don't. What is m1f?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874312):
I only required an extistential result, rather than a universal quantification.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874317):
m1f = introduction to proof course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874358):
@**Kevin Buzzard** one should probably change the course name then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874359):
So let's rephrase then: does there exist a participant other than myself that also sees the following output ... ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874360):
Yes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874361):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874422):
@**Kenny Lau** I think it's not only the [dictionary](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/constructing.20proofs.20by.20hand/near/124872856) that uses English to describe English. We also do that here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874443):
doom day's clock is ticking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874490):
@**Nima** I'm just curious what your background is relevant to Lean. Have you worked with functional programming or proof assistants?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874634):
Alright! Enough excitement for today. I have to wake up in a few hours and get back to writing. Good <<insert current period of the day of your timezone here>> everyone!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874652):
And good night to you, @**Simon Hudon**!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874654):
Good night. @**Sean Leather** has returned too, neat! Hello.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874656):
You can check time zones on Zulip I noticed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874658):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874661):
@**Moses Schönfinkel** Hello, hello! You don't have any news on Lean 5 to tell me about, do you? :worried:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874663):
click on the down-arrow which appears when you mouse over a person's name on the right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874703):
and you see their local time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874704):
I have been having some issues with my crystal ball ever since my cat cracked it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874706):
although Kenny went from Lon to HK and didn't update his

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874708):
```quote
 functional programming:
```
Only Scala, which based on what I see, I would not be surprised if people find it insulting that I put Scala and FP side by side ;)
```quote
proof assistants
```
I worked with PVS, for example, I have a paper in which I said something is wrong and this is the right version. In order to be more confident, I proved some of the stuff in PVS (about 25K proof commands, which of course could be very inefficient proofs)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874716):
```quote
although Kenny went from Lon to HK and didn't update his
```
done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874766):
Scala is the best way to target JVM.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874825):
@**Nima** Would you mind giving us a reference to your paper? I did some PVS too and I'd like to see what you did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874898):
Revisiting MITL to Fix Decision Procedures 
https://link.springer.com/chapter/10.1007/978-3-319-73721-8_22
Proofs can be found here (link is also in the paper)
http://uofi.box.com/v/PVSProofsOfMITL

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874946):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874949):
Ok, now I'm really off

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899110):
I have a type `constraint` which represents something like `bnd < x` or `x < bnd`.
I have a function `sem` (semantics) that receives a constraint as input and return a predicate one `ℕ` as output (the set of values satisfied by the constraint). Let `c` be a constraint. I would like to be able to write `x : c`. For that, I have the following code, but I am not sure about `{x // sem S x}`. Is there a mistake or a better way there?

```lean
open nat

inductive constraint 
| low (bnd: ℕ)
| upp (bnd: ℕ)
open constraint

def sem (c : constraint) (a : ℕ) : Prop :=
match c with
| low bnd := bnd < a
| upp bnd := a < bnd
end

instance constraint_to_pred : 
  has_coe (constraint) (ℕ → Prop) :=
  ⟨λ c, λ a, sem c a⟩

instance constraint_to_sort: 
  has_coe_to_sort (constraint ) :=
  {S := Type*, coe := λ S, {x // sem S x}}
```

If everything is fine, how do I finish the following example:
```lean
example : ∀ a : (low 1), a.val > 1 := 
begin
  intro a,
  admit,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899250):
It looks good to me except that I don't know that you actually need the `has_coe` instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899258):
For the proof, you can try:

```lean
example : ∀ a : (low 1), a.val > 1 :=
begin
  unfold_coes,
  intro a,
  admit,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899280):
It should unfold all the coercions and then you should see a clear way to finishing the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899441):
If I comment the first instance then the second one won't type check (may be because of `{x // sem S x}` that I prefer not to have any way)
```
type mismatch at field 'coe'
  λ (S : constraint), {x // ⁇}
has type
  constraint → Sort (max 1 ?) : Type (max 1 ?)
but is expected to have type
  constraint → Type ? : Type (?+1)
```
If I don't comment the first instance then I will receive the following error: `unknown identifier 'unfold_coes'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899492):
You need `import tactic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899573):
If you want to remove the first instance, I think you need to change the second to:

```
instance constraint_to_sort:
  has_coe_to_sort (constraint ) :=
  {S := Sort*, coe := λ S, {x // sem S x}}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899844):
OK, I don't know what happened, but removing the first instance does not give me error any more
```quote
You need import tactic
```
Do you mean `open tactic`? Line `import init.meta.tactic` will type check, but `import tactic` will not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899858):
You're not using `leanpkg` and `mathlib` right? Now would be a good time to bring them in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 10 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899909):
In a terminal where your sources are, type in:

```
leanpkg init lets-learn-some-lean
leanpkg add leanprover/mathlib
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 10 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124902193):
OK, I have imported tactic. But I still receive the same error.
```lean
import tactic
import tactic.interactive
open nat

inductive constraint
| low (bnd: ℕ)
| upp (bnd: ℕ)
open constraint

def sem (c : constraint) (a : ℕ) : Prop :=
match c with
| low bnd := bnd < a
| upp bnd := a < bnd
end

-- this instance seems redundant for now
instance constraint_to_pred :
  has_coe (constraint) (ℕ → Prop) :=
  ⟨λ c, λ a, sem c a⟩

instance constraint_to_sort:
  has_coe_to_sort (constraint ) :=
  {S := Type*, coe := λ S, {x // sem S x}}

example : ∀ a : (low 1), a.val > 1 :=
begin
  unfold_coes, -- ERROR: unknown identifier 'unfold_coes'
  intro a,
  admit,
end  
```
I think dependency is successfully created. For example, I can make the following work perfectly fine.
```lean
variables A B C D : Prop
example (H : A) (H₁ : ¬ B) : ¬ (A → B) := by finish
```
But no luck with `unfold_coes`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970239):
Inside a proof, I have two cases. In case 1, I prove something about lower bound and in case 2, I prove something about upper bound. Each case has multiple steps, but the structure is identical (in order to obtain the second part from the first part, all I need to do is replace word `mid` with `max`).
How do I write both these cases without practically writing a part of the proof twice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970283):
where is the word `mid` and `max`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970284):
could you post your code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970345):
The whole code is too long, but here is the part I was talking about (I just wanted to see what the general approach is in these situations. Do you create a whole new `meta` function, or you can do something inline):
```lean
  by_cases is_lower_bound c with hl ; simp [hl],
  begin
    have hl' := iff.mp (is_lower_bound_is_lower c ht) hl,
    have hm := number.min_prop α,
    cases number.min α with m; unfold min_prop at hm,
    begin
      specialize hm bnd,
      cases hm with m' hm',
      specialize h₁ m',
      unfold sem at h₁,
      simp [ht,hb,hl',hs',sem] at h₁,
      have := iff.mp lt_iff_le_not_le hm',
      simp [h₁,this] at h₁,
      contradiction,
    end,
    specialize hm bnd,
    specialize h₁ m,
    unfold sem at h₁,
    simp [ht,hb,hl',hs'] at h₁,
    unfold sem at h₁, 
    have := le_antisymm hm h₁, 
    simp [this],
  end,
-- next case replace words "lower" with "upper" and "min" with "max"
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970386):
You are not likely to be able to simplify this unless you formalize the symmetry between `min` and `max` here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970390):
You can try to extract a lemma with something with the same type as `min` and `max`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970450):
If I don't extract any lemma, is there any way, I can write this proof but replace for example `(is_lower_bound_is_lower c ht)` with a placeholder and later fill that placeholder twice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970504):
You can run the same tactic script twice. As long as you set up the state (before or after) with suitable modifications, you can do this kind of thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970548):
For example, you could have `have lem := is_lower_bound_is_lower` in one branch and `have lem := is_upper_bound_is_upper` in the other branch, and then run a script that refers to `lem` which means different things in the two branches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970597):
gotcha, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970598):
or just copy it once already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971067):
How do I combine the following two:
```lean
unfold f1 at h1 h2 -- only at h1 and h2
unfold f1 -- only at goal (?)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971268):
`unfold f1` can also be written `unfold f1 at |-`, and you can do both with `unfold f1 at h1 h2 |-`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971269):
there's also a unicode version of `|-`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971554):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124981003):
I wonder if `wlog` might be of help for your repetition problem. Like Mario said, you'd need to formalize the symmetry some more but maybe `wlog` can do some of that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005327):
Sorry, but how do I finish this example?
```
class number := (aa1 := tt)
example [nn:number] : number.aa1 = tt := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005396):
Try `by simp!`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005400):
(the `!` is part of the proof)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005417):
I got error: `command expected`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005472):
Restart your Lean server (C-c C-r in emacs)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005522):
I am on VS Code, restarted the whole program. But no luck!
```lean
class number := (aa1 := tt)
example [nn:number] : number.aa1 = tt := by simp!  -- error command expected
```
Lean 3.3.0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005571):
Oh! 3.3.0 ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005574):
ok, one sec

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005580):
ok `by refl` should do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005670):
```lean
invalid apply tactic, failed to unify
  number.aa1 = tt
with
  ?m_2 = ?m_2
state:
nn : number
⊢ number.aa1 = tt
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005701):
What happens if you do:

```
begin
  unfold number.aa1
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005794):
Sorry, I just got what is happening. The proof shouldn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005855):
Yep, it does not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005877):
In `class number := (aa1 := tt)`, `aa1` is a field of type `bool` whose default value (when you build an instance) is `tt`. You can still specify a different value so you don't know for sure that `aa1` is `tt` in your example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005923):
What are you trying to do with that example? I suspect you're misusing classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005995):
First, how do I change a default value? Is this like a programming language that I can assign value to variables??
I wanted to show `number.has_prev a` is decidable for any value `a`. But I guess you are saying value of `has_prev` can be changed later (can mark it like a constant! I am lost)
```lean
(has_prev  := λ a:α, dense = ff ∧ some a ≠ min)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006160):
No, this is not about mutating variables. Think of `class number` as a type declaration:

```
@[class]
structure number :=
  (aa1 : bool)
```

the `:= tt` part allows you to write:

```
instance : number := 
{ }
```

and it is taken to mean:

```
instance : number :=
{ aa1 := tt }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006189):
ooo!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006246):
And in keeping with desugaring the `class` / `instance` syntax, the latter is equivalent to:

```
@[instance]
def my_number_instance : number :=
{ aa1 := tt }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006293):
What was I thinking!!
Thanks a lot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006340):
No worries

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125121921):
How do I finish this example without using `finish`?
```lean
inductive param | p1 | p2 | p3
example : param.p1 = param.p2 → false := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 15 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125121986):
`example : param.p1 = param.p2 → false := λ h, param.no_confusion h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 15 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125122032):
you can also use `by injection h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 15 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125122172):
Thank you both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 15 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125122183):
I think you could create new topics, instead of always reusing the same one. It would make it easier for other readers to decide whether they could learn something from your questions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123108):
That is definitely an option. However, most (if not all) of my questions are trivially answered by experienced users like Simon or Mario. I look at "Fresh off the boat" as a topic that contains questions a new user like me with a very little experience might ask. Nothing deep, but they come from everywhere (for example, because I read a book and that book talks about lots of different things). That is how I see them related. 

Of course, another option is to create one topic for basically every one of them. The point is, 1) I don't know the answer is in `no_confusion` or `injection`, so most likely the topic I would create won't have a meaningful representation of its content. 2) I doubt that a user will learn much just by reading a single one of them. Either, they already know the answer, or if they don't, they are likely to benefit from similar questions that now they would not know how to find.

I agree, for some concepts having a separate topic makes a lot of sense. For example, Code Generation, Meta Programming, mathlib (may be each with subtopics as well). But I don't see enough benefit to bloat list of topic by wanting every topic to be as specific as possible. Maybe having both kinds would be more helpful. Some are general-nothing-deep-scattered-subjects and some focused-deep-into-a-concent topics.

Please let me know what you think. If I see you guys prefer separate topics anyway, I will do my best to post that way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 15 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123341):
I think you can already pick a good topic by describing the problem that you're having. In this case you could say "how to I prove that different constructors form distinct values". I don't think the topic should contain the answer to your question because, if someone has the same problem as you, they won't know to look in the thread you created.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 15 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123382):
You can also pick a very bad topic name and change it later as suggestions come in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123395):
No problem,
Thanks for letting me know your thought.


{% endraw %}
