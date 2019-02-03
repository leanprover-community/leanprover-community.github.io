---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17893Notexpectedbehaviorusingnormnum.html
---

## Stream: [general](index.html)
### Topic: [Not expected behavior using norm_num](17893Notexpectedbehaviorusingnormnum.html)

---


{% raw %}
#### [ Bruno Bentzen (Dec 21 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302446):
<p>Hi everyone,</p>
<p>I have a bare project (with mathlib imported) in which the following code</p>
<div class="codehilite"><pre><span></span>import data.nat.prime  tactic.norm_num

lemma prime_seven : nat.prime (7 : ℕ) := by
norm_num
</pre></div>


<p>displays the error 'norm_num failed to simplify'. Does it work for you?</p>
<p>Best,<br>
Bruno</p>

#### [ Bryan Gin-ge Chen (Dec 21 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302655):
<p>I get no errors on my system. What version of mathlib are you using? Do other primes like 2, 3 work?</p>

#### [ Mario Carneiro (Dec 21 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302857):
<p>If you click on <code>norm_num</code> to go to the definition, search in that file for a function called <code>eval_prime</code></p>

#### [ Mario Carneiro (Dec 21 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302868):
<p>If you don't have it, chances are you are running an old version of mathlib</p>

#### [ Bryan Gin-ge Chen (Dec 21 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302883):
<p>Oh, is this the 3.4.1 branch issue again?</p>

#### [ Mario Carneiro (Dec 21 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302890):
<p>oh, that might be it</p>

#### [ Mario Carneiro (Dec 21 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302964):
<p>go into <code>_target/deps/mathlib</code> and <code>git checkout master</code> then <code>lean --make</code> (which will take a while)</p>

#### [ Bruno Bentzen (Dec 21 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152302974):
<p>yeah, no <code>eval_prime</code>. Then I should be really using an old version of it.</p>

#### [ Bruno Bentzen (Dec 21 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152303187):
<p>Thanks! I'm fixing the build, I think it should work now.</p>

#### [ Bruno Bentzen (Dec 21 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Not%20expected%20behavior%20using%20norm_num/near/152304585):
<p>It works now. Thanks, Bryan and Mario!</p>


{% endraw %}
