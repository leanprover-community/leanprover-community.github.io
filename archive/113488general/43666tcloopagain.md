---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43666tcloopagain.html
---

## Stream: [general](index.html)
### Topic: [tc loop again](43666tcloopagain.html)

---

#### [Patrick Massot (May 28 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127213712):
I tried to define norms on indexed product, but it seems I have a type class loop again. It's dinner time here, but if someone wants to have a look at why https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean#L319 fails I'd be very grateful

#### [Nicholas Scheel (May 28 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127213727):
does `begin admit end` act any differently?

#### [Patrick Massot (May 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127220182):
No. I can replace the infinite loop by weirder error messages using `refine` but that's all I can get

#### [Patrick Massot (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127271172):
@**Mario Carneiro** could you have a look at this issue if you have some time please? This only other it depends on is Johannes' https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/metric_space_fintype_pi.lean

#### [Kevin Buzzard (May 30 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277524):
This would be so much easier to do if you could minimise

#### [Kevin Buzzard (May 30 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277533):
cutting and pasting one file works

#### [Kevin Buzzard (May 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277569):
even cutting and pasting the file you import would be better than this

#### [Kevin Buzzard (May 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277583):
I don't want to dump Johannes' file into the project I have open

#### [Kevin Buzzard (May 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277586):
if I put it in scratch then I don't know how to import it

#### [Kevin Buzzard (May 30 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277604):
I mean -- even if it's a huge gist -- for *me* at least, one file is a whole lot easier than two

#### [Kevin Buzzard (May 30 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279386):
https://gist.github.com/kbuzzard/e8c1b1ac3d50795b1bdf3094bc823de6

#### [Kevin Buzzard (May 30 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279387):
there's the error

#### [Kevin Buzzard (May 30 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279694):
so you made all these instances in this file and they are all those terrifying things like normed space to normed group, and then product of normed spaces is a normed space and product of normed groups is a normed group. Are all these safe? Is this unrelated to your problem?

#### [Kevin Buzzard (May 30 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279851):
Patrick I wrote the error to a file, and then deleted all the lines with failed is_def_eq underneath and now it looks like this:

#### [Mario Carneiro (May 30 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279854):
The problem is in the very first few lines. 
```
[class_instances] (0) ?x_2 : @module ?x_0 (Π (i : ι), E i) ?x_1 := @pi.module ?x_3 ?x_4 ?x_5 ?x_6 ?x_7
[class_instances] (1) ?x_6 : ring ?x_5 := @prod.ring ?x_8 ?x_9 ?x_10 ?x_11
failed is_def_eq
```
After matching `pi.module` for the typeclass, it immediately attempts to resolve `?x_6`, which is the `[ring A]` argument

#### [Kevin Buzzard (May 30 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279863):
```
[class_instances] (8) ?x_70 : @is_absolute_value ℝ real.discrete_linear_ordered_field α
  (@normed_ring.to_ring α (@normed_field.to_normed_ring α _inst_1))
[class_instances] (8) ?x_68 : ring ?x_67 := @cau_seq.ring ?x_74 ?x_75 ?x_76 ?x_77 ?x_78 ?x_79
[class_instances] (9) ?x_75 : discrete_linear_ordered_field ?x_74 := real.discrete_linear_ordered_field
[class_instances] (9) ?x_77 : ring ?x_76 := @normed_ring.to_ring ?x_84 ?x_85
[class_instances] (10) ?x_85 : normed_ring ?x_84 := @normed_field.to_normed_ring ?x_86 ?x_87
[class_instances] (11) ?x_87 : normed_field ?x_86 := _inst_1
[class_instances] (9) ?x_79 : @is_absolute_value ℝ real.discrete_linear_ordered_field α
```

#### [Kevin Buzzard (May 30 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279864):
that's the period

#### [Kevin Buzzard (May 30 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279867):
with the number going up each time

#### [Mario Carneiro (May 30 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279909):
but since it hasn't figured out `?x_5` yet, it's on a wild goose chase to come up with a ring, any ring, and it gets caught up in a loop somewhere with some iterating ring construction

