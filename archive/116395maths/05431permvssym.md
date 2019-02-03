---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/05431permvssym.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [perm vs sym](https://leanprover-community.github.io/archive/116395maths/05431permvssym.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134819090):
<p>In the determinants PR <a href="https://github.com/leanprover/mathlib/pull/378#issuecomment-425396841" target="_blank" title="https://github.com/leanprover/mathlib/pull/378#issuecomment-425396841">https://github.com/leanprover/mathlib/pull/378#issuecomment-425396841</a> I have copy-pasted <span class="user-mention" data-user-id="110064">@Kenny Lau</span>s take on the symmetric group (<code>group_theory/sym.lean</code>). But in <code>group_theory/perm.lean</code> we already have a version by <span class="user-mention" data-user-id="110044">@Chris Hughes</span>. Both files are several hundred lines long. There is substantial overlap, but both take their own approach in several places. I would like to use this thread to discuss how to merge these two files.</p>

#### [ Johan Commelin (Sep 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134819387):
<p>Oh, the PR is from the <code>determinants</code> branch on community mathlib.</p>

#### [ Chris Hughes (Sep 28 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134821943):
<p>I think I've done everything necessary for determinants, now that fintype is in mathlib, so anything that Kenny's done should probably be PRed separately from determinants.</p>

#### [ Johan Commelin (Sep 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134826417):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110044">@Chris Hughes</span> I removed <code>group_theory/sym.lean</code>.</p>


{% endraw %}
