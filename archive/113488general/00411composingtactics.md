---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00411composingtactics.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [composing tactics](https://leanprover-community.github.io/archive/113488general/00411composingtactics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Jun 02 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127458510):
<p>Suppose I prove a goal using <code>by repeat {constructor}</code>. What is the syntax for creating a new def of type <code>tactic unit</code> that does the same thing? Do I have to drop down into using the non-interactive tactics?</p>

#### [ Andrew Ashworth (Jun 02 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127458561):
<p>I guess handling the context and goals explicitly in a <code>do</code> block isn't so bad, but I was wondering if this is the correct way to do it</p>

#### [ Andrew Ashworth (Jun 02 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127459735):
<p>ahh, figured it out. it's just <code>interactive.repeat interactive.constructor</code>. I didn't know about the <code>itactic</code> type</p>

#### [ Gabriel Ebner (Jun 02 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127460627):
<p>1) Go to the definition of <code>tactic.interactive.repeat</code>and look how its defined.  I don't know if we have any documentation on how to write interactive tactics beyond the ICFP paper.  Short version: when you use <code>begin foo bar end</code>, lean looks for a definition named <code>tactic.interactive.foo</code>.  The type of the arguments of <code>tactic.interactive.foo</code> determine how the arguments to the tactic are parsed.  For example, <code>itactic</code> tells lean to parse a tactic block in curly braces.</p>

#### [ Gabriel Ebner (Jun 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127460634):
<p>2) You can use <code> `[repeat {constructor}] </code> to use interactive tactic syntax outside of begin-end blocks.</p>


{% endraw %}
