---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40322easyinmathsunionquestion.html
---

## Stream: [general](index.html)
### Topic: [easy-in-maths union question](40322easyinmathsunionquestion.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196178):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">uu</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">}),</span> <span class="n">f</span> <span class="n">uu</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃₀</span><span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>"Two ways of writing a union are the same".</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196225):
<p>This is a joy to prove in tactic mode using <code>set.subset.antisymm</code></p>

#### [ Kenny Lau (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196229):
<p>is "joy" sarcasm?</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196232):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">y</span> <span class="n">Hy</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">Hy</span> <span class="k">with</span> <span class="n">V</span> <span class="n">HV</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">HV</span> <span class="n">HyV</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">uu</span> <span class="n">HuV</span><span class="o">,</span>
    <span class="n">change</span> <span class="n">V</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">uu</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">at</span> <span class="n">HuV</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">V</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">HyV</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">uu</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">uu</span><span class="bp">.</span><span class="n">property</span><span class="o">,</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">HuV</span><span class="bp">⟩</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">y</span> <span class="n">Hy</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">Hy</span> <span class="k">with</span> <span class="n">V</span> <span class="n">HV</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">HV</span> <span class="n">HyV</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">u</span> <span class="n">HuV</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">V</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">HyV</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">u</span><span class="o">,</span><span class="n">HuV</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">}),</span>
    <span class="n">exact</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">HuV</span><span class="bp">.</span><span class="mi">2</span>
  <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196238):
<p>no, not at all</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196248):
<p>I feel like goals like this are ones that I know I can crush</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196250):
<p>so it's a bit like grinding in the early Zeldas</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196251):
<p>you know you can do it and it's quite fun to do</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196252):
<p>But for something of this form which is trivially true in maths</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196291):
<p>my understanding is that one should seek a short "obfuscated" proof</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196301):
<p>i.e. pull a couple of things out the library and you're done</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196302):
<p>so I looked through <code>data.set.lattice</code></p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196303):
<p>and I found</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196308):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">set</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">sUnion_image</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">Union_eq_sUnion_image</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">sUnion_eq_Union</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">sUnion_eq_Union&#39;</span>
</pre></div>

#### [ Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196317):
<p>all of which said "a union equals a union"</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196318):
<p>but I just can't put them all together</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196322):
<p>So I am wondering if this is a hole in the library or if I'm missing a trick</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196324):
<p>I don't know this file very well</p>

#### [ Kenny Lau (Apr 17 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196365):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">uu</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">}),</span> <span class="n">f</span> <span class="n">uu</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃₀</span><span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">H1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">H3</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">H3</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">H3</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">H1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">H2</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">H3</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kevin Buzzard (Apr 17 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196369):
<p>I need to be quick because my daughter just woke up (she is sick and off school)</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196376):
<p>but while I'm here let me mention the independent question that I was talking about <code>existsi _</code> yesterday or so and Mario advised me not to use it, saying it was better to go back and fill it in later.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196384):
<p>However in my proof above, I used it because the thing that exists is another existsi</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196391):
<p>Aah excellent -- that looks much more like the 2-line obfuscated proof which this result deserves.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196437):
<p>Should it be in the library?</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196438):
<p>Thanks Kenny.</p>

#### [ Kenny Lau (Apr 17 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196441):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">uu</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">}),</span> <span class="n">f</span> <span class="n">uu</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃₀</span><span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">set_eq_def</span><span class="o">]</span>
</pre></div>

#### [ Johannes Hölzl (Apr 17 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196452):
<p>the simplifier also works: <code>by simp [set.set_eq_def]</code></p>

#### [ Kenny Lau (Apr 17 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196454):
<p>now we just switched camps :P</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196507):
<p>Aah! I tried to use simp a lot too, but my simp-fu is weak.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196511):
<p>Thanks Johannes. How long did it take you to find that?</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196522):
<p>You see, the long tactic mode proof took me a very short time to write, because at each stage I just did the only thing which could be done.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196528):
<p>I suspect that Kenny had a similar experience with the term proof.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196543):
<p>But when I tried to find a short proof using library functions, all that happened was that I spent a long time looking through the library and noting down possibly useful functions</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196584):
<p>and then a long time failing to glue them together.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196587):
<p>I want to get to the stage where if it's easy in maths, I can just nail it in Lean</p>

#### [ Kenny Lau (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196593):
<div class="codehilite"><pre><span></span>example {X Y : Type u} (U : set X) (f : X → set Y) :
(⋃ (uu : {x // x ∈ U}), f uu.val) = ⋃₀(f &#39;&#39; U) :=
set.ext $ by simp
</pre></div>

#### [ Kevin Buzzard (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196596):
<p>right</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196604):
<p>But this stinks because surely my strategy is basically the same</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196607):
<p>except I split the iff into two distinct implications</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196609):
<p>and then somehow simp failed to deal with either of them</p>

#### [ Kenny Lau (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196658):
<p><code>simp</code> simplifies iff's and equalities, lol</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196659):
<p>As I said, my simp-fu is weak</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196664):
<p>so that's the trick -- don't break the symmetry.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196665):
<p>Thanks -- that was very instructive!</p>

#### [ Kenny Lau (Apr 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196674):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">uu</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">}),</span> <span class="n">f</span> <span class="n">uu</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃₀</span><span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">hz</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">hz</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">hz</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196676):
<p>splitting into two implications ^</p>

#### [ Kevin Buzzard (Apr 17 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125204693):
<p>so to prove <code>X -&gt; Y</code> using simp, you intro h and then <code>simpa using h</code>?</p>

#### [ Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125204786):
<p>right</p>

#### [ Kevin Buzzard (Apr 17 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125205075):
<p>This trick is sufficiently important that it should be mentioned in the simp docs.</p>


{% endraw %}
