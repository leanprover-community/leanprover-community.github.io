---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19566modeqrefl.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [modeq.refl](https://leanprover-community.github.io/archive/113488general/19566modeqrefl.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911585):
<p><code>@[refl] protected theorem refl (a : ℕ) : a ≡ a [MOD n] := @rfl _ _</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911591):
<p>looks funny because <code>rfl</code> unfolds to exactly <code>@rfl _ _</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911637):
<p>but it's one of those situations where you can't prove the result by the exact three letter combination <code>rfl</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911646):
<p>because you get the error <code>not a rfl-lemma, even though marked as rfl</code></p>

#### [ Kenny Lau (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911647):
<p>do you know what the <code>@[refl]</code> <code>@[symm]</code> <code>@[trans]</code> are for (as a sidenote)?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911658):
<p>but the funny thing is, it is tagged <code>[refl]</code> anyway</p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911673):
<p>what is the difference between being <code>a rfl-lemma</code> and being tagged with <code>@[refl]</code>?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911678):
<p>Kenny here are some ramblings</p>

#### [ Kenny Lau (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911683):
<p>they are for the reflexivity symmetry transitivty tactics respectively</p>

#### [ Kenny Lau (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911686):
<p>(refl = reflexivity)</p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911688):
<p>If you are in calc mode then calc will use any lemma tagged <code>trans</code></p>

#### [ Kenny Lau (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911732):
<p>that also</p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911735):
<p>to concatenate <code>a R b</code> and <code>b R c</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911738):
<p>or even <code>b S c</code></p>

#### [ Chris Hughes (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911741):
<p>le_refl is refl but not rfl</p>

#### [ Gabriel Ebner (May 01 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125934512):
<p><code>rfl</code>-lemmas show definitional equalities (i.e. <code>a = b</code> where <code>a</code> and <code>b</code> are def-eq).  The three letters <code>rfl</code> are essentially hardcoded into the parser for this purpose.  The reason is that typically lemmas are completely independent of their proofs, (well-founded recursion aside) it should not matter what proof you use for a lemma.  However whether an equality is proved by definitional equality has important consequences: for example, <code>dsimp</code> can only use definitional equalities.  Hence we have an easy syntactic criterion to determine whether a lemma is proven by definitional equality.</p>


{% endraw %}
