---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66889lastdigitchallenge.html
---

## Stream: [maths](index.html)
### Topic: [last digit challenge](66889lastdigitchallenge.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 29 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157144680):
<p>Ali asked me about digits of nats (in base 10) today and I'm writing a little API for him, but this is a pain: </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="err">%</span> <span class="mi">10</span> <span class="bp">=</span> <span class="mi">9</span> <span class="bp">→</span> <span class="n">m</span> <span class="err">%</span> <span class="mi">10</span> <span class="bp">+</span> <span class="n">n</span> <span class="err">%</span> <span class="mi">10</span> <span class="bp">=</span> <span class="mi">9</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>These things are still far more painful than I'd like. In a 3rd year number theory class I'd even claim that this was "obvious". Should I be using ZMOD or something?</p>

#### [ Chris Hughes (Jan 29 2019 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157144787):
<p>I think this is omega.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157144873):
<p>My plan was to prove <code>(m % 10 + n % 10) % 10 = 9</code> and then do some case bash because <code>nat.mod_lt</code> says n % 10 &lt; 10. But I'm not sure how to do the case bash or prove this intermediate step.</p>

#### [ Patrick Massot (Jan 29 2019 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157144886):
<p>I think we already have that lemma</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157144936):
<p>I thought there were some lemmas like this but I can't find any that are useful to me. We have <code>(x + y * z) % y = x % y</code></p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157144948):
<p>and <code>a % n % n = a % n</code></p>

#### [ Chris Hughes (Jan 29 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145007):
<p>nat.modeq.modeq_add I believe.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145010):
<p>I'm trying to prove something for Ali so he can formalise his claimed proof that he's found the smallest positive integer which is a multiple of 91 and whose digit sum is also a multiple of 91.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145050):
<p>ooh I've not even got that imported I suspect. So I'm not using the right tools by the looks of things.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145668):
<p>Ok thanks Chris; I'm now down to <code>example (a b : ℕ) : a ≤ 9 → b ≤ 9 → (a + b) % 10 = 9 → a + b = 9 := sorry</code>; I want to do this by <code>dec_trivial</code> even though it's a bit lame; it would be better to show that a + b \le 18 and any solution to x % 10 = 9 other than 9 is &gt;= 19.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145863):
<p>now down to <code>e &lt;= 18 -&gt; e % 10 = 9 -&gt; e = 9</code></p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145922):
<p>OK I can do it with mod_add_div :-)</p>

#### [ Kevin Buzzard (Jan 29 2019 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157145924):
<p>Thanks Chris!</p>

#### [ Chris Hughes (Jan 29 2019 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157146406):
<p>If you reorder it to <code>forall a le 9, forall b le 9</code>, it's <code>dec_trivial</code></p>

#### [ Mario Carneiro (Jan 30 2019 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/last%20digit%20challenge/near/157149510):
<p>aah, please no gratuitous case bash on 10</p>


{% endraw %}
