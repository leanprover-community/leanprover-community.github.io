---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26316inequalityproof.html
---

## Stream: [general](index.html)
### Topic: [inequality proof](26316inequalityproof.html)

---


{% raw %}
#### [ Kevin Sullivan (Sep 14 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133955902):
What is the simplest exact proof term that proves ~0=1 (not zero equals one)?

#### [ Kevin Sullivan (Sep 14 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956061):
I.e., without tactics complete this: theorem zneqo: not 0 = 1 := _

#### [ Rob Lewis (Sep 14 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956252):
`zero_ne_one`

#### [ Rob Lewis (Sep 14 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956802):
Oh, wait, there's a better one, although it may not count depending on what you call an "exact proof term."
```lean
theorem zneqo : ¬ (0 = 1).
#check zneqo
```

#### [ Kenny Lau (Sep 14 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956828):
dec_trivial

#### [ Rob Lewis (Sep 14 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133957509):
`dec_trivial` is notation for a tactic though.

#### [ Kenny Lau (Sep 14 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133957581):
dec_trivial isn't a tactic

#### [ Rob Lewis (Sep 14 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133957629):
It's notation for `of_as_true (by tactic.triv)`

#### [ Kenny Lau (Sep 14 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958450):
heh...

#### [ Kevin Sullivan (Sep 14 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958695):
Right. I'm really looking for the proof term that I'd write to fill in the _. It'd presumably say something about injectivity of constructors.

#### [ Rob Lewis (Sep 14 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958745):
That's what the `.` proof is doing under the hood. Look at the proof term it generates.
```lean
theorem zneqo : ¬ (0 = 1).
#print zneqo
```

#### [ Kevin Sullivan (Sep 14 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958775):
```quote
Oh, wait, there's a better one, although it may not count depending on what you call an "exact proof term."
```lean
theorem zneqo : ¬ (0 = 1).
#check zneqo
```
```
Right, I'm really looking for the proof term that I'd use to fill in the _. Presumably something about injectivity of constructors. Also, where is it documented that and how Lean accepts your version?

#### [ Reid Barton (Sep 14 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958894):
This is the `no_confusion` stuff right?

#### [ Reid Barton (Sep 14 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959044):
The strategy is: you can define a function `t : nat \to Prop` which sends `nat.zero` to `false` and `nat.succ _` to `true` (using `nat.cases`). Then if you had an equality `nat.zero = nat.succ x`, you could use it to transport `trivial : true` to a proof of `false`

#### [ Rob Lewis (Sep 14 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959061):
It's an empty pattern match. I guess it's documented somewhere in TPiL, but I couldn't tell you where. The only proof that `0 = 1` is by `rfl`, but this is structurally impossible, and the equation compiler fills in the `no_confusion` proof automatically.

#### [ Reid Barton (Sep 14 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959100):
I think if you look for `no_confusion` in TPiL you might be able to find it

#### [ Kenny Lau (Sep 14 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959429):
```lean
prelude

inductive nat : Type
| zero : nat
| succ : nat → nat

inductive eq {α : Sort*} (x : α) : α → Sort 0
| refl : eq x

inductive false : Sort 0.

def strange_prop (n : nat) : Sort 0 :=
nat.rec_on n (eq nat.zero nat.zero) (λ n _, false)

example : (eq nat.zero (nat.succ nat.zero)) → false :=
λ H, show strange_prop (nat.succ nat.zero),
from eq.rec_on H (eq.refl nat.zero)
```

#### [ Kenny Lau (Sep 14 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959494):
also see [this](https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/) blogpost by kevin

#### [ Kenny Lau (Sep 14 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959561):
(I followed Reid Barton's idea)

#### [ Kevin Sullivan (Sep 15 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133993284):
```quote
That's what the `.` proof is doing under the hood. Look at the proof term it generates.
```lean
theorem zneqo : ¬ (0 = 1).
#print zneqo
```
```
Sorry, here's a better response.

First, the proof term is: λ (a : 0 = 1), eq.dcases_on a (λ (a_1 : 1 = 0), nat.no_confusion a_1) (eq.refl 1) (heq.refl a)

However, when I copy and paste it in place of the underscore, after the :=, I get the following error. Still not sure exactly what I need to type after the := as an exact proof term.

[Lean]
"eliminator" elaborator type mismatch, term
  λ (a_1 : 1 = 0), nat.no_confusion a_1
has type
  1 = 0 → nat.no_confusion_type (_ == _ → false) 1 0
but is expected to have type
  0 = 0 → _ == _ → false
Additional information:
/Users/sullivan/teaching/2102f18/cs-dm.sullivan/06_Negation/00_intro.lean:60:40: context: the inferred motive for the eliminator-like application is
  λ (_x : ℕ) (_x_1 : 0 = _x), _x = _x → _x_1 == _x_1 → false
eq.dcases_on : ∀ {α : Type} {a : α} {C : Π (a_1 : α), a = a_1 → Prop} {a_1 : α} (n : a = a_1), C a _ → C a_1 n

#### [ Andrew Ashworth (Sep 15 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133998674):
`example : 0 ≠ 1 := λ h, nat.no_confusion h`

#### [ Kevin Sullivan (Sep 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/134026746):
```quote
`example : 0 ≠ 1 := λ h, nat.no_confusion h`
```
Thank you. That got me where I needed to go.


{% endraw %}
