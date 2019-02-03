---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/38132shouldthisbedectrivial.html
---

## Stream: [maths](index.html)
### Topic: [should this be dec_trivial?](38132shouldthisbedectrivial.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 18 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920509):
<p><code>example (n : ℕ) : n &gt; 0 → n ≤ 6 → fact n &lt; 3 ^ n := dec_trivial -- fails</code></p>
<p>I do 6 case splits and <code>dec_trivial</code> seems to be able to handle the arithmetic, but I can't do it all in one go. I sometimes run into these. How is one supposed to diagnose what has happened and fix it?</p>

#### [ Chris Hughes (Nov 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920516):
<p>Revert n, and put <code>n \le 6</code> before <code>0&lt;n</code></p>

#### [ Kevin Buzzard (Nov 18 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920517):
<p>Thanks Chris.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147920557):
<p>I see, so <code>forall n : nat, n &lt;= X -&gt; P n</code> works, and I just need to ensure I'm in this format.</p>

#### [ Mario Carneiro (Nov 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921371):
<p>sigh... why the horrible case split proofs?</p>

#### [ Mario Carneiro (Nov 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921374):
<p>you could reason it instead</p>

#### [ Kevin Buzzard (Nov 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921375):
<p>I don't really know what you're saying</p>

#### [ Kevin Buzzard (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921379):
<p>or even if you're talking to me</p>

#### [ Kevin Buzzard (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921383):
<p>But my job is to solve the problems I set, in Lean</p>

#### [ Mario Carneiro (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921386):
<p>if you had to prove that theorem by hand I am sure you wouldn't evaluate 6 factorials</p>

#### [ Kevin Buzzard (Nov 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921387):
<p>and the problem is "for which positive integers n is n! &lt; 3^n"</p>

#### [ Mario Carneiro (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921389):
<p>you can prove that it's true for 5 and stop because monotonicity</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921440):
<p>ha ha</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921442):
<p>I'm not sure it's that easy</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921448):
<p>n! and 3^n are changing in different ways</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921450):
<p>and things get weird at n=3</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921452):
<p>I think I have to check all 6</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921462):
<p>dec_trivial times out for 7 :-/</p>

#### [ Kevin Buzzard (Nov 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20this%20be%20dec_trivial%3F/near/147921463):
<p>(hence the norm_num approach, which was also troublesome -- see other thread)</p>


{% endraw %}
