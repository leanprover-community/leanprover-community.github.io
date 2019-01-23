---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55645nattostring.html
---

## Stream: [general](index.html)
### Topic: [nat to string?](55645nattostring.html)

---


{% raw %}
#### [ Scott Morrison (Apr 10 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861127):
How to I get a string from a nat?

#### [ Simon Hudon (Apr 10 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861272):
`to_string`

#### [ Scott Morrison (Apr 10 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861290):
````
invalid field notation, 'to_string' is not a valid "field" because environment does not contain 'nat.to_string'
  k
which has type
  ℕ
````

#### [ Simon Hudon (Apr 10 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861356):
try `to_string k`. It's part of the `has_to_string` class so it won't support field notation

#### [ Scott Morrison (Apr 10 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20to%20string%3F/near/124861359):
thank you!


{% endraw %}
