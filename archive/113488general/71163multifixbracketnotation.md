---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71163multifixbracketnotation.html
---

## Stream: [general](index.html)
### Topic: [multifix bracket notation](71163multifixbracketnotation.html)

---

#### [Johan Commelin (Jun 11 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127889037):
Is this bound to become a massive headache, if possible at all?
```lean
universe u
class has_bracket (α : Type u) := (bracket : α → α → α)
local notation `[` a `,` b `]` := has_bracket.bracket
```
The notation $$[x,y]$$ is very common (I would say, *mandatory*) in the theory of Lie algebras.

#### [Kevin Buzzard (Jun 11 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127889262):
it breaks list notation, so one question is: are you likely to be using list notation? Let's face it, list notation isn't that common in mathematics. Will you use it behind the scenes though? I am not sure I used a single list when doing schemes.

#### [Kevin Buzzard (Jun 11 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127889303):
(at least, not explicitly)

#### [Johan Commelin (Jun 11 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899035):
```lean
import algebra.module

universes u v

class has_bracket (α : Type u) := (bracket : α → α → α)

local notation `[` a `,` b `]` := has_bracket.bracket a b

class lie_algebra (R : out_param $ Type u) (𝔤 : Type v) [out_param $ comm_ring R]
extends module R 𝔤, has_bracket 𝔤 :=
(left_linear  := ∀ y : 𝔤, is_linear_map (λ x : 𝔤, [x,y]))
(right_linear := ∀ x : 𝔤, is_linear_map (λ y : 𝔤, [x,y]))
(alternating  := ∀ x : 𝔤, [x,x] = 0)
(Jacobi_identity := ∀ x y z : 𝔤, [x,[y,z]] + [z,[x,y]] + [y,[z,x]] = 0)
(anti_comm    := ∀ x y : 𝔤, [x,y] = -([y,x]))

variables {R : Type*} [comm_ring R]
variables {𝔤 : Type*} [lie_algebra R 𝔤]

/-- `𝔥` is a Lie subalgebra: a set closed under the Lie bracket. -/
class is_lie_subalgebra (𝔥 : set 𝔤) := (closed {x y} : x ∈ 𝔥 → y ∈ 𝔥 → [x,y] ∈ 𝔥)
```
I am bitten again by type class inference. Once again Lean can't infer the class of `has_bracket 𝔤` in the last line, even though it knows that `𝔤` is a Lie algebra. 
If I compare this with
```lean
class is_add_subgroup [add_group α] (s : set α) extends is_add_submonoid s : Prop :=
(neg_mem {a} : a ∈ s → -a ∈ s)
```
How does Lean figure out `has_mem α` to make sense of the `-a`? The cargo-cult programmer in me is stumped.

#### [Reid Barton (Jun 11 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899473):
I don't know why, but changing the last line to
```lean
variables {𝔤 : Type*} [la : lie_algebra R 𝔤]
include la
```
made it work for me.

#### [Reid Barton (Jun 11 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899477):
If I had to guess, it has something to do with the additional parameter `R`

#### [Johan Commelin (Jun 11 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899495):
Thanks... that'll do for now :wink:

#### [Sebastian Ullrich (Jun 11 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899771):
Yes, section variables used as `out_param`s are a bit broken. Lean will auto-include section class variables only when all its parameters are (auto-)included, but it should ignore `out_param`s during that.

#### [Sebastian Ullrich (Jun 11 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899782):
So `include R` should work too

#### [Johan Commelin (Jun 11 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899849):
It doesn't...

#### [Sebastian Ullrich (Jun 11 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899927):
¯\_(ツ)_/¯

#### [Reid Barton (Jun 11 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127900028):
Maybe need to include the `[comm_ring R]` variable also then

