---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93629anotherextensionalitylemma.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [another extensionality lemma?](https://leanprover-community.github.io/archive/113488general/93629anotherextensionalitylemma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/another%20extensionality%20lemma%3F/near/147421643):
<p>Any complaints about adding <code>@[extensionality]</code> to <code>subtype.eq</code>?</p>
<div class="codehilite"><pre><span></span>protected lemma eq : ∀ {a1 a2 : {x // p x}}, val a1 = val a2 → a1 = a2
| ⟨x, h1⟩ ⟨.(x), h2⟩ rfl := rfl
</pre></div>

#### [ Scott Morrison (Nov 10 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/another%20extensionality%20lemma%3F/near/147421650):
<p>(deleted)</p>


{% endraw %}
