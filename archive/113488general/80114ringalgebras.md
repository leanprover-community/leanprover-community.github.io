---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80114ringalgebras.html
---

## Stream: [general](index.html)
### Topic: [ring algebras](80114ringalgebras.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299335):
This problem has come up several times in this year, and I decided it's time to face it instead of to avoid it. This is the definition of an algebra over a commutative ring:
```lean
class algebra (R : out_param $ Type*) [comm_ring R] (A : Type*) extends ring A :=
(f : R → A) [hom : is_ring_hom f]
(commutes : ∀ r s, s * f r = f r * s)
```
Mathematically there are no problems, but somehow every time I try to introduce this class, the class inferences become a mess, consistently. So, my question is: what is the best way to introduce this whole algebra thing to Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299411):
Yeah! Go for it! I recognize the troubles, and I don't know the answer...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299424):
Concerning terminology... I think Bourbaki has a more general notion of algebra.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299477):
For example, a Lie algebra is an algebra.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299481):
MWE:
```lean
import data.polynomial

class algebra (R : out_param $ Type*) [comm_ring R] (A : Type*) extends ring A :=
(f : R → A) [hom : is_ring_hom f]
(commutes : ∀ r s, s * f r = f r * s)

variables (R : Type*) [ring R]

instance ring.to_ℤ_algebra : algebra ℤ R :=
{ f := coe,
  hom := by constructor; intros; simp,
  commutes := λ n r, int.induction_on n (by simp)
    (λ i ih, by simp [mul_add, add_mul, ih])
    (λ i ih, by simp [mul_add, add_mul, ih]), }

set_option trace.class_instances true
#check (by apply_instance : ring (polynomial ℤ))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299500):
Don't you get diamonds this way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299559):
What do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299562):
every algebra is already a ring, and now you are turning rings into algebras, so you are getting loops, not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299565):
Maybe diamond is not the right word, but certainly loops.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299571):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299574):
but it's an important fact that every ring is a Z-algebra, no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299633):
Just as important as the fact that every abelian group is a Z-module.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299759):
Maybe that's the place to start this discussion. For example, my correspondence theorem is written for R-modules. How does one deduce the correspondence theorem for abelian groups? For mathematicians, the answer is easy -- "set R=Z; done". How do we do it in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194100):
At the time, the answer to this question was "just wait until the module refactor hits and then try again". Did you try again after the module refactor? What is still problematic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194328):
@**Kevin Buzzard** the original MWE I posted above still works (in the sense that it still fails)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194329):
and if you define algebra differently, you run into another typeclass problem:
```lean
import data.polynomial

universes u v

class algebra (R : out_param $ Type u) (A : Type v) [out_param $ comm_ring R] [ring A] :=
(f : R → A) [hom : is_ring_hom f]
(commutes : ∀ r s, s * f r = f r * s)

attribute [instance] algebra.hom

namespace algebra

variables (R : Type u) (A : Type v)
variables [comm_ring R] [ring A] [algebra R A]

instance to_module : module R A := module.of_core
{ smul := λ r x, f A r * x,
  smul_add := by intros; simp [mul_add],
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry }

@[simp] lemma mul_smul (s : R) (x y : A) :
  x * (s • y) = s • (x * y) :=
by rw [smul_def, smul_def, ← mul_assoc, commutes, mul_assoc]

