---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54876rwcantmatchthis.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rw can't match this](https://leanprover-community.github.io/archive/113488general/54876rwcantmatchthis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 15 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765206):
<div class="codehilite"><pre><span></span>@has_mem.mem.{u u} α α
    (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_comprehension.to_has_zmem.{u} α has_comprehension))
    ?m_1
    (@zfc.comprehension.{u} α has_comprehension ?m_2 ?m_3)
</pre></div>


<div class="codehilite"><pre><span></span>@has_mem.mem.{u u} α α (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_zmem.mk.{u} α to_has_mem)) x
    (@zfc.comprehension.{u} α has_comprehension infinity (λ (x : α), false))
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765219):
<p>hmm, the situation is quite complicated</p>

#### [ Simon Hudon (Mar 15 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765285):
<p>Question?</p>

#### [ Kenny Lau (Mar 15 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765301):
<p>I've filled in more holes</p>

#### [ Kenny Lau (Mar 15 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765305):
<p>now <code>rw</code> can't match this:</p>
<div class="codehilite"><pre><span></span>@has_mem.mem.{u u} α α
    (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_comprehension.to_has_zmem.{u} α has_comprehension))
    x
    (@zfc.comprehension.{u} α has_comprehension infinity (λ (x : α), false))
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765307):
<p>where the goal contains:</p>
<div class="codehilite"><pre><span></span>@has_mem.mem.{u u} α α (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_zmem.mk.{u} α to_has_mem)) x
    (@zfc.comprehension.{u} α has_comprehension infinity (λ (x : α), false))
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765363):
<p>If I'm analyzing correctly, it would be a failure to match this with this:</p>
<div class="codehilite"><pre><span></span>@zfc.has_comprehension.to_has_zmem.{u} α has_comprehension
</pre></div>


<div class="codehilite"><pre><span></span>@zfc.has_zmem.mk.{u} α to_has_mem
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765368):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> question: do you see any way to fix it?</p>

#### [ Simon Hudon (Mar 15 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765379):
<p>What are you trying to do?</p>

#### [ Kenny Lau (Mar 15 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765444):
<p>rewrite <code>hx : x ∈ comprehension infinity (λ (x : α), false)</code></p>

#### [ Simon Hudon (Mar 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765470):
<p>What is the rule that you're using?</p>

#### [ Kenny Lau (Mar 15 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765517):
<div class="codehilite"><pre><span></span>∀ A p x, x ∈ comprehension A p ↔ x ∈ A ∧ p x
</pre></div>

#### [ Simon Hudon (Mar 15 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765631):
<p>Why do you have <code>(@zfc.has_zmem.mk.{u} α to_has_mem)</code>?</p>

#### [ Simon Hudon (Mar 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765654):
<p>And where does <code>to_has_mem</code> come from?</p>

#### [ Kenny Lau (Mar 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765655):
<p>I'm in the middle of a structure doing things like this</p>

#### [ Kenny Lau (Mar 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765659):
<div class="codehilite"><pre><span></span>(has_zempty : has_zempty α :=
  { emptyc := @@comprehension has_comprehension infinity (λ x, false),
    empty_not_zmem := λ x hx, begin simp [∅] at hx, rw [@@zmem_comprehension_iff has_comprehension infinity (λ (x : α), false) x] at hx, end })
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765723):
<div class="codehilite"><pre><span></span>class has_zmem extends has_mem α α

class has_zempty extends has_zmem α, has_emptyc α :=
(empty_not_zmem : ∀ x, x ∉ (∅:α))
</pre></div>

#### [ Simon Hudon (Mar 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765725):
<p>Try extracting </p>
<div class="codehilite"><pre><span></span><span class="o">{</span> <span class="n">emptyc</span> <span class="o">:=</span> <span class="bp">@@</span><span class="n">comprehension</span> <span class="n">has_comprehension</span> <span class="n">infinity</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">false</span><span class="o">),</span>
    <span class="n">empty_not_zmem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span> <span class="k">begin</span> <span class="n">simp</span> <span class="o">[</span><span class="err">∅</span><span class="o">]</span> <span class="n">at</span> <span class="n">hx</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="bp">@@</span><span class="n">zmem_comprehension_iff</span> <span class="n">has_comprehension</span> <span class="n">infinity</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">false</span><span class="o">)</span> <span class="n">x</span><span class="o">]</span> <span class="n">at</span> <span class="n">hx</span><span class="o">,</span> <span class="kn">end</span> <span class="o">})</span>
</pre></div>


<p>into a separate definition</p>

#### [ Kenny Lau (Mar 15 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765947):
<p>thanks</p>


{% endraw %}
