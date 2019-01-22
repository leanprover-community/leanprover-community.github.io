---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35860categorytheorydocumentation.html
---

## [maths](index.html)
### [category theory documentation](35860categorytheorydocumentation.html)

#### [Simon Hudon (Jan 01 2019 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154133811):
Is there a transcript of the rationale behind the design decisions of the category theory part? Specifically, I'd like to know what were the pros and cons of defining `category` as a type class versus as a structure.

#### [Johan Commelin (Jan 01 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154136146):
I guess one of the big pros of using a type class is that Lean will do more work for you... more automation. And the category theory tries to maximize automation as much as possible.
(There is still a lot more to be done, and in fact more has been done in Scott's repositories. Quite often you will see proof obligations in the category-lib written out explicitly that are transparent in Scott's repos because he has better automation than mathlib.)

#### [Reid Barton (Jan 01 2019 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154137154):
The main pro is it lets you write `a ⟶ b`

#### [Simon Hudon (Jan 01 2019 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138026):
@**Reid Barton** That's a good point. At the same time, that's also a downside because this notation does not tell you which category you're talking of and, I don't know if it's the corner of category theory that I'm in but it seems to be often relevant to distinguish.

#### [Simon Hudon (Jan 01 2019 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138030):
@**Johan Commelin** Can you give me examples of automation that are made possible that way?

#### [Johan Commelin (Jan 01 2019 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138082):
@**Simon Hudon** Maybe it is not so much automation as it is brevity. Now you don't have to feed Lean the category structure when writing down functors or limits (or hom-sets).

#### [Johan Commelin (Jan 01 2019 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138085):
Are you saying that you often have multiple category structures on the same type?

#### [Reid Barton (Jan 01 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138484):
You can always use `@category.hom` explicitly but it might be more convenient (or not) to create synonyms of the underlying type for the different category structures

#### [Simon Hudon (Jan 01 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138486):
Yes. Often might be over stating it as I'm a very fresh category noob. Let's say I'm seeing a repetition in the proofs I find the hardest and this confusion contributes to it

#### [Simon Hudon (Jan 01 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138563):
But Johan, I'm not suggesting that you write `functor C 𝒞 D 𝒟`; rather I'd let `𝒞` and `𝒟` stand for both the carrier type and the data+proofs by using `has_coe_to_sort` (please don't kill me @**Scott Morrison|110087**, I know you're sick of coercions but maybe this time ...)

#### [Simon Hudon (Jan 01 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138657):
```quote
You can always use `@category.hom` explicitly but it might be more convenient (or not) to create synonyms of the underlying type for the different category structures
```
 Maybe you're right. I could write a reducible definition so that I don't have to feed both the type and the instance. It does not make up for the other shortcoming of type classes though: with `category.{u}`, inference is often hindered.

#### [Mario Carneiro (Jan 01 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138672):
`small_category` was supposed to help with that, but I guess it doesn't get used much in favor of more generality

#### [Simon Hudon (Jan 01 2019 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138754):
I thought so. That's too bad!

#### [Reid Barton (Jan 01 2019 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138799):
```quote
But Johan, I'm not suggesting that you write `functor C 𝒞 D 𝒟`; rather I'd let `𝒞` and `𝒟` stand for both the carrier type and the data+proofs by using `has_coe_to_sort` (please don't kill me @**Scott Morrison|110087**, I know you're sick of coercions but maybe this time ...)
```
 This sounds like bundled vs unbundled categories (e.g. https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/bundled.lean). I'm not sure whether bundled categories were ever considered as the primary interface. It seems like it could be a viable option. It's possible that Scott just chose to use unbundled ones on the basis that other structures (groups, etc.) are unbundled.

#### [Johan Commelin (Jan 01 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138871):
Instead of a reducible type, you could also create a `local abbreviation` for `@category.hom`, right?

#### [Simon Hudon (Jan 01 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139060):
I didn't know you could make abbreviation local. Is that useful?

#### [Simon Hudon (Jan 01 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139071):
@**Reid Barton** That looks good! I might steal it for myself. Do you see a downside to having the coercion?

#### [Reid Barton (Jan 01 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139079):
Like at lines 22-23?

#### [Reid Barton (Jan 01 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139082):
To be honest, I've hardly used this at all. I was going to prove that Cat has colimits, but I didn't get very far.

#### [Johan Commelin (Jan 01 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139126):
@**Simon Hudon** I think they have `tspace` as abbreviation for `@topological_space` in the `topological_space.lean` file.

#### [Reid Barton (Jan 01 2019 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139182):
there's some ``local notation `cont` := @continuous _ _`` I think

