---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97486trolledbyundergrad.html
---

## Stream: [general](index.html)
### Topic: [trolled by undergrad](97486trolledbyundergrad.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 20 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130014811):
It took me 20 minutes to diagnose this deterministic time-out:

```lean
import analysis.real 

theorem infinite_cover {a b : ℝ} {c : set (set ℝ)} (n : ℕ) :
∃ k : ℕ, 1 ≤ k ≤ n ∧ ∀ c' ⊆ c, {r : ℝ | a+(k-1)*(a+b)/n ≤ r ∧ r ≤ a+k*(a+b)/n} ⊆ ⋃₀ c' → ¬ set.finite c' := sorry
```

In my defence, the code was far longer to begin with, and probably about 15 were spent reducing it to this.

#### [ Kevin Buzzard (Jul 20 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015487):
I'm about to set off for home and I'll spill the beans if nobody has spotted it by the time I get in

#### [ Patrick Massot (Jul 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015541):
I don't understand what you are asking for

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015604):
Cut and paste that code -- it times out

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015613):
deterministic time-out

#### [ Chris Hughes (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015615):
`1 ≤ k ≤ n`

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015618):
:-)

#### [ Kevin Buzzard (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015625):
I spotted it when I changed `n` to `1`

#### [ Kevin Buzzard (Jul 20 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015658):
I was quite surprised that the statement managed to parse

#### [ Kevin Buzzard (Jul 20 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015659):
in retrospect

#### [ Mario Carneiro (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015677):
because obviously `k ≤ n` is also a nat

#### [ Mario Carneiro (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015719):
bigger than one no less

#### [ Chris Hughes (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130015737):
is `≤` left or right associative?

#### [ Mario Carneiro (Jul 20 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016247):
left assoc, my bad

#### [ Mario Carneiro (Jul 20 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016271):
```
infix ≤        := has_le.le
```
`infix` means `infixl`

#### [ Mario Carneiro (Jul 20 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016335):
oh I see so it tried to find a Prop coercion for `n`

#### [ Mario Carneiro (Jul 20 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016351):
and then it means "if `1 <= k` then `n`"

#### [ Mario Carneiro (Jul 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016440):
`1 ≤ k ≤ (n ≤ 1)` parses just fine

#### [ Chris Hughes (Jul 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016450):
Because Prop has an order structure for some reason.

#### [ Mario Carneiro (Jul 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016464):
because Prop has a natural order structure...

#### [ Mario Carneiro (Jul 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016479):
which we use funky notation for

#### [ Mario Carneiro (Jul 20 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130016545):
In fact I'm pretty sure boolean algebras are basically generalized Prop

#### [ Mario Carneiro (Jul 21 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130035267):
@**Sebastian Ullrich** I just noticed that this error is a bit subtler than expected. It doesn't give a instance overflow error, it times out and produces no output in the trace. Do you know how the typeclass instance mechanism could run out of time without overflowing?

#### [ Mario Carneiro (Jul 21 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130035317):
example without trolling:
```
import analysis.real
example (n : ℕ) : Prop := n
```

