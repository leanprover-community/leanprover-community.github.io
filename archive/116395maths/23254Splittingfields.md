---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/23254Splittingfields.html
---

## Stream: [maths](index.html)
### Topic: [Splitting fields](23254Splittingfields.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 12 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151535820):
So I thought I'd revive the splitting fields branch on community mathlib. So far I've just updated it to work with current mathlib. This is my definition of splitting fields. It's a bit unusual to write a recursive function like this returning a Type; is this a good approach? Also my definition of `of_field` the embedding from the base field gives me the error `rec_fn_macro only allowed in meta definitions`. What is this?
```lean
def splitting_field' : Π {n : ℕ} {α : Type u} [discrete_field α] (f : by exactI polynomial α),
  by exactI nat_degree f = n → Type u
| 0 := λ α I f hn, α 
| 1 := λ α I f hn, α
| (n + 2) := λ α I f hn, by exactI 
  have hf : nat_degree (f.map (coe : α → adjoin_root (irr_factor f (by rw hn; exact dec_trivial))) / 
    (X - C root)) = n + 1, from sorry,
  splitting_field' (f.map (coe : α → adjoin_root (irr_factor f (by rw hn; exact dec_trivial))) / 
    (X - C root)) hf

def of_field' : Π {n : ℕ} {α : Type u} [discrete_field α] (f : by exactI polynomial α)
  (hf : by exactI nat_degree f = n), α → by exactI splitting_field' f hf
| 0     := λ α I f hf a, a
| 1     := λ α I f hf a, a
| (n+2) := λ α I f hf a, by exactI of_field' _ _ (↑a : adjoin_root _)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 12 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151536840):
Okay I still get the error `rec_fn_macro only allowed in meta definitions` even if I make it `meta`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 12 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151536970):
Could you rearrange the arguments so that ` {α : Type u} [discrete_field α]` are left of the colon? If nothing else it will let you get rid of the `exactI`s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 12 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151536981):
That error sounds like something funny in the equation compiler, so simplifying its job might help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 12 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537095):
Not without changing my method significantly. I use a different type when I recursively call it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 12 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537161):
Oh, yeah, sorry. I misread that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 12 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537354):
Where is `adjoin_root` defined?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 12 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537395):
In the splitting field branch on community, I take it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 12 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537405):
Think I'm having trouble reading today.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537835):
@**Chris Hughes** I think this is exactly the approach that we had in mind when @**Mario Carneiro**, you and me were hacking on this in Orsay. Too bad it's giving troubles.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151538608):
I'm always tempted to package everything I care about together in a single recursive definition--here the type, its field instance, the map from the base field, the factorization of f

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151538615):
using a big sigma or a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 12 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151541456):
I found a work around by using `nat.rec_on` instead of the equation compiler. Seems like it has something to do with this https://github.com/leanprover/lean/issues/1890

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 12 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151552987):
@**Chris Hughes** I think that this thread should know about this thread: https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple.20field.20theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151806515):
I've had a new problem, and it's taken me most of the day to figure out what's going on. I think the trouble is that I have an expression where `f : polynomial α` is mentioned and also some stuff of type `adjoin_root f`. When I try to rewrite with `f = _` It tries to rewrite all the types that mention `f` and hangs. I solved it using `conv` but I thought there might be a better way to do this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 15 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151831239):
Isn't this what `conv` is meant for? I think there's nothing wrong with using it here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868222):
So I've some up against a more serious problem. I've defined something of this type
```lean
lemma splitting_field_aux : Π {α : Type u} [discrete_field α] (f : by exactI polynomial α),
  by exactI Σ' (β : Type u) [discrete_field β] (i : α → β) [is_field_hom i]
  (hs : by exactI splits i f), ∀ {γ : Type u} [discrete_field γ] (j : α → γ)
  [is_field_hom j] (hj : by exactI splits j f),
  ∃ k : β → γ, (∀ x, k (i x) = j x) ∧ is_field_hom k
