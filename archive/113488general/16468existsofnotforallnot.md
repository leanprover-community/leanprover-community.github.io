---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16468existsofnotforallnot.html
---

## Stream: [general](index.html)
### Topic: [exists_of_not_forall_not](16468existsofnotforallnot.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 10 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists_of_not_forall_not/near/123536960):
<p>I am a classical guy. Is <code>example (α : Type) (P : α → Prop) : (¬ (∀ a : α, ¬ P a)) → (∃ a : α, P a) := sorry</code> already in Lean or mathlib?</p>

#### [ Andrew Ashworth (Mar 10 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists_of_not_forall_not/near/123537206):
<p>some variant is in mathlib, see <code>not_forall</code> and the lemmas near it in <code>logic/basic.lean</code></p>

#### [ Kevin Buzzard (Mar 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists_of_not_forall_not/near/123538465):
<p>Thanks. My mistake was searching for exists_of rather than concentrating on not_forall...</p>

#### [ Chris Hughes (Mar 10 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists_of_not_forall_not/near/123539394):
<blockquote>
<p>Thanks. My mistake was searching for exists_of rather than concentrating on not_forall...</p>
</blockquote>
<p>I thought the convention was that lemmas should be named after their conclusion.</p>

#### [ Kevin Buzzard (Mar 10 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists_of_not_forall_not/near/123540476):
<p>Yes but the lemma in the library was an iff ;-)</p>


{% endraw %}
