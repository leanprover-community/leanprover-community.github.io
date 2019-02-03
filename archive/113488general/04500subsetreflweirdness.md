---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04500subsetreflweirdness.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [subset refl weirdness](https://leanprover-community.github.io/archive/113488general/04500subsetreflweirdness.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (May 04 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108434):
<p>Is this a bug?</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">s</span> <span class="err">⊆</span> <span class="n">s</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">error: invalid apply tactic, failed to unify</span>
<span class="cm">  @has_subset.subset.{0} (set.{0} α) (@set.has_subset.{0} α) s s</span>
<span class="cm">with</span>
<span class="cm">  @has_subset.subset.{?l_1} (list.{?l_1} ?m_2) (@list.has_subset.{?l_1} ?m_2) ?m_3 ?m_3</span>
<span class="cm">state:</span>
<span class="cm">α : Type,</span>
<span class="cm">s : set.{0} α</span>
<span class="cm">⊢ @has_subset.subset.{0} (set.{0} α) (@set.has_subset.{0} α) s s</span>
<span class="cm">-/</span>
</pre></div>

#### [ Reid Barton (May 04 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108665):
<p>I guess this actually does not exist anywhere...?</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">refl</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">s</span> <span class="err">⊆</span> <span class="n">s</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">id</span>
</pre></div>

#### [ Simon Hudon (May 04 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108698):
<p>You're probably right. You can try:</p>
<div class="codehilite"><pre><span></span>local attribute [refl] set.subset.refl -- if that&#39;s the name of the appropriate lemma
</pre></div>

#### [ Simon Hudon (May 04 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108701):
<p>Then your proof will work</p>

#### [ Reid Barton (May 04 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108905):
<p>Ah, the lemma does exist in mathlib, but without <code>@[refl]</code></p>

#### [ Kevin Buzzard (May 05 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126115996):
<p>The proof of a refl lemma is often <code>rfl</code>, and conversely any proof which is proved with <code>rfl</code> is I think automatically tagged <code>@[refl]</code>, but because the proof wasn't rfl here the tag is needed.</p>

#### [ Simon Hudon (May 05 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126116079):
<p><code>rfl</code> is only for reflexivity of equality and the tag comes from the fact that <code>rfl</code> implies that the two terms are definitionally equal. But if we're talking of reflexivity of other relations than equality, it doesn't imply anything with regards to definitional equality</p>

#### [ Kevin Buzzard (May 05 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126116346):
<p>I just tried my theory and the lemma I proved with rfl was tagged <code>@[_refl_lemma]</code> not <code>@[refl]</code></p>

#### [ Chris Hughes (May 05 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126151045):
<p><code>@[refl]</code> means it's a proof that a relation is reflexive and is for the <code>refl</code> tactic. <code>@[_refl_lemma]</code> means it's a proof of equality proved using <code>rfl</code> for the <code>dsimp</code> tactic.</p>


{% endraw %}
