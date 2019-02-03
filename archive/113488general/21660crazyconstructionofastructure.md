---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21660crazyconstructionofastructure.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [crazy construction of a structure](https://leanprover-community.github.io/archive/113488general/21660crazyconstructionofastructure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 19 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805454):
<p>I never knew one could do this: <a href="https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/ring_theory/localization.lean#L80" target="_blank" title="https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/ring_theory/localization.lean#L80">https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/ring_theory/localization.lean#L80</a> (definition of ring structure on a localization).</p>

#### [ Kevin Buzzard (May 19 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805506):
<p>Here are the two ways I knew of building instances of a structure:</p>

#### [ Kevin Buzzard (May 19 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805508):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">baz</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">bar</span> <span class="o">:=</span> <span class="mi">34</span><span class="o">,</span>
  <span class="n">baz</span> <span class="o">:=</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span>
<span class="o">}</span>

<span class="kn">definition</span> <span class="n">y</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">3</span><span class="o">,</span><span class="n">true</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 19 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805518):
<p>The second one I always think of as "pointy brackets are a generic way of building something which needs two (say) "inputs", like a proof of <code>P and Q</code>"</p>

#### [ Kevin Buzzard (May 19 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805558):
<p>The first one I always just assumed was custom notation that only made sense for structures</p>

#### [ Kevin Buzzard (May 19 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805567):
<p>I don't really know what the link is doing, but I do know that <code>by {blah,blah,blah}</code> is pretty much the same as <code>(begin blah,blah,blah, end)</code>, which is surely a different usage of the squiggly brackets</p>

#### [ Reid Barton (May 19 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805607):
<p><code>by</code> takes a tactic. The tactic is <code>refine ...</code>.<br>
<code>refine</code> takes an expression with some holes. The expression is <code>{ ... }</code>. Here the <code>{</code>...<code>}</code> are building a structure, like you already know.</p>

#### [ Patrick Massot (May 19 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805614):
<p>This pattern has been discussed many times here</p>

#### [ Patrick Massot (May 19 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805616):
<p>Put every definition in the refine and then proofs</p>

#### [ Patrick Massot (May 19 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805656):
<p>The <code>..</code> at the end is important</p>

#### [ Reid Barton (May 19 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126805659):
<p>Well, really the tactic is <code>refine ...; { ... }</code> and these other <code>{}</code>s are <code>solve_one begin ... end</code> or whatever</p>

#### [ Kevin Buzzard (May 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126807008):
<blockquote>
<p>The <code>..</code> at the end is important</p>
</blockquote>
<p>I don't see any <code>..</code> at the end in my link</p>

#### [ Patrick Massot (May 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126807096):
<p>That's because there are underscores around. If you do what I wrote (define operations, leave out proofs), you need <code>..</code></p>

#### [ Patrick Massot (May 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/crazy%20construction%20of%20a%20structure/near/126807101):
<p>I think</p>


{% endraw %}
