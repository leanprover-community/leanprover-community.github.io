---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45701rwbugletIthink.html
---

## Stream: [general](index.html)
### Topic: [rw buglet (I think)](45701rwbugletIthink.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528036):
<p>before : 38 hypotheses including <code> HyT2 : y ∈ T </code> and <code> HTUih : T = Ui h </code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528039):
<p>Then I do <code> rw HTUih at HyT2</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528041):
<p>and I end up with 39 hypotheses</p>

#### [ Kenny Lau (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528042):
<p>quite hard to confirm it if you don't have MWE</p>

#### [ Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528044):
<p>oh that isn't a bug</p>

#### [ Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528049):
<p>because that hypothesis can't be replaced</p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528050):
<p>including <code> HyT2 : y ∈ T </code> and <code> HyT2 : y ∈ Ui h </code></p>

#### [ Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528051):
<p>because it's being used by other things</p>

#### [ Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528052):
<p>so instead it creates another hypothesis</p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528055):
<p>Oh I see...</p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528057):
<p>...with the same name?</p>

#### [ Kenny Lau (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528096):
<p>well what other name would it be</p>

#### [ Kenny Lau (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528097):
<p>you can do <code>dedup</code> if you don't like it</p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528098):
<p><code>revert HyT2,intro HyT</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528114):
<p>It could have called it <code>a</code> ;-)</p>


{% endraw %}
