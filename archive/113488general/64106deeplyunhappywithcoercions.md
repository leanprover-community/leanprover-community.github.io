---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64106deeplyunhappywithcoercions.html
---

## Stream: [general](index.html)
### Topic: [deeply unhappy with coercions](64106deeplyunhappywithcoercions.html)

---


{% raw %}
#### [ Scott Morrison (Oct 25 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441426):
We've tried using coercions throughout the `category_theory/` development within mathlib, so that one can write `F X` for a functor applied to an object, and `a X` for a natural transformation applied to an object.

#### [ Scott Morrison (Oct 25 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441491):
This causes a lot of problems. In particular coercions incorrectly applied, deep inside the enormous implicit arguments common in dependent type theory, cause `simp` and `rw` to often fail.

#### [ Scott Morrison (Oct 25 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441521):
I think I'm about ready to declare the experiment of using coercions a failure, and to rip them out  of the category_theory development for now.

#### [ Scott Morrison (Oct 25 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441610):
The time I have wasted diagnosing "why won't simp just do this" seems to far outweigh the value of not having to write `F.obj X` or `a.app X`.

#### [ Scott Morrison (Oct 25 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441741):
Just as a typical example:
```
rewrite tactic failed, did not find instance of the pattern in the target expression
  ⇑α X ≫ ⇑(iso.symm α) X
state:
C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
⊢ ⇑↑α X ≫ ⇑↑(iso.symm α) X = ?m_1
```

#### [ Scott Morrison (Oct 25 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441750):
`erw` works fine, but `rw` and `simp` choke.

#### [ Chris Hughes (Oct 25 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441768):
Make a `simp` lemma that simplifies the double coercions?

#### [ Scott Morrison (Oct 25 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441979):
I mean, yes, I can try that. But diagnosing what the double coercion going on here actually is will take me more time than I ever would have spent in the entire history of working on mathlib writing out the explicit `.obj` and `.app` fields myself...

#### [ Scott Morrison (Oct 25 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447529):
And yet more examples, in the same proof, all caused by coercions.

With tactic state:
```
C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
⊢ ⇑(functor.map (functor.const J) (𝟙 (x.X))) X ≫ ⇑(x.π) X = ⇑(x.π) X
```
Of course `simp` should work, by applying the `@[simp]` lemma `functor.map_id`. It doesn't, even though `rw functor.map_id` works fine. The reason of course is because the coercion to function types break `simp`, because it doesn't have congruence lemmas that let it reliably step inside dependent functions.

#### [ Scott Morrison (Oct 25 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447573):
You can see a similar thing if you instead try to `conv` your way in:

#### [ Scott Morrison (Oct 25 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447584):
`conv {to_lhs, congr}` gets you to the state 
```
2 goals
C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
| ⇑(functor.map (functor.const J) (𝟙 (x.X))) X

C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
| ⇑(x.π) X
```

#### [ Scott Morrison (Oct 25 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447597):
but one further `congr` (which should step us inside the coercion), just says `congr tactic failed, unsupported congruence lemma`.

#### [ Scott Morrison (Oct 25 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447602):
On every front, coercions are just unpleasant.

#### [ Chris Hughes (Oct 25 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136449146):
The dependent argument problem is a biggy. It might even be fixed by having a non-dependent `has_coe_to_fun` class, since most of them are non-dependent anyway.

#### [ Scott Morrison (Oct 25 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136450130):
I think all my cases really are coercions to dependent function types.

#### [ Chris Hughes (Oct 25 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136450426):
Won't it still break simp if you don't use `coe_to_fun` then?

#### [ Johan Commelin (Oct 25 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136453416):
@**Scott Morrison|110087** two reactions:
* Reading this makes me sad. It shows that we aren't there yet. I hope Lean 4 fixes this, maybe using the idea of Reid to have type-dependent notation.
* Writing `.obj`, `.map` and `.app` isn't so much of a hassle. I'll get used to it quickly.

