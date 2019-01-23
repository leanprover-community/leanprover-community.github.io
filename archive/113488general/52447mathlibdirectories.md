---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52447mathlibdirectories.html
---

## Stream: [general](index.html)
### Topic: [mathlib directories](52447mathlibdirectories.html)

---


{% raw %}
#### [ Reid Barton (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288114):
Not sure whether joke suggestion: one top-level directory per arXiv primary category.

#### [ Mario Carneiro (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288176):
lol they are all physics

#### [ Patrick Massot (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288208):
https://arxiv.org/archive/math

#### [ Reid Barton (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288213):
I had in mind https://arxiv.org/archive/math, though one could include at least the CS ones as well

#### [ Mario Carneiro (Dec 20 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288227):
which one is `data`?

#### [ Reid Barton (Dec 20 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288379):
there's always math.GM - General Mathematics, though it's not totally clear to me that `data` should exist in the first place

#### [ Reid Barton (Dec 20 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288386):
though it's indeed unclear where many of the contents of `data` would be categorized

#### [ Kenny Lau (Dec 20 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152288472):
one has to ask the question: why is [insert file name] not included in `data/`?

#### [ Mario Carneiro (Dec 20 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152289052):
I would broadly categorize it as "stuff useful for programming, but not meta"

#### [ Scott Morrison (Dec 21 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20directories/near/152301210):
I think we should reserve the `/math.GM/` folder for crank contributions to mathlib, keeping with tradition. Maybe we could hardcode leanpkg to not compile math.GM unless you are a "contributor" to that folder?


{% endraw %}
