---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96945quotientmodulebreakage.html
---

## Stream: [maths](index.html)
### Topic: [quotient_module breakage](96945quotientmodulebreakage.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325716):
```lean
import data.set.basic
import linear_algebra.quotient_module

example (R : Type*) (S : set R) [ring S] : S :=
begin
  exact (4 : S)
end

/-

maximum class-instance resolution depth has been reached (the limit can be increased by setting option 'class.instance_max_depth') (the class-instance resolution trace can be visualized by setting option 'trace.class_instances')
state:
R : Type ?,
S : set R,
_inst_1 : ring ↥S
⊢ ↥S

-/
```

What is going on here? If I remove the import of `linear_algebra.quotient_module` then this compiles fine. @**Chris Hughes** you thought about quotient module instances maybe -- do you know how to diagnose these things?

Related -- I have to ask here because I cannot diagnose the issue myself.  I cannot read the `trace.class_instances` output and I would really love to be able to. For what it's worth, just before it chokes it looks like this gist (and it's quite funny, manifestly something has gone wrong and it's a nice change from the usual, it's not a loop, it's a recursive hell).

https://gist.github.com/kbuzzard/2582db6593c7b7467f3e0020909af467

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325803):
nice picture

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325866):
Could you give a more realistic example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325879):
Is R actually a ring and S a subring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325883):
I don't understand why that would compile. If S is empty, it's trivial to get a contradiction from this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325972):
Also note I had to modify stuff like this recently in the perfectoid project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326401):
There's nothing wrong with the statement of the theorem. It is a set with a ring structure, which is therefore nonempty and has a `4`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326574):
As usual, modules are acting up because of the search for a ring instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326633):
Chris : you're happy with `(x : nat) (h : x > 4)`, right? But if x was 2 it's trivial to get a contradiction from this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326662):
As long as it's a nonempty set there is a ring structure on it and a `4`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326675):
and being a ring implies it is nonempty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326693):
Patrick -- it was trying to fix up the perfectoid project which led me to this. We need p in R^o for the definition to be OK. The statement that p divides something in R is vacuous because p is a unit in R -- R is like Q_p and R^o is like Z_p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326712):
I don't think the offending instances are in `quotient_module`. Do you get the same problem with `algebra.pi_instances` and `algebra.module`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326777):
anyway this is yet another problem that will be solved by my refactor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326801):
OK, I can definitely wait. I was planning on spending tomorrow thinking about the perfectoid project in a top-down way; this issue came up because the definition of a perfectoid ring is currently broken :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134327608):
I'm having a day off real life tomorrow; my last day off for a while.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331345):
```quote
Patrick -- it was trying to fix up the perfectoid project which led me to this. We need p in R^o for the definition to be OK. The statement that p divides something in R is vacuous because p is a unit in R -- R is like Q_p and R^o is like Z_p
```
I told you to carefully review that PR. I fixed the compilation error but I was really unsure I didn't change the maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331353):
```quote
I'm having a day off real life tomorrow; my last day off for a while.
```
Do you mean you'll have a Lean day or a no-Lean day?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331541):
```quote
anyway this is yet another problem that will be solved by my refactor
```
Do you have any estimation about when this refactor will be ready for use?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331826):
I am going to have a Lean day, but it's a bit cheeky -- I should really be doing other things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331861):
Do you have stuff you can do without modules? Do you want to have fun with uniform spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331952):
ha ha, I have been working from the bottom up during the little time I've had over the last month or so. I was going to try defining the presheaf on Spa(A), sorrying whatever I couldn't do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331983):
Great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331986):
It gets my vote


{% endraw %}
