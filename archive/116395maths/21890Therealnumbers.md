---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/21890Therealnumbers.html
---

## Stream: [maths](index.html)
### Topic: [The real numbers](21890Therealnumbers.html)

---


{% raw %}
#### [ Kevin Buzzard (May 31 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331937):
<p>How are our real numbers getting along? Do we have the definition of a differentiable function yet, and of its derivative?</p>

#### [ Kenny Lau (May 31 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331992):
<p>one thing about analysis is that there are a lot of promises made</p>

#### [ Kenny Lau (May 31 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331996):
<p>when we say the derivative of a function, we don't just mean the derivative of a function</p>

#### [ Kenny Lau (May 31 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331999):
<p>we mean that it exists</p>

#### [ Kevin Buzzard (May 31 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332157):
<p>Do we have that the reals are the unique Dedekind-complete ordered field up to unique isomorphism?</p>

#### [ Kenny Lau (May 31 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332202):
<p>is R[ε] Dedekind-complete?</p>

#### [ Kevin Buzzard (May 31 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332210):
<p>I was writing a chapter in my book on reals and I was trying to figure out the interface that a mathematician needed.</p>

#### [ Kevin Buzzard (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332219):
<p>I figure we need the uniqueness statement above, and the intermediate value theorem and the mean value theorem</p>

#### [ Kevin Buzzard (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332221):
<p>and I reckon we have then got a huge chunk of 1st year Imperial analysis</p>

#### [ Andrew Ashworth (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332225):
<p>analysis is tricky, I took a long look at awhile back since I was interested in probability</p>

#### [ Kevin Buzzard (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332231):
<p>I could get students working on this over the summer but I don't have a clue about the current state of things and just thought it was easiest to ask</p>

#### [ Kenny Lau (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332232):
<p>I already proved the IVT ^^</p>

#### [ Kevin Buzzard (May 31 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332274):
<p>Where Kenny?</p>

#### [ Kenny Lau (May 31 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332279):
<p>in my own construction of the real numbers</p>

#### [ Kenny Lau (May 31 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332294):
<p><a href="https://github.com/kckennylau/Lean/blob/master/cauchy_real.lean#L1508" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/cauchy_real.lean#L1508">https://github.com/kckennylau/Lean/blob/master/cauchy_real.lean#L1508</a></p>

#### [ Andrew Ashworth (May 31 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332316):
<p>my plan for attacking it (which I eventually gave up on when I realized is was quite some work) was to follow the isabelle analysis theorems (many of them were written by johannes and jeremy avigad!)</p>

#### [ Andrew Ashworth (May 31 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332393):
<p>well, you could just ask <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  for his advice on what analysis developments to work on :)</p>

#### [ Kevin Buzzard (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332436):
<p>Kenny did you prove that your real numbers were the unique complete ordered field up to unique isomorphism?</p>

#### [ Kenny Lau (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332438):
<p>no</p>

#### [ Kevin Buzzard (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332442):
<p>Is it in mathlib?</p>

#### [ Kenny Lau (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332444):
<p>no idea</p>

#### [ Andrew Ashworth (May 31 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332530):
<p>out of curiosity is there a good reference on filters around? I only know about the Cauchy sequence construction, but it seems I must know more to use the reals in mathlib...</p>

#### [ Johannes Hölzl (May 31 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332539):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span>  most of Isabelle's analysis developed over some time. Starting from Fleuriot, over porting stuff from HOL Light by Amine Chaieb, and then generalizing it to type classes by Brian Huffman, Fabian Immler and me.</p>

#### [ Johannes Hölzl (May 31 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332541):
<p>and a lot of other people</p>

#### [ Johannes Hölzl (May 31 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332591):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I don't think there is a uniqueness proof in mathlib</p>

#### [ Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332645):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Given a point in a space, you get a "filter" of sets on the space, namely the sets containing the point.</p>

#### [ Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332652):
<p>So a filter is kind-of a generalization of a point</p>

#### [ Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332655):
<p>it's a really cool way of saying "tends to +infinity" for example</p>

#### [ Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332658):
<p>because even though infinity isn't a real number</p>

#### [ Johannes Hölzl (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332659):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> do you know our filter paper <a href="http://home.in.tum.de/~hoelzl/documents/hoelzl2013typeclasses.pdf" target="_blank" title="http://home.in.tum.de/~hoelzl/documents/hoelzl2013typeclasses.pdf">http://home.in.tum.de/~hoelzl/documents/hoelzl2013typeclasses.pdf</a> ? at least it explains how filters are used in Isabelle.</p>

#### [ Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332663):
<p>the sets of reals that contain an open interval (r,infinity) is a filter</p>

#### [ Johannes Hölzl (May 31 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332686):
<ul>
<li>the sets of sets (r, infinite) over all r</li>
</ul>

#### [ Johannes Hölzl (May 31 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332740):
<p>the sets of all neighbourhoods around x forms a filter, all left neighbourhoods (and right neibourhoods) etc</p>

#### [ Johannes Hölzl (May 31 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332826):
<p>but currently you need to do a lot of operations directly with filters, there is a lot of <em>porcelian</em> missing. Porcelain the sense that a lot the nice lemmas to show continuity of a function and using it are just not there yet. Many should be proved in a couple of lines but need to be written down.</p>

#### [ Kevin Buzzard (May 31 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332892):
<p>Am I right in thinking that <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> and <span class="user-mention" data-user-id="110064">@Kenny Lau</span> -- that all of you wrote distinct definitions of real numbers recently?</p>

#### [ Kevin Buzzard (May 31 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332893):
<p>Each one of you should prove the fundamental theorem of real numbers</p>

#### [ Kevin Buzzard (May 31 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332904):
<p>that you are a Dedekind complete ordered field</p>

#### [ Kevin Buzzard (May 31 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332913):
<p>and the moment you do that you can access all the theorems proved about the other real numbers</p>

#### [ Kevin Buzzard (May 31 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332921):
<p>Did you all do that?</p>

#### [ Mario Carneiro (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332965):
<p>Uniqueness is overrated</p>

#### [ Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332967):
<p>rofl</p>

#### [ Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332969):
<p>you people</p>

#### [ Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332971):
<p>you don't understand equality</p>

#### [ Mario Carneiro (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332974):
<p>It's really not needed for anything practical though</p>

#### [ Mario Carneiro (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332978):
<p>in a sense it tells you you "got it right" but that's it</p>

#### [ Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332979):
<p>it's needed for clear thinking</p>

#### [ Kevin Buzzard (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332984):
<p>and so we have to teach it to computers</p>

#### [ Kevin Buzzard (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332990):
<p>it makes the world a simpler place</p>

#### [ Mario Carneiro (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332993):
<p>when you want to apply theorems about reals, you need to have theorems on (your) reals</p>

#### [ Mario Carneiro (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332995):
<p>a uniqueness statement doesn't help here</p>

#### [ Kevin Buzzard (May 31 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333062):
<p>I just mean you can port theorems with the uniqueness statement</p>

#### [ Mario Carneiro (May 31 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333067):
<p>yeah, that's a bad idea, avoid if you can help it</p>

#### [ Kevin Buzzard (May 31 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333079):
<p>I want to do more than port theorems</p>

#### [ Kevin Buzzard (May 31 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333083):
<p>I want to identify them as one</p>

#### [ Mario Carneiro (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333125):
<p>Better to have a single definition and prove equivalent "views" of it</p>

#### [ Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333128):
<p>uniqueness theorem is a part of interface, because sometimes you would have more than one instance, because it's describing a class of objects (e.g. algebra homomorphism)</p>

#### [ Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333130):
<p>but in this case there is only one object that we call the real numbers</p>

#### [ Kevin Buzzard (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333131):
<p>I have so much to learn about the way you guys think about things.</p>

#### [ Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333133):
<p>we won't be constructing other real numbers</p>

#### [ Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333135):
<p>so I don't see why uniqueness is important</p>

#### [ Kevin Buzzard (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333149):
<p>What is the point of having three copies of the real numbers?</p>

#### [ Kevin Buzzard (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333154):
<p>Is one of them "the best one" or do they all have their merits or what?</p>

#### [ Kenny Lau (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333158):
<p>i just did it for myself</p>

#### [ Mario Carneiro (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333161):
<p>There's only one I'm aware of, unless Kenny did something</p>

#### [ Kenny Lau (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333164):
<p>i did it privately</p>

#### [ Mario Carneiro (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333204):
<p>There was an old construction by Johannes and I replaced it with my own</p>

#### [ Kevin Buzzard (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333207):
<p>I thought we had a filter one and a cauchy sequence one in mathlib at different times</p>

#### [ Kevin Buzzard (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333208):
<p>right</p>

#### [ Kevin Buzzard (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333210):
<p>and then Kenny's</p>

#### [ Mario Carneiro (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333213):
<p>The filter construction is gone, although the theorems aren't</p>

#### [ Kenny Lau (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333219):
<p>rip filter construction 2017-2018</p>

#### [ Kevin Buzzard (May 31 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333229):
<p>OK so Mario, let's say that in Johannes' construction of real numbers with filters, he proved that the real numbers were a Dedekind complete totally ordered field (he almost certainly did prove this, I believe I remember checking once).</p>

#### [ Kevin Buzzard (May 31 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333231):
<p>Then isn't that all you will ever need from the real numbers?</p>

#### [ Mario Carneiro (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333284):
<p>Yes, and that theorem is still there</p>

#### [ Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333287):
<p>no, you need a way to construct real numbers</p>

#### [ Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333288):
<p>like sqrt(2)</p>

#### [ Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333291):
<p>and filters are hard to work with</p>

#### [ Kevin Buzzard (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333292):
<p>but if Johannes had made it to that pinnacle</p>

#### [ Kevin Buzzard (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333294):
<p>you would never need to think about filters any more</p>

#### [ Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333299):
<p>how would you make sqrt(2)?</p>

#### [ Kevin Buzzard (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333310):
<p>take the sup of the set of real whose square was less than 2</p>

#### [ Mario Carneiro (May 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333329):
<p>My construction just slots in where the old one was, all the theorems still work after porting (with filters and everything)</p>

#### [ Kevin Buzzard (May 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333333):
<p>and then say that you're a complete field</p>

#### [ Mario Carneiro (May 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333347):
<p>The abstract theorems like that exist, but that's still a far cry from the "algebraic" theory with say transcendental functions</p>

#### [ Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333392):
<p>Chris did exp and sin and cos</p>

#### [ Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333395):
<p>did that ever make it into mathlib?</p>

#### [ Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333398):
<p>I need that for October!</p>

#### [ Kenny Lau (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333399):
<p>it's still in PR i think</p>

#### [ Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333406):
<p>If it needs work, let me know, that would be a great thing for students to work on</p>

#### [ Kevin Buzzard (May 31 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333414):
<p>I need e^(i theta) = cos(theta) + i sin(theta)</p>

#### [ Kenny Lau (May 31 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333422):
<p>you're on the wrong thread then</p>

#### [ Kevin Buzzard (May 31 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333432):
<p>you mentioned R[e] earlier, this is R[i]</p>

#### [ Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333708):
<p><a href="https://math.stackexchange.com/questions/269353/isomorphism-of-dedekind-complete-ordered-fields" target="_blank" title="https://math.stackexchange.com/questions/269353/isomorphism-of-dedekind-complete-ordered-fields">https://math.stackexchange.com/questions/269353/isomorphism-of-dedekind-complete-ordered-fields</a></p>

#### [ Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333715):
<p>The quote from Spivak</p>

#### [ Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333718):
<p>[not the question itself]</p>

#### [ Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333726):
<p>Is that proof, that any two complete ordered fields are isomorphic, in mathlib?</p>

#### [ Kenny Lau (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333767):
<p>(removed)</p>

#### [ Kevin Buzzard (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333774):
<p>up to unique isomorphism</p>

#### [ Kevin Buzzard (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333780):
<p>they are _the same_</p>

#### [ Kevin Buzzard (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333784):
<p>they are equal</p>

#### [ Kevin Buzzard (May 31 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333813):
<p>they are <code>maths-equivalent</code></p>

#### [ Mario Carneiro (May 31 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333950):
<p>Having that theorem will just make you more frustrated when it isn't as powerful as you want</p>

#### [ Reid Barton (May 31 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334011):
<p>Incidentally, in my limited experience, it's better not to work with any particular model of the reals directly, but just axiomatize the features that you need using type classes</p>