end algebra
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194330):
in any case I'm quite tired of Lean's typeclass inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194336):
@**Mario Carneiro** Help! Is this sort of thing still a problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194926):
@**Kenny Lau** I know I'm just commenting without having tried anything out. But I have been working with over-categories a bit. And there has been some work with `CommRing`, I understand. So couldn't we define `algebra R` as `under R`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194927):
I hope that should just work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151195058):
@**Johan Commelin** could you show me what the code I just posted would become?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196687):
@**Kenny Lau** Sorry, I was distracted for a while. You have worked on colimits in `CommRing` haven't you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196688):
I haven't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196692):
Aah, I thought you did, together with Ramon and Kevin.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196694):
Anyway, I think `CommRing` is currently being PR'd or about to be PR'd.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196735):
oh well I didn't use the category theory language

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196737):
https://github.com/leanprover/mathlib/blob/master/category_theory/examples/rings.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196739):
So, there is something there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196744):
Next, you could define under categories, as in https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheafy_preamble.lean#L180

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196745):
And combining those, you would have commutative algebras over a commring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196787):
yes, yes, yes, you could, provided that your URL doesn't contain "leanprover-community"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196790):
You only need that 1 line.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196792):
Comma categories are already in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196803):
The `functor.of.obj` is currently being PR'd to replace `functor.of_obj`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151212724):
Is there any chance that we will be able to use `\Z` notation as an object of `Ring`? Will we always have to type `Ring.int`? Somehow I wish that we can automatically coerce a type into an object of a category if the right type class instance is found... (maybe let's not worry if that is possible with modules, atm) It would be possible if that would at least be possible with the most basic examples, like nats, ints (modulo `n`), rats, reals, complexes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151213510):
@**Kenny Lau** This is what I came up with, after a little bit of hacking. https://github.com/leanprover-community/mathlib/blob/jmc-leftmod/category_theory/examples/left_module.lean
Need to go now. Of course there is lots to be done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151214428):
well... are you sure there will be no type-class issues?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151217969):
@**Kenny Lau** Of course I can't be sure about that. But I think that the more you bundle, the less type class issues you will have. Otoh, the more you will have to be explicit about "coercions", and things like that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151217971):
so are you implying that the Lean typeclass system cannot be salvaged unless we bundle everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218021):
I don't know. The current type class system clearly isn't the most powerful thing imaginable. But for now I wouldn't mind trying more module stuff with less type class stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218080):
@**Kenny Lau** Shall we try to define `map f` and `comap f` between `R-Mod` and `S-Mod` if `f : R \hom S` is a morphism of commutative rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218120):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 09 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218181):
First complication: `CommRing` is not a full subcategory of `Ring` in the current setup. So we can't just speak of `R-Mod`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 09 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151220181):
Isn't Lean's type class system the most powerful thing you can imagine subject to the requirement that you promise that if you ever define two terms of a given typeclass then they will be defeq? The problem might be that mathematicians are expecting too much from it perhaps. One way of upgrading it is to weaken the promise from "defeq" to "either defeq, or the typeclass is provably a subsingleton".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 09 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151220287):
Maybe there is an art to using priorities somehow? You could imagine that mathematicians could try to get better at this art. I've not seen this technique used before. @**Chris Hughes** you had problems with finsets or fintypes when you ended up with...something like two "different" empty lists representing the empty finset, right? Could you imagine carefully switching the priority of something to either very low or very high, to ensure that type class inference issues don't occur? Johan/Kenny, could you imagine doing the same thing here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151220971):
I don't think priority switching works. In the algebra example maybe who end up with the two different instances because you used a lemma that had to use the polynomial instance, because it was proved in more generality than just the integers, and likewise for the other instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223377):
will auxiliary types be the solution?
```lean
def to_module (i : algebra R A) : Type v := A

instance to_module.comm_ring : comm_ring (to_module i) :=
by dunfold to_module; apply_instance

instance to_module.module : module R (to_module i) := module.of_core
{ smul := λ r x, i r * x,
  smul_add := by intros; simp [mul_add],
  add_smul := by intros; simp [add_mul],
  mul_smul := by intros; simp [mul_assoc],
  one_smul := by intros; simp; exact one_mul x }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223424):
But you're still going to end up needing to prove the two instances are equal right? If you use lemmas about each of the different instances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223593):
I made it a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 09 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223656):
Maybe you can use `convert` cleverly at some point. Can you remove things from the type class inference machine? I can't help but think that it will somehow be possible to do all this, maybe we're not having the clearest ideas about how to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151229632):
```quote
Maybe you can use `convert` cleverly at some point. Can you remove things from the type class inference machine? I can't help but think that it will somehow be possible to do all this, maybe we're not having the clearest ideas about how to do it
```
 convert and congr are handy in these situations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237409):
(non-MWE incoming)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237411):
[2018-12-09-2.png](/user_uploads/3121/OP41IwlpQ8GAgQpW6UFtBNmB/2018-12-09-2.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237456):
"there's a type mismatch so I use `convert` which produces a proof by `eq.mpr (eq.refl _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237458):
so what is happening"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246670):
R[X] is an R-algebra so it has a module structure (where the scalar multiplication is `C r * p`). However `R[X]` is a finsupp so it also gets another module structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246708):
The two module structures are not definitionally equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246711):
can we get rid of the latter structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 10 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246878):
Isn't the latter instance "the direct sum of R-modules is an R-module"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246932):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 10 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247189):
How does the second instance come up in practice? Are you manually unfolding to a finsupp?
Ah, do you mean the line `instance : module α (polynomial α) := finsupp.to_module ℕ α`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 10 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247250):
(does R[X] refer to `data.polynomial`?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247375):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 10 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247440):
I think I mostly caught up on this thread. Deleting that instance makes sense, though I wouldn't be too surprised if you end up with new problems...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257075):
@**Mario Carneiro** what do you think about this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257150):
```
class algebra (R : out_param $ Type*) [comm_ring R] (A : Type*) extends ring A :=
```
this is trouble, because this will make `ring A` typeclass problems go looking for instances of `algebra ? A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257201):
right, so I am not using this now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257205):
```lean
structure algebra (R : Type u) (A : Type v) [comm_ring R] [comm_ring A] :=
(to_fun : R → A) [hom : is_ring_hom to_fun]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257208):
I've been using this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257288):
@**Mario Carneiro** would there be any problem if we forgot about the module structure on R[X] induced by finsupp?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257303):
or maybe I should just prove that these two modules are isomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257358):
I thought an algebra was a ring that is also a module

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 10 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257370):
why not have it extend module, and assert that the function's induced smul matches the existing one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257442):
I thought we like definitional equalities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257466):
hmm, I see that can be a solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258425):
```quote
I thought an algebra was a ring that is also a module
```
 In CS you have to think really carefully about these sorts of things. In my mind, an $$R$$-algebra is a ring which is also an $$R$$-module, *and* an $$R$$-algebra is the codomain of a ring homomorphism from $$R$$ -- the two notions are completely interchangeable. In Lean things seem to be much more delicate.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258478):
