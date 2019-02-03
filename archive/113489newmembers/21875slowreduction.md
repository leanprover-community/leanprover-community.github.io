---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/21875slowreduction.html
---

## Stream: [new members](index.html)
### Topic: [slow reduction](21875slowreduction.html)

---


{% raw %}
#### [ Scott Olson (Sep 28 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134782780):
<p>I have a <code>#reduce</code> that's leading to "(deterministic) timeout" and I'm wondering what I can do to find out what's taking so long. Can I <code>#reduce</code> step-by-step?</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783570):
<p>Unfortunately no. <code>#reduce</code> is not really intended for serious use</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783577):
<p>It turns out that unfolding a proof down to axioms is actually kind of expensive :)</p>

#### [ Scott Olson (Sep 28 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783646):
<p>Hmm, well it's also breaking my examples/tests, since it can't even prove things by <code>rfl</code> at very small input sizes, and I can't figure out why, because the code seems fairly straightforward.</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783655):
<p>this is also not unusual</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783660):
<p>I think <code>theorem nat.prime 5 := dec_trivial</code> times out</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783706):
<p>it depends on what numerical functions you are calling</p>

#### [ Scott Olson (Sep 28 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783720):
<p>I guess it would be nice to have bytecode-based tests for quick dumb sanity checks</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783731):
<p>You should use <code>#eval</code> for that</p>

#### [ Scott Olson (Sep 28 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134783741):
<p>I do, I just wish I could write something that asserts on the result rather than simply printing it</p>

#### [ Mario Carneiro (Sep 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134784254):
<p>you can use <code>run_cmd</code>: </p>
<div class="codehilite"><pre><span></span>run_cmd guard (2 + 2 = 4)
run_cmd guard (2 + 2 = 5) -- failed
</pre></div>

#### [ Scott Olson (Sep 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/slow%20reduction/near/134784267):
<p>Perfect, thanks!</p>


{% endraw %}
