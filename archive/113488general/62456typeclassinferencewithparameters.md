---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62456typeclassinferencewithparameters.html
---

## Stream: [general](index.html)
### Topic: [type class inference with parameters](62456typeclassinferencewithparameters.html)

---


{% raw %}
#### [ Floris van Doorn (Nov 07 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146970992):
<p>Is there a way to tell type class inference to "use the current parameter"? In the following code, the <code>apply_instance</code> fails, because the argument of type <code>decidable_eq A</code> is a metavariable, and I want Lean to use the parameter.</p>
<div class="codehilite"><pre><span></span>section
parameters {A : Type} {h : decidable_eq A}
def X := A ⊕ A
def decidable_eq_X : decidable_eq X := @sum.decidable_eq _ h _ h
local attribute [instance] decidable_eq_X
set_option trace.class_instances true
def foo : decidable_eq X := by apply_instance
end
</pre></div>


<p>(note: it is unacceptable in my actual application to let <code>X</code> depend on <code>h</code>)</p>

#### [ Simon Hudon (Nov 07 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146971329):
<p>What if you use <code>[ ]</code> around the declaration of <code>h</code>?</p>

#### [ Floris van Doorn (Nov 07 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146971982):
<p>That works, but in my actual example <code>h</code> is not a type class parameter, but just some extra data to construct a <code>setoid</code>.</p>

#### [ Simon Hudon (Nov 07 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972041):
<p>You could do something like <code>by haveI := h; apply_instance</code>, replacing <code>h</code> with whatever you need it to be.</p>

#### [ Simon Hudon (Nov 07 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972171):
<p>(you need <code>mathlib</code> for <code>haveI</code> by the way, and to import <code>tactic</code>)</p>

#### [ Floris van Doorn (Nov 07 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972280):
<p>this is a more faithful representation of my actual scenario:</p>
<div class="codehilite"><pre><span></span>constant some_data (α : Type) : Type
definition foo {α : Type} (h : some_data α) : setoid (α ⊕ α) := sorry
section
parameters {α : Type} (h : some_data α)
def X := α ⊕ α
def setoid_X : setoid X := foo h
local attribute [instance] setoid_X
set_option trace.class_instances true
def foo : setoid X := by apply_instance
end
</pre></div>

#### [ Floris van Doorn (Nov 07 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972375):
<p>yes, that works, but is still a little annoying.</p>

#### [ Floris van Doorn (Nov 07 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972463):
<p>I only have a problem with <code>quotient.mk</code>, so currently I just have something like <code>def my_quotient.mk := @quotient.mk _ setoid_X</code>, which is also a little annoying.</p>

#### [ Simon Hudon (Nov 07 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972512):
<p>There's been a couple of back-and-forth on the subject. Leo doesn't like to allow instances to be created on the fly but he still granted us a way to do it.</p>

#### [ Simon Hudon (Nov 07 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972748):
<p>Does it work if you replace <code>@quotient.mk _ setoid_X</code> with <code>by haveI := setoid_X; apply quotient.mk</code>?</p>

#### [ Floris van Doorn (Nov 07 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972896):
<blockquote>
<p>There's been a couple of back-and-forth on the subject. Leo doesn't like to allow instances to be created on the fly but he still granted us a way to do it.</p>
</blockquote>
<p>Yeah, I know, but I don't want to add instances on the fly, I just want that in that section I have an instance of type <code>setoid X</code>.</p>

#### [ Simon Hudon (Nov 07 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146973032):
<p>I see. I mistook your issue. I think the problem is that your instance depend on stuff that can't be inferred. You may have to make <code>some_data</code> a class locally.</p>


{% endraw %}