#### [ Kevin Buzzard (May 31 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334024):
<p>Don't prove a single theorem about the reals</p>

#### [ Kevin Buzzard (May 31 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334027):
<p>just prove a theorem about complete totally ordered fields?</p>

#### [ Reid Barton (May 31 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334032):
<p>I got frustrated when Lean would keep running out of memory when trying to check stuff like <code>rfl : 2 * 1 = 1 + 1</code></p>

#### [ Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334077):
<p>but then when I switched to working over a general totally ordered discrete topological whatever field, my compile times went way down</p>

#### [ Kenny Lau (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334078):
<p>that one is mul_one :P</p>

#### [ Kevin Buzzard (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334081):
<p>norm_num ftw</p>

#### [ Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334089):
<p>I know, but it's hard to stop Lean from trying to reduce</p>

#### [ Kenny Lau (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334090):
<p>2 is defined to be bit0 1, which is defined to be 1+1</p>

#### [ Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334100):
<p>It means every time you use <code>simp</code> or something, you might fall into a memory leak</p>

#### [ Mario Carneiro (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334102):
<p>but you still have to reduce (1+1)*1 = 1+1 there</p>

#### [ Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334103):
<p>and then you have to back up and carefully walk around it</p>

#### [ Reid Barton (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334115):
<p>Sure, and then <code>norm_num</code> can do that for you</p>

#### [ Kenny Lau (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334117):
<p>so I said it's <code>mul_one</code></p>

#### [ Andrew Ashworth (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334125):
<p>I have wondered whether the reals should be a typeclass too, in case somebody wants to have a really efficient computable version at some point in the future</p>

#### [ Kevin Buzzard (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334135):
<p>but Kenny what about <code>2/3*4/5=8/30*2</code></p>

#### [ Kenny Lau (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334137):
<p>but there is no computable version</p>

#### [ Mario Carneiro (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334179):
<p>well, the current version is as computable as it gets</p>

#### [ Kevin Buzzard (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334186):
<p>I see, so the issue is of course not about proving theorems, it is about doing calculations</p>

#### [ Kevin Buzzard (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334188):
<p>computations</p>

#### [ Mario Carneiro (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334189):
<p>i.e. stuff like <code>2 * 3 = 6</code> computes</p>

#### [ Kenny Lau (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334194):
<p>everything is about computation</p>

#### [ Kevin Buzzard (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334196):
<p>which are of course important when you want to prove theorems</p>

#### [ Kevin Buzzard (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334200):
<p>you want your reals to be "as computable as possible"?</p>

#### [ Mario Carneiro (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334206):
<p>well yes</p>

#### [ Kevin Buzzard (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334213):
<p>Don't you take one look at a question involving rationals and instantly descend to the rationals?</p>

#### [ Kenny Lau (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334216):
<p>then make <code>inv</code> into a function that takes a proof that it is not zero</p>

#### [ Mario Carneiro (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334217):
<p>I did</p>

#### [ Andrew Ashworth (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334218):
<p>Kenny, there is such a thing as constructive, computable reals. You can treat it as arbitrary-precision floating point</p>

#### [ Mario Carneiro (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334256):
<p>It's called <code>divp</code></p>

#### [ Kevin Buzzard (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334263):
<p>and does it work on an arbitrary complete totally ordered field?</p>

#### [ Mario Carneiro (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334265):
<p>It works on any <em>ring</em></p>

#### [ Kenny Lau (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334268):
<p>you won't want to formalize computable reals</p>

#### [ Andrew Ashworth (May 31 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334284):
<p>you won't want to, but yet it'll be super useful</p>

#### [ Kenny Lau (May 31 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334345):
<p>are you going to set up turing machines now</p>

#### [ Mario Carneiro (May 31 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334354):
<p>lol I'm actually typing out turing machines right now</p>

#### [ Mario Carneiro (May 31 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334361):
<p>Actually I'm going via Wang B-machines</p>

#### [ Kevin Buzzard (May 31 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127336402):
<p>Lean challenge : <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi mathvariant="normal">√</mi><mn>2</mn><mo>+</mo><mi mathvariant="normal">√</mi><mn>3</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">√</mi><mn>6</mn></mrow><annotation encoding="application/x-tex">(\surd2+\surd3)^2=5+2\surd6</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathrm">√</span><span class="mord mathrm">2</span><span class="mbin">+</span><span class="mord mathrm">√</span><span class="mord mathrm">3</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">5</span><span class="mbin">+</span><span class="mord mathrm">2</span><span class="mord mathrm">√</span><span class="mord mathrm">6</span></span></span></span></p>

#### [ Kenny Lau (May 31 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127336620):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>

<span class="kn">prefix</span> <span class="bp">`</span><span class="err">√</span><span class="bp">`</span><span class="o">:</span><span class="mi">90</span> <span class="o">:=</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="err">√</span><span class="mi">2</span> <span class="bp">+</span> <span class="err">√</span><span class="mi">3</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">2</span><span class="bp">*</span><span class="err">√</span><span class="mi">6</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span>
  <span class="err">←</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul</span><span class="o">,</span>
  <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul_self</span><span class="o">,</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul_self</span><span class="o">]</span><span class="bp">;</span> <span class="n">norm_num</span><span class="bp">;</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">add_assoc</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>

#### [ Kenny Lau (May 31 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127336744):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>

<span class="kn">prefix</span> <span class="bp">`</span><span class="err">√</span><span class="bp">`</span><span class="o">:</span><span class="mi">90</span> <span class="o">:=</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="err">√</span><span class="mi">2</span> <span class="bp">+</span> <span class="err">√</span><span class="mi">3</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">2</span><span class="bp">*</span><span class="err">√</span><span class="mi">6</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span>
  <span class="err">←</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul</span><span class="o">,</span>
  <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul_self</span><span class="o">,</span> <span class="n">real</span><span class="bp">.</span><span class="n">sqrt_mul_self</span><span class="o">,</span> <span class="n">add_right_comm</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">norm_num</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127341099):
<p>Thanks Kenny.</p>

#### [ Kevin Buzzard (May 31 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127341111):
<p>In <code>data/real/basic.lean</code> there is an import of <code>algebra.big_operators </code> which doesn't seem to me to be used. Is this sort of PR welcome?</p>

#### [ Kevin Buzzard (May 31 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342055):
<p><a href="https://github.com/leanprover/mathlib/blob/bdd54acda358f535b42951b784757135213dcf52/data/real/basic.lean#L16" target="_blank" title="https://github.com/leanprover/mathlib/blob/bdd54acda358f535b42951b784757135213dcf52/data/real/basic.lean#L16">https://github.com/leanprover/mathlib/blob/bdd54acda358f535b42951b784757135213dcf52/data/real/basic.lean#L16</a></p>

#### [ Kevin Buzzard (May 31 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342065):
<p>At that line, <code>#check mk</code> gives that <code>mk</code> is <code>rat.mk</code>. And then on the next line it feels like it was redefined. Why is mk not overloaded now?</p>

#### [ Kevin Buzzard (May 31 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342067):
<p>Is there some priority trick?</p>

#### [ Mario Carneiro (May 31 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342234):
<p><code>mk</code> is overloaded at that point. But when one of the theorems with that name is in the current namespace (i.e. inside a <code>namespace</code> block), it takes precedence over other <code>open</code> namespaces.</p>

#### [ Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342250):
<p>I see. Thanks.</p>

#### [ Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342253):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">ℝ</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">x</span> <span class="n">y</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="n">mk</span> <span class="o">(</span><span class="n">f</span> <span class="bp">+</span> <span class="n">g</span><span class="o">))</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">f₁</span> <span class="n">g₁</span> <span class="n">f₂</span> <span class="n">g₂</span> <span class="n">hf</span> <span class="n">hg</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span>
  <span class="k">by</span> <span class="n">simpa</span> <span class="o">[(</span><span class="bp">≈</span><span class="o">),</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">r</span><span class="o">]</span> <span class="kn">using</span> <span class="n">add_lim_zero</span> <span class="n">hf</span> <span class="n">hg</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342254):
<p>and then</p>

#### [ Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342255):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_neg</span> <span class="n">ℝ</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on</span> <span class="n">x</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">mk</span> <span class="o">(</span><span class="bp">-</span><span class="n">f</span><span class="o">))</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">f₁</span> <span class="n">f₂</span> <span class="n">hf</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span>
  <span class="k">by</span> <span class="n">simpa</span> <span class="o">[(</span><span class="bp">≈</span><span class="o">),</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">r</span><span class="o">]</span> <span class="kn">using</span> <span class="n">neg_lim_zero</span> <span class="n">hf</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342257):
<p>That's the same code again!</p>

#### [ Mario Carneiro (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342305):
<p>sure is, less than 30 seconds copy paste work</p>

#### [ Kevin Buzzard (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342307):
<p>That should be <code>by math_trivial [add_lim_zero]</code></p>

#### [ Kevin Buzzard (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342311):
<p>and then <code>by math_trivial [neg_lim_zero]</code></p>

#### [ Mario Carneiro (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342315):
<p>like I said, ~20 times repetition before I even consider making a tactic</p>

#### [ Mario Carneiro (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342321):
<p>6 or 7 times is not enough</p>

#### [ Kevin Buzzard (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342329):
<p>but if someone just came along and made that tactic and offered it to mathlib, do you think it would be useful?</p>

#### [ Kevin Buzzard (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342330):
<p>I am seeing this ... idiom or whatever you call it over and over again</p>

#### [ Kevin Buzzard (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342332):
<p>"we laboriously transport structure"</p>

#### [ Mario Carneiro (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342334):
<p>in particular, it is often the case that all the axioms of concrete structure X are similar to each other, but not similar to structure Y</p>

#### [ Mario Carneiro (May 31 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342382):
<p>having a tactic that proves axioms of X is not that helpful since there are only O(1) of them, and the tactic won't help with Y</p>

#### [ Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342387):
<p>Transport of structure is a central idea of mathematics as we see in the work of Grothendieck and Deligne</p>

#### [ Mario Carneiro (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342390):
<p>Would this <code>math_trivial</code> tactic apply equally to <code>real</code> and <code>pnat</code>?</p>

#### [ Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342392):
<p>This is just the sort of thing I want to find out</p>

#### [ Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342395):
<p>I found myself when doing schemes</p>

#### [ Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342397):
<p>wanting a tactic like this</p>

#### [ Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342398):
<p>and I know that when I start perfectoids</p>

#### [ Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342401):
<p>I'll find it again</p>

#### [ Mario Carneiro (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342444):
<p>My point is that there are not that many similarities between the proof that <code>pnat</code> has an add and <code>real</code> does</p>

#### [ Kevin Buzzard (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342447):
<p>yeah isn't that interesting</p>

#### [ Kenny Lau (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342450):
<p>lol</p>

#### [ Kenny Lau (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342451):
<p>Kevin</p>

#### [ Kenny Lau (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342452):
<p>the sky is blue</p>

#### [ Kevin Buzzard (May 31 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342462):
<p>These guys need to make a proper mathematician</p>

#### [ Kevin Buzzard (May 31 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342464):
<p>with the right kind of equals</p>

#### [ Kenny Lau (May 31 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342506):
<p>it's foggy</p>

#### [ Kenny Lau (May 31 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342511):
<p>relative humidity 98%</p>

#### [ Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342570):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> Extra instances to short-circuit type class resolution -/</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="n">ℝ</span>      <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">monoid</span> <span class="n">ℝ</span>         <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_semigroup</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">ℝ</span>    <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">add_monoid</span> <span class="n">ℝ</span>     <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">ℝ</span>      <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">add_comm_group</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">ℝ</span>           <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342571):
<p>Why do they make life better?</p>

#### [ Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342572):
<p>This is all in data/real/basic.lean</p>

#### [ Kenny Lau (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342573):
<p>because beneath you is an uncomputable instance</p>

#### [ Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342575):
<p>those are the best kind IMO</p>

#### [ Kenny Lau (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342576):
<p>if you don't do this, the uncomputable instance will be used</p>

#### [ Kenny Lau (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342614):
<p>so your definitions would have to be noncomputable</p>

#### [ Kenny Lau (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342619):
<p>and it is used because it is declared the latest</p>

#### [ Kevin Buzzard (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342620):
<p>none of this makes any sense to me</p>

#### [ Mario Carneiro (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342621):
<p>no, that's not related</p>

#### [ Mario Carneiro (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342623):
<p>those instances</p>
<blockquote>
<p>short-circuit type class resolution</p>
</blockquote>

#### [ Kevin Buzzard (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342626):
<p>so they are creating new paths in the system</p>

#### [ Kenny Lau (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342627):
<p>well in my construction, if I don't do that, my things become uncomputable</p>

#### [ Kevin Buzzard (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342629):
<p>which are defeq to longer paths</p>

#### [ Mario Carneiro (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342630):
<p>yes</p>

#### [ Kevin Buzzard (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342635):
<p>and this is perhaps making the system better for some reason</p>

#### [ Kevin Buzzard (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342640):
<p>why doesn't the system run all those commands every time anyone makes anything a comm_ring?</p>

#### [ Mario Carneiro (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342641):
<p>it means less time traversing the instance graph</p>

#### [ Kevin Buzzard (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342642):
<p>then it would be much less time</p>

#### [ Mario Carneiro (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342645):
<p>because that wouldn't save any time, it would just create lots of space</p>

#### [ Kevin Buzzard (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342685):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_lt</span> <span class="n">ℝ</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">x</span> <span class="n">y</span> <span class="o">(</span><span class="bp">&lt;</span><span class="o">)</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">f₁</span> <span class="n">g₁</span> <span class="n">f₂</span> <span class="n">g₂</span> <span class="n">hf</span> <span class="n">hg</span><span class="o">,</span> <span class="n">propext</span> <span class="err">$</span>
  <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">lt_of_eq_of_lt</span> <span class="o">(</span><span class="n">setoid</span><span class="bp">.</span><span class="n">symm</span> <span class="n">hf</span><span class="o">)</span> <span class="o">(</span><span class="n">lt_of_lt_of_eq</span> <span class="n">h</span> <span class="n">hg</span><span class="o">),</span>
   <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">lt_of_eq_of_lt</span> <span class="n">hf</span> <span class="o">(</span><span class="n">lt_of_lt_of_eq</span> <span class="n">h</span> <span class="o">(</span><span class="n">setoid</span><span class="bp">.</span><span class="n">symm</span> <span class="n">hg</span><span class="o">))</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342687):
<p>They're getting quite tricky for my tactic now</p>

#### [ Mario Carneiro (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342689):
<p>If you do it in <em>every</em> case, there is no advantage over just searching the graph, since you have just precalculated all paths</p>

#### [ Kevin Buzzard (May 31 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342692):
<p>ha ha</p>

#### [ Mario Carneiro (May 31 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342699):
<p>the point is that I know that <code>real</code> is important and people want to use it lots</p>

#### [ Mario Carneiro (May 31 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342702):
<p>so I set up the system to make that easier</p>

#### [ Kevin Buzzard (May 31 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342742):
<p>What else can you control within the type class inference system?</p>

#### [ Mario Carneiro (May 31 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342743):
<p>so that when weirdos state <code>ring</code> theorems over the reals for some reason, it's not horribly slow</p>

#### [ Kevin Buzzard (May 31 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342748):
<p>I liked <span class="user-mention" data-user-id="110032">@Reid Barton</span> 's comment about typeclasses.</p>

#### [ Kevin Buzzard (May 31 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342763):
<div class="codehilite"><pre><span></span><span class="c1">--def real := quotient (@cau_seq.equiv ℚ _ _ _ abs _) -- orig</span>
<span class="n">def</span> <span class="n">real</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">equiv</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">cau_seq</span> <span class="n">ℚ</span> <span class="n">abs</span><span class="o">))</span> <span class="c1">-- clearer for me</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342764):
<p>You prefer yours?</p>

