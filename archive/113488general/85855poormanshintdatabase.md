---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85855poormanshintdatabase.html
---

## Stream: [general](index.html)
### Topic: [poor man's hint database](85855poormanshintdatabase.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Nov 19 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951801):
Is there a way to simulate Coq's hint database? For example, I often find myself writing `simp [x₁, x₂, x₃, x₄]`, which I would like to replace with `simp [x_lemmas]` where `x_lemmas` is a sort of a "hint database" for lack of better term. (Do note that I don't want to designate `xₙ` to be simp lemmas.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951920):
there are simp sets, but we don't use them very often

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951926):
you can write `simp with x_lemmas`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Nov 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951950):
Where `x_lemmas` is a "simp set"? Would it be weird for you to encounter that somewhere in Lean code - is that something to avoid?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951992):
The "default" simp set is not necessarily a superset of other simp sets, so it should be fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951997):
It would be unusual, but not unheard of

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147952001):
good enough, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147952005):
It forms part of the public interface, so I don't use it for one off things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953651):
```quote
The "default" simp set is not necessarily a superset of other simp sets, so it should be fine
```

No. We have demonstrated more than once that using a simp set speeds things up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953658):
I don’t know why you don’t like it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953898):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953956):
what does that have to do with my quote

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147954062):
well that means the default simp set is much bigger

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147954155):
I said it is *not* a superset

