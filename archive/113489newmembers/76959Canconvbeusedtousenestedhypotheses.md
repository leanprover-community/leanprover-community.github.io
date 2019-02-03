---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/76959Canconvbeusedtousenestedhypotheses.html
---

## Stream: [new members](index.html)
### Topic: [Can conv be used to use nested hypotheses?](76959Canconvbeusedtousenestedhypotheses.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150884801):
<p>The situation is as follows: I have a proof of:</p>
<div class="codehilite"><pre><span></span><span class="n">convertor</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
    <span class="n">h</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">))</span> <span class="bp">-</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">h</span><span class="o">))</span> <span class="bp">/</span> <span class="n">h</span> <span class="bp">=</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">))</span> <span class="bp">-</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">h</span><span class="o">))</span> <span class="bp">/</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">/</span> <span class="n">h</span>
</pre></div>


<p>And I have the following goal in which I need to perform a rewrite using <code>convertor</code>:</p>
<div class="codehilite"><pre><span></span><span class="bp">∀</span> <span class="o">(</span><span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
    <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span>
    <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">δ</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">δ</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span>
       <span class="bp">∀</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
         <span class="n">h</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">abs</span> <span class="n">h</span> <span class="bp">&lt;</span> <span class="n">δ</span> <span class="bp">→</span> <span class="n">abs</span> <span class="o">((</span><span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">))</span> <span class="bp">-</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="o">))</span> <span class="bp">/</span> <span class="n">h</span> <span class="bp">-</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">f&#39;</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="n">g&#39;</span> <span class="n">x</span><span class="o">)</span> <span class="n">x</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span>
</pre></div>


<p>Within the goal, we have the nested hypothesis <code> ∀ (h : ℝ), h ≠ 0</code> which is needed to apply <code>convertor</code>. But I can't perform this rewrite without unfolding everything.</p>

#### [ Kenny Lau (Dec 04 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150884874):
<p><code>simp only [convertor]</code></p>

#### [ Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885042):
<p>Doesn't work.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885084):
<p>Oh wait, there's a typo in my convertor -- nope, still doesn't work.</p>

#### [ Kenny Lau (Dec 04 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885093):
<p><code>simp only [convertor] {contextual:=tt}</code></p>

#### [ Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885178):
<p>Still doesn't work.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885310):
<p>What exactly would <code>simp</code> be doing behind the scenes here? Something involving <code>conv</code>? Or something else? Is there any way that I can dig into it the way <code>simp</code> is supposed to work?</p>

#### [ Kevin Buzzard (Dec 04 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150885899):
<p>See if forall h, h ne 0 -&gt; X = Y can ever be used to rewrite forall h, h ne 0 -&gt; something else -&gt; X = Z maybe?  I mean do some experiments. If the rewrite never works you could ask on #general...oh, I just noticed that you're asking on the main chat anyway :-) sorry.</p>

#### [ Patrick Massot (Dec 05 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150912877):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> this is typically a case where you need to paste a MWE if you really want help. Reluctant rewriting is a complicated topic, and the answer very much depends on the specific situation. Meanwhile you can learn a couple of important lessons:</p>

#### [ Patrick Massot (Dec 05 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150912960):
<p>When using Lean, you need to reconsider every side assumption. They will be a pain, whatever the situation, and we have all sorts of tricks to avoid them. One of Kevin's favorite ones is how division is totalized. You convertor lemma (without typos) does not need assumptions, thanks to the division trick:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">convertor</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">):</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
     <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">))</span> <span class="bp">-</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="o">))</span> <span class="bp">/</span> <span class="n">h</span> <span class="bp">=</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">))</span> <span class="bp">-</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="o">))</span> <span class="bp">/</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">/</span> <span class="n">h</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">H</span> <span class="o">:</span> <span class="n">g</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">H</span><span class="o">,</span> <span class="n">mul_zero</span><span class="o">,</span> <span class="n">zero_div</span><span class="o">,</span> <span class="n">eq_of_sub_eq_zero</span> <span class="n">H</span><span class="o">,</span> <span class="n">sub_self</span><span class="o">,</span> <span class="n">zero_div</span><span class="o">]</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rwa</span> <span class="n">div_mul_cancel</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Dec 05 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150913069):