#### [ Mario Carneiro (Jul 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130036027):
Ah, I finally got an instance trace, and it does something I didn't think the typeclass inference engine does: it repeatedly does the same search, at the same depth level, which is why it timeouts from iteration rather than recursion. Here's the beginning, with the depth shown using indentation:
```
(0) ?x_3 : has_coe_to_sort ℕ := @coe_sort_trans ?x_5 ?x_6 ?x_7 ?x_8
 (1) ?x_7 : has_coe_t_aux ℕ ?x_6 := @coe_base_aux ?x_9 ?x_10 ?x_11
  (2) ?x_11 : has_coe ℕ ?x_10 := int.has_coe
 (1) ?x_8 : has_coe_to_sort ℤ := @coe_sort_trans ?x_22 ?x_23 ?x_24 ?x_25
  (2) ?x_24 : has_coe_t_aux ℤ ?x_23 := @coe_base_aux ?x_26 ?x_27 ?x_28
   (3) ?x_28 : has_coe ℤ ?x_27 := @int.cast_coe ?x_49 ?x_50 ?x_51 ?x_52 ?x_53
    (4) ?x_50 : has_zero ?x_49 := real.has_zero
    (4) ?x_51 : has_one ℝ := real.has_one
    (4) ?x_52 : has_add ℝ := real.has_add
    (4) ?x_53 : has_neg ℝ := real.has_neg
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_55 ?x_56 ?x_57 ?x_58
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_base_aux ?x_59 ?x_60 ?x_61
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_trans_aux ?x_59 ?x_60 ?x_61 ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @lattice.boolean_algebra.to_has_neg ?x_60 ?x_61
     (5) ?x_61 : lattice.boolean_algebra ℝ := @lattice.complete_boolean_algebra.to_boolean_algebra ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @add_group.to_has_neg ?x_55 ?x_56
     (5) ?x_56 : add_group ℝ := real.add_group
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_58 ?x_59 ?x_60 ?x_61
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_base_aux ?x_62 ?x_63 ?x_64
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_trans_aux ?x_62 ?x_63 ?x_64 ?x_65 ?x_66
     (5) ?x_56 : add_group ℝ := @add_comm_group.to_add_group ?x_59 ?x_60
      (6) ?x_60 : add_comm_group ℝ := real.add_comm_group
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_62 ?x_63 ?x_64 ?x_65
   (3) ?x_64 : has_coe_t_aux ℝ ?x_63 := @coe_base_aux ?x_66 ?x_67 ?x_68
   (3) ?x_64 : has_coe_t_aux ℝ ?x_63 := @coe_trans_aux ?x_66 ?x_67 ?x_68 ?x_69 ?x_70
      (6) ?x_60 : add_comm_group ℝ := @nonneg_comm_group.to_add_comm_group ?x_61 ?x_62
       (7) ?x_62 : nonneg_comm_group ℝ := @linear_nonneg_ring.to_nonneg_comm_group ?x_63 ?x_64
       (7) ?x_62 : nonneg_comm_group ℝ := @nonneg_ring.to_nonneg_comm_group ?x_63 ?x_64
        (8) ?x_64 : nonneg_ring ℝ := @linear_nonneg_ring.to_nonneg_ring ?x_65 ?x_66
      (6) ?x_60 : add_comm_group ℝ := @ring.to_add_comm_group ?x_63 ?x_64
       (7) ?x_64 : ring ℝ := real.ring
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_66 ?x_67 ?x_68 ?x_69
   (3) ?x_68 : has_coe_t_aux ℝ ?x_67 := @coe_base_aux ?x_70 ?x_71 ?x_72
   (3) ?x_68 : has_coe_t_aux ℝ ?x_67 := @coe_trans_aux ?x_70 ?x_71 ?x_72 ?x_73 ?x_74
       (7) ?x_64 : ring ℝ := @nonneg_ring.to_ring ?x_71 ?x_72
        (8) ?x_72 : nonneg_ring ℝ := @linear_nonneg_ring.to_nonneg_ring ?x_73 ?x_74
       (7) ?x_64 : ring ℝ := @domain.to_ring ?x_65 ?x_66
        (8) ?x_66 : domain ℝ := real.domain
```

#### [ Mario Carneiro (Jul 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130036032):
notice that `(2) ?x_25 : has_coe_to_sort ℝ` keeps coming up; this continues for all 38000 lines of output before it times out

#### [ Mario Carneiro (Jul 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130037002):
Oh whoa I just figured out why this is happening, and why it's called a "prolog-like search" - nota bene @**Kevin Buzzard**  :)

Whenever it tries something which doesn't work, it reverts all the metavariable assignments up to that point and then tries again. Like here around the newline:
```
  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_55 ?x_56 ?x_57 ?x_58
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_base_aux ?x_59 ?x_60 ?x_61
   (3) ?x_57 : has_coe_t_aux ℝ ?x_56 := @coe_trans_aux ?x_59 ?x_60 ?x_61 ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @lattice.boolean_algebra.to_has_neg ?x_60 ?x_61
     (5) ?x_61 : lattice.boolean_algebra ℝ := @lattice.complete_boolean_algebra.to_boolean_algebra ?x_62 ?x_63
    (4) ?x_53 : has_neg ℝ := @add_group.to_has_neg ?x_55 ?x_56
     (5) ?x_56 : add_group ℝ := real.add_group

  (2) ?x_25 : has_coe_to_sort ℝ := @coe_sort_trans ?x_58 ?x_59 ?x_60 ?x_61
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_base_aux ?x_62 ?x_63 ?x_64
   (3) ?x_60 : has_coe_t_aux ℝ ?x_59 := @coe_trans_aux ?x_62 ?x_63 ?x_64 ?x_65 ?x_66
     (5) ?x_56 : add_group ℝ := @add_comm_group.to_add_group ?x_59 ?x_60
      (6) ?x_60 : add_comm_group ℝ := real.add_comm_group
```
The line `(5) ?x_56 : add_group ℝ := real.add_group` is a failure, but it assigns a value to `?x_56` from the (2) line. So it rolls all the way back to the (2) line and replays the same assignments until it gets to the bad choice `real.add_group`, and tries something different, in this case `@add_comm_group.to_add_group ?x_59 ?x_60`.

