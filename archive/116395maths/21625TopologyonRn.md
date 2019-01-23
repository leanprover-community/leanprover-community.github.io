---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/21625TopologyonRn.html
---

## Stream: [maths](index.html)
### Topic: [Topology on R^n](21625TopologyonRn.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528202):
I have the following code
```lean
import analysis.topology.topological_space analysis.real data.finsupp
open classical

definition type_pow : Type* → ℕ → Type*
| α 0       := unit
| α (n+1) := type_pow α n × α

instance type_pow_instance : has_pow Type* ℕ := ⟨type_pow⟩

definition sum_in_Rn : Π (n : ℕ), ℝ^n → ℝ
| 0      x    :=  0
| (m+1) (x,y) := (sum_in_Rn m x) + y

definition standard_simplex (n : ℕ) : set (ℝ^(n+1)) := λ x, sum_in_Rn (n+1) x = 1

namespace standard_simplex

variable {n : ℕ}

definition topology_Rn : Π (n : ℕ), topological_space (ℝ^n)
| 0     := begin show topological_space unit, apply_instance end
| (n+1) := begin show topological_space (_ × _),
 have t₁ : topological_space (type_pow ℝ (nat.add n 0)) := topology_Rn n,
 have t₂ : topological_space ℝ, begin apply_instance end,
 exact topological_space.induced prod.fst t₁ ⊔ topological_space.induced prod.snd t₂,
 end

definition inclusion : standard_simplex n → ℝ^(n+1) := λ x, x

instance : topological_space (standard_simplex n)
 := topological_space.induced inclusion (@topology_Rn (n+1))

end standard_simplex
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528205):
I get red squiggles under `topology_Rn`, in its definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528226):
The error is: `rec_fn_macro only allowed in meta definitions`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528267):
So, two questions: how do I get lean to automatically deduce the topology on R^n on the second line of the induction? There is already an instance of `topological_space (α × β)`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528272):
The second is, how did I get this error, if I only copied a line from the proof of `topological_space (α × β)`...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528752):
It looks like you need to mark your definition`noncomputable` (or your entire theory).

But in general I would not advice to use this type construction. I think for `R ^ n`there are two options: Use `vec n R` (define the canonical topology on lists using `lfp`, and then use subtype for `vec`), or use `fin n -> R` and use the topological space construction on function spaces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528822):
The advantage of seeing `R^n` as a function space is that you can do a lot of proofs assuming arbitrary functions, and no induction is necessary on your type itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 14 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528935):
@**Johan Commelin** You stumbled upon this bug: https://github.com/leanprover/lean/issues/1890  The unsoundness issue was fixed last year, but apparently there are still cases where you can accidentally use general recursion in non-meta definitions.  The culprit is the `begin apply_instance end`, which defines t₂ in terms of itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528991):
So.. how do I fix it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126528995):
I some how wish I could skip those `have`-lines anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529047):
The system should figure that out itself..., although maybe the first `have`-line is to hard for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529049):
```quote
So.. how do I fix it?
```
Seriously: Use another type!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529069):
Like what? (Confused newbie behind this keyboard...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529144):
Use `fin n -> R`, the topological space is already setup, i.e. it only needs the instance for `α → β` where `β` has a topological space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529208):
Ok, I'll try that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 14 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126529325):
> So.. how do I fix it?

Aside from "don't do it" as Johannes already said, the main thing you can try if you see this bug is to move the `have` statements out of the begin-end block.  In this case, it is enough if you move just the `have t₁` before the begin.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530333):
@**Johannes Hölzl** Ok, so now I have `fin n \to \R`, but how do I get a topology on it? Because I can't find the instance that you just described...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530364):
Hm, works here:
```lean
import analysis.real

def test {α : Type*} {n:ℕ} [t : topological_space α] : topological_space (fin n → α) :=
by apply_instance

#print test
/-
def test : Π {α : Type u_1} {n : ℕ} [t : topological_space α], topological_space (fin n → α) :=
λ {α : Type u_1} {n : ℕ} [t : topological_space α], Pi.topological_space
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530429):
Or more specific
```lean
noncomputable def test {n:ℕ} : topological_space (fin n → ℝ) :=
by apply_instance

set_option pp.all true
#print test
/-
noncomputable def test : Π {n : nat}, topological_space.{0} (fin n → real) :=
λ {n : nat},
  @Pi.topological_space.{0 0} (fin n) (λ (a : fin n), real)
    (λ (a : fin n),
       @uniform_space.to_topological_space.{0} real (@metric_space.to_uniform_space'.{0} real real.metric_space))
-/
```

Don't forget `noncomputable` Maybe you want to setup it for your theory: use `noncomputable theory`  at the beginning (after the imports)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530805):
Ok, that helped.
```lean
definition topology_Rn : Π (n : ℕ), topological_space (ℝ^n) :=
begin
intros n, show topological_space (fin n → ℝ), apply_instance,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20on%20R%5En/near/126530844):
Not term-mode, but I don't care too much (-;

