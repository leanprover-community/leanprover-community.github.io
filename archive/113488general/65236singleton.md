---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65236singleton.html
---

## Stream: [general](index.html)
### Topic: [singleton](65236singleton.html)

---


{% raw %}
#### [ Scott Morrison (Aug 12 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976871):
Am I just missing a `singleton` class, the pushout of `inhabited` and `subsingleton`? Am I meant to define my own?

#### [ Mario Carneiro (Aug 12 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976914):
do you need one?

#### [ Mario Carneiro (Aug 12 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976922):
You can just assume both classes if you need

#### [ Scott Morrison (Aug 12 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976965):
just seems wordy: I was about to use this a whole bunch of times

#### [ Mario Carneiro (Aug 12 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976966):
for what?

#### [ Scott Morrison (Aug 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976967):
universal properties

#### [ Scott Morrison (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976975):
I wanted to try out a design for equalizers/products/pushouts based on a class `is_equalizer`, which would have a `singleton ...` field that expresses that there's a map with some property, and that map is unique.

#### [ Mario Carneiro (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977017):
hm, I would say that's a bit too clever

#### [ Mario Carneiro (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977020):
just state the map and state a separate field asserting it is unique

#### [ Scott Morrison (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977021):
my current design just says these things separately

#### [ Mario Carneiro (Aug 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977027):
You will have to unpack it all the time

#### [ Scott Morrison (Aug 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977028):
```
structure Equalizer (f g : X ⟶ Y) :=
(equalizer     : C)
(inclusion     : equalizer ⟶ X)
(map           : ∀ {Z : C} (k : Z ⟶ X) (w : k ≫ f = k ≫ g), Z ⟶ equalizer)
(witness       : inclusion ≫ f = inclusion ≫ g . obviously)
(factorisation : ∀ {Z : C} (k : Z ⟶ X) (w : k ≫ f = k ≫ g), (map k w) ≫ inclusion = k . obviously)
(uniqueness    : ∀ {Z : C} (a b : Z ⟶ equalizer) (witness : a ≫ inclusion = b ≫ inclusion), a = b . obviously)
```

#### [ Scott Morrison (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977072):
the alternative would be to pack `map`, `witness`, `factorisation`, and `uniqueness` all into one `singleton` instance, with an appropriate subtype

#### [ Mario Carneiro (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977073):
uniqueness can be stated with one fewer pi btw

#### [ Scott Morrison (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977075):
you mean don't name `witness`?

#### [ Mario Carneiro (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977076):
just say `a = witness` at the end

#### [ Scott Morrison (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977077):
sure

#### [ Mario Carneiro (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977078):
the other `witness`

#### [ Scott Morrison (Aug 12 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977083):
oh, I see

#### [ Scott Morrison (Aug 12 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977084):
yeah, I've gone back and forth on that a few times

#### [ Mario Carneiro (Aug 12 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977085):
er, I mean `a = map something something`

#### [ Mario Carneiro (Aug 12 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977125):
Also, you can pack `witness` and `factorisation` and `uniqueness` into one field with an iff

#### [ Scott Morrison (Aug 12 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977133):
that was Reid's design

#### [ Scott Morrison (Aug 12 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977136):
I feel like that has the same objection to using `singleton`, but the unpacking and packing required is even less intuitive

#### [ Mario Carneiro (Aug 12 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977141):
I just want to avoid packing the data in too

#### [ Scott Morrison (Aug 12 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977181):
I see.

#### [ Mario Carneiro (Aug 12 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977190):
Would you like a way to quickly say `{a | p a} = {x}`?

#### [ Scott Morrison (Aug 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977238):
(a = x) iff p a

#### [ Mario Carneiro (Aug 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977245):
right, with `a` abstracted

#### [ Scott Morrison (Aug 12 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977257):
Ok. This is exactly how Reid did things in the category theory he has in his homotopy library. At first I didn't like it much, but I'm coming around. :-)

#### [ Mario Carneiro (Aug 12 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977315):
like `def is_the {α} (p : α → Prop) (x : α) := ∀ a, x = a ↔ p a`

#### [ Scott Morrison (Aug 12 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977316):
I will see if I can do something that feels uniform across product/equalizer/pullback, and makes things sufficiently obvious.

#### [ Mario Carneiro (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977326):
the definition might be gratuitous

#### [ Scott Morrison (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977330):
perhaps something like `universal_property` instead of `is_the`? Longer, but friendlier to the mathematicians.

#### [ Scott Morrison (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977332):
I'll try with and without. :-)

#### [ Mario Carneiro (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977336):
the name is based on the `the` sometimes used for definite description

#### [ Mario Carneiro (Aug 12 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977379):
it's `∃!` with the witness free

#### [ Scott Morrison (Aug 12 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977385):
Yeah; just a note that this is how you talk about universal properties will be good enough for the mathematicians.

#### [ Scott Morrison (Aug 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977390):
okay, kids need lunch!

#### [ Mario Carneiro (Aug 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977396):
I'm open to slick binder notations for that


{% endraw %}
