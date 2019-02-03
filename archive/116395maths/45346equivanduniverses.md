---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45346equivanduniverses.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [equiv and universes](https://leanprover-community.github.io/archive/116395maths/45346equivanduniverses.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 29 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837442):
<p>I am interested in beefing up equiv but I am only now coming to terms with how universes work and do not yet really understand how they affect the picture if at all</p>

#### [ Kevin Buzzard (Apr 29 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837448):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">y</span> <span class="n">z</span>
<span class="n">def</span> <span class="n">αu</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span>
<span class="n">def</span> <span class="n">αuv</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span>
<span class="n">def</span> <span class="n">αv</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span>

<span class="kn">definition</span> <span class="n">u_v</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">z</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">z</span><span class="o">}</span> <span class="o">:</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">αu</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">αv</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span><span class="n">f</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span><span class="n">f</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span>
<span class="o">}</span>

<span class="kn">definition</span> <span class="n">u_uv</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">z</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">z</span><span class="o">}</span> <span class="o">:</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">αu</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">αuv</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span><span class="n">f</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span><span class="n">f</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span>
<span class="o">}</span>

<span class="kn">definition</span> <span class="n">u_uv</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">:</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">αu</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="err">\</span><span class="n">auv</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837452):
<p>the last one isn't a puzzle</p>

#### [ Kevin Buzzard (Apr 29 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837455):
<p>it unfortunately doesn't typecheck because of universe issues</p>

#### [ Kevin Buzzard (Apr 29 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125837460):
<p>Is there any way of somehow forcing it to typecheck with universe coercion or something? And then would equiv still fail?</p>

#### [ Reid Barton (Apr 29 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125838746):
<p>I guess the zeroth thing to know about universes is that <code>universe u</code> doesn't mean "Fix a universe $U$"; it just makes <code>u</code> a legal thing to put somewhere that a universe is expected.<br>
In other words, the <code>u</code> and <code>v</code>s in <code>\au</code>, <code>\auv</code>, <code>\av</code> are unrelated, and definitions <code>\au</code> and <code>\av</code> are exactly the same.</p>

#### [ Reid Barton (Apr 29 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125838886):
<p>You can think of Lean universes as corresponding to Grothendieck universes except that Lean universes are not cumulative, so that a type belongs to <code>Type u</code> for just one <code>u</code>.</p>

#### [ Reid Barton (Apr 29 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/equiv%20and%20universes/near/125839130):
<p>To "move" a type from one universe to a bigger one, use <code>ulift</code>. The new type is <code>equiv</code> to the old one (<code>equiv.ulift</code>).</p>


{% endraw %}
