---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/19335module.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [module](https://leanprover-community.github.io/archive/116395maths/19335module.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 23 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227117):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Shouldn't this be flipped, for consistency with <code>comp</code> and <code>llcomp</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lcomp</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span><span class="o">)</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span> <span class="o">:=</span> <span class="bp">_</span> <span class="c1">-- I would expect:   def lcomp (f : N →ₗ P) : (M →ₗ N) →ₗ M →ₗ P :=</span>
</pre></div>

#### [ Mario Carneiro (Nov 23 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227175):
<p>maybe, but the other direction is harder</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227185):
<p>there is an order to the definitions</p>

#### [ Johan Commelin (Nov 23 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227192):
<p>Also, are there compatibilities between <code>comp</code> and <code>lcomp</code> etc...? Is <code>(lcomp f).to_fun</code> defeq to <code>f.comp</code>?</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227195):
<p>yeah, it's all defeq</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227203):
<p>it's just composition so it's easy</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227283):
<p>also there is a difference between <code>lcomp</code> that is there and the one you said</p>

#### [ Mario Carneiro (Nov 23 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148227284):
<p>one is precomposition and the other is postcomposition</p>

#### [ Johan Commelin (Nov 23 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148228046):
<p>Right, and I think the library isn't completely consistent about which one it uses for <code>comp</code>, <code>lcomp</code> and <code>llcomp</code>. Wouldn't it be easier if they were all post-composition?</p>

#### [ Mario Carneiro (Nov 23 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148228136):
<p>I mean there is a need for it, I didn't write that for no reason</p>

#### [ Mario Carneiro (Nov 23 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148228156):
<p>it's used before we have tensor products and swap and eval and such, so they aren't yet interchangeable</p>

#### [ Johan Commelin (Nov 23 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148228209):
<p>Ok, I see</p>

#### [ Johan Commelin (Nov 23 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148228225):
<p>So, may I then complain that the name is slightly confusing?</p>

#### [ Mario Carneiro (Nov 23 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148228232):
<p><code>rcomp</code> :)</p>

#### [ Johan Commelin (Nov 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/module/near/148241025):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I couldn't find where the zero linear map is defined, but apparently it is somewhere. However <code>⇑0 m</code> doesn't <code>simp</code> to <code>0</code>. Where should I add this simp rule?</p>


{% endraw %}
