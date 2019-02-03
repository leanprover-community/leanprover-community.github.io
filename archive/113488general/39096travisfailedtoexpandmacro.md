---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39096travisfailedtoexpandmacro.html
---

## Stream: [general](index.html)
### Topic: [travis "failed to expand macro"](39096travisfailedtoexpandmacro.html)

---


{% raw %}
#### [ Scott Morrison (Nov 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20%22failed%20to%20expand%20macro%22/near/147562010):
<p>I just got another of these:</p>
<div class="codehilite"><pre><span></span>44.13s$ lean --recursive --export=mathlib.txt
&lt;unknown&gt;:1:1: error: failed to expand macro
The command &quot;lean --recursive --export=mathlib.txt&quot; exited with 1.
</pre></div>


<p>on travis.</p>

#### [ Scott Morrison (Nov 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20%22failed%20to%20expand%20macro%22/near/147562012):
<p><a href="https://travis-ci.org/leanprover/mathlib/jobs/454247679" target="_blank" title="https://travis-ci.org/leanprover/mathlib/jobs/454247679">https://travis-ci.org/leanprover/mathlib/jobs/454247679</a></p>

#### [ Scott Morrison (Nov 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20%22failed%20to%20expand%20macro%22/near/147562019):
<p><code>lean --make .</code> and <code>lean --make .</code> return happily.</p>

#### [ Reid Barton (Nov 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20%22failed%20to%20expand%20macro%22/near/147562026):
<p>that's because you used <code>sorry</code>, I'm pretty sure</p>

#### [ Scott Morrison (Nov 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20%22failed%20to%20expand%20macro%22/near/147562029):
<p>I remember someone else hitting this recently, but can't find it.</p>

#### [ Scott Morrison (Nov 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20%22failed%20to%20expand%20macro%22/near/147562036):
<p>ah, okay, you're absolutely right, my mistake!</p>


{% endraw %}
