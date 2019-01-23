---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43765typeclassissues.html
---

## Stream: [general](index.html)
### Topic: [type class issues](43765typeclassissues.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147694692):
This is amazing: https://gist.githubusercontent.com/jcommelin/8736c28a8e74f3d478b1c2b7737fa513/raw/d655018af064ef75572afb17d2ffb7d051c500c0/crazy_type_class_error.lean
I feel like the algorithm could be a lot smarter here. For example, search for `x_52` on that page, and go to the first match. You will be on the last line of this chunk of code:
```lean
[class_instances] (1) ?x_32 : category
  (@comma {X // B X}
     (@category_theory.full_subcategory (@opens X _inst_1)
        (@site.to_category (@opens X _inst_1) (@category_theory.site X _inst_1))
        (λ (X : @opens X _inst_1), B X))
     punit
     category_theory.punit_category
     (@opens X _inst_1)
     (@site.to_category (@opens X _inst_1) (@category_theory.site X _inst_1))
     (@full_subcategory_inclusion (@opens X _inst_1)
        (@site.to_category (@opens X _inst_1) (@category_theory.site X _inst_1))
        B)
     (@functor.of_obj (@opens X _inst_1) (@site.to_category (@opens X _inst_1) (@category_theory.site X _inst_1)) U)) := @category_theory.comma_category ?x_51 ?x_52 ?x_53 ?x_54 ?x_55 ?x_56 ?x_57 ?x_58
```
So basically it has already figured out all these type class instances, and it should immediately be able to fill in `?x_52` and friends. But it doesn't... and then it hits the search limit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695687):
```lean
[class_instances] (4) ?x_238 : category punit := @category_theory.small_category ?x_422 ?x_423
```
goes all the way down to
```lean
[class_instances] (12) ?x_460 : linear_ordered_field punit := @discrete_linear_ordered_field.to_linear_ordered_field ?x_461 ?x_462
```
I guess it might be a good idea to insert a shortcut somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695787):
looks like the actual solution is `category punit := category_theory.punit_category`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695801):
can we use instance priority to guide the search here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695900):
the funny thing is that `punit`actually has a unique structure of all those classes it looks for

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695970):
@**Reid Barton** I'm really confused, because a lot of the time it is finding that instance. But that sometimes it goes astray...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696000):
Well, it did find it here, eventually

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696077):
Everything looks more or less fine until the max depth error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696157):
Hmmm, would it be good strategy if Lean is searching for an instance of `foo bar` to first check if maybe `bar.foo` exists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696190):
Because that would find `punit.category` instantly...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696563):
Ahrg, this is so annoying. So now I can start writing lots of `@` signs, and insert the typeclass instances manually, and the code becomes unreadable...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696720):
I really doubt how this will scale

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696724):
as we get more things into mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696835):
I think `category_theory.small_category` is misnamed...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697038):
Either :four_leaf_clover: will have to improve the instance search algorithm, or we will have to start being more careful about how we write instances, with other tradeoffs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697069):
@**Mario Carneiro** Can you elaborate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697085):
I now have
```lean
obj := λ U, @limit _ (@category_theory.opposite _
(@category_theory.comma_category _ _ _ category_theory.punit_category _ _ _ _)) _ _
((comma.fst (full_subcategory_inclusion B) (functor.of_obj U)).op ⋙ F) _,
```
and I get red squiggles under the `⋙` at the end.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697150):
Errors:
```lean
failed to synthesize type class instance for
X : Type v,
_inst_1 : topological_space X,
B : set (opens X),
C : Type u,
𝒞 : category C,
F : category_theory.presheaf ↥B C,
U : opens Xᵒᵖ
⊢ category comma (full_subcategory_inclusion B) (functor.of_obj U)ᵒᵖ
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  category_theory.opposite
sheaf.lean:414:66: error

failed to synthesize type class instance for
X : Type v,
_inst_1 : topological_space X,
B : set (opens X),
C : Type u,
𝒞 : category C,
F : category_theory.presheaf ↥B C,
U : opens Xᵒᵖ
⊢ category comma (full_subcategory_inclusion B) (functor.of_obj U)ᵒᵖ
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  category_theory.opposite
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  𝒞
inferred
  ?m_1
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  𝒞
inferred
  ?m_1
Additional information:
/home/jmc/data/math/community-mathlib/category_theory/sheaf.lean:415:20: context: switched to simple application elaboration procedure because failed to use expected type to elaborate it, error message
  type mismatch, term
    limits.limit.pre ?m_7 ?m_9
  has type
    limits.limit ?m_5 ⟶ limits.limit (?m_9 ⋙ ?m_5) : Type ?
  but is expected to have type
    ⁇ U₁ ⟶ ⁇ U₂ : Type v
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  𝒞
inferred
  ?m_1
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  𝒞
inferred
  ?m_1
sheaf.lean:414:66: error

synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  𝒞
inferred
  ?m_1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697169):
`instance [preorder α] : small_category α := ...` got the name `category_theory.small_category`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697217):
Aaah, that's not so nice. That should be in the `preorder` namespace.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697224):
@**Mario Carneiro** talk about `is_ring_hom.is_ring_hom`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697277):
what is that even?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697318):
https://github.com/leanprover/mathlib/blob/master/ring_theory/subring.lean#L28

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697322):
```lean
namespace is_ring_hom

