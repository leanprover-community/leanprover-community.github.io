---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53986subtypeinstance.html
---

## [maths](index.html)
### [subtype instance](53986subtypeinstance.html)

#### [Patrick Massot (Aug 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132419278):
In PR [#261](https://github.com/leanprover/mathlib/pull/261) coming from the perfectoid project, Johan defined subrings and subfields and proved they are rings and fields respectively. The proofs were of course extremely similar to the case of monoids and groups. So I exploited^Wencouraged Simon to write a new tactic built on top of `refine_struct` in the spirit of `pi_instance`. The result is  [#267](https://github.com/leanprover/mathlib/pull/267). Of course any comment is welcome, but I'd be particularly interested in trying to answer question about how [this tactic](https://github.com/leanprover/mathlib/pull/267/files#diff-040c2692bc712ca8fface6e4aa45ce62R31) works, since I managed to fool myself into believing I mostly understand it and should write a tutorial about it.

#### [Johan Commelin (Aug 20 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132434842):
Just for the record, I only did the parts on subrings. @**Andreas Swerdlow** deserves all credit for the work on subfields.

#### [Patrick Massot (Aug 20 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132444138):
Oh, sorry I misunderstood.

#### [Patrick Massot (Aug 20 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132444477):
but actually the file header is correct

#### [Andreas Swerdlow (Aug 20 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132444644):
@**Simon Hudon**  deserves credit for the newest version of subfield.lean

#### [Patrick Massot (Aug 20 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132445068):
I'm not sure we have a very clear attribution policy in mathlib. But it's a very small file in any case. The main thing Simon added is the tactic, which is not in this file

#### [Simon Hudon (Aug 20 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132467672):
I think we can mention more names than just mine. That was a team effort.

#### [Scott Morrison (Aug 22 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype instance/near/132559536):
I think a good policy with attribution on files is to just gradually add more names: even if someone does a complete rewrite of a file, keep the old names as well. We have `git blame` and git history generally if the details ever matter.

