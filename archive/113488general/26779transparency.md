---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26779transparency.html
---

## Stream: [general](index.html)
### Topic: [transparency](26779transparency.html)

---


{% raw %}
#### [ Edward Ayers (Aug 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transparency/near/132514588):
In `tactic.meta` there is a definition called `transparency`:
```lean
inductive transparency
| all | semireducible | instances | reducible | none
```
 which seems to be a setting for how aggressively definitions are unfolded. In the reference manual I see that you can set `reducible`, `semireducible` and `irreducible` as attributes. My impression is that these attributes and settings are used when doing unification or matching. I can't find any documentation on what *exactly* these different transparency modes are changing about the unifier. Please could someone explain it to me or point me to some docs or C++ code that will help me understand what is going on here?

So an example might be that you want `ℝ` to be irreducible because you rarely prove things about reals in terms of equivalence classes of cauchy sequences.

#### [ Edward Ayers (Oct 10 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transparency/near/135536162):
bump

#### [ Scott Morrison (Oct 10 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transparency/near/135537299):
Sorry, probably such documentation doesn't exists. Gabriel and Sebastian are probably the people to hope can point you to right parts of the C++ code.


{% endraw %}