#### [ Kevin Buzzard (May 31 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342767):
<p><code>@</code> and <code>_</code> are a bit ugly maybe</p>

#### [ Kevin Buzzard (May 31 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342806):
<p>but yours is shorter</p>

#### [ Mario Carneiro (May 31 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342867):
<div class="codehilite"><pre><span></span>def real := @quotient (cau_seq ℚ abs) cau_seq.equiv
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343308):
<p>What is your preference? The mathlib one?</p>

#### [ Mario Carneiro (May 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343310):
<p>I don't have a strong preference</p>

#### [ Kevin Buzzard (May 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343312):
<p>In terms of Lean they're all presumably defeq</p>

#### [ Kevin Buzzard (May 31 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343321):
<p>but in terms of readability some have more worth than others</p>

#### [ Mario Carneiro (May 31 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343351):
<p>they are all syntactically equal</p>

#### [ Kevin Buzzard (May 31 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343365):
<p>My favourite is the last one <code>@quotient (cau_seq ℚ abs) cau_seq.equiv</code> because it's the most readable to mathematicians</p>

#### [ Kevin Buzzard (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343406):
<p><code>instance : has_le ℝ := ⟨λ x y, x &lt; y ∨ x = y⟩</code></p>

#### [ Kevin Buzzard (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343408):
<p>You've gone the wrong way</p>

#### [ Kevin Buzzard (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343411):
<p>you can do <code>has_le</code> first and get <code>has_lt</code> for free!</p>

#### [ Mario Carneiro (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343412):
<p>I know</p>

#### [ Kevin Buzzard (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343413):
<p>You did it this way for a reason, presumably?</p>

#### [ Mario Carneiro (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343418):
<p>the constructively natural one is lt</p>

#### [ Kevin Buzzard (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343419):
<p>I see</p>

#### [ Kevin Buzzard (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343420):
<p>it's all about computing</p>

#### [ Mario Carneiro (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343421):
<p>it states that there is some epsilon separating them</p>

#### [ Mario Carneiro (May 31 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343422):
<p>for le, it's either the negation of that or the disjunction with equals</p>

#### [ Patrick Massot (May 31 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127349002):
<blockquote>
<p>that you are a Dedekind complete ordered field</p>
</blockquote>
<p>Note: as a mathematician, I use real numbers every day, and I have no idea what is a "Dedekind complete ordered field"</p>

#### [ Patrick Massot (May 31 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127349061):
<blockquote>
<p>How are our real numbers getting along? Do we have the definition of a differentiable function yet, and of its derivative?</p>
</blockquote>
<p>I have a definition of a function from a real normed vector space to another one which is differentiable at a point. But I don't have a normed space structure on ℝ^n because I'm swamped in type class resolution issues (<a href="#narrow/stream/113488-general/topic/tc.20loop.20again" title="#narrow/stream/113488-general/topic/tc.20loop.20again">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc.20loop.20again</a>). Life is really hard here.</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388365):
<p><em>boggle</em> I am typing up my exam into Lean and I need the fact that the decimal expansion of the real number 0.71 contains no 8's :-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388372):
<p>does Lean have decimal expansions??</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388432):
<p>maybe a function from the non-negative reals to (functions from nat to nat)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388438):
<p>with f(succ n)&lt;=9</p>

#### [ Kenny Lau (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388441):
<p>you can write that yourself</p>

#### [ Kenny Lau (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388444):
<p>it's quite explicit using floor</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388446):
<p>you are right!</p>

#### [ Kenny Lau (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388450):
<p>given a real number r</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388452):
<p>But I was just asking if someone had already written it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388454):
<p>Kenny I can do it :-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388456):
<p>I even lecture it in M1F some years</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388459):
<p>Darn it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388463):
<p>if I'd lectured it this year then <span class="user-mention" data-user-id="110044">@Chris Hughes</span>  would have done it :-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389782):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="c1">-- should come with a warning</span>

<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">real</span><span class="bp">.</span><span class="n">floor</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="o">:=</span>
  <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">real</span><span class="bp">.</span><span class="n">exists_floor</span> <span class="n">x</span><span class="o">)</span>

<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">expansion</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">≥</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">real</span><span class="bp">.</span><span class="n">floor</span> <span class="n">r</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">7</span>
</pre></div>

#### [ Kevin Buzzard (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389786):
<p>I made a slip: real.floor r on the last but one line is an int not a nat</p>

#### [ Kenny Lau (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389791):
<p>Kevin</p>

#### [ Kenny Lau (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389792):
<p>the fllor is there already</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389794):
<p>but when using reals, sllips like this bring the system to its knees. 100% CPU usage, orange bars</p>

#### [ Kenny Lau (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389797):
<p>it's in archimedean</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389804):
<p>Thanks</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389809):
<p>but why does my code make Lean have a deterministic timeout?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389811):
<p>Mario has answered this before</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389853):
<p>but this behaviour ("use the imported definitions wisely or there will be timeouts") is not the norm</p>

#### [ Kenny Lau (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389864):
<p>it's just a typeclass fallout</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389866):
<p>right</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389870):
<p>but is this a design problem with Lean or something which can be fixed in mathlib or what?</p>

#### [ Kenny Lau (Jun 01 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389877):
<p>no idea</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389940):
<p>hey that floor_ring stuff is a really cool way of doing it :-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390072):
<p><code>⌊10 / 3⌋ : ℤ</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390088):
<p><code>#reduce ⌊(real.sqrt 2 : ℝ)⌋</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390092):
<p>100% CPU usage!</p>

#### [ Mario Carneiro (Jun 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390094):
<p>For some reason, coercing an int to a nat causes a typeclass overflow</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390096):
<p>segv :-)</p>

#### [ Mario Carneiro (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390133):
<p>I've seen this many times before</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390141):
<p>but it's only with reals</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390143):
<p>Lean is really good with most structures</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390151):
<p>Oh indpt of reals?</p>

#### [ Mario Carneiro (Jun 01 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390169):
<p>you defined an int function and applied it to get a  nat</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390186):
<p>I know</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390193):
<p>I assumed the problem was because reals always time out</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390237):
<p>but maybe you fixed that</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390253):
<p>and this is an independent timeout</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390254):
<p>The major source of that was fixed a while ago</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390260):
<p>this is just Z -&gt; N timeout</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390266):
<p>What do you get with</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390267):
<p><code>#reduce ⌊(real.sqrt 2 : ℝ)⌋</code> ?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390276):
<p>something horrible, don't do that</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390279):
<p>What part of <code>noncomputable</code> don't you understand?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390283):
<p>:-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390286):
<p>I thought there was no harm trying</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390288):
<p>it will be some huge stuck term depending on <code>classical.choice</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390289):
<p>after all, schoolkid can do it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390326):
<p>it's 1 Mario</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390330):
<p>You can do it, but not like this</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390334):
<p>In order for <code>reduce</code> to work it has to be true generally</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390335):
<p>this is going to be tough to explain to the mathematicians</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390340):
<p>I'm just being daft, I know about eval</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390344):
<p>and there are messy terms you can give where it's impossible to decide</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390347):
<p><code>#eval</code> won't do any better</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390354):
<p>no but it could</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390356):
<p>actually it will just complain up front</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390362):
<p>no it can't, <code>real.floor</code> is <em>necessarily</em> noncomputable</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390371):
<p>the reduce gives me a segv (twice now)</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390414):
<p>What <em>can</em> do better is <code>norm_num</code> style tactics that prove specific instances of this in some subset of the full language of lean</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390415):
<p>but the floor of the square root of 2 isn't noncomputable</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390426):
<p>That statement doesn't make sense</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390431):
<p>noncomputability is a property of a term, not its denotation</p>

#### [ Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390432):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> local computability does not patch to give global computability</p>

#### [ Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390442):
<p>it ain't no sheaf</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390443):
<p>is the obstruction finite?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390444):
<p>?</p>

#### [ Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390446):
<p>floor is computable iff halting problem can be solved</p>

#### [ Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390448):
<p>you have an obstructio in each integer, so no it ain't finite</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390449):
<p>I know but you can do it on sqrt(2)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390450):
<p>I can prove that 1 is floor of sqrt(2)</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390491):
<p>So do that</p>

#### [ Kenny Lau (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390493):
<p>that doesn't mean you can compute floor(sqrt(2))</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390495):
<p>so it can be computed in this case</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390497):
<p>Kenny -- doesn't it?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390500):
<p><code>floor (sqrt 2)</code> is a computable number, yes</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390502):
<p>but <code>floor</code> is not a computable function</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390509):
<p>so you can't just plug <code>sqrt 2</code> into <code>floor</code> and expect an answer</p>

#### [ Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390516):
<p>you need uniform computability without creativeness</p>

#### [ Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390519):
<p>informally</p>

