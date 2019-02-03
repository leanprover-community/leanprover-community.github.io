---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52942exactthis.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [exact this](https://leanprover-community.github.io/archive/113488general/52942exactthis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130305391):
<p>Today I came across several instance of <code>have := stuff, exact this</code> closing a goal where <code>exact stuff</code> doesn't. I guess this is yet another elaboration subtlety, but I'd like to know if there is a nicer way to do this in one tactic.</p>

#### [ Mario Carneiro (Jul 26 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130314992):
<p>I use Chris's trick: <code>exact (stuff : _)</code></p>

#### [ Patrick Massot (Jul 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130327840):
<p>Thanks!</p>

#### [ Patrick Massot (Jul 26 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130353906):
<p>Could we get a mathlib tactic replacing <code>exact</code> which tries <code>exact</code> and then Chris's trick?</p>

#### [ Patrick Massot (Jul 26 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130353926):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> : is this a well known bug or a feature?</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354033):
<p>I'll go with feature</p>

#### [ Patrick Massot (Jul 26 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354040):
<p>Too easy...</p>

#### [ Patrick Massot (Jul 26 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354069):
<p>Seriously, what do I miss to understand this thing?</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354309):
<p>I mean, it's clear that omitting the expected type can lead to different elaboration results in some cases, and in some of these cases, the result without expected type may even be preferable. Whether that is something that could be improved in the elaborator can only be decided on a case by case basis.</p>

#### [ Patrick Massot (Jul 26 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354494):
<p>I sort of understand this. What I don't get is how <code>(stuff : _)</code> differs from not specifying the expected type of <code>stuff</code>. Here we really mean underscore, this is not an abbreviation for Zulip purposes.</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355110):
<p>Where do you not specify it? If you use <code>exact stuff</code>, the expected type is the goal.</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355120):
<p>In both <code>have := stuff</code> and <code>(stuff : _)</code>, there is no expected type</p>

#### [ Patrick Massot (Jul 26 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355632):
<p>I mean <code>exact stuff</code> versus <code>exact (stuff : _)</code>, both meant to close the current goal.</p>

#### [ Patrick Massot (Jul 26 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355646):
<p>Sometimes only the later succeeds</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356150):
<p>As I said, only in <code>exact stuff</code> do you have an expected type. It's the goal.</p>

#### [ Patrick Massot (Jul 26 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356190):
<p>Sorry I'm slow.</p>

#### [ Patrick Massot (Jul 26 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356242):
<p>But it's really really hot here</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356283):
<p>I'm very grateful to spend the remaining summer in the land of air conditioning :)</p>

#### [ Patrick Massot (Jul 26 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356295):
<p>USA?</p>

#### [ Sebastian Ullrich (Jul 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356748):
<p>Yes, I'm doing an internship under Leo until October</p>

#### [ Patrick Massot (Jul 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356771):
<p>Oooh, that sounds like a very good idea!</p>


{% endraw %}