instance {S : set R} [is_subring S] : is_ring_hom (@subtype.val R S) :=
by refine {..} ; intros ; refl

end is_ring_hom
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697323):
guess how this would be called

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697386):
also what on earth is it with the `local attribute [instance] classical.prop_decidable`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697389):
There's also some bug where Lean's normal naming strategy for an instance is not used under certain circumstances (I'm not sure exactly which)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697402):
`classical.prop_decidable` existed long before `classical.dec`, I think it's in the style guide and TPIL

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697419):
I mean, who on earth put it there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697433):
you don't need any classical stuff for subrings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697448):
We could have a strategy where we don't write instances like `instance [preorder α] : small_category α`, but rather `instance [preorder α] : small_category (preorder α)`, where `def preorder α := α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697501):
maybe it was needed once, or a mathematician wrote the file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697510):
```
Authors: Johan Commelin
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697534):
but curiously he was never part of the file's history

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697546):
That would cut out all the silly search starting `preorder punit` (actually it is not really silly, since `punit` could very well be a `preorder`, but anyways we want a different instance)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697571):
I think we need to think about a more principled approach to instance priorities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697726):
for preorder categories, I guess it depends on whether you view it as "a preorder is a special kind of category" or "any preorder can be equipped with a canonical category structure"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697751):
I think we need to refactor the typeclass search system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697754):
but I don't know how any of those things work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697761):
so I might have said nothing in the first place

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697770):
Well I'm not necessarily thinking about anything as anything, I just want to avoid these 20 pages of failed instance searches whenever I try to look for a category instance which is after the preorder one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697771):
:four_leaf_clover:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697786):
I think the instance search is as stupid as `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697792):
it's much worse than `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697793):
and we still haven't fixed the problem with `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697796):
for the love of god

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697859):
who thought depth first search is a good idea (instance) and who thought breadth first search is a good idea (simp)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697865):
but I don't study CS

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697892):
But it's not a tactic, it's built into lean, so there is very little customization or alternatives we can try in lean 3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697903):
at least not without forking lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697923):
OK here is a thought. What if we by convention give each instance which doesn't match against the head a lower priority

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697982):
i.e. each instance of the form \Pi a, ... : C a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698031):
Because of course we want to match against things like ... : C (T a) first, if we're trying to find an instance C (T ...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698041):
@**Mario Carneiro** but from your CS experience, what is the best search method?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698061):
There are two essentially different kinds of instances: "parent coercions" that change the head, and things that change the type to something smaller and leave the head alone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698151):
we know the search terminates in the second case because it's well founded on the structure construction, and in the first case because our tree of classes is finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698155):
```
git grep "^instance" | wc -l
1515
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698156):
that last one is obviously problematic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698176):
because it gets worse as you add more things anywhere in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698179):
I think TREE(3) is also finite so I don't really get your point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698220):
are we satisfied with "it will eventually terminate"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698273):
it's an important first step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698287):
the next question is "how finite" of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698316):
and this depends on how much typeclass caching lean does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698326):
so I'm not sure on the details

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698353):
We want it to be mostly linear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698380):
How about prioritizing type 1? Like Reid suggested?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698457):
Parent coercions have a fixed priority, I don't think we can change it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698471):
This is one place where I think lean is using the wrong search strategy btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698489):
Oh I forgot about parent coercions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698509):
we don't we ask the big guys about the typeclass system  in lean 4?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698568):
If we call type coercions type 1 and parent / "head changing" coercions type 2, then I think we should use backward chaining for type 1 and forward chaining for type 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698636):
For example, if you prove that `ordered_field real` then lean will pre-calculate proofs of `preorder real` and a bunch of other stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698639):
Are we talking about actual parent coercions like from `group` to `monoid`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698640):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698651):
So then there are also things like `preorder` to `category`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698657):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698711):
And I guess both of those fall under type 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698721):
and if you have `ordered_field A` in the context then it calculates `preorder A` when solving typeclass problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698730):
@**Mario Carneiro** how does this work in metamath?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698822):
You get to do this stuff yourself, but there is a smallish spine so it's at most two or three theorem applications to get from anything to anything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698838):
the backward chaining stuff might be done automatically in later versions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698844):
It's all third party stuff though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698856):
So is there any hope we can improve the system in Lean 3?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698861):
this is emphatically not part of "metamath core"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698889):
priorities seem like the best option, but we need a good rule

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698960):
I have hope for reid's proposal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699006):
The obvious, but more annoying variant is to raise the priority of every "type 1" instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699081):
I think Mario said that those were fixed... but maybe I misunderstood which type he referred to...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699099):
I'm also a little confused about Mario's description of the two types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699106):
In Haskell, if we have an instance C (T a b), we call T the instance head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699112):
C is the class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699143):
I'm not sure whether Mario is using the same terminology, or switched the classes or what

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699181):
I called `C` the head there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699257):
so parent coercions change the head, i.e. C a => D a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699274):
and type coercions are like C a , C b => C (T a b)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699409):
I might be wrong in assuming instances like C a, C b => C (T a b) are more common in mathlib--in standard Haskell they're the only kind of instances you are allowed to write

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699421):
(instance C a => D a is illegal)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699422):
That's not true, I think you can do parent coercions in Haskell too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699436):
With GHC extensions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699460):
But the effect is probably like 99% of all instances are of the C (T a b) form

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699675):
oh, I see, there are parent coercions but no user defined parent coercions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699698):
```
class Test a where
  test :: a -> a
