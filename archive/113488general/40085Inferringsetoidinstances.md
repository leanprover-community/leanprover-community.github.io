---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40085Inferringsetoidinstances.html
---

## Stream: [general](index.html)
### Topic: [Inferring setoid instances](40085Inferringsetoidinstances.html)

---

#### [Chris Hughes (Jul 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129811730):
I've had a bit of trouble with setoid instances in quotient rings and groups. Changes the brackets around `setoid` in `quotient.induction_on` and similar lemmas form `[]` to `{}` improves matters a lot. Is there a downside to this approach? There should always only be one possibility for `setoid` from the type of `q` right?
```lean
lemma quotient.induction_on' {α : Sort u} {s : setoid α} {β : quotient s → Prop} 
  (q : quotient s) (h : ∀ (a : α), β ⟦a⟧) : β q := quotient.induction_on q h
```

#### [Reid Barton (Jul 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812715):
I have also thought the same thing "why not just infer the relation based on the type of `q`".

#### [Reid Barton (Jul 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812730):
I'm guessing you have a type (like, a group) on which you have a relation that depends on some other variable (like, a subgroup) which isn't mentioned in the carrier type?

#### [Reid Barton (Jul 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812795):
I also found these type class arguments annoying to deal with in this kind of situation, although I don't remember what I did about it.
It's possible that switching to a different elaboration strategy fixed my problem, and I didn't look into exactly why.

#### [Reid Barton (Jul 17 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812897):
Or maybe I just used `quot` methods instead. https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator

#### [Reid Barton (Jul 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812930):
Yes, now I remember wondering whether mixing `quotient` with `quot.induction_on` was a sensible thing to do, and then I saw that TPIL does the same thing in the section on quotients.

#### [Chris Hughes (Jul 17 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129814544):
I'm not sure what you mean by carrier type, but basically it's struggling to find the setoid instances for the standard relation for quotienting by an ideal. It's particularly bad when I have two ideals in my context, but at the moment I only have one and it's still struggling.

#### [Chris Hughes (Jul 17 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815018):
Deleting my instance for preimage of a ring_hom is an ideal helps, even though my lemma has nothing to do with preimages or ring_homs.

#### [Reid Barton (Jul 17 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815052):
By carrier I mean the type that you're putting an equivalence relation on.

#### [Reid Barton (Jul 17 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815143):
in this case, (the underlying type of) the ring

#### [Reid Barton (Jul 17 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815513):
The equivalence relation here depends on the ideal I, which cannot be inferred from the ring or from instance synthesis.
Basically, when you have an instance which has non-typeclass variables to the left of the colon which don't also appear to the right of the colon, I don't see how Lean can ever select the instance by type class inference.

#### [Patrick Massot (Jul 17 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815620):
We certainly don't want Lean to guess which ideal we want to quotient. And one can always add local setoid instances if we have a whole section of file where the ideal is fixed.

#### [Chris Hughes (Jul 17 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129816521):
@pat
```quote
We certainly don't want Lean to guess which ideal we want to quotient. And one can always add local setoid instances if we have a whole section of file where the ideal is fixed.
```
Not actually that easy to add a local attribute that depends on a variable.

#### [Patrick Massot (Jul 17 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836199):
I see Mario merged your PR (before anyone added your name to the authors list). Did you solve your instance issue?

#### [Mario Carneiro (Jul 17 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836266):
oops

#### [Chris Hughes (Jul 17 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836295):
Not really. I think in general we shouldn't be using type class inference for quotient rings and groups, and maybe we need some infrastructure to deal with that, like a whole load of new quotient lemmas. But I'm not sure. I usually find a way round it, but it's a constant nuisance

#### [Kevin Buzzard (Jul 17 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836545):
Here's another type class inference issue which Keji pointed out to me:

```lean
import group_theory.subgroup 

#check is_subgroup 

example (G : Type) [group G] (H1 H2 : set G) [is_subgroup H1] [is_subgroup H2] : is_subgroup (H1 ∩ H2) :=
{ inv_mem := λ g Hyp,⟨is_subgroup.inv_mem Hyp.1,is_subgroup.inv_mem Hyp.2⟩,
  
}
```
->


```
failed to synthesize type class instance for
G : Type,
_inst_1 : group G,
H1 H2 : set G,
_inst_2 : is_subgroup H1,
_inst_3 : is_subgroup H2
⊢ is_submonoid (H1 ∩ H2)
```