#### [Kevin Buzzard (May 30 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279918):
So the red flag for you is the attempt to prove `ring ?x_5`

#### [Mario Carneiro (May 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279923):
right

#### [Mario Carneiro (May 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279936):
you can see that also in the period; the number is the stack depth, so you can see it's recursing each time on a `ring ?` goal

#### [Kevin Buzzard (May 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279984):
```
[class_instances] (1) ?x_6 : ring ?x_5 := @prod.ring ?x_8 ?x_9 ?x_10 ?x_11
failed is_def_eq
[class_instances] (1) ?x_6 : ring ?x_5 := @normed_ring.to_ring ?x_12 ?x_13
[class_instances] (2) ?x_13 : normed_ring ?x_12 := @normed_field.to_normed_ring ?x_14 ?x_15
[class_instances] (3) ?x_15 : normed_field ?x_14 := _inst_1

#### [Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279988):
It looks like it solves it there

#### [Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279992):
it can prove it's a ring if it proves it's a normed ring

#### [Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279993):
or a normed field

#### [Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279994):
and something was a normed field at the time

#### [Mario Carneiro (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279996):
it solves a subgoal, but it hasn't solved the main goal

#### [Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279997):
has it solved ring ?x_5?

#### [Mario Carneiro (May 30 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280041):
no, the last (1) line is line 27 which is a `ring ?x_5` goal

#### [Kevin Buzzard (May 30 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280053):
the line after I quoted

#### [Kevin Buzzard (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280104):
`[class_instances] (1) ?x_6 : ring ?x_5 := @cau_seq.ring ?x_11 ?x_12 ?x_13 ?x_14 ?x_15 ?x_16`
`

#### [Mario Carneiro (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280109):
The role of `cau_seq.ring` here is that it produces a ring from a ring

#### [Kevin Buzzard (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280110):
I thought I'd seen the last of it

#### [Mario Carneiro (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280117):
so it's building a ring of the form `(cau_seq (cau_seq (cau_seq ? ?) ?) ?)`

#### [Mario Carneiro (May 30 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280136):
the fault isn't `cau_seq` though, that was just the first recursing construction it fell upon

#### [Kevin Buzzard (May 30 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280137):
`[class_instances] (9) ?x_77 : ring ?x_76 := @cau_seq.ring ?x_83 ?x_84 ?x_85 ?x_86 ?x_87 ?x_88`

#### [Kevin Buzzard (May 30 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280139):
There's the last `(9)`

#### [Mario Carneiro (May 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280184):
The real problem is that it's solving `ring ?`

#### [Kevin Buzzard (May 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280192):
`cau_seq.ring :
  Π {α : Type u_3} [_inst_1 : discrete_linear_ordered_field α] {β : Type u_4} [_inst_2 : ring β] {abv : β → α}
  [_inst_3 : is_absolute_value abv], ring (cau_seq β abv)`

#### [Kevin Buzzard (May 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280198):
"you give me a ring, I'll give you another ring"

#### [Mario Carneiro (May 30 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280268):
@**Sebastian Ullrich** Why don't out_params work here? Adding `out_param` to `pi.module` does not change the order of inference for the arguments

#### [Mario Carneiro (May 30 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280339):
maybe it has to do with the fact that the `module` argument is in a pi?

#### [Kevin Buzzard (May 30 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280417):
It's funny that `instance product_normed_space : normed_space α (E × F) ` works

#### [Kevin Buzzard (May 30 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280422):
but then `instance fintype.normed_space {ι : Type*} {E : ι → Type*} [fintype ι] [∀i, normed_space α (E i)]` gives him trouble

#### [Mario Carneiro (May 30 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280915):
Here's a minimized version:
```
class ring' (α : Type*).

class module' (α : out_param $ Type*) (β : Type*) [out_param $ ring' α].

class normed_field' (α : Type*) extends ring' α.

class normed_space' (α : out_param $ Type*) (β : Type*) [out_param $ normed_field' α] extends module' α β.

instance pi.module' {I : Type*} {f : I → Type*}
 {α : out_param Type*} [out_param $ ring' α] [∀ i, module' α $ f i] : module' α (Π i : I, f i) :=
sorry

instance loop (α) [ring' α] : ring' (option α) := sorry

set_option trace.class_instances true

instance fintype.normed_space' {α} [normed_field' α]
  {ι : Type*} {E : ι → Type*} [∀i, normed_space' α (E i)] :
  normed_space' α (Πi, E i) :=
⟨_, _⟩
```

