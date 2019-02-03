---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58083universeparametersofinstances.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [universe parameters of instances](https://leanprover-community.github.io/archive/113488general/58083universeparametersofinstances.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jun 03 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127507965):
<p>Is this a known issue?</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">cat</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>
<span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span>

<span class="kn">section</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="c1">-- OK</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">cat</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span>

<span class="kn">section</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">cat</span> <span class="n">α</span><span class="o">]</span>
<span class="c1">-- Fails: &quot;invalid reference to undefined universe level parameter &#39;u_1&#39;&quot;</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jun 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508011):
<p>It is known in the sense that it is a design that's hard to work with.</p>

#### [ Reid Barton (Jun 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508012):
<p>It seems that the elaborator fails to gather the second universe variable of <code>cat</code></p>

#### [ Simon Hudon (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508022):
<p>If you absolutely need to use it, you need to specify the universes as <code>cat.{u v} α</code></p>

#### [ Simon Hudon (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508024):
<p>It makes it unpleasant to use though</p>

#### [ Reid Barton (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508025):
<p>That makes no difference (except the error message complains about <code>v</code> now)</p>

#### [ Reid Barton (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508032):
<p>I think this one is just a bug</p>

#### [ Simon Hudon (Jun 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508073):
<p>I don't think so. Can you try <code>cat.{v u} α</code> instead?</p>

#### [ Reid Barton (Jun 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508077):
<p>why <code>{v u}</code>?</p>

#### [ Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508082):
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span><span class="o">]</span>
<span class="c1">-- Fails: &quot;invalid reference to undefined universe level parameter &#39;v&#39;&quot;</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508083):
<p>Sometimes, the order of the universes is weird</p>

#### [ Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508090):
<p><code>{v u}</code> gives many worse errors</p>

#### [ Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508093):
<p>I think if we could just, like, <code>include</code> the universe parameter <code>v</code>, then this would work</p>

#### [ Simon Hudon (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508095):
<p>Is the error on the equality?</p>

#### [ Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508096):
<p>The error is located on the word <code>example</code></p>

#### [ Simon Hudon (Jun 03 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508130):
<p>You may need <code>cat.x.{u v} α = cat.x.{u v} α</code></p>

#### [ Simon Hudon (Jun 03 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508153):
<p>This here works for me:</p>
<div class="codehilite"><pre><span></span>section
universes u v
variables {α : Type u} [cat.{u v} α]
example : cat.x.{u v} α = cat.x α := rfl
end
</pre></div>

#### [ Reid Barton (Jun 03 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508207):
<p>That does work</p>

#### [ Simon Hudon (Jun 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508220):
<p>Can you show me an example where using two universes is necessary? Maybe I can show you a way around it</p>

#### [ Reid Barton (Jun 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508221):
<p>But, this also works</p>

#### [ Reid Barton (Jun 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508223):
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span><span class="o">]</span>
<span class="c1">-- OK</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">∧</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">})</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">rfl</span><span class="o">,</span> <span class="bp">⟨⟨⟩⟩⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jun 03 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508283):
<p>That makes sense. Every definition and theorem has an implicit list of free universe variables. The type of <code>example</code> did not mention <code>v</code> which meant that the instance of <code>cat</code> it needed was not necessarily parameterized by <code>v</code></p>

#### [ Reid Barton (Jun 03 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508285):
<p>So it really seems that the elaborator just does not understand that it ought to bind the universe variable <code>v</code></p>

#### [ Reid Barton (Jun 03 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508326):
<p>The type of <code>example</code> does mention <code>v</code> though</p>

#### [ Simon Hudon (Jun 03 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508327):
<p>I don't think I would say that it ought to.</p>

#### [ Simon Hudon (Jun 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508341):
<p>Only the versions that work</p>

#### [ Reid Barton (Jun 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508343):
<p>No, all of them</p>

#### [ Reid Barton (Jun 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508344):
<p>since they are really <code>∀ {α : Type u} [_inst_1 : cat.{u v} α], ...</code></p>

#### [ Reid Barton (Jun 03 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508386):
<p>Consider the other original working version, which did not use <code>variables</code></p>

#### [ Reid Barton (Jun 03 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508394):
<p>Its full inferred type is <code>ok.{u_1 u_2} : ∀ {α : Type u_1} [_inst_1 : cat.{u_1 u_2} α], cat.x.{u_1 u_2} α = cat.x.{u_1 u_2} α</code></p>

