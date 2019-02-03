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
<p>Hi all, this is a follow-up to my difficulties with the <code>occs</code> configuration for <code>rw</code>. I'm still not there writing a "please find _all_ the possible rewrites" function.</p>
<p>Something that would be really helpful for me would be a "rewrite entire" function, that takes <code>r:expr</code> and <code>e:expr</code>, where <code>r</code> is some rewrite rule, and tells me whether it can rewrite the entirety of <code>e</code> using it (that is, not rewriting a subexpression).</p>

#### [ Scott Morrison (Mar 14 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679208):
<p>I'm pretty confident I can implement that myself, but I think it may exist already, or be even easier than I'm anticipating, so I thought I'd ask here.</p>

#### [ Simon Hudon (Mar 14 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679467):
<p>I haven't seen it anywhere</p>

#### [ Simon Hudon (Mar 14 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679514):
<p>To be clear, <code>r</code> may be <code>forall x y z, E = F</code> and that tactic would unify E with the parameter <code>e</code>. Is that accurate?</p>

#### [ Scott Morrison (Mar 14 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679591):
<p>Yes, that's exactly what I want.</p>

#### [ Scott Morrison (Mar 14 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679595):
<p>Ok, I can do it myself easily enough.</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679602):
<p>I think <code>simp_lemmas</code> will do that</p>

#### [ Scott Morrison (Mar 14 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679758):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, the documentation for <code>simp_lemmas</code> talks about simplification lemmas. Can I ignore that and<br>
 attempt to use it with arbitrary rewrite rules? And it won't attempt to look in subexpressions, just rewrite the entire thing?</p>

#### [ Scott Morrison (Mar 14 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679823):
<p>I guess I can read the implementation of <code>simp_lemmas.rewrite</code> myself... :-)</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679869):
<p>Pretty sure it doesn't look in subexpressions, since it is intended for use with <code>ext_simplify_core</code> which does the subexpression traversal itself</p>

#### [ Scott Morrison (Mar 14 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679871):
<p>Ah, I see.</p>

#### [ Scott Morrison (Mar 14 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123679881):
<p>okay, I will give that a go.</p>

#### [ Scott Morrison (Mar 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123698442):
<p>Do we have an analogue of <code>mk_eq_symm</code> that traverses through binders?</p>

#### [ Scott Morrison (Mar 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123698486):
<p>e.g. turning the <code>expr</code> <code>λ a : A, λ b : B, f a b = g a b</code> into <code>λ a : A, λ b : B, g a b = f a b</code>?</p>

#### [ Scott Morrison (Mar 14 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123698913):
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/meta/expr.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/expr.lean">expr.lean</a> is spectacularly unhelpful about the arguments of <code>expr.elet</code>. One can glean from it that the four <code>expr</code> arguments of <code>elet</code> ought to be called <code>n</code>, <code>g</code>, <code>e</code>, <code>f</code>, in that order, but not much more. Is there somewhere these things are written down?</p>

#### [ Scott Morrison (Mar 14 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123699122):
<p>Oh... I was asking for the wrong thing, and I don't think I know how to do it. Suppose I have an <code>expr</code> which is just the name of a equation lemma; how can I get the <code>eq.symm</code> version of that lemma?</p>

#### [ Scott Morrison (Mar 14 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20entire/near/123699509):
<p>I'm guessing I need to ... <code>infer</code> the type of my expression, and then while the type is Pi, replace the expression with a lambda wrapped around it, and then when there are no more Pis use <code>mk_eq_symm</code>?</p>


{% endraw %}
