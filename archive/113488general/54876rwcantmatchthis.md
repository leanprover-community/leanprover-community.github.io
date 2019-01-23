---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54876rwcantmatchthis.html
---

## Stream: [general](index.html)
### Topic: [rw can't match this](54876rwcantmatchthis.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765206):
```
@has_mem.mem.{u u} α α
    (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_comprehension.to_has_zmem.{u} α has_comprehension))
    ?m_1
    (@zfc.comprehension.{u} α has_comprehension ?m_2 ?m_3)
```
```
@has_mem.mem.{u u} α α (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_zmem.mk.{u} α to_has_mem)) x
    (@zfc.comprehension.{u} α has_comprehension infinity (λ (x : α), false))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765219):
hmm, the situation is quite complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765285):
Question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765301):
I've filled in more holes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765305):
now `rw` can't match this:
```
@has_mem.mem.{u u} α α
    (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_comprehension.to_has_zmem.{u} α has_comprehension))
    x
    (@zfc.comprehension.{u} α has_comprehension infinity (λ (x : α), false))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765307):
where the goal contains:
```
@has_mem.mem.{u u} α α (@zfc.has_zmem.to_has_mem.{u} α (@zfc.has_zmem.mk.{u} α to_has_mem)) x
    (@zfc.comprehension.{u} α has_comprehension infinity (λ (x : α), false))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765363):
If I'm analyzing correctly, it would be a failure to match this with this:
```
@zfc.has_comprehension.to_has_zmem.{u} α has_comprehension
```
```
@zfc.has_zmem.mk.{u} α to_has_mem
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765368):
@**Simon Hudon** question: do you see any way to fix it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765379):
What are you trying to do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765444):
rewrite `hx : x ∈ comprehension infinity (λ (x : α), false)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765470):
What is the rule that you're using?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765517):
```
∀ A p x, x ∈ comprehension A p ↔ x ∈ A ∧ p x
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765631):
Why do you have `(@zfc.has_zmem.mk.{u} α to_has_mem)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765654):
And where does `to_has_mem` come from?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765655):
I'm in the middle of a structure doing things like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765659):
```
(has_zempty : has_zempty α :=
  { emptyc := @@comprehension has_comprehension infinity (λ x, false),
    empty_not_zmem := λ x hx, begin simp [∅] at hx, rw [@@zmem_comprehension_iff has_comprehension infinity (λ (x : α), false) x] at hx, end })
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765723):
```
class has_zmem extends has_mem α α

class has_zempty extends has_zmem α, has_emptyc α :=
(empty_not_zmem : ∀ x, x ∉ (∅:α))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765725):
Try extracting 

```lean
{ emptyc := @@comprehension has_comprehension infinity (λ x, false),
    empty_not_zmem := λ x hx, begin simp [∅] at hx, rw [@@zmem_comprehension_iff has_comprehension infinity (λ (x : α), false) x] at hx, end })
```

into a separate definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20can%27t%20match%20this/near/123765947):
thanks

