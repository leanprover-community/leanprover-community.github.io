---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74349provingequalityofstructures.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [proving equality of structures](https://leanprover-community.github.io/archive/113488general/74349provingequalityofstructures.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (May 16 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126644596):
<p>Is there a tactic or something that's like <code>apply subtype.eq</code>, but works for a general structure? Or do I have to write down the equality lemma manually?</p>

#### [ Kenny Lau (May 16 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126644607):
<p><code>congr</code>, which doesn't always work</p>

#### [ Reid Barton (May 16 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126644746):
<p>I thought about <code>congr</code>, but my goal is literally <code>e1 = e2</code> and <code>congr</code> made no progress. Somehow I need to eta expand each side first, and then apply <code>congr</code>.</p>

#### [ Kevin Buzzard (May 16 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126646065):
<p>From the changelog:</p>

#### [ Kevin Buzzard (May 16 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126646068):
<p>"simp now reduces equalities c a_1 ... a_n = c b_1 ... b_n to a_1 = b_1 /\ ... /\ a_n = b_n if c is a constructor. This feature can be disabled using simp {constructor_eq := ff}"</p>

#### [ Kevin Buzzard (May 16 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126646116):
<p>of course, simp might do other things as well...</p>

#### [ Nicholas Scheel (May 16 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126654166):
<p>hm I asked a similar question a while ago, but it was about a lemma not a tactic: <a href="#narrow/stream/113488-general/subject/structure.20equality.20from.20parts/near/124033713" title="#narrow/stream/113488-general/subject/structure.20equality.20from.20parts/near/124033713">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20equality.20from.20parts/near/124033713</a></p>

#### [ Reid Barton (May 16 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126654471):
<p>Yes, same goal. I managed to write my lemma by copying <code>subtype.eq</code> very carefully.</p>

#### [ Scott Morrison (May 17 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674624):
<p>Someone (yikes, I've forgotten who, and my copy doesn't record the name) wrote for me a tactic called <code>congr_struct</code> that sometimes is useful for proving equalities of structures. In the presence of fields with dependencies on earlier fields it create new <code>heq</code> goals, which isn't always what you want.</p>

#### [ Scott Morrison (May 17 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674631):
<p>There's a copy at &lt;<a href="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/congr_struct.lean" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/congr_struct.lean">https://github.com/semorrison/lean-tidy/blob/master/src/tidy/congr_struct.lean</a>&gt; (you can just remove the import if you want to steal a copy).</p>

#### [ Scott Morrison (May 17 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674640):
<p>If anyone wants it I can PR it into mathlib. I'm not actually using it anywhere myself at the moment.</p>

#### [ Scott Morrison (May 17 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674691):
<p>I end up writing my own lemmas, e.g. of the form</p>
<div class="codehilite"><pre><span></span>structure NaturalTransformation (F G : C ↝ D) : Type (max (u+1) v) :=
  (components: Π X : C, (F +&gt; X) ⟶ (G +&gt; X))
  (naturality: ∀ {X Y : C} (f : X ⟶ Y), (F &amp;&gt; f) ≫ (components Y) = (components X) ≫ (G &amp;&gt; f))

infixr ` ⟹ `:50  := NaturalTransformation

lemma NaturalTransformations_componentwise_equal
  (α β : F ⟹ G)
  (w : ∀ X : C, α.components X = β.components X) : α = β :=
  begin
    induction α with α_components α_naturality,
    induction β with β_components β_naturality,
    have hc : α_components = β_components := funext w,
    subst hc
  end
</pre></div>

#### [ Scott Morrison (May 17 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674692):
<p>(and I have lots of these, unfortunately)</p>

#### [ Mario Carneiro (May 17 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126676097):
<p>Mathlib is calling these lemmas "extensionality" theorems, for use with Simon's <code>ext</code> tactic. The fastest way to prove them is to case on both structures, then apply <code>congr</code> and other extensionality theorems to the resulting goals</p>

#### [ Mario Carneiro (May 17 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126676208):
<p>I don't have the necessary stuff to test your example, but I think it is possible to have a proof that looks something like <code>by cases α; cases β; congr; exact funext w</code></p>

#### [ Scott Morrison (May 17 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126679010):
<p>Yes, that proof works too.</p>


{% endraw %}
