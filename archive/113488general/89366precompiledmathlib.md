---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89366precompiledmathlib.html
---

## Stream: [general](index.html)
### Topic: [precompiled mathlib](89366precompiledmathlib.html)

---

#### [Johan Commelin (Apr 20 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/precompiled%20mathlib/near/125449071):
```quote
That being said, we really need mathlib nightlies (ie. precompiled mathlib) — Patrick Massot
```
Can this be done using Travis? Or do we need other infrastructure?

#### [Johan Commelin (Apr 20 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/precompiled%20mathlib/near/125452560):
Ok, this seems possible:
https://gist.github.com/Maumagnaguagno/84a9807ed71d233e5d3f
https://gist.github.com/willprice/e07efd73fb7f13f917ea

#### [Johan Commelin (Apr 20 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/precompiled%20mathlib/near/125452567):
I think a fully compiled mathlib including sources is about 15mb

#### [Johan Commelin (Apr 20 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/precompiled%20mathlib/near/125452572):
So I think it is not too much of a burden to push back to github