```quote
```lean
class algebra (R : out_param $ Type*) [comm_ring R] (A : Type*) extends ring A :=
```
this is trouble, because this will make `ring A` typeclass problems go looking for instances of `algebra ? A`
```
 Can someone explain this to me? I don't know how the type class machine works *at all* and I would really like to know what its algorithm is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258929):
Maybe what I need is some abstract examples of classes and instances and an explanation of what typeclass inference does to solve typeclass problems, and also an example of how type class inference can get into trouble and cause one of those huge log files which ends up in a max class instance resolution error.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258959):
If this isn't going to change in Lean 4 then perhaps it's worth documenting how all this works a bit better. Currently I just regard it as magic, but as Kenny once informed me, Lean does not do magic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259223):
well in the future a neural network will resolve typeclass issues and none of us would know the algorithm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259284):
So Lean 7 does do magic after all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259301):
But how does Lean 7 resolve the problem that it can find two non-defeq instances of `topological_space X \times Y` when `X` and `Y` are both metric spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259312):
There is a fundamental issue unrelated to algorithms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259376):
Can we feed useful theorems into the network and tell it to try applying them whenever it can't resolve type class issues? "If you can't prove that `instance1 : foo A` and `instance2 : foo A` are defeq, take look at the useful theorems about terms of type `foo A` which I told you about".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259384):
@**Sebastian Ullrich** am I living in a dream world?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259442):
This happens to mathematicians in practice, in particular in cases where `foo A` is a subsingleton and not a prop, and the two terms are not defeq but are trivially equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259451):
We want to do hard algebra in Lean but we cannot do it in a natural way and also use the typeclass system because our structures seem to be slightly too complex for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259503):
Well -- maybe we can use it -- maybe we just didn't figure out how to use it yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259599):
Type classes only work well when all instances are unique. In other languages this property is enforced, but Lean's type class inference is too general to implement that in a sensible way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259686):
I haven't followed these threads closely enough to say what should be done about the examples that don't satisfy this property right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151260066):
By "unique" you mean that any two instances are defeq, I guess. Could you imagine a strengthening of the system which could handle non-defeq instances which are equal because of a theorem which the type class system "knows" ? Or is this just somehow completely computationally unfeasible? The simplest case is when the class is a subsingleton.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151260884):
The type class system doesn't even know anything about definitional equality, it just uses the same unification as any other part of Lean. I'm not sure if it would be weird to add some sense of definitional extensionality to just this one part of the system, or what that should look like.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261422):
What about the following modification: if the type class search terminally fails (not an intermediate fail during exploration), unfold the head symbol and try again? It seems to me this would make the type wrapping solution much more usable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261745):
@**Patrick Massot** The failed inference can involve many other classes, should they also be unfolded if possible? No, if you want a def to be unfolded by type class inference, it should be reducible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261760):
Can one locally mark a def as reducible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261761):
I don't want it to be reducible, I want is to be unfolded only in the situation I described

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261816):
This is strictly an extension of the current algorithm, it takes over after everything else failed, and start again on a different problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261829):
By "failure" you presumably do you not include "max type class instance resolution reached", which might just mean it's not trying hard enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261851):
Excluding maxdepth error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261904):
My vague understanding is that Coq canonical structure instance resolution does what I wrote

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261985):
By the way, Sebastian, would it make sense to add shortcuts for the instance problems that Lean keeps solving for each proof (like `has_bind tactic` or `has_one ℕ` or `has_add ℕ`)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151266117):
```quote
By the way, Sebastian, would it make sense to add shortcuts for the instance problems that Lean keeps solving for each proof (like `has_bind tactic` or `has_one ℕ` or `has_add ℕ`)?
```
 Shortcut instances are a valid optimization, though they can also increase run time when the subproblem fails (whereas the full problem could still succeed) because there simply are more instances to check. In theory, better caching could also help there, which is the one part of the type class system that's likely to change in Lean 4.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 10 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151266186):
how is the Lean 4 system better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151266584):
I don't know, it hasn't changed yet


{% endraw %}
