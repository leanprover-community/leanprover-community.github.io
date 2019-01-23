---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79129whatiswrongwithHoTT.html
---

## Stream: [general](index.html)
### Topic: [what is wrong with HoTT](79129whatiswrongwithHoTT.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135265404):
Let me start by saying that I really don't want to start a flamewar. I am just very uneducated.
My question is simply this:
Is there a documented reason why mathlib chose "classical DTT" instead of HoTT + univalence?
Has there been some experience that shows that HoTT makes daily life for the working formalising mathematician harder rather than easier?

Motivation: in the https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/tutorial thread there is a discussion going on about transport of structure. And this is not the first time this has happened. If I understand univalence correctly, one would just be able to apply univalence to the `equiv`, which turns it into an `identity`. By induction on `identity`, one would be reduced to proving a claim that is `rfl`. Maybe I'm drastically oversimplifying. Maybe I misunderstand univalence. But this truly sounds like what mathematicians do "between the lines".
Please educate me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 05 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135272847):
I'm also curious about HoTT. So I think from the thread people were discussing 
```lean
lemma card_eq_of_equiv {s : finset α} {t : finset β} (h : s.to_set ≃ t.to_set) :s.card = t.card :=  sorry
```
AFAIK the univalence axiom is `(X=Y)→(X≃Y)`. How do you apply it in this case? Wouldn't you need `(X≃Y)→(X=Y)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135273023):
The function `(X=Y)→(X≃Y)` comes for free. Univalence says that it is an equivalence.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135273073):
`(X=Y)→(X≃Y)` doesn't look like it needs any extra axioms. I think univalence is `(X≃Y)→(X=Y)`. I'm curious about how it works with isomorphisms of structures, If I have two isomorphic rings `R` and `S`, do I know `(1 : R) == (1 : S)`. Equality of the types doesn't seem like a very strong axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135273180):
In fact `(1 : R) == (1 : S)` seems like it could lead to some easy contradictions, but do I know anything a bit like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135273490):
If you're using the correct equiv (ring isomorphisms) you know that the function maps one to the other of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135273525):
What does univalence actually say?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135273589):
No idea, I'd love to know more about HOTT. Can it do perfectoid spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135274063):
There's [this recent talk](https://video.ias.edu/VoevodskyMemConf-2018/0912-BenediktAhrens) from the Voevodsky memorial conference by Benedikt Ahrens titled "Univalent foundations and the equivalence principle". I haven't watched it yet though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 05 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135274190):
How does univalence save you work? You'd still have to prove the isomorphism you chose to encode in `equiv` preserves structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135274206):
I tried googling it, and it seems like it doesn't assume proof irrelevance. It's stated as something like `(A = B) ≃ (A ≃ B)`, where `≃` means the same thing as it does in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135274570):
IIRC "book HoTT" has no built-in Prop/Type distinction, so no proof irrelevance in that sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135274615):
If you see Prop in a book HoTT context, it means basically the same as what we call a subsingleton

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135276936):
```quote
There's [this recent talk](https://video.ias.edu/VoevodskyMemConf-2018/0912-BenediktAhrens) from the Voevodsky memorial conference by Benedikt Ahrens titled "Univalent foundations and the equivalence principle". I haven't watched it yet though.
```
Thanks for this link. I think from 49.30 onwards it might be pretty relevant to this thread.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135277436):
```quote
How does univalence save you work? You'd still have to prove the isomorphism you chose to encode in `equiv` preserves structure
```
Right. But in the case of Bryan's problem, there is not structure. So we win.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135277511):
In the case of Chris's example, he is talking about `(1 : R)`, so you need an `equiv` (or path, in HoTT-speak) that preserves `has_one`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135277680):
@**Mario Carneiro** Can you shed some light on these questions?
```quote
Is there a documented reason why mathlib chose "classical DTT" instead of HoTT + univalence?
Has there been some experience that shows that HoTT makes daily life for the working formalising mathematician harder rather than easier?
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135278023):
I guess implementing it in Lean involve creating a non proof irrelevant version of `eq` and implementing it using that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135278873):
Is that exactly the `equiv`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135278940):
Oh you mean there are parts of the `eq` API which need to be ported to `equiv`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279051):
You need the recursor, because the point is to be able to show things like "if R is artinian and S is isomorphic to R, then S is artinian" by applying univalence and then doing cases on the equality you get out so that you can assume S is R

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279110):
I've thought about it some more, and I think what it would actually look like is `eq,rec_on` with equiv instead of `eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279218):
`eq.rec_on : Π {α : Sort u_3} {a : α} {C : α → Sort u_2} {a_1 : α}, a = a_1 → C a → C a_1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279257):
So the idea would be that there would be some typeclass `[plays_well_with_equiv C]`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279266):
But I don't think you can really go about it this way, unless you can rule out "being equal to R" as a property which you can apply the recursor to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279294):
Because then you could just conclude that `S = R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279335):
that rule doesn't get tagged with my cool typeclass though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279374):
Right, so `plays_well_with_equiv` seems to be viable and I think it's what people were calling "transportable" earlier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279473):
Another way might be `equiv A B -> for all C : Sort u -> Sort v, C A = C B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279500):
plus the typeclass on C

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279522):
Oh wait -- you want `C A = C B`? Not just an equiv?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 05 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279663):
ah, this paper points out a big problem with hott `https://hal.inria.fr/hal-01559073v2/document`. Just like with `acc`, you get stuck terms when you use axiomatic univalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279726):
But does that stop me from defining a perfectoid space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279755):
Why are we having this discussion again? I thought HoTT is irremediably tied to constructive mathematics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 05 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135279782):
if restriction maps, id, and def reduction made you tear your hair out, trying to deal with univalence will do so similarly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135281859):
> Motivation: in the https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/tutorial thread there is a discussion going on about transport of structure. And this is not the first time this has happened. If I understand univalence correctly, one would just be able to apply univalence to the equiv, which turns it into an identity. By induction on identity, one would be reduced to proving a claim that is rfl.

