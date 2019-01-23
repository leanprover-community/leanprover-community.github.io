---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83252nonemptyquotient.html
---

## Stream: [general](index.html)
### Topic: [nonempty quotient](83252nonemptyquotient.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nonempty%20quotient/near/134934075):
Do we already have something like:
```lean
lemma nonempty_quotient_iff {α : Type*} (s : setoid α) : nonempty (quotient s) ↔ nonempty α :=
begin
  split ; rintro ⟨c⟩,
  { cases quotient.exists_rep c with a h, 
    exact ⟨a⟩ },
  { exact ⟨⟦c⟧⟩ }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 30 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nonempty%20quotient/near/134935619):
That would be in `data/quot` and I don't see it there.

