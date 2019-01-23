---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28136Theorems.html
---

## Stream: [general](index.html)
### Topic: [Theorems](28136Theorems.html)

---

#### [Guillermo Barajas Ayuso (Aug 04 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130894817):
Hi guys do you know how types can somehow be theorems? E.g. strong_indefinite_description in classical.

#### [Mario Carneiro (Aug 04 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130894929):
There is nothing preventing you from marking a type as a theorem, or a prop as a def

#### [Mario Carneiro (Aug 04 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130895079):
Usually we stick to `theorem` or `lemma` for things in `Prop` and `def` for things in `Sort` or `Type`, though, for a few reasons. The VM will not generate code for `theorem`s, and this will affect downstream definitions as well, so that is one reason; it is not a problem with `strong_indefinite_description` because this theorem is not computable anyway. Also a `theorem` is never unfolded, which is almost never necessary for a `Prop` because of proof irrelevance but is often important for `def`s since we may want to prove theorems about the def later. Here it is not a problem in `strong_indefinite_description` because the definition is supposed to be arbitrary in its type, so unfolding should never be necessary.

#### [Guillermo Barajas Ayuso (Aug 05 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130936748):
Ok that makes sense, thanks a lot!

