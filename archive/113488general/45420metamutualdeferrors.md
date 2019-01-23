---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45420metamutualdeferrors.html
---

## Stream: [general](index.html)
### Topic: [meta mutual def errors](45420metamutualdeferrors.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 24 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697613):
Does anyone know the source of this error? I get `unexpected error, failed to generate equational lemmas in the front-end` even though it's a meta def so it shouldn't have equations
```lean
meta mutual def A, B
with A : unit → tactic unit | _ := return ()
with B : unit → tactic unit | _ := return ()
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697723):
(Mario and I are sitting next to each other and just discovered the curious answer. I'll explain while he does something useful. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697746):
This doesn't work:
```
meta mutual def A, B
with A : ℕ → ℕ  
| n := 0
with B : ℕ → ℕ  
| n := 0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697747):
with the same error.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697787):
However
```
meta mutual def A, B
with A : ℕ → ℕ  
| 0 := 0
| (n+1) := B 0
with B : ℕ → ℕ  
| n := 0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697792):
or even 
```
meta mutual def A, B
with A : ℕ → ℕ  
| 0 := 0
| (n+1) := A 0
with B : ℕ → ℕ  
| n := 0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697840):
Somehow the compiler is insisting that the definitions actually refer to either themselves or each other.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697844):
And this only happens in `meta`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697846):
Oh well! :-)


{% endraw %}
