---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11367matchindefs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [match in defs](https://leanprover-community.github.io/archive/113488general/11367matchindefs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Apr 02 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124532070):
<p>Out of the following two definitions, I find the first much easier to use.</p>
<div class="codehilite"><pre><span></span><span class="kn">private</span>  <span class="n">def</span>  <span class="n">mul_aux</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">loc</span> <span class="n">α</span> <span class="n">S</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="err">⟦</span><span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span>  <span class="bp">*</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span>  <span class="bp">*</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="err">⟧</span>

<span class="kn">private</span> <span class="n">def</span> <span class="n">mul_aux</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">loc</span> <span class="n">α</span> <span class="n">S</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">r₁</span><span class="o">,</span> <span class="n">s₁</span><span class="o">,</span> <span class="n">hs₁</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">r₂</span><span class="o">,</span> <span class="n">s₂</span><span class="o">,</span> <span class="n">hs₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="err">⟦</span><span class="bp">⟨</span><span class="n">r₁</span> <span class="bp">*</span> <span class="n">r₂</span><span class="o">,</span> <span class="n">s₁</span> <span class="bp">*</span> <span class="n">s₂</span><span class="o">,</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">hs₁</span> <span class="n">hs₂</span><span class="bp">⟩</span><span class="err">⟧</span>
</pre></div>


<p>The first one unfolds much more easily if I give it arguments either of the form <code>x y</code> but also works okay with <code>⟨r₁, s₁, hs₁⟩ ⟨r₂, s₂, hs₂⟩</code> as arguments. What are the advantages/disadvantages of each approach?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124540129):
<p>Let me make the comment that in the past, when I have used pointy brackets and lambdas when writing a definition, I've found it much more difficult to prove things by rfl because high powered stuff is going on behind the scenes.</p>

#### [ Chris Hughes (Apr 02 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124544887):
<p>Essentially, I think it's because<code> λ ⟨r₁, s₁, hs₁⟩ </code> uses prod.rec and subtype.rec, or the various derived lemmas like <code>subtype.cases_on</code> and these don't reduce to anything unless you give them something of the form <code>subtype.mk _ _</code> The first def will unfold when the arguments are not of the form <code>subtype.mk _ _</code></p>

#### [ Kenny Lau (Apr 02 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124545185):
<p>don't use any pointy brackets or tactics in a definition</p>

#### [ Simon Hudon (Apr 03 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552407):
<p>Any reason not to want this?</p>
<div class="codehilite"><pre><span></span>private def mul_aux : α × S → α × S → loc α S
| ⟨r₁, s₁, hs₁⟩ ⟨r₂, s₂, hs₂⟩ := ⟦⟨r₁ * r₂, s₁ * s₂, is_submonoid.mul_mem hs₁ hs₂⟩⟧
</pre></div>


<p>It only unfolds with explicit tuples, unlike the first alternative. In the second alternative, it will unfold to a useless auxiliary definition.</p>

#### [ Kenny Lau (Apr 03 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552424):
<p>it's private</p>

#### [ Simon Hudon (Apr 03 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552442):
<p>Why is that relevant?</p>

#### [ Kenny Lau (Apr 03 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552499):
<p>it isn't</p>

#### [ Simon Hudon (Apr 03 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552550):
<p>Why was that your response to my question then?</p>

#### [ Kenny Lau (Apr 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552626):
<p>it wasn't</p>

#### [ Kenny Lau (Apr 03 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552651):
<p>it's relevant because I'm not going to unfold that definition except in the definition of multiplication</p>

#### [ Kenny Lau (Apr 03 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552691):
<p>and I only need to use its properties, not its definition</p>

#### [ Simon Hudon (Apr 03 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552703):
<p>Are you saying that the whole conversation is pointless?</p>

#### [ Kenny Lau (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552745):
<p>he's asking about one of my definitions</p>

#### [ Kenny Lau (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552746):
<p>I don't know why he's doing that</p>

#### [ Simon Hudon (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552749):
<p>ok</p>

#### [ Kenny Lau (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552750):
<blockquote>
<p>Are you saying that the whole conversation is pointless?</p>
</blockquote>
<p>• &lt;-- there you go, a point</p>

#### [ Simon Hudon (Apr 03 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552879):
<p>Sorry that, was the wrong place to write that.</p>

#### [ Kenny Lau (Apr 03 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552882):
<p>sorry</p>


{% endraw %}