#### [ Simon Hudon (Jun 03 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508395):
<p><code>v</code> does not appear in it either. It is inferred</p>

#### [ Simon Hudon (Jun 03 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508442):
<p>Since it's not specified, it's found through unification. <code>v</code> starts off as a universe meta variable and <code>cat</code> and <code>cat.x</code> start off with different universe variables, we do instance resolution and then unification and then they are forced to be the same.</p>

#### [ Simon Hudon (Jun 03 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508453):
<p>The the example with <code>variable</code>, the <code>cat</code> instance already has a universe so it's not inferred during elaboration</p>

#### [ Simon Hudon (Jun 03 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508502):
<p>Universe polymorphism is a pretty nasty can of worms. Keep it to a minimum. <code>ulift</code> can help you with that.</p>

#### [ Reid Barton (Jun 03 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508514):
<p>I have to say I still don't really buy any of this!</p>

#### [ Reid Barton (Jun 03 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508554):
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">γ</span><span class="o">)</span>
<span class="c1">-- OK</span>
<span class="n">def</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">∧</span> <span class="n">nonempty</span> <span class="n">γ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">rfl</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">y</span><span class="bp">⟩⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jun 03 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508558):
<p>This is consistent with my explanation</p>

#### [ Simon Hudon (Jun 03 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508570):
<p>Think of it as matching universe levels by name.</p>

#### [ Reid Barton (Jun 03 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508627):
<p>FWIW, this is the full error message with the failing version</p>
<div class="codehilite"><pre><span></span><span class="n">kernel</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">type</span> <span class="kn">check</span> <span class="n">declaration</span> <span class="err">&#39;</span><span class="n">test&#39;</span> <span class="n">this</span> <span class="n">is</span> <span class="n">usually</span> <span class="n">due</span> <span class="n">to</span> <span class="n">a</span> <span class="n">buggy</span> <span class="n">tactic</span> <span class="n">or</span> <span class="n">a</span> <span class="n">bug</span> <span class="k">in</span> <span class="n">the</span> <span class="n">builtin</span> <span class="n">elaborator</span>
<span class="n">elaborated</span> <span class="n">type</span><span class="o">:</span>
  <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span><span class="o">],</span>
    <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">cat</span><span class="bp">.</span><span class="n">β</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">cat</span><span class="bp">.</span><span class="n">x</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">cat</span><span class="bp">.</span><span class="n">x</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span>
<span class="n">elaborated</span> <span class="n">value</span><span class="o">:</span>
  <span class="bp">λ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span><span class="o">],</span> <span class="bp">@</span><span class="n">rfl</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">cat</span><span class="bp">.</span><span class="n">β</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">cat</span><span class="bp">.</span><span class="n">x</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span>
<span class="n">nested</span> <span class="n">exception</span> <span class="n">message</span><span class="o">:</span>
<span class="n">invalid</span> <span class="n">reference</span> <span class="n">to</span> <span class="n">undefined</span> <span class="kn">universe</span> <span class="n">level</span> <span class="kn">parameter</span> <span class="err">&#39;</span><span class="n">v&#39;</span>
</pre></div>

#### [ Simon Hudon (Jun 03 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508628):
<p>In <code>cat.x</code> we don't what the universes will be so they start off as meta variables. <code>α</code> brings in universe <code>u</code> and <code>γ</code> brings in <code>v</code></p>

#### [ Reid Barton (Jun 03 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508668):
<p>So why doesn't the instance resolution of <code>cat.x</code> bring in <code>v</code>?</p>

#### [ Simon Hudon (Jun 03 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508674):
<p>Because its <code>v</code> is a local <code>v</code> to the class.</p>

#### [ Reid Barton (Jun 03 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508714):
<p>It's using this variable <code>_inst_1</code> whose type mentions <code>v</code>, and when I make it use the variables <code>γ</code> and <code>y</code> then it understands that it should bring in <code>v</code>.</p>

#### [ Simon Hudon (Jun 03 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508717):
<p>I just tried:</p>
<div class="codehilite"><pre><span></span>universes u v

class cat (α : Type u) :=
(β : Type v)
(x : β)
</pre></div>


<p>and that doesn't work either. That's weird</p>

#### [ Simon Hudon (Jun 03 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508727):
<p>Ok, I'm not sure now. Maybe <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> or <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> can come clear this up</p>

#### [ Reid Barton (Jun 03 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508833):
<p>I guess it cannot "see" the dependence on the <code>variable</code> which was used through instance resolution as easily as it can see a direct reference</p>

