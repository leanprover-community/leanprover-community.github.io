---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24264groupequivleftcosetstimessubgroup.html
---

## Stream: [general](index.html)
### Topic: [group_equiv_left_cosets_times_subgroup](24264groupequivleftcosetstimessubgroup.html)

---


{% raw %}
#### [ Kenny Lau (Apr 16 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140026):
```
import data.equiv group_theory.coset

universe u

namespace quotient

variables {α : Type u} [s : setoid α]

def fibre : quotient s → set α :=
λ Q, {x | ⟦x⟧ = Q}

end quotient

namespace equiv

variables {α : Type u} [s : setoid α]

def equiv_fibre : α ≃ Σ Q : quotient s, quotient.fibre Q :=
⟨λ x, ⟨⟦x⟧, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨Q, x, (hx : ⟦x⟧ = Q)⟩, sigma.eq hx $ by subst hx⟩

end equiv

variables {G : Type u} [group G] (S : set G) [is_subgroup S]

instance left_rel : setoid G :=
⟨λ x y, x⁻¹ * y ∈ S,
 λ x, by simp [is_submonoid.one_mem],
 λ x y hxy, have _ := is_subgroup.inv_mem hxy, by simpa using this,
 λ x y z hxy hyz, have _ := is_submonoid.mul_mem hxy hyz, by simpa [mul_assoc] using this⟩

def left_cosets' : Type u := quotient (left_rel S)

namespace is_subgroup

theorem fibre_equiv (L : left_cosets' S) : nonempty (quotient.fibre L ≃ S) :=
⟨⟨λ x, ⟨(quotient.out L)⁻¹ * x.1, quotient.exact ((quotient.out_eq L).trans x.2.symm)⟩,
  λ x, ⟨quotient.out L * x.1, eq.trans (eq.symm $ quotient.sound $ by simpa [(≈), setoid.r] using x.2) (quotient.out_eq L)⟩,
  λ ⟨x, hx⟩, subtype.eq $ by simp,
  λ ⟨x, hx⟩, subtype.eq $ by simp⟩⟩

theorem group_equiv_left_cosets_times_subgroup' : nonempty (G ≃ (left_cosets' S × S)) :=
⟨calc G
    ≃ Σ L : left_cosets' S, quotient.fibre L :
  equiv.equiv_fibre
... ≃ Σ L : left_cosets' S, S :
  equiv.sigma_congr_right (λ L, classical.choice $ fibre_equiv _ _)
... ≃ (left_cosets' S × S) :
  equiv.sigma_equiv_prod _ _ ⟩

end is_subgroup

#### [ Kenny Lau (Apr 16 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140057):
@**Mario Carneiro** @**Johannes Hölzl** do you think this is better than the one in mathlib?

#### [ Kenny Lau (Apr 16 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140116):
https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean

#### [ Mario Carneiro (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140219):
I suggest skipping the `nonempty` here, there's not much point to it

#### [ Kenny Lau (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140222):
it is uncomputable

#### [ Mario Carneiro (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140223):
ok

#### [ Kenny Lau (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140224):
but I'm making verseion 2 where that is computable

#### [ Mario Carneiro (Apr 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140231):
just use `noncomputable def` instead

#### [ Kenny Lau (Apr 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140234):
oh?

#### [ Kenny Lau (Apr 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140235):
@**Johannes Hölzl** what do you think

#### [ Mario Carneiro (Apr 16 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140237):
it's definitely a classical theorem, but wrapping in `nonempty` just means using `choice` later

#### [ Johannes Hölzl (Apr 16 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140276):
I agree with Mario, using nonempty was a bad idea on my side.

#### [ Kenny Lau (Apr 16 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140277):
ok

#### [ Kenny Lau (Apr 16 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140433):
```
import data.equiv group_theory.coset

universe u

namespace quotient

variables {α : Type u} [s : setoid α]

def fibre : quotient s → set α :=
λ Q, {x | ⟦x⟧ = Q}

end quotient

namespace equiv

variables {α : Type u} [s : setoid α]

def equiv_fibre : α ≃ Σ Q : quotient s, quotient.fibre Q :=
⟨λ x, ⟨⟦x⟧, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨Q, x, (hx : ⟦x⟧ = Q)⟩, sigma.eq hx $ by subst hx⟩

end equiv

variables {G : Type u} [group G] (S : set G) [is_subgroup S]

instance left_rel : setoid G :=
⟨λ x y, x⁻¹ * y ∈ S,
 λ x, by simp [is_submonoid.one_mem],
 λ x y hxy, have _ := is_subgroup.inv_mem hxy, by simpa using this,
 λ x y z hxy hyz, have _ := is_submonoid.mul_mem hxy hyz, by simpa [mul_assoc] using this⟩

def left_cosets' : Type u := quotient (left_rel S)

namespace is_subgroup

