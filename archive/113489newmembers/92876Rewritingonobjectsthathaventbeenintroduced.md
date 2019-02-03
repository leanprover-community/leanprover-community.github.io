---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/92876Rewritingonobjectsthathaventbeenintroduced.html
---

## Stream: [new members](index.html)
### Topic: [Rewriting on objects that haven't been introduced](92876Rewritingonobjectsthathaventbeenintroduced.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147983997):
<p>I have the following term in my goal:</p>
<div class="codehilite"><pre><span></span><span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="o">((</span><span class="n">f</span> <span class="bp">+</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">-</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">g&#39;</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="n">h</span><span class="o">)</span> <span class="bp">/</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">+</span> <span class="mi">0</span><span class="o">))</span>
</pre></div>


<p>And want to rewrite <code>pi.add_apply</code> to the <code>(f + g) (x + h)</code> term. But I can't, since <code>h</code> is not really a variable. Is there any way to work with rewrites on <code>h</code> without introducing everything before it?</p>

#### [ Patrick Massot (Nov 19 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984304):
<p><code>simp</code> can do it</p>

#### [ Patrick Massot (Nov 19 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984323):
<p>Try <code>simp only [pi.add_apply]</code></p>

#### [ Patrick Massot (Nov 19 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984354):
<p>In this case it's probably definitionaly true, so you could probably also use <code>change</code></p>

#### [ Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984402):
<p>Ok, sure, that works here -- but in a situation where the rewrite can't be done with <code>simp</code> (e.g. if it involves <code>\l</code>), is there a more general solution? I mean, what is <code>simp</code> actually using behind the scenes?</p>

#### [ Patrick Massot (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984408):
<p>something like <code>tendsto (λ (h : ℝ), (f (x + h) + g (x + h) - (f x + g x) - (f' x + g' x) * h) / h) (nhds 0) (nhds (0 + 0))</code></p>

#### [ Patrick Massot (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984423):
<p><code>conv</code> can be the answer</p>

#### [ Patrick Massot (Nov 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984435):
<p>but <code>simp</code> can also go under binders sometimes</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984444):
<p>Hm, hadn't heard of <code>conv</code>. Interesting.</p>

#### [ Patrick Massot (Nov 19 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984465):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md</a></p>

#### [ Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984520):
<p>One more question -- to get the goal in the form above with <code>nhds(0 + 0)</code> and stuff, I couldn't just use a simple rewrite <code>rw ←zero_add</code>, because <code>rw</code> becomes too overzealous and turns both <code>0</code>s to <code>0+0</code> (instead I had to <code>have</code> a statement that the new goal implies the old goal and prove that by <code>rw zero_add</code>). Is there any way to gain some control over the rewrite and make it transform things one at a time?</p>

#### [ Patrick Massot (Nov 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984625):
<p>See <a href="#narrow/stream/113488-general/topic/rewrite_cfg" title="#narrow/stream/113488-general/topic/rewrite_cfg">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg</a> and also the <code>conv</code> doc I mentioned in my previous answer</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Rewriting%20on%20objects%20that%20haven%27t%20been%20introduced/near/147984664):
<p>Thanks, I'll have a look at it.</p>


{% endraw %}
