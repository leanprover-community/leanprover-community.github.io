---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49396addinductive.html
---

## Stream: [general](index.html)
### Topic: [add_inductive](49396addinductive.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 21 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010223):
Why does
```
tactic.add_inductive `foo [] 0 `(Type) $
[(`mk, expr.pi `mk binder_info.default (expr.app (expr.const `list [level.zero]) (expr.const `foo [])) (expr.const `foo []))],
```
fail?

#### [ Sebastian Ullrich (Mar 21 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010398):
That's a nested inductive type, `add_inductive` only supports basic inductive types

#### [ Jakob von Raumer (Mar 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010420):
Too bad, and there's no API for the nested ones, right?

#### [ Sebastian Ullrich (Mar 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010467):
Right

#### [ Jakob von Raumer (Mar 21 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010567):
But are they internally reduced to basic inductive types?

#### [ Kevin Buzzard (Mar 21 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010636):
That's what is claimed in section 7.9 of TPIL : https://leanprover.github.io/theorem_proving_in_lean/inductive_types.html#mutual-and-nested-inductive-types

#### [ Sebastian Ullrich (Mar 21 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010637):
Yes https://github.com/leanprover/lean/wiki/Compiling-nested-inductive-types

#### [ Jakob von Raumer (Mar 21 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010694):
Nice, thanks!

#### [ Jakob von Raumer (Mar 21 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010830):
This is done in C++ but outside the kernel, right?

#### [ Mario Carneiro (Mar 21 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010832):
yes

#### [ Jakob von Raumer (Mar 21 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010842):
Why isn't it done in Lean?

#### [ Mario Carneiro (Mar 21 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010976):
It could be...

#### [ Mario Carneiro (Mar 21 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124011034):
I started working on that a while back, but then the ground started shaking and I decided to wait for the dust to settle

#### [ Moses Schönfinkel (Mar 21 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124011580):
Very poetic!


{% endraw %}
