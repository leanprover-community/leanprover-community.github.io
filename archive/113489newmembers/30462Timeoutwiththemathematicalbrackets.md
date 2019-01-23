---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/30462Timeoutwiththemathematicalbrackets.html
---

## Stream: [new members](index.html)
### Topic: [Time out with the mathematical brackets](30462Timeoutwiththemathematicalbrackets.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141051):
I've defined a prime field, and tried to define a function that maps `int` to`pf`, but somehow timeout at the function...
```
def pf {p : ℕ} := {e // prime p ∧ 0 ≤ e ∧ e < p}

variable {p : ℕ}

def int_to_pf (x : ℤ) : @pf p := ⟨x, begin end⟩
```

while my friend succeed with
```
def pf (p  : ℕ ) [prime p] := {e // 0 ≤ e ∧ e < p}

variable p : ℕ
variable [pp: prime p]

def int_to_pf (x : ℤ) : @pf p (prime p) :=  ⟨x, begin end⟩
```

Why is there a difference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 04 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141678):
you are casting an `int` to a `nat` in both examples, this times out searching for a coercion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 04 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141733):
In the second example it fails fast only because it gets stuck in the type of the theorem: `@pf p (prime p)` is not well typed because `prime p` does not have type `prime p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141838):
sorry for a mistake, I think my friend wrote
```
pp: prime p
def int_to_pf (x : ℤ) : @pf p pp ...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141882):
Where did I cast int to nat?
Aren't elements in pf all have value of type nat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Nov 04 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144099):
Your x in int to pf is an int?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144602):
yes, but aren't val of elements of type pf also int?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Nov 04 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144763):
You defined p in pf as a nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144977):
But the second example can work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 04 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137145287):
lean does not have a subtyping relation, so if something has type `pf p` it does not have type `int`. But more importantly you are going the other way around here: `x` has type `int` and you are putting it in the first component of `pf p`, which you didn't write explicitly (it is the type of `e`) but is `nat`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137145499):
Oh!! Got it! thanks a lot!!