I had a discussion with @**Jeremy Avigad** on this very issue today. What you have said is not wrong; you can use univalence to prove these kinds of theorems almost trivially, because it's basically the content of that axiom. But there are some huge asterisks that come with this assertion, which make it almost disingenuous to trot out as an advantage of HoTT, because even if in an alternate universe mathlib was based on HoTT we would still have a considerable amount of difficulty with transfer of structure proofs in exactly the form we want them to be, the problem would just be with different parts of the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282014):
> (X=Y)→(X≃Y) doesn't look like it needs any extra axioms. I think univalence is (X≃Y)→(X=Y). I'm curious about how it works with isomorphisms of structures, If I have two isomorphic rings R and S, do I know (1 : R) == (1 : S). Equality of the types doesn't seem like a very strong axiom.

HoTT is kind of magic when it comes to this. One of the things which is the most impressive about how HoTT works is how it always seems to get exactly the right kind of equivalence between objects. Two types are equal iff they are (constructively) bijective, two bundled groups are equal iff they are isomorphic as groups, two bundled rings are equal iff they are isomorphic as rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282053):
In HoTT, `==` is actually a "bad" notion of equality. Instead they have a "pathover" `a =[h] b` where `h : A = B`, which is basically equivalent to `cast a h = b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282377):
The key is that equality of sigma types `\Sigma x : A, B x = \Sigma x : A', B' x` is the same as the pair of an equality `h : A = A'` and a pathover `B x =[h] B' x`. For a simple example, consider equality of pointed types (i.e. a type with a zero element and no axioms). This can be defined as `\Sigma A : Type, A`, and so an equality of sigma types `(A, a)` and `(A', a')` is an equality `h : A = A'` with a pathover `a =[h] a'`. If you unpack this, it means `h` is a bijective function from `A` to `A'` such that `h` maps `a` to `a'`. In other words, it is a pointed equivalence, which is what we wanted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282432):
If you do this with groups, the pathover thing exactly asserts that the map between types preserves the 0, inv, + which is a group isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282548):
> How does univalence save you work? You'd still have to prove the isomorphism you chose to encode in equiv preserves structure

In HoTT, the equiv is just a plain equiv, i.e. a function `f` with an inverse `g` and two *paths* `f o g = id`, `g o f = id`. That is, it looks just like the usual definition of equiv, but the new interpretation gives it magic powers to be a group isomorphism when talking about groups, etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282629):
> I tried googling it, and it seems like it doesn't assume proof irrelevance. It's stated as something like (A = B) ≃ (A ≃ B), where ≃ means the same thing as it does in Lean.

Technically, it's not just any equiv, it asserts that the natural map `A = B -> A ≃ B` is an equivalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282634):
HoTT is inconsistent with proof irrelevance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282647):
because if equalities of groups are group isos, we can't possibly assert there is only one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282738):
> I guess implementing it in Lean involve creating a non proof irrelevant version of eq and implementing it using that?

Yes, but it's not that simple. Just the fact that propositional equality exists in the system is enough to prove that Type eq and Prop eq are equivalent, and hence the fact that Prop eq is proof irrelevant collapses Type eq. In the hott3 library they go to great lengths to mark everything using Prop eq as "bad" and unusable in HoTT stuff to avoid contradictions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282803):
> I've thought about it some more, and I think what it would actually look like is eq,rec_on with equiv instead of eq

Yes, this is an equivalent way to state univalence. Something with the same recursor as eq is provably equivalent to eq, and vice versa

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135282952):
> Another way might be equiv A B -> for all C : Sort u -> Sort v, C A = C B

> Oh wait -- you want C A = C B? Not just an equiv?

These are equivalent. Even if you only had `A ≃ B -> for all C : Sort u -> Sort v, C A ≃ C B` you could just apply it to `C = \lam x, A = x` to deduce `(A = A) ≃ (A = B)`, and since the first is inhabited you just apply the function to prove `A = B`. So this is also univalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135283041):
> ah, this paper points out a big problem with hott https://hal.inria.fr/hal-01559073v2/document . Just like with acc, you get stuck terms when you use axiomatic univalence

This is why cubical type theory was invented. It provides a way to compute with univalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 05 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135283559):
"provides a way to compute with univalence" maybe should be "hopefully provides a way to compute with univalence, except that currently some of the things we think should compute instead blow up our computers".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 05 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135283577):
(If I understood the cubical type theorists at Dagstuhl talking about Brunerie's number correctly.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135283614):
I watched the talk and the main thing I don't understand is why and when Id is not a subsingleton. If i define it in a similar in Lean, as Type, so without proof irrelevance, but it's still a subsingleton. 
```lean
inductive Id {α : Type} (x : α) : α → Type
| refl : Id x

