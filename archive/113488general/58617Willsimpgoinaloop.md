---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58617Willsimpgoinaloop.html
---

## Stream: [general](index.html)
### Topic: [Will simp go in a loop?](58617Willsimpgoinaloop.html)

---

#### [Kenny Lau (Apr 03 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Will%20simp%20go%20in%20a%20loop%3F/near/124558352):
If I have two simp lemmas that are the inverse of each other, will simp go into a loop? For example:
```
@[simp] lemma mul_act : (g * h) • x = g • h • x :=
group_action.mul g h x

@[simp] lemma act_act : g • h • x = (g * h) • x :=
eq.symm $ group_action.mul g h x
```

#### [Mario Carneiro (Apr 03 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Will%20simp%20go%20in%20a%20loop%3F/near/124558393):
Why don't you try it? I think the answer is yes

#### [Kenny Lau (Apr 03 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Will%20simp%20go%20in%20a%20loop%3F/near/124558407):
I tried it and it succeeded

#### [Kenny Lau (Apr 03 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Will%20simp%20go%20in%20a%20loop%3F/near/124558449):
oh, it went in a loop when the goal can't be closed

#### [Simon Hudon (Apr 03 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Will%20simp%20go%20in%20a%20loop%3F/near/124558451):
I think you should think of `simp` lemmas as a way to decrease the complexity of your expressions. If they cancel each other, one of them must not be decreasing the complexity. Which one should you apply by name?

