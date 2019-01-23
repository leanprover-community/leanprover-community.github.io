---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/89474ultrafilters.html
---

## Stream: [maths](index.html)
### Topic: [ultrafilters](89474ultrafilters.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136077666):
I want to define the ultrafilter monad. I suppose this means I need a bundled type: filter plus the ultrafilter property. (Currently, we have `ultrafilter : Π {α : Type u}, filter α → Prop`.) Thoughts on naming?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136077752):
I assume naming it `β` won't fly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079204):
Would it be okay to rename `ultrafilter` to `is_ultrafilter`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079213):
I think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079266):
otherwise, I'm having a hard time coming up with a name for the bundled thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136079285):
I guess I should just say "subtype"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 19 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136094257):
renaming `ultrafilter` to `is_ultrafilter` is fine for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 19 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ultrafilters/near/136094337):
Alternatively, you could have called it `Ultrafilter`...


{% endraw %}
