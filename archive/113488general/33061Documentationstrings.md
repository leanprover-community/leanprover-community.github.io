---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33061Documentationstrings.html
---

## Stream: [general](index.html)
### Topic: [Documentation strings](33061Documentationstrings.html)

---


{% raw %}
#### [ Joe Hendrix (Aug 06 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131003087):
<p>Is there a convention in Lean for attaching documentation to specific declarations as in Haddock or Javadoc?</p>

#### [ Reid Barton (Aug 06 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131003136):
<p>Yes. use <code>---</code> or <code>/-- ... -/</code></p>

#### [ Joe Hendrix (Aug 06 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131003264):
<p>Does that show up in the Emacs or VSCode interfaces?  I'm using the emacs interface primarily.</p>

#### [ Joe Hendrix (Aug 06 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131003391):
<p>Surprisingly, I get an error <code>command expected</code> when I use the <code>/-- ... -/</code> syntax in front of a record field name.  So it seems like there is some parsing.</p>

#### [ Simon Hudon (Aug 06 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131003541):
<p>In emacs, it should show you the doc string in the minibuffer. </p>
<blockquote>
<p>Surprisingly, I get an error command expected when I use the /-- ... -/ syntax in front of a record field name.</p>
</blockquote>
<p>I think they are only allowed on declarations (<code>theorem</code>, <code>def</code>, <code>constant</code>, etc) and not on their components.</p>

#### [ Joe Hendrix (Aug 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131003709):
<p>Thanks!  I see it now.</p>

#### [ Mario Carneiro (Aug 06 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20strings/near/131004824):
<p>for other places in a definition you should just use normal comments (<code>--</code> or <code>/- -/</code>), not doc comments</p>


{% endraw %}