#### [ Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390520):
<p>you need a canonical function</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390521):
<p>We could get transcendental numbers into Lean if we could get Chris' sin and cos stuff</p>

#### [ Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390523):
<p>that works across everything</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390566):
<p>floor is daft. Give me exp any day</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390572):
<p>Is that computable?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390574):
<p>By the way, floor is computable on algebraic numbers</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390575):
<p>I reckon I can prove the sequence is Cauchy</p>

#### [ Kenny Lau (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390579):
<p>everything is computable on algebraic numbers</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390581):
<p>so you can write <code>floor (sqrt 2)</code> and compute to <code>1</code></p>

#### [ Kenny Lau (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390584):
<p>surprise</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390586):
<p><code>exp</code> is computable</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390589):
<p>Kenny I'm sure there are non-recursive or whatever subsets of the natural numbers</p>

#### [ Kenny Lau (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390640):
<p>I was uttering hyperbole</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390641):
<p>and so of the algebraic numbers</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390643):
<p>I think real numbers are overrated in math</p>

#### [ Kenny Lau (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390644):
<p>agree</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390645):
<p>They're just some random completion</p>

#### [ Kenny Lau (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390646):
<p>I was about to say, let's study other local fields</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390647):
<p>that sometimes helps in physics</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390649):
<p>exactly</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390651):
<p>you don't need <em>full</em> completion in 99.9% of cases</p>

#### [ Kenny Lau (Jun 01 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390657):
<p>but there's a problem <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390658):
<p>in number theory we need the product of all the completions :-)</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390659):
<p>something like complete under computable sequences is more than enough</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390699):
<p>Mario do you think Langlands' work on cyclic base change would work with this smaller subset of the reals?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390700):
<p>or maybe "complete under all the operations I'm talking about today"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390705):
<p>I'm sure it uses AC everywhere</p>

#### [ Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390706):
<p>I can't recall the name of the theroem</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390707):
<p>it's not so different to doing categories in ZFC</p>

#### [ Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390709):
<p>but essentially, if you include exp, then your field is noncomputable</p>

#### [ Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390710):
<p>algebraic numbers and exp</p>

#### [ Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390711):
<p>maybe some other things</p>

#### [ Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390712):
<p>maybe you'll know the name</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390713):
<p>you just want enough stuff for your theorem, but you assume too much for simplicity</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390779):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I guess it would be too easy to just compute to find out if e + pi is irrational</p>

#### [ Kenny Lau (Jun 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390782):
<p>that's irrelevant</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390784):
<p>for every rational r, if you spent enough time, you can prove that e+pi is not r</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390825):
<p>you just can't prove that, for every rational r, e+pi is not r</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390829):
<p>decidable equality doesn't mean decidable pi equality</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390831):
<p>pi equality meaning forall equality</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390832):
<p>not 3.14159</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390834):
<p>I know, but rationality is decidable on algebraic numbers</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390835):
<p>oh is it</p>

#### [ Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390837):
<p>how do you define algebraic numbers?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390838):
<p>yes, just compute the minimal polynomial and see if it has degree 1</p>

#### [ Kenny Lau (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390845):
<p>do you store the minimal polynomial?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390846):
<p>yes</p>

#### [ Kenny Lau (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390847):
<p>I see</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390900):
<p>I think the most impressive thing about the algebraic numbers is that irreducibility and factoring of Q[x] polynomials is decidable</p>

#### [ Kenny Lau (Jun 01 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390904):
<p>agree</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391365):
<p>come on norm-num</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391366):
<p><code>↑⌊0⌋ * 10 = 0</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391367):
<p>you can do it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391369):
<p>gaargh</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391374):
<p>stupid floor function</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391420):
<p>oh there is a lemma</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391422):
<p>I remember now</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391429):
<p><code>floor_coe</code></p>

#### [ Mario Carneiro (Jun 01 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391439):
<p>I guess floor_zero and floor_one should be simp lemmas</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391442):
<p>and theorems</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391511):
<p>oh you're right, that's not (0 : Z)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391514):
<p>that one of your other zeros</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391560):
<p>it's defeq though, you can just apply <code>floor_coe</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391939):
<p>not in a rewrite :-/</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391953):
<p>here, use as you like:</p>
<div class="codehilite"><pre><span></span>@[simp] theorem floor_zero : ⌊(0:α)⌋ = 0 := floor_coe 0

@[simp] theorem floor_one : ⌊(1:α)⌋ = 1 :=
by rw [← int.cast_one, floor_coe]
</pre></div>

#### [ Kenny Lau (Jun 01 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391956):
<blockquote>
<p>that one of your other zeros</p>
</blockquote>
<p>lol</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392017):
<p>unfortunately this doesn't help with say <code>⌊2⌋ = 2</code>, that gets tricky in general</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392018):
<p>because the two <code>2</code>'s are represented differently</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392030):
<p>I've got interested in what needs names</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392031):
<p>I would vote for floor_zero</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392080):
<p>rofl I just tried it in my code and it didn't work</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392085):
<p>and then I remembered that someone writing some code on the internet doesn't mean my computer runs it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392087):
<p>and you have to copy paste</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392101):
<p>Those lines were written in <code>archimedean.lean</code>, they might not work out of context</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392176):
<p>I know archimedean.lean so I could fix it up</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392179):
<p>I've been reading some of the real code recently</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392181):
<p>and I'd missed archimedean so I read it the moment Kenny pointed it out to me</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392183):
<p>I already have added those lines to my local copy, they will be out with the next batch</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392224):
<p>I was just thinking I should do the same</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392225):
<p>but for me it's much harder</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392232):
<p>I'm doing undergrad stuff in my xena project at the minute (e.g. decimal expansions) but the library imports your mathlib</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392249):
<p>so I can't edit my fork of your mathlib and then run it easily in my project, unless I actually start importing my mathlib</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393083):
<p>ha ha, to finish Q2 of my exam all I now need to do is to prove that if <code>s : ℝ := 71/100</code> then <code>⌊s⌋ = 7</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393085):
<p>the students didn't spend too much time on this bit</p>

#### [ Kenny Lau (Jun 01 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393100):
<p>does that mean you finished Q1?</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393146):
<p>I guess this isn't stated as a theorem explicitly, but the way to prove <code>⌊x⌋ = n</code> is to prove <code>n &lt;= x &lt; n+1</code>, and norm_num will usually take care of that</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393148):
<p>no</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393149):
<p>I liked Q2 better</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393151):
<p>right</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393153):
<p>also, the theorem you stated is false</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393159):
<p>the floor of s is zero</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393160):
<p>:-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393161):
<p>oh too many 10s</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393162):
<p>sorry</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393167):
<p>I have to work out the full decimal expansion</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393169):
<p>so i need a fair few floors</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393211):
<p>You really want to do this on rat</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393212):
<p>then you can just compute</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393216):
<p>just take your real number and map it to rat</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393271):
<p>I didn't know to what extent that mattered</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393275):
<p>now I need some theorem that says that the floors agree</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393282):
<p><code>noncomputable definition s : ℝ := 71/100
lemma bound1 : 0 ≤ s := by norm_num -- fails</code> :-(</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393284):
<p>I am already on it</p>

#### [ Kenny Lau (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393285):
<p><code>by unfold s; norm_num</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393286):
<p>thanks</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394102):
<p>this should work for you:</p>
<div class="codehilite"><pre><span></span>@[simp] theorem rat.cast_floor
  {α} [linear_ordered_field α] [archimedean α] (x : ℚ) :
  by haveI := archimedean.floor_ring α; exact ⌊(x:α)⌋ = ⌊x⌋ :=
begin
  haveI := archimedean.floor_ring α,
  apply le_antisymm,
  { rw [le_floor, ← @rat.cast_le α, rat.cast_coe_int],
    apply floor_le },
  { rw [le_floor, ← rat.cast_coe_int, rat.cast_le],
    apply floor_le }
end
</pre></div>

#### [ Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394219):
<p>you have to use <code>haveI</code> in the statement to make it typecheck</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394222):
<p>I did...</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394224):
<p>and then again in the proof</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394227):
<p>The devs don't come here, this is the maths chat</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394230):
<p>what do you think about all this haveI stuff?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394269):
<p>Aren't things worse than they used to be?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394272):
<p>Or did other stuff get fixed when that change was made?</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394273):
<p>I think I got Leo angry about it, so I'm not going to try again</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394275):
<p>haveI is the compromise position</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394281):
<p>...but it's not unreasonable here</p>

#### [ Mario Carneiro (Jun 01 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394290):
<p>I'm injecting an instance which is not an instance normally</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394371):
<p>Thanks.</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394670):
<p>I feel like I want to apply <code>int.succ_le_of_lt</code> out of decency</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394677):
<p><code>lemma int.succ_le_of_lt (a b : ℤ) : a &lt; b → int.succ a ≤ b :=</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394680):
<p>but proof is id</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394683):
<p>It's up to you</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394721):
<p>it looks like bad style to just know it's id</p>

#### [ Kenny Lau (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394724):
<p>who the .... cares</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394727):
<p>it's the interface Kenny</p>

#### [ Kenny Lau (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394734):
<p>proofs are irrelevant</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394735):
<p>id sometimes deserves a name :-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394740):
<p>proofs are irrelevant but names are important</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394744):
<p>You are absolutely right, using defeq like this breaks the interface</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394750):
<p>but it's not a hill I want to die on</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394759):
<p>I would say "use in moderation"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395229):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">floor_of_bounds</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span>
  <span class="err">↑</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">↔</span> <span class="err">⌊</span> <span class="n">r</span> <span class="err">⌋</span> <span class="bp">=</span> <span class="n">z</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span> <span class="c1">-- easy one</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span><span class="n">rw</span> <span class="err">←</span><span class="n">H</span><span class="o">,</span>
    <span class="n">split</span><span class="o">,</span><span class="n">exact</span> <span class="n">floor_le</span> <span class="n">r</span><span class="o">,</span>
    <span class="n">suffices</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="err">↑⌊</span><span class="n">r</span><span class="err">⌋</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span>
      <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:=</span> <span class="n">lt_succ_floor</span> <span class="n">r</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H&#39;</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">d</span><span class="o">,</span> <span class="bp">@</span><span class="n">le_floor</span> <span class="n">α</span> <span class="bp">_</span> <span class="n">d</span> <span class="n">r</span><span class="o">,</span>

  <span class="n">intro</span> <span class="n">J</span><span class="o">,</span><span class="n">cases</span> <span class="n">J</span> <span class="k">with</span> <span class="n">floor_le&#39;</span> <span class="n">lt_succ_floor&#39;</span><span class="o">,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">le_or_gt</span> <span class="err">⌊</span><span class="n">r</span><span class="err">⌋</span> <span class="n">z</span><span class="o">)</span> <span class="k">with</span> <span class="n">HT</span> <span class="n">HF</span><span class="o">,</span>
  <span class="n">swap</span><span class="o">,</span> <span class="n">exfalso</span><span class="o">,</span> <span class="c1">-- false one</span>
  <span class="o">{</span> <span class="k">have</span> <span class="n">XXX</span> <span class="o">:=</span> <span class="o">(</span><span class="n">H</span> <span class="o">(</span><span class="n">z</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">succ_le_of_lt</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">HF</span><span class="o">),</span>
    <span class="n">rw</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span> <span class="n">at</span> <span class="n">XXX</span><span class="o">,</span>
    <span class="n">clear</span> <span class="n">HF</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">lt_of_le_of_lt</span> <span class="n">XXX</span> <span class="n">lt_succ_floor&#39;</span><span class="o">,</span>
    <span class="n">revert</span> <span class="n">H2</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="n">cases</span> <span class="n">lt_or_eq_of_le</span> <span class="n">HT</span> <span class="k">with</span> <span class="n">HF</span> <span class="n">HT&#39;</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span><span class="n">exact</span> <span class="n">HT&#39;</span><span class="o">,</span>
  <span class="n">exfalso</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">XXX</span> <span class="o">:=</span> <span class="o">(</span><span class="n">H</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">floor_le&#39;</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">lt_irrefl</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">lt_of_le_of_lt</span> <span class="n">XXX</span> <span class="n">HF</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 01 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395230):
<p>Rubbish lean code but it's a proof</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395235):
<p>What tricks am I missing?</p>

#### [ Kenny Lau (Jun 01 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395291):
<p><code>le_floor</code>?</p>

#### [ Kenny Lau (Jun 01 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395337):
<p>given <code>z &lt;= r</code>, use <code>le_floor</code> to deduce <code>z &lt;= floor(r)</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395346):
<p>here's the reals back to their old tricks</p>

#### [ Kenny Lau (Jun 01 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395388):
<p>given <code>r &lt; z+1</code>, <code>floor_lt</code> tells you <code>floor(r) &lt; z + 1</code></p>

#### [ Kenny Lau (Jun 01 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395391):
<p>then deduce <code>floor(r) &lt;= z</code> (everything is an integer now)</p>

#### [ Kenny Lau (Jun 01 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395393):
<p>and then <code>le_antisymm</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395400):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">s</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="mi">71</span><span class="bp">/</span><span class="mi">100</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">floor</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">show</span> <span class="n">floor</span> <span class="o">((</span><span class="mi">71</span><span class="bp">/</span><span class="mi">100</span><span class="o">:</span><span class="n">ℚ</span><span class="o">):</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 01 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395401):
<p>deterministic timeout</p>

