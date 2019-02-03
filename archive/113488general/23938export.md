---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23938export.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [export?](https://leanprover-community.github.io/archive/113488general/23938export.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jun 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995777):
<p>From lean core:</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995779):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">has_pow</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">pow</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">export</span> <span class="n">has_andthen</span> <span class="o">(</span><span class="n">andthen</span><span class="o">)</span>
<span class="kn">export</span> <span class="n">has_pow</span> <span class="o">(</span><span class="n">pow</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995786):
<p>What does <code>export</code> do? The line reminds me of those old batman TV shows.</p>

#### [ Kenny Lau (Jun 13 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995829):
<p>like <code>open</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995833):
<p>oh I just remembered <code>#help</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995835):
<p><code>export: create aliases for declarations</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995846):
<p>At the end of the day, does this just mean that <code>pow</code> can be used instead of <code>has_pow.pow</code>?</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995886):
<p>Aah -- does it mean that this is true globally?</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995890):
<p>I see -- <code>#check pow</code> seems to work fine in a new file</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995894):
<p>so it's open on steroids</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995899):
<p>"open and never close"?</p>

#### [ Johan Commelin (Jun 13 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995954):
<p>No, I guess that is an artifact of the fact that it is in core.</p>

#### [ Johan Commelin (Jun 13 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995963):
<p>Hmm, no... that is not what I meant.</p>

#### [ Sebastian Ullrich (Jun 13 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995966):
<blockquote>
<p>"open and never close"?</p>
</blockquote>
<p>Yes, basically. You can locally "close" it with <code>hide</code>.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996018):
<p>Thanks Sebastian.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996073):
<p>The reason I asked was that I noticed that if I import <code>tactic.ring</code> then I can do <code>a ^ 2</code> for a in a <code>comm_ring</code>, but I can't do this otherwise. I was just trying to figure out where that instance was defined, but I don't know how to do this, short of looking at what <code>tactic.ring</code> imports and importing all of those things instead, until I finally find the import which actually makes it work.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996075):
<p>That's one approach -- and searching for has_pow.pow is another, but actually I should just search for <code>pow</code> perhaps</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996085):
<p>Got it -- obviously to get powers in a ring the key import is <code>group_power.lean</code> ;-)</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996088):
<p>[mumble mumble monoid]</p>


{% endraw %}
