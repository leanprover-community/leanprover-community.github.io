---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31843unfoldingdefinitions.html
---

## Stream: [general](index.html)
### Topic: [unfolding definitions](31843unfoldingdefinitions.html)

---


{% raw %}
#### [ Guy Leroy (Aug 22 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20definitions/near/132573040):
I have the following def:
```lean
def jacobi_sym : ℤ → ℤ → ℤ
| a          1 := 1
| a          b := if b % 2 = 1 then jacobi_sym_aux a b else 0

local notation {a|b} := jacobi_sym a b 
```
and I am trying to prove 

```lean
h : ¬n = 1
⊢ {a|n} = ite (quadratic_res a n ∧ ¬n ∣ a) 1 (ite (¬quadratic_res a n) (-1) 0)
```

How can I unfold ``` jacoby_sym ``` such that it shows ``` if b % 2 = 1 then jacobi_sym_aux a b else 0``` ? 
If I write ```unfold jacobi_sym``` the tactic fails

#### [ Kenny Lau (Aug 22 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20definitions/near/132573174):
MWE please

#### [ Kenny Lau (Aug 22 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20definitions/near/132573310):
but `rw [jacobi_sym.equations._eqn_2 a n h]` should work

#### [ Kenny Lau (Aug 22 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20definitions/near/132573444):
but a better solution would be to not use the equation compiler to define `jacobi_sym`, but rather use ite

#### [ Guy Leroy (Aug 22 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20definitions/near/132573551):
Thank you very much!

#### [ Simon Hudon (Aug 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20definitions/near/132583964):
Out of curiosity, have you tried `dunfold`? It is based on `dsimp` which is more careful about preserving definitional equality.


{% endraw %}