def fibre_equiv (g : G) : quotient.fibre ⟦g⟧ ≃ S :=
⟨λ x, ⟨x.1⁻¹ * g, quotient.exact x.2⟩,
 λ x, ⟨g * x⁻¹, quotient.sound $ by simpa [(≈), setoid.r] using x.2⟩,
 λ ⟨x, hx⟩, subtype.eq $ by simp,
 λ ⟨g, hg⟩, subtype.eq $ by simp⟩

noncomputable def group_equiv_left_cosets_times_subgroup' :
  G ≃ (left_cosets' S × S) :=
calc G ≃ Σ L : left_cosets' S, quotient.fibre L :
  equiv.equiv_fibre
    ... ≃ Σ L : left_cosets' S, quotient.fibre ⟦quotient.out L⟧ :
  equiv.sigma_congr_right (λ L, by simp)
    ... ≃ Σ L : left_cosets' S, S :
  equiv.sigma_congr_right (λ L, fibre_equiv _ _)
    ... ≃ (left_cosets' S × S) :
  equiv.sigma_equiv_prod _ _

end is_subgroup

#### [ Kenny Lau (Apr 16 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140434):
version 2

#### [ Kenny Lau (Apr 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140441):
who is Mitchell Rowett?

#### [ Kevin Buzzard (Apr 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140442):
Student of Scott?

#### [ Kevin Buzzard (Apr 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140443):
UG I think

#### [ Kenny Lau (Apr 16 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140486):
would he/she mind if, you know, I basically refactor the whole thing

#### [ Kevin Buzzard (Apr 16 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140487):
Isn't the logic of doing the non-empty version that you can go from that to the noncomputable version but you can't go back?

#### [ Kenny Lau (Apr 16 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140495):
I don't get you

#### [ Mario Carneiro (Apr 16 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140498):
full file refactorings are permitted in mathlib, you don't need permission from the original author (and conversely, be prepared for your work to be refactored to unrecognizability in the future)

#### [ Kenny Lau (Apr 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140537):
@**Mario Carneiro** should I refactor coset?

#### [ Johannes Hölzl (Apr 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140538):
Mitchel did the coset theory, the things your changing were mine. I think we can add a more general version of `equiv_fibre`:
```lean
namespace equiv

def equiv_fibre {α : Type*} {β : Type*} {f : α → β} : α ≃ Σb:β, f ⁻¹' {b} :=
⟨λa, ⟨f a, a, by simp⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨b, a, hx⟩, have f a = b, by simpa using hx, sigma.eq this (by subst this; refl)⟩

end equiv
```

#### [ Kenny Lau (Apr 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140540):
how do you make those red rectangles?

#### [ Mario Carneiro (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140543):
```` ```lean ... ``` ````

#### [ Johannes Hölzl (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140548):
I don't know were they come from. I just copied stuff from vs code.

#### [ Kenny Lau (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140550):
I mean red rectangles

#### [ Kenny Lau (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140551):
oh, lean

#### [ Mario Carneiro (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140553):
the red rectangles are what happens when the syntax highlighter gets confused

#### [ Kenny Lau (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140556):
@**Johannes Hölzl** did I tell you how much I hate `{b}`?

#### [ Mario Carneiro (Apr 16 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140601):
On further review, I'm not sure it can be changed, the definition `singleton a = insert a empty` is in core.lean

#### [ Johannes Hölzl (Apr 16 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140650):
@**Kenny Lau**  you shouldn't depend too much on definitional equality. It breaks modularity of the library.

#### [ Kenny Lau (Apr 16 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140692):
don't you like it when every theorem is just `rfl`?

#### [ Johannes Hölzl (Apr 16 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140694):
Of course I like it, but I also hate it to not be able to change a definition because it would break 1000 places in mathlib.

#### [ Kenny Lau (Apr 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140699):
```lean
import data.equiv group_theory.coset

universes u v

variables {α : Type u} {β : Type v} (f : α → β)

def fibre (y : β) : set α :=
{x | f x = y}

namespace equiv

def equiv_fibre : α ≃ Σ y : β, fibre f y :=
⟨λ x, ⟨f x, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨y, x, (hx : f x = y)⟩, sigma.eq hx $ by subst hx⟩

end equiv

variables {G : Type u} [group G] (S : set G) [is_subgroup S]

instance left_rel : setoid G :=
⟨λ x y, x⁻¹ * y ∈ S,
 λ x, by simp [is_submonoid.one_mem],
 λ x y hxy, have _ := is_subgroup.inv_mem hxy, by simpa using this,
 λ x y z hxy hyz, have _ := is_submonoid.mul_mem hxy hyz, by simpa [mul_assoc] using this⟩

def left_cosets' : Type u := quotient (left_rel S)

namespace is_subgroup

def fibre_equiv (g : G) : fibre quotient.mk ⟦g⟧ ≃ S :=
⟨λ x, ⟨x.1⁻¹ * g, quotient.exact x.2⟩,
 λ x, ⟨g * x⁻¹, quotient.sound $ by simpa [(≈), setoid.r] using x.2⟩,
 λ ⟨x, hx⟩, subtype.eq $ by simp,
 λ ⟨g, hg⟩, subtype.eq $ by simp⟩

noncomputable def group_equiv_left_cosets_times_subgroup' :
  G ≃ (left_cosets' S × S) :=
calc G ≃ Σ L : left_cosets' S, fibre quotient.mk L :
  equiv.equiv_fibre quotient.mk
    ... ≃ Σ L : left_cosets' S, fibre quotient.mk ⟦quotient.out L⟧ :
  equiv.sigma_congr_right (λ L, by simp)
    ... ≃ Σ L : left_cosets' S, S :
  equiv.sigma_congr_right (λ L, fibre_equiv _ _)
    ... ≃ (left_cosets' S × S) :
  equiv.sigma_equiv_prod _ _

end is_subgroup
```

#### [ Johannes Hölzl (Apr 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140701):
In Isabelle one can always change a definition, make it more general. And then just prove that it is the same.

#### [ Kenny Lau (Apr 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140703):
Isabelle is crap

#### [ Mario Carneiro (Apr 16 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140750):
be sure to have good reasons to make invective statements

#### [ Kenny Lau (Apr 16 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140751):
it's nonconstructive

#### [ Johannes Hölzl (Apr 16 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140757):
Well, your claim is also nonconstructive

#### [ Kenny Lau (Apr 16 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140758):
so how is version 3?

#### [ Johannes Hölzl (Apr 16 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140802):
I think we should stay with `f ⁻¹' {b}`.

#### [ Mario Carneiro (Apr 16 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140854):
the other advantage of not giving the definition a name is we don't need to debate if it should be `fibre` or `fiber` :upside_down_face:

#### [ Kenny Lau (Apr 16 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140857):
who cares about cosets of sub-not-groups?

#### [ Mario Carneiro (Apr 16 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140863):
I guess Patrick might, that is the same as the translate of a set

#### [ Kenny Lau (Apr 16 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140905):
why would he care?

#### [ Mario Carneiro (Apr 16 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140998):
it relates to affine spaces and the group conjugation action. It also comes up with "neighborhoods of zero" in a topological group

#### [ Kenny Lau (Apr 16 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141009):
singleton is really unusable

#### [ Kenny Lau (Apr 16 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141102):
```lean
import data.equiv group_theory.coset

universes u v

namespace equiv

def equiv_fib {α : Type u} {β : Type v} (f : α → β) :
  α ≃ Σ y : β, {x // f x = y} :=
⟨λ x, ⟨f x, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨y, x, (hx : f x = y)⟩, sigma.eq hx $ by subst hx⟩

end equiv

variables {G : Type u} [group G] (S : set G) [is_subgroup S]

instance left_rel : setoid G :=
⟨λ x y, x⁻¹ * y ∈ S,
 λ x, by simp [is_submonoid.one_mem],
 λ x y hxy, have _ := is_subgroup.inv_mem hxy, by simpa using this,
 λ x y z hxy hyz, have _ := is_submonoid.mul_mem hxy hyz, by simpa [mul_assoc] using this⟩

def left_cosets' : Type u := quotient (left_rel S)

namespace is_subgroup

def fib_equiv (g : G) : {x // ⟦x⟧ = ⟦g⟧} ≃ S :=
⟨λ x, ⟨x.1⁻¹ * g, quotient.exact x.2⟩,
 λ x, ⟨g * x⁻¹, quotient.sound $ by simpa [(≈), setoid.r] using x.2⟩,
 λ ⟨x, hx⟩, subtype.eq $ by simp,
 λ ⟨g, hg⟩, subtype.eq $ by simp⟩

noncomputable def group_equiv_left_cosets_times_subgroup' :
  G ≃ (left_cosets' S × S) :=
calc G ≃ Σ L : left_cosets' S, {x // ⟦x⟧ = L} :
  equiv.equiv_fib quotient.mk
    ... ≃ Σ L : left_cosets' S, {x // ⟦x⟧ = ⟦quotient.out L⟧} :
  equiv.sigma_congr_right (λ L, by simp)
    ... ≃ Σ L : left_cosets' S, S :
  equiv.sigma_congr_right (λ L, fib_equiv _ _)
    ... ≃ (left_cosets' S × S) :
  equiv.sigma_equiv_prod _ _

end is_subgroup
```

#### [ Kenny Lau (Apr 16 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141108):
conflict between `fibre` and `fiber` resolved :P

#### [ Chris Hughes (Apr 16 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141154):
Slightly shortened.
```lean
def equiv_fib {α : Type u} {β : Type v} (f : α → β) :
  α ≃ Σ y : β, {x // f x = y} :=
⟨λ x, ⟨f x, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨y, x, ⟨hx⟩⟩, rfl⟩
```

#### [ Kenny Lau (Apr 16 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141160):
you win

#### [ Mario Carneiro (Apr 16 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141203):
it's a bit weird to write ` ⟨hx⟩` in the last bit there, since it's refl. Use `λ ⟨_, x, rfl⟩, rfl` instead

#### [ Kenny Lau (Apr 16 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141322):
wait, how does that also work :o

#### [ Kenny Lau (Apr 16 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141327):
oh, automatic casing


{% endraw %}
