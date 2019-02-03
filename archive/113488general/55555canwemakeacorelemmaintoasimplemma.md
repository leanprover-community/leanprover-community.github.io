---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55555canwemakeacorelemmaintoasimplemma.html
---

## Stream: [general](index.html)
### Topic: [can we make a core lemma into a simp lemma](55555canwemakeacorelemmaintoasimplemma.html)

---


{% raw %}
#### [ Johan Commelin (Aug 07 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041229):
<p><code>nat.sub_self</code> is in core. I think it should be a simp lemma. Can we add such an attribute post-hoc in a mathlib file?</p>

#### [ Sean Leather (Aug 07 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041281):
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_self</span>
</pre></div>

#### [ Kevin Buzzard (Aug 07 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041567):
<p>or <code>local attribute [simp] nat.sub_self</code> if you're scared that making it a simp lemma more globally will cause other problems. I see that the additive group version <code>sub_self</code> isn't a simp lemma either. This might be something to do with subtraction being involved. I think <code>a - b = a + (-b)</code> is a <code>simp</code> lemma and because of this <code>simp</code> might change your <code>a - a</code> to <code>a + (-a)</code> before it notices your attribute.</p>
<p>We were talking about a related thing a day or two ago, where <code>simp</code> just failed to simplify quite a complicated thing because it couldn't manage <code>a + (b + -a) = b</code>.</p>

#### [ Johan Commelin (Aug 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041932):
<p>Right. But I think whenever <code>n : nat</code> and you encounter <code>(n - n)</code> somewhere in your goal, there should be no harm at all if you replace it with <code>0 : nat</code>...</p>

#### [ Johan Commelin (Aug 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041935):
<p>Maybe I just don't understand <code>simp</code>.</p>

#### [ Mario Carneiro (Aug 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131041937):
<p><code>nat.sub_self</code> should be a simp lemma. We can add it to <code>data.nat.basic</code>. As I've mentioned, <code>sub_self</code> will never trigger as a simp lemma</p>

#### [ Johan Commelin (Aug 07 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042034):
<p>Right... because "group vs semigroup" ?</p>

#### [ Mario Carneiro (Aug 07 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042055):
<p><code>nat.sub</code> is not the same as the one defined for additive groups</p>

#### [ Mario Carneiro (Aug 07 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042090):
<p>the sub-unfolding simp lemma only applies to the additive group sub</p>

#### [ Mario Carneiro (Aug 07 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042093):
<p>of course <code>n + -n</code> doesn't even make sense over nat</p>

#### [ Kevin Buzzard (Aug 07 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20we%20make%20a%20core%20lemma%20into%20a%20simp%20lemma/near/131042688):
<p>Aah very nice :-) Is there any way of telling <code>simp</code> to try <code>sub_self</code> before trying the dreaded <code>sub_eq_add_neg</code>?</p>


{% endraw %}
