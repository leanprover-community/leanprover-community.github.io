---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23060existsXY.html
---

## [general](index.html)
### [exists (X) (Y)](23060existsXY.html)

#### [Kevin Buzzard (May 17 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126709974):
`topological_space.is_topological_basis` has, as part of its definition, `∃ (t₃ : set α) (H : t₃ ∈ s), x ∈ t₃ ∧ ...`, that is, "there exists a set with some property such that..."

#### [Kevin Buzzard (May 17 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126709984):
So I've just sat down to write some trivial thing and it's ended up like this:

#### [Kevin Buzzard (May 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126709996):
```lean
import analysis.topology.topological_space
universe u 

variables {X : Type u} [topological_space X] {B : set (set X)}

definition basis_nhds (HB : topological_space.is_topological_basis B) (x : X) := {U : set X // x ∈ U ∧ U ∈ B} 

noncomputable instance basis_nhds_has_so_called_sup (HB : topological_space.is_topological_basis B) (x : X) :
lattice.has_sup (basis_nhds HB x) := {
  sup := λ Us Vs, begin
    cases (classical.indefinite_description _ (HB.1 Us.1 Us.2.2 Vs.1 Vs.2.2 x ⟨Us.2.1,Vs.2.1⟩))
      with W HW,
    cases (classical.indefinite_description _ HW) with HB HW,
    exact ⟨W,⟨HW.1,HB⟩⟩
  end 
}
```

#### [Kevin Buzzard (May 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710000):
[this is all your fault @**Kenny Lau** ]

#### [Kevin Buzzard (May 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710018):
I want to define a function "sup", so I need some classical stuff to pull out witnesses for the exists

#### [Kevin Buzzard (May 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710067):
and I have to run it twice because it's "exists this, such that exists that, such that..."

#### [Kevin Buzzard (May 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710139):
Based on the "it's trivial so write a one-liner in term mode" principle I'd ideally like to write a one-liner in term mode, but writing `classical.indefinite_description` twice fills up most of the line already :-/

#### [Kevin Buzzard (May 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710140):
Is there a trick I'm missing?

#### [Reid Barton (May 17 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126717885):
This only saves one of your lines, but for `∃ (H : p), q` where `p` is a `Prop`, check out `Exists.fst` and `Exists.snd`.
You can eliminate the second line and change the third to `exact ⟨W,⟨HW.snd.1,HW.fst⟩⟩`

#### [Reid Barton (May 17 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126718073):
This little detail about how `∃ t₃∈s, ...` means `∃ t₃, ∃ H : (t₃∈s), ...` is a bit annoying in this case, but using `.fst` and `.snd` you can pretty much pretend it actually means `∃ t₃, t₃∈s ∧ ...`

#### [Kevin Buzzard (May 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719052):
Here's a mathlib-free version of what I'm moaning about:

#### [Kevin Buzzard (May 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719053):
```lean
example (α : Type) (p q : α → Prop) (r : { x : α // p x ∧ q x} → Type) (H : ∃ (x : α) (H1 : p x), q x) : Type :=
begin
  cases (classical.indefinite_description _ H) with x H2,
  cases (classical.indefinite_description _ H2) with H3 H4,
  exact r ⟨x,H3,H4⟩
end 
```

#### [Reid Barton (May 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719176):
```lean
example (α : Type) (p q : α → Prop) (r : { x : α // p x ∧ q x} → Type) (H : ∃ (x : α) (H1 : p x), q x) : Type :=
begin
  cases (classical.indefinite_description _ H) with x H2,
  exact r ⟨x,H2.fst,H2.snd⟩
end
```

#### [Kevin Buzzard (May 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719179):
Aah I see @**Reid Barton**  -- thanks for these tips.

#### [Kevin Buzzard (May 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719190):
I hadn't really internalised why there were two exists, or the trick with "exists proof".

#### [Reid Barton (May 17 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719195):
or
```lean
let ⟨x,H2⟩ := classical.indefinite_description _ H in r ⟨x,H2.fst,H2.snd⟩
```

