---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06147underhandedlean.html
---

## [general](index.html)
### [underhanded lean](06147underhandedlean.html)

#### [Mario Carneiro (Dec 27 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/underhanded lean/near/152579911):
wow, I didn't expect this to work:
```lean
open lean.parser interactive interactive.types

@[user_command] meta def my_print (_ : parse $ tk "#print") : lean.parser unit :=
tk "axioms" >> ident $> trace "totally ok" ().

@[user_command] meta def my_def (_ : parse $ tk "def") : lean.parser unit :=
ident >> tk ":" >> texpr >> tk ":=" >> ident $> trace "looks good to me" ().

def contradiction : false := sure -- looks good to me
#print axioms contradiction -- totally ok
```
Apparently you can override basically all lean command tokens, including `section`, `namespace`, `def` and `end`

#### [Keeley Hoek (Dec 27 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/underhanded lean/near/152597048):
Yep
At one point I tried a sneaky 'begin' override, but the problem is you can never close a block you open

