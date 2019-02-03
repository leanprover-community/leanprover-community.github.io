---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52447mathlibdirectories.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mathlib directories](https://leanprover-community.github.io/archive/113488general/52447mathlibdirectories.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288114):
<p>Not sure whether joke suggestion: one top-level directory per arXiv primary category.</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288176):
<p>lol they are all physics</p>

#### [ Patrick Massot (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288208):
<p><a href="https://arxiv.org/archive/math" target="_blank" title="https://arxiv.org/archive/math">https://arxiv.org/archive/math</a></p>

#### [ Reid Barton (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288213):
<p>I had in mind <a href="https://arxiv.org/archive/math" target="_blank" title="https://arxiv.org/archive/math">https://arxiv.org/archive/math</a>, though one could include at least the CS ones as well</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288227):
<p>which one is <code>data</code>?</p>

#### [ Reid Barton (Dec 20 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288379):
<p>there's always math.GM - General Mathematics, though it's not totally clear to me that <code>data</code> should exist in the first place</p>

#### [ Reid Barton (Dec 20 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288386):
<p>though it's indeed unclear where many of the contents of <code>data</code> would be categorized</p>

#### [ Kenny Lau (Dec 20 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288472):
<p>one has to ask the question: why is [insert file name] not included in <code>data/</code>?</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152289052):
<p>I would broadly categorize it as "stuff useful for programming, but not meta"</p>

#### [ Scott Morrison (Dec 21 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152301210):
<p>I think we should reserve the <code>/math.GM/</code> folder for crank contributions to mathlib, keeping with tradition. Maybe we could hardcode leanpkg to not compile math.GM unless you are a "contributor" to that folder?</p>


{% endraw %}