#### [Kevin Buzzard (May 17 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719240):
let cases := classical.indefinite_description _ :-/

#### [Mario Carneiro (May 18 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722300):
I would prefer to do the proof in two stages, first showing it's directed and then extracting the witness
```
section
variables {X : Type u} [topological_space X] {B : set (set X)}
variables (HB : topological_space.is_topological_basis B) (x : X)
include HB

definition basis_nhds := {U : set X // x ∈ U ∧ U ∈ B}

theorem basis_nhds_directed (U V : basis_nhds HB x) :
  ∃ W : basis_nhds HB x, W.1 ⊆ U.1 ∧ W.1 ⊆ V.1 :=
let ⟨W, h₁, h₂, h₃⟩ := HB.1 _ U.2.2 _ V.2.2 _ ⟨U.2.1, V.2.1⟩ in
⟨⟨W, h₂, h₁⟩, set.subset_inter_iff.1 h₃⟩

noncomputable instance basis_nhds_has_so_called_sup :
  lattice.has_sup (basis_nhds HB x) :=
{ sup := λ Us Vs, classical.some (basis_nhds_directed HB x Us Vs) }
end
```
You don't need `indefinite_description` here since you don't need the proof part for the definition

#### [Kevin Buzzard (May 18 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722619):
Of course I need it the moment I want to prove `le_sup_left`, but I got distracted by all the function.comp shenannigans in the other thread and never got to this bit :-/

#### [Kevin Buzzard (May 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722676):
This is a much better approach though -- my initial attempt ran into problems when I tried proving `le_sup_left` because my definition used tactics so wouldn't unfold definitionally when I wanted it to. This is a much better idea.

#### [Kevin Buzzard (May 18 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722729):
So many tricks still to learn!

#### [Mario Carneiro (May 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722943):
```
section
variables {X : Type u} [topological_space X] {B : set (set X)}
variables (HB : topological_space.is_topological_basis B) (x : X)
include HB

definition basis_nhds := {U : set X // x ∈ U ∧ U ∈ B}

instance : partial_order (basis_nhds HB x) :=
{ le := λ u v, v.1 ⊆ u.1,
  le_refl := λ u, set.subset.refl u.1,
  le_trans := λ u v w uv vw, set.subset.trans vw uv,
  le_antisymm := λ u v vu uv, subtype.eq $ set.subset.antisymm uv vu }

theorem basis_nhds_directed (U V : basis_nhds HB x) :
  ∃ W : basis_nhds HB x, U ≤ W ∧ V ≤ W :=
let ⟨W, h₁, h₂, h₃⟩ := HB.1 _ U.2.2 _ V.2.2 _ ⟨U.2.1, V.2.1⟩ in
⟨⟨W, h₂, h₁⟩, set.subset_inter_iff.1 h₃⟩

noncomputable instance basis_nhds_has_so_called_sup :
  lattice.has_sup (basis_nhds HB x) :=
{ sup := λ Us Vs, classical.some (basis_nhds_directed HB x Us Vs) }

theorem sup_le_left (u v : basis_nhds HB x) : u ≤ u ⊔ v :=
(classical.some_spec (basis_nhds_directed HB x u v)).1

theorem sup_le_right (u v : basis_nhds HB x) : v ≤ u ⊔ v :=
(classical.some_spec (basis_nhds_directed HB x u v)).2

end
```

#### [Kevin Buzzard (May 18 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722994):
Indeed

#### [Kevin Buzzard (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723001):
You missed a trick with le_antisymm though

#### [Kevin Buzzard (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723005):
Oh actually maybe you didn't

#### [Mario Carneiro (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723006):
I guess you can throw a `function.swap` in there if you want to be "point-free"

#### [Kevin Buzzard (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723007):
Because the order is the other way

#### [Mario Carneiro (May 18 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723050):
but also that circ madness is limited in usefulness since it's nondependent

