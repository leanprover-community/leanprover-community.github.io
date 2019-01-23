---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13941Importinganalysisnormedspacedmakesthingsnoncomputable.html
---

## Stream: [new members](index.html)
### Topic: [Importing analysis.normed_spaced makes things noncomputable](13941Importinganalysisnormedspacedmakesthingsnoncomputable.html)

---

#### [Abhimanyu Pallavi Sudhir (Dec 18 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Importing%20analysis.normed_spaced%20makes%20things%20noncomputable/near/152088656):
The following code:

```lean
import data.real.basic

def seq : Type := ℕ → ℝ
def seq_add : seq → seq → seq := λ s t n, s n + t n
```

Works perfectly fine, but if I add `import analysis.normed_space`to the top, `seq_add` becomes noncomputable, it `depends on real.normed_field`. But this line works perfectly with or without the import:

```lean
def seq_smul (c : ℝ) : seq → seq := λ s n, c * (s n)
```

#### [Mario Carneiro (Dec 18 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Importing%20analysis.normed_spaced%20makes%20things%20noncomputable/near/152088730):
hm, I guess the instance priorities need adjustment

