---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70244casesintermmode.html
---

## Stream: [maths](index.html)
### Topic: [cases in term mode](70244casesintermmode.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937140):
I am trying to tell Lean what a path in a quiver is. How do I finish `is_a_path`?
```lean
universes u

structure quiver :=
(V : Type u)
(E : Type u)
(s : E → V)
(t : E → V)

variable {Q : quiver}

definition is_a_path : (list Q.E) → Prop :=
λ l, sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937192):
hint: use `list.chain`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937200):
```lean
inductive list.chain : Π {α : Type u}, (α → α → Prop) → α → list α → Prop
constructors:
list.chain.nil : ∀ {α : Type u} (R : α → α → Prop) (a : α), list.chain R a list.nil
list.chain.cons : ∀ {α : Type u} {R : α → α → Prop} {a b : α} {l : list α},
  R a b → list.chain R b l → list.chain R a (b :: l)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937201):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937248):
By the way, do you think it is a good idea to use lists to capture paths?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937304):
You may want more complicated inductive structures in some circumstances, but here a list of edges is sufficient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937307):
```lean

universes u v

structure quiver :=
(V : Type u)
(E : Type v)
(s : E → V)
(t : E → V)

variable {Q : quiver}

definition is_a_path : (list Q.E) → Prop
| []             := true
| [x]            := true
| (hd1::hd2::tl) := Q.t hd1 = Q.s hd2 ∧ is_a_path (hd2::tl)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937323):
Aaah, so I should use `|`. Thanks! But now you are not using `list.chain`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937326):
you could use `list.chain` for the latter two cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937328):
the definition using `list.chain` is left to the reader as an exercise :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937371):
alternatively, you could define it as an inductive type, which may be more natural

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937375):
oh... I just realized I wanted induction-recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937379):
not for this...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937383):
```lean
mutual inductive path, head
with path : Type (max u v)
| A : Q.E → path
with head : path → Q.V
| (path.A x) := _
```
failed idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937390):
you want the head to be a parameter, like in `chain`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937446):
oh what

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937459):
Kenny, I don't understand your last definition. What does `mutual` do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937460):
https://leanprover.github.io/theorem_proving_in_lean/theorem_proving_in_lean.pdf
P.120, Section 7.9

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937499):
note that I was trying induction-recursion which is not a thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937501):
not to confuse you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937524):
But your current definition is not equivalent to mine, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937532):
yours? I haven't seen your definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937572):
Hmm, agreed. My bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937574):
Let me try again: your second definition is not equivalent to your first, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937576):
but I haven't finished my second definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937591):
Aaah, ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937592):
@**Mario Carneiro** (maybe on its own thread?) if Lean had induction-recursion, would you be able to prove false? would there be a shorter proof than following godel?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937643):
No. Induction recursion would strengthen the system, it wouldn't be able to prove its own consistency because it now has induction-recursion and the simulated lean language would not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937649):
why can't you simulate induction-recursion with induction-recursion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937654):
you probably need induction-recursion-recursion or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937655):
hmm


{% endraw %}