#### [Mario Carneiro (May 18 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723053):
so for example it wouldn't work in the definition of `sup`

#### [Kevin Buzzard (May 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723104):
You mean the HB and x screw it up?

#### [Mario Carneiro (May 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723112):
no, the u and v do - the type of `basis_nhds_directed HB x u v` depends on them

#### [Mario Carneiro (May 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723122):
if it worked, it would look something like `((∘) ∘ (∘)) classical.some (basis_nhds_directed HB x)`

#### [Kevin Buzzard (May 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723126):
So now all I need is for that PR to be accepted 😉

#### [Mario Carneiro (May 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723127):
There is a `dcomp` function which is dependent, but I don't think it has nice notation

#### [Kevin Buzzard (May 18 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723172):
Unfortunately it looks like it might still need some work by someone who is in the middle of exams...

#### [Mario Carneiro (May 18 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723187):
hm, lean doesn't like `((∘') ∘' (∘'))`

#### [Kevin Buzzard (May 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723239):
You're being sucked into the circ madness...

#### [Kevin Buzzard (May 18 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126738602):
So thanks for writing that proof for me Mario. I was completely on top of everything after Reid's comment about this trick for Exists so I knew I could write it, so I did the optimal thing of just writing it all myself anyway and then comparing with what you wrote. I missed the trick with `let ⟨W, h₁, h₂, h₃⟩ =...` -- I did the expansion using the trick Reid explained later on. But I also didn't use `include` and I carried `HB` around with me as an input variable. Aah, I see -- this is why you have used a section; include plays two roles and I'd only appreciated one of them until now. It can be used to insert hypotheses into the context in a tactic proof, but also to include variables into defintions in a section. I'll remark that I just learnt this by searching the pdf of TPIL for `include` -- I find the sphinx search very disappointing in this regard -- if you search the online docs for include then you just get the unenlightening response that the word is mentioned in every section, and are told the first occurrence of the word in each section; I would in this case far rather see all occurrences so I can try and spot which ones are in code blocks.

#### [Patrick Massot (Jun 01 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127424574):
It tried to read this thread but I still don't understand how to use `exists` classical stuff. How do you tell Lean about `example (X Y : Type) (f : X → Y) :  (∀ y : Y, ∃ x : X, f x = y) → (∃ g : Y → X, f ∘ g = id)`

#### [Reid Barton (Jun 01 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127424633):
use `axiom_of_choice` on that hypothesis and then `funext`

#### [Patrick Massot (Jun 01 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425370):
Thanks you very much. 
```lean
example (X Y : Type) (f : X → Y) :  (∀ y : Y, ∃ x : X, f x = y) → (∃ g : Y → X, f ∘ g = id) :=
begin
  intro hyp,
  replace hyp := classical.axiom_of_choice hyp,
  cases hyp with g H,
  existsi g,
  funext y,
  exact H y
end
```
works. I still have questions: is it what you had in mind? is there a simpler solution? can we hide this to mathematicians? can we avoid frightening stuff like `∃ (f_1 : Π (x : Y), (λ (y : Y), X) x), ∀ (x : Y), (λ (y : Y) (x : X), f x = y) x (f_1 x)` which is defeq to `∃ f_1 : Y → X, ∀ (x : Y), f (f_1 x) = x`?

#### [Patrick Massot (Jun 01 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425457):
the frightening is what you get from `classical.axiom_of_choice hyp`

#### [Reid Barton (Jun 01 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425460):
`set_option pp.beta true` should help

#### [Patrick Massot (Jun 01 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425513):
perfect

#### [Reid Barton (Jun 01 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425517):
And yeah, that's pretty much what I had in mind (or you can write it more succinctly in term mode)

#### [Patrick Massot (Jun 01 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425532):
Why is this `pp.beta` not true by default?

#### [Patrick Massot (Jun 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425612):
Is there any way to merge the two lines `replace hyp := classical.axiom_of_choice hyp,  cases hyp with g H,` into one `I_really_mean hyp with g H`?

#### [Reid Barton (Jun 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425637):
`cases` can take an expression, so you can inline the redefinition of `hyp`

#### [Patrick Massot (Jun 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425640):
I tried that and couldn't succeed

#### [Reid Barton (Jun 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425681):
```lean
  intro hyp,
  cases classical.axiom_of_choice hyp with g H,
