---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05477usinginfixindefinition.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [using infix in definition](https://leanprover-community.github.io/archive/113488general/05477usinginfixindefinition.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Minchao Wu (Mar 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004353):
<p>I remember that in Lean 2 we could use <code>infix</code> inside a definition, referring  to the thing being defined.<br>
Is this implemented in the latest master branch?</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004476):
<p>I don't think there is anything like that</p>

#### [ Sebastian Ullrich (Mar 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004526):
<div class="codehilite"><pre><span></span>inductive sub : env → type → type → Prop
  notation e ` ⊢ `:40 a ` &lt;: `:40 b:40 := sub e a b
| ...
</pre></div>

#### [ Sebastian Ullrich (Mar 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004527):
<p>The only change is the removal of <code>:=</code> after the type</p>

#### [ Minchao Wu (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004632):
<p>Worked for me! Thanks Sebastian and Mario.</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004639):
<p>Wait, does that work for <code>def</code> as well? I thought it only worked in <code>inductive</code> and <code>structure</code></p>

#### [ Minchao Wu (Mar 21 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004662):
<p>My bad, I should have said <code>inductive</code> definitions</p>


{% endraw %}
