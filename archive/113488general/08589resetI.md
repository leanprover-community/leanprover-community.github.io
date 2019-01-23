---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08589resetI.html
---

## Stream: [general](index.html)
### Topic: [resetI](08589resetI.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 11 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124910648):
Is there any reason `resetI` wouldn't work in the latest nightly? I have a very short proof with `intro ; resetI` in it and I get:

```
excessive memory consumption detected at 'vm' (potential solution: increase memory consumption threshold)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 11 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124911049):
Ok, I found the problem. I had a local definition of `resetI` that just called `mathlib`'s `resetI` but it wasn't fully qualified so it just worked as a recursive function ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 11 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124911339):
oh thank god... fixing `resetI` was giving me nightmares

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 11 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124911556):
It doesn't seem to give you much leeway in how you use it, am I wrong?


{% endraw %}