#### [ Floris van Doorn (Oct 25 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136455046):
The coercion mechanism in Lean 3 was one of the major headaches/bottlenecks in porting the HoTT library from Lean 2 to Lean 3. In Lean 2, coercions worked much better. My two main complaints with the coercion mechanism in Lean 3 (neither of which was a problem in Lean 2):
* The  same complaint as Scott gave: it is super hard to make coercions reduce well. You need lemmas to rewrite the non-coercion function to the coercion (or the other way around), and you need to make sure that *all* simplification lemmas use the "normal form": either they all use coercions, or all use the underlying function explicitly.
* Lean 3 is more restrictive when inserting coercions. If the preprocessor has found out that `F : functor ?M1 ?M2` and it needs to be of type `?M3 -> ?M4` (for example, when it is applied to a term), then in Lean 3, the coercion mechanism doesn't fire yet, because for some reason, it needs to know the exact type of `F` without any metavariables in it. In Lean 2, a coercion was inserted, and then from the context, it could afterwards figure out the exact value of the metavariables.

#### [ Kevin Buzzard (Oct 25 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136456991):
There is some sort of sociological side to all of this. As mathematicians we are *so used* to these coercions that the thought of some computer claiming that they can do all pure maths means that surely it must be smart enough to do the coercions too, like us. But of course we know they're there, and it is a *complete triviality* to write them ("if I write $$F(X)$$ it's clearly the functor on objects; if I write $$F(f)$$ it's clearly the functor on morphisms, so I guess I could write `F.obj` easily, it's not as if I don't know which one I'm using"). This now raises the question -- if it's so easy, how come the computer can't do it? But if Scott has found an answer to this (and of course he may not have -- one can't rule out Mario just appearing and saying "do this trick and it'll be fine") then so be it. I know at all times if I'm applying my functor to an object or a morphism and I'm not scared of telling you, if you really want to know.

#### [ Reid Barton (Oct 25 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136479587):
I think I was one of the people asking for coercions in category theory. However, when I tried upgrading the mathlib dependency of my homotopy theory project to the version which uses coercions, I also found them to be much more of a hassle then they were worth. So, I'm actually glad to hear that Scott is of the same opinion.

#### [ Reid Barton (Oct 25 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136479710):
It really is the combination of the two points mentioned by Floris: `simp` really wants you to write the same thing in the same way every time, but coercions are not always conveniently available because of the way they interact with metavariables.

#### [ Reid Barton (Oct 25 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136479750):
On the plus side, I now have a better understanding of how to use `erw` :)

#### [ Scott Morrison (Oct 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136534446):
So, ... @**Mario Carneiro** and @**Johannes Hölzl**, how would you feel about me exploring removing the coercions from `category_theory/`?

#### [ Johannes Hölzl (Oct 26 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136535059):
I would prefer them to stay. But I can see why you want to remove them. In your original example `⇑↑α X ≫ ⇑↑(iso.symm α) X = ?m_1`, where does the coercion on `↑α` and `↑(iso.symm α)` come from?

#### [ Scott Morrison (Oct 26 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536337):
There are coercions there from isomorphisms to morphisms, and from natural transformations to the component function.

#### [ Scott Morrison (Oct 26 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536358):
That original example is not the complaint I should have started with. Adding yet more simp lemmas about certain classes of double coercions solves it.

#### [ Scott Morrison (Oct 26 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536525):
The real problems are:
* the presence of coercions to dependent function types significantly inhibits `simp` and `conv`, forcing us to construct long `rw` proofs by hand
* even in rewrite proofs, we find ourselves having to use `erw` instead of `rw` at mysterious moments, because of coercions not being in the perfect form deep inside implicit arguments
* it's an extra "dimension" for `simp` to work in, and we need to consistently simp everything back to the coerced form.
* sometimes the coercions just don't fire, and so we need to write things explicitly, and then perform trickery to rewrite lemmas back into coerced form, so they are relevant in the "always use coercions" world.

#### [ Scott Morrison (Oct 26 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536535):
In all, very unpleasant.


{% endraw %}
