---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83984funextxrfl.html
---

## Stream: [general](index.html)
### Topic: [funext $ λ x, rfl](83984funextxrfl.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521378):
conjecture: everything that can be proven using `funext $ λ x, rfl` can be proven using `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521441):
that's correct (modulo funny business regarding algorithmic equality not really being definitional equality)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521443):
could you expand on your parentheses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521482):
Sometimes lean doesn't know when to eta expand stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521492):
could you provide an example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521603):
```
def foo : true = true → plift true := @eq.rec Prop true (λ p, plift true) ⟨trivial⟩ true
def bar : true = true → plift true := @eq.rec Prop true (λ p, plift p) ⟨trivial⟩ true
example : foo = bar := funext $ λ x, rfl
example : foo = bar := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521611):
ah, that funny `rec` business

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521612):
Mario, aren't you sleeping?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521613):
LOL

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523564):
I found myself writing this yesterday:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523566):
```
Hid :=  λ U OU,funext (λ x,subtype.eq rfl),
Hcomp :=  λ U V W OU OV OW HUV HVW,funext (λ x, subtype.eq rfl)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523568):
and I couldn't move the rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523572):
`subtype.eq rfl` cannot be replaced by `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523573):
and I could understand why `subtype.eq` wasn't a simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523579):
well it's just `congr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523580):
because it's ` a1.val = a2.val → a1 = a2 `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523581):
which doesn't look great for simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523582):
but then I found

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523584):
`subtype.mk_eq_mk`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523626):
which is an iff and is marked as a simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523635):
so I was hopeful that `by simp` would work, but I couldn't get it to

