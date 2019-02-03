---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99733Leanlovestactics.html
---

## Stream: [general](index.html)
### Topic: [Lean loves tactics](99733Leanlovestactics.html)

---


{% raw %}
#### [ Patrick Massot (Jun 26 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672482):
<p>Why?</p>
<div class="codehilite"><pre><span></span><span class="n">structure</span><span class="w"> </span><span class="n">foo</span><span class="w"> </span><span class="p">(</span><span class="n">X</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">Type</span><span class="p">)</span><span class="w"> </span><span class="p">:</span><span class="o">=</span><span class="w"></span>
<span class="p">(</span><span class="n">domain</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">set</span><span class="w"> </span><span class="n">X</span><span class="p">)</span><span class="w"></span>
<span class="p">(</span><span class="n">map</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">domain</span><span class="w"> </span><span class="err">→</span><span class="w"> </span><span class="n">X</span><span class="p">)</span><span class="w"></span>


<span class="k">class</span><span class="w"> </span><span class="n">bar</span><span class="w"> </span><span class="p">(</span><span class="n">X</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">Type</span><span class="p">)</span><span class="w"> </span><span class="p">:</span><span class="o">=</span><span class="w"></span>
<span class="p">(</span><span class="n">foos</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">set</span><span class="w"> </span><span class="p">(</span><span class="n">foo</span><span class="w"> </span><span class="n">X</span><span class="p">))</span><span class="w"></span>
<span class="p">(</span><span class="n">prop</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">∀</span><span class="w"> </span><span class="n">f</span><span class="w"> </span><span class="err">∈</span><span class="w"> </span><span class="n">foos</span><span class="p">,</span><span class="w"> </span><span class="n">by</span><span class="w"> </span><span class="n">exact</span><span class="w"> </span><span class="p">(</span><span class="n">set.range</span><span class="w"> </span><span class="n">f.map</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">univ</span><span class="p">))</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="n">bar</span><span class="err">&#39;</span><span class="w"> </span><span class="p">(</span><span class="n">X</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">Type</span><span class="p">)</span><span class="w"> </span><span class="p">:</span><span class="o">=</span><span class="w"></span>
<span class="p">(</span><span class="n">foos</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">set</span><span class="w"> </span><span class="p">(</span><span class="n">foo</span><span class="w"> </span><span class="n">X</span><span class="p">))</span><span class="w"></span>
<span class="p">(</span><span class="n">prop</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">∀</span><span class="w"> </span><span class="n">f</span><span class="w"> </span><span class="err">∈</span><span class="w"> </span><span class="n">foos</span><span class="p">,</span><span class="w"> </span><span class="n">set.range</span><span class="w"> </span><span class="n">f.map</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">univ</span><span class="p">)</span><span class="w"> </span><span class="o">--</span><span class="w"> </span><span class="n">invalid</span><span class="w"> </span><span class="n">field</span><span class="w"> </span><span class="n">notation</span><span class="p">,</span><span class="w"> </span><span class="n">type</span><span class="w"> </span><span class="n">is</span><span class="w"> </span><span class="n">not</span><span class="w"> </span><span class="k">of</span><span class="w"> </span><span class="n">the</span><span class="w"> </span><span class="n">form</span><span class="w"> </span><span class="p">(</span><span class="n">C</span><span class="w"> </span><span class="p">...)</span><span class="w"> </span><span class="k">where</span><span class="w"> </span><span class="n">C</span><span class="w"> </span><span class="n">is</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="n">constant</span><span class="w">  </span><span class="n">f</span><span class="w"> </span><span class="n">has</span><span class="w"> </span><span class="n">type</span><span class="w">  </span><span class="n">?m_1</span><span class="w"></span>
</pre></div>

#### [ Simon Hudon (Jun 26 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672828):
<p>I think that's because the type of <code>f</code> is not fully elaborated by the time <code>f.map</code> is parsed. If you wrote:</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">prop</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">f</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">_</span><span class="o">,</span> <span class="n">f</span> <span class="err">∈</span> <span class="n">foos</span> <span class="bp">-&gt;</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="bp">=</span> <span class="n">univ</span><span class="o">)</span>
</pre></div>


<p>I think that should work</p>

#### [ Patrick Massot (Jun 26 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672972):
<p>I guessed the issue comes from elaboration but couldn't see the fix</p>

#### [ Patrick Massot (Jun 26 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672977):
<p>This fix indeed works</p>

#### [ Patrick Massot (Jun 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673023):
<p>In the mean time I also realize that defining an auxiliary function from <code>foo X</code> to <code>Prop</code> also works</p>

#### [ Patrick Massot (Jun 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673026):
<p>Thanks</p>

#### [ Simon Hudon (Jun 26 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673104):
<p>Also <code>has_mem</code> has two type parameters so the type of <code>∈</code> is not enough to impose a type on <code>f</code> until type class resolution</p>

#### [ Simon Hudon (Jun 26 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673109):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Patrick Massot (Jun 26 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673162):
<p>hum</p>

#### [ Simon Hudon (Jun 26 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673304):
<p>Can I clarify something?</p>

#### [ Patrick Massot (Jun 26 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673320):
<p>I think I sort of see</p>

#### [ Chris Hughes (Jun 26 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673587):
<p>Does elaboration always happen before type class resolution?</p>

#### [ Simon Hudon (Jun 26 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673704):
<p>I'm unsure whether elaboration is completed before type class resolution begins but most of it is done before type class resolution</p>


{% endraw %}
