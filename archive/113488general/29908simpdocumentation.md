---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29908simpdocumentation.html
---

## Stream: [general](index.html)
### Topic: [simp documentation](29908simpdocumentation.html)

---


{% raw %}
#### [ Simon Hudon (Mar 15 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728672):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'm having a look at your recent PR. In "When it is unadvisable to use simp", why not use <code>show</code> instead of <code>suffices</code>?</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728716):
<p>I think that's kind of backwards</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728718):
<p>let's say you're a long way from a goal</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728719):
<p>and simp makes tiny progress</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728727):
<p>no wait</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728728):
<p>simp changes your goal slightly</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728729):
<p>it makes it into X</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728730):
<p>then <code>suffices X, simpa [this]</code> does the same thing</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728731):
<p>but show won't work</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728734):
<p>becuase X isn't defeq to the original goal</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728777):
<p>The idiom (is that the right word?) is that if simp changes your goal to X, then why not make a new goal and instantly close it with simp.</p>

#### [ Simon Hudon (Mar 15 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728825):
<p>Good point. Then you can only choose <code>show</code> in the special case where the new goal is <code>defeq</code> to the old one.</p>

#### [ Simon Hudon (Mar 15 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728831):
<p>It might be worth having a shortcut for <code>suffices : (simplified thing), by simpa [this]</code></p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728985):
<p>yeah, it's <code>simp</code> ;-)</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728992):
<p><code>simp to (simplified thing)</code>?</p>

#### [ Mario Carneiro (Mar 15 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728999):
<p><code>simpa</code> was intended for basically exactly that use case. It's not exactly wasting that many keywords as it is</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729000):
<p>yeah but golf</p>

#### [ Mario Carneiro (Mar 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729002):
<p>for golf, <code>simpa [bla] using bla</code> is even more effective</p>

#### [ Kevin Buzzard (Mar 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729041):
<p><code>simp {answer := simplified thing}</code></p>

#### [ Mario Carneiro (Mar 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729053):
<p>also, you can just write <code>suffices : (simplified thing), {simpa}</code></p>


{% endraw %}
