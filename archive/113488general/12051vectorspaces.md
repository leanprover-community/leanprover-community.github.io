---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12051vectorspaces.html
---

## Stream: [general](index.html)
### Topic: [vector spaces](12051vectorspaces.html)

---


{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133922950):
Before we go on a rampage proving things about vector spaces: there was some suggestion that we should just turn `vector_space` into notation/abbreviation for `module`. Maybe now is a good point to decide on this, since Kenny is already PR'ing stuff where he needs new instances of `vector_space`.

#### [ Mario Carneiro (Sep 14 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133925427):
this is also affected by my upcoming refactoring. Note that `semimodule` and `module` are also related in a similar way to `module` and `vector_space`, that is, there are no new axioms, just the parameters change.

#### [ Johan Commelin (Sep 14 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133931912):
Ok, so why don't we just call everything a `module`, and only require the base thingy to be a `semiring`?

#### [ Mario Carneiro (Sep 14 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133931953):
I'm on board with that if the rest of you are, but mathematicians seem to be picky about names

#### [ Johan Commelin (Sep 14 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133931960):
True, but usually we are ok with generalising a notion.

#### [ Kenny Lau (Sep 14 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933360):
@**Mario Carneiro** why are 0 and 1 defined using ulift empty and ulift unit, instead of pempty and punit?

#### [ Kenny Lau (Sep 14 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933361):
```lean
instance : has_zero cardinal.{u} := ⟨⟦ulift empty⟧⟩
instance : has_one cardinal.{u} := ⟨⟦ulift unit⟧⟩
```

#### [ Mario Carneiro (Sep 14 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933387):
because they didn't exist at the time

#### [ Kenny Lau (Sep 14 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933403):
should I change it?

#### [ Mario Carneiro (Sep 14 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933412):
if you want

#### [ Kenny Lau (Sep 14 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933417):
it will certainly shorten my proofs:
```lean
@[simp] theorem mk_empty : mk empty = 0 :=
fintype_card empty

@[simp] theorem mk_pempty : mk pempty = 0 :=
fintype_card pempty

@[simp] theorem mk_empty' (α : Type u) : mk (∅ : set α) = 0 :=
quotient.sound ⟨(equiv.set.empty α).trans equiv.ulift.symm⟩

@[simp] theorem mk_plift_false : mk (plift false) = 0 :=
quotient.sound ⟨equiv.plift.trans $ equiv.false_equiv_empty.trans equiv.ulift.symm⟩

@[simp] theorem mk_unit : mk unit = 1 :=
(fintype_card unit).trans nat.cast_one

@[simp] theorem mk_punit : mk punit = 1 :=
(fintype_card punit).trans nat.cast_one

@[simp] theorem mk_singleton {α : Type u} (x : α) : mk ({x} : set α) = 1 :=
quotient.sound ⟨(equiv.set.singleton x).trans equiv.ulift.symm⟩

@[simp] theorem mk_plift_true : mk (plift true) = 1 :=
quotient.sound ⟨equiv.plift.trans $ equiv.true_equiv_unit.trans $ equiv.ulift.symm⟩

@[simp] theorem mk_bool : mk bool = 2 :=
quotient.sound ⟨equiv.bool_equiv_unit_sum_unit.trans $ equiv.sum_congr equiv.ulift.symm equiv.ulift.symm⟩

@[simp] theorem mk_Prop : mk Prop = 2 :=
(quotient.sound ⟨equiv.Prop_equiv_bool⟩ : mk Prop = mk bool).trans mk_bool

@[simp] theorem mk_option {α : Type u} : mk (option α) = mk α + 1 :=
quotient.sound ⟨(equiv.option_equiv_sum_unit α).trans $ equiv.sum_congr (equiv.refl α) equiv.ulift.symm⟩

theorem mk_eq_of_injective {α β : Type u} {f : α → β} {s : set α} (hf : injective f) : mk (f '' s) = mk s :=
quotient.sound ⟨(equiv.set.image f s hf).symm⟩
```

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933547):
I think `empty` and `pempty` and `false` should be all definitionall equal

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933548):
but that's just me

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933549):
the same goes with `punit` and `true`

#### [ Mario Carneiro (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933551):
I think that `punit` is defeq to `unit`

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933553):
now I have to prove 6 equiv lemmas about the first one

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933554):
right, but not to `true`

#### [ Mario Carneiro (Sep 14 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933593):
no, they can't be

#### [ Mario Carneiro (Sep 14 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933599):
they are in different universes

#### [ Kenny Lau (Sep 14 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933603):
then punit should be made to sort

#### [ Kenny Lau (Sep 14 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933673):
also, why can't `punit.star` be `()`?

