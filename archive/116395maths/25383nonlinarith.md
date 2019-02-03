---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/25383nonlinarith.html
---

## Stream: [maths](index.html)
### Topic: [nonlinarith](25383nonlinarith.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 29 2019 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157066131):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">hc</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">hd</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span>
<span class="o">(</span><span class="n">hA</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hB</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hC</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">hD</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">C</span> <span class="bp">*</span> <span class="n">D</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>How am I supposed to be solving goals like this? Is there a tactic that Coq has which can just do this? I think that if I were to ask an undergrad they'd say it was "obvious".</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157066189):
<p>[in my use case a,b,c,d are all of the form <code>|x|</code>]</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157066209):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">hc</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">hd</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span>
<span class="o">(</span><span class="n">hA</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hB</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hC</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">hD</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">C</span> <span class="bp">*</span> <span class="n">D</span> <span class="o">:=</span>
<span class="k">calc</span>
<span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">mul_le_mul_of_nonneg_right</span> <span class="n">hA</span> <span class="n">hb</span><span class="o">)</span> <span class="bp">_</span>
<span class="bp">...</span>           <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="n">add_le_add_right</span> <span class="o">(</span><span class="n">mul_le_mul_of_nonneg_left</span> <span class="n">hB</span> <span class="o">(</span><span class="n">le_trans</span> <span class="n">ha</span> <span class="n">hA</span><span class="o">))</span> <span class="bp">_</span>
<span class="bp">...</span>           <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">C</span> <span class="bp">*</span> <span class="n">d</span> <span class="o">:</span> <span class="n">add_le_add_left</span> <span class="o">(</span><span class="n">mul_le_mul_of_nonneg_right</span> <span class="n">hC</span> <span class="n">hd</span><span class="o">)</span> <span class="bp">_</span>
<span class="bp">...</span>           <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">C</span> <span class="bp">*</span> <span class="n">D</span> <span class="o">:</span> <span class="n">add_le_add_left</span> <span class="o">(</span><span class="n">mul_le_mul_of_nonneg_left</span> <span class="n">hD</span> <span class="o">(</span><span class="n">le_trans</span> <span class="n">hc</span> <span class="n">hC</span><span class="o">))</span> <span class="bp">_</span>
</pre></div>


<p>I'm assuming this is golfable...</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157066256):
<p>I just tried goofing around with <code>apply_rules</code> but I'm a first-timer.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157066310):
<p>Does <code>mono</code> help?</p>

#### [ Reid Barton (Jan 29 2019 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157066943):
<p><code>by mono* with [0 ≤ A, 0 ≤ C]; linarith</code></p>

#### [ Reid Barton (Jan 29 2019 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067007):
<p>actually it works even without the <code>with</code> part</p>

#### [ Reid Barton (Jan 29 2019 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067114):
<p>Kind of weird that <code>mono</code> can't deduce <code>0 ≤ A</code> from <code>0 ≤ a</code> and <code>a ≤ A</code> itself</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067256):
<p>Right -- I was trying </p>
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="n">mono_rules</span><span class="o">]</span> <span class="n">add_le_add_right</span> <span class="n">add_le_add_left</span>
<span class="n">mul_le_mul_of_nonneg_right</span> <span class="n">mul_le_mul_of_nonneg_left</span> <span class="n">le_trans</span>
</pre></div>


<p>and then <code>by apply_rules mono_rules</code> but the <code>le_trans</code> makes it loop, and without it it can't do it.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067383):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span>
<span class="o">(</span><span class="n">hA</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hB</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hC</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">hD</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:</span>
<span class="n">abs</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">abs</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">abs</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">abs</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">C</span> <span class="bp">*</span> <span class="n">D</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Maybe this one is harder. How do I insert the <code>abs</code> into the picture? Note <code>abs_nonneg : ∀ (a : ?M_1), abs a ≥ 0</code></p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067630):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">linarith</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span>
<span class="o">(</span><span class="n">hA</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hB</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hC</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">hD</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:</span>
<span class="n">abs</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">abs</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">abs</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">abs</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">A</span> <span class="bp">*</span> <span class="n">B</span> <span class="bp">+</span> <span class="n">C</span> <span class="bp">*</span> <span class="n">D</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">a</span> <span class="bp">≥</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">abs_nonneg</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">b</span> <span class="bp">≥</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">abs_nonneg</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">c</span> <span class="bp">≥</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">abs_nonneg</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">d</span> <span class="bp">≥</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">abs_nonneg</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">mono</span><span class="bp">*;</span><span class="n">linarith</span>
<span class="kn">end</span>
</pre></div>


<p>Is there a better way of inserting <code>abs_nonneg</code> into the picture?</p>

#### [ Reid Barton (Jan 29 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067643):
<p>That's basically what I was about to write except with <code>have := abs_nonneg a</code>, etc.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067720):
<p>Still, this is much better than what I had!</p>

#### [ Reid Barton (Jan 29 2019 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067721):
<p>I don't know if we have enough smarts to figure out to prove 0 &lt;= A from the assumption abs a &lt;= A and the lemma 0 &lt;= abs a</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067727):
<p><code>by undergrad</code></p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067807):
<p>Thanks Reid, by the way! The more my code looks like how a maths undergraduate thinks, the better it is. I don't think they're thinking about <code>mul_le_mul_of_nonneg_right</code>, at least not explicitly.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067812):
<p>It's just "obvious".</p>

#### [ Reid Barton (Jan 29 2019 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067821):
<p>I had never tried out <code>mono</code> before so this was also enlightening for me</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067827):
<p>Well thanks <span class="user-mention" data-user-id="110031">@Patrick Massot</span> too.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157067912):
<p><a href="#narrow/stream/116395-maths/topic/linarith.20failure/near/157061326" title="#narrow/stream/116395-maths/topic/linarith.20failure/near/157061326">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/linarith.20failure/near/157061326</a></p>

#### [ Johan Commelin (Jan 29 2019 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157086362):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Can't you ask some former IMO participant to write a tactic that solves IMO-style inequalities? There are probably some among Imperial's first and second year students...<br>
It would be cool if we have all the mean inequalities, and Chebyshev, Jensen, etc...</p>

#### [ Kevin Buzzard (Jan 29 2019 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nonlinarith/near/157087191):
<p>Yeah, we should tell Rob to add them to linarith :-) I am not sure how far you can get knowing all of those standard "IMO syllabus" inequalities, it always seemed to me that even if you knew them all you still needed more ideas to prove a random IMO inequality.</p>


{% endraw %}
