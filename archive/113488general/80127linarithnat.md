---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80127linarithnat.html
---

## Stream: [general](index.html)
### Topic: [linarith nat](80127linarithnat.html)

---


{% raw %}
#### [ Patrick Massot (Dec 23 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20nat/near/152434102):
Is it part of the known limitations of `linarith` that I can't do better than
```lean
example  (n m : ℕ) (h : 0 < n) (h' : ¬ m < n) : m - n < m :=
begin
  apply nat.sub_lt ;
  linarith
end
```
I would like to get rid of the first line?

#### [ Patrick Massot (Dec 23 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20nat/near/152434103):
@**Rob Lewis**

#### [ Rob Lewis (Dec 23 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20nat/near/152436375):
To `linarith`, `m - n` is some arbitrary constant with type `nat` that it knows no extra information about. So no, it shouldn't be expected to solve that.


{% endraw %}
