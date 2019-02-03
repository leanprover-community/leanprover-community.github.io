---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67120isatypewithparametersinjective.html
---

## Stream: [general](index.html)
### Topic: [is a type with parameters injective?](67120isatypewithparametersinjective.html)

---


{% raw %}
#### [ Scott Buckley (May 02 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/125994740):
<p>forgive me for perhaps not using the correct terminology. what i want to know is similar to below:</p>
<div class="codehilite"><pre><span></span>lemma type_something_injectivity: ∀ {T1 T2:Type} {l1:list T1} {l2:list T2},
  l1 == l2 -&gt;
  T1 = T2
:= begin
  ???
end
</pre></div>


<p>Is the above provable?</p>
<p>More specifically, I have some inductive type <code>vexp: forall (T:Type 0), T -&gt; Type 1</code>, and I want to know that <code>vexp T1 v1 == vexp T2 v2 -&gt; T1 = T2 and v1 == v2</code></p>
<p>does this make sense?</p>

#### [ Mario Carneiro (May 02 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/125998623):
<p>Yes it makes sense to ask this question, and the answer is that it is usually independent in lean and sometimes provably false</p>

#### [ Mario Carneiro (May 02 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/125998731):
<div class="codehilite"><pre><span></span>import logic.function

inductive noninj (T : set Type) : Type
| mk : noninj

example : ¬ (∀ x y, noninj x = noninj y → x = y) :=
function.cantor_injective _
</pre></div>

#### [ Scott Buckley (May 03 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/126023472):
<p>I thought that may be the case, however I couldn't understand why, but your example makes it clear. Thanks very much! :)</p>


{% endraw %}