#### [ Mario Carneiro (Jul 21 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130037108):
I wonder if typeclass search will change in lean 4. This seems like such a poor strategy I'm surprised it works as well as it does in mathlib. I know Leo thinks many things about lean 3 are fundamentally broken, and I wouldn't be surprised if this was on the list

#### [ Sebastian Ullrich (Jul 21 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130044916):
@**Mario Carneiro** This is not how class inference should work, nor have I seen such a trace before. Class inference uses temporary mvars that can be unassigned individually. https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/type_context.cpp#L1405

#### [ Mario Carneiro (Jul 21 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130044978):
If you like I can make a mathlib-free example

#### [ Sebastian Ullrich (Jul 21 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045083):
That would be great, thanks

#### [ Mario Carneiro (Jul 21 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045431):
I think this should do the trick (WARNING: this brings VSCode to its knees due to quantity of output)
```
@[priority 0] instance cast_coe {α} [has_zero α] [has_one α] [has_add α] : has_coe ℕ α := ⟨λ _, 0⟩
constant R : Type
instance : has_zero R := sorry

set_option trace.class_instances true
example (n : ℕ) : Prop := n
```
The `constant R` is optional but gives the typeclass system something to fixate on rather than whatever random thing it finds first (usually `unsigned` for me on the init library and `real` when it is imported)

#### [ Sebastian Ullrich (Jul 21 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045547):
hmm
```
$ lean +3.4.1 scratch.lean |& wc -l
381659
 $ lean +master scratch.lean |& wc -l
3342
```
I guess Leo fixed it already :D

#### [ Mario Carneiro (Jul 21 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130045637):
well... I'm glad it was fixed, although I'm still puzzled over the cause...

#### [ Mario Carneiro (Jul 21 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046079):
Oh, looking at the trace from that version, I noticed that it searches for `(1) ?x_7 : has_coe_to_sort ℤ` 2826 times (with 26000 lines in between, not counting failures) before finally getting to `(1) ?x_7 : has_coe_to_sort ℕ`, which is the same typeclass search it started with. So I think if I let it run long enough it *would* hit the recursion limit, it would just take an extremely long time to do so.

#### [ Patrick Massot (Jul 21 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046129):
Maybe it would be worth checking that it was not fixed by accident (since another modification could reinstate the bug), or at least add it to the test suite?

#### [ Patrick Massot (Jul 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046199):
Do you think the type class search could become more programmable for users? For instance we already saw that it would be nice to be able to tell it: whenever you're looking for `ring ?x_i` then you should give up on that branch.

#### [ Mario Carneiro (Jul 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046200):
I'm not sure how much I should care about this bug, since it has to do with lean performance on an unsuccessful typeclass search anyway

#### [ Mario Carneiro (Jul 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046222):
I think "negative instances" would be great, they could probably speed up the search a lot. I.e. `unsigned` is not a field, stop looking there

#### [ Patrick Massot (Jul 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046225):
Obviously I don't know either, this is far above my competences. My reaction is only triggered by Sebastian not knowing something has been fixed

#### [ Mario Carneiro (Jul 21 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046264):
but there is a lot of planning necessary to get a feature like that right

#### [ Mario Carneiro (Jul 21 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046266):
and obviously it's up to Sebastian and Leo to make that happen

#### [ Mario Carneiro (Jul 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046275):
so I will just let them ponder and figure out whatever works

#### [ Patrick Massot (Jul 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046291):
and soon Gabriel, according to Leo's talk

#### [ Sebastian Ullrich (Jul 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046296):
The type context will remain in C++, so it will not be arbitrarily configurable like other parts (hopefully will)

#### [ Mario Carneiro (Jul 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046340):
is typeclass search done in the type context?

#### [ Patrick Massot (Jul 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130046344):
You could still let users pass options to the C++ code, couldn't you?

#### [ Sebastian Ullrich (Jul 22 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103015):
@**Mario Carneiro** Yes, it uses many type context internals. Still, reimplementing it on top of the new type context monad may be an interesting idea, now that I think about it.

#### [ Sebastian Ullrich (Jul 22 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103045):
@**Patrick Massot** Sure, that's what I meant by "not arbitrarily". For the parts reimplemented in Lean, I'd like users to be able to completely replace the default implementations if they want to.

#### [ Mario Carneiro (Jul 22 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103086):
it would certainly be good if at least potential writing of the typeclass search could guide what of the type context gets exposed to lean

#### [ Sebastian Ullrich (Jul 22 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trolled%20by%20undergrad/near/130103093):
Yes, exactly


{% endraw %}
