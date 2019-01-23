---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87229unoption.html
---

## Stream: [general](index.html)
### Topic: [unoption](87229unoption.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948591):
What is the function which takes `a : option X` and a proof that `a` isn't `none` and returns the x such that `a = some x` called? I can write it -- but I suspect someone else already thought of it...

#### [ Kevin Buzzard (Jul 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948631):
I found `get` but that seems to involve bools...

#### [ Mario Carneiro (Jul 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948720):
it is `option.get`

#### [ Mario Carneiro (Jul 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129948739):
you can use a bool as a Prop fyi...

#### [ Kevin Buzzard (Jul 19 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unoption/near/129952337):
OK thanks!


{% endraw %}