#### [ Kenny Lau (Jun 01 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395406):
<p>because 71:R / 100:R is not defeq to 71:Q / 100:Q</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395446):
<p>I did it by contradiction :-)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395450):
<p>you always want to do things constructively</p>

#### [ Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395451):
<p>?</p>

#### [ Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395454):
<p>I see</p>

#### [ Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395455):
<p>to each their own</p>

#### [ Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395457):
<p>I have no time</p>

#### [ Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395458):
<p>I need to learn what the Weil group is</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395459):
<p>oh the coercion to R is done before the division</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395466):
<p>The magic of biconditional theorems...</p>
<div class="codehilite"><pre><span></span>lemma floor_of_bounds (r : α) (z : ℤ) :
  ↑z ≤ r ∧ r &lt; (z + 1) ↔ ⌊ r ⌋ = z :=
by rw [← le_floor, ← int.cast_one, ← int.cast_add, ← floor_lt,
  int.lt_add_one_iff, le_antisymm_iff, and.comm]
</pre></div>

#### [ Kenny Lau (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395470):
<p>lol</p>

#### [ Kenny Lau (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395472):
<p>two lines vs 100 lines</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395473):
<p>very nice</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395475):
<p>but I never got stuck</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395477):
<p>I just proved it and enjoyed it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395478):
<p>walking around the gardens of mathematics</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395526):
<p>oh you proved by contradiction</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395527):
<p>that's a bit roundabout</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395571):
<p>it's inbuilt</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395575):
<p>I asked 250 students to prove sup(S) + sup(T) = sup(S+T)</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395576):
<p>you have so many cases in this proof...</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395577):
<p>and about 80 did it</p>

#### [ Kenny Lau (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395578):
<p>really</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395579):
<p>and 79 did it by contradiction</p>

#### [ Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395581):
<p>such a simple theorem</p>

#### [ Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395584):
<p>only 80 out of 250</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395588):
<p>it's about that</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395590):
<p>I didn't count carefully and it's all gone back to the exams office now</p>

#### [ Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395591):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and the 1 is me lol</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395592):
<p>maybe more</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395594):
<p>I recall this story</p>

#### [ Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395595):
<p>like seriously</p>

#### [ Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395598):
<p>the UMPs of sup is all you need</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395599):
<p>contradiction is the most powerful method of proof</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395600):
<p>you get to assume the most stuff</p>

#### [ Kenny Lau (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395640):
<p>but 0% of the people know about UMP and UMP of sup</p>

#### [ Kenny Lau (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395644):
<p>rounded down to the nearest percent</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395645):
<p>I'm not even against it on intuitionistic grounds</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395647):
<p>if you've never had your brain polluted by constructivism it's a very natural first step</p>

#### [ Kenny Lau (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395652):
<p>cleansed</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395654):
<p>it has a way of making thinking easier and proof more complicated</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395656):
<p>right</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395658):
<p>I even saw, on several occasions, and this is certainly not the first time,</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395659):
<p>people writing</p>

#### [ Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395666):
<p>it's not even about constructivism anymore, I'm just chaining UMPs all around</p>

#### [ Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395669):
<p>it's not about constructivism when people use UMP in category theory</p>

#### [ Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395670):
<p>because it's what it is</p>

#### [ Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395671):
<p>it's the UMP</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395672):
<p>"We want to prove X. Let's prove it by contradiction. So assume X is false. Now consider the following perfectly good proof of X. But X is false! Contradiction!</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395674):
<p>"</p>

#### [ Kenny Lau (Jun 01 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395713):
<p>if you are a lazy person who only knows proof by contradiction it's a very natural first step</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395720):
<p>For things like timed tests it's a good strategy</p>

#### [ Kenny Lau (Jun 01 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395723):
<p>I find UMPs easier</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395726):
<p>where you just write and write until you get the answer</p>

#### [ Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395732):
<p>I just use 100 UMPs until I get the answer</p>

#### [ Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395733):
<p>and I always get it</p>

#### [ Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395734):
<p>because it's universal</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395736):
<p>Also resolution theorem proving is based on this idea</p>

#### [ Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395745):
<p>solve_by_elim ain't</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395748):
<p>where you whittle down a counterexample until it is impossible</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395790):
<p>but the resulting proof looks ugly I think</p>

#### [ Kenny Lau (Jun 01 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395800):
<p>(whatever)</p>

#### [ Mario Carneiro (Jun 01 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395801):
<p>when you want that "polished" look it's best to avoid proof by contradiction</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395980):
<p>My goal is <code>has_le.le (coe 0) (has_div.div 71 100)</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395983):
<p>and if I try and unfold either <code>has_le.le</code> or <code>coe</code> I get a deterministic timeout</p>

#### [ Kenny Lau (Jun 01 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396024):
<p>so don't unfold them?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396038):
<p>norm_num times out too</p>

#### [ Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396081):
<p>did you use <code>div</code> lemmas?</p>

#### [ Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396082):
<p><code>div_nonneg</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396084):
<p>oh I need to feed those in</p>

#### [ Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396085):
<p>you just need that one</p>

#### [ Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396087):
<p>the rest should be <code>norm_num</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396088):
<p>do I put it in the context?</p>

#### [ Kenny Lau (Jun 01 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396096):
<p>no, you apply it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396146):
<p>you want me to actually prove it by hand??</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396149):
<p>what is this -- the 1980s?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396152):
<p>we have norm_num!</p>

#### [ Kenny Lau (Jun 01 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396163):
<p>my math teacher at high school would tell the story of people using calculators to verify that 5 x 0 = 0</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396207):
<p><code>refine div_nonneg _ _,</code> times out</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396209):
<p>everything times out</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396211):
<p>my goal is corrupted</p>

#### [ Kenny Lau (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396215):
<p>code</p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396229):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">s</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="mi">71</span><span class="bp">/</span><span class="mi">100</span>

<span class="kn">theorem</span> <span class="n">sQ</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">71</span><span class="bp">/</span><span class="mi">100</span><span class="o">:</span><span class="n">ℚ</span><span class="o">):</span><span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">s</span><span class="bp">;</span><span class="n">norm_num</span>

<span class="c1">--set_option pp.all true</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">floor</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">sQ</span><span class="o">,</span><span class="n">rat</span><span class="bp">.</span><span class="n">cast_floor</span><span class="o">],</span>
<span class="n">apply</span> <span class="o">(</span><span class="n">floor_of_bounds</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
<span class="n">split</span><span class="o">,</span>
<span class="o">{</span> <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">100</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span><span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span>
  <span class="n">refine</span> <span class="n">div_nonneg</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="c1">--unfold has_le.le,</span>
<span class="c1">--show 0 ≤ 71 / 100,</span>

    <span class="n">sorry</span><span class="o">},</span>
<span class="o">{</span><span class="n">sorry</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 01 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396231):
<p>all this fuss about <code>0.71</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396232):
<p>I should have been in bed hours ago</p>

#### [ Kevin Buzzard (Jun 01 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396276):
<p>I'm glad none of my students spent 2 hours on this bit</p>

#### [ Kevin Buzzard (Jun 01 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396283):
<p>it was only a 2 hour exam</p>

#### [ Kenny Lau (Jun 01 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396337):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">floor</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="n">floor_of_bounds</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">unfold</span> <span class="n">s</span><span class="o">,</span> <span class="n">apply</span> <span class="n">div_nonneg</span><span class="bp">;</span> <span class="n">norm_num</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">unfold</span> <span class="n">s</span><span class="o">,</span> <span class="n">rw</span> <span class="n">div_lt_iff</span><span class="bp">;</span> <span class="n">norm_num</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Jun 01 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396449):
<div class="codehilite"><pre><span></span>example : floor s = 0 := by rw [← floor_of_bounds, s, int.cast_zero]; norm_num
</pre></div>

#### [ Kevin Buzzard (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396503):
<p>So using rat.cast_floor was a bad idea</p>

#### [ Kevin Buzzard (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396509):
<p>Even though my instinct is to get out of R ASAP</p>

#### [ Kenny Lau (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396510):
<p>there's a box</p>

#### [ Mario Carneiro (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396511):
<p>I meant to use that if you were planning on kernel computation</p>

#### [ Kenny Lau (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396512):
<p>think out of it</p>

#### [ Kenny Lau (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396513):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> i couldn't get the kernel to compute it</p>

#### [ Mario Carneiro (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396517):
<p>Actually <code>71</code> might be too big for the kernel...</p>

#### [ Kenny Lau (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396521):
<p>lol</p>

#### [ Kenny Lau (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396524):
<p>71 is too big for the kernel</p>

#### [ Kenny Lau (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396526):
<p><a href="https://tio.run/##K6gsycjPM/7/v6AoM69Ew9xQS8vcUPP/fwA" target="_blank" title="https://tio.run/##K6gsycjPM/7/v6AoM69Ew9xQS8vcUPP/fwA">https://tio.run/##K6gsycjPM/7/v6AoM69Ew9xQS8vcUPP/fwA</a></p>

#### [ Mario Carneiro (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396531):
<p>that's VM computation though</p>

#### [ Mario Carneiro (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396534):
<p>or would be if it were lean</p>

#### [ Mario Carneiro (Jun 01 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396578):
<p>python doesn't have to bother proving it is correct</p>

#### [ Mario Carneiro (Jun 01 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396582):
<p>and it also doesn't use a braindead representation</p>

#### [ Kevin Buzzard (Jun 01 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127397530):
<p>Kenny I did it:</p>

#### [ Kevin Buzzard (Jun 01 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127397531):
<p><code>theorem no_eights (n : ℕ) : decimal.expansion s (by unfold s;norm_num) n ≠ 8 := ...</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127397532):
<p><code>0.71</code> has no 8's in its decimal expansion</p>

#### [ Johan Commelin (Jun 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402805):
<blockquote>
<p>Actually <code>71</code> might be too big for the kernel...</p>
</blockquote>
<p>Would it help if we compute in base <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>r</mi></mrow><annotation encoding="application/x-tex">r</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">r</span></span></span></span> (with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>r</mi><mo>=</mo><mn>1</mn><mn>0</mn></mrow><annotation encoding="application/x-tex">r = 10</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.64444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mrel">=</span><span class="mord mathrm">1</span><span class="mord mathrm">0</span></span></span></span> or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>1</mn><mn>6</mn></mrow><annotation encoding="application/x-tex">16</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.64444em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">1</span><span class="mord mathrm">6</span></span></span></span>)? Then we could have a lookup-table of simp-lemmas. And we could implement stuff like <a href="https://en.wikipedia.org/wiki/Multiplication_algorithm#Karatsuba_multiplication" target="_blank" title="https://en.wikipedia.org/wiki/Multiplication_algorithm#Karatsuba_multiplication">https://en.wikipedia.org/wiki/Multiplication_algorithm#Karatsuba_multiplication</a></p>

#### [ Johan Commelin (Jun 01 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402818):
<p>And for specific computations, of course a specific base could be used, with pre-computed lookup-tables.</p>

#### [ Johan Commelin (Jun 01 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402890):
<p>Ok, to be clear: I am not suggesting that we change the implementation of <code>nat</code>. But I am suggesting that we have a parallel implementation specifically for computations in base <code>r</code>. And an isomorphism between the implementations.</p>

