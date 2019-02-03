---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24101cardinalsoffinitesets.html
---

## Stream: [general](index.html)
### Topic: [cardinals of finite sets](24101cardinalsoffinitesets.html)

---


{% raw %}
#### [ Mario Carneiro (Aug 18 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132344762):
<p>People have mentioned that working with the size of finite sets is a bit complicated right now. We have two methods to talk about the cardinality of a type:</p>
<ul>
<li><code>fintype.card A</code>, which requires a <code>[fintype A]</code> instance (and hence asserts cardinality separately from finiteness), and</li>
<li><code>cardinal.mk A</code>, which works on any type but has type <code>cardinal</code> instead of <code>nat</code> (which makes it useful for different sizes of infinite sets).</li>
</ul>
<p>In order to use this latter expression to assert a set has a finite number cardinality you have to write <code>cardinal.mk A = ↑n</code> where <code>n : nat</code>, which is a bit messy, since <code>cardinal.mk A = 37</code> is not the same as <code>cardinal.mk A = ↑37</code> (you can use <code>simp</code> to turn one into the other).</p>
<p>I would like to make it easy to talk about finite sets with natural number cardinalities, without having finiteness as a precondition. Some options:</p>
<ul>
<li><code>has_card A n</code> is <code>{ x : fintype A // card A x = n }</code>. This has the advantage that it is computable, and a subsingleton, although it is not a proposition stated this way. Since it is a relation rather than a function, you can't rewrite with it, but whether this is a problem depends on how it is used.</li>
<li><code>card_xnat A : with_top nat</code> is a noncomputable function that takes the value <code>⊤</code> on infinite sets and <code>n</code> on finite sets of cardinality <code>n</code>. Here we can state lemmas like <code>card_xnat (sum A B) = card_xnat A + card_xnat B</code> without preconditions, and prove equality with other kinds of cardinality to relate back to the computable versions.</li>
<li><code>card_nat A : nat</code> is the same as <code>card_xnat</code> but with a 0 default value instead of <code>⊤</code>. This is really just a totalized partial function, so many theorems will not hold without finiteness assumptions, but it has the advantage that it takes values in <code>nat</code> so you get the same experience as <code>fintype.card A</code> but without the dependent argument, which can sometimes mess up rewrites.</li>
</ul>

#### [ Johannes Hölzl (Aug 18 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132355335):
<p>I'm currently finishing <code>ennreal := with_top nnreal</code>. The setup should work also for <code>nat</code>, then <code>card_xnat</code> (maybe named <code>card_enat</code>, c.f. <code>ennreal</code>) would work nice, as it goes into a complete lattice.</p>

#### [ Chris Hughes (Aug 18 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356222):
<p>What's the solution used on Coq? Presumably they must have dealt with this a lot to prove Feit Thompson.</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356604):
<p>feit thompson dealt almost exclusively in finite group theory</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356605):
<p>so it wasn't a problem to have finiteness assumptions everywhere</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356614):
<p>plus ssreflect has a lot of slightly different approaches to all this stuff which emphasizes <code>bool</code> predicates over propositions</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356665):
<p>Metamath has a <code>#</code> function which is essentially <code>card_enat</code>; it has a range which is a subset of ennreal (of course they don't deal with subtypes like we do here)</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356675):
<p>but you could say basically <code>#({A, B, C}) = 3</code> where that is the usual <code>3</code></p>

#### [ Mario Carneiro (Aug 18 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356726):
<p>and this was a distinct function from <code>card : V -&gt; On</code> which takes values in the ordinals (and defines the cardinals as the range of this function)</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/132356791):
<p>I think that in general the classical mathematics approach used in lean makes it resemble Isabelle and Metamath a lot more than Coq</p>

#### [ Chris Hughes (Aug 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133084180):
<p>May I suggest another option. If we're going down the noncomputable route and the having two different definitions route, I think the best solution is to have a <code>finite</code> predicate to use instead of <code>fintype</code>. This has the advantage of solving the <code>rw</code> issue, which also indirectly helps the type class inference issue, because theorems like <code>card_empty</code> wouldn't need <code>fintype empty</code> as an input, which makes the type class inference issue easier as well.</p>
<p>All of these options seem wrong to me however, and I'd much rather not confuse people even more by introducing a fourth way of talking about finite cardinals.</p>

#### [ Kenny Lau (Aug 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133084213):
<p>what is your fourth way?</p>

#### [ Chris Hughes (Aug 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133084379):
<p>Making a <code>finite</code> predicate instead of <code>fintype</code> which is <code>Type</code></p>

#### [ Johannes Hölzl (Aug 31 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cardinals%20of%20finite%20sets/near/133108434):
<p>We have already <code>set.finite</code>. It was defined as inductive over empty and insert, currently it is defined by saying that the set coerced to a type is a <code>fintype</code>.</p>


{% endraw %}
