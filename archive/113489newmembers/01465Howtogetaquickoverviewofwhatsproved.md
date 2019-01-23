---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01465Howtogetaquickoverviewofwhatsproved.html
---

## Stream: [new members](index.html)
### Topic: [How to get a quick overview of what's proved?](01465Howtogetaquickoverviewofwhatsproved.html)

---

#### [Joseph Corneli (Jul 23 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130145533):
Hi, I'm new to Lean.  Specifically, I'm working my way through Chapter 3 of  "Theorem Proving in Lean" at the moment, having also installed mathlib and and the [xena-UROP-2018](https://github.com/ImperialCollegeLondon/xena-UROP-2018) work in progress.  Is there an efficient and meaningful way to get an overview of what has been proved in Lean to date?   I've run `find ./ | xargs grep "theorem"` in the `mathlib` directory, and adding a `grep -c "."` tells me roughly how many theorems have been proved, but the data is otherwise a bit hard to navigate.  It occurs to me that perhaps this question is most conveniently asked relative to some extrinsic knowledge base or bases, though something intrinsic, like the [pictures of the Linux Kernel](http://fcgp.sourceforge.net/), would also be interesting.   In addition to studying the TPiL book,  it's also nice to learn by reading the source.  I look forward to getting to the point where I can contribute!

#### [Kenny Lau (Jul 23 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130145546):
welcome

#### [Joseph Corneli (Jul 23 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130145592):
Thanks!

#### [Kenny Lau (Jul 23 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130145609):
you can look at the names of the files if you want to know what is in Lean... other than that I don't really know.

#### [Patrick Massot (Jul 23 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130147185):
At some point @**Kevin Buzzard** started to try to document this at https://github.com/leanprover/mathlib/blob/master/docs/theories.md, with some help from Chris. But it didn't go very far. You're welcome to contribute to this effort!

#### [Joseph Corneli (Jul 23 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130149675):
@**Patrick Massot** thanks I'll look (and perhaps add) there.  It might be interesting to have a version with "red links" (like on Wikipedia), to specifically indicate the things that people are interested in working on  (rather than trying to sum up the totality of all mathematical theories that aren't yet defined).

#### [Patrick Massot (Jul 23 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130149910):
Do you mean something like https://github.com/leanprover/mathlib/blob/master/docs/wip.md?

#### [Patrick Massot (Jul 23 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130149929):
We should update it by the way

#### [Joseph Corneli (Jul 23 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130149951):
Yes that's what I meant by "red links", thanks.

#### [Sean Leather (Jul 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130150496):
```quote
Do you mean something like https://github.com/leanprover/mathlib/blob/master/docs/wip.md?
```
@**Patrick Massot** Thanks for pointing that out. I [PR'd](https://github.com/leanprover/mathlib/pull/215) an update to add myself.

#### [Patrick Massot (Jul 23 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130154245):
We could even have a list of results that are very much proved: https://github.com/leanprover/mathlib/issues/216

#### [Kevin Buzzard (Jul 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130170995):
Brief overview: it's a bit random. Let me stick to maths. For example in ring theory we have rings, modules, and for commutative rings we have localisation, tensor products, and some stuff about Spec of a ring. There's currently a debate ranging about what the correct definition of Euclidean domain should be. For vector spaces we don't even have the equivalence between finite-dimensional vector spaces and k^n and all the consequences (linear maps = matrices etc); we don't have det(AB)=det(A)det(B) or anything like that -- we don't have signature of a permutation. On the other hand we have a bunch of stuff on Pell's equation and on Matiyesevich's proof that Diophantine = r.e. . For measure theory there is a whole bunch of stuff on measurable subsets of the reals -- however we don't have the definition of a differentiable function from R to R. No exp or sin or cos (although there is a PR), no proof that exp is continuous. I should say that I'm sticking here to what's in mathlib -- there are a bunch of random other things floating around, e.g. I have some repo which claims to define schemes (and even prove that an affine scheme is a scheme), and a bunch of students at Imperial College are working on completely random things (like finite-dimensional vector spaces, Sylow's theorems [done], fundamental groups). We're trying for perfectoid spaces but it's been slow going recently.

#### [Kevin Buzzard (Jul 24 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130179008):
Oh -- topology, there's stuff like completeness and compactness and various basic facts about these things. One vague aim of mine is to make coverage of the basics (by which I mean the material covered in the pure maths course in the first year or two of a university maths course) a little more consistent. Although I've heard terrifying things about the Cauchy integral formula...

#### [Joseph Corneli (Jul 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130222387):
Hi @**Kevin Buzzard** thanks for the comprehensive answer!  I've found another answer that's less comprehensive, but integrated with Lean in an interesting way: https://hanoifabs.wordpress.com/2018/06/14/mario-lean-catalog-june-13-2018/  -- I'm on Emacs, and browsing the file there with a Lean+mathlib installation causes lots of informative messages to appear in the `*Flycheck errors*` buffer.

#### [Mario Carneiro (Jul 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130259194):
It just so happens that I am presenting a talk today at ICMS which aims to answer exactly this question, so hopefully you will have some more stuff to look at soon

#### [Patrick Massot (Jul 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130259262):
Great!

#### [Patrick Massot (Jul 26 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130306917):
Do you have slides of your talks? I was just reminded of ICMS because a colleague attending ICMS just emailed me to tell he heard of a Lean conference in Amsterdam that I might be interested in :smile:

#### [Simon Hudon (Jul 26 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130312512):
I used Leo's slides from his Oxford talk as an introduction and the rest of the talk happened in emacs

#### [Simon Hudon (Jul 26 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130312518):
I'm really unhelpful, aren't I?

#### [Mario Carneiro (Jul 26 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130315090):
That would be Rob's talk, which ended with an ad for Lean Together

#### [Patrick Massot (Jul 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20get%20a%20quick%20overview%20of%20what%27s%20proved%3F/near/130327831):
This was my guess indeed

