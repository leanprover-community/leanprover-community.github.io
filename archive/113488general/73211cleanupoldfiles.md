---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73211cleanupoldfiles.html
---

## Stream: [general](index.html)
### Topic: [clean up old files](73211cleanupoldfiles.html)

---


{% raw %}
#### [ Reid Barton (Jan 22 2019 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/clean%20up%20old%20files/near/156607187):
<p>I wrote two Python scripts this morning to help with the transition of moving everything to <code>src/</code>. One deletes <code>.olean</code> files without a corresponding <code>.lean</code> file, the other deletes directory trees that contain no files.<br>
I notice <span class="user-mention" data-user-id="110026">@Simon Hudon</span> also wrote an equivalent shell script in the fold PR (<a href="https://github.com/leanprover/mathlib/pull/376/files#diff-81a7c4de26bf82dac09e943b11b95792" target="_blank" title="https://github.com/leanprover/mathlib/pull/376/files#diff-81a7c4de26bf82dac09e943b11b95792">https://github.com/leanprover/mathlib/pull/376/files#diff-81a7c4de26bf82dac09e943b11b95792</a>).<br>
Windows users: is one of shell scripts/Python scripts more usable than the other?</p>

#### [ Jeremy Avigad (Jan 24 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/clean%20up%20old%20files/near/156801906):
<p>BTW, I simply used <code>git clean -xdf</code> to do this (<code>git clean -xdn</code> will do a dry run without deleting anything).</p>


{% endraw %}
