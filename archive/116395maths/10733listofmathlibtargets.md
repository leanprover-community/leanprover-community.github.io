---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10733listofmathlibtargets.html
---

## Stream: [maths](index.html)
### Topic: [list of mathlib targets](10733listofmathlibtargets.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132746533):
Over the next couple of days I'm going to have a good look at the perfectoid project from a "bottom up" perspective and try and get a coherent idea of some easy targets for mathlib. For example (although not directly related to the perfectoid project) I would imagine it would be relatively easy to define PID's now and prove that Euclidean domains are PID's and that PID's are UFD's. My feeling is that achievable goals like this should be on some sort of informal list somewhere. Once the p-adic numbers get accepted then defining the adeles of a number field should also be on this list (and if people aren't happy with a definition being on the list then I can propose a random simple theorem about adeles, but for me a definition is fine). Where should such a list live? I remember once, when I was thinking about formalising my graduate course of earlier this year, I thought about formalising the adeles and I made it an issue in mathlib, but now I realise that probably there is a huge list of little things which I'd like to see in mathlib (several of which I'll probably end up doing myself) and I don't think it's sane to have an issue for each of them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132746635):
I should perhaps say that as well as some easy targets I guess I might also end up listing some harder targets. Is there already a place for this? I've realised now that I want mathlib to become the new Bourbaki; that's what people are doing here, and that's the style that they're writing. I think it would be nice to help things along the way by having a list of goals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 25 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132747583):
p-adic numbers are already in mathlib: https://github.com/leanprover/mathlib/pull/262

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132748753):
I didn't notice that it already got merged! I was just leaving for a holiday the day it did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 25 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132750840):
There is https://github.com/leanprover/mathlib/blob/master/docs/wip.md but you can also use https://github.com/leanprover-community/mathlib/wiki

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751311):
This is not works in progress -- this is stuff which I want there to be progress on :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751428):
I agree PIDs are gap that needs fixing soon! I've been suggesting my students @**Jack Crawford** and Ed Hofflin look at those, but as they're still getting started on Lean it may take a while.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751469):
Let's have a list on the leanprover-community wiki!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751530):
How does that work? If you start something, can other people edit it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751532):
I think so --- everyone who has commit access on leanprover-community, and I think the intention is that everyone who wants to make PRs to mathlib can have this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751573):
You should try editing the list I wrote for ideas of things to go over next week: https://github.com/leanprover-community/mathlib/wiki/Lean-in-Orsay,-2018

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 25 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751574):
My first thought would be to just use the github issue tracker. You can organize issues using labels, so I don't think having lots of "feature request" issues would be overwhelming.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751593):
What if we used issues on the main mathlib repository to indicate defects, and issues on the leanprover-community fork of mathlib for summaries of work in progress, or for wishlists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 25 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751747):
That's possible if that arrangement is clearly signposted somewhere (like, at the top of mathlib's README.md). I do like the idea of including entries for work-in-progress since we're already at the stage at which it can be hard to keep track of what everyone is working on.
Actually, brainstorming small projects of just the sort that Kevin mentioned is on my list of things to do next week, and part of the aim here is to give potential new contributors things to work on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 25 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751831):
For example, Zulip has the "good first issue" tag
https://github.com/zulip/zulip/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752066):
Maybe it does make sense to have them all in one place...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 25 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752140):
I'm kind of neutral about it. I do also see the appeal of keeping a separate list.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 25 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752210):
BTW, one of the items on my wishlist is the structure theorem for f.g. modules over a PID. Guess I didn't realize there are no PIDs yet either :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752296):
Smith normal form is a great project for someone who wants to learn how to do recursion well!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jack Crawford (Aug 25 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752682):
Yeah @**Scott Morrison**  I’m pretty keen on tackling Smith Normal Form sometime soon, along with PIDs. (At least, after midsems next week)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 25 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132756802):
Someone should also take a serious stab at algebraic closures.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758625):
I'm occasionally pestering @**Kenny Lau** to do these :-) Kenny -- can you give us an update of what needs to be done?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758632):
I think the issue is that there's some infrastructure which isn't there yet, but I've forgotten what.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758642):
For a while the hold-up was no robust theory of polynomials in 1 variable, but that is now done thanks to Chris.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758645):
splitting fields

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758647):
*boggle*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758649):
Do you need all the facts about them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758702):
I mean -- uniqueness? That's the annoying one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758704):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758705):
we don't even need minimality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758731):
Given a polynomial of degree n over a field K it's not too hard to prove by induction on n that there's a bigger field L contaning K where that polynomial factors into linear factors.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758734):
yeah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758735):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758740):
Is that tough?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758741):
Oh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758787):
You need that K[X]/(irred poly) is a field.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758792):
and you also need to prove that K[X] is UFD

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758794):
I don't think you need as much as that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758798):
Do you need uniqueness?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758807):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758808):
actually we don't need it to be a field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758809):
It suffices to prove we can add a root of a poly to a field and get a new field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758810):
given f

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758812):
K[X]/(f) is a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758813):
now what do you do with rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758814):
now take a max ideal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758815):
you quotient by a maximal ideal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758816):
tada

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758817):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758860):
genius

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758861):
I think Chris proved quotient by a max ideal was a field, recently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759244):
Polynomials are a Euclidean domain is there. I don't think Euclidean implies PID and PID implies prime ideals are maximal is that hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759250):
also PID doesn't imply prime ideals are maximal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759251):
also s/is/are/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 25 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759352):
Would the following idea be an option. It's a bit of a hack, because of `K : Type u`, then `K-bar : Type (u+1)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759361):
You let `Alg(K)` be the type of algebraic extensions of `K`, and then apply Zorn's lemma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759365):
Maybe with some trickery you can even get `K-bar` back into `Type u`. I'm not an expert on this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 25 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759411):
Anyway, whatever the definition, we will want a theorem that says that `K-bar` is unique up to iso.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Morenikeji Neri (Aug 26 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132787623):
I've actually defined PIDs and have a proof that compiles of ED -> PID (with some help from Chris) @**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132787801):
great, now get it to mathlib :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132788247):
I saw that yesterday!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132788248):
I'm hoping we can bring the proof down to something much smaller. After all, to explain it to a human is only a few lines!

