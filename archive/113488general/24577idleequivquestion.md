---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24577idleequivquestion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [idle equiv question](https://leanprover-community.github.io/archive/113488general/24577idleequivquestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831713):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="n">def</span> <span class="n">αu</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span>
<span class="n">def</span> <span class="n">αv</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span>
<span class="n">def</span> <span class="n">αuv</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831714):
<p>Which of those types are related by equiv?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831756):
<p>equiv is my new toy</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831759):
<p>and I realise I don't understand universes</p>

#### [ Chris Hughes (Apr 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831764):
<p>none of them? equiv has nothing to do with universes.</p>

#### [ Gabriel Ebner (Apr 29 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846281):
<p>All of them?  Given <code>X</code> and <code>Y</code>, all of <code>αu X Y</code>, <code>@αv X Y</code>, and <code>@αuv X Y</code> are definitionally equal (and hence equiv).  You cannot even state that <code>αu ≃ @αuv</code> (as they are not types).</p>

#### [ Gabriel Ebner (Apr 29 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846329):
<p>Since you're worried about universes, let me annotate the first example with universes:  Given <code>X : Type u</code> and <code>Y : Type u</code>, all of <code>αu.{u} X Y</code>, <code>@αv.{u u} X Y</code>, and <code>@αuv.{u} X Y</code> are definitionally equal (and hence equiv).  The only potential way to even write down this statement is by using the same universe variable for both <code>X</code> and <code>Y</code>.</p>

#### [ Gabriel Ebner (Apr 29 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846414):
<p>(deleted)</p>

#### [ Gabriel Ebner (Apr 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846600):
<p>Maybe it's useful to think about the interpretation of <code>equiv</code> in the set-theoretic model: there, two sets are <code>equiv</code> iff they have the same cardinality.  And <code>Type u</code> is the <code>u</code>-th inaccessible cardinal.  So you're asking when two function spaces are equinumerous.</p>

#### [ Kevin Buzzard (Apr 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125852120):
<p>The question that remains, which is not particularly well-defined, is whether it is somehow possible using <code>ulift</code> to have <code>{X : Type u}</code> and <code>{Y : Type v}</code> and (maybe using ulift here) making some kind of<code>alphau X Y</code> which is equiv to <code>alphauv X Y</code></p>

#### [ Mario Carneiro (Apr 29 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125852168):
<p>sure, <code>U -&gt; V</code> is equiv to <code>ulift U -&gt; V</code> or <code>U -&gt; ulift V</code></p>

#### [ Mario Carneiro (Apr 29 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125852179):
<p>(not sure why you are writing it with the funny notation, but that's just the arrow type)</p>


{% endraw %}