#### [Mario Carneiro (May 30 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280979):
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_2 : @module' ?x_0 (Π (i : ι), E i) ?x_1 := @pi.module' ?x_3 ?x_4 ?x_5 ?x_6 ?x_7
[class_instances] (1) ?x_6 : out_param (ring' ?x_5) := @loop ?x_8 ?x_9
[class_instances] (2) ?x_9 : ring' ?x_8 := @loop ?x_10 ?x_11
[class_instances] (3) ?x_11 : ring' ?x_10 := @loop ?x_12 ?x_13
[class_instances] (4) ?x_13 : ring' ?x_12 := @loop ?x_14 ?x_15
...
```

#### [Mario Carneiro (May 30 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127286141):
@**Johannes Hölzl** I think we should just abandon the `out_param` in module and live with having to give the type explicitly in scalar multiplication. It's too brittle and there is very little I can do about these issues without modifying lean.

#### [Patrick Massot (May 30 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293689):
Thank you very much Mario and Kevin. I understood what was happening, the question is how to solve this (and I also wanted to point out to Sebastian that out_param stuff maybe requires more thinking in Lean 4, I don't know).

#### [Patrick Massot (May 30 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293699):
What confuses me is:
```lean
example {ι : Type*} {E : ι → Type*} [fintype ι] [∀i, vector_space α (E i)] :
  vector_space α (Πi, E i) := by apply_instance
```
works fine

#### [Patrick Massot (May 30 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293706):
But the type class mechanism doesn't search for this. Why?

#### [Patrick Massot (May 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293750):
Is there any way I could help the type class search here?

#### [Patrick Massot (May 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293764):
`vector_space` is very closely related to `module`, the full definition is simply `class vector_space (α : out_param $ Type u) (β : Type v) [field α] extends module α β`

#### [Patrick Massot (May 30 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293839):
but I would still naively expect the search that is currently failing to start by looking for some `vector_space α (Πi, E i)` rather than `@module ?x_0 (Π (i : ι), E i) ?x_1`

#### [Patrick Massot (May 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293945):
Note that the working instance here is `pi.vector_space` whose definition is literally: `instance vector_space (α : Type*) [field α] [∀ i, vector_space α $ f i] : vector_space α (Π i : I, f i) :=
{ ..pi.module }`

#### [Sebastian Ullrich (May 30 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127294838):
@**Mario Carneiro** Do you want
```
instance pi.module' {I : Type*} {f : I → Type*}
 {α : Type*} {r : ring' α} [∀ i, module' α (f i)] : module' α (Π i : I, f i) :=
```
?

#### [Johannes Hölzl (May 30 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298089):
@**Sebastian Ullrich** this still loops. One problem is that it looks for `@module' ?x_0 (Π (i : ι), E i) ?x_1` instead of`@module' α (Π (i : ι), E i) ?x_1` . Then the type class inference loops by making `loop` steps.

#### [Sebastian Ullrich (May 30 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298146):
It doesn't loop in Mario's example

#### [Johannes Hölzl (May 30 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298202):
Ah, sorry, I didn't see that you also changed `[ring' α]` to `{r : ring' α}`.

#### [Sebastian Ullrich (May 30 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298212):
Yes, that's the important part :) . `instance` doesn't do anything special with `out_param`.

#### [Sebastian Ullrich (May 30 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298320):
The intended meaning behind making it implicit is "don't try to infer an instance at this point, we don't even know α yet".

#### [Johannes Hölzl (May 30 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298985):
Thanks, this is a good explanation. It doesn't work now, but it seams to be a problem that the pi instance can not be applied.

#### [Patrick Massot (May 31 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127349063):
So, do we have a solution?

