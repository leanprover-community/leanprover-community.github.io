---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39509declarationlinter.html
---

## Stream: [general](index.html)
### Topic: [declaration linter](39509declarationlinter.html)

---


{% raw %}
#### [ Reid Barton (Oct 19 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20linter/near/136122617):
<p>I wrote a "declaration linter" that processes each declaration and checks for things that look dodgy.<br>
Currently, it looks for lemmas whose type is not a Prop, and structures/classes which could be Props but aren't.<br>
Here's the output on the core library and (a slightly out-of-date) mathlib: <a href="https://gist.github.com/rwbarton/4e119ba9b812debac08c8a54afb104bd" target="_blank" title="https://gist.github.com/rwbarton/4e119ba9b812debac08c8a54afb104bd">https://gist.github.com/rwbarton/4e119ba9b812debac08c8a54afb104bd</a></p>

#### [ Reid Barton (Oct 19 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20linter/near/136122653):
<p>I want to add warnings for unused variables next, but that will be a bit more difficult.</p>

#### [ Reid Barton (Oct 19 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20linter/near/136122882):
<p>Hmm, some of the output is duplicated--not sure why</p>

#### [ Reid Barton (Oct 19 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20linter/near/136122893):
<p>Start at line 141</p>

#### [ Reid Barton (Oct 19 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20linter/near/136122980):
<p>Ah, I figured out why--some leftover testing code.</p>


{% endraw %}
