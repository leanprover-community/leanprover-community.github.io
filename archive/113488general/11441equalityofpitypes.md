---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11441equalityofpitypes.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [equality of pi types?](https://leanprover-community.github.io/archive/113488general/11441equalityofpitypes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Buckley (Apr 26 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125702762):
<p>Hi guys, I'm stuck trying to prove the following, which seems intuitively true to me:</p>
<div class="codehilite"><pre><span></span>((T1 -&gt; T2) = (T1 -&gt; T2&#39;)) -&gt;
T2 = T2&#39;
</pre></div>


<p>If it helps, I have instances of T1, (T1 -&gt; T2), and (T1 -&gt; T2'). <code>cases</code> on the equality hypotheses doesn't get me anywhere. I've tried building proofs various ways, but I always come back to the fundamental problem.</p>
<p>Is this even true?</p>
<p>Cheers,<br>
Scott.<br>
EDIT: fixed parameterisation</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703075):
<p>Could you post a complete statement of the claim? In particular I want to know what are the types of <code>T1</code>, <code>T2</code>, and <code>T2'</code></p>

#### [ Mario Carneiro (Apr 26 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703125):
<p>If <code>T2</code> and <code>T2'</code> are propositions, then this follows purely from the ancillary instances you have; from <code>T1</code> and <code>T1 -&gt; T2</code> we find that <code>T2</code> is true, and similarly <code>T2'</code> is true, so they are equal by <code>propext</code></p>

#### [ Mario Carneiro (Apr 26 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703310):
<p>Oh, I just realized that you are misinterpreting the binding power of equality over arrow - I think you wanted to say</p>
<div class="codehilite"><pre><span></span>(T1 -&gt; T2) = (T1 -&gt; T2&#39;) -&gt; T2 = T2&#39;
</pre></div>


<p>This claim is known as injectivity of pi, and it is independent in lean's axiomatization. I am pretty sure it's consistent with DTT but for some reason it's never assumed in any interactive proof assistant I know. (Warning: Also seemingly reasonable is injectivity on the left, i.e. <code>(T1 -&gt; T2) = (T1' -&gt; T2) -&gt; T1 = T1'</code>, but this one is false when <code>T2</code> is a proposition.)</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703385):
<p>Oh wait, even injectivity on the right is false when <code>T1</code> is empty and <code>T2</code> and <code>T2'</code> are propositions, i.e. <code>(false -&gt; false) = (false -&gt; true)</code> but <code>false != true</code></p>

#### [ Scott Buckley (Apr 26 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703441):
<p>Thanks Mario. Yeah you're right, I mis-parameterised.<br>
T1, T2, and T2' are Type. All are inhabited.</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703491):
<p>I think I will stick with my original answer then - unprovable in Lean but consistent with it</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703497):
<p>May I ask why you need this?</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703541):
<p>I know it comes up in attempting to prove</p>
<div class="codehilite"><pre><span></span>f == g -&gt; a == b -&gt; f a == g b
</pre></div>


<p>which would be nice if it were provable but you have to assume <code>f = g</code> for it to work.</p>

#### [ Scott Buckley (Apr 26 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125703666):
<p>I'm proving type determinism for my operational semantics. Some expressions contain lean functions. If I have an application, its subexpressions must have function types, so the output of an application must have the same type. That's where this comes in.</p>

#### [ Mario Carneiro (Apr 26 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125704324):
<p>So the types of your functions are calculated dynamically? I think you want to bundle the types as auxiliary data for this kind of thing to work. It's not sufficient to know that they <em>can be</em> well typed, you need to keep track of the type itself so that one pi doesn't get swapped with another that is equal but has different parts (assuming pi is noninjective)</p>

#### [ Scott Buckley (Apr 26 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125704716):
<p>yeah that's a good point. thanks for the advice :)</p>

#### [ Kenny Lau (Apr 26 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125732960):
<blockquote>
<p>I think I will stick with my original answer then - unprovable in Lean but consistent with it</p>
</blockquote>
<p>this is very interesting</p>

#### [ Kenny Lau (Apr 26 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/125732962):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (May 28 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127208536):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is the converse true / provable?</p>

#### [ Kenny Lau (May 28 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127208538):
<p><code>T2 = T2' -&gt; ((T1 -&gt; T2) = (T1 -&gt; T2'))</code></p>

#### [ Chris Hughes (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209021):
<p>Isn't that just <code>rw</code></p>

#### [ Kenny Lau (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209024):
<p>yes</p>

#### [ Kenny Lau (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209029):
<p>what if the right hand side is a pi</p>

#### [ Kenny Lau (May 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127209033):
<p>does pi have an ext theorem?</p>

#### [ Kenny Lau (May 28 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211597):
<div class="codehilite"><pre><span></span><span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">},</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="n">x</span> <span class="bp">==</span> <span class="n">γ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">==</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">γ</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (May 28 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211600):
<p>Is this true/false/independent?</p>

#### [ Johannes Hölzl (May 28 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211882):
<p>You don't need <code>==</code> to state this. The type of <code>β x</code> and <code>γ x</code> are the same. dito on the rhs.</p>

#### [ Johannes Hölzl (May 28 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127211934):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">γ</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">((</span><span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">γ</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">β</span> <span class="bp">=</span> <span class="n">γ</span><span class="o">,</span> <span class="k">from</span> <span class="n">funext</span> <span class="n">h</span><span class="o">,</span>
<span class="k">by</span> <span class="n">subst</span> <span class="n">this</span>
</pre></div>

#### [ Kenny Lau (May 28 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127212180):
<p>hmm</p>

#### [ Mario Carneiro (May 28 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20pi%20types%3F/near/127219583):
<p>The converse is false for some choices of T1, and independent for others</p>


{% endraw %}
