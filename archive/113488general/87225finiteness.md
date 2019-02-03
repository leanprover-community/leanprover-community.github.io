---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87225finiteness.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [finiteness](https://leanprover-community.github.io/archive/113488general/87225finiteness.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 04 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610398):
<p>Do mathlib have something that behaves like:</p>
<div class="codehilite"><pre><span></span>class  Finite (α : Type u) :=
  (cardinality : nat)
  (bijection : trunc (equiv α (fin cardinality)))
</pre></div>

#### [ Scott Morrison (Apr 04 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610440):
<p>Is this gross for some reason, and should be avoided?</p>

#### [ Kenny Lau (Apr 04 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610449):
<p>It is in my category theory repo (the category “set”)</p>

#### [ Kenny Lau (Apr 04 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610450):
<p>and it’s called fintype</p>

#### [ Scott Morrison (Apr 04 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610479):
<p>It can't be called fintype, because mathlib already has a fintype which is slightly different (but equivalent, of course).</p>

#### [ Scott Morrison (Apr 04 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610492):
<p>I guess I'm asking if there is a strong reason to (bite the bullet and learn how to use multisets and) use mathlib's fintype, or if it's okay to use something like this.</p>

#### [ Kenny Lau (Apr 04 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610554):
<p>oops i meant the category is called set and uses fintype</p>

#### [ Kenny Lau (Apr 04 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610595):
<p>but I guess I didn’t notice that you used trunc</p>

#### [ Mario Carneiro (Apr 04 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610881):
<p>That's <code>fintype</code>. If you want to use such an interface to it, prove it and use it</p>

#### [ Scott Morrison (Apr 04 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610925):
<p>Okay, I  guess that's a good point. In the meantime I'm discovering <code>fintype</code> is pretty easy to use anyway.</p>

#### [ Scott Morrison (Apr 04 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611257):
<p>What is the lemma that says <code>fintype</code> gives <code>decidable_eq</code>?</p>

#### [ Mario Carneiro (Apr 04 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611576):
<p>I don't think it's true. So your formulation is a bit stronger, since it equips the set with a function to <code>fin</code>; in mathlib's <code>fintype</code>, this function is <code>index_of</code>, but it requires a separate proof of <code>decidable_eq</code></p>

#### [ Mario Carneiro (Apr 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611584):
<p>your <code>Finite</code> should be equivalent to the conjunction of <code>fintype</code> and <code>decidable_eq</code></p>

#### [ Scott Morrison (Apr 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611585):
<p>ah, okay.</p>


{% endraw %}
