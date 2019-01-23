---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28918vectorspacesvsmodulesoverafield.html
---

## Stream: [maths](index.html)
### Topic: [vector spaces vs modules over a field](28918vectorspacesvsmodulesoverafield.html)

---

#### [Johan Commelin (Jun 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128233939):
I have a module over a field. How do I upgrade it to a vector_space? We can't have a generic instance, because we would immediately get loops (every vector_space is already a module).

#### [Johan Commelin (Jun 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128233981):
I really wish this would be transparent, because there is no content at all.

#### [Chris Hughes (Jun 18 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237488):
Something like this?
```lean
import linear_algebra.basic

variables {F : Type*} [field F] {M : Type*} [m : module F M]

instance Mvector_space : vector_space F M := {..m}
```

#### [Gabriel Ebner (Jun 18 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237549):
Maybe make vector_space a reducible definition for module?

#### [Johan Commelin (Jun 18 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237680):
@**Chris Hughes** That is tricky right? Because then we get cycles in the type class system.

#### [Johan Commelin (Jun 18 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237682):
@**Gabriel Ebner** How do I make a class reducible?

#### [Chris Hughes (Jun 18 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237786):
I agree it does seem a little silly. I'm not sure we'd get cycles any more than we would by any other use of extends. This is a little weird because there aren't any extra axioms, but extends is used all the time without any problems.

#### [Chris Hughes (Jun 18 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237806):
In fact just making what I just wrote a global instance is probably a good idea.

#### [Gabriel Ebner (Jun 18 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237812):
Not class, just `@[reducible] def vector_space (α : Type u) (β : Type v) [field α] := module α β`

#### [Johan Commelin (Jun 18 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237871):
But then we can't use the type class instance anymore...

#### [Johan Commelin (Jun 18 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237896):
Chris, Hmmm, I thought introducing cycles was a bad idea. I think we try to avoid them.

#### [Johan Commelin (Jun 18 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237910):
`extends` does not introduce cycles. So I don't understand your point.

#### [Chris Hughes (Jun 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238026):
The definition of `vector_space` just `extends` `module` with no extra axioms. So it won't introduce cycles.

#### [Chris Hughes (Jun 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238028):
If `extends` doesn't introduce cycles.

#### [Gabriel Ebner (Jun 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238029):
@**Chris Hughes** There is the cycle module -> vector_space -> module.

#### [Gabriel Ebner (Jun 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238033):
(If you add the instance.)

#### [Chris Hughes (Jun 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238038):
Oh I see.

#### [Gabriel Ebner (Jun 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238046):
@**Johan Commelin** I just tried replacing the vector_space class by a definition and everything seems to work.  Why do you think it would break type class instances?

#### [Johan Commelin (Jun 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238097):
I mean, then I can't any longer write `{V : Type} [vector_space real V]` in my theorems. Right?

#### [Johan Commelin (Jun 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238103):
Because the `[]` only work for classes.

#### [Chris Hughes (Jun 18 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238156):
Maybe it will just interpret it as `module real V`

#### [Johan Commelin (Jun 18 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238167):
The reason that nothing breaks after your change, is because mathlib has not *really used* vector spaces yet. It only defines them...

#### [Johan Commelin (Jun 18 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238185):
Chris, hmm, that might be true! Then it might work!

#### [Johan Commelin (Jun 18 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238264):
@**Gabriel Ebner** Ok, I see that in fact on the line below there is already `[vector_space ...]` and it seems to work. You are right. Thanks!

#### [Mario Carneiro (Jun 18 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242421):
IIRC I set this up before (`vector_space` as reducible def) and @**Johannes Hölzl** reverted it to the current wrapper class style, so there was probably a reason although I forget what it is.

#### [Mario Carneiro (Jun 18 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242443):
I think the preferred solution is just to have instances of `vector_space` for all your vector spaces

#### [Johan Commelin (Jun 18 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242581):
Ok, but aren't you scared that this creates cycles?

#### [Mario Carneiro (Jun 18 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242598):
Chris's instance will create cycles. I'm not suggesting that

#### [Johan Commelin (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242640):
Or, you mean, explicitly saying
```lean
instance foobar : vector_space real V := {}
```

#### [Johan Commelin (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242648):
whenever `V` is a module over the reals.

#### [Mario Carneiro (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242649):
depends on what `V` is there

#### [Mario Carneiro (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242659):
if `V` is an arbitrary module over the reals, then no

#### [Mario Carneiro (Jun 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242677):
if you replace `V` with `my_R_vec` then yes

#### [Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242737):
If you want to deal with an arbitrary real vector space, the assumption should say `vector_space` not `module`

#### [Chris Hughes (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242744):
What happens if you have something like a vector space instance for polynomials over a field, but also a module instance for polynomials over a ring. Then you have cycles.

#### [Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242750):
no

#### [Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242752):
that's perfectly okay

#### [Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242755):
that's a diamond not a cycle

#### [Mario Carneiro (Jun 18 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242763):
and the defeq constraint will be easy to satisfy here

#### [Johan Commelin (Jun 18 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242909):
Mario, I am defining Lie algebras. They are modules over a ring with extra data and properties. But if my ring happens to be a field, then I want to prove extra things about my Lie algebras (using things like `dimension` etc...). How should I explain to Lean that if I have `[field R]` I want to upgrade my `[lie_algebra L]` to a `[vector_space R L]` instead of just the `module R L` that it extends?

#### [Mario Carneiro (Jun 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243070):
you can have an instance for that

#### [Mario Carneiro (Jun 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243075):
`instance [field R] [lie_algebra L] : vector_space R L`

#### [Johan Commelin (Jun 18 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243174):
ok, I see

#### [Johan Commelin (Jun 18 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243182):
That's a good solution, I guess (-;

#### [Johannes Hölzl (Jun 18 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128263024):
I don't remember why I changed it to a `class` maybe I had a problem in combination with the `inout` parameter. We can change it back and see what happens.

