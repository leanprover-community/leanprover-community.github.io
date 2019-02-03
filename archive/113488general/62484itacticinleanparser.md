---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62484itacticinleanparser.html
---

## Stream: [general](index.html)
### Topic: [itactic in lean.parser](62484itacticinleanparser.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 22 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148152572):
<p>Inside a <code>lean.parser</code> monad, I can for example read a <code>name</code> by</p>
<div class="codehilite"><pre><span></span>n &lt;- ident
</pre></div>


<p>Is there any way to do the same thing with an <code>itactic</code> block? i.e. expecting a <code>begin ... end</code> or <code>{ ... }</code> block?</p>

#### [ Keeley Hoek (Nov 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148152614):
<p>In the end, I'm trying to make a command which _optionally_ accepts an <code>itactic</code> block</p>

#### [ Sebastian Ullrich (Nov 22 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148162764):
<p>Unfortunately no. <code>itactic</code> is not a parser in Lean 3 for technical reasons and can only be used directly as a parameter type.</p>

#### [ Keeley Hoek (Nov 22 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148166371):
<p>&lt;/3 Heartbreaking but good to know, thanks Sebastian</p>

#### [ Kevin Buzzard (Nov 22 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148167149):
<p>And Lean 4?</p>

#### [ Sebastian Ullrich (Nov 22 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/itactic%20in%20lean.parser/near/148179070):
<p>There <em>will</em> be some <code>itactic</code> parser in Lean 4 since all parsing will be done in Lean, and you should be able to reuse it to you heart's content</p>


{% endraw %}
