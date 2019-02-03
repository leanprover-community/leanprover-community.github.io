---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51149Dependenttypes.html
---

## Stream: [general](index.html)
### Topic: [Dependent types](51149Dependenttypes.html)

---


{% raw %}
#### [ Sebastien Gouezel (Jan 31 2019 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300084):
<p>Suppose that I have two natural numbers <code>n</code> and <code>m</code>, and a proof that they are equal <code>h : n = m</code>. I have essentially never needed dependent types, but here I really have to deal with them and define the identity map from <code>fin n</code> to <code>fin m</code>. Can someone help with this? (I am in tactic mode, if that matters).</p>

#### [ Johannes Hölzl (Jan 31 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300169):
<p>use <code>fin.cast</code></p>

#### [ Johannes Hölzl (Jan 31 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300195):
<p>The important thing is that it copies the contained value, so when projecting it you don't have an <code>rw</code> in your data</p>

#### [ Simon Hudon (Jan 31 2019 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300289):
<p>If you're in tactic mode, you may have better result if you call <code>subst n</code> first.</p>

#### [ Simon Hudon (Jan 31 2019 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300307):
<p>Then you don't need <code>cast</code></p>

#### [ Simon Hudon (Jan 31 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300422):
<p>Here's my thinking when considering using <code>cast</code>:</p>
<ul>
<li>try to avoid cast</li>
<li>try harder</li>
<li>are you sure it doesn't work</li>
<li>hide cast as far from public view as possible</li>
</ul>

#### [ Sebastien Gouezel (Jan 31 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157300891):
<p><code>fin.cast</code> uses the specifics of<code>fin</code> if I look at the definition. I am more looking for the syntax for the more general situation where you have dependent types <code>C k</code>, a proof that <code>k = l</code>, and want to define the identity from <code>C k</code> to <code>C l</code> starting from the identity from <code>C k</code> to <code>C k</code> (which is the same map, but I don't how to convince lean of this). How would I use <code>cast</code> or <code>subst</code> in such a situation? (I never used any of them, so I don't know what they are supposed to do, or their syntax!)</p>

#### [ Johannes Hölzl (Jan 31 2019 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157301046):
<p>You can use <code>eq.rec</code>. But be very careful, it is usually a bad idea to do computation under it</p>

#### [ Reid Barton (Jan 31 2019 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157301254):
<p>But note that all of the general-purpose alternatives like the <code>subst</code> and <code>rw</code> tactics are also going to use <code>eq.rec</code> under the hood.</p>

#### [ Neil Strickland (Jan 31 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157301465):
<p>In some sense the "obvious" thing to do is is as follows: given <code>h : k = l</code> you have <code>congr_arg C h : C k = C l</code> and <code>cast (congr_arg C h) : C k -&gt; C l</code>.  But this approach leads to a lot of awkwardness.  It is common that you have some data combined with some properties, and you can define a map that just applies <code>cast</code> to the properties while leaving the data alone.  This is what <code>fin.cast</code> does.  It generally works much better because of proof irrelevance: any two proofs of the same proposition are considered the same, so you don't need to worry about what exactly the cast did.</p>

#### [ Reid Barton (Jan 31 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157302017):
<p>The issue is that in a situation like</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">i</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">m</span><span class="o">)</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">e</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">mk</span> <span class="n">i</span> <span class="n">h</span><span class="o">)</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">m</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span>
</pre></div>


<p>this expression is not definitionally equal to <code>i</code>, even though you can prove that it is equal to <code>i</code>.</p>

#### [ Sebastien Gouezel (Jan 31 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependent%20types/near/157302210):
<p>OK, thanks a lot for your explanations. Definitional equality is really useful for me here, so I will go for <code>fin.cast</code> as advocated by Johannes, but I have learnt a lot!</p>


{% endraw %}
