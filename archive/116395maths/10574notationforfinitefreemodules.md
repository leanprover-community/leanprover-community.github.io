---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10574notationforfinitefreemodules.html
---

## Stream: [maths](index.html)
### Topic: [notation for finite free modules](10574notationforfinitefreemodules.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/notation%20for%20finite%20free%20modules/near/132570684):
Some students here have developed the basic theory of free modules of finite rank over a ring (which later becomes a commutative ring and then a field). One issue I have with their work is that they are still using some placeholder notation for the fundamental construction of $$R^n$$, the free rank $$n$$ module over the ring $$R$$. What should the function which takes a ring `R` and a natural `n` and returns the `R`-module `R^n` be called? Any suggestions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/notation%20for%20finite%20free%20modules/near/132580671):
I guess there are two questions: name, and notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/notation%20for%20finite%20free%20modules/near/132580689):
For notation, assuming we can't use `R^n`, how about `R^⊕n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 22 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/notation%20for%20finite%20free%20modules/near/132581065):
Why can't we use `R^n`? As for the name, how about `finite_free_module R n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/notation%20for%20finite%20free%20modules/near/132581638):
Maybe we can use `R^n`, but in that case I assumed there was no choice to be made :)


{% endraw %}