I just wanted to populate the fields of the structure but I couldn't figure out an easy way to do so without proving `is_submonoid (H1 ∩ H2)` first and making it an instance

#### [Kevin Buzzard (Jul 17 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836549):
Is there a way round this?

#### [Patrick Massot (Jul 17 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836743):
```lean
example (G : Type) [group G] (H1 H2 : set G) [is_subgroup H1] [is_subgroup H2] : is_subgroup (H1 ∩ H2) :=
begin
  refine_struct {..},
  sorry, sorry, sorry
end
```
state after first line looks good to me

#### [Chris Hughes (Jul 17 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837625):
```quote
I just wanted to populate the fields of the structure but I couldn't figure out an easy way to do so without proving `is_submonoid (H1 ∩ H2)` first and making it an instance
```
It's probably good practice to make `inter.is_submonoid` an instance first anyway.

#### [Kevin Buzzard (Jul 17 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837657):
Yeah but I was teaching.

#### [Kevin Buzzard (Jul 17 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837666):
I just wanted it to look relatively easy. In the end I re-defined is_subgroup (and didn't import it)

#### [Patrick Massot (Jul 18 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837913):
Full proof could be either
```lean
example (G : Type) [group G] (H1 H2 : set G) [is_subgroup H1] [is_subgroup H2] : is_subgroup (H1 ∩ H2) :=
{ one_mem := ⟨is_submonoid.one_mem H1, is_submonoid.one_mem H2⟩,
  mul_mem := λ a b a_in b_in, ⟨is_submonoid.mul_mem a_in.1 b_in.1, is_submonoid.mul_mem a_in.2 b_in.2⟩,
  inv_mem := λ g Hyp, ⟨is_subgroup.inv_mem Hyp.1,is_subgroup.inv_mem Hyp.2⟩ }
```
or
```lean
example (G : Type) [group G] (H1 H2 : set G) [is_subgroup H1] [is_subgroup H2] : is_subgroup (H1 ∩ H2) :=
begin
  refine_struct {..},
  { exact ⟨is_submonoid.one_mem H1, is_submonoid.one_mem H2⟩ },
  { intros a b a_in b_in,
    exact ⟨is_submonoid.mul_mem a_in.1 b_in.1, is_submonoid.mul_mem a_in.2 b_in.2⟩ }, 
  { intros g Hyp,
    exact ⟨is_subgroup.inv_mem Hyp.1,is_subgroup.inv_mem Hyp.2⟩ }
end
```
depending whether you want to get tactical or not. I'm not sure I understand your question

#### [Patrick Massot (Jul 18 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837927):
The teaching advantage of the tactical way is what I showed in my first answer: Lean tells you want it wants, even putting names on questions

#### [Mario Carneiro (Jul 18 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838009):
I'm going to make a rather radical suggestion and suggest that perhaps `subgroup G` should be a type on its own, like `filter`

#### [Kevin Buzzard (Jul 18 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838032):
I am surprised the first one works! With no structure fields just the `{}` Lean complains it has no `inv_mem` and that type class inference fails to prove `is_submonoid`. I hadn't expected that just declaring the fields anyway would work.

#### [Kevin Buzzard (Jul 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838104):
In particular Lean doesn't put all names on questions -- you have to look at what `is_submonoid` wants -- but that's not too hard.

#### [Patrick Massot (Jul 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838122):
Did you try my suggestion with three `sorry`?

#### [Patrick Massot (Jul 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838129):
The crucial part is Simon's `refine_struct` tactic

#### [Patrick Massot (Jul 18 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838188):
Mario, do you mean bundling the subset and its properties?

#### [Mario Carneiro (Jul 18 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838197):
yes, and adding a `has_mem` instance and so on

#### [Chris Hughes (Jul 18 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838198):
How does that solve the `setoid` problem?

#### [Mario Carneiro (Jul 18 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838200):
what setoid?

#### [Mario Carneiro (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838244):
it solves the typeclass inference problem

#### [Patrick Massot (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838246):
he wants quotients by subgroups

#### [Chris Hughes (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838247):
The problem about inferrinf `setoid` instances for quotient groups and rings.

#### [Mario Carneiro (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838248):
example?

#### [Chris Hughes (Jul 18 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838266):
I don't have an MWE right now, but having two subgroups around means it uses the wrong one sometimes.

#### [Mario Carneiro (Jul 18 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838337):
I don't mean MWE, just sketch the problem. I don't see how two quotient groups with different subgroups can be confused

#### [Chris Hughes (Jul 18 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838361):
It always tries to use the setoid instance with the subgroup which comes last in the statement of the theorem.

#### [Mario Carneiro (Jul 18 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838410):
why are you inferring a setoid instance?

#### [Reid Barton (Jul 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838430):
Because the setoid argument to `quotient.induction_on` is a `[]` argument for some reason

#### [Mario Carneiro (Jul 18 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838483):
you could use `quot.induction_on`...

#### [Chris Hughes (Jul 18 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838552):
What do you suggest in place of `quotient.mk`?

#### [Chris Hughes (Jul 18 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838565):
And there's no `quot.lift_on₂`

#### [Mario Carneiro (Jul 18 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838568):
`quot.mk` of course

#### [Chris Hughes (Jul 18 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838612):
Then I have a really long expression.

#### [Mario Carneiro (Jul 18 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838619):
You usually want to make custom versions of all these anyway

#### [Chris Hughes (Jul 18 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838620):
A `has_coe` instance seems like a sensible substitute.

#### [Chris Hughes (Jul 18 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838634):
How about `quotient.exact`?

#### [Mario Carneiro (Jul 18 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838685):
You can always use `@` if you like the `quotient` version

#### [Mario Carneiro (Jul 18 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838695):
just put `(id _)` in the typeclass slot and it will unify for it instead of use typeclass inference

#### [Chris Hughes (Jul 20 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/130011028):
I had a go at following Mario's recommendation and not using type class inference for setoids for quotient groups. I wanted to find a solution that made it easy, and initially it wasn't. 
I used the follwing definitions
```lean
section quotients
variables {α : Sort*} {β : Type*} {γ : Type*} {φ : Type*} 
  {s₁ : setoid α} {s₂ : setoid β} {s₃ : setoid γ}

@[elab_as_eliminator, reducible]
def quotient.lift_on' (q : quotient s₁) (f : α → φ) 
  (h : ∀ a b, @setoid.r α s₁ a b → f a = f b) : φ := quotient.lift_on q f h

@[elab_as_eliminator, reducible]
def quotient.lift_on₂' (q₁ : quotient s₁) (q₂ : quotient s₂) (f : α → β → γ)
  (h : ∀ a₁ a₂ b₁ b₂, @setoid.r α s₁ a₁ b₁ → @setoid.r β s₂ a₂ b₂ → f a₁ a₂ = f b₁ b₂) : γ :=
quotient.lift_on₂ q₁ q₂ f h

@[elab_as_eliminator]
lemma quotient.induction_on' {p : quotient s₁ → Prop} (q : quotient s₁)
  (h : ∀ a, p (quot.mk s₁.1 a)) : p q := quotient.induction_on q h

@[elab_as_eliminator]
lemma quotient.induction_on₂' {p : quotient s₁ → quotient s₂ → Prop} (q₁ : quotient s₁)
  (q₂ : quotient s₂) (h : ∀ a₁ a₂, p (quot.mk s₁.1 a₁) (@quotient.mk β s₂ a₂)) : p q₁ q₂ :=
quotient.induction_on₂ q₁ q₂ h

@[elab_as_eliminator]
lemma quotient.induction_on₃' {p : quotient s₁ → quotient s₂ → quotient s₃ → Prop} 
  (q₁ : quotient s₁) (q₂ : quotient s₂) (q₃ : quotient s₃) 
  (h : ∀ a₁ a₂ a₃, p (quot.mk s₁.1 a₁) (quot.mk s₂.1 a₂) (quot.mk s₃.1 a₃)) : p q₁ q₂ q₃ :=
quotient.induction_on₃ q₁ q₂ q₃ h

end quotients
```
Using these definitions everything was easy. They differ from the library definitions in two ways, the absence of the `elab_strategy` attribute, not sure what this does, but it makes stuff harder for some reason, and the use of `{}` instead of `[]` for setoids. Using `quot` versions of these lemmas has two problems, one is the `elab_strategy` attribute, and the other is that `quot.lift_on₂` as well as `quot.exact` are not provable without the relations being equivalence relations.

#### [Mario Carneiro (Jul 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/130014064):
Hm, this sounds like reason enough to PR these theorems. (Since we all know that mathlib is collecting patches of core lean theorems.) I actually have no idea what the `elab_strategy` attribute does, I've never heard of it