```
I bundled everything we needed to know together in one definition because I didn't want to have to deal with `eq.rec` and non definitional equation lemmas. The only trouble with this approach is that the homomorphism from the splitting field into any field that splits only goes into fields in the same universe. The only way around this that I can see is to unbundle the definition, and deal with nasty equation lemmas. Is there any easier way around this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 16 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868598):
I'm inclined to say that we shouldn't worry about universes here. If universe issues show up, I hope `ulift` will help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 16 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868614):
good luck transporting everything to `ulift` :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868620):
what is the problem with unbundling exactly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868667):
I guess that would be much more convenient to use if it were unbundled, although maybe you need this for the construction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868675):
I think you should try to stay away from "universal definitions" of universal objects, because they are never universe polymorphic enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868679):
Then I'd have to unfold the definition to prove things about it. And the equation lemmas are not definitional, so I'd need eq.rec to turn it into `adjoin_root whatever ` and eq.rec is hard to use.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868720):
What do you mean by stay away from universal definitions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868721):
right, we definitely want to avoid that. But I'm still not following. Could you show a bit of how you get to this point?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868729):
For example, you can define `nat := \forall X, {X -> (X -> X) -> X // naturality property}` but it's not a good definition because `X` only lives in one universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868774):
https://github.com/ChrisHughes24/mathlib/blob/5efef7b26f78b5bcbcbc43d4d3ae32be7aa6018b/field_theory/splitting_field.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868775):
instead you want some kind of "intrinsic" characterization of the object that implies the universal property, in any universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868790):
So in this example, maybe the fact that any proper subfield does not split?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868793):
I'll have to think about whether that approach is much harder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868957):
In this case, it looks like that is indeed the right "smallness" property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868963):
another way to express it is to start from the theorem you just proved, and show that splitting in one universe implies splitting in all the rest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868966):
by taking a special choice of gamma, namely the subfield isomorphic to the gamma in another universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869580):
Proving that such a subfield exists is hard though, unless I'm missing a trick?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869584):
This is a general fact about fields

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869631):
Every field hom is injective, so when you restrict to the range you get an isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869647):
(the isomorphism is not constructive in the reverse direction)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869788):
I still don't understand. Given a field, which subfield do I choose?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869922):
oh wait I had it backwards, you need a field *into* the large universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869945):
for that you can take a subfield of gamma sufficiently large to contain all the action from beta

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869949):
like the subfield generated by polynomials in alpha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870003):
this subfield will be isomorphic to a quotient of a polynomial ring etc etc which is in `Type u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870007):
I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870008):
and so your lemma applies and the polynomial splits there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870059):
you should double check with @**Kevin Buzzard** , I walked him through this a few months ago and I think he did almost exactly the same thing in the perfectoid project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870110):
as an alternative, returning to the unbundling problem: I assume the reason it isn't definitional is because you are using wf recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870112):
If you define one step of the induction as a lemma, then it will be definitional there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870163):
That sounds easier.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870166):
so you have something like `F : (A : Type u) (h : P.{u} A), Type u` and `prop : (A : Type u) (h : P.{u} A), P.{v} (F A)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870228):
and then you have an induction proof putting it together, which does `F /\ P.{u} F`, and a cases proof doing the same thing with conclusion `P.{v} F`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870287):
It's also not definitional because I've got an `ite` on `degree f \le 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870289):
Also, before I forget: a very general way of avoiding problems with types defined by complicated rules is to use an inductive type instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870347):
for example, simulating `if x < 2 then nat else unit`:
```lean
inductive my_cases (x : ℕ) : Type
| nat : x < 2 → nat → my_cases
| unit : x >= 2 → unit → my_cases
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870352):
You can do similar stuff with crazy well founded definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870393):
in the inductive case you don't even have to worry about well foundedness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870896):
The other major issue I have is that making it a def gives me the error `rec_fn_macro` only allowed in meta definitions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871212):
that means there is probably a tactic referencing one of the `_match` type variables in the context by accident

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871259):
you can fix this by `clear`ing it when you have used it, or even using it right at the start and clearing it then (or if its random junk then just remove it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871614):
Will `resetI` cause problems with that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871616):
I don't think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 16 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871661):
At some version of `resetI` I recall it deleting the recursive function variable as a side effect, not sure if that's still the case but I think not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 16 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151874009):
I've only just seen this thread. Chris I'll dig out the universe conversation Mario and I had when I'm at a pc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018880):
All done and sorry free. @**Mario Carneiro** are you happy for me to push all of this to the splitting fields branch in community?
```lean
def splitting_field (f : polynomial α) := splitting_field.type_aux f rfl

namespace splitting_field

instance field (f : polynomial α) : discrete_field (splitting_field f) :=
by unfold splitting_field; apply_instance

def mk (f : polynomial α) : α → splitting_field f := mk_aux f rfl

instance (f : polynomial α) : is_field_hom (mk f) :=
by unfold mk; apply_instance

lemma splitting_field_splits (f : polynomial α) : splits (mk f) f :=
(splitting_field_aux f rfl).2.2.2.2

def hom {β : Type v} [discrete_field β] (i : α → β) [is_field_hom i] (f : polynomial α)
  (hβ : splits i f) : splitting_field f → β :=
classical.some (exists_hom _ f rfl i hβ)

@[instance] lemma hom_is_field_hom {β : Type v} [discrete_field β] (i : α → β) [is_field_hom i]
  (f : polynomial α) (hβ : splits i f) : is_field_hom (hom i f hβ) :=
(classical.some_spec (exists_hom _ f rfl i hβ)).2

@[simp] lemma hom_fixes {β : Type v} [discrete_field β] (i : α → β) [is_field_hom i]
  (f : polynomial α) (hβ : splits i f) : ∀ x, hom i f hβ (mk f x) = i x :=
(classical.some_spec (exists_hom _ f rfl i hβ)).1

attribute [irreducible] hom splitting_field splitting_field.field splitting_field.mk
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018894):
@**Chris Hughes** so how did you extract an element from `factor_set`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018952):
I proved the irreducible factor lemma for a noetherian domain.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018963):
see @**Mario Carneiro** this is problematic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019049):
I don't think it's problematic. You shouldn't use UFD for that anyway since it's true in greater generality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019448):
Looks good to me, although I would call `hom` `lift` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019459):
what's problematic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019463):
that `factor_set` is hard to use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019540):
demo? what's `factor_set` doing here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019543):
well could you prove that the factor set of a non-unit non-zero element is nonempty?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019546):
what is `factor_set`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019590):
`associates.factor_set`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019591):
Kenny, you shouldn't be so negative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019604):
it's not in the mathlib version, remind me what it does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019613):
```lean
associates.factors :
  Π {α : Type u_1} [_inst_1 : integral_domain α] [_inst_2 : unique_factorization_domain α]
  [_inst_3 : decidable_eq (associates α)], associates α → associates.factor_set α
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019624):
@**Patrick Massot** well played

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019637):
If it was empty the product would be one. Seems like it's probably not that hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019643):
oh it's a ufd thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019646):
how about that any non-zero non-unit is divisible by an irreducible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019685):
how do we convert from factors to divisibility

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019697):
`dvd_eq_le`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019698):
Prove that a UFD is noetherian, and use the lemma I proved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019702):
and `factors_le`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019721):
I see @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019761):
it's a bit cumbersome to state, but it looks like the lemmas are there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019840):
Anyway I think you could certainly push this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019848):
next stop algebraic closure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019851):
I guess that's another messy induction like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152022286):
Before going towards algebraic closure, I would like to have this PR'd. This is going to be a very useful tool in the theory if finite extensions. I think it makes sense to start defining `separable` and `normal` extensions now. We're pretty close to finite Galois extensions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152022370):
@**Chris Hughes** What are your plans now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023539):
@**Chris Hughes** I merged master into this branch and pushed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023867):
This branch does now depend on unmerged PRs that I have made.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023951):
The one on multiplicities?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023975):
And some others. I have three open to do with polynomials right now I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152024033):
Yes, I see. Ok, let's hope those get merged soon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152024064):
Do you want to do more with this branch? I mean, it's name is `splitting_fields`, so maybe new stuff should happen on a new branch?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152024628):
I think new stuff should happen on a new branch. I think it's best to not make PRs too big.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152025969):
So, if I'm not mistaken... the first 10 points of https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md have now been done. (Although not everything is in mathlib yet.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026250):
Kenny, do you mind if I copy-paste that roadmap to the github wiki of the community repo? Then we can start ticking of things that we've done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026341):
might want to replace the whole discriminant business with just GCD? ah the beauty of impredicativity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026448):
According to wiki, a polynomial is separable if it has just as many roots in its splitting field as its degree. So a square of a separable polynomial is not separable... choices...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026483):
I don't think we're talking about the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026504):
No, indeed. I was asking if we should copy your roadmap to the github wiki...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027091):
and I was asking if you might want to change 11-14 to just 14

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027295):
That seems like a good plan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027590):
@**Johan Commelin** and my only objection would be predicativity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027650):
which I'm sure less people care about, compared to constructivity...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152033427):
https://github.com/leanprover-community/mathlib/wiki/Algebraic-closure-roadmap

