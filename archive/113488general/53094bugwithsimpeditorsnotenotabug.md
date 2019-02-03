---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53094bugwithsimpeditorsnotenotabug.html
---

## Stream: [general](index.html)
### Topic: [bug with simp (editor's note: not a bug)](53094bugwithsimpeditorsnotenotabug.html)

---


{% raw %}
#### [ Kenny Lau (Mar 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123327630):
<div class="codehilite"><pre><span></span>import algebra.linear_algebra.basic

variables (α β : Type) [ring α] [module α β]

example (v : lc α β) (h : v 0 = 0) : sorry :=
begin
  simp [lc] at v,
end
</pre></div>

#### [ Kenny Lau (Mar 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123327634):
<div class="codehilite"><pre><span></span>α β : Type,
_inst_1 : ring α,
_inst_2 : module α β,
v : lc α β,
h : ⇑v 0 = 0,
v : β →₀ α
⊢ sorry
</pre></div>

#### [ Kenny Lau (Mar 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123327637):
<p>the bug is that it creates another <code>v</code></p>

#### [ Reid Barton (Mar 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123328368):
<p>I think it has to do with the fact that the hypothesis <code>h</code> depends on <code>v</code>, but I'm not sure what you're supposed to do about that</p>

#### [ Reid Barton (Mar 06 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123328469):
<p><code>dsimp</code> works</p>

#### [ Mario Carneiro (Mar 06 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123330492):
<p>Yeah, this is not a bug. The new <code>v</code> cannot necessarily take the place of the old <code>v</code> in <code>h</code></p>

#### [ Mario Carneiro (Mar 06 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123330505):
<p><code>dsimp</code> allows this because the rewrite is definitional, so the new <code>v</code> has the same type as the old one, but if it's merely a propositionally equal type, then you may have to replace <code>v</code> with <code>cast v &lt;ugly proof&gt;</code> in uses of <code>v</code></p>

#### [ Scott Morrison (Mar 06 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123335508):
<p>It would be nice if there was either a mode for simp, or just a cousin, that was much more aggressive about replacing later appearances of the simplified hypothesis, even if it required casts. I run into this fairly often.</p>

#### [ Scott Morrison (Mar 06 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123335548):
<p>Very often a step or two later the cast itself becomes easy to simplify, and you're back on safe ground.</p>

#### [ Mario Carneiro (Mar 06 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123335626):
<p>I think you can achieve this effect by reverting the dependent hypotheses</p>

#### [ Mario Carneiro (Mar 06 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123337049):
<p>But in my experience <code>cast</code>s are a pain to get rid of. What kind of proof strategy causes them to be "easy to simplify"?</p>

#### [ Scott Morrison (Mar 06 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123337471):
<p>At some point I'll try to come up with a full example. But I've certainly found situations where "almost trivial" lemmas such as </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="o">{</span><span class="n">u₁</span> <span class="n">u₂</span><span class="o">}</span> <span class="n">parallel_transport_for_trivial_bundles</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u₂</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="n">α</span> <span class="n">a</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">β</span><span class="o">)</span> <span class="n">x</span> <span class="n">b</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">induction</span> <span class="n">p</span><span class="o">,</span>
<span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>cause <code>@eq.rec</code>s to vanish away again. Right now I have to deal with some jet lag.</p>


{% endraw %}
