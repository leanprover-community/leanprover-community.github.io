---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53986subtypeinstance.html
---

## Stream: [maths](index.html)
### Topic: [subtype instance](53986subtypeinstance.html)

---


{% raw %}
#### [ Patrick Massot (Aug 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132419278):
<p>In PR <a href="https://github.com/leanprover/mathlib/pull/261" target="_blank" title="https://github.com/leanprover/mathlib/pull/261">#261</a> coming from the perfectoid project, Johan defined subrings and subfields and proved they are rings and fields respectively. The proofs were of course extremely similar to the case of monoids and groups. So I exploited^Wencouraged Simon to write a new tactic built on top of <code>refine_struct</code> in the spirit of <code>pi_instance</code>. The result is  <a href="https://github.com/leanprover/mathlib/pull/267" target="_blank" title="https://github.com/leanprover/mathlib/pull/267">#267</a>. Of course any comment is welcome, but I'd be particularly interested in trying to answer question about how <a href="https://github.com/leanprover/mathlib/pull/267/files#diff-040c2692bc712ca8fface6e4aa45ce62R31" target="_blank" title="https://github.com/leanprover/mathlib/pull/267/files#diff-040c2692bc712ca8fface6e4aa45ce62R31">this tactic</a> works, since I managed to fool myself into believing I mostly understand it and should write a tutorial about it.</p>

#### [ Johan Commelin (Aug 20 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132434842):
<p>Just for the record, I only did the parts on subrings. <span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span> deserves all credit for the work on subfields.</p>

#### [ Patrick Massot (Aug 20 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132444138):
<p>Oh, sorry I misunderstood.</p>

#### [ Patrick Massot (Aug 20 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132444477):
<p>but actually the file header is correct</p>

#### [ Andreas Swerdlow (Aug 20 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132444644):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  deserves credit for the newest version of subfield.lean</p>

#### [ Patrick Massot (Aug 20 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132445068):
<p>I'm not sure we have a very clear attribution policy in mathlib. But it's a very small file in any case. The main thing Simon added is the tactic, which is not in this file</p>

#### [ Simon Hudon (Aug 20 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132467672):
<p>I think we can mention more names than just mine. That was a team effort.</p>

#### [ Scott Morrison (Aug 22 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtype%20instance/near/132559536):
<p>I think a good policy with attribution on files is to just gradually add more names: even if someone does a complete rewrite of a file, keep the old names as well. We have <code>git blame</code> and git history generally if the details ever matter.</p>


{% endraw %}