#### [Johan Commelin (Jan 01 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139194):
```
git grep tspace
analysis/topology/continuity.lean:local notation `tspace` := topological_space
```

#### [Johan Commelin (Jan 01 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139196):
So my memory partly failed me.

#### [Simon Hudon (Jan 01 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139198):
Ah! Ok! It's a local notation, not an an abbreviation

#### [Johan Commelin (Jan 01 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139243):
Right... (I don't even know the difference...)

#### [Reid Barton (Jan 01 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139249):
the difference is nobody knows what `abbreviation` does :smile:

#### [Reid Barton (Jan 01 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139267):
Coercions tend to break down once you have implicit parameters inside the term being coerced that Lean needs to infer.

#### [Simon Hudon (Jan 01 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139279):
Haha! Abbreviation is sometimes useful but if you use it wrong it's pretty annoying because it doesn't come with equations and you can decide to unfold it. And yet, it's not notation because it is represented in the syntax tree, it has a type, etc

#### [Simon Hudon (Jan 01 2019 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139323):
I've seen that, it's true. I hear coercion used to be better in Lean 2.

#### [Reid Barton (Jan 01 2019 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139330):
Maybe an example would be if we had `over X : Cat`, where `X : C` and `C : Cat`, then in `A : over X`, Lean might play dumb and pretend not to be able to figure out what `C` is

#### [Simon Hudon (Jan 01 2019 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139386):
Did it happen with this example?

#### [Reid Barton (Jan 01 2019 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139399):
This is just hypothetical because I never got as far as doing things like that with bundled categories

#### [Reid Barton (Jan 01 2019 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139415):
I guess one could test with something like `def over {C : Cat} (X : C) : Cat := C` (not the right definition, but it shouldn't matter) and then try to use the coercion

#### [Reid Barton (Jan 01 2019 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139465):
It also might only fail when Lean needs to use information from outside the thing being coerced to infer implicit arguments inside it--not sure

#### [Simon Hudon (Jan 01 2019 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139611):
I mostly ran into trouble when using coercion to function types and never with coerce to sort. And one reason I would run into trouble was that I coerced to a polymorphic function type and I needed to infer some of the type parameters and Lean would just give up

#### [Simon Hudon (Jan 01 2019 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139820):
I think I'll run an experiment with reformulating mathlib that way and see how difficult it is

#### [Reid Barton (Jan 01 2019 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139854):
Yeah, I can't remember having any issues with coercions to sort either

#### [Simon Hudon (Jan 01 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154140187):
I just had a quick look and the following works:

```lean
structure cat : Type.{max (u+1) v+1} :=
(carrier : Type u)
[inst : category.{v} carrier]

instance has_coe_to_sort.cat : has_coe_to_sort cat.{u v} :=
{ S := Type u,
  coe := cat.carrier }

def Hom {C : cat.{u v}} (x y : C) : Type v := @category.hom _ C.inst x y

variables {C : cat.{u v}} (x y : C)

#check Hom x y
```

#### [Simon Hudon (Jan 01 2019 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154140275):
And then I can define the following notation:

```lean
notation x ` ⟶[` c `] ` y := Hom c x y
#check Hom C x y
-- x ⟶[C] y : Type v

local infix ` ⟶ ` := Hom _

#check Hom C x y
-- x ⟶ y : Type v
```

#### [Reid Barton (Jan 01 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154140405):
A bonus is that we can now give the category of types the correct name, namely **Set**

#### [Johan Commelin (Jan 01 2019 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154141701):
@**Simon Hudon** Don't you mean to make the argument `C` to `Hom` *explicit*?

#### [Simon Hudon (Jan 01 2019 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154141723):
@**Johan Commelin** Yes you're right! I changed it in my file and didn't bother fixing it here but it does matter you're right

#### [Simon Hudon (Jan 01 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154141731):
@**Reid Barton** Wouldn't you define *Set* using `set_theory` instead?

#### [Reid Barton (Jan 01 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142219):
Nope!

#### [Reid Barton (Jan 01 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142273):
It would be messy, and equivalent anyways

#### [Reid Barton (Jan 01 2019 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142345):
`set_theory` sets have notions like global membership/subset predicates, which aren't relevant to Set

#### [Simon Hudon (Jan 01 2019 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142459):
Oh! That simplifies a lot! I was trying to understand pushouts and pullbacks and on ncatlab.org, they refer to Set a lot so I kind of pulled back from them

#### [Reid Barton (Jan 01 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142511):
The dictionary for reading mathematics is `Type` = set, and `set` = subset

#### [Reid Barton (Jan 01 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142514):
(outside of set theory of course)

#### [Simon Hudon (Jan 01 2019 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142524):
Ooooh

