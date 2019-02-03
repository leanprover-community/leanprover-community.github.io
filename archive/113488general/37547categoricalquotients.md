---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37547categoricalquotients.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [categorical quotients](https://leanprover-community.github.io/archive/113488general/37547categoricalquotients.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870843):
<p>Is everyone ready for a new puzzle about how to formalise things mathematicians use without thinking about? :-)</p>

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870844):
<p>I would like to define a notion of a "categorical quotient".</p>

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870846):
<p>Recall that a quotient of a type <code>X</code> by a relation <code>R</code> is a type <code>Y</code>, which is pretty much useless, _except_ that we can construct functions <code>Y -&gt; Z</code> by giving two pieces of data:</p>

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870847):
<p>1. a function <code>f : X -&gt; Z</code>, and<br>
2. a proof that <code>R x x' -&gt; (f x = f x')</code>.</p>

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870848):
<p>I want instead a categorical quotient of a type <code>X</code> by a relation <code>R</code>, let's call it <code>Q</code> which is useless except that we can construct functions <code>Q -&gt; C</code>, where <code>C</code> are the objects of some category, by giving three pieces of data:</p>

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870849):
<p>1. a function <code>f : X -&gt; C</code>,<br>
2. for each <code>R x x'</code>, an isomorphism <code>φ x x' : f x ≅ f x'</code>, and<br>
3. for each <code>x x' x''</code> so that <code>R x x'</code> and <code>R x' x''</code> (and so automatically <code>R x x''</code>), we have <code>φ x x'</code> composed with <code>φ x' x''</code> is equal to `φ x x''.</p>

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870889):
<p>This says: you are only allowed to make functions out of <code>Q</code> that are independent of choices of representative _up to coherent isomorphisms_.</p>

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870890):
<p>So --- how do I do this in Lean?</p>

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870891):
<p>(The point of course is hygiene: we can sometimes help make our programs more correct by only using quotient types, when that's all that's needed. Unfortunately quotient types are a bit too restrictive for what actually happens in the real world.)</p>

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870892):
<p>(And no, it not useful in this situation to merely define functions to the isomorphism classes of objects of <code>C</code>, which is something you could do with a plain quotient and data 1-3.)</p>

#### [ Scott Morrison (Apr 30 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125871041):
<p>(A categorical quotient is at least as good as a quotient: you can take <code>C</code> to be a discrete category, where the only (iso)morphisms are identities, and this recovers the usually construction of function out of a quotient.)</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882176):
<p>Is this a non-trivial problem in dependent type theory?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882177):
<p>Is there a chance that it is not possible to define such a quotient?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882240):
<p>Note that Scott's question is really flagging the difference between and equivalence relation, and <code>equiv</code>. The statement that two terms in a setoid are equivalent is a proposition. However an instance of <code>equiv x y</code> really is data, and to a mathematician sometimes that data really is important.</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882310):
<p>There is a piece missing from the specification: what property do you get from those lift functions <code>Q -&gt; C</code>?</p>

#### [ Johan Commelin (Apr 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882354):
<p>They fit in a commutative diagram</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882404):
<p>of course, but what is it exactly?</p>

#### [ Johan Commelin (Apr 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882405):
<p>So, there is a quotient map <code>q : X -&gt; Q</code>, and the map <code>g : Q -&gt; C</code> that you have obtained is such that <code>f</code> is <em>equal</em> to <code>g \circ q</code></p>

#### [ Johan Commelin (Apr 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882407):
<p>I guess that <em>equal</em> does not mean defeq but only provable equality in a set of morphisms in the category</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882518):
<p>What prevents the definition <code>Q := X</code> and <code>lift f := f</code>?</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882624):
<p>I guess in the plain quotient case you have <code>quot.sound : R x y -&gt; q x = q y</code>, so here you want <code>sound : R x y -&gt; q x ~= q y</code>; then presumably <code>transport  (lift f φ) (sound (h : R x y)) = φ x y</code></p>

