---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69770rewriteentire.html
---

## Stream: [general](index.html)
### Topic: [rewrite entire](69770rewriteentire.html)

---


{% raw %}
#### [ Scott Morrison (Mar 14 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679200):
Hi all, this is a follow-up to my difficulties with the `occs` configuration for `rw`. I'm still not there writing a "please find _all_ the possible rewrites" function.

Something that would be really helpful for me would be a "rewrite entire" function, that takes `r:expr` and `e:expr`, where `r` is some rewrite rule, and tells me whether it can rewrite the entirety of `e` using it (that is, not rewriting a subexpression).

#### [ Scott Morrison (Mar 14 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679208):
I'm pretty confident I can implement that myself, but I think it may exist already, or be even easier than I'm anticipating, so I thought I'd ask here.

#### [ Simon Hudon (Mar 14 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679467):
I haven't seen it anywhere

#### [ Simon Hudon (Mar 14 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679514):
To be clear, `r` may be `forall x y z, E = F` and that tactic would unify E with the parameter `e`. Is that accurate?

#### [ Scott Morrison (Mar 14 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679591):
Yes, that's exactly what I want.

#### [ Scott Morrison (Mar 14 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679595):
Ok, I can do it myself easily enough.

#### [ Mario Carneiro (Mar 14 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679602):
I think `simp_lemmas` will do that

#### [ Scott Morrison (Mar 14 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679758):
@**Mario Carneiro**, the documentation for `simp_lemmas` talks about simplification lemmas. Can I ignore that and
 attempt to use it with arbitrary rewrite rules? And it won't attempt to look in subexpressions, just rewrite the entire thing?

#### [ Scott Morrison (Mar 14 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679823):
I guess I can read the implementation of `simp_lemmas.rewrite` myself... :-)

#### [ Mario Carneiro (Mar 14 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679869):
Pretty sure it doesn't look in subexpressions, since it is intended for use with `ext_simplify_core` which does the subexpression traversal itself

#### [ Scott Morrison (Mar 14 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679871):
Ah, I see.

#### [ Scott Morrison (Mar 14 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679881):
okay, I will give that a go.

#### [ Scott Morrison (Mar 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123698442):
Do we have an analogue of `mk_eq_symm` that traverses through binders?

#### [ Scott Morrison (Mar 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123698486):
e.g. turning the `expr` `λ a : A, λ b : B, f a b = g a b` into `λ a : A, λ b : B, g a b = f a b`?

#### [ Scott Morrison (Mar 14 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123698913):
[expr.lean](https://github.com/leanprover/lean/blob/master/library/init/meta/expr.lean) is spectacularly unhelpful about the arguments of `expr.elet`. One can glean from it that the four `expr` arguments of `elet` ought to be called `n`, `g`, `e`, `f`, in that order, but not much more. Is there somewhere these things are written down?

#### [ Scott Morrison (Mar 14 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123699122):
Oh... I was asking for the wrong thing, and I don't think I know how to do it. Suppose I have an `expr` which is just the name of a equation lemma; how can I get the `eq.symm` version of that lemma?

#### [ Scott Morrison (Mar 14 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123699509):
I'm guessing I need to ... `infer` the type of my expression, and then while the type is Pi, replace the expression with a lambda wrapped around it, and then when there are no more Pis use `mk_eq_symm`?


{% endraw %}
