---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72014subrings.html
---

## Stream: [maths](index.html)
### Topic: [subrings](72014subrings.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127699034):
```lean
/-- `S` is a subgroup: a set containing 1 and closed under multiplication, addition and and additive inverse. -/
class is_subring  (S : set R) : Prop := -- would like `extends is_add_subgroup`, but that class doesn't exist
(one_mem       : (1 : R) ∈ S)
(mul_mem {x y} : x ∈ S → y ∈ S → x * y ∈ S)
(add_mem {x y} : x ∈ S → y ∈ S → x + y ∈ S)
(inv_mem {x}   : x ∈ S → -x ∈ S)

instance subtype.ring {S : set R} [is_subring S] : ring S := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127699067):
I think the route of defining `is_add_subgroup` will pay off in the end. Is this again one of those things where `[to_additive]` should help? The last time I tried that, it didn't work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127699721):
Ok, the easy way out: I'll extend `is_submonoid`. Even though it feels "unmathematical" to me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127703755):
A minimalist definition of subgroup is : non-empty and closed under lam x y,xy^{-1}. Is there any point using this minimalist definition? You could do the same with add_mem and inv_mem here. Does this save time or obfuscate? Or both?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127706197):
I think it would be best if we could extend both `is_submonoid` and `is_add_subgroup`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 07 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127711064):
Regarding minimalist definitions (`x * y^{-1}`), I think it is best if the official definition is the bog standard definition, with no clever tricks or surprises. It's fine to then provide an alternative constructor which allows you to take advantage of shortcuts like this if you want them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127711149):
Until the constructions become seriously dire, I think it's best to optimise definitions to be usable (after you've constructed instances), rather than easy to satisfy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127711160):
(Of course actually redundant things should be lemmas.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127723434):
https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring/src/for_mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127723435):
Here is a small start on subrings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758357):
Update: https://github.com/jcommelin/lean-perfectoid-spaces/blob/subring/src/for_mathlib/subring.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758368):
@**Kevin Buzzard** what do you think is the best strategy for integral elements?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758422):
Were univariate polynomials already there? Somewhere? Did Chris or Nicholas do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758494):
I think lots of people did univariate polynomials

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758500):
but I don't know if anyone submitted a PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758507):
I think Kenny proved a universal property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758520):
@**Chris Hughes** @**Kenny Lau** @**Johannes Hölzl** Did any of you PR a definition of a polynomial in 1 variable into mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758567):
@**Johan Commelin** Note that for the definition of a perfectoid space it might be the case that one only has to formalise the definition, i.e. "I am a root of a monic poly with coefficients in the smaller ring"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758569):
Yes, that is what I am currently trying to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758571):
To prove integral closure is a ring will involve some Noetherian arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758572):
but I am not sure this result is needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758573):
We need "I am a subring of R^o"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758574):
but I am not sure we need "...and by the way R^o is a ring"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758614):
Right, we never take the closure (-; We only have stuff that already is a subring, and then prove it is closed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758621):
Oooh, what you are saying is different from what I was saying...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 08 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127762328):
@**Kevin Buzzard**  There are no univariate polynomials in mathlib or in a PR. I want to move the polynomials from Mason-Stother proof in July / August.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 08 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127766040):
I will do that once I've done my project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127766743):
What is the best way to define the n-th power of an ideal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127767182):
Current proposal:
```lean
span {i | ∃ x : multiset I, x.card = n ∧ i = (x.map subtype.val).prod}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772173):
I think Kenny did product of ideals so you could just define them recursively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 08 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772572):
Are Kenny's ideals a subtype parameterised by the ring? I guess they form a monoid? Then you could just write `I ^ n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772627):
But `I` has type `set R`. And there is some instance hanging around telling you that it is an ideal. So now Lean wants `have_pow (set R) nat`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772630):
And that doesn't make sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772637):
But maybe I'm missing something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773371):
It doesn't make sense to a mathematician -- that's what you're missing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773379):
I think the idea in CS is that you just define I*J for I and J sets to be the ideal generated by the ij

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773380):
why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773388):
it's the same math/CS thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773391):
it's just like dividing by zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773393):
Is that even a CS thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773396):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773400):
nobody divides by zero except CS people

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773404):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773405):
maybe applied mathematicians do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773407):
no not even them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773408):
where's the division by zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773409):
they only do 0 / 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773413):
the "division by zero" is when you multiply two sets that are not ideals together

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773414):
when nobody in their right mind would do this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773415):
presumably this is exactly what is meant by I^n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773416):
Exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773470):
The notion A*B for A,B sets is well defined even if they are not ideals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773472):
It's just a different way of thinking about things. I know exactly why Johan is confused.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773485):
Yes, well-defined and kind-of pointless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773486):
but if you want to restrict to ideals, it makes no difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773487):
so we don't think of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773488):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773491):
and then whenever you apply it, you are probably carrying around a proof that things are ideals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773495):
not at all pointless, the notation is not limited to ring theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773497):
This is just another instance of this canonical disconnect

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773503):
we only define things where we need them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773513):
you over-define and sift later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773516):
it's just cultural

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773523):
I'm certain I've seen A - B and A + B and other things as well with weirder sets than ideals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773576):
i.e. "prove C + C = [0, 2] where C is the cantor set"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773599):
0/0 is also well-defined. It is 57.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773615):
but I'm not even stressing this domain of definition, define it on ideals if you want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773623):
you can still define I^n that way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773630):
And `A * B` for `A B : set R` has two definitions that make sense. (1) `{ a*b | a \in A, b \in B}` or (2) ~~`span { a*b | a \in A, b \in B}`~~ sorry, I meant `span { a*b | a \in span A, b \in span B}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773673):
since I^(n+1) = I^n * I and I^0 = B and these are both ideals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773680):
in ring theory you obviously need the second definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773685):
I would say that (1) is more natural. But for ideals you want (2)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773722):
A question: using the set definition, is `span (I*I*I) = span (span (I*I) * I)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 08 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773729):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773771):
Anyway, Kevin, here is https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring with `is_integrally_closed` up to some sorrys in mason-stother.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 08 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773788):
A subset B is trivial, to see that B subset A, suffices to show that `span(I*I)*I subset I*I*I`, and then it follows from distributivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773808):
Here's another CS-ism: instead of dealing with ideals, generalize to all sets by implicitly taking the span when you need to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773872):
Ok, so we put a semiring structure on `set R`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773903):
One problem with doing this generally is that `-A` is taken in sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773973):
Hmm, there is no semiring structure actually. Because `neg A` is `span (-A)`, and so `neg neg A \ne A`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773984):
Unless `A` is an ideal... but that is a very crazy assumption. (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774029):
I think the nice thing to do is to define a class `ideals R`, just as with `opens X`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774043):
And then put the nice structure on `ideals R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774051):
actually if you only want a semiring you don't need neg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774056):
I don't think you have to worry about any cancellation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774067):
but the distributive law fails I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774069):
Aah, you are right of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774147):
`{1, 2}*({1} + {1}) = {2, 4}`, `{1, 2}*{1} + {1,2}*{1} = {2,3,4}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774188):
No, your counterexample fails. Both sides are `R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774235):
And in fact, I think you get a semiring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774259):
The output of `+` and `*` is always an ideal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774283):
`A + B` is defined as `span (span A +' span B)`, where `+'` is the stupid element-wise addition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774288):
Analogously for `*`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774346):
(I agree that my initial definition was wrong. But I had not learnt your CS-ism back then. So I didn't put in enough `span`s.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774416):
I think `span (A +' B)` should suffice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774476):
My observation is that elementwise addition is non-distributive (although it is associative and commutative if the underlying op is)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774499):
Right, but you want that multiplication and addition of ideals is distributive.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774504):
That is a fact that will someday be in mathlib, I hope.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774514):
So we tweak our definition, and throw in some extra `span`s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774669):
You don't need the extra spans though, the span in the upgraded addition is sufficient to fix the issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774696):
`span (A *' span (B +' C)) = span (span (A *' B) +' span (A *' C))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774957):
Take `A = R`, `B = {1}` and `C = {-1}`. Then LHS = 0 while RHS = R.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 08 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127780905):
The main point here is that you should be writing `(I : ideal R)`, not `(I : set R) (h : is_ideal I)` or whatever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781504):
So why do we still write `(R : Type) [ring R]`? Shouldn't we write `R : Ring` and `G : Group` or something like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781586):
Or does the difference have to do with whether your class is a `Prop`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781612):
So all the `is_open`s, `is_ideal`s and `is_subring`s get gathered into classes `opens`, `ideals`, and `subrings`. But things like rings and groups shouldn't...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781677):
I think in many cases you should also be writing `R : Ring` etc. Particularly in settings where the only thing you know about `R` is that it is a ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781694):
`R : Ring` might be less convenient when dealing with specific objects. For examples, the real numbers are a ring but they are also a topological space, etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781772):
Right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781873):
@**Reid Barton** I think Mario said something along the lines that type inference and coercions don't work together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781959):
So, suppose you have the following statement `instance {R : Type} [ring R] (S: subrings R) : ring S`. If you then want to prove `instance {R : Type} [comm_ring R] (S: subrings R) : comm_ring S` I think you run in to trouble, because now Lean needs to turn `S` into a `Type` and also infer that it is a `ring`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127782008):
And I couldn't just easily prove stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127782026):
(I don't have Lean here atm... so I can't reproduce the exact problem I ran into.


{% endraw %}
