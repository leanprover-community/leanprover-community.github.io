---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90876mlmethodsininteractivetheoremproving.html
---

## [general](index.html)
### [ml methods in interactive theorem proving](90876mlmethodsininteractivetheoremproving.html)

#### [Andrew Ashworth (Jun 14 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ml methods in interactive theorem proving/near/128046890):
interesting paper here: "GamePad: A Learning Environment for Theorem Proving" https://arxiv.org/abs/1806.00608
unfortunately the conclusion is the same as it has been for the past 30 years... not quite there yet, needs more funding and research :)

#### [Moses Schönfinkel (Jun 14 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ml methods in interactive theorem proving/near/128051268):
"We also note that position evaluation <omitted> should assign a high number to proof states which do not yet contain the requisite hypotheses to prove the current goal." This metric (representing how far someone is from completing a proof) seems so silly - sadly I can't check how well this works in practice without compiling their entire project because  their results sub-chapter doesn't say much :(.

#### [Andrew Ashworth (Jun 14 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ml methods in interactive theorem proving/near/128060042):
i wish they had dealt with `have` statements properly. in a way, they can be regarded as additional  lemmas

#### [Moses Schönfinkel (Jun 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ml methods in interactive theorem proving/near/128108440):
I can't get it to compile. I wanted to check how many steps would be predicted for FLT to reaffirm myself in the belief that this is an incredibly random metric :).

