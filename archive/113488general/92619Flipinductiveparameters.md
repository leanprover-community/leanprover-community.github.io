---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92619Flipinductiveparameters.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Flip inductive parameters](https://leanprover-community.github.io/archive/113488general/92619Flipinductiveparameters.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Nicholas Scheel (Jun 05 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578848):
<p>Is there a way to flip the <code>Type</code> and <code>ℕ</code> parameters around so I can make this a functor?</p>
<div class="codehilite"><pre><span></span>inductive Bezier (β : Type) : ℕ → Type
| point : β → Bezier 0
| curve : Π {n}, Bezier n → β → Bezier (n+1)
</pre></div>

#### [ Simon Hudon (Jun 05 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578914):
<p>You can do </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Bezier&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Bezier</span> <span class="n">β</span> <span class="n">n</span>
</pre></div>

#### [ Simon Hudon (Jun 05 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578955):
<p>And make <code>Bezier'</code> a functor (or switch the names)</p>

#### [ Nicholas Scheel (Jun 05 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578967):
<p>okay, that should work :)</p>

#### [ Nicholas Scheel (Jun 05 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127579887):
<p>wat</p>
<div class="codehilite"><pre><span></span>invalid type ascription, term has type
  g &lt;$&gt; @Bezier&#39;.curve α n (@pure (Bezier&#39; n) (@Bezier&#39;.has_pure n) α x) x =
    @Bezier&#39;.curve β n (g &lt;$&gt; @pure (Bezier&#39; n) (@Bezier&#39;.has_pure n) α x) (g x)
but is expected to have type
  g &lt;$&gt; @Bezier&#39;.curve α n (@pure (Bezier&#39; n) (@Bezier&#39;.has_pure n) α x) x = ?m_1
</pre></div>

#### [ Simon Hudon (Jun 05 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127579928):
<p>try <code>set_option pp.all true</code> before your proof. It will display all the implicit parameters, universe levels and expand notations</p>

#### [ Nicholas Scheel (Jun 05 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580056):
<p>aha, thank you! it was using <code>applicative.to_functor</code> and applicative's default map <span class="emoji emoji-1f926" title="face palm">:face_palm:</span></p>

#### [ Simon Hudon (Jun 05 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580100):
<p>Do you by any chance have a <code>functor</code> and a <code>applicative</code> instance available in your context?</p>

#### [ Simon Hudon (Jun 05 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580101):
<p>If you're used to Haskell, you'll see that Lean does not ensure that instances are globally unique</p>

#### [ Nicholas Scheel (Jun 05 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580114):
<p>I get that :) and yes, I have <code>functor</code> and <code>applicative</code>, working on <code>is_lawful_applicative</code></p>

#### [ Simon Hudon (Jun 05 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580157):
<p>I suggest you make sure that only one is available at any time</p>


{% endraw %}
