---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96209canonicalringhomfrominttoR.html
---

## Stream: [maths](index.html)
### Topic: [canonical ring hom from int to R](96209canonicalringhomfrominttoR.html)

---


{% raw %}
#### [ Johan Commelin (Jul 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130132971):
<p>Does the canonical ring homomorphism from <code>int</code> to a ring <code>R</code> already have a name in Lean?</p>

#### [ Kenny Lau (Jul 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130132977):
<p>something something <code>int.coe</code></p>

#### [ Mario Carneiro (Jul 23 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130132982):
<p><code>int.cast</code></p>

#### [ Johan Commelin (Jul 23 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130133232):
<p>Aah, of course. And do we already know that this is a ring hom?</p>

#### [ Kenny Lau (Jul 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130133599):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">instance</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast</span><span class="bp">.</span><span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">cast</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_add</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span>
  <span class="n">map_one</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130133600):
<p>now you know</p>

#### [ Johan Commelin (Jul 23 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130135077):
<p>(Sorry, I got distracted by other stuff.) Anyway, I'm not surprised that it is a 4-liner. It is just that I don't know how to figure out if this is somewhere in mathlib or not...</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130135209):
<p>it is not, but kenny is pointing out that all the theorems are already there</p>

#### [ Kevin Buzzard (Jul 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130135926):
<blockquote>
<p>(Sorry, I got distracted by other stuff.) Anyway, I'm not surprised that it is a 4-liner. It is just that I don't know how to figure out if this is somewhere in mathlib or not...</p>
</blockquote>
<p>You can check to see if Lean's type class inference system already knows a fact by seeing if you can prove it with <code>by apply_instance</code>. Of course this does not tell you whether the proof is in mathlib in a file you didn't import yet...</p>

#### [ Johan Commelin (Jul 23 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130136073):
<p>True, I keep forgetting that trick.</p>

#### [ Kevin Buzzard (Jul 23 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130137120):
<p>I used it extensively over the weekend in the middle of code just to make sure that type class inference was keeping up with what I was trying to do</p>

#### [ Kevin Buzzard (Jul 23 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/canonical%20ring%20hom%20from%20int%20to%20R/near/130137155):
<p>Just debugging lines which I'd delete after, checking my quotient group instances were working</p>


{% endraw %}
