---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49946wheredidIgoclassical.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [where did I go classical?](https://leanprover-community.github.io/archive/113488general/49946wheredidIgoclassical.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 29 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368857):
<div class="codehilite"><pre><span></span>theorem aux3 (n : nat) (H1 : ¬n &lt; 3) (H2 : even n) : aux (n - 2) &lt; aux n :=
begin
  have H3 := le_of_not_gt H1,
  rw [aux, aux, if_neg H1, if_pos H2],
  let m := n - 3,
  have H4 : n = m + 3,
  { dsimp [m], rw [nat.sub_add_cancel H3] },
  rw H4 at *,
  rw nat.add_sub_assoc,
  rw nat.add_sub_assoc,
  rw nat.add_sub_assoc,
  { simp,
    by_cases m + 1 &lt; 3,
    { simp [h],
      apply add_lt_add_left,
      exact dec_trivial },
    { simp [h, even_of_even_add_two _ H2],
      apply nat.lt_add_of_pos_right,
      exact dec_trivial } },
  exact dec_trivial,
  exact dec_trivial,
  exact dec_trivial
end
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368864):
<p>this isn't MWE. I would understand if you can't read it off the lines</p>

#### [ Kenny Lau (Mar 29 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368909):
<p>(it matters in this context, not because I'm a constructivist, it has nothing to do with my constructivism, I really need this to be constructive)</p>

#### [ Kenny Lau (Mar 29 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368916):
<p>I suspect it's the <code>dec_trivial</code>, but natural inequality should be decidable</p>

#### [ Kenny Lau (Mar 29 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124368998):
<p>update: I removed every <code>dec_trivial</code> and proved the inequalities using <code>constructor</code>, it's still classical</p>

#### [ Gabriel Ebner (Mar 29 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369007):
<p>It's <code>le_of_not_gt</code>, of course.</p>

#### [ Kenny Lau (Mar 29 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369050):
<p>oh, how do I fix it?</p>

#### [ Gabriel Ebner (Mar 29 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369100):
<p>If you really, really don't want classical logic, then you should probably prove a specialized version of <code>le_of_not_gt</code> for decidable linear orders.</p>

#### [ Kenny Lau (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369109):
<p>is there no simple fix for naturals</p>

#### [ Johannes Hölzl (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369153):
<p>Why do you need this as a constructive proof? There is no computable content.<br>
You can constructively prove <code>le_of_not_gt</code> for <code>nat</code> using the decidability of <code>lt</code> on natural numbers.</p>

#### [ Kenny Lau (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369161):
<p>because the content is outside</p>

#### [ Kenny Lau (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369163):
<p>this is just a part</p>

#### [ Johannes Hölzl (Mar 29 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124369331):
<p>But rewriting <code> ¬n &lt; 3 </code> to <code>n &lt;= 3</code> is not a problem for decidability in Lean. You are fine as long as only your proofs are classical.</p>

#### [ Kenny Lau (Mar 29 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/where%20did%20I%20go%20classical%3F/near/124380166):
<p>oh and for the sake of completeness, the final product is here <a href="https://github.com/kckennylau/Lean/blob/master/recursion.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/recursion.lean">https://github.com/kckennylau/Lean/blob/master/recursion.lean</a></p>


{% endraw %}
