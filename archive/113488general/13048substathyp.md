---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13048substathyp.html
---

## Stream: [general](index.html)
### Topic: [subst at hyp](13048substathyp.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497289):
Could we have `subst foobar at hyp` for substituting in the hypotheses of the local context? Currently I am using `repeat {rw foobar at hyp}` which feels a bit verbose...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497352):
`subst foobar`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497411):
What about `simp only [foobar] at hyp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497450):
aah never mind. `subst` is only for local constants. I wanted to substitute `x = y` where `x = y` was the result of some proposition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497493):
`simp only` works!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497565):
MWE?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497570):
https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497619):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497678):
Right, so now you only see the `simp`s. For the `repeat {rw ...}` you have to look in the history.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497681):
Basically I'm challenging you to golf it :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497852):
what import is allowed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497883):
I don't really care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497892):
What would you want to use? `tidy`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497943):
you didn't import any file from mathlib, so I can't use any mathlib tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497962):
Wasnt `have ... simp at this ... exact this` some sort of idiom that can be golfed into a `simpa`-oneliner? I tried but failed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498111):
`simpa using this`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498115):
Or rather `simpa using ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498231):
And what do I need to import to get `simpa`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498273):
My attempt: https://gist.github.com/rwbarton/b79b804e4bff300a5aa2a4ec2951c55e

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498276):
Anything in mathlib, but say `tactic.interactive`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498303):
```lean
import tactic.interactive

universe u

namespace eckmann_hilton
variables (X : Type u)

local notation a `<`m`>` b := @has_mul.mul X m a b

class is_unital [m : has_mul X] [e : has_one X] : Prop :=
(one_mul : ∀ x : X, (e.one <m> x) = x)
(mul_one : ∀ x : X, (x <m> e.one) = x)

attribute [simp] is_unital.one_mul is_unital.mul_one

variables {X} {m₁ : has_mul X} {e₁ : has_one X} {m₂ : has_mul X} {e₂ : has_one X}
variables (h₁ : @is_unital X m₁ e₁) (h₂ : @is_unital X m₂ e₂)
variables (distrib : ∀ a b c d, ((a <m₂> b) <m₁> (c <m₂> d)) = ((a <m₁> c) <m₂> (b <m₁> d)))
include h₁ h₂ distrib

lemma one : (e₁.one = e₂.one) :=
by simpa using distrib e₂.one e₁.one e₁.one e₂.one

lemma mul : (m₁.mul = m₂.mul) :=
by funext a b; have := distrib a e₁.one e₁.one b;
simp at this; simpa [one h₁ h₂ distrib] using this

lemma mul_comm : is_commutative _ m₂.mul :=
⟨λ a b, by simpa [mul h₁ h₂ distrib] using distrib e₂.one a b e₂.one⟩

lemma mul_assoc : is_associative _ m₂.mul :=
⟨λ a b c, by simpa [mul h₁ h₂ distrib] using distrib a b e₂.one c⟩

instance : comm_monoid X :=
{ mul_comm := (mul_comm h₁ h₂ distrib).comm,
  mul_assoc := (mul_assoc h₁ h₂ distrib).assoc,
  ..m₂, ..e₂, ..h₂ }

end eckmann_hilton
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498562):
Well done!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498636):
@**Kenny Lau** https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf
I added your name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498642):
lol


{% endraw %}
