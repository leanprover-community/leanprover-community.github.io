---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28850howtoproveoffindsimpletheorem.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [how to prove of find simple theorem](https://leanprover-community.github.io/archive/116395maths/28850howtoproveoffindsimpletheorem.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Truong Nguyen (Aug 10 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131837673):
<p>Hi everyone, I am a new user, my question is maybe too simple. Please make it lear for me.<br>
Can you tell me how to find in the library or prove the simple theorem like:</p>
<p>theorem ttt1 (n m: ℕ ) : n &lt;= m → n &lt; m ∨ n = m :=<br>
sorry</p>

#### [ Mario Carneiro (Aug 10 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131837777):
<p>the <a href="https://github.com/leanprover/mathlib/blob/master/docs/naming.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/naming.md">naming convention</a> would call that <code>lt_or_eq_of_le</code></p>

#### [ Truong Nguyen (Aug 11 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131849186):
<p>Thank you, but can you tell me how can find the stuffs like this one?</p>
<p>Is there a “search” command to find a theorem in the library?<br>
I am working in some proof, sometime, it looks me quite a lot of time to find simple theorem to use.<br>
For example, I need this one:</p>
<p>theorem tq (a b: ℕ ): ¬ a ≤ b ↔ b &lt; a :=<br>
sorry</p>
<p>Is there a way that I can find or prove it easily? I think it should be easy.<br>
Thank you,<br>
Truong</p>

#### [ Kenny Lau (Aug 11 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131849401):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">find</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="n">run_cmd</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">skip</span>

<span class="bp">#</span><span class="n">find</span> <span class="bp">¬</span> <span class="bp">_</span> <span class="bp">≤</span> <span class="bp">_</span> <span class="bp">↔</span> <span class="bp">_</span> <span class="bp">&lt;</span> <span class="bp">_</span>
<span class="c1">-- not_le: ∀ {α : Type u} [_inst_1 : linear_order α] {a b : α}, ¬a ≤ b ↔ b &lt; a</span>
</pre></div>

#### [ Kevin Buzzard (Aug 11 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131849545):
<p><span class="user-mention" data-user-id="125610">@Truong Nguyen</span> Mario already explained how to find stuff like this -- learn the naming convention :-) Follow the link!</p>

#### [ Truong Nguyen (Aug 11 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/131932809):
<p>Oh, thank you</p>

#### [ Truong Nguyen (Aug 31 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/133143211):
<p>Dear Kenny Lau,<br>
Can you give some instruction for how to use the "#find" command?</p>

#### [ Kevin Buzzard (Aug 31 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20to%20prove%20of%20find%20simple%20theorem/near/133147051):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">find</span>

<span class="n">def</span> <span class="n">x</span> <span class="o">:=</span> <span class="mi">0</span> <span class="c1">-- or anything -- for some reason you can&#39;t use #find immediately</span>

<span class="bp">#</span><span class="n">find</span> <span class="bp">_</span> <span class="bp">+</span> <span class="bp">_</span> <span class="bp">≤</span> <span class="bp">_</span> <span class="bp">+</span> <span class="bp">_</span>
</pre></div>


{% endraw %}