#### [ Johan Commelin (Apr 30 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882764):
<p>Wait, so now we are merging two themes? (-;</p>

#### [ Johan Commelin (Apr 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882778):
<p>But, to answer your question about <code>Q := X</code>. I should have added that the quotient map <code>q</code> should also satisfy points 2 and 3 from Scott's post.</p>

#### [ Johan Commelin (Apr 30 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882819):
<p>So <code>Q</code> is the universal gadget among all the data that satisfies 1, 2, and 3</p>

#### [ Johan Commelin (Apr 30 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882826):
<p>Also, it does not need to exist in all situations. Its existence is a theorem that has to be proven.</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883456):
<p>How can its existence be conditional? It doesn't have a category as input, so either Lean can prove these things exist in general or not</p>

#### [ Johan Commelin (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883461):
<blockquote>
<p>I want instead a categorical quotient of a type <code>X</code> by a relation <code>R</code>, let's call it <code>Q</code> which is useless except that we can construct functions <code>Q -&gt; C</code>, <strong>where <code>C</code> are the objects of some category</strong>, by giving three pieces of data:</p>
</blockquote>
<p>(emphasis mine)</p>

#### [ Johan Commelin (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883462):
<p>So, there is some category lurking in the background</p>

#### [ Scott Morrison (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883463):
<p>But Johan, it's not a fixed category.</p>

#### [ Scott Morrison (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883464):
<p>(I think? Maybe I'm confused about my own question. I wanted that description to hold for any category <code>C</code>.)</p>

#### [ Johan Commelin (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883465):
<p>Ok... then I'm confused</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883505):
<p><code>C</code> plays the role of beta in <code>quot.lift</code></p>

#### [ Scott Morrison (Apr 30 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883509):
<p>Yes.</p>

#### [ Johan Commelin (Apr 30 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883515):
<p>So, maybe Q always exists, but it is not always an object of <em>some category</em></p>

#### [ Johan Commelin (Apr 30 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883520):
<p>Because it only lives in some cocompletion of <em>said category</em></p>

#### [ Mario Carneiro (Apr 30 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883530):
<p>I don't think there is a requirement that <code>Q</code>be an element of <code>C</code></p>

#### [ Mario Carneiro (Apr 30 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883575):
<p>It's just some type, with a function to the objects of <code>C</code></p>

#### [ Mario Carneiro (Apr 30 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883576):
<p>it's the index category for a diagram in <code>C</code></p>

#### [ Johan Commelin (Apr 30 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883583):
<p>Ok, got it</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883625):
<p>Hm, there's a problem interpreting <code>Q</code> as a category: what are the equivs?</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883674):
<p>If <code>Q</code> is the universal thing satisfying 1-3, then we can slot <code>q</code> in for <code>f</code>, <code>Q</code> for <code>C</code>, and <code>sound</code> for <code>φ</code> to get the properties expected of <code>Q</code> itself, but then this means that <code>sound x x' : q x ~= q x'</code> and this doesn't make any sense since <code>q x : Q</code> is not a type</p>

#### [ Johan Commelin (Apr 30 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883724):
<p>Ok, I'm confused again...</p>

#### [ Johan Commelin (Apr 30 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883727):
<p>First I thought that Scott was trying to formalise some colimit inside some category</p>

#### [ Johan Commelin (Apr 30 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883730):
<p>But now it seems he wants to do something more general?</p>

#### [ Johan Commelin (Apr 30 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883776):
<p>Scott, is this an example of what you try to achieve: taking the quotient of all groups by the relation of isomorphism?</p>

#### [ Johan Commelin (Apr 30 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883782):
<p>But that is not coherent, I guess</p>

#### [ Mario Carneiro (Apr 30 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883785):
<p>I suspect what Scott wants to do is not possible unless you make a lot of non-canonical choices, but I await a full specification first</p>

#### [ Kevin Buzzard (May 02 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/126004937):
<p>This is very much related to all this canonical stuff I'm thinking about, so I would be interested in bumping this thread. I've only seen the notion of categorical quotient in algebraic geometry, where it looks like this: <a href="https://en.wikipedia.org/wiki/Categorical_quotient" target="_blank" title="https://en.wikipedia.org/wiki/Categorical_quotient">https://en.wikipedia.org/wiki/Categorical_quotient</a></p>

#### [ Kevin Buzzard (May 02 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/126005124):
<p>But here it's not just a relation on the object X you want to quotient, there is a group action. <span class="user-mention" data-user-id="110524">@Scott Morrison</span> did you need something more general than this? Note that X isn't a type in the version I know, it's an object in the category.</p>


{% endraw %}
