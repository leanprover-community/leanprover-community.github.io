---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/13714howtousethepowaddtheorem.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [how to use the pow_add theorem](https://leanprover-community.github.io/archive/116395maths/13714howtousethepowaddtheorem.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Truong Nguyen (Sep 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225323):
<p>Dear Alls,<br>
The pow_add theorem is as follow:</p>
<p>#check pow_add<br>
pow_add : ∀ (a : ?M_1) (m n : ℕ), a ^ (m + n) = a ^ m * a ^ n</p>
<p>By why can't I prove the consequence theorem: </p>
<p>theorem th01 (a: ℕ ): ∀ m n:ℕ, a ^ (m + n) = (a ^ m) * (a ^ n) :=<br>
begin<br>
rw pow_add (a:ℕ)<br>
end</p>
<p>Here is the error that I got:</p>
<p>rewrite tactic failed, did not find instance of the pattern in the target expression<br>
  a ^ (?m_1 + ?m_2)<br>
Thank you,</p>

#### [ Kenny Lau (Sep 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225393):
<p>(deleted)</p>

#### [ Chris Hughes (Sep 02 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225436):
<p>It's because you need to use <code>nat.pow_add</code></p>

#### [ Kenny Lau (Sep 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225444):
<p>because the <code>^</code> are different</p>

#### [ Mario Carneiro (Sep 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225445):
<p><code>nat</code> has a different instance for the power function, so it has its own theorems to go with it, like <code>nat.pow_add</code></p>

#### [ Chris Hughes (Sep 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225446):
<p>This is a very annoying feature of current lean. There are two definitions of <code>pow</code> on the naturals.</p>

#### [ Mario Carneiro (Sep 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225489):
<p>If <code>nat.pow_add</code> was not proven, you could also use <code>by simpa using pow_add a</code> to prove it</p>

#### [ Truong Nguyen (Sep 02 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225601):
<p>Dear Mario,<br>
can you be more specific, what is  <code>by simpa using pow_add a</code>.</p>

#### [ Truong Nguyen (Sep 02 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225696):
<p>I changed to this:</p>
<p>theorem th01 (a: ℕ ): ∀ m n:ℕ, a ^ (m + n) = (a ^ m) * (a ^ n) :=<br>
begin<br>
rw [nat.pow_add (a:ℕ )]<br>
end</p>
<p>But, it did not work neither.</p>

#### [ Mario Carneiro (Sep 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225757):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">theorem</span> <span class="n">th01</span> <span class="o">(</span><span class="n">a</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">m</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">pow_add</span> <span class="n">a</span> <span class="n">m</span> <span class="n">n</span>
</pre></div>

#### [ Mario Carneiro (Sep 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225765):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">th01</span> <span class="o">(</span><span class="n">a</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">m</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_add</span>
</pre></div>

#### [ Mario Carneiro (Sep 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225767):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">th01</span> <span class="o">(</span><span class="n">a</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">m</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">pow_add</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
</pre></div>

#### [ Mario Carneiro (Sep 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133225813):
<p>note that you need to have all the variables left of the colon for <code>rw</code> to work here</p>

#### [ Truong Nguyen (Sep 02 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133226550):
<p>Oh, great<br>
Do you know how can I find the tutorial of using "simpa".</p>
<p>I have the following issue as well. I think it can be done in similar way.</p>
<p>How to use the theorem:<br>
#check cardinal.mul_power <br>
cardinal.mul_power : (?M_1 * ?M_2) ^ ?M_3 = ?M_1 ^ ?M_3 * ?M_2 ^ ?M_3</p>
<p>To prove that:<br>
theorem th07 (a b n: \N): (a * b)^n = a ^n*b^n.</p>

#### [ Mario Carneiro (Sep 02 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133226706):
<p>That is an unrelated use of power; although it is possible it would be a weird way to prove that theorem for natural numbers</p>

#### [ Mario Carneiro (Sep 02 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133226715):
<p>the theorem itself is <code>nat.mul_pow</code></p>

#### [ Truong Nguyen (Sep 02 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133226815):
<p>when I run the command:<br>
#check nat.mul_pow</p>
<p>it gave me nothing.</p>

#### [ Patrick Massot (Sep 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133227003):
<p>you need to import <a href="https://github.com/leanprover/mathlib/blob/dd0c0aeefcaf6a438ab4273d7a1f42e1b8225847/data/nat/basic.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/dd0c0aeefcaf6a438ab4273d7a1f42e1b8225847/data/nat/basic.lean">https://github.com/leanprover/mathlib/blob/dd0c0aeefcaf6a438ab4273d7a1f42e1b8225847/data/nat/basic.lean</a></p>

#### [ Patrick Massot (Sep 02 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133227007):
<p><code>import data.nat.basic</code></p>

#### [ Truong Nguyen (Sep 03 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133268897):
<p>Hello,<br>
do you know where can I find the tutorial of using "simpa".</p>

#### [ Patrick Massot (Sep 03 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133268911):
<p>I think we don't have anything better than <a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa</a></p>

#### [ Truong Nguyen (Sep 03 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20use%20the%20pow_add%20theorem/near/133270921):
<p>Oh, thank you</p>


{% endraw %}