#### [ Kenny Lau (Sep 14 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933777):
```lean
@[simp] def arrow_unit_equiv_unit (α : Sort*) : (α → punit.{v}) ≃ punit.{w} :=
⟨λ f, punit.star, λ u f, punit.star, λ f, by funext x; cases f x; refl, λ u, by cases u; reflexivity⟩

@[simp] def unit_arrow_equiv (α : Sort*) : (punit.{u} → α) ≃ α :=
⟨λ f, f punit.star, λ a u, a, λ f, by funext x; cases x; refl, λ u, rfl⟩

@[simp] def empty_arrow_equiv_unit (α : Sort*) : (empty → α) ≃ punit.{u} :=
⟨λ f, punit.star, λ u e, e.rec _, λ f, funext $ λ x, x.rec _, λ u, by cases u; refl⟩

@[simp] def pempty_arrow_equiv_unit (α : Sort*) : (pempty → α) ≃ punit.{u} :=
⟨λ f, punit.star, λ u e, e.rec _, λ f, funext $ λ x, x.rec _, λ u, by cases u; refl⟩

@[simp] def false_arrow_equiv_unit (α : Sort*) : (false → α) ≃ punit.{u} :=
calc (false → α) ≃ (empty → α) : arrow_congr false_equiv_empty (equiv.refl _)
             ... ≃ punit       : empty_arrow_equiv_unit _
```

#### [ Kenny Lau (Sep 14 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933781):
@**Mario Carneiro** should I change the name of these to `punit` etc?

#### [ Mario Carneiro (Sep 14 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933820):
yes, if it says punit it should be called punit

#### [ Kenny Lau (Sep 14 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933831):
the fact that it is tagged with `simp` makes it hard to trace

#### [ Kenny Lau (Sep 14 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933832):
let's hope for the best

#### [ Kenny Lau (Sep 14 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933879):
wow there's a lot more misnamed theorems

#### [ Kenny Lau (Sep 14 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933891):
also what is wrong with this proof
```lean
def punit_equiv_punit : punit.{v} ≃ punit.{w} :=
⟨λ _, punit.star, λ _, punit.star, λ u, by cases u; refl, λ u, by cases u; reflexivity⟩
```

#### [ Mario Carneiro (Sep 14 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933992):
nothing

#### [ Mario Carneiro (Sep 14 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933999):
although there are a lot more theorems where that came from

#### [ Mario Carneiro (Sep 14 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934003):
any universe polymorphic definition is going to have a theorem like that

#### [ Kevin Buzzard (Sep 14 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934055):
It seems weird to have to say that J is a submodule of R instead of an ideal of R.

#### [ Kenny Lau (Sep 14 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934123):
```quote
nothing
```
seriously, `reflexivity`?

#### [ Mario Carneiro (Sep 14 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934419):
the asymmetry is a bit odd

#### [ Johan Commelin (Sep 14 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934731):
@**Kevin Buzzard** I think the idea was that `ideal` could be notation for `submodule`. That way it is transparent to Lean, but we can still have our beloved terminology. Of course it means that you could start talking about ideals of a module, but you should just avoid that: Lean doesn't care, you will only confuse users.

#### [ Kevin Buzzard (Sep 14 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934800):
Then do we get is_ideal.add or ideal.add etc? And is_submodule.smul is different to is_ideal.smul because it's the ring multiplication in the second case. I found myself having to unfold things explicitly, it was a bit weird

#### [ Kevin Buzzard (Sep 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934850):
I was going to wait until all the semimodule stuff died down before making any explicit comments though. I'm using ideals a lot in the Hilbert basis proof course, but I have a lot of other stuff to worry about right now so it's slow progress

#### [ Kevin Buzzard (Sep 14 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934867):
For ideals you don't need to find the instance of module R R (and indeed yesterday I couldn't find it)

#### [ Kevin Buzzard (Sep 14 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934908):
(but that might be because things are currently in a state of flux)

#### [ Kenny Lau (Sep 14 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937436):
@**Mario Carneiro** so at the current moment, how should we know that a field is a vector space over itself?

#### [ Mario Carneiro (Sep 14 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937444):
there is an instance for this

#### [ Mario Carneiro (Sep 14 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937488):
but if it isn't working you can also introduce it locally

#### [ Kenny Lau (Sep 14 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937518):
oh ok

#### [ Kenny Lau (Sep 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937972):
```lean
def module_equiv_lc (hs : is_basis s) : β ≃ (s →₀ α) :=
```

#### [ Kenny Lau (Sep 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938015):
@**Mario Carneiro** should I change this to the idiomatic `lc \a s`?

#### [ Mario Carneiro (Sep 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938027):
that theorem is the centerpiece of my current refactoring, so I recommend you leave it alone until I'm done

#### [ Mario Carneiro (Sep 14 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938036):
anyway `lc A s` doesn't work because `s` isn't a module

#### [ Kenny Lau (Sep 14 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938049):
ok...

#### [ Kenny Lau (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938090):
you see

#### [ Kenny Lau (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938095):
this would help my dimension stuff a lot

#### [ Mario Carneiro (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938096):
then wait

#### [ Kenny Lau (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938097):
alright


{% endraw %}