#### [ Johan Commelin (Jun 01 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402899):
<p>But maybe this means that we also need a parallel implementation of <code>int</code> and <code>rat</code>. And then I'm not sure if I would want to go down that rabbit-hole</p>

#### [ Mario Carneiro (Jun 01 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403216):
<p>Yes, it would help to work in base r. The really important part is that r should be greater than 1</p>

#### [ Mario Carneiro (Jun 01 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403221):
<p>The <code>num</code> type is used to address these issues, by implementing binary natural numbers instead of the default <code>nat</code> which is unary</p>

#### [ Mario Carneiro (Jun 01 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403272):
<p><code>znum</code> is the parallel implementation of <code>int</code>; there is no qnum type (yet)</p>

#### [ Johan Commelin (Jun 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403365):
<p>Hmm, ok. So then you would need a <code>qnum</code> and afterwards an <code>rnum</code> and a <code>cnum</code>...</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403409):
<p>well, those last two don't matter anyway</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403415):
<p>or at least, they would be significantly different from the <code>real</code> type you know and love</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403421):
<p>because computable reals are not like regular reals</p>

#### [ Johan Commelin (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403424):
<p>I am not suggesting that <code>rnum</code> be computable</p>

#### [ Johan Commelin (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403431):
<p>But maybe then it isn't useful either (-;</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403438):
<p>That's the whole point</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403446):
<p>The idea is to have a "programming numbers" type which is proven isomorphic to the abstract version</p>

#### [ Johan Commelin (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403450):
<p>Right</p>

#### [ Johan Commelin (Jun 01 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403501):
<p>But for a speed-up of Kevin's question, you would like to convert to <code>num</code> at some point. Is that correct?</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403502):
<p>Unfortunately, you currently have to make a decision between VM-optimized and kernel-optimized data types</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403511):
<p>so there are valid reasons to keep both around</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403555):
<p><code>nat</code> is actually the faster one in the VM, because lean replaces it with GMP bignums or C ints if small enough</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403558):
<p>while <code>num</code> is just a regular inductive type so it's implemented as a linked list of digits</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403607):
<p>If you want to prove theorems by <code>rfl</code> or <code>dec_trivial</code>, you need to use kernel-efficient data types or else keep the numbers very small</p>

#### [ Johan Commelin (Jun 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403619):
<p>Yes, I understand. So, are things like Karatsuba or Tom-Cook implemented for <code>num</code>?</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403621):
<p>If you are using <code>norm_num</code> or <code>simp</code>, you want VM-efficient data types</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403622):
<p>No, the numbers have not got that big (yet)</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403662):
<p>That requires significant size before it pays off</p>

#### [ Johan Commelin (Jun 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403665):
<p>I guess another problem is that for big numbers the conversion between <code>nat</code> and <code>num</code> will become the bottle-neck. Right?</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403666):
<p>You can't do anything that even mentions <code>nat</code> in the kernel with big numbers</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403686):
<p>you can't even accept nat input and convert to num because the parser produces some <code>bit0 (bit0 ... 1)</code> term to pass to your function, and the kernel evaluates it before getting to your function</p>

#### [ Johan Commelin (Jun 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403713):
<p>O.o (-;</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403716):
<p>So this means that any conversion from <code>nat</code> has to be done in the VM. The good news is that this can be done efficiently and still be verified</p>

#### [ Johan Commelin (Jun 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403722):
<p>Ok, I don't follow this anymore... but I think it means that I can relax (-;</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403724):
<p>You just have theorems saying <code>bit0 \u x = \u bit0 x</code> where <code>\u : nat -&gt; num</code></p>

#### [ Johan Commelin (Jun 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403725):
<p>I thought that the VM cheated... and you would lose verification</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403754):
<p>and you have a tactic (running in the VM) that selectively chooses to apply this theorem</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403766):
<p>by looking at the <em>term</em> in the goal</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403771):
<p>with regular lean functions you can only look at the value that is given, but tactics can decompose the expr that represents the value</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403779):
<p>so something like <code>bit0 (bit0 ... 1)</code> has reasonable size as a term but not as a value</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403816):
<p>and you can apply log(n) <code>bit0 \u x = \u bit0 x</code> theorems to get it down to a theorem just about <code>num</code></p>

#### [ Mario Carneiro (Jun 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403820):
<p>and then you prove by <code>rfl</code> or whatever</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403821):
<p>and the kernel never has to evaluate big nats</p>

#### [ Johan Commelin (Jun 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403881):
<p>Ok, I see the strategy.</p>

#### [ Johan Commelin (Jun 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403891):
<p>I think Kevin is going to like that if at some point he wants to do some modular form stuff...</p>

#### [ Johan Commelin (Jun 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403897):
<p>Because their coefficients explode</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403938):
<p>So <code>norm_num</code> is also working in binary, I guess</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403940):
<p>it produces a theorem that is longer for larger numbers though</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403944):
<p>while a kernel proof is always just <code>rfl</code></p>

#### [ Mario Carneiro (Jun 01 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403990):
<p>For the most part, kernel computation is discouraged because it's not particularly optimized for that</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404013):
<p>But I think it's amusing that in dependent type theory you can write down a very short proof of almost anything</p>

#### [ Johan Commelin (Jun 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404066):
<p>What do you mean with that last statement?</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404068):
<p>for example, I can write a program that enumerates proofs in ZFC or whatever, and then if there is a proof of RH with fewer than 2^2^2^2^2^2^2^2^2^2^2 symbols, then I can prove it by <code>rfl</code></p>

#### [ Johan Commelin (Jun 01 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404077):
<p>Right, but that proof will require a lot of prerequisite work</p>

#### [ Johan Commelin (Jun 01 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404078):
<p>(Which I consider part of the proof.)</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404123):
<p>The only work that needs to be done is the setup, stating the problem</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404127):
<p>the "hard part" is completely absent from the accounting, except in the length bound</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404134):
<p>but I can write functions that grow ridiculously fast in DTT so that's not saying much</p>

#### [ Johan Commelin (Jun 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404140):
<p>Ok, so we can prove that RH doesn't have a short proof.</p>

#### [ Johan Commelin (Jun 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404141):
<p>And neither has Fermat's Last Theorem</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404183):
<p>Okay, fermat is a good example, since we know that one is true</p>

#### [ Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404184):
<p>For otherwise they would already have been in mathlib with a <code>rfl</code> proof.</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404190):
<p>I can prove Fermat's last theorem by <code>rfl</code></p>

#### [ Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404193):
<p>I would love to see that done.</p>

#### [ Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404195):
<p>The statement is already there</p>

#### [ Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404196):
<p>And that is all the setup you need.</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404211):
<p>I just write a <code>bool</code> function that checks the first bazillion proofs and returns <code>tt</code> if one works, and assert by <code>rfl</code> that it is <code>tt</code></p>

#### [ Johan Commelin (Jun 01 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404258):
<p>Right. And of course Lean will never finish running.</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404270):
<p>that proof checks if and only if there is a short enough proof of FLT, and since we know there is, that means I have a short proof</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404282):
<p>Of course the problem with this kind of analysis is that lean will run (almost) forever on such a proof</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404288):
<p>But it seems to be some kind of deficiency in DTT, that the length of a proof is no longer a suitable measure of the hardness of the proof</p>

#### [ Johan Commelin (Jun 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404323):
<p>Yes, and that's why we still dont have FLT in mathlib (-;</p>

#### [ Johan Commelin (Jun 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404333):
<p>No, but compile-time is still a good measure</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404340):
<p>Yes. Or number of proof steps including definitional reductions</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404351):
<p>This doesn't come up in ZFC since there's no definitional reduction, what you see is what you get</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404418):
<p>anyway, this "feature" of DTT should be thought of as abuse of lean, so don't be surprised if it starts to sweat</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404428):
<p>when you try to <code>#reduce 71 / 100</code></p>

#### [ Johan Commelin (Jun 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404477):
<p>Sure, and in fact, we don't even know what the value of "bazillion" is for your <code>bool</code> function. We only have a very clear suggestion that it is finite.</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404491):
<p>I think there are some pretty reasonable upper bounds based on physical considerations</p>

#### [ Mario Carneiro (Jun 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404496):
<p>i.e. the proof appears to fit in the universe, so it's shorter than Graham's number</p>

#### [ Johan Commelin (Jun 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404502):
<p>ok, fair enough</p>

#### [ Johan Commelin (Jun 01 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127411378):
<p>It seems that <code>real</code> is not an instance of <code>has_pow</code>. Should I add it, or is there some computability reason for not doing that?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414076):
<p>I think the definition of <code>has_pow</code> is post-real so it might just be that nobody used them seriously enough since. As you can see, I've come back to the reals recently, and I am always interested in making them "undergraduate-friendly" so I would have run into this sooner or later.</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414077):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> -- where do these definitions go? Mathlib? My own Xena library? (I'm writing a library for stuff my UG mathematicians might want or need and which is not in mathlib -- can you envisage there being good reasons for such a library?)</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">is_upper_bound</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">S</span><span class="o">,</span> <span class="n">s</span> <span class="bp">≤</span> <span class="n">x</span>
<span class="kn">definition</span> <span class="n">is_bounded_above</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_upper_bound</span> <span class="n">x</span> <span class="n">S</span>
<span class="kn">definition</span> <span class="n">is_LUB</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">is_upper_bound</span> <span class="n">x</span> <span class="n">S</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">is_upper_bound</span> <span class="n">y</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span>

<span class="kn">definition</span> <span class="n">has_LUB</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_LUB</span> <span class="n">x</span> <span class="n">S</span>
</pre></div>

#### [ Johan Commelin (Jun 01 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414310):
<p>Hmm, I guess to do has_pow properly, we should define <code>x^r</code> for <code>x r : real</code>. And then all of a sudden you have to work.</p>

#### [ Johan Commelin (Jun 01 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414359):
<p>Or can we have multiple instances, depending on whether <code>r</code> has type <code>nat</code> or <code>int</code> or <code>rat</code> or <code>real</code>.</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414447):
<p>this is exactly the problem with pow</p>

#### [ Johan Commelin (Jun 01 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414459):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Isn't <code>Sup</code> already on line 316 of data.real.basic?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414460):
<p>Chris Hughes wrote exp : C -&gt; C but it's still not in mathlib</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414712):
<p>That's CS sup</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414713):
<p>sup(S)+sup(T) = sup(S+T) is not true for that sup</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414714):
<p>let S have one element and let T be empty</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414715):
<p>(deleted)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414716):
<p>it returns 37 if the set has no sup</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414717):
<p>This is philosophy not mathematics</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414723):
<p>but if you're going to define sup globally</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414776):
<p>then it should be taking values in -infty + R + infty</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414781):
<p>not just spewing out 37s when it's stuck</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414795):
<p>You see how my predicate solves this problem?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414799):
<p>I can say "if a is the sup of S and b is the sup of T then a + b is the sup of S + T</p>

#### [ Johan Commelin (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414804):
<p>Ok, so I read too quickly (-;</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414807):
<p>My question is how to formalize that statement in mathlib</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414813):
<p>and my predicates make it look nice and easy</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414815):
<p>whereas I can't quite do it with what we have</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414856):
<p>however I am unclear about whether "what I want as someone who wants to formulate elementary lemmas about sup"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414862):
<p>has anything to do with "what should be in mathlib"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414863):
<p>I am very unclear about what the boundaries of mathlib are</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414865):
<p>Look, watch this:</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414867):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> -- should I put schemes in mathlib? Let me know. I don't care either way but you never answer</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414871):
<p>he never answers</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414878):
<p>I think he reads the question, thinks "hmm, I don't know offhand, I should look at the repo, oh look it's 7000 lines of sometimes poorly-written code"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414879):
<p>"this will need some thought"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414886):
<p>I'll try another approach</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414954):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think definitions of high-level mathematical objects and statements of extremely technical theorems are extremely important things to have in Lean and I will be making quite a few of these in the future. Do you want them in mathlib or do you feel that they are beyond mathlib's remit? I hope I have conveyed in the past how I feel about this matter (namely that I think that there are many people whose interest would be sparked by a small database of complex objects built in Lean)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414996):
<p>I believe <span class="user-mention" data-user-id="110087">@Scott Morrison</span> thinks they should be in mathlib</p>

