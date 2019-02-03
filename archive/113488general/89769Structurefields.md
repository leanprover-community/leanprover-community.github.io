---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89769Structurefields.html
---

## Stream: [general](index.html)
### Topic: [Structure fields](89769Structurefields.html)

---


{% raw %}
#### [ Sebastien Gouezel (Nov 07 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146965379):
<p>Is there a quick way to unfold something defined in a class? Let me be more specific. The product of metric spaces starts with</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">prod</span><span class="bp">.</span><span class="n">metric_space_max</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">dist</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">max</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
<span class="bp">......</span><span class="o">}</span>
</pre></div>


<p>Now, in a proof, I have <code>dist x y</code> where <code>x</code> and <code>y</code> are in a product metric space, and I would like to unfold it to <code>max (dist x.1 y.1) (dist x.2 y.2)</code>. <br>
I can <code>change</code> it, or use <code>show</code>, or prove a lemma giving the formula for the distance (with <code>rfl</code>) and then unfold this lemma. But I am wondering if I am missing something and if there is something I can just unfold, like <code>prod.metric_space_max._secret_access_to_dist_</code> or something like that.</p>

#### [ Johannes Hölzl (Nov 07 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146967395):
<p>I don't think so. you can unfold <code>prod.metric_space_max</code>, and then call <code>dsimp</code> to unfold the projection. But this will not work in general. The best thing to do is to add the lemma as a <code>simp</code>-rule (which we should have anyway)</p>

#### [ Sebastian Ullrich (Nov 07 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146968934):
<p>Does <code>simp [dist]</code> not work? Or do you want to unfold only this specific <code>dist</code>?</p>

#### [ Sebastien Gouezel (Nov 07 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969406):
<p>No, simp does not work here:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">prod</span><span class="bp">.</span><span class="n">dist_eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">dist</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">max</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">dist</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>


<p>fails with</p>
<div class="codehilite"><pre><span></span>simplify tactic failed to simplify
</pre></div>


<p>I have proved the lemma using <code>rfl</code>, and then used it explicitly later. This seems to be the canonical way to proceed. By the way, this is not the kind of thing I would want to unfold all the time, so I don't think it is a good simp lemma (but it is definitely useful to have it in explicit form like this)</p>

#### [ Sebastian Ullrich (Nov 07 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969573):
<p>You have to pass the projection explicitly: <code>simp [dist]</code></p>

#### [ Sebastien Gouezel (Nov 07 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969749):
<p>Sorry, I should learn to read. Yes, <code>simp [dist]</code> works. Can you explain why?</p>

#### [ Sebastian Ullrich (Nov 07 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969913):
<p><code>simp</code> accepts not just rewrite lemmas but also function and projection names, which tell it to unfold usages of them</p>

#### [ Sebastien Gouezel (Nov 07 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146970400):
<p>OK, thanks (and this is very useful, I don't know why I never noticed this)</p>

#### [ Kevin Buzzard (Nov 07 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146970867):
<p>Oh nice trick Sebastian! I thought that the philosophy was to always prove these lemmas and give them names. Wait -- maybe that is the philosophy anyway.</p>

#### [ Floris van Doorn (Nov 07 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146971122):
<p>I also didn't know this. This is very useful!</p>


{% endraw %}
