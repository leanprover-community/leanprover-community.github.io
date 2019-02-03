---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36268Triangularparentinstances.html
---

## Stream: [general](index.html)
### Topic: [Triangular parent instances](36268Triangularparentinstances.html)

---


{% raw %}
#### [ Nicholas Scheel (Dec 16 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151864665):
<p>Is there any way to work around this error?</p>
<div class="codehilite"><pre><span></span>synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  steppable.to_functor t
inferred
  mergeable.to_functor f
</pre></div>


<p>(I have two classes, <code>steppable</code> and <code>mergeable</code> that both extend <code>functor</code>, and I'm using them both as assumptions for some generic code I am writing)</p>

#### [ Chris Hughes (Dec 16 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151864720):
<p>I think you more or less have to create a new class <code>steppable_and_mergeable</code>. I don't think there's another way.</p>

#### [ Nicholas Scheel (Dec 16 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151864731):
<p>Okay, that's what I figured ...</p>

#### [ Chris Hughes (Dec 16 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151864777):
<p>There is actually another way. Change the definition of <code>mergeable</code> and <code>steppable</code> to take <code>[functor]</code> as an argument instead of extending <code>functor</code></p>

#### [ Nicholas Scheel (Dec 16 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151864894):
<p>I see; that could work, but it seems it doesn't play nicely with <code>out_param</code> then</p>

#### [ Chris Hughes (Dec 16 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151864940):
<p>I know nothing about <code>out_param</code></p>

#### [ Simon Hudon (Dec 16 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151888684):
<p>What's your worry about out_param?</p>

#### [ Nicholas Scheel (Dec 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151888986):
<p>Oh hm. I was getting this error, but also marking the instance as <code>out_param</code> seemed to fix it:</p>
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
t : Type u,
f : Type u → Type u,
_inst_1 : mergeable f,
_inst_2 : steppable t f,
_inst_3 : traversable f,
_inst_4 : is_lawful_functor f,
_inst_5 : is_lawful_traversable f,
a b : t
⊢ Type u → Type u
</pre></div>


<p>(i.e. it looked like it was failing to figure out what <code>f</code> was even though I gave it <code>t</code>)<br>
<code>steppable</code> now looks like:</p>
<div class="codehilite"><pre><span></span>class steppable (t : Type u) (f : out_param $ Type u → Type u) [out_param $ functor f] :=
(step : t ≃ f t)
</pre></div>

#### [ Sebastian Ullrich (Dec 16 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Triangular%20parent%20instances/near/151892913):
<p>There shouldn't be any need for that instance param if it's not used in the class body</p>


{% endraw %}