#### [Johan Commelin (Jun 11 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127900036):
Then yours becomes more efficient (-;

#### [Johan Commelin (Jun 11 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127900184):
After Reid's (hacky) fix, the next line gives problems. I would like to solve it myself, but I don't know why Lean is unhappy. Here is the line:
```lean
instance subset.lie_algebra {𝔥 : set 𝔤} [is_lie_subalgebra 𝔥] : lie_algebra R 𝔥 := sorry
```
I get red squiggles before the `is_lie_subalgebra` instance. Lean thinks it needs to infer an extra Type. I have tried some `set_option`s to get more info, but I couldn't figure it out (e.g. `trace.class_instances` and `pp.all`). How should I attack this error?

#### [Johan Commelin (Jun 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914479):
Is there documentation for `out_param`? What is it's purpose? I think I heard somewhere that there have been long discussions about it. Has that been condensed into some docs? It feels to me like `out_param` is making it harder to work with modules, rather than easier.

#### [Patrick Massot (Jun 11 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914499):
I think all documentation is here on Zulip (or gitter) and source code

#### [Johan Commelin (Jun 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914575):
I tried implicitly turning an `R`-algebra into an `R`-module, by chaining together `ring.to_module` and restriction of scalars... guess what happened

#### [Johan Commelin (Jun 11 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914657):
(I wanted to put the commutator bracket on the algebra [to make the link with this thread])

#### [Johan Commelin (Jun 11 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914674):
Anyway, I ran head first into the type class loop again.

#### [Kevin Buzzard (Jun 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924610):
Mario explaining out_param to me on gitter:

#### [Kevin Buzzard (Jun 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924612):
```
elaborator deals with opt_param, type class deals with out_param

Normally a typeclass won't trigger until all its parameters are fixed

So for example [has_mem A B] won't be solved until A and B are known

i.e. if I have x \in y and the types of x y are unknown, it will fail

However, has_mem works a bit differently than this because A is marked as an out_param

@[class]
structure has_mem : out_param (Type u) → Type v → Type (max u v)
fields:
has_mem.mem : Π {α : out_param (Type u)} {γ : Type v} [c : has_mem α γ], α → γ → Prop

In fact, if you have x \in y and y : B, even if the type of x is unknown it will try to solve the typeclass problem has_mem ?M B

This is important because it often comes up in notations like \forall x \in y, ... where y : set A and x is unknown type, we want lean to figure out that x : A

This doesn't affect the meta theory in any way, of course, once the full term is given the elaborator and typeclass inference is done and it's basic DTT. In that situation it really is just an identity function


And opt_param?
Mario Carneiro
@digama0
20:39
That's just the way (x : A := y) is translated, to x : opt_param A y
it holds the optional value so it can be inferred by the usual rules for optional arguments


It is occasionally useful when you want to have an optional argument right of the colon (the := syntax only works on the parameters)
```

#### [Kevin Buzzard (Jun 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924746):
Mario and Sebastian talking about module and params:

#### [Kevin Buzzard (Jun 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924752):
```
To review, the problem is that the definition:

class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
...

leads to a search problem in which ring ?M1 is solved before module ?M1 β, which leads to a loop when there is an instance like [ring A] [ring B] : ring (A x B)
I would like to make lean search for module ?M1 β only, obtaining α and the ring instance by unification
Johannes suggested using {out_param $ ring α} instead of [out_param $ ring α], but then it doesn't work as a typeclass, and all the multiplications etc in the theorem statements break
A possible solution is to skip out_param typeclass search problems until after all the others are solved

***

So the real issue is: You want the elaborator to handle applying a function {A B} [ring A] [module A B] (x : B) : ..., yes...?
Mario Carneiro
@digama0
Jan 19 10:10
yes
Sebastian Ullrich
@Kha
Jan 19 10:10
Where you want it to solve the second instance first, which fixes A and the first instance
```

#### [Kevin Buzzard (Jun 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924890):
https://gitter.im/leanprover_public/Lobby?at=5a61beb85ade18be399654c0

#### [Kevin Buzzard (Jun 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924893):
Johannes too

#### [Johan Commelin (Jun 12 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127939887):
Ok, I think I half understand the issues involved. Does this mean that
```lean
namespace restriction_of_scalars

variables {R : Type u} [ring R]
variables {S : Type v} [ring S]
variables {f : R → S}  [is_ring_hom f]
variables {M : Type w} [module S M]

instance : module R M :=
{ smul     := λ r m, f(r) • m,
  smul_add := λ _ _ _, smul_add,
  add_smul := λ r s m, begin
    show f (r + s) • m = f(r) • m + f(s) • m,
    rw is_ring_hom.map_add f,
    apply add_smul,
  end,
  mul_smul := λ r s m, begin
    show f (r * s) • m = f(r) • f(s) • m,
    rw is_ring_hom.map_mul f,
    apply mul_smul
  end,
  one_smul := λ m, begin
    show f (1) • m = m,
    rw is_ring_hom.map_one f,
    apply one_smul,
  end,
}

end restriction_of_scalars
```
implies self-destruction :boom: ?

#### [Johan Commelin (Jun 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127940673):
Ok, maybe this is asking to much. But would it be ok if we restrict to the case where `R` is a subring, and `f = subtype.val`?

