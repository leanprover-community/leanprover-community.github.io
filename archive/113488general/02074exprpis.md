---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02074exprpis.html
---

## [general](index.html)
### [expr.pis](02074exprpis.html)

#### [Jakob von Raumer (Mar 14 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123711391):
Why doesn't ``#reduce expr.pis [expr.local_const  ` A `A binder_info.default `(Sort 1)] `(Sort 1)``terminate?

#### [Kevin Buzzard (Mar 14 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123711636):
In an ideal world you would go to the set_option docs and look at the section "how do I track down an excessive memory consumption error?"

#### [Gabriel Ebner (Mar 14 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123711953):
@**Jakob von Raumer** You should use `#eval` since `expr.pis` is meta.

#### [Gabriel Ebner (Mar 14 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712203):
And I think the following should explain why kernel reduction fails on this example:
```lean
set_option pp.all true
#print raw `A
/-
name.mk_string
  (string.str string.empty
     (char.of_nat
        (@bit1.{0} nat nat.has_one nat.has_add
           (@bit0.{0} nat nat.has_add
              (@bit0.{0} nat nat.has_add
                 (@bit0.{0} nat nat.has_add
                    (@bit0.{0} nat nat.has_add (@bit0.{0} nat nat.has_add (@has_one.one.{0} nat nat.has_one)))))))))
  name.anonymous
-/
```

#### [Gabriel Ebner (Mar 14 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712256):
(I just tried all subterms of the example, and already ``#reduce `A`` fails.)

#### [Jakob von Raumer (Mar 14 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712261):
Thanks :)

#### [Jakob von Raumer (Mar 14 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712357):
But for `#eval` I'm getting a "result type does not have an instance of type class 'has_repr', dumping internal representation"?

#### [Gabriel Ebner (Mar 14 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.pis/near/123712411):
```lean
meta instance: has_repr expr := ⟨expr.to_string⟩
```
:smile: I'm not sure if Leo would like a PR though...

