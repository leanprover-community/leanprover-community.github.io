---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/48097CreatingdefinitionsinLean.html
---

## Stream: [new members](index.html)
### Topic: [Creating definitions in Lean](48097CreatingdefinitionsinLean.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772739):
I am trying to define an equivalence class in Lean, where I already have a binary relation, defined as a variable `variable (r : S → S → Prop)` -- how would I insert the requirement of `binary_relation` satisfying `equivalence` while defining an equivalence class?

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772781):
I.e. surely just def `class (a : S) : set S := { x | r x a }` is not enough. Do I need some squiggly brackets here to impose the requirement `equivalence binary_relation`?

#### [ Kenny Lau (Oct 14 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772896):
the philosophy is that we create the definition as general as possible, and only insert the hypothesis in the proofs

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772964):
Perhaps, but I just want to learn how definitions work. Can we make them specific in this way?

#### [ Kenny Lau (Oct 14 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772975):
`def equivalence_class (h : is_equivalence r) (a : S) : set S := { x | r x a }`

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135773069):
Right, and then when using the definition we'd need to provide a proof of is_equivalence r as a parameter, right?

#### [ Kenny Lau (Oct 14 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135773077):
yes

#### [ Bryan Gin-ge Chen (Oct 14 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135773243):
Note that if you use that definition, the variable `r` becomes something lean can very easily infer. Thus it's convenient to make it implicit (by writing `variable {r}` immediately beforehand), so that when you use `equivalence_class`, you won't need to write `equivalence_class r h a` but only `equivalence_class h a`.

#### [ Kevin Buzzard (Oct 14 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135777737):
@**Abhimanyu Pallavi Sudhir** just to note that `class` is already a keyword in Lean so you might want to stick to Kenny's suggestion of `equivalence_class` in any experiments you try.


{% endraw %}