instance {α : Type} (x y : α) : subsingleton (Id x y) :=
⟨λ i j, begin cases i, cases j, refl end⟩

example {α : Type} (x y : α) (i j : Id x y) : Id i j :=
by cases i; cases j; exact Id.refl _
```
The recursors/ eliminators/ computation rules mentioned in the talk https://www.youtube.com/watch?v=okx4Uklvwco are the same as they are in Lean, so why do they not imply Id is a subsingleton? Obviously there are types where it is a subsingleton, which he calls "Sets", what would make a type a Set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 06 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135287498):
Something subtle is happening in your examples. Check out what the equation compiler actually generated.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 06 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135287763):
If you try to implement these by hand, you can do the case analysis on `i` but then you'll get stuck on `j`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135288559):
Reid is right. `cases` and the equation compiler use a HoTT-unsound proof method that introduces Prop eq to eliminate from inductive predicates. In the end the resulting proof uses the assumption that a proof of `a = a` is definitionally refl, which is provably false in HoTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135296892):
```quote
Why are we having this discussion again? I thought HoTT is irremediably tied to constructive mathematics.
```
@**Patrick Massot**  The last sentence of §7 in https://arxiv.org/pdf/1711.01477.pdf (by Dan Grayson) says: *"The Law of Excluded Middle and the Axiom of Choice are also validated by this interpretation, so classical mathematics is supported soundly by the univalent foundations."*
So I wonder if you (we?) have been tricked by a version of the myth that all formalised math needs to be constructive.
Or is Dan Grayson pulling a trick on us?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135296941):
The excluded middle and the axiom of choice are indeed consistent with HoTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135296942):
`choice` is not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135296989):
"The axiom of choice" here means `classical.axiom_of_choice`, that is, the one that ends in an existential

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297036):
But actually that's kind of a lie, because in HoTT you have an explicit "propositional truncation" operator that has the same role as putting things in Prop in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297037):
there is no proof irrelevant universe in HoTT, like I said that's not consistent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297095):
I think it would be instructional to actually look at Dan Grayson's work in UniMath and judge for yourself whether the style of mathematics being done there works for you. They also are aiming for the formalization of conventional mathematics, although HoTT-isms are a frequent distraction (e.g. "ooh, I wonder if transfinite induction still holds over n-types")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297098):
just as constructive math is an occasional distraction here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297193):
To respond to the original question, it's my understanding that Lean/mathlib is using more traditional type theory rather than HoTT basically "by default". Research is on-going wrt formalizing mathematics with HoTT and making univalence compute via things like cubical types but it's still a bit avant-garde

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297211):
I think that's fair. I would even possibly go so far as to say that we tried it and it "didn't work" in the sense that the issues thrown up are not minor annoyances but major research projects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297257):
```quote
there is no proof irrelevant universe in HoTT, like I said that's not consistent
```
But if you have a `P : Prop` and `x y : P`, then you would know that `Id p q` is contractible. Which seems to me just as good as proof irrelevance. In practice, I think you can even teach the computer to use this fact, without bothering you with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297258):
I don't think HoTT is really suitable as a practical foundation for all of math, except in the logical sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297261):
> But if you have a P : Prop and x y : P, then you would know that Id p q is contractible.

This is not true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297271):
this is the same as chris's proof attempt, and it's not provable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297273):
```quote
I think that's fair. I would even possibly go so far as to say that we tried it and it "didn't work" in the sense that the issues thrown up are not minor annoyances but major research projects
```
This is exactly what I would like to know about. Are those problems even there if you don't care about computability?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297276):
It's provably false with HITs, or even just with type equalities using univalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297328):
```quote
> But if you have a P : Prop and x y : P, then you would know that Id p q is contractible.

