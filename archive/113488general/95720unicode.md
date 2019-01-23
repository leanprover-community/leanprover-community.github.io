---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95720unicode.html
---

## Stream: [general](index.html)
### Topic: [unicode](95720unicode.html)

---


{% raw %}
#### [ Kenny Lau (Mar 31 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unicode/near/124443168):
Does every symbol have a non-unicode equivalent?

#### [ Mario Carneiro (Mar 31 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unicode/near/124443263):
No. Most do, but the strict policy on this was dropped a while ago and new features have crept in with no non-unicode equivalents. Basically no one uses lean without unicode anymore (if they ever did), so it wasn't felt necessary to continue to support.

#### [ Mario Carneiro (Mar 31 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unicode/near/124443307):
Here's one:
```
theorem «a strange-identifier!» : true := trivial
```
the double french quotes escape everything, and have no non-unicode equivalent


{% endraw %}
