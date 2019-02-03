---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/89474ultrafilters.html
---

## Stream: [maths](index.html)
### Topic: [ultrafilters](89474ultrafilters.html)

---


{% raw %}
#### [ Reid Barton (Oct 19 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136077666):
<p>I want to define the ultrafilter monad. I suppose this means I need a bundled type: filter plus the ultrafilter property. (Currently, we have <code>ultrafilter : Π {α : Type u}, filter α → Prop</code>.) Thoughts on naming?</p>

#### [ Reid Barton (Oct 19 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136077752):
<p>I assume naming it <code>β</code> won't fly</p>

#### [ Reid Barton (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079204):
<p>Would it be okay to rename <code>ultrafilter</code> to <code>is_ultrafilter</code>?</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079213):
<p>I think so</p>

#### [ Reid Barton (Oct 19 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079266):
<p>otherwise, I'm having a hard time coming up with a name for the bundled thing</p>

#### [ Reid Barton (Oct 19 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079285):
<p>I guess I should just say "subtype"</p>

#### [ Johannes Hölzl (Oct 19 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136094257):
<p>renaming <code>ultrafilter</code> to <code>is_ultrafilter</code> is fine for me.</p>

#### [ Johan Commelin (Oct 19 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136094337):
<p>Alternatively, you could have called it <code>Ultrafilter</code>...</p>


{% endraw %}
