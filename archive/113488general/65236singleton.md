---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65236singleton.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [singleton](https://leanprover-community.github.io/archive/113488general/65236singleton.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 12 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976871):
<p>Am I just missing a <code>singleton</code> class, the pushout of <code>inhabited</code> and <code>subsingleton</code>? Am I meant to define my own?</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976914):
<p>do you need one?</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976922):
<p>You can just assume both classes if you need</p>

#### [ Scott Morrison (Aug 12 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976965):
<p>just seems wordy: I was about to use this a whole bunch of times</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976966):
<p>for what?</p>

#### [ Scott Morrison (Aug 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976967):
<p>universal properties</p>

#### [ Scott Morrison (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131976975):
<p>I wanted to try out a design for equalizers/products/pushouts based on a class <code>is_equalizer</code>, which would have a <code>singleton ...</code> field that expresses that there's a map with some property, and that map is unique.</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977017):
<p>hm, I would say that's a bit too clever</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977020):
<p>just state the map and state a separate field asserting it is unique</p>

#### [ Scott Morrison (Aug 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977021):
<p>my current design just says these things separately</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977027):
<p>You will have to unpack it all the time</p>

#### [ Scott Morrison (Aug 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977028):
<div class="codehilite"><pre><span></span>structure Equalizer (f g : X ⟶ Y) :=
(equalizer     : C)
(inclusion     : equalizer ⟶ X)
(map           : ∀ {Z : C} (k : Z ⟶ X) (w : k ≫ f = k ≫ g), Z ⟶ equalizer)
(witness       : inclusion ≫ f = inclusion ≫ g . obviously)
(factorisation : ∀ {Z : C} (k : Z ⟶ X) (w : k ≫ f = k ≫ g), (map k w) ≫ inclusion = k . obviously)
(uniqueness    : ∀ {Z : C} (a b : Z ⟶ equalizer) (witness : a ≫ inclusion = b ≫ inclusion), a = b . obviously)
</pre></div>

#### [ Scott Morrison (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977072):
<p>the alternative would be to pack <code>map</code>, <code>witness</code>, <code>factorisation</code>, and <code>uniqueness</code> all into one <code>singleton</code> instance, with an appropriate subtype</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977073):
<p>uniqueness can be stated with one fewer pi btw</p>

#### [ Scott Morrison (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977075):
<p>you mean don't name <code>witness</code>?</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977076):
<p>just say <code>a = witness</code> at the end</p>

#### [ Scott Morrison (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977077):
<p>sure</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977078):
<p>the other <code>witness</code></p>

#### [ Scott Morrison (Aug 12 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977083):
<p>oh, I see</p>

#### [ Scott Morrison (Aug 12 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977084):
<p>yeah, I've gone back and forth on that a few times</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977085):
<p>er, I mean <code>a = map something something</code></p>

#### [ Mario Carneiro (Aug 12 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977125):
<p>Also, you can pack <code>witness</code> and <code>factorisation</code> and <code>uniqueness</code> into one field with an iff</p>

#### [ Scott Morrison (Aug 12 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977133):
<p>that was Reid's design</p>

#### [ Scott Morrison (Aug 12 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977136):
<p>I feel like that has the same objection to using <code>singleton</code>, but the unpacking and packing required is even less intuitive</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977141):
<p>I just want to avoid packing the data in too</p>

#### [ Scott Morrison (Aug 12 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977181):
<p>I see.</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977190):
<p>Would you like a way to quickly say <code>{a | p a} = {x}</code>?</p>

#### [ Scott Morrison (Aug 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977238):
<p>(a = x) iff p a</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977245):
<p>right, with <code>a</code> abstracted</p>

#### [ Scott Morrison (Aug 12 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977257):
<p>Ok. This is exactly how Reid did things in the category theory he has in his homotopy library. At first I didn't like it much, but I'm coming around. :-)</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977315):
<p>like <code>def is_the {α} (p : α → Prop) (x : α) := ∀ a, x = a ↔ p a</code></p>

#### [ Scott Morrison (Aug 12 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977316):
<p>I will see if I can do something that feels uniform across product/equalizer/pullback, and makes things sufficiently obvious.</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977326):
<p>the definition might be gratuitous</p>

#### [ Scott Morrison (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977330):
<p>perhaps something like <code>universal_property</code> instead of <code>is_the</code>? Longer, but friendlier to the mathematicians.</p>

#### [ Scott Morrison (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977332):
<p>I'll try with and without. :-)</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977336):
<p>the name is based on the <code>the</code> sometimes used for definite description</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977379):
<p>it's <code>∃!</code> with the witness free</p>

#### [ Scott Morrison (Aug 12 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977385):
<p>Yeah; just a note that this is how you talk about universal properties will be good enough for the mathematicians.</p>

#### [ Scott Morrison (Aug 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977390):
<p>okay, kids need lunch!</p>

#### [ Mario Carneiro (Aug 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton/near/131977396):
<p>I'm open to slick binder notations for that</p>


{% endraw %}
