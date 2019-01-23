---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94825custominduction.html
---

## Stream: [general](index.html)
### Topic: [custom induction](94825custominduction.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133786062):
Can we tag our induction lemmas and have the tactic `induction` recognize it? Maybe create a new tactic `induction'`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 12 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133786384):
You can do `induction using`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133787915):
@**Chris Hughes** I can't work it out for polynomials

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 12 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133788643):
```lean
example (p : polynomial ℤ) : 1 = 2 :=
begin
  induction p using polynomial.induction_on,
end

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133788749):
can you put p in the result?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 12 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133788807):
```lean
example (p : polynomial ℤ) : p = 2 :=
begin
  induction p using polynomial.induction_on,
end

```