This is not true
```
I thought it was the definition of being a `Prop` in HoTT.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297331):
For example, S^1 is a higher inductive type defined by `base : S^1` and `loop : base = base`. Since this is a "free" construction, this `base` is not `refl base`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297341):
Oh, I missed that you said it was a prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297344):
Sure, that makes all the difference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297347):
That's not how it works in HoTT. Instead you would say `P : Type` and `is_prop P`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297348):
props are *defined as* types whose path space is contractible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297353):
and `is_prop` is basically `subsingleton`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297400):
because there is no "universe of props"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297402):
Anyway, does this mean that proof irrelevance is there in the cases that we actually care about? (The other things just aren't *proofs*. They are higher order.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297418):
No. Being a proposition is a property which may or may not hold, and it holds a lot less than you would expect

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297419):
`def Prop := subtype is_prop` wouldn't cut it, I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297469):
There is `trunc` though (indeed I borrowed the terminology from HoTT), which will make a subsingleton from any type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297473):
```quote
No. Being a proposition is a property which may or may not hold, and **it holds a lot less than you would expect**
```
(Emphasis mine). This is important information! Has this been documented somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297478):
and things like exists and or are defined by truncating after taking the sum/sigma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297535):
But I think that equalities not being subsingletons will get in your way a lot more than you think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297547):
Here is a question: How do you define a group in HoTT?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297558):
I mean... what I'm getting from this thread is that there are "problems" with HoTT in practice. And I already had this vague feeling. But otoh, univalence seems a mathematician's dream. So I would like to understand those "problems" in more detail. And I'm asking whether someone wrote some docs saying: here's some problems for the *working mathematician* (someone who doesn't care about constructivity and computability, a priori).
Does something like this exist?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297574):
```quote
Here is a question: How do you define a group in HoTT?
```
Benedikt did this for monoids in that talk.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297579):
So it is `(M : Set, mul : M × M → M, e : M, 3 proofs)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297623):
And I'm using his notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297629):
But `Set` should probably be `Type` + `is_set M`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297630):
I am alluding to the `Set` part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297644):
I guarantee you that will be a sticking point for getting mathematicians involved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297645):
Ok, what's wrong with it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297654):
It is a restriction that people don't want to have to think about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297662):
There is an obvious definition of a group where you say `Type` instead, and it's not correct, and it will take you a while to realize this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297706):
Hmmm... can't notation help us there?
I claim that every mathematician understands in a few minutes that higher monoids don't have proof irrelevance for their associativity etc... (in fact there are even multiple generalisations)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297709):
Is that much more to ask than understanding `Prop` vs. `Type` and universe levels?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297718):
I think it is, mathematicians have *no concept whatsoever* about the higher structure of equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297720):
```quote
There is an obvious definition of a group where you say `Type` instead, and it's not correct, and it will take you a while to realize this
```
It takes a while. But if you point out the analogy with actual homotopy theory, I think people get it fairly quickly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297726):
and now you've got people thinking about homotopy theory to do groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297727):
```quote
I think it is, mathematicians have *no concept whatsoever* about the higher structure of equality
```
This is blatantly false for mathematicians coming from algebraic topology.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297732):
I see I've targeted the wrong audience :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297741):
Np, I think I'm getting your points.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297789):
So I repeat: Can't notation take care of this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297795):
The point is that HoTT makes you think about homotopy stuff whether you want to or not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297796):
Can't we have easy access to "`Set`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297800):
Maybe? It will still come up in proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297810):
maybe you can automate that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297826):
If it comes up in proofs after the definition, then this is probably for a good reason. Unless the computer should have been able to figure out `is_Set` or `is_Prop` on its own.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297832):
but no one has really seriously attempted to "just do math" in HoTT AFAICT, except possibly UniMath. Everyone gets distracted by the abstract homotopy stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297880):
Right. I think I wouldn't get distracted. Neither would @**Scott Morrison|110087**, @**Patrick Massot** or @**Kevin Buzzard**. We just want to take a far and high leap into normal classical research math.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297881):
Quotient modules in UniMath: https://github.com/UniMath/UniMath/blob/master/UniMath/Algebra/Modules/Quotient.v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297894):
Do these rings and modules live in "Set", or are they higher order?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297898):
looking at it, I don't see anything really out of place for regular math in Coq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135297951):
their setup for modules looks much less nice than lean's: https://github.com/UniMath/UniMath/blob/master/UniMath/Algebra/Modules/Core.v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298019):
Ooh, a hott-ism:
```
(** The type of linear functions M -> N is a set. *)
Lemma isasetlinearfun {R : ring} (M N : module R) : isaset (linearfun M N).
Proof.
  intros. apply (isasetsubset (@pr1linearfun R M N)).
  - change (isofhlevel 2 (M -> N)).
    apply impred.
    exact (fun x => setproperty N).
  - refine (isinclpr1 _ _).
    intro.
    apply isapropislinear.
Defined.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298022):
They lack the pretty notation. But maybe that's because they don't distinguish between `has_mul` and `has_add`? Otherwise it looks pretty normal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298024):
Ooh, let me see what you found.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298069):
I think it makes sense that HoTT represents too big a shift in thinking about equality to be a drop-in replacement. I've gotten the impression that they hope it will help us do a lot of (non-homotopy...) math in a better way, but if it's a new way of doing math it couldn't be for the working mathematician until the working mathematician starts doing math differently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298073):
@**Mario Carneiro** Maybe that could have been proven `by obviously`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298139):
But it seems like that's still mainly hopes and works in progress. I'm curious to what extent they could eventually move away from homotopy terminology to make it more approachable to the mainstream

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298144):
`@[derive is_Set] def linearfun ...` and automation derives it for you. I don't see anything blocking this...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298148):
I think even dependent type theory is a hard sell what with the casts and hard types and such... HoTT adds even more irrelevant junk from the mathematicians POV

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298209):
Right, I think no mathematician would want HoTT without univalence. But univalence is very enticing. And it might be worth the hurdles.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298210):
But speaking of automation, we started on this discussion because we wanted to do transport of structure and anything HoTT can do using univalence we can do with a tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298215):
```quote
But speaking of automation, we started on this discussion because we wanted to do transport of structure and anything HoTT can do using univalence we can do with a tactic
```
Seriously? That sounds cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298222):
@**Kevin Buzzard** :up: voila!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298226):
We only need to get that tactic and you'll never hear us talking about HoTT or univalence again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298227):
It's not like it's an unsolved problem... that paper that was linked earlier seems to explain it in detail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298229):
https://hal.inria.fr/hal-01559073v2/document

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298277):
But I also wanted to cure you of the idea that HoTT would magically solve these problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298280):
You still have to prove that all your notions respect equality, it's just expressed differently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298320):
you need to prove how transport computes on a bunch of things, and this is where the work is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298321):
I think we should try again with `transfer` and see what goes wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298334):
Still, I hope that such a tactic would significantly decrease the length and mental overhead of Bryan's proof that equivalent sets have equivalent partitions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298374):
Right, but currently `transfer` seems a *framework* that doesn't have any tactics to guide mere mortal mathematicians through it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298375):
You need to prove that equivs respect filter and powerset... it's not that difficult

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298381):
I've tried a couple of times, but got stuck all the time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298386):
The key is to prove those relators for lots of interesting notions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298388):
`transfer` is useless without them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298390):
Right. We need a (general) tactic that would generate those two goals (in this specific case)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298393):
no, you need to *prove* them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298401):
they are not trivial claims

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298402):
but `transfer` will glue them together into larger proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298403):
No, I mean it takes the main goal. I invoke `univalence`. And it splits into the two goals you mentioned. Then I prove those.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298404):
So we're talking about the same thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298444):
Ideally the lemmas about `powerset` and `filter` will already be in the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298445):
Currently there is no tactic called `transfer`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298446):
there is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298447):
```quote
Ideally the lemmas about `powerset` and `filter` will already be in the library
```
Sure... at some point they will be.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298448):
it's in core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298456):
And if VScode has a mode "Turn current goal into lemma" I think we would generate those facts even faster. (Instead of hiding them as subproofs.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298457):
they aren't hard theorems, but no one has tried to prove them, or more likely they are already there but without the peculiar notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298499):
```quote
You still have to prove that all your notions respect equality, it's just expressed differently
you need to prove how transport computes on a bunch of things, and this is where the work is
```
this was my impression when looking into cubical type theory. for example, there univalence itself seems small and easy to prove, because the details are bound up in the more fundamental ideas of transport-respecting equality in the type theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298507):
@**Mario Carneiro** What exactly would "equiv respects powerset" look like in Lean, to make it usable for `transfer`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 06 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298553):
you also get things like how equalities between pairs are actually equal to pairs of equalities between the two fields (with proof-relevant equalities), which maps to how transporting pairs requires transporting each of the fields

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298623):
right, you have to recurse through that stuff to prove your theorem about transport of `partition`, so in the end it's not much different from the recursion that `transfer` will do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298635):
or more precisely, you know immediately that the partitions of A and B are isomorphic, but what that isomorphism does is not obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135298664):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135299309):
@**Mario Carneiro** I know you are really busy. But I would love that after the module refactoring is done this issue would land somewhere near the top of your todo list. Turning `transfer` into something that we smoothly use on a daily basis would be a huge win.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 06 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135309614):
@**Mario Carneiro** here is a practical question. Once I said "oh we need `ring`". I probably said it about three times. And then one day I woke up and found that all of a sudden we had `ring`. My *impression* (correct me if I'm wrong) was that once you got down to it, it was just a cool project that maybe took you a weekend of coding because you understood exactly what needed to be done and then you just sat down and did it.

Well, now we "need" (in the same sense) the fact that if A and B are `equiv` topological rings then `Spa A` and `Spa A` are equiv topological spaces equipped with presheaves of topological rings, and to a mathematician the proof is `rw h` where `h` is the equiv. I fully understand that in Lean life is not so easy. But is this a tactic which will randomly just appear one day in mathlib like `ring` did or is this a far more serious research project? If it is I am wondering whether it is worth making it an issue for mathlib, so we know where we are and what needs doing. It would not surprise me if mathematicians have got big ideas about what this tactic is supposed to be doing, and I have no real feeling for whether Lean is capable of doing what we actually want, or whether Lean 4 changes things. 

I have this mathlib issue which is not really an "issue" -- "let's define the adeles!". I am about to close it and put it instead on the "list of stuff which we should formalise at some stage". But my troubles with `module` are an issue I think, and non-existence of `transfer` is another issue. Is this a sensible usage of the "issue" functionality of github?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135315441):
@**Floris van Doorn** @**Cyril Cohen** I heartily invite you to read through this thread and share some of your insights and expertise with us.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 07 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135330245):
```quote
What does univalence actually say?
```
perhaps I'm too late, but there's this explanation with Agda code http://www.cs.bham.ac.uk/~mhe/agda-new/UnivalenceFromScratch.html (see also the arXiv version https://arxiv.org/abs/1803.02294)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 07 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135330253):
@**Scott Morrison|110087**  yes, there are programs that have been extracted, but they are so slow and memory-hungry they cannot be run to completion, even to calculate Brunerie's number (which is known to be 2 even in HoTT, on paper)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135358192):
Thanks for the ping, Johan. 
I think Mario has said most things already, but let me reiterate some points.

In HoTT you can develop ordinary mathematics. It will be mostly the same as formalizing things in mathlib. If you stay in the fragment of sets in HoTT, things will look very familiar. Here with "set" I mean a type `A` where for all `a b : A` the type `a = b` is a subsingleton (what we would call a propositon). 

**Disadvantages**
There will be some disadvantages/inconviences when doing set-level mathematics in HoTT:
* You won't have definitional proof irrelevance. Even if you are working with sets, if you have two equalities `h1 h2 : a = b`, `h1` and `h2` will not be definitionally equal.
* You will have to prove that the objects you're dealing with are a set or proposition. For example: it is a lemma that `n ≤ m` is a proposition for natural numbers `n` and `m`. This is definitely automatable in 99% of the cases. 
* `classical.choice` is inconsistent. The law of excluded middle and the axiom of choice are consistent with HoTT (and HoTT is no more tied to constructive mathematics than ordinary type theory is), as long as you restrict LEM to propositions (subsingletons) and the axiom of choice to sets. The restriction of `classical.choice` to a `subsingleton` type is consistent (and actually provable) in HoTT.
* Instead of a single universe of propositions, there is a subuniverse of propositions (defined as `Prop := subtype is_prop` as Johan suggested above) inside every universe. This means that if you talk about a proposition, you have to decide in which universe that proposition lives. This hasn't come up as a problem in the HoTT library yet, but could lead to the insertion of some `ulift`s.

I think the main reason why mathlib doesn't use HoTT is that we don't want to explain HoTT to all users of mathlib. Type theory is already weird enough for mathematicians, I think explaining the higher groupoid structure of equality would be too much. I think for experts, formalizing mathematics in HoTT won't be any harder than doing it in mathlib, but there will be a steeper learning curve. For example, if you have an element `⟨a, H⟩ : subtype P`, and you apply a lemma which expects the term `⟨a, H'⟩` (same element, different proof of `P a`), you will get a type error. It's easy to fix this, but very confusing for an average user (`⟨a, H⟩ = ⟨a, H'⟩` is provable by `subtype_eq rfl`).