#### [ Johannes Hölzl (Jun 01 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127416299):
<p>least upper bounds etc as predicates are already there: <a href="https://github.com/leanprover/mathlib/blob/master/order/bounds.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/bounds.lean">https://github.com/leanprover/mathlib/blob/master/order/bounds.lean</a></p>

#### [ Sebastien Gouezel (Jun 01 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127417740):
<p>You can also have a look at <a href="https://github.com/leanprover/mathlib/blob/master/order/conditionally_complete_lattice.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/conditionally_complete_lattice.lean">https://github.com/leanprover/mathlib/blob/master/order/conditionally_complete_lattice.lean</a></p>

#### [ Mario Carneiro (Jun 01 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422500):
<blockquote>
<p>-- should I put schemes in mathlib? Let me know. I don't care either way but you never answer</p>
</blockquote>
<p>RIght now? No. As Patrick has mentioned before, the scheme code is huge and requires major refactoring to go into mathlib, much like some other planned additions, e.g. Scott's category theory stuff (and he's made some progress on this last I checked). As it currently exists, it is written as a "race to the finish" which gets the job done without worrying about looking good while doing it, whereas I need "polished" code to go into mathlib. It's like the difference between research notes and a journal article or textbook. This process of bringing schemes in will take a lot of both of our time and right now I think you have bigger plans, so I would hold off on attempting this for the present.</p>

#### [ Mario Carneiro (Jun 01 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422552):
<blockquote>
<p>I think definitions of high-level mathematical objects and statements of extremely technical theorems are extremely important things to have in Lean and I will be making quite a few of these in the future. Do you want them in mathlib or do you feel that they are beyond mathlib's remit?</p>
</blockquote>
<p>The "level" of the definition is not a problem, it can be as advanced as you like. But it must also be good lean code, that's my main concern.</p>

#### [ Mario Carneiro (Jun 01 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422727):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> There is a definition of has_pow on real, because it is a field. You can use <code>a^n</code> where <code>n : nat</code> and <code>a : real</code></p>

#### [ Mario Carneiro (Jun 01 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422826):
<p>Actually <code>a^n</code> where <code>n : int</code> is not quite there, since the instance that exists is for <code>group</code>s and <code>real</code> isn't a (multiplicative) group. Maybe there should be another definition for <code>division_ring</code>s that sets <code>0^-n = 0</code>?</p>

#### [ Mario Carneiro (Jun 01 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422964):
<p>You could use the (tiny) library of proper division in mathlib though: <code>units.mk0 a h</code> where <code>a : real</code> and <code>h : a != 0</code> is an element of <code>units real</code>, which is a group, so you can raise it to an integer power and coerce back to real</p>

#### [ Johan Commelin (Jun 01 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127425169):
<p>Ok, thanks. I will take a look at those functions.</p>

#### [ Johan Commelin (Jun 01 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127425350):
<p>Is it now easy to have the integers \cup infty? How about <code>int \cup -\infty</code> ? Including the order and addition on them. (Otherwise I could just take <code>option int</code>.</p>

#### [ Mario Carneiro (Jun 01 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127425837):
<p>Yes, <code>with_top int</code> has an addition operation and an order, and is defeq to <code>option int</code></p>

#### [ Johan Commelin (Jun 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426287):
<p>Hmm, but there is no <code>with_bot</code> for semigroups. I want to define a function <code>f : nat \to (with_top int)</code>, and then another function <code>nat \to real := \lam n, b^(- f(n))</code>, where <code>b</code> is some fixed real number.</p>

#### [ Johan Commelin (Jun 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426324):
<p>So then I need to extend <code>-</code> to <code>- : with_top int \to with_bot int</code>. And I need to explain to <code>has_pow real</code> that <code>b^(-infty) = 0</code>.</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426376):
<p>eww</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426384):
<p>that's a bit specialized</p>

#### [ Johan Commelin (Jun 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426404):
<p>Ok, <code>f(n) = infty \iff n = 0</code>.</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426420):
<p>You can define <code>-</code> as <code>option.map (\lam x, -x)</code>, and <code>b^o</code> where <code>o : with_bot int</code> by cases</p>

#### [ Johan Commelin (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426421):
<p>The other option is that I just use if-then-else everywhere... but I don't really like that either...</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426432):
<p>no if-then</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426437):
<p>it's an option, use cases</p>

#### [ Johan Commelin (Jun 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426457):
<p>Right. (I meant avoiding <code>option</code> and just do <code>dite (n = 0)</code> in all the definitions.</p>

#### [ Johan Commelin (Jun 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426525):
<p>(This stuff shows up everywhere in nonarchimedean valuations.)</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426532):
<p>what <code>n = 0</code> are you talking about?</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426548):
<p>you said <code>f</code> returns an option</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426554):
<p>well, a <code>with_top</code></p>

#### [ Johan Commelin (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426559):
<p>Yes, but I could also define <code>f</code> on <code>pnat</code>, and <code>g</code> with a <code>dite</code>.</p>

#### [ Johan Commelin (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426561):
<p>Right?</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426610):
<p>Oh, I misunderstood your iff statement</p>

#### [ Johan Commelin (Jun 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426662):
<p>But I like your approach. I'll try to implement it when I'm back at Lean. (And should I just clone and dualise the <code>with_top</code> stuff to <code>with_bot</code> for semigroups?</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426664):
<p>It's already there</p>

#### [ Johan Commelin (Jun 01 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426731):
<p>Hmm, for <code>with_bot</code> I only see instances for partial orders and lattices. Not for semigroups.</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426754):
<p>There is <code>with_zero</code> also, there are lots of ways to construe the added element in all the structures</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426835):
<p>Oh, I see, <code>with_top</code> and <code>with_bot</code> are actually the same as add_semigroups</p>

#### [ Johan Commelin (Jun 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426845):
<p>Ok, so maybe you can also give a hint on how to define <code>f</code>. It is the p-adic valuation (where p is a prime). So <code>f(n)</code> is the maximal <code>e : nat</code> such that <code>p^e</code> divides <code>n</code>.</p>

#### [ Johan Commelin (Jun 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426852):
<blockquote>
<p>Oh, I see, <code>with_top</code> and <code>with_bot</code> are actually the same as add_semigroups</p>
</blockquote>
<p>Yes, but not as ordered add_semigroups.</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426863):
<p>Yeah, I'll work on that</p>

#### [ Reid Barton (Jun 01 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426978):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> see <a href="https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea" target="_blank" title="https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea">https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea</a></p>

#### [ Mario Carneiro (Jun 01 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426979):
<p>First, I would want a "prime count" function that takes a nat and finds the appropriate power of p. It is defined arbitrarily at zero, but for concreteness that means <code>f 0 = 0</code></p>

#### [ Reid Barton (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427030):
<p>I gave that to Kevin earlier and I think he has improved it some in the Fibonacci project</p>

#### [ Johan Commelin (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427033):
<p>Yes, or f 0 = infty. And then you would be done.</p>

#### [ Johan Commelin (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427047):
<p>Reid, thanks. I'll take a look.</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427048):
<p>Then the valuation function is defined by cases on <code>n</code></p>

#### [ Mario Carneiro (Jun 01 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427138):
<p>actually, I just checked what I did in metamath for this and I used with_top as well. So past me seems to think that's a better idea</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427163):
<p>I'm a bit worried about having to coerce all the time though</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428342):
<p>I don't think I ever got the code completely working in the Fibonacci project, there was perhaps one sorry I never got rid of</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428438):
<blockquote>
<p>As it currently exists, it is written as a "race to the finish" which gets the job done without worrying about looking good while doing it, whereas I need "polished" code to go into mathlib. It's like the difference between research notes and a journal article or textbook. This process of bringing schemes in will take a lot of both of our time and right now I think you have bigger plans, so I would hold off on attempting this for the present.</p>
</blockquote>
<p>Yes, this is exactly how I wrote it, and I put very little thought into how to make structures because I didn't really know how to make structures at the time. Here are my more long-term thoughts on these matters:</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428457):
<p>I'm going to do perfectoid spaces because I think it would be funny to do them</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428470):
<p>Some scheme stuff we will need e.g. sheaves</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428479):
<p>but I was thinking about re-doing it</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428485):
<p>doing it all for a second time in a perfectoid spaces directory</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428548):
<p>and this time doing it better and checking with people like Mario along the way as to whether the structures looked sensible</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428559):
<p>I understand now much better what I can do well and what I do badly</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428567):
<p>and especially what I do so badly that it will take a lot of time to fix</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428580):
<p>I make no apologies for the race to the finish with schemes -- this was simply a test to see if it could be done, and it could be done</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428624):
<p>I thnk that's a good plan</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428673):
<p>In the long term with schemes, I propose doing perfectoid spaces, seeing the parts which are common to both theories, using this commonality as an argument for inclusion in mathlib, and then spending some time writing these parts of the code properly</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428688):
<p>so for example we will need sheaves of types at some point</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428693):
<p>and when we need them in the perfectoid theory I will revisit what I did for schemes</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428694):
<p>The second time around you will have a <em>much</em> better appreciation for the subtleties and design questions and can do it right</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428705):
<p>(in fact we did these already and I even have a suggested definition from Mario somewhere in my starred messages)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428708):
<p>yes -- second time round much better</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428729):
<p>Not to mention you are a better lean programmer now than last month (and the month before that etc)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428731):
<p>so second time round I think "this is important, I knocked up a definition in 10 minutes when I was doing schemes, here are the problems I had with it, let's fix those problems now and aim for mathlib"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428737):
<p>"and write a proper interface while we're here"</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428749):
<p>so it's partly some random repo with random bits of people's papers formalised</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428789):
<p>and then some directory called "mathlib_someday"</p>

#### [ Mario Carneiro (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428799):
<p>When I look at <code>dioph.lean</code> I am ashamed of myself, I would write that so much better now and it's been only a year</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428805):
<p>where we put files where someone has actually made an effort to make the file mathlib-worthy</p>

#### [ Kevin Buzzard (Jun 01 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428825):
<p>You're absolutely right that I get better every month. When I started schemes I had no idea how to use type class inference so never used it -- I would just supply all the missing proofs myself.</p>

#### [ Scott Morrison (Jun 02 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127440781):
<p>This all sounds like a great plan --- schemes absolutely deserve to be in mathlib (what would be the point of mathlib if we weren't aiming for it to cover the basic essentials?), and at the same time we should try to make sure code going into mathlib is good (not perfect, though).</p>

#### [ Scott Morrison (Jun 02 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127440829):
<p>My categories code (getting there! :-) is still abysmal, probably, and I appreciate it's going to be lots of work to get it into mathlib. :-)</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482657):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">archimedean</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">abs_nonneg</span>
<span class="c1">-- abs_nonneg : ∀ {α : Type u_1}</span>
<span class="c1">--   [_inst_1 : decidable_linear_ordered_comm_group α] (a : α),</span>
<span class="c1">--   abs a ≥ 0</span>

<span class="kn">theorem</span> <span class="n">abs_nonneg&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">floor_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_linear_ordered_comm_group</span> <span class="n">α</span><span class="o">]</span>
<span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">r</span> <span class="bp">≥</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">abs_nonneg</span> <span class="n">r</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Kevin Buzzard (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482660):
<p>My understanding of something Reid said a few days ago about the reals</p>

#### [ Kenny Lau (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482661):
<p>diamond of death?</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482664):
<p>was that I shouldn't be proving things about the reals</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482670):
<p>I should just demand I'm a complete totally ordered field and deduce everything from that</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482671):
<p>yeah, this is a diamond problem</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482672):
<p>but the real problem was decidability I think</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482674):
<p>you have two conflicting group structures on A</p>

#### [ Kenny Lau (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482675):
<p>and order structure?</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482676):
<p>I want to use this abs &gt;= 0 lemma</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482721):
<p>a floor_ring has an order</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482723):
<p>Why do you have two typeclasses here? that's the question</p>

#### [ Reid Barton (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482728):
<p>In this case I think you don't need <code>decidable_linear_ordered_comm_group</code></p>

#### [ Mario Carneiro (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482730):
<p>you do, to state <code>abs</code></p>

