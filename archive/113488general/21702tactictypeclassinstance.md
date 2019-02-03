---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21702tactictypeclassinstance.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tactic type class instance](https://leanprover-community.github.io/archive/113488general/21702tactictypeclassinstance.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ petercommand (Jan 09 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708014):
<div class="codehilite"><pre><span></span>meta def opt_fst (a: tactic unit) (b: tactic unit) : tactic unit := (a &gt;&gt; b) &lt;|&gt; b
</pre></div>


<p>I am trying to define a tactic combinator, but it seems that I cannot use it like this:</p>
<div class="codehilite"><pre><span></span>opt_fst { symmetry } { symmetry }
</pre></div>


<p>and I am getting errors like</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
|- has_emptyc (tactic unit)
</pre></div>


<p>Am I doing something wrong here?</p>

#### [ petercommand (Jan 09 2019 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708130):
<p>I want the tactic to accept begin...end blocks or {...} blocks</p>

#### [ Sebastian Ullrich (Jan 09 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708169):
<p>You'll want your parameters to have type <code>itactic</code> (for "interactive tactic"). Try searching for itactic in core or mathlib for examples.</p>

#### [ Rob Lewis (Jan 09 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708213):
<p><code>meta def tactic.interactive.opt_fst (a: tactic.interactive.itactic) (b: tactic.interactive.itactic) : tactic unit := (a &gt;&gt; b) &lt;|&gt; b</code></p>

#### [ petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708254):
<p>Isn't <code>tactic.interactive.itactic</code> defined as <code>tactic unit</code>?</p>

#### [ Sebastian Ullrich (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708297):
<p>Yes, but it's special-cased in the tactic block parser</p>

#### [ petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708301):
<p>Ah</p>

#### [ petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708303):
<p>Hmm..I am still getting the same error</p>

#### [ Gabriel Ebner (Jan 09 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708334):
<p>You need to call it inside <code>begin..end</code>: <code>begin opt_fst {} {} end</code></p>

#### [ petercommand (Jan 09 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708347):
<p>do I have to prefix the name of the tactic with <code>tactic.interactive.</code>?</p>

#### [ Gabriel Ebner (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708385):
<p>No.</p>

#### [ Sebastian Ullrich (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708394):
<p>(if you're in <code>tactic.interactive</code>, which your definition should be)</p>

#### [ petercommand (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708400):
<p>after changing the name of the tactic, it worked..</p>

#### [ Rob Lewis (Jan 09 2019 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708416):
<p>The tactic should be named <code>tactic.interactive.whatever</code>. You don't need to write the <code>tactic.interactive</code> part when you use it.</p>

#### [ petercommand (Jan 09 2019 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708478):
<blockquote>
<p>The tactic should be named <code>tactic.interactive.whatever</code>. You don't need to write the <code>tactic.interactive</code> part when you use it.</p>
</blockquote>
<p>Hmm..seems that this is also hardcoded</p>

#### [ petercommand (Jan 09 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708504):
<p>Thanks!</p>


{% endraw %}
