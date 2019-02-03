---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20567changingdefaultcoercion.html
---

## Stream: [general](index.html)
### Topic: [changing default coercion](20567changingdefaultcoercion.html)

---


{% raw %}
#### [ Chris Hughes (Apr 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125456190):
<p>I've just defined the integers mod n, and since they are a <code>comm_ring</code> there is a default coercion from <code>int</code>. However rather than using the default coercion, it would be nicer to have <code>quotient.mk</code> as the coercion. Is there a way to change this?</p>

#### [ Simon Hudon (Apr 20 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125456275):
<p>I think if you declare the <code>has_coe</code> instance, it will use your instance whenever applicable before even trying the coercion from <code>int</code> to arbitrary <code>comm_ring</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125457130):
<p>Is there a risk of a diamond here though?</p>

#### [ Simon Hudon (Apr 20 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125457174):
<p>You mean like when you have multiple inheritance?</p>

#### [ Chris Hughes (Apr 20 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125459795):
<blockquote>
<p>Is there a risk of a diamond here though?</p>
</blockquote>
<p>What's the diamond? I think that the same idea has been used for coercions from <code>nat</code> to <code>int</code>. The only risk is if I make a <code>coe</code> from <code>Zmod</code> to <code>int</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125460970):
<p>the diamond occurs in 5 years' time when someone else imports your code and then writes down some innocuous-looking coe and stuff doesn't work. My question is whether this is a possibility</p>

#### [ Simon Hudon (Apr 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125461446):
<p>Not for any notion of diamond that I've worked with</p>

#### [ Kevin Buzzard (Apr 20 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125463614):
<p>Somehow what I was concerned about is that if someone one day writes down a coercion from the integers mod n to another comm_ring then they will have to deal with the issue that they now have two coercions from int to the other comm_ring which may not be defeq.</p>

#### [ Patrick Massot (Apr 20 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125463925):
<p>You could define a local instance</p>

#### [ Patrick Massot (Apr 20 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125463970):
<p>That way only people editing your file would have to deal with this</p>

#### [ Chris Hughes (Apr 20 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125466482):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I don't think coercions are transitive, so if something is coerced from integers to integers mod n to R, then it will appear as two up arrows. I think these issues happen anyway with int to rat to real etc, and there are a load of lemmas proving equivalence of different permutations of coercions. I don't want a local coercion, because the quotient coercion is the most useful for everyone.</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20default%20coercion/near/125477762):
<p>There is definitely a "diamond risk", but of an even more trivial variety than an actual diamond: you are talking about two arrows from A to B in the category of typeclass instances, which is only acceptable (by my rule of thumb) if they are defeq, which presumably defeats the purpose of having a second coercion.</p>
<p>That said, in the specific case of replacing the default coercion, you can do it by similar methods to the ones used for <code>int.of_nat</code>, as Simon mentions, although you will have to prove lots of lemmas to replace the ones that <code>int.cast</code> gives you, and users will need to know that you are doing this since they have to refer to different lemmas.</p>
<p>Coercions are transitive, in the sense that if there is <code>has_coe A B</code> and <code>has_coe B C</code> and a <code>C</code> is needed where <code>A</code> is given, Lean will insert a single <code>coe</code> up-arrow with a composite typeclass instance. However, mathlib has a simp lemma explicitly to break these composite arrows up, because they work poorly with other simp lemmas that are all keyed to single coercions.</p>


{% endraw %}