**Univalence**
As mentioned before, univalence roughly states that if you have an equivalence between two types, then they are equal. More formally, it states that the function `(A = B) → (A ≃ B)` (which is easily defined by - for example - `eq.rec`) is itself an equivalence. One pedantic remark here is that stating that a function `f : A → B` is an equivalence (`is_equiv f`) is defined slightly different in HoTT than in mathlib. One important property we need is that `is_equiv f` is a subsingleton, and the type `Σ(g : B → A), g ∘ f = id × f ∘ g = id` is not. There are many definitions which do satisfy this property, the simplest is by saying that `f` has a left-inverse *and* `f` has a right-inverse, so `(Σ(g : B → A), g ∘ f = id) × (Σ(h : B → A), f ∘ h = id)`. To be clear: there is a bi-implication between these two different definitions, but only the second one is a subsingleton, while the first one is not.

While univalence is only a statement about types, we can then prove it for all kinds of other structures: the type of equalities `(G = H)` between groups correspond to the type of group isomorphism between `G` and `H`. Equalities `(C = D)` between categories correspond to isomorphism of categories (and if `C` and `D` are so-called *univalent* categories, then it also corresponds to equivalence of categories), etc.

Univalence allows you to transport definitions and theorems between isomorphic structures. The catch is that if univalence is an axiom, these transported definitions will not be definitionally equal to what you want/expect (in cubical type theory it is, see below). As long as you are working with set-level objects, this will not be a problem. You can easily prove that the transported definition is equal to what you expect (and this is definitely automatable with a tactic). When transporting theorems, this will not be a problem, since we don't care about how we've proven these theorems.
Let's look at two examples. In both cases I have a group `G`, a subgroup `H` of `G` and have proven that the property `PH : P H` holds. Now suppose `ϕ` is a group isomorphism from `G` to `G'`
* It is easy to now find a subgroup `H'` of `G'` such that `P H'` holds. Just transport `⟨H, PH⟩` along the equality `G = G'` obtained from the group isomorphism. It is a lemma that `H'` is the image of `H` under `ϕ`.
* Suppose we already have defined a subgroup `H'` of `G'`. To show that `P H'` holds, we can show that `H'` is the image of `H` under `ϕ`. We can then use univalence to get `P H'`. This will require some reasoning steps, but I'm sure that this can be automated using a tactic.