class Test a => Test2 a where
  test2 :: a -> a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699702):
this is okay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699713):
There isn't even a coercion in the same sense as in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699716):
There, to write a `Test2` instance, you must first write a `Test` instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699746):
The purpose of `Test a => Test2 a` is instead to avoid writing contexts like `(Test a, Test2 a) => t`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699751):
that's the same as in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699839):
Oh, well... I guess Lean hides the need to write the `Test` instance separately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699854):
```
class Test (a : Type) := (test : a → a)
class Test2 (a : Type) extends Test a := (test2 : a → a)

instance : Test nat := {test := id}
instance : Test2 nat := {test2 := id} --requires the first instance
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699882):
But you can also write `instance : Test2 nat := {test := id, test2 := id}` without the first instance, which has no equivalent in Haskell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699933):
Maybe lean should do that too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699943):
that is essentially requiring the user to do the forward chaining thing I said

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699966):
I actually don't know off-hand how GHC solves a `Test a` constraint if you only have `Test2` in the context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699996):
I wouldn't be surprised if it does forward chaining in that situation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147700076):
you mean when you have `test :: Test2 a => a -> a`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147700092):
Basically, yeah.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147700424):
I think it is complete in Haskell's case to always saturate downwards (derive all superclasses of all the things in the context) and then backward chain from uses (without using any parent coercions)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731225):
Aahrg, Lean is just becoming completely unresponsive when I try to fill in the instances by hand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731254):
Look at the code that I have now: this is getting pretty crazy...
```lean
def extend : presheaf X C :=
{ obj := λ U, @limit.{u v} _ (@category_theory.opposite.{v v} _
(@category_theory.comma_category.{v v v v v v}
  _ (category_theory.full_subcategory.{v v} _)
  _ category_theory.punit_category.{v}
  _ (@site.to_category.{v} (@opens.{v} X _inst_1) (@category_theory.site.{v} X _inst_1)) _ _))
  _ _
((comma.fst (full_subcategory_inclusion B) (functor.of_obj U)).op ⋙ F)
(limits.has_limit_of_has_limits_of_shape.{u v} _),
  map := _ }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 15 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731470):
welcome to the club :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731810):
Ok, I need to confess. I'm making a big fool out of myself. There was actually a missing assumption... so no wonder Lean couldn't find the instance. The code is now back to
```lean
def extend : presheaf X C :=
{ obj := λ U, limit ((comma.fst (full_subcategory_inclusion B) (functor.of_obj U)).op ⋙ F),
  map := _ }
```
**However** it is still taking >10s to typecheck this stuff. Before I removed all the explicit instances, it also took >10s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797050):
@**Johan Commelin** 
> Johan Commelin: So is there any hope we can improve the system in Lean 3?

To improve Lean 3, you need to fork it, and improve it yourself. The development is frozen in the main repo, and all efforts are focused on Lean 4. That being said, nobody should expect Lean 4 will solve all problems and everybody will be happy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797116):
@**Kenny Lau** 
> Kenny Lau: we don't we ask the big guys about the typeclass system in lean 4?

We didn't get there yet. We have only random ideas on how to improve the typeclass system in lean 4.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797179):
@**Kenny Lau** 
> Kenny Lau: I think we need to refactor the typeclass search system

If you want a better typeclass system in the next few months, you should fork the current system, and refactor the typeclass search system yourself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 16 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797342):
@**Leonardo de Moura** Ok, I was hoping that maybe we could use priorities to guide the type class system. Anyway, thanks for the input! And thanks for all you're doing for Lean (3 and 4).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797450):
@**Johan Commelin** Yes, priorities will help. Shortcuts will help too. Example: https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean#L418-L429

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797467):
These are just workarounds.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 16 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800392):
It's not clear to me how much shortcuts actually help, though, because they make the typeclass graph even larger

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 16 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800445):
if you have instances from A -> B -> C and add a shortcut A -> C, then a typeclass search for some unrelated F will traverse both paths to C (and possibly the entire subtree rooted at C)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 16 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800469):
Are there any plans for lean 4 to do anything with the typeclass system?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800852):
You can add the shortcuts using local attributes. In this way, you can add shortcuts to a file without affecting other files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Nov 16 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800886):
Sebastian and I discussed a few improvements (e.g., better indexing and caching), but as I said above these are just ideas on the whiteboard. We didn’t get there yet.

