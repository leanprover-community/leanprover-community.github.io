---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86653printexprinplaintext.html
---

## Stream: [general](index.html)
### Topic: [print `expr` in plaintext](86653printexprinplaintext.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012147):
How to print an `expr` in a plaintext way? That is, represented as all constructors `app` `lam` `var`, etc..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012314):
Maybe I should provide a context: I'm parsing a `expr` which (in pretty print) read like \forall (a b : bool), (b -> a). But somehow I encouter `var 2` at `b` 's position, which is not possible because there should be only `0`(refering to `b`) and `1`(refering to `a`).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 12 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012324):
use `e.to_raw_fmt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012325):
it's actually `      ∀ (a b : bool), ↥b → ↥a`, to be precise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 12 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012338):
Did you use `expr.lambdas` or `expr.pis`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012398):
thank you, I got this: 
```
(pi a default (const bool []) (pi b default (const bool []) (pi a default (app (app (app (const coe_sort [1,
         1]) (const bool [])) (const coe_sort_bool [])) (var 0)) (app (app (app (const coe_sort [1,
         1]) (const bool [])) (const coe_sort_bool [])) (var 2)))))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 12 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012450):
`pis` and `lambdas` have a known bug which behaves like you showed and there's a fix in mathlib, in `meta.expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012460):
Oh, no, that's not what I thought

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012463):
I think I didn't use expr.lambdas/pis explicitly. I just wrote the formula in this form.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012467):
You don't have only two bound variables, you have three because implication is also a pi-type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012512):
Gee.. rookie mistake...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012515):
I recommend you don't manipulate `var` directly, there's a better interface for it. What do you need with them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012516):
I need to parse a user-provided formula to generate a query to SMT solvers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012523):
these formulas are mostly like the one I said above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 12 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012524):
So first I need extract declarations, (a, b : bool), then the assertions (a -> b), or something more complex.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012721):
I see. So you're trying to use constants in your smt formulas rather than use quantifiers. What you can do is strip one quantifier at a time like this:

```lean
meta def unbind_vars : expr -> tactic (list expr × expr)
| e :=
do (expr.pi n bi d b) ← return e | return ([],e),
   v ← mk_local' n bi d,
   let b' := b.instantiate_var v,
   (vs,b'') ← unbind_vars b',
   return (v :: vs, b'')
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012763):
The only thing you do with `var` in this code is use `intantiate_var`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 13 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012813):
this is so much better than mine. Right now I have to keep track of the variable stack myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012925):
The more you know ... :shooting_star:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 13 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012975):
..the more I have to worry about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Aug 13 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012978):
:grinning:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132013027):
I'm hoping not in this case :laughing:


{% endraw %}