**Cubical Type Theory**
In cubical type theory univalence does compute. The disadvantage is that the type theory is a lot more complicated and under active research. For example, for many variants of cubical type theory meta-theoretic properties like canonicity and decidable type-checking are still open. Reducing a couple instances of univalence will be fast and efficient. In this way it's nothing like computing Brunerie's number. Computing Brunerie's number is slow in the same way that kernel reduction in Lean is slow: you wouldn't want to compute `2^100` using kernel computation, but reducing a couple of beta-redexes with the kernel is fine. 

I hope this answers some questions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 07 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135358972):
@**Floris van Doorn** Thanks a lot for this extensive reply!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 07 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/135365207):
Many thanks Floris! Your comments are very clarifying for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 31 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/136865419):
One thing about this I haven't managed to work out is how you can end up with two different proofs of equality that are provably not equal. Are there any simple examples?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 31 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/136866828):
There are two ways:
(1) Using the univalence axioms, equality between types `A` and `B` correspond to (more precisely: are equivalent to) equivalences between `A` and `B`. So for example, for every bijection between `nat` and `int` you get an equality between `nat` and `int`, and these are provably unequal the corresponding bijections are unequal.

(2) In HoTT, you can extend the language with *Higher Inductive Types*. These are like inductive types, where your constructors can be either new elements of the type you're constructing, but also new paths (equalities) between the elements. 
For example, you can have an interval `I` with three constructors:
* `zero : I`
* `one : I`
* `segment : zero = one`