#### [ Reid Barton (Jun 03 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508981):
<p>Or, here is another way to look at it. Intuitively, I expect <code>variables &lt;bindings&gt;</code> to prepend <code>&lt;bindings&gt;</code> to the parameters of every definition/lemma. Well that's not quite true, I only expect bindings that are used somehow to get prepended.</p>

#### [ Reid Barton (Jun 03 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508987):
<p>Here lean obviously understands that it needs to include the <code>cat</code> instance, since otherwise there would be an error earlier about <code>cat.x</code>. But, if I just manually prepend both variables, as in the first example, then it works fine.</p>

#### [ Reid Barton (Jun 03 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127509033):
<p>aha, here is another workaround!</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">inst</span> <span class="o">:</span> <span class="n">cat</span> <span class="n">α</span><span class="o">]</span>
<span class="n">include</span> <span class="n">inst</span>
<span class="c1">-- OK</span>
<span class="n">def</span> <span class="n">ok</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">x</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Jun 03 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127509248):
<p>not very surprising that that works, but certainly a palatable workaround. Actually, this could nicely solve my "upgrading" type class issue too. Just name both instances as variables and then <code>include</code> the one you want at any given time and <code>hide</code> it when done.</p>

#### [ Scott Morrison (Jun 04 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520290):
<p>Thanks for the interesting discussion here! I've absolutely run into this in my category theory library. Unfortunately, universe issues are a pain. Unavoidably, one needs to be able to discuss "small_category", where objects and morphisms live in the same universe, and "large_category", where objects live in a universe one higher than the morphisms.</p>

#### [ Scott Morrison (Jun 04 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520333):
<p>Rather than develop these in parallel (and deal with the combinatorial explosion of functors and natural transformations going between the worlds), I've settled on the somewhat ugly solution of having a single "category", with</p>

#### [ Scott Morrison (Jun 04 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520339):
<div class="codehilite"><pre><span></span>abbreviation large_category (C : Type (u+1)) : Type (u+1) := category.{u+1 u} C
abbreviation small_category (C : Type u)     : Type (u+1) := category.{u u} C
</pre></div>

#### [ Scott Morrison (Jun 04 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520354):
<p>If you're only dealing with small or large categories (or even one of each at the same time), everything works nicely, and typeclass inference remains your friend.</p>

#### [ Scott Morrison (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520378):
<p>If you're trying to write library code that covers both cases, it is slightly ugly, and we need to specify universes explicitly and do a certain amount of "including" typeclass instances.</p>

#### [ Reid Barton (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520399):
<p>As you might have guessed, <code>cat</code> stands for your <code>category</code> class.<br>
In my so far limited use, I haven't had any issues just using <code>category</code> directly where mathematically reasonable, aside from the issue discussed in this topic, which I now have a workaround for.</p>

#### [ Scott Morrison (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520400):
<p>I have to write:</p>
<div class="codehilite"><pre><span></span>variable {C : Type u₁}
variable [𝒞 : category.{u₁ v₁} C]
variable {D : Type u₂}
variable [𝒟 : category.{u₂ v₂} D]
include 𝒞 𝒟
</pre></div>

#### [ Scott Morrison (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520402):
<p>quite often!</p>

#### [ Reid Barton (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520406):
<p>Aha, so you already discovered the <code>include</code> workaround I guess.</p>

#### [ Scott Morrison (Jun 04 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520411):
<p>(But that said, that's usually as ugly as it gets, and after those includes everything works pretty naturally.)</p>

#### [ Reid Barton (Jun 04 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127559852):
<p>Here's another, admittedly silly workaround for the issue here:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">Type₂</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">Type₂</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
</pre></div>


<p>Now the type of <code>C</code> mentions <code>v</code>, so the elaborator correctly includes <code>v</code></p>

#### [ Thang Nguyen (Jun 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779348):
<p>Hi, I am new in lean programming. I am attending to Hanoi FABS summer school 2018 and really interested in doing. <br>
My homework is formalizing the statement of Polignac Conjecture: <strong>For every even number 2n, there are infinitely many pairs of consecutive primes which differ by 2n.</strong><br>
I have formalized and wonder regarding that: </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Polignac</span> <span class="o">:</span><span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">isEven</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">p</span> <span class="n">q</span> <span class="bp">&gt;</span> <span class="n">m</span><span class="o">,</span> <span class="n">isPrime</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">isPrime</span> <span class="n">q</span> <span class="bp">∧</span> <span class="o">((</span><span class="n">p</span> <span class="bp">-</span> <span class="n">q</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">q</span> <span class="bp">-</span> <span class="n">p</span><span class="o">)</span> <span class="bp">=</span><span class="n">n</span><span class="o">)</span>
</pre></div>


