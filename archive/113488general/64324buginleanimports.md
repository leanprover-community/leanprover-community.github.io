---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64324buginleanimports.html
---

## Stream: [general](index.html)
### Topic: [bug in lean imports](64324buginleanimports.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20in%20lean%20imports/near/152471531):
@**Sebastian Ullrich** I guess no one has ever tried to use 7 dots in a row in relative imports, but it doesn't work. The `=` should be a `+=` [here](https://github.com/leanprover/lean/blob/master/src/frontends/lean/parser.cpp#L2422), and I tested that if you put `import .......test` it counts as only one level up (and in general `k` dots means `k mod 3` levels up)


{% endraw %}
