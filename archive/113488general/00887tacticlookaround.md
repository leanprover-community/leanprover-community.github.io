---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00887tacticlookaround.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tactic look around](https://leanprover-community.github.io/archive/113488general/00887tacticlookaround.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Mar 06 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123344266):
<p>Assume I write</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">bar</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">magic</span> <span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Mar 06 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123344320):
<p>Can I write a tactic <code>magic</code> which knows that the instance I'm trying to create has type <code>foo</code> and the current field I'm working on is called <code>bar</code>?</p>

#### [ Patrick Massot (Mar 06 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123344599):
<p>The motivation for this question is <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean</a> (look at all lines containing <code>funext</code>)</p>

#### [ Scott Morrison (Mar 06 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123350559):
<p>I'm also interested in this question! As far as I understand, this isn't possible, but it seems quite desirable for tactics to be able to know the "reason" they have been invoked.</p>

#### [ Simon Hudon (Mar 06 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123362941):
<p>The closest I can find is <code>decl_name</code> which tells you the name of the declaration being elaborated. I haven't tried but I'm not sure <code>resolve_name</code> would work on it to then get the type</p>

#### [ Simon Hudon (Mar 06 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123363136):
<p>What you could try is </p>
<div class="codehilite"><pre><span></span>instance : foo :=
begin magic ... end
</pre></div>


<p>Where magic acts a bit like <code>refine</code> and use <code>structure_fields</code> to apply <code>funext ; ...</code> for every fields for which it works and leaves the other ones untouched.</p>

#### [ Scott Morrison (Mar 07 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123375425):
<p><span class="user-mention" data-user-email="simon.hudon@gmail.com" data-user-id="110026">@Simon Hudon</span>, <code>decl_name</code> works fine, but feeding that into <code>resolve_name</code> just gets an error message <code>identifier not found</code>. Oh well!</p>

#### [ Simon Hudon (Mar 07 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123375435):
<p>I'm not too surprised. I'm looking at that file right now and I think <code>target</code> is more promising.</p>

#### [ Simon Hudon (Mar 07 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123375437):
<p>I think the tactic will look like:</p>
<div class="codehilite"><pre><span></span>instance monoid [∀ i, monoid $ f i] : monoid (Π i : I, f i) :=
by lifted_instance [indexed_product.has_one,indexed_product.semigroup]
</pre></div>

#### [ Simon Hudon (Mar 07 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123376745):
<p>Here's what I ended up with: <a href="https://github.com/PatrickMassot/lean-differential-topology/pull/1" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/pull/1">https://github.com/PatrickMassot/lean-differential-topology/pull/1</a></p>

#### [ Simon Hudon (Mar 07 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123376765):
<p>The Lean developers added <code>pexpr.mk_structure_instance</code> after I complained about it but I never got around to using it. I think it's a very nice feature.</p>


{% endraw %}
