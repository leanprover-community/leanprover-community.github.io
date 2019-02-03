---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78247categories.html
---

## Stream: [new members](index.html)
### Topic: [categories](78247categories.html)

---


{% raw %}
#### [ Edward Ayers (Aug 08 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131073671):
<p>I made a silly .lean file for mathematical category theory.<br>
<a href="https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681" target="_blank" title="https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681">https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681</a><br>
Two questions; <br>
- what is the best way to solve the lemmas with <code>sorry</code> in them?<br>
- doesn't the definition of <code>Cat</code> break the type universe hierarchy? And if so why doesn't lean care?</p>

#### [ Edward Ayers (Aug 08 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131074009):
<p>Also any comments on style / readability would be appreciated</p>

#### [ Kevin Buzzard (Aug 08 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131074344):
<p>Just to comment that fresh this week we've had a huge category theory PR accepted into mathlib: <a href="https://github.com/leanprover/mathlib/commit/9b1be732e122d371100b0df479ca000c2a3f73b0" target="_blank" title="https://github.com/leanprover/mathlib/commit/9b1be732e122d371100b0df479ca000c2a3f73b0">https://github.com/leanprover/mathlib/commit/9b1be732e122d371100b0df479ca000c2a3f73b0</a></p>

#### [ Edward Ayers (Aug 08 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131074686):
<p>ok thanks I can compare it to my code</p>

#### [ Scott Morrison (Aug 08 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131079511):
<p>Hi <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, sorry to disappoint, but that PR that was merged was only the first epsilon of the actual category theory library (just 3 files!) It's still a long way to go anything useful to you is there. :-)</p>

#### [ Scott Morrison (Aug 08 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131079519):
<p>There's a second PR waiting, if anyone feels like giving some comments.&lt;<a href="https://github.com/leanprover/mathlib/pull/239" target="_blank" title="https://github.com/leanprover/mathlib/pull/239">https://github.com/leanprover/mathlib/pull/239</a>&gt;.</p>

#### [ Patrick Massot (Aug 09 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131165293):
<blockquote>
<p>I made a silly .lean file for mathematical category theory.<br>
<a href="https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681" target="_blank" title="https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681">https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681</a></p>
</blockquote>
<p>Who keeps the record of all beginners who had category theory as their first idea of something to formalize?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131165597):
<p>If you want to add to the list of "stuff which it looks like a good idea to be the first thing to formalise" then you seem to be able to add basic number theory to that list. My students ended up in coercion hell going from nat to int to zmod n</p>

#### [ Reid Barton (Aug 09 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131169156):
<p>Heh, the first two things I tried to formalize were fibrations of categories (that went poorly) and FLT for n=4</p>

#### [ Kevin Buzzard (Aug 09 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131169279):
<p>At least FLT for n=4 is a statement about nat.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131169292):
<p>The proof might not stray too far from nat either</p>

#### [ Kevin Buzzard (Aug 09 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131169296):
<p>oh actually maybe it strays into int a fair bit...</p>

#### [ Reid Barton (Aug 09 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131169410):
<p>I managed to nearly avoid using int, I think, but it might have been better to use it more. Lots of annoying inequality side conditions to check when doing algebraic manipulations over nat</p>

#### [ Edward Ayers (Aug 09 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131170956):
<p>I chose cats because that's the area of maths I'm strongest at and because it forces me to use lots of dependent-type features</p>

#### [ Mario Carneiro (Aug 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131171043):
<p>I don't disagree that it's a logical choice when starting to play with a DTT prover, but it really is so common it's almost a joke</p>

#### [ Mario Carneiro (Aug 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131171049):
<p>I'm sure I've seen this happen at least 8 times</p>

#### [ Edward Ayers (Aug 09 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131171320):
<p>Another fun one is making <code>vec n</code> and matrices and so on.</p>

#### [ Mario Carneiro (Aug 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/131171614):
<p>Those might be in TPIL though</p>

#### [ David Michael Roberts (Oct 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135524085):
<p>So I would like to say that I have some category, and say that it has some object. It's not obvious how to even declare a variable of type <code>category</code>. What I would like to do is to define the type of terminal objects of a given category. In type theory I guess I would do something like the dependent type</p>
<p>C:category |- terminalObj(C): C.obj</p>
<p>where C.obj is the type of objects of C.</p>

#### [ David Michael Roberts (Oct 10 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135524246):
<p>(I should say I'm using <code>category_theory</code> in mathlib)</p>
<p>Then terminalObj(C) := Σ t: C.Obj Π_{x:C.Obj} Π_{f,g:Hom(x,t)} f = g</p>

#### [ Mario Carneiro (Oct 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135524331):
<p>In lean, we have <code>category A</code> as the type of categories where <code>A</code> is the type of objects. (That is, they are "partially unbundled" with the type of objects exposed.) Then you can define a structure <code>is_terminal (X : A) : Type</code> with fields for the unique map in, and the statement of uniqueness</p>

#### [ David Michael Roberts (Oct 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135527489):
<p>Ah, that makes sense. Particularly as Cat is fibred over Class by sending a category to its class of objects, so that it makes sense to talk of the dependent type A:Type |- category(A): Type.</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135527835):
<p>Yes, what you call fibration is what we call unbundling</p>

#### [ Scott Morrison (Oct 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135528430):
<p>Terminal objects (along with every other shape of (co)limit) are on the horizon. If you want to peek, and don't mind peeking at often-broken code, see the <code>working</code> branch of <a href="https://github.com/semorrison/lean-category-theory/tree/working/src/category_theory/limits" target="_blank" title="https://github.com/semorrison/lean-category-theory/tree/working/src/category_theory/limits">https://github.com/semorrison/lean-category-theory/tree/working/src/category_theory/limits</a>.</p>

#### [ Scott Morrison (Oct 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135528440):
<p>("working" here is as-in "I'm working on it", not "it is working"...)</p>

#### [ Mario Carneiro (Oct 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135528454):
<p>I think <code>wip</code> is less susceptible to misinterpretation</p>

#### [ Scott Morrison (Oct 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135528498):
<p>ok, I'll use that in future! thanks.</p>

#### [ David Michael Roberts (Oct 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/categories/near/135529320):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> thanks, I'll check it out</p>


{% endraw %}
