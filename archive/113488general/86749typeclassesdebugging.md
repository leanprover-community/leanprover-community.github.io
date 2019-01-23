---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86749typeclassesdebugging.html
---

## Stream: [general](index.html)
### Topic: [type classes debugging](86749typeclassesdebugging.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 29 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707443):
A t2 space is a topological space with some separation property. Every metric space is a t2 space. If you try
```lean
lemma success {α : Type u} [metric_space α] (s : set α) : true :=
begin
  letI : t2_space s := by apply_instance,
  trivial
end
```
it works fine: the subset `s` of `α` inherits a metric space structure, and is therefore t2. Now, try
```lean
lemma fail (s : set ℝ) : true :=
begin
  letI : t2_space s := by apply_instance,
  trivial
end
```
This should be a special case of the previous one, but it loops forever. I have no idea how to debug this kind of behavior.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707631):
```lean
subtype.metric_space :
  Π {α : Type u_1} [_inst_1 : metric_space α] {p : α → Prop} [t : metric_space α], metric_space (subtype p)
```
problematic instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707791):
```lean
orderable_topology.t2_space :
  ∀ {α : Type u_1} [_inst_1 : topological_space α] [_inst_2 : linear_order α] [t : orderable_topology α],
    t2_space α
```

```lean
ordered_topology.to_t2_space :
  ∀ {α : Type u_1} [_inst_1 : topological_space α] [_inst_2 : partial_order α] [t : ordered_topology α],
    t2_space α
```

Lean got stuck trying these two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707797):
because R has like 10000 properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707804):
and the typeclass instance system is not clever enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707852):
```lean
local attribute [instance, priority 0] orderable_topology.t2_space
local attribute [instance, priority 0] ordered_topology.to_t2_space
```
putting these two lines before the lemma is one solution @**Sebastien Gouezel**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 29 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152708153):
This works perfectly (and also in my use case, which involves subtypes of something more complicated than R). Thanks a lot! Could you tell us how you located the problematic instances?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152708162):
I just... read through the instance trace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 29 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152708502):
Just to be sure: before the statement of the lemma, I insert
```lean
set_option trace.class_instances true
set_option class.instance_max_depth 15
```
(the second line to ensure that the process terminates in a reasonable amount of time, the first one to get access to the trace). Then if I put the cursor on `apply_instance`, I get access to the trace. There, I can see indeed a lot of `@orderable_topology ↥s`. And I can see at depth (0) that it tries `@orderable_topology.t2_space`, and gets stuck there. OK, thanks again, I think I will be able to do this by myself next time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152715634):
Not sure I get what the problem is. Is the `orderable_topology.t2_space` a wrong turn for the typeclass inference? I guess R is an orderable topology so I don't see the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152715681):
Although I guess `ordered_topology.to_t2_space` implies `orderable_topology.t2_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152715853):
I think I had the same issue at https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/t2_space/near/147451283

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Dec 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716158):
I don't understand what is going on. The trace output is filled with entries like
```lean
[class_instances] (1) ?x_4 : @orderable_topology ↥s
  (@uniform_space.to_topological_space ↥s
     (@metric_space.to_uniform_space' ↥s
        (@subtype.metric_space ℝ real.metric_space (λ (x : ℝ), x ∈ s)
           (@normed_group.to_metric_space ℝ
              (@normed_space.to_normed_group ℝ ℝ real.normed_field
                 (@normed_field.to_normed_space ℝ real.normed_field))))))
  (@linear_order.to_partial_order ↥s
     (@subtype.linear_order ℝ
        (@linear_ordered_semiring.to_linear_order ℝ
           (@decidable_linear_ordered_semiring.to_linear_ordered_semiring ℝ real.decidable_linear_ordered_semiring))
        (λ (x : ℝ), x ∈ s))) := ennreal.orderable_topology
failed is_def_eq
```
or
```lean
[class_instances] (1) ?x_4 : @orderable_topology ↥s
  (@uniform_space.to_topological_space ↥s
     (@metric_space.to_uniform_space' ↥s
        (@subtype.metric_space ℝ real.metric_space (λ (x : ℝ), x ∈ s)
           (@normed_group.to_metric_space ℝ
              (@normed_space.to_normed_group ℝ ℝ real.normed_field
                 (@normed_field.to_normed_space ℝ real.normed_field))))))
  (@linear_order.to_partial_order ↥s
     (@subtype.linear_order ℝ
        (@decidable_linear_order.to_linear_order ℝ
           (@conditionally_complete_linear_order.to_decidable_linear_order ℝ
              real.lattice.conditionally_complete_linear_order))
        (λ (x : ℝ), x ∈ s))) := ennreal.orderable_topology
failed is_def_eq
```
or
```lean
[class_instances] (1) ?x_4 : @orderable_topology ↥s
  (@uniform_space.to_topological_space ↥s
     (@metric_space.to_uniform_space' ↥s
        (@subtype.metric_space ℝ real.metric_space (λ (x : ℝ), x ∈ s)
           (@normed_group.to_metric_space ℝ
              (@normed_ring.to_normed_group ℝ (@normed_field.to_normed_ring ℝ real.normed_field))))))
  (@linear_order.to_partial_order ↥s
     (@subtype.linear_order ℝ
        (@linear_ordered_semiring.to_linear_order ℝ
           (@linear_ordered_ring.to_linear_ordered_semiring ℝ
              (@linear_ordered_field.to_linear_ordered_ring ℝ
                 (@discrete_linear_ordered_field.to_linear_ordered_field ℝ real.discrete_linear_ordered_field))))
        (λ (x : ℝ), x ∈ s))) := ennreal.orderable_topology
failed is_def_eq
```
All of them are subtly different. There are so many ways to use the different structures on ℝ that it gives rise to an exponential blowup. And, while lean has not checked that all the possibilities fail, it will not go and try a more successful path.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716218):
surely depth-first search is troublesome... but that doesn't mean breadth-first search would have no problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716611):
aha, even though R is an orderable topology its subspaces aren't necessarily

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716666):
I think the `top_space` and `linear_order` arguments should be implicit in the two `t2_space` instances


{% endraw %}
