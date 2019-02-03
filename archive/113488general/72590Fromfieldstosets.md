---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72590Fromfieldstosets.html
---

## Stream: [general](index.html)
### Topic: [From fields to sets](72590Fromfieldstosets.html)

---


{% raw %}
#### [ Anthony Bordg (Oct 04 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217336):
<p>Hello,</p>
<p>is there an easy way to get the underlying set of a (discrete) field ?<br>
Thanks</p>

#### [ Simon Hudon (Oct 04 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217489):
<p>If you have <code>field α</code>, <code>set.univ α</code> is the underlying set.</p>

#### [ Anthony Bordg (Oct 04 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217940):
<blockquote>
<p>If you have <code>field α</code>, <code>set.univ α</code> is the underlying set.</p>
</blockquote>
<p>Great! Thank you Simon.</p>

#### [ Simon Hudon (Oct 04 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217959):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Simon Hudon (Oct 04 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218041):
<p>What do you use it for? Typically, I don't see that set used much because the type does most of the work on its own</p>

#### [ Mario Carneiro (Oct 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218290):
<p>I think maybe you just want <code>α</code>?</p>

#### [ Mario Carneiro (Oct 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218339):
<p>It's not an "underlying set", it's an "underlying type"</p>

#### [ Mario Carneiro (Oct 04 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218382):
<p>and there is no underlying about it because we define "a field on α" rather than just "a field", so α is the carrier</p>

#### [ Anthony Bordg (Oct 04 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135219190):
<blockquote>
<p>What do you use it for? Typically, I don't see that set used much because the type does most of the work on its own</p>
</blockquote>
<p>You're right, I realized that I don't need it. <span class="emoji emoji-1f44d" title="+1">:+1:</span></p>


{% endraw %}
