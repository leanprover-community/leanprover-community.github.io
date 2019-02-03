---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02483casebashtactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [case bash tactic](https://leanprover-community.github.io/archive/113488general/02483casebashtactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 19 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136128666):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I incorrectly assumed that your <code>case_bash</code> tactic was related to the <code>fin</code>-bashing tactic. Nevertheless I wonder if there is place for a mechanism as follows:</p>
<ul>
<li><code>case_bash</code> goes into <code>tactics/</code></li>
<li><code>tidy</code> takes an optional list of tactics to apply (besides the <code>local [attribute]</code> thing that we use nowadays)</li>
<li>So we can prove thing with <code>tidy [case_bash]</code> or something like that.</li>
</ul>
<p>Does that make sense?</p>

#### [ Scott Morrison (Oct 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136139714):
<p>I think you can already override the list of tactics: <code>tidy { tactics := tactic.tidy.default_tactics ++ [foo] }</code>, although <code>foo</code> has to be a <code>tactic string</code> for this to work.</p>

#### [ Scott Morrison (Oct 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136139744):
<p>Certainly that can be given nicer syntax, and use some reflection to allow passing more complicated things than just a <code>tactic string</code>.</p>

#### [ Scott Morrison (Oct 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136139757):
<p>(e.g. a <code>tactic A</code> for any A, a function with arguments that have default values, etc.)</p>


{% endraw %}
