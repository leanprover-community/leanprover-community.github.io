---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90492circularimportsinmathlib.html
---

## Stream: [maths](index.html)
### Topic: [circular imports in mathlib](90492circularimportsinmathlib.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/circular%20imports%20in%20mathlib/near/135037582):
Johannes said in the p-adic PR

```quote
I'm fine with merging, with one exception: Please don't import topology in `data/polynomial`. I guess we need a `analysis/polynomial.lean` for the continuity statement.

I don't like this, as we get into a huge mess if we have too much cyclic dependencies between the top level directories. I think `data` shouldn't depend on `analysis` or the `*_theory` directories.
```

I've never thought about these issues. Are there general rules written down somewhere about what is acceptable and what is not when it comes to this sort of question?


{% endraw %}
