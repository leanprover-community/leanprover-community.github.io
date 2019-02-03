---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03929ExpectedTypeinmatch.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Expected Type in match](https://leanprover-community.github.io/archive/113488general/03929ExpectedTypeinmatch.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Nima (Apr 21 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483132):
<p>Is there anyway to <strong>explicitly</strong> tell lean the expected type of <code>match</code>, so I would not receive the following error:</p>
<blockquote>
<p>invalid match/convoy expression, user did not provide type for the expression, <br>
lean tried to infer one using expected type information, but result is not type correct</p>
</blockquote>

#### [ Kenny Lau (Apr 21 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483171):
<p>for example?</p>

#### [ Mario Carneiro (Apr 21 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483313):
<p><code>match a, b : \forall a b, expected_type_of_match with ... end</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483320):
<p>You can also often use type ascription in some cases, i.e. <code>(match a, b with ... end : expected type)</code></p>

#### [ Nima (Apr 21 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483564):
<p>OK, I don't have a good example for this.<br>
Will get back if I found one.</p>

#### [ Nima (Apr 21 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Expected%20Type%20in%20match/near/125483729):
<p>Thank you, this following worked (the other one did not), </p>
<blockquote>
<p><code>match a, b : \forall a b, expected_type_of_match with ... end</code></p>
</blockquote>


{% endraw %}
