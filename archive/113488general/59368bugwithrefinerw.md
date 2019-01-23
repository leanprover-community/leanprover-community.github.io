---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59368bugwithrefinerw.html
---

## Stream: [general](index.html)
### Topic: [bug with refine + rw](59368bugwithrefinerw.html)

---

#### [Kenny Lau (Dec 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20refine%20%2B%20rw/near/152093977):
```lean
example (H : (0 = 0 → 0 = 1) → true) : true :=
begin
  refine H (λ h, _), rw h --fails
/-
rewrite tactic failed, lemma is not an equality nor a iff
state:
H : (0 = 0 → 0 = 1) → true,
h : 0 = 0
⊢ 0 = 1
-/
end


example (H : (0 = 0 → 0 = 1) → true) : true :=
begin
  refine H _, intro h, rw h --works
end
```

#### [Kenny Lau (Dec 18 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20refine%20%2B%20rw/near/152094049):
and also workaround:
```lean
example (H : (0 = 0 → 0 = 1) → true) : true :=
begin
  refine H (λ h, _),
  change _ at h, rw h --works
end
```

