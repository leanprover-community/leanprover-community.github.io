---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45571generalizingpadicval.html
---

## Stream: [maths](index.html)
### Topic: [generalizing padic_val](45571generalizingpadicval.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952749):
In my proof of FTA, I need the highest power of a polynomial that divides another polynomial. Should `padic_val` be generalized to do this. What's the correct generality for this function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952773):
You should be able to say this in any comm semiring (where dvd is defined)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952824):
But maybe UFD's are the right level of generality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952829):
no, some of this you want to be able to state even without ufd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952832):
for example you can use it to define a ufd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952846):
plus that's a hell of a proof obligation for using the notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147952992):
The theory really takes off in a ring where the notions of prime and irreducible elements coincide; then for r an irreducible element of a comm ring with this property, the "r-adic valuation" is very well-behaved (e.g. it's additive). Even for a ring like $$\mathbb{Z}[(-5)^{1/2}]:=\{\,a+b(-5)^{1/2}\,\mid\,a,b\in\mathbb{Z}\,\}$$ the 2-adic valuation of both $$1\pm (-5)^{1/2}$$ is 0 but the 2-adic valuation of $(1+(-5)^{1/2})(1-(-5)^{1/2})$ is 1, and 2 is irreducible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953038):
I don't think it necessarily has to be a valuation like in the padics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953047):
you can say 2 is the highest power of 4 that divides 48

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953057):
and you have to worry about infinity being a possible answer regardless, because of 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953061):
so at that point it's really valid as long as dvd and power are defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953104):
We do rely on the property a^m | b -> a^n | b when m >= n, but that is true in any monoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953109):
Right. I don't know the answer to Chris' question of the generality it should be defined in Lean, I was just explaining the boundaries of where it started to be useful in commutative algebra.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953118):
I wish dvd was defined on monoids instead of semirings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953170):
although you could argue about whether commutative matters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953175):
I can't imagine ever needing this function for a non prime element and it won't have any nice properties, but over a UFD this function is used all the time by mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953196):
One interesting thing you can do with this function is define the class of rings where it is always finite for nonzeros

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953202):
It's like an archimedean property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953329):
Here is a silly example using a non-prime: the count of 10 inside a number n is its number of trailing zeros

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953477):
Maybe Noetherian rings with no nilpotents have this property. Nilpotents will always screw you up, and Noetherian is a finiteness hypothesis which typically makes intuitive things like this true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953504):
Maybe it follows from Krull. @**Kenny Lau** ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953572):
how should I know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953639):
Krull needs proper ideals. Aah. So for a unit it's always infinite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953662):
You didn't do krull yet Kenny? It's in AM. .

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147953687):
oh right, ignoring units

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967315):
If I define it over a `comm_semiring` it's going to be noncomputable. Is that the right approach?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967633):
ah, that's true. How about a `decidable_rel dvd` assumption?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967655):
Still not computable. I have to decide whether it's finite or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967755):
right, this puts it in the same class as order-finding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967784):
how is it being represented in the first place? are you using with_top nat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967826):
I haven't decided. Probably default to zero since zero's not being used for anything else.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967880):
well, zero has a meaning here (no powers of p in the number)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967886):
is that a problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967893):
Sorry yeah.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967897):
Might be a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967910):
It just means `p_adic_val_eq_zero_iff` has an extra assumption

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967949):
although for general comm semirings that assumption is kind of complicated, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967953):
Currently it defaults to zero.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147967965):
Yes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968031):
But maybe in a UFD or something it's simpler, so there'll have to be a UFD version of the lemma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968056):
or a proposition asserting finiteness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968081):
perhaps the `roption nat` version works best here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968107):
since that way you get the proposition for free, encoded in the `roption`, and it's computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968192):
but we will want to specialize the function to rings where we can prove finiteness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968197):
like padics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968220):
You still have to decide if somethings a unit or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968273):
With the `roption` version, you can just do the naive search and it's computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968281):
because of `pfun.fix`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968380):
maybe `nat.rfind` is easier to use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968382):
It's "computable" but you still have to give a proof to actually compute it. I'm not a fan of worsening ease of proof for the sake of computability.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968409):
my point is that here the mathematics and computability aspects coincide

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968415):
we need an extra "infinity" value, and roption gives us that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968471):
and as far as giving a proof, that is exactly what we can do in nice rings like `int`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/147968524):
(actually, in the VM you can cheat and evaluate any `roption`, even if it is an infinite search)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 21 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148115154):
@**Mario Carneiro** One downside of generalizing padic val, is that now for integers it will return an `int` rather than a `nat`, which I know can be very annoying. Is this a good reason to have two definitions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 21 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148115253):
How so? If it's defined based on monoid.pow then it should give a nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 21 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148115990):
You're right. I'm being stupid.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148127500):
In maths you would have valuations taking on natural values on the "integers" and valuations taking integer values on the "rationals", and both would be used (in some generality).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 21 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148130014):
@**Kevin Buzzard** Is the statement that every non-zero non unit has a finite padic val equivalent to UFD. It seems to be provided there aren't any elements which can be divided by infinitely many distinct primes, and I'm not sure if that's possible or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 21 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148130128):
@**Chris Hughes** In $$\mathbb{Z}[\surd{-5}]$$ you have $$(1 - \surd{-5})(1 + \surd{-5}) = 6 = 2 \cdot 3$$. So that is not a UFD.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 21 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148130239):
But I think it satisfies your other requirement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148141439):
Situation like that happening didn't occur to me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 22 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148154102):
Some of the statements become a bit ugly with `roption`. Is there a good way around this?
```lean
protected lemma mul {a b : α} (ha0 : a ≠ 0) (hb0 : b ≠ 0) :
  get (padic_val p a) (finite_of_prime hp ha0) +
  get (padic_val p b) (finite_of_prime hp hb0) =
  get (padic_val p (a * b)) (finite_of_prime hp (mul_ne_zero ha0 hb0))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 22 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148158928):
@**Chris Hughes** What is your current definition of `padic_val`? Is there someplace we can read your latest code?
I think the idea was that you don't even assume that `p` is prime... (I didn't even know that we had prime elements in arbitrary rings already). If you want to make an assumption on the element, it is probably most natural to assume that it is irreducible. Also, maybe the name should now also be generalised to `adic_val`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 22 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148159267):
I called it "prime count" in metamath, although it wasn't defined only on primes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 22 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148159273):
it's not really the padic valuation since usually that involves a reciprocal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 22 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148159287):
how about `divisibility`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 22 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148161166):
Re the `get`s -- can you just define addition on `roption`? I don't quite know what I'm talking about here. Re
```quote
it's not really the padic valuation since usually that involves a reciprocal
```
 even though the term is used for both the multiplicative and additive versions of this idea, I think "the $$p$$-adic  valuation" usually refers to the map $$v_p$$ with $$v_p(p)=1$$, where as "the $$p$$-adic norm" is the one with $$|p|_{p}=1/p$$. Sadly, in perfectoid land, the norm is referred to as a "valuation" :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 22 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148171739):
The current definition is 
```lean
def padic_val [comm_semiring α] [decidable_rel ((∣) : α → α → Prop)] (a b : α) : roption ℕ :=
⟨∃ n : ℕ, ¬a ^ (n + 1) ∣ b, λ h, nat.find h⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 22 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148172800):
I'll probably change the name at some point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 23 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225756):
@**Mario Carneiro** Are you in favour of making a version of `with_top` with `roption` instead of `option`, with all the order and algebra on it? It would make sense for `padic_val`, but also order of elements of infinite groups.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 23 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225784):
maybe specialized to `enat`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 23 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225838):
that particular structure seems useful, not so sure about generally with-topping a set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 23 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148225854):
Okay sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 23 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/generalizing%20padic_val/near/148231085):
I can't do `inf` computably for the lattice on enat. Should I leave it out?

