---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/99756468revisedlimitsPR.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#468 revised limits PR](https://leanprover-community.github.io/archive/144837PRreviews/99756468revisedlimitsPR.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 09 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23468%20revised%20limits%20PR/near/147348952):
<p>Is this the biggest PR so far? Adds +3,634 lines.</p>

#### [ Scott Morrison (Nov 09 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23468%20revised%20limits%20PR/near/147349003):
<p>Of course, because writing an all-singing all-dancing <code>dualize</code> tactic still feels hard, you get to divide that number by exactly two, since everything gets said exactly twice ...</p>

#### [ Kenny Lau (Nov 09 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23468%20revised%20limits%20PR/near/147357101):
<p>Is <code>dualize</code> harder than <code>to_additive</code>?</p>

#### [ Scott Morrison (Nov 10 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23468%20revised%20limits%20PR/near/147411779):
<p>Yes. At the very least, there needs to be a mechanism to tell it which category needs to be "opposited" --- lots of the theorems we have in the limits PR talk about several categories at once, and it's the categories we take limits in that need to be switched, while the diagram categories don't.</p>

#### [ Scott Morrison (Nov 10 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23468%20revised%20limits%20PR/near/147411782):
<p>If someone wants to prove me wrong, and start writing a <code>dualize</code> tactic, that would be awesome. :-)</p>

#### [ Scott Morrison (Nov 15 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23468%20revised%20limits%20PR/near/147769590):
<p>I've just removed <code>examples/CommRing/equalizers.lean</code>, that still deserved more work, and so the <code>limits</code> branch is ready for further review and/or merging.</p>


{% endraw %}
