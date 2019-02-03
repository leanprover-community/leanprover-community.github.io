---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32934Prooftermsize2200.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Proof term size * 2^200](https://leanprover-community.github.io/archive/113488general/32934Prooftermsize2200.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Jan 10 2019 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20term%20size%20%2A%202%5E200/near/154864164):
<p>I became curious how sizes of proof terms affect speed, so I ran a quick experiment: </p>
<div class="codehilite"><pre><span></span>def foo : nat → Prop
| 0 := true
| (n+1) := (foo n) ∧ (foo n)

meta def mk_foo_expr : nat → expr
| 0 := `(trivial)
| (n+1) :=
  expr.app
    (expr.app
      (reflected.to_expr `(@and.intro (foo n) (foo n)))
      (mk_foo_expr n))
    (mk_foo_expr n)

open tactic

meta def show_foo : tactic unit :=
do `(foo %%nx) ← target,
   n ← eval_expr nat nx,
   exact (mk_foo_expr n)

set_option profiler true

lemma foo_200 : foo 200 :=
by show_foo

#print foo_200
</pre></div>


<p>To my surprise Lean handles it with ease, in roughly 50ms. I don' t think Lean is constructing and checking a gigantic proof term that has 2^200 occurrences of <code>trivial</code>. What's going on here?</p>

#### [ Gabriel Ebner (Jan 10 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20term%20size%20%2A%202%5E200/near/154868623):
<p>To a certain degree, Lean can handle terms with dag-like sharing (your term is very small when viewed as a dag).  This happens e.g. because type inference and whnf and unifiability are cached, i.e., only evaluated once for every subterm (there are only few subterms).</p>

#### [ Gabriel Ebner (Jan 10 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20term%20size%20%2A%202%5E200/near/154868637):
<p>See also <a href="https://github.com/leanprover/tc/issues/8" target="_blank" title="https://github.com/leanprover/tc/issues/8">https://github.com/leanprover/tc/issues/8</a></p>

#### [ Seul Baek (Jan 10 2019 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20term%20size%20%2A%202%5E200/near/154876865):
<p>I see. Thanks!</p>


{% endraw %}
