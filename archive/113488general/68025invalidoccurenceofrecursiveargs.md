---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68025invalidoccurenceofrecursiveargs.html
---

## Stream: [general](index.html)
### Topic: [invalid occurence of recursive args](68025invalidoccurenceofrecursiveargs.html)

---


{% raw %}
#### [ Zesen Qian (Jun 20 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128381305):
<p>Not sure if it's a place for routine trouble shooting, but I'm trying to do some theory inside lean, I defined a inductive family but lean is not happy with it. <a href="https://ptpb.pw/3O0a" target="_blank" title="https://ptpb.pw/3O0a">https://ptpb.pw/3O0a</a><br>
The error is at the constructor satlem, "invalid occurence of recursive arg#5, the body of the functional type depends on it".</p>

#### [ Mario Carneiro (Jun 20 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128381813):
<p>I don't think lean likes that you have placed the recursive argument before the variable <code>v</code></p>

#### [ Mario Carneiro (Jun 20 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128381941):
<p>you had:</p>
<div class="codehilite"><pre><span></span>| satlem (c : context) (cl cl&#39; : clause) :
  proof c (type.holds cl) →
  ∀ v : string, proof ((v, type.holds cl) :: c) (type.holds cl&#39;) →
  proof c (type.holds cl&#39;)
</pre></div>


<p>This works:</p>
<div class="codehilite"><pre><span></span>| satlem (c : context) (cl cl&#39; : clause) :
  ∀ v : string, proof c (type.holds cl) →
  proof ((v, type.holds cl) :: c) (type.holds cl&#39;) →
  proof c (type.holds cl&#39;)
</pre></div>


<p>Or maybe you got the parentheses wrong? This works too, but means something different:</p>
<div class="codehilite"><pre><span></span>| satlem (c : context) (cl cl&#39; : clause) :
  proof c (type.holds cl) →
  (∀ v : string, proof ((v, type.holds cl) :: c) (type.holds cl&#39;)) →
  proof c (type.holds cl&#39;)
</pre></div>

#### [ Zesen Qian (Jun 20 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128382752):
<p>Thanks! this works. I also fixed similar issues in the code.<br>
question tho: why is this required? intuitively I don't see how it's invalid.</p>

#### [ Mario Carneiro (Jun 20 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128383088):
<p>There was a restriction along the lines that recursive arguments must come after non-recursive args, mostly for convenience of implementation, but last I checked that restriction had been lifted, so I'm not sure why you are getting the error still</p>

#### [ Zesen Qian (Jun 20 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128383377):
<p>maybe because it's inductive family, so impl. could be harder.</p>

#### [ Gabriel Ebner (Jun 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128403732):
<p>There is still a restriction on <em>dependent</em> arguments, none of the arguments after the first recursive argument may occur in other arguments.  In this case <code>v</code> comes after the first recursive argument and occurs in the second recursive argument.</p>


{% endraw %}
