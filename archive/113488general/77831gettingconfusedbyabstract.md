---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77831gettingconfusedbyabstract.html
---

## Stream: [general](index.html)
### Topic: [getting confused by 'abstract'](77831gettingconfusedbyabstract.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 16 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20confused%20by%20%27abstract%27/near/128164505):
I'm really confused by `abstract`. I've used it successfully in the past, but tonight it just won't do anything for me.  Can anyone see what's wrong with this:
````
open tactic

structure C :=
(a : ℕ)
(b : a > 0)
(c : array a ℕ)

lemma H : C :=
begin
abstract foo { split, rotate 2, exact 1, abstract { exact dec_trivial }, split, abstract bar { intros, exact 0 } }
end

set_option pp.proofs true
#print H   -- theorem H : C := {a := 1, b := of_as_true trivial, c := {data := λ (i : fin 1), 0}}
#print foo -- 'unknown identifier foo'
#print bar -- 'unknown identifier bar'
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 16 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20confused%20by%20%27abstract%27/near/128165091):
Ah... writing `lemma` instead of `def`.


{% endraw %}
