---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/97874affineschemesareschemes.html
---

## Stream: [maths](index.html)
### Topic: [affine schemes are schemes](97874affineschemesareschemes.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963591):
I just reached a milestone:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963592):
`noncomputable definition scheme_of_affine_scheme (R : Type u) [comm_ring R] : scheme := [definition which typechecks]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963595):
This was a very surprising process.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963635):
Several times over the last few months I have confidently felt that I was "just a few hours' work away" from this result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963640):
and then I would run into a "trivial to a mathematician, not so trivial in dependent type theory" type issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963649):
The most recent was last night, where I had to write down a map `F U -> F (id '' U)` (here `U : set X`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963689):
and I foolishly rewrote `id '' U` to `U` and used the identity map and ran into all sorts of problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963722):
but this time I was ready for it -- I changed it to a more general construction which gave a map `F U -> F V` for any `V \sub U` and applied it in this case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963728):
There is a subtlety happening here which I am not entirely sure I 100% understand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963731):
I think it might be to do with an equivalence of categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963780):
A mathematician takes a topological space X and then defines a presheaf of abelian groups on X to be, for every open set U in X an abelian group F U

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963790):
and for every pair of opens V in U, a restriction map F U -> F V

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963798):
[the model is that F U is the set of "functions on U", so this restriction map is restriction of functions]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963846):
and this pair F,res has to satisfy two axioms: res : F U -> F U is the identity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963850):
and if W in V in U the two maps F U -> F W (res, and res circ res) are the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963909):
And then an algebraic geometry textbook might then say "here's a cool way of looking at this: let's make the set of open subsets of X into a category -- the objects are the opens and there's one morphism from U to V iff V is a subset of U, and then the axioms for a presheaf are just the statement that F is a functor"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963914):
but somehow this is just a language, this particular fact that something is a functor is never really used in any deep way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963926):
there are plenty of functors around like global sections functors which really do play a role, with derived functors etc etc, but this is not one of them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963929):
In dependent type theory, I think there is something deeper going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963972):
The "category of open sets" is somehow replaced by a much more complex category, the category of terms each of which can be proved to be an open set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963975):
but there is only countably many terms!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963983):
and there's a morphism t1 -> t2 precisely when there's a proof that the open set corresponding to t2 is a subset of the open set corresponding to t1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963989):
I don't care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963990):
I don't think I care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963995):
Maybe I haven't got the language right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964038):
I am happy that if I have a term and a proof that it is an open set then it's in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964042):
and the term might be U and the proof might be sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964046):
and that pretty much covers everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964050):
So in some sense I did not even realise when I defined a presheaf that I was defining it on this much bigger category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964053):
but because the two categories are equivalent it doesn't matter mathematically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964063):
but a consequence of this incorrect mindset was that I often wanted to identify things like F ((U cap V) cap W) and F(U cap (V cap W)) as _equal_

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964064):
because to a mathematician they are equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964104):
but in dependent type theory they are just canonically isomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964106):
Isn't this another instance of "we really need transport of structure"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964107):
No they're equal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964109):
and the correct way to move between them is via the restriction map associated to the proof that the sets are equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964113):
Chris, perhaps they really are equal, but by equal here I think I mean defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964118):
Johan -- in this case I am suggesting another approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964122):
I know, but it means that you are becoming more of a CS guy...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964124):
Here you actually have transport of structure, because `eq.rec` asserts that everything you can express commutes with equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964125):
"transport of structure" in this situation seems to be some sort of brute force collapsing of the bigger category into the equivalent smaller one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964170):
That brute force is exactly what we need, if we ever hope to get up to speed with formalising maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964171):
The `eq.rec` remark is true, *however*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964172):
but that doesn't mean the transport is easy to use without a lot of lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964174):
in practice, because I was dealing with complicated things on top of all this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964180):
eq.rec did not suffice to solve all my problems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964185):
If I had some complex term with `id '' U` in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964187):
and all of a sudden I thought "crap, my life would be much easier if that term was just U`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964191):
then sometimes I would try and rewrite and the rewrite would fail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964193):
or it would be a PITA to formulate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964198):
because the naively written rewrite was not type correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964242):
because H used to be proof of V subset (id '' U) and that needed rewriting as swell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964245):
and congr was not good enough at this sort of thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964248):
and subst was not either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964251):
sorry, subst, not congr

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964262):
@**Kevin Buzzard** have you pushed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964263):
the `eq.rec` term itself acts as a function `F U -> F (id '' U)`, and then you need to know this is functorial for later stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964268):
In this particular case all my problems went away when I started thinking about the equivalent category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964269):
Kenny, I just pushed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964304):
and this is true, but more complicated to prove; and you may need *that* proof to be functorial and it gets yet more complicated...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964309):
this is what HoTT people deal with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964310):
Mario -- I'm sure you're right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964311):
This certainly sounds like the sort of issue which we have to deal with here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964312):
And to be quite frank I did feel like I had dodged a bullet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964317):
When I realised I couldn't use id, I knew things might be bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964318):
At the same time, you have already a robust language of restriction maps that you already know are functorial, because they are the object of study

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964320):
when I realised I could use res, I had some hope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964321):
the choice is obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964323):
and then when gigantic one-page-long goals started yielding to refl I realised I'd had the right insight

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964327):
```quote
the choice is obvious
```
To you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964367):
I would argue that the choice is not at all obvious to a practicing algebraic geometer trained in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964368):
and in some sense this is a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964369):
because it means that we are teaching people in slightly the wrong way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964370):
The important part is to recognize the issue itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964376):
As is so often the case (I have seen this time and time again in mathematics)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964382):
the insight came to me ten minutes after I'd spent an hour being stuck and whining here about how stupid Lean was, and then turned off my laptop and thought about something else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964432):
but I could _envisage_ situations where that bullet cannot be dodged and you have to take the hit and transport your structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964433):
Did you get any insights with the ALEXANDRIA / Peter Koepke lecture person today?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126967797):
I reached another milestone:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126967803):
`definition scheme_of_affine_scheme (R : Type u) [comm_ring R] : scheme := [definition which typechecks]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126967862):
@**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126968834):
So an affine scheme is one that is isomorphic to Spec(A) for some ring A

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126968835):
my question is: how important is that ring A?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969006):
What do you mean? Whether you should carry A around?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969021):
In *maths* it is not important at all. Only the fact that it exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969044):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969051):
I don't understand that question. You can recover A from its affine scheme, is that what you want to know?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969054):
oh really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969056):
is it just the global section?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969119):
now a scheme is covered by affine schemes. Are the affine schemes important?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969162):
Nope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969165):
Only the existence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969166):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969168):
```quote
is it just the global section?
```
Yes, up to isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969169):
Sure, global sections of the structure sheaf gives you back A

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969172):
Too late

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969184):
@**Kenny Lau** This what the Gamma-Spec adjunction is all about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969190):
So, if you feel like writing an interface for schemes (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969196):
That is what would be the first challenge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969247):
https://stacks.math.columbia.edu/tag/01I2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969260):
Oh! The new Stacks project website went live!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969396):
indeed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969798):
Kevin, will you come to http://www.ihes.fr/~abbes/Gabber/gabber60-programme.html?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969927):
I wasn't planning on it. I just have too much on at the minute.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201413):
@**Kevin Buzzard** why are you using the broken definition of `basis` in `009I`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201813):
```lean
instance presheaf_on_basis_stalk.setoid  :
   setoid (presheaf_on_basis_stalk.aux) :=
{ r := λ Us Vt, ∃ (W : set X) (Hx : x ∈ W) (BW : W ∈ B) (HWU : W ⊆ Us.U) (HWV : W ⊆ Vt.U), 
   FPTB.res Us.BU BW HWU Us.s = FPTB.res Vt.BU BW HWV Vt.s,
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201818):
@**Kevin Buzzard** do you think we can change this definition to saying that they agree in the intersection?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201822):
oh no, we can't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202622):
It was a real annoyance that the intersection of two basis elements was not a basis element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202625):
I proved several results under two additional hypotheses:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202632):
1) intersection of two basis elements was a basis element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202633):
2) intersection of no basis elemnts was a basis element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202636):
Both of these are true for the D_f basis of Spec(R)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202638):
So in some cases I actually cut corners

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202689):
Kenny if you are sufficiently fanatical to go through those proofs and actually prove the correct statements then feel free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202702):
Even the definition of a sheaf got so much more complicated when working with a basis not closed under intersection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202719):
You have to check that the two functions are equal on the intersection by covering each intersection with new basis elements and checking that the res's coincide

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202726):
I just couldn't be bothered

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202851):
cf https://stacks.math.columbia.edu/tag/009L

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202852):
That's the tag I did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202880):
not the one before


{% endraw %}
