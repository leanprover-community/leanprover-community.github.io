---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51171oleanfiles.html
---

## Stream: [general](index.html)
### Topic: [olean files](51171oleanfiles.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 06 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20files/near/133457869):
If I invoke lean on a single file like `lean src/category_theory/rel.lean`, then it should write out an `.olean` file if it finishes and succeeds, right? (Let's say there is no existing `.olean` file to start with.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 06 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20files/near/133457924):
No, you need `--make` as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 06 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20files/near/133458106):
Oh okay. Well that's one mystery solved.
I still have a situation where `leanpkg build` is doing a build which is running out of memory, but I'm pretty sure it has finished building a lot of other files first, and it's not writing `.olean` files for them. But I should at least be able to work around that now


{% endraw %}
