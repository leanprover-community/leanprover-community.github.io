---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26829notation.html
---

## Stream: [general](index.html)
### Topic: [notation](26829notation.html)

---


{% raw %}
#### [ Reid Barton (Feb 28 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation/near/123093960):
Does anyone have a suggestion for Lean-friendly notation corresponding to TeX $$f_*$$ and $$f^*$$?
(Meaning whatever you want them to mean, but for example, post- and pre-composition with the morphism $$f$$.)

#### [ Reid Barton (Feb 28 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation/near/123094002):
Apparently there are no Unicode subscript or superscript asterisk characters

#### [ Reid Barton (Feb 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation/near/123095373):
`f^*` works okay for $$f^*$$, but `f_*` isn't as nice because `f_` parses as a single identifier, so it needs a space.

#### [ Andrew Ashworth (Feb 28 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation/near/123097520):
you could cheat and use ＿, which is not _

#### [ Sebastian Ullrich (Feb 28 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation/near/123097707):
Or use one of the up/down arrows


{% endraw %}
