---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/69812Ismathlibbrokencurrentlyno.html
---

## [maths](index.html)
### [Is mathlib broken currently? (no)](69812Ismathlibbrokencurrentlyno.html)

#### [Kevin Buzzard (Sep 06 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133406331):
```lean
import ring_theory.ideals

def is_fg {α β} [ring α] [module α β]
  (s : set β) [is_submodule s] : Prop :=
∃ t : finset β, _root_.span ↑t = s

/-
maximum class-instance resolution depth has been reached
 (the limit can be increased by setting option 'class.instance_max_depth')
  (the class-instance resolution trace can be visualized by setting option
   'trace.class_instances')
-/
```
I think I'm up to date. This is from the Noetherian branch of community mathlib but it doesn't seem to work with (non-community) mathlib master either.

#### [Kevin Buzzard (Sep 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133406390):
hmm on the other hand I just managed to compile mathlib master so I don't know what's going on.

#### [Kevin Buzzard (Sep 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133406443):
It's the coercion from finset beta to set beta which seems to cause the loop

#### [Johannes Hölzl (Sep 06 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133408030):
`(2) ?x_7 : has_coe (finset β) ?x_5 := @quotient_ring.has_coe ?x_9 ?x_10 ?x_11 ?x_12`
ouch, doesn't seam to be a good coercion rule...

#### [Johannes Hölzl (Sep 06 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133408329):
not this one but the `quotient_module` one

#### [Johannes Hölzl (Sep 06 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133408472):
it should work now

#### [Mario Carneiro (Sep 06 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133409247):
This is the same kind of problem as in `option.has_coe`. You can't coerce out of an arbitrary type in `has_coe`, you have to use `has_coe_t` directly

#### [Johannes Hölzl (Sep 06 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133409438):
hm, then it needs to be changed further. I just fixed the implicit instead of instance for the out_param problem.

#### [Kevin Buzzard (Sep 06 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133425189):
I'm sick of not being able to understand and debug this stuff. What happened in practice is that I wanted to do a bit more work on the noetherian branch yesterday evening but instead spent 30 minutes pulling, rebasing and compiling mathlib because I could see the error and I could not see how to fix it, I could only see how to try and get up to date and hope the error would go away. I would like to learn how to diagnose and fix what just happened and I still find these traces intimidating. Because I don't understand the traces I spent some time looking through recent mathlib commits to try and spot some suspicious looking instances but I couldn't find any. My next step would have been to go through each commit in mathlib, because I know the code worked last week and it didn't work yesterday, to try and find the offending one, but I suspect that neither of you did this.

OK so I still have a borked noetherian branch [because I didn't update yet]. Presumably I start with `set_option trace.class_instances true`. I now get 100+ lines of output. Here is a random snippet:

```lean
[class_instances] (13) ?x_94 : ring ?x_93 := @cau_seq.ring ?x_97 ?x_98 ?x_99 ?x_100 ?x_101 ?x_102
[class_instances] (14) ?x_98 : discrete_linear_ordered_field ?x_97 := rat.discrete_linear_ordered_field
[class_instances] (14) ?x_100 : ring ?x_99 := _inst_1
[class_instances] (14) ?x_102 : @is_absolute_value ℚ rat.discrete_linear_ordered_field α _inst_1 ?x_101 := @abs_is_absolute_value ?x_103 ?x_104
failed is_def_eq
[class_instances] (14) ?x_100 : ring ?x_99 := @cau_seq.ring ?x_103 ?x_104 ?x_105 ?x_106 ?x_107 ?x_108
[class_instances] (15) ?x_104 : discrete_linear_ordered_field ?x_103 := rat.discrete_linear_ordered_field
[class_instances] (15) ?x_106 : ring ?x_105 := _inst_1
[class_instances] (15) ?x_108 : @is_absolute_value ℚ rat.discrete_linear_ordered_field α _inst_1 ?x_107 := @abs_is_absolute_value ?x_109 ?x_110
failed is_def_eq
```

That's not the relevant part, because I have no idea how to read this in detail or what the relevant part is. Let me instead say what I see when I look at this output. Firstly the numbers in brackets near the beginning of each line ((13),(14),(15)) are slowly increasing, which probably means there's a loop. Looking more carefully it seems that other than these numbers and the names of metavariables, the output is periodic with period 4, which means there really is a loop. Looking at the output in more detail, I see `?x_100 : ring ?x_99` and I know from the experience that this is the line which makes Mario say "aah, something is wrong, because that should never happen". I still don't understand why, because I don't understand what the output represents. What does it represent? Lean is trying to prove that something is a ring -- that doesn't sound too bad to me; sometimes it is supposed to do that. So far I have managed to diagnose that something is wrong and I need to ask for help. 

The full 200+ line output is here:

https://gist.github.com/kbuzzard/e113b65c54e35bff839fb88365811ef5

There is now no hurry on this (hopefully) but if at some point someone could explain how to get from it to the diagnosis above (which I must admit I do not fully understand -- but I see the words "it should work now" which I am very grateful for -- thanks Johannes!), I'd be much obliged.

#### [Kevin Buzzard (Sep 06 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133430208):
PS I can confirm that the noetherian branch is now building again (and also that I am unsure whether I should be merging or rebasing when I update mathlib-community from mathlib master and then update the noetherian branch, or indeed whether it even matters).