#### [ Mario Carneiro (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482731):
<p>but you don't need the floor_ring</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482878):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">abs_expansion</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_linear_ordered_comm_group</span> <span class="n">α</span><span class="o">]:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
  <span class="n">expansion</span> <span class="o">(</span><span class="n">abs</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">abs_nonneg</span> <span class="n">r</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Jun 03 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482879):
<p>that's what the problem becomes if I remove the floor_ring</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482884):
<p>what's <code>expansion</code></p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482885):
<div class="codehilite"><pre><span></span>type mismatch at application
  expansion (abs r) _
term
  abs_nonneg r
has type
  @ge α
    (@preorder.to_has_le α
       (@partial_order.to_preorder α
          (@ordered_comm_group.to_partial_order α
             (@decidable_linear_ordered_comm_group.to_ordered_comm_group α _inst_3))))
    (@abs α _inst_3 r)
    0
but is expected to have type
  @ge α
    (@preorder.to_has_le α
       (@partial_order.to_preorder α
          (@ordered_comm_monoid.to_partial_order α
             (@ordered_cancel_comm_monoid.to_ordered_comm_monoid α
                (@ordered_semiring.to_ordered_cancel_comm_monoid α
                   (@ordered_ring.to_ordered_semiring α
                      (@linear_ordered_ring.to_ordered_ring α (@floor_ring.to_linear_ordered_ring α _inst_2))))))))
    (@abs α _inst_3 r)
    0
</pre></div>

#### [ Mario Carneiro (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482887):
<p>Again, conflicting typeclasses</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482890):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">expansion</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">≥</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">to_nat</span> <span class="o">(</span><span class="n">floor</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">to_nat</span> <span class="o">(</span><span class="n">floor</span> <span class="o">(</span><span class="n">chomp</span> <span class="n">r</span> <span class="n">n</span><span class="o">))</span>
</pre></div>

#### [ Mario Carneiro (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482892):
<p><code>inst_3</code> in one, <code>inst_2</code> in the other</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482895):
<p>But it's just a decidability issue</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482933):
<p>no it's a conflicting typeclasses issue</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482936):
<p>I just want to "switch decidability on"</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482938):
<p>I assume you don't care about classical?</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482940):
<p>right</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482941):
<p>just <code>local instance decidable_prop</code></p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482942):
<p>This is stuff for mathematicians</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483004):
<p>Maybe you should just do this over <code>\R</code> instead of <code>A</code></p>

#### [ Mario Carneiro (Jun 03 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483006):
<p>or else use the noncomputable floor instance for archimedean <code>A</code></p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483010):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">floor_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">add_comm_group</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">floor_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">linear_order</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kevin Buzzard (Jun 03 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483116):
<p>I am a complete idiot</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483117):
<p>I should just be proving a junk theorem</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483158):
<p>I was defining decimal expansions of real numbers</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483159):
<p>and being fussy about issues with negative numbers</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483168):
<p>I should just let the function return some random result if the input is negative and then stop fussing</p>

#### [ Kenny Lau (Jun 03 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483214):
<p>57</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483216):
<p>I can't believe I'm going to prove a junk theorem</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483218):
<p>I feel dirty</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483233):
<p>This is the problem</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483234):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">expansion</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">≥</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">to_nat</span> <span class="o">(</span><span class="n">floor</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">to_nat</span> <span class="o">(</span><span class="n">floor</span> <span class="o">(</span><span class="n">chomp</span> <span class="n">r</span> <span class="n">n</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Jun 03 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483237):
<p>I just have to drop <code>H</code></p>

#### [ Mario Carneiro (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483279):
<p>It's not even used</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483280):
<p>and coerce a negative integer into nat</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483283):
<p>that's not the point Mario</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483285):
<p>it's all part of the mathematician's promise</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483288):
<p>That goes in theorems, not definitions</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483289):
<p>we don't quite model things in the same way</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483298):
<p>I have never seen a mathematician write a function that has an additional proof argument</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483303):
<p>I think they would have a hard time even understanding what that means</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483304):
<blockquote>
<p>It's not even used</p>
</blockquote>
<p>it should be there on moral grounds</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483346):
<p>there should be some tactic bringing it along</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483349):
<p>"mathematicians promise that they will not run this programme on negative numbers"</p>

#### [ Kenny Lau (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483354):
<p>@kevin just treat it like how you treat <code>nat.sub</code></p>

#### [ Mario Carneiro (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483355):
<p>You could use <code>roption</code> for partial functions too</p>

#### [ Kenny Lau (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483356):
<p>"subtraction with a star"</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483399):
<p>alternatively, you could actually make sense of expansions of negative numbers</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483402):
<p>which of course makes perfect sense and generates p-adic numbers</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483404):
<p>or two's complement for the CS folks</p>

#### [ Kevin Buzzard (Jun 03 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483414):
<blockquote>
<p>It's not even used</p>
</blockquote>
<p>It's used in <code>int.to_nat</code></p>

#### [ Mario Carneiro (Jun 03 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483464):
<p>Yet more alternatively, don't define it as a function, have an existence theorem</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483466):
<p>the inverse to this is a lot easier to state</p>

#### [ Mario Carneiro (Jun 03 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483624):
<div class="codehilite"><pre><span></span>def expansion (r : α) (n : ℕ) : ℕ :=
⌊r * (10 ^ n : ℕ)⌋.nat_mod 10
</pre></div>

#### [ Mario Carneiro (Jun 03 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483636):
<p>I'm not sure why <code>n</code> is a nat here, there are both negative and positive exponent terms in the expansion</p>

#### [ Kevin Buzzard (Jun 03 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484618):
<blockquote>
<p>least upper bounds etc as predicates are already there: <a href="https://github.com/leanprover/mathlib/blob/master/order/bounds.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/bounds.lean">https://github.com/leanprover/mathlib/blob/master/order/bounds.lean</a></p>
</blockquote>
<p>I see that I did mine a different way around to you. I defined <code>is_LUB x S</code> and you <code>is_lub S x</code>. Is there a preference for yours over mine? I chose "x S" because I would say x before S ("x is a least upper bound for S")</p>

#### [ Mario Carneiro (Jun 03 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484680):
<p>yes, this allows you to view <code>is_lub S</code> as a predicate by currying</p>

#### [ Mario Carneiro (Jun 03 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484692):
<p>generally speaking, more "parameter" like things should come first</p>

#### [ Kevin Buzzard (Jun 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484745):
<p>I'm far more likely to be fixing S and trying various x's than I am to be fixing an x and seeing if it bounds any S's, this seems far more unlikely to occur in practice</p>

#### [ Mario Carneiro (Jun 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484944):
<p>that's why I said that</p>

#### [ Mario Carneiro (Jun 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484947):
<p><code>S</code> is the parameter, <code>x</code> is the variable</p>

#### [ Mario Carneiro (Jun 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484948):
<p>so <code>S</code> comes first</p>

#### [ Kevin Buzzard (Jun 03 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127503868):
<blockquote>
<p>that's why I said that</p>
</blockquote>
<p>I know, I was just translating you into maths</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518169):
<p>Hey <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518175):
<p>I was playing with sups</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518193):
<p>what do you think this is:</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518220):
<div class="codehilite"><pre><span></span><span class="bp">⟨λ</span> <span class="n">u</span> <span class="n">Hu</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">Hs</span><span class="o">,</span><span class="n">t</span><span class="o">,</span><span class="n">Ht</span><span class="o">,</span><span class="n">Hu</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">Hu</span> <span class="k">in</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">Hu</span><span class="bp">;</span><span class="n">exact</span> <span class="n">add_le_add</span> <span class="o">(</span><span class="n">HSb</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s</span> <span class="n">Hs</span><span class="o">)</span> <span class="o">(</span><span class="n">HTc</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span> <span class="n">Ht</span><span class="o">),</span>
 <span class="bp">λ</span> <span class="n">d</span> <span class="n">Hd</span><span class="o">,</span><span class="n">add_le_of_le_sub_right</span> <span class="err">$</span> <span class="n">HSb</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">d</span> <span class="bp">-</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">s</span> <span class="n">Hs</span><span class="o">,</span><span class="n">le_sub</span><span class="bp">.</span><span class="mi">1</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">s₁</span> <span class="n">Hs₁</span><span class="o">,</span><span class="n">HTc</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span> <span class="n">Ht</span><span class="o">,</span><span class="n">le_sub_left_of_add_le</span> <span class="err">$</span> <span class="n">Hd</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">s₁</span><span class="o">,</span><span class="n">Hs₁</span><span class="o">,</span><span class="n">t</span><span class="o">,</span><span class="n">Ht</span><span class="o">,</span><span class="n">rfl</span> <span class="c1">-- the proof</span>
   <span class="bp">⟩</span><span class="o">))</span> <span class="n">s</span> <span class="n">Hs</span><span class="o">))</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518224):
<p>my constructive proof?</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518226):
<p>right</p>

#### [ Kenny Lau (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518228):
<p>yay</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518236):
<p>here's an even better version</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518237):
<p>I wrote it twice</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518238):
<p>second time looked like this</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518240):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">lub_add&#39;&#39;</span> <span class="o">(</span><span class="n">S</span> <span class="n">T</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">HSb</span> <span class="o">:</span> <span class="n">is_lub</span> <span class="n">S</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">HTc</span> <span class="o">:</span> <span class="n">is_lub</span> <span class="n">T</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_lub</span> <span class="o">(</span><span class="n">S</span> <span class="bp">+</span> <span class="n">T</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">u</span> <span class="n">Hu</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">Hs</span><span class="o">,</span><span class="n">t</span><span class="o">,</span><span class="n">Ht</span><span class="o">,</span><span class="n">Hu</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">Hu</span> <span class="k">in</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">Hu</span><span class="bp">;</span><span class="n">exact</span> <span class="n">add_le_add</span> <span class="o">(</span><span class="n">HSb</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s</span> <span class="n">Hs</span><span class="o">)</span> <span class="o">(</span><span class="n">HTc</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span> <span class="n">Ht</span><span class="o">),</span>
<span class="bp">λ</span> <span class="n">d</span> <span class="n">Hd</span><span class="o">,</span><span class="n">add_le_of_le_sub_right</span> <span class="err">$</span> <span class="n">HSb</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">s</span> <span class="n">Hs</span><span class="o">,</span><span class="n">le_sub</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">HTc</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">t</span> <span class="n">Ht</span><span class="o">,</span><span class="n">le_sub_left_of_add_le</span> <span class="err">$</span> <span class="n">Hd</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">Hs</span><span class="o">,</span><span class="n">t</span><span class="o">,</span><span class="n">Ht</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span>
<span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518244):
<p>more dollar signs?</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518245):
<p><code>instance : has_add (set ℝ) := ⟨λ S T,{u | ∃ (s ∈ S) (t ∈ T), u = s + t}⟩</code></p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518291):
<p><code>import order.bounds </code></p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518294):
<p>and <code>analysis.real</code></p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518295):
<p>and it will run</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518298):
<p>I couldn't get that stupid triangle thing to work on the first line of the proof</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518300):
<p>the \t triangle that Patrick and I both dread</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518302):
<p>so I have to use rw;exact :-)</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518309):
<p>so that can be golfed a bit more</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518311):
<p>but the proof the other way I was extremely pleased with :-)</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518315):
<p>I formulated the theorem</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518316):
<p>I proved it in tactic mode</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518318):
<p>I then translated my tactic mode proof into term mode</p>

#### [ Kenny Lau (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518357):
<p>nice!</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518358):
<p>and then I started again and proved it in term mode</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518365):
<p>from scratch</p>

#### [ Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518370):
<p>looking at my old term mode proof for hints about which arithmetic functions to use :-)</p>

#### [ Kevin Buzzard (Jun 04 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518441):
<p>in that last proof line, Lean was somehow always "on the last term" -- I never had to fill in a hole with a non-zero number of characters to the right of it (other than the close bracket)</p>

#### [ Kevin Buzzard (Jun 04 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518446):
<p>Kenny if you had given me that answer I would have had a hard time marking it.</p>

#### [ Kevin Buzzard (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518485):
<p>I mean the lambda</p>

#### [ Kevin Buzzard (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518486):
<p>it's become unreadable, right?</p>

#### [ Kenny Lau (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518487):
<p>lol</p>

#### [ Kenny Lau (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518488):
<p>but you can verify it</p>

#### [ Kevin Buzzard (Jun 04 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518498):
<p>that is a very different thing from understanding it</p>


{% endraw %}
