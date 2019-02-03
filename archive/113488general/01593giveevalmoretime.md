---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01593giveevalmoretime.html
---

## Stream: [general](index.html)
### Topic: [give #eval more time](01593giveevalmoretime.html)

---


{% raw %}
#### [ Chris Hughes (Sep 09 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615259):
<p>Is there a way to give <code>#eval</code> more time before a deterministic timeout?</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615377):
<p>On the command line there is a <code>--timeout=num</code> option.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615398):
<p>So I guess you could try editing your VS Code preferences (if you want to do this in VS Code)</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615458):
<p>wooah Ctrl-comma in VS Code has changed.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615530):
<p>oh actually I've just found that it is an option in VS Code: </p>
<div class="codehilite"><pre><span></span>  // Set a deterministic timeout (it is approximately the maximum number of memory allocations in thousands) for the Lean server.
  &quot;lean.timeLimit&quot;: 100000
</pre></div>


<p>So try ctrl-comma (or file -&gt; preferences -&gt; settings) and then search for <code>lean.timeLimit</code> and try changing that (maybe you have to click on a pencil and say you want to edit it before you can edit it)</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615544):
<p>I only half-know what I'm talking about here though, so no guarantee of success.</p>

#### [ Chris Hughes (Sep 09 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615727):
<p>Doesn't seem to make any difference.</p>

#### [ Keeley Hoek (Sep 09 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133615731):
<p>did you restart the lean server after you did it? I forget this more often than I'd like...</p>

#### [ Chris Hughes (Sep 09 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133616137):
<p>No I didn't. Thanks <span class="user-mention" data-user-id="110111">@Keeley Hoek</span></p>

#### [ Chris Hughes (Sep 09 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133616412):
<p>Thanks. I have now managed to compute that my proof of quadratic reciprocity used exactly 5000 theorems, definitions, axioms and constants traced all the way back to axioms.</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give%20%23eval%20more%20time/near/133617608):
<p>That's cool! Have you posted the script for doing that somewhere?</p>


{% endraw %}