<p>The other lesson is that you shouldn't be doing all those computations, you should have better infrastructure. This is why I should be working on the big-O/little-o library, but I don't have enough time (but maybe you don't know yet <a href="https://en.wikipedia.org/wiki/Big_O_notation" target="_blank" title="https://en.wikipedia.org/wiki/Big_O_notation">this technology</a>)</p>

#### [ Kenny Lau (Dec 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150914237):
<p>well I find it useful that <code>f</code> is differentiable at <code>p</code> iff <code>f(p+h) = f(p) + h f1(h)</code> for some <code>f1</code> continuous at <code>0</code> with <code>f1(0) = f'(p)</code>. Chain rule follows immediately:<br>
1. <code>for all h, f(p+h) = f(p) + h f1(h)</code> with <code>f1</code> continuous and <code>f1(0) = f'(p)</code><br>
2. <code>for all h, g(f(p)+h) = g(f(p)) + h g1(h)</code> with <code>g1</code> continuous and <code>g1(0) = g'(f(p))</code><br>
3. <code>for all h, g(f(p+h)) = g(f(p) + h f1(h)) = g(f(p)) + h f1(h) g1(h f1(h))</code>, and then <code>f1(h) g1(h f1(h))</code> is continuous at <code>0</code>, and also <code>f1(0) g1(0 f1(0)) = f'(p) g'(f(p))</code></p>

#### [ Patrick Massot (Dec 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150915954):
<p>We already discussed that trick here. What you wrote is the full extent of what it can do, and you'll have to prove this is equivalent to the usual definition (which is more convenient for everything else) anyway, so the gain is not even that large.</p>

#### [ Patrick Massot (Dec 05 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150916063):
<p>Of course all this (the explicit computation with quotient and the exotic definition of derivatives) is perfectly fine for experimentation purposes, what I'm describing is the library building point of view</p>

#### [ Kevin Buzzard (Dec 05 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150919265):
<p>Abhi is (perhaps at my suggestion) working on a simple library for differentiating functions of one real variable. I know that others have promised some much better things, but Abhi is a first year undergraduate and we are just experimenting and learning as we go. Does anyone know how this stuff is done in Coq, or any other system which implements dependent type theory in pretty much the same general way as Lean? In fact, which other systems have this property? I'm sure Isabelle will have this stuff, but my understanding is that Isabelle has a very different kind of type theory. How do I go about finding out how this stuff is implemented in Coq? Is it easiest to just ask on some Coq mailing list? Is <a href="https://github.com/coq-contribs" target="_blank" title="https://github.com/coq-contribs">https://github.com/coq-contribs</a> any use? I would like to know more about what has been done before. Is Coq the only system that is similar enough to Lean to make a comparison worthwhile?</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 05 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150920025):
<blockquote>
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> this is typically a case where you need to paste a MWE if you really want help. Reluctant rewriting is a complicated topic, and the answer very much depends on the specific situation. Meanwhile you can learn a couple of important lessons:</p>
</blockquote>
<p>Thanks <span class="user-mention" data-user-id="110031">@Patrick Massot</span> -- I tried using <code>ring</code> and it didn't work, so I decided that the division by zero trick didn't work for some reason. I would've posted an MWE, but it was a bit large -- I'll try the experiments <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> suggested to get a better feel of contextual rewrites.</p>

#### [ Patrick Massot (Dec 05 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150927121):
<p>As I wrote, I know this is only experimentation, but I hope it's still useful to have information from the library point of view. The chain rule in Coq is at <a href="https://github.com/math-comp/analysis/blob/master/derive.v#L699-L702" target="_blank" title="https://github.com/math-comp/analysis/blob/master/derive.v#L699-L702">https://github.com/math-comp/analysis/blob/master/derive.v#L699-L702</a>. I think Isabelle is already a bit too different for comparing here.</p>

#### [ Patrick Massot (Dec 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%20conv%20be%20used%20to%20use%20nested%20hypotheses%3F/near/150927255):
<p>Well, it's more honest to point to <a href="https://github.com/math-comp/analysis/blob/master/derive.v#L687-L697" target="_blank" title="https://github.com/math-comp/analysis/blob/master/derive.v#L687-L697">https://github.com/math-comp/analysis/blob/master/derive.v#L687-L697</a></p>


{% endraw %}
