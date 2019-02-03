---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51153addinganelementtoaset.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [adding an element to a set](https://leanprover-community.github.io/archive/113488general/51153addinganelementtoaset.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 26 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330334):
<p>The notation <code>+</code> is attached to <code>has_add.add : X -&gt; X -&gt; X</code>. Mathematicians use <code>+</code> in more general ways though. I find myself wanting to write <code>r + J</code> for <code>r</code> an element of, and <code>J</code> a subset of, an additive abelian group (<code>J</code> is a subgroup in fact). This is standard notation in mathematics and I suspect I can't have it given the set-up we have. Does anyone have any thoughts as to how I might try and represent such an idea in Lean? I can make the object I want no problem, the issue is simply that I want the notation to be as close to what a mathematician would write as possible.</p>

#### [ Kenny Lau (Jul 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330459):
<p>It's called a coset.</p>

#### [ Kenny Lau (Jul 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330461):
<p>specifically, a left coset</p>

#### [ Kevin Buzzard (Jul 26 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330474):
<p>I've seen cosets in group theory but unfortunately this is an additive group ;-)</p>

#### [ Kenny Lau (Jul 26 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130330478):
<p><code>additive</code></p>

#### [ Kevin Buzzard (Jul 26 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331527):
<p>How scalable is this <code>additive</code> idea I wonder? I recently wanted a free abelian group with group law multiplication but ultimately settled on group law addition because thay was what the finsupp construction gave me and I couldn't face cluttering everything up with additive and multiplicative everywhere.</p>

#### [ Kenny Lau (Jul 26 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331592):
<p>as scalable as I made it in my constructive tensor product</p>

#### [ Kenny Lau (Jul 26 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331599):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">free_abelian_group</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="n">additive</span> <span class="err">$</span> <span class="n">abelianization</span> <span class="err">$</span> <span class="n">free_group</span> <span class="n">α</span>
</pre></div>

#### [ Kenny Lau (Jul 26 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331610):
<p>and the proof that it works is that I built the whole tensor product out of the free abelian group</p>

#### [ Chris Hughes (Jul 26 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331623):
<p><code>(+ r) '' J</code></p>

#### [ Kenny Lau (Jul 26 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331660):
<p>I would prefer <code>((-) r) ⁻¹' J</code></p>

#### [ Johan Commelin (Jul 26 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130331735):
<p>I would prefer readable notation.</p>

#### [ Kevin Buzzard (Jul 26 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20an%20element%20to%20a%20set/near/130332818):
<p>I would prefer the notation mathematicians use, i.e. what we can't have.</p>


{% endraw %}
