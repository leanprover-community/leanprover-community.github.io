---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35875semimodulesmoremoduleheadaches.html
---

## Stream: [general](index.html)
### Topic: [semimodules, more module headaches](35875semimodulesmoremoduleheadaches.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133678716):
@**Johannes Hölzl** I had problems with using `smul_add'` directly on modules, so I had to duplicate the theorems [here](https://github.com/leanprover/mathlib/blob/b33764d942dc8b1b7f55cace89429c948c1a4b2f/algebra/module.lean#L38-L43). Do you have any ideas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 10 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133679172):
hm, are the problems related to projecting the ring to semirings? I think we might also get problems with field to rings for vector spaces...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133679278):
I vote for making `vector_space` notation or abbreviation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 10 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133680412):
Making `vector_space` an abbreviation is okay for me.
But I'm not sure if this solves our problems here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133680743):
yes, `rw` fails because it can't derive the semiring instance (at the right time)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133680836):
I am going to try implementing a solution I mentioned a while ago and not have `module` extend `add_comm_group` but take it as an argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 10 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133681100):
hm, how does this help?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133685721):
It avoids the `ring ?` problem in that typeclass searches for e.g. `has_zero A` go via `add_comm_group A` to `module ? A` and then to `ring ?`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133685804):
But I've stumbled on yet another inexplicable lean bug while attempting this. I've only lightly minimized
```lean
import algebra.big_operators

universes u v
variables {α : Type u} {β : Type v}

class has_scalar (α : out_param $ Type u) (γ : Type v) := (smul : α → γ → γ)

infixr ` • `:73 := has_scalar.smul

class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  [add_comm_group β] extends has_scalar α β

class is_submodule {α : Type u} {β : Type v} [ring α]
  [add_comm_group β] [module α β] (p : set β) : Prop :=
(zero' : (0:β) ∈ p)
(add' : ∀ {x y}, x ∈ p → y ∈ p → x + y ∈ p)
(smul : ∀ c {x}, x ∈ p → c • x ∈ p)

namespace is_submodule
variables [ring α] [add_comm_group β] [module α β] {p : set β} [is_submodule p]
include α

lemma zero : (0 : β) ∈ p := zero' α _

example : (0 : β) ∈ p := by simp [zero] -- fails

end is_submodule
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133685958):
`by apply zero` also fails, but `by refine zero` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133686066):
the failing instance problem:
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : @is_submodule ?m__fresh.1533.3973 β ?m__fresh.1533.3975 _inst_2 ?m__fresh.1533.3977 p := _inst_4
failed is_def_eq
```


{% endraw %}
