---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64659notationintroducevariables.html
---

## Stream: [general](index.html)
### Topic: [notation introduce variables](64659notationintroducevariables.html)

---


{% raw %}
#### [ Joe Hendrix (Aug 10 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131200648):
Is it possible to write notation that will allow introducing variables?  e.g. have something like the following work:
```
local notation `flet` var `:=` rhs `fin` body := let var := rhs in body
example : ℕ := flet x := 1 fin x
```

#### [ Simon Hudon (Aug 10 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131200900):
Yes, the following can be found in `core.lean`: ``notation `exists` binders `, ` r:(scoped P, Exists P) := r`` which illustrates how the binder / scoped notation works.

It let's you tell Lean how to parse a lambda abstract and choose a function (i.e. `Exists`) to feed that lambda expression to.

#### [ Simon Hudon (Aug 10 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131200992):
I think your notation could work as ``local notation `flet` binder `:=` rhs `fin` body:(scoped P, P rhs) := body``

#### [ Simon Hudon (Aug 10 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131201428):
To help with the pretty printing, you may way to define a function that Lean will associate with your notation:

```lean
def my_let {α β : Sort*} (f : α → β) (x : α) := f x

local notation `flet` binder `:=` rhs `fin` body:(scoped P, my_let P rhs) := body
```

#### [ Joe Hendrix (Aug 10 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131202287):
Great.  Thanks for finding that.

#### [ Simon Hudon (Aug 10 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131202453):
:+1: To be fair, a few months back, there was intense session on gitter, looking through the C++ code and figuring out the ins and outs of the `notation` notation


{% endraw %}
