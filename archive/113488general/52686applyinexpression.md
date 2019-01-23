---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52686applyinexpression.html
---

## Stream: [general](index.html)
### Topic: [apply in expression](52686applyinexpression.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Nov 06 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20in%20expression/near/146851453):
Is there a way to `apply` in the middle of an expression? Let me explain. Assume that lemma `foo` tells me that `Q` can be deduced from `P`. Now, I have in the middle of a proof a goal of the form `∀x, Q x`, and I would like to reduce it to `∀x, P x` without introducing `x`. Just like `simp` would do instead of `rw`, but for implications instead of equivalences. Is this possible?


{% endraw %}