This is a trivial example, where we get a type with two points, and a path from `zero` to `one`. A more interesting example is the `circle` with two constructors:
* `base : circle`
* `loop : base = base`

Using the univalence axiom you can *prove* that `loop` is not equal to `refl base`. Moreover, you can prover that the type `base = base` is equivalent to the type `int`. (the map `int -> base = base` sends `n` to `loop ^ n`.)

Another higher inductive type you know is `quotient` in Lean 3. For `quotient A` you have two constructors:
* A point constructor `quotient.mk : A -> quotient A`
* A path constructor `quotient.sound : \forall (a b : A), a ~ b -> mk a = mk b`

If you want to define this quotient in HoTT you want to add an additional constructor with type`\forall (a b : quotient A) (p q : a = b), p = q`. This enforces that the resulting type is in fact a "set": a type where any two proofs of the same equality are in fact equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 31 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/136867092):
For all higher inductive types you get an induction principle/recursion principle like `foo.rec` in Lean. It roughly states that to define a function out of a higher inductive type, you have to say to what elements you have to send the point constructors, and show that the map respects the path constructors. For `quotient`, this corresponds exactly to `quotient.lift` and `quotient.rec`. And for the circle, you have to use this principle to show that `loop != refl base`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 31 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/136868896):
@**Chris Hughes** The example about `circle` is very good. In general topology (or homotopy theory) gives good intuition for HoTT. (What's in a name?)
Have you seen fundamental groups in topology yet? Then you will have seen homotopies (continuously deforming a path into another path). And of course we want to call two paths in a topological space "equal" if they are homotopic. Any two homotopies between two paths `p_1` and `p_2` will be proofs that `p_1 = p_2`, but of course those homotopies don't have to be equal.
In ordinary maths we are using setoids and quotients for all of this. (So instead of homotopies, I could have talked about equality in quotient groups instead...) The difference in homotopy theory is that we don't actually want to take the quotient. We want to remember the homotopies. And we also want to remember homotopies between homotopies. HoTT allows us to do this synthetically in the type theory. It is thus suited very well for higher-categorical reasoning in mathematics (and for synthetic homotopy theory).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 31 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20wrong%20with%20HoTT/near/136870378):
I have googled the definition of fundamental group, but I don't know much more than that about them. I understand it well enough to understand most of the analogies given when reading about HoTT, but I had no idea why they were relevant to Type theory until now. I think I'll have to read up on higher inductive types. Thanks @**Floris van Doorn**


{% endraw %}
