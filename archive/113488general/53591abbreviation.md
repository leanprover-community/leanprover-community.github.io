---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53591abbreviation.html
---

## Stream: [general](index.html)
### Topic: [abbreviation](53591abbreviation.html)

---


{% raw %}
#### [ Reid Barton (Dec 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746902):
I don't suppose `abbreviation` is documented anywhere?

#### [ Reid Barton (Dec 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746904):
It seems to do something very specific that I want (MWE incoming)

#### [ Reid Barton (Dec 03 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746954):
```lean
def test1 {α : Type} [has_add α] (x : α) := x + x
@[class, reducible] def my_add := has_add
def test2 {α : Type} [my_add α] (x : α) := x + x -- failed to synthesize type class instance for has_add α
abbreviation my_add' := has_add
def test3 {α : Type} [my_add' α] (x : α) := x + x -- ok!
```

#### [ Reid Barton (Dec 03 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746955):
Is there a catch?

#### [ Reid Barton (Dec 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150747018):
You can also do more interesting things like `abbreviation my_add' (α : Type) := has_add (list α)`


{% endraw %}
