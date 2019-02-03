---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23550listmapwithpi.html
---

## Stream: [new members](index.html)
### Topic: [list.map with pi](23550listmapwithpi.html)

---


{% raw %}
#### [ Gavid Liebnich (Nov 09 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147355746):
<p>Hello. I have an issue using dependent function space in conjunction with <code>list.map</code>. Could anyone take a peek?<br>
In the following state:</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">g</span> <span class="n">g&#39;</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">α</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g&#39;</span>
<span class="err">⊢</span> <span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">g</span><span class="o">}),</span> <span class="n">f</span> <span class="o">(</span><span class="n">c</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">attach</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="n">nil</span>
</pre></div>


<p>I would like to rewrite <code>g</code> with <code>g'</code>. However, I get "motive is not type correct" error.<br>
I <em>think</em> I understand why this is. Given <code>c.2</code> is supposed to be <code>x ∈ g</code>, I would end up with mismatching types as <code>attach g'</code> would lead to <code>c.2</code> being <code>x ∈ g'</code>.<br>
However, I am not sure how to proceed - I think I need some kind of a congruence that says I can switch <code>map f l</code> for <code>map f' l'</code> if I can show <code>f = f'</code> and <code>l = l'</code>, but "modulo types".<br>
You can reconstruct the goal (and the error) with:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="n">g&#39;</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">g</span><span class="o">),</span> <span class="n">α</span><span class="o">}</span>
<span class="n">def</span> <span class="n">foo</span> <span class="o">:=</span> <span class="n">map</span> <span class="o">(</span><span class="bp">λ</span><span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">g</span><span class="o">}),</span> <span class="n">f</span> <span class="n">c</span><span class="bp">.</span><span class="mi">1</span> <span class="n">c</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="n">attach</span> <span class="n">g</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g&#39;</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">foo</span> <span class="n">α</span> <span class="n">g</span> <span class="n">f</span> <span class="bp">=</span> <span class="o">[]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">foo</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">h</span> <span class="c1">-- motive not type correct</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Nov 09 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147356172):
<p>Is <code>g</code> a variable? If so, <code>subst g</code> is probably the easiest thing</p>

#### [ Gavid Liebnich (Nov 09 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147356421):
<p>I am not sure I know what variable means in this context, but <code>g</code> is a list computed by a function, so I think it is not. The equivalence <code>h : g = g'</code> basically expands <code>bar x y</code> to <code>x :: bar x' y</code>. I've tried <code>subst expand_bar</code>, but the "given expression is not a local constant".</p>

#### [ Gavid Liebnich (Nov 09 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147356591):
<p>Definitely not a variable, come to think of it, <code>h : g = g'</code> is just <code>h : expand_bar a b = a :: expand_bar a' b</code>. And I don't think I can <code>subst expand_bar</code>.</p>

#### [ Mario Carneiro (Nov 09 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147357025):
<p>I think you need to unsimplify your example then. This is generally speaking a complicated problem with nonuniform solutions, I would have to know more about the problem to say how to proceed</p>

#### [ Gavid Liebnich (Nov 09 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147357098):
<p>I will give it a try, thanks. I did a lot of simplifying, may have lost something along the way :).</p>

#### [ Patrick Massot (Nov 09 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147357269):
<p>The <code>subst</code> tactic (instead of <code>rw</code>) may help you</p>

#### [ Floris van Doorn (Nov 10 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147436293):
<p>I don't know if this works in your actual example, but you could try reverting everything which depends on <code>g</code>:</p>
<div class="codehilite"><pre><span></span>example (h : g = g&#39;) : @foo α g f = [] :=
begin
  unfold foo,
  revert f,
  rw h,
  intro f
end
</pre></div>

#### [ Floris van Doorn (Nov 10 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/list.map%20with%20pi/near/147436358):
<p>Note that this <code>rw</code> now also rewrites the type of <code>f</code>.</p>


{% endraw %}
