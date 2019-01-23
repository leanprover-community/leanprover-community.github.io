---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93629anotherextensionalitylemma.html
---

## Stream: [general](index.html)
### Topic: [another extensionality lemma?](93629anotherextensionalitylemma.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/another%20extensionality%20lemma%3F/near/147421643):
Any complaints about adding `@[extensionality]` to `subtype.eq`?
```
protected lemma eq : ∀ {a1 a2 : {x // p x}}, val a1 = val a2 → a1 = a2
| ⟨x, h1⟩ ⟨.(x), h2⟩ rfl := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 10 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/another%20extensionality%20lemma%3F/near/147421650):
(deleted)


{% endraw %}
