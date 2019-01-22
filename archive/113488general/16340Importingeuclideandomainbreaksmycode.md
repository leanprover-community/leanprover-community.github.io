---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16340Importingeuclideandomainbreaksmycode.html
---

## [general](index.html)
### [Importing euclidean_domain  breaks my code](16340Importingeuclideandomainbreaksmycode.html)

#### [Chris Hughes (May 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Importing%20euclidean_domain%20%20breaks%20my%20code/near/127176176):
For some reason importing euclidean domain breaks my code, and causes a deterministic timeout. The same problem happens if I try to import `algebra.euclidean_domain` into `linear_algebra.multivariate_polynomial`. What's happening?

#### [Chris Hughes (May 28 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Importing%20euclidean_domain%20%20breaks%20my%20code/near/127180205):
Discovered a solution. Delete the unnecessary `decidable_equality` argument from the euclidean_domain class