<p>I need your help!</p>

#### [ Simon Hudon (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779506):
<p>Can you be a bit more specific? Why do you wonder about that definition? Or more precisely, what is giving you trouble about that definition?</p>

#### [ Patrick Massot (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779510):
<p>It would be easier to actually use n as in the informal statement (and write <code>2*n</code> where you want 2n</p>

#### [ Patrick Massot (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779524):
<p>And the disjunction at the end is unnecessary</p>

#### [ Patrick Massot (Jun 08 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779645):
<p>Note also that your attempt says nothing about p and q being consecutive</p>

#### [ Thang Nguyen (Jun 08 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779806):
<p>I need to define the statement of Polignac Conjecture. And I defined it and dont know that is okay.</p>

#### [ Thang Nguyen (Jun 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779824):
<blockquote>
<p>Note also that your attempt says nothing about p and q being consecutive</p>
</blockquote>
<p>so how to fix to p q consecutive</p>

#### [ Patrick Massot (Jun 08 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779871):
<p>What you wrote is not the correct statement, even assuming isEven and isPrime are defined</p>

#### [ Simon Hudon (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779910):
<p>You'd need to say every number between <code>p</code> and <code>q</code> is not prime. Using a different definition for that may be best</p>

#### [ Patrick Massot (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779911):
<p>You could add a condition that no natural number between p and q (p and q excluded) is prime</p>

#### [ Patrick Massot (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779916):
<p>And you don't need to have a notation for q</p>

#### [ Patrick Massot (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779926):
<p>You really want <code>n</code>, a prime <code>p</code> and asserting that <code>p+2*n</code> is also prime</p>

#### [ Patrick Massot (Jun 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779968):
<p>and there is no prime number in between</p>

#### [ Thang Nguyen (Jun 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127780320):
<p>That is correct?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Polignac</span> <span class="o">:</span><span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">n</span> <span class="n">m</span><span class="o">:</span> <span class="n">nat</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">p</span> <span class="o">:</span> <span class="n">nat</span><span class="o">,</span> <span class="n">isPrime</span> <span class="n">m</span> <span class="bp">→</span> <span class="o">(</span><span class="n">m</span> <span class="bp">=</span> <span class="n">p</span> <span class="bp">∨</span> <span class="n">m</span> <span class="bp">=</span> <span class="o">(</span><span class="n">p</span> <span class="bp">+</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="o">))</span>
</pre></div>

#### [ Patrick Massot (Jun 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127782321):
<p>No, it's not</p>

#### [ Andrew Ashworth (Jun 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127785046):
<p>today I learned about <a href="https://en.wikipedia.org/wiki/Sexy_prime" target="_blank" title="https://en.wikipedia.org/wiki/Sexy_prime">https://en.wikipedia.org/wiki/Sexy_prime</a></p>

#### [ Simon Hudon (Jun 08 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127785119):
<p>I learned that when I got married: our age is 6 apart and both of our ages were prime numbers. It's probably partly responsible for my saying yes</p>

#### [ Patrick Massot (Jun 08 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127786525):
<p>(23, 29)?</p>

#### [ Simon Hudon (Jun 08 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127786669):
<p>(31,37)</p>

#### [ Andrew Ashworth (Jun 08 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127787334):
<p>Going back to his question, I feel like you would want to define a prime gap counting function, as in wikipedia (the number of prime gaps of size n below x). Then you take the limit as x goes to infinity. Is that a standard way to formalize it?</p>

#### [ Johan Commelin (Jun 08 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127787405):
<p>Given <code>k</code>the size of the gaps, I would write: <code>\forall n, \ex p, p &gt; n \and is_prime_gap p k</code></p>

#### [ Johan Commelin (Jun 08 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127787438):
<p>And then you need to express that <code>p</code> and <code>p+k</code> have a prime gap of size <code>k</code> in <code>is_prime_gap p k : Prop</code></p>

#### [ Scott Morrison (Jun 11 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127889246):
<p><span class="user-mention" data-user-id="117668">@Thang Nguyen</span>, just a suggestion --- in zulipchat you can set the "topic" name for a conversation, and it helps organise the conversation here a lot! For example, this one could have been "help with a statement about primes".</p>


{% endraw %}
