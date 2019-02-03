---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54841haltingproblem.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [halting problem](https://leanprover-community.github.io/archive/116395maths/54841haltingproblem.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964377):
<p><a href="https://github.com/leanprover/mathlib/commit/d62bf5605ec8971d446a01af40abf9183447cb42#diff-6650f7dae83be3a52c8eb036a23d7b26R175" target="_blank" title="https://github.com/leanprover/mathlib/commit/d62bf5605ec8971d446a01af40abf9183447cb42#diff-6650f7dae83be3a52c8eb036a23d7b26R175">https://github.com/leanprover/mathlib/commit/d62bf5605ec8971d446a01af40abf9183447cb42#diff-6650f7dae83be3a52c8eb036a23d7b26R175</a></p>

#### [ Kenny Lau (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964379):
<p>holy mother you did it <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964380):
<p>congratulations</p>

#### [ Mario Carneiro (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964383):
<p>You can see it's just a corollary of a much stronger theorem</p>

#### [ Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964401):
<p>oh and which commit should i checkout?</p>

#### [ Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964425):
<p>you didn't bother to build any</p>

#### [ Mario Carneiro (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964426):
<p>I think Rice's theorem is cool</p>

#### [ Mario Carneiro (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964427):
<p>?</p>

#### [ Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964428):
<p>I eat them every day</p>

#### [ Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964429):
<p><a href="https://github.com/leanprover/mathlib/commits" target="_blank" title="https://github.com/leanprover/mathlib/commits">https://github.com/leanprover/mathlib/commits</a></p>

#### [ Kenny Lau (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964430):
<p>there are no green ticks after April 29</p>

#### [ Mario Carneiro (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964434):
<p>that's weird</p>

#### [ Mario Carneiro (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964442):
<p>travis usually kicks in automatically</p>

#### [ Kenny Lau (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964445):
<p>so which commit should i use?</p>

#### [ Mario Carneiro (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964450):
<p>I have been building locally so they should work, but I guess I should find out what's up with travis</p>

#### [ Kenny Lau (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964490):
<p>and which lean version?</p>

#### [ Mario Carneiro (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964491):
<p>3.4.1</p>

#### [ Gabriel Ebner (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964492):
<p>Travis is broken on the other packages as well. "This is not an active repository<br>
You don't have sufficient rights to enable this repo on Travis. <br>
Please contact the admin to enable it or to receive admin rights yourself." <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> ?</p>

#### [ Mario Carneiro (May 23 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964497):
<p>I always get that message, but it did not affect the build itself</p>

#### [ Gabriel Ebner (May 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126964505):
<p>Either way, <code>super</code> does not get built by travis either at the moment.</p>

#### [ Sebastian Ullrich (May 23 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126965515):
<p>I'll have to ask Leo</p>

#### [ Kevin Buzzard (May 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126965572):
<p>you have a halting problem</p>

#### [ Sebastian Ullrich (May 23 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/halting%20problem/near/126979574):
<p><a href="https://travis-ci.org/leanprover/mathlib" target="_blank" title="https://travis-ci.org/leanprover/mathlib">https://travis-ci.org/leanprover/mathlib</a> now looks more promising</p>


{% endraw %}