-- etc.
```

#### [Patrick Massot (Jun 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425701):
Ok, Lean is afraid of you

#### [Reid Barton (Jun 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425704):
or
```lean
example (X Y : Type) (f : X → Y) :  (∀ y : Y, ∃ x : X, f x = y) → (∃ g : Y → X, f ∘ g = id) :=
assume hyp,
  let ⟨g, H⟩ := classical.axiom_of_choice hyp in
  ⟨g, funext H⟩
```

#### [Patrick Massot (Jun 01 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425711):
it didn't work with me before you wrote it

#### [Patrick Massot (Jun 01 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425735):
I also tried various stuff involving `let`...

#### [Reid Barton (Jun 01 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425809):
just remember that everything in term mode is subtly different from the corresponding thing in tactic mode and you should be fine :simple_smile:

#### [Patrick Massot (Jun 01 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425828):
it's a bit confusing that the `funext` tactic takes the variable name as argument while the term version takes the quantified equality

#### [Patrick Massot (Jun 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425906):
Anyway, I have to go back home now. Thank you very much Reid!

#### [Kevin Buzzard (Jun 01 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429106):
Patrick I asked this very question here a month or two ago. Let me see if I can dig out the thread.

#### [Kevin Buzzard (Jun 01 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429119):
All I remember is that I used the axiom of choice twice and Mario pointed out that I should only be using it once

#### [Kevin Buzzard (Jun 01 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429204):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases.20eliminating.20into.20type

#### [Kevin Buzzard (Jun 01 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429208):
Maybe that will have some relevant material

#### [Patrick Massot (Jun 01 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127431357):
I thought so, bu I found the wrong thread when I searched. Thank you

#### [Patrick Massot (Jun 03 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127515866):
So, @**Kevin Buzzard** and @**Mario Carneiro**, should I PR something like:
```lean
namespace tactic
namespace interactive
open interactive interactive.types

/--
  `choice hyp with g H` takes an hypothesis `hyp` of the form 
  `∀ (y : Y), ∃ (x : X), P x y` for some `P : X → Y → Prop` and outputs into
  context a function `g : Y → X` and a proposition `H` stating 
  `∀ (y : Y), P (g y) y`. It presumably also works with dependent versions 
  (see the actual type of `classical.axiom_of_choice`)
-/
meta def choice (e : parse cases_arg_p) (ids : parse with_ident_list) :=
do cases (e.1,``(classical.axiom_of_choice %%(e.2))) ids

end interactive
end tactic

example (X Y : Type) (P : X → Y → Prop) :  (∀ y : Y, ∃ x : X, P x y) → (∃ g : Y → X, ∀ y, P (g y) y) :=
begin
  intro hyp,
  choice hyp with g H,
  existsi g, 
  exact H
end
```
I know this is purely cosmetic, but I think it would help mathematicians to have a nice interface to choice.

#### [Patrick Massot (Jun 03 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127515910):
Of course this is a version of what Simon wrote in the other thread

#### [Kevin Buzzard (Jun 03 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516186):
This is really nice and I want to be showing this to my 1st years.

#### [Kevin Buzzard (Jun 03 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516187):
It was on my todo list to  get this into a xena library.

#### [Kevin Buzzard (Jun 03 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516194):
Patrick -- can choice be used to replace cases everywhere?

#### [Kevin Buzzard (Jun 03 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516301):
@**Mario Carneiro** it's important we make a good interface for mathematicians, so they can learn more quickly.

#### [Kenny Lau (Jun 03 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516364):
Skolem normal form?

