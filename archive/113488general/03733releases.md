---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03733releases.html
---

## Stream: [general](index.html)
### Topic: [releases](03733releases.html)

---


{% raw %}
#### [ Patrick Massot (Mar 05 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123313063):
<p>Is there anything like a Lean release policy? It seems to me quite a bit happened since Lean 3.3.0 and I don't see any indication that some new release is coming.</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123342909):
<p>short answer: no</p>

#### [ Patrick Massot (Mar 06 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344199):
<p>I suspected the short answer. Is there a longer answer?</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344597):
<p>The long answer is that we really haven't given much thought to a release policy yet. There are many refactorings going on right now, so maybe after that would be a good time for a release. Though that may also describe Lean's perpetual state.</p>

#### [ Patrick Massot (Mar 06 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344647):
<p>Do you mean after monad refactoring or after new parser/hygienic stuff?</p>

#### [ Mario Carneiro (Mar 06 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344665):
<blockquote>
<p>Though that may also describe Lean's perpetual state.</p>
</blockquote>
<p>this</p>

#### [ Mario Carneiro (Mar 06 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344716):
<p>I don't think lean will reach a "stopping point" in my lifetime...</p>

#### [ Mario Carneiro (Mar 06 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344726):
<p>If anything it will probably die someday (hopefully long) in the future in the middle of another refactoring</p>

#### [ Patrick Massot (Mar 06 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344769):
<p>I'm very happy that Lean is always improving. The reason why I ask for releases is because TPIL doesn't update between releases. And I fear that this wonderful resource will become useless (or even confusing hence harmful)</p>

#### [ Mario Carneiro (Mar 06 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123345794):
<p>Of course it is not a bad thing that lean is always in an improvement cycle, but I point this out only to stress that there is no point waiting for development to stop or even finish a big project before making a release. I think releases should be done at any point once a decent amount of changes have accrued since the last release. By my estimate we have passed at least 3 minor versions' worth of material since 3.3.0</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123347274):
<p>I will ask Leo about a release after the monad/type_context/name refactorings (yeah, I do think right now is a particularly bad time). On the other hand, for TPIL I think it would be great to have some kind of versioned docs a la <a href="https://robpol86.github.io/sphinxcontrib-versioning/" target="_blank" title="https://robpol86.github.io/sphinxcontrib-versioning/">https://robpol86.github.io/sphinxcontrib-versioning/</a></p>

#### [ Patrick Massot (Mar 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123347386):
<p>I already suggested having two branches of TPIL on the relevant github issue board</p>

#### [ Sebastian Ullrich (Mar 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123347502):
<p>Yes, and that plugin would allow us to show both branch contents on the same page. We should really do that for the reference too.</p>

#### [ Patrick Massot (Mar 06 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123350064):
<p>That sounds nice, I'll try to push this idea. You can go back to think about smarter issues <span class="emoji emoji-1f604" title="smile">:smile:</span></p>


{% endraw %}
