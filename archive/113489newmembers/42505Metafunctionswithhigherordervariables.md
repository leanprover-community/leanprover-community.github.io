---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/42505Metafunctionswithhigherordervariables.html
---

## Stream: [new members](index.html)
### Topic: [Meta functions with higher order variables](42505Metafunctionswithhigherordervariables.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 29 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Meta%20functions%20with%20higher%20order%20variables/near/130493380):
How can I get the following to parse:
```lean
meta def test : expr → expr
| `(λ s, %%f s) := `(λ s, %%f (s+1))
| x := x.
```
Currently, I'm getting the error:
```lean
function expected at
  _x_1
term has type
  ?m_1
```
on the first %%f.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 29 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Meta%20functions%20with%20higher%20order%20variables/near/130503396):
You should use an explicit type annotation `(%%f : ...) s`. Though if you don't statically know the type, you shouldn't use expr quotations.

