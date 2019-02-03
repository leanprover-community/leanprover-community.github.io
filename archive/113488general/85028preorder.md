---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85028preorder.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [preorder](https://leanprover-community.github.io/archive/113488general/85028preorder.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 03 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133250860):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">preorder</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">has_le</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_lt</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">le_refl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">le_trans</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt_iff_le_not_le</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="bp">.</span> <span class="n">order_laws_tac</span><span class="o">)</span>
</pre></div>


<p>I just want to check I've got this right. The <code>lt</code> field does not even seem to document its type, but given that we have an example of how to fill it in, we can infer the type. The <code>lt_iff_le_not_le</code> field demands that <code>lt a b</code> is logically equivalent to <code>(a ≤ b ∧ ¬ b ≤ a)</code>, so from a mathematician's point of view it may as well be defined to be <code>λ a b, a ≤ b ∧ ¬ b ≤ a</code>. However from a computer scientist's point of view they might want some other algorithm for computing <code>&lt;</code> and then a theorem saying it's equivalent. The <code>order_laws_tac</code> thing -- this is some tactic, which presumably is a beefed-up version of <code>exact iff.refl</code>. Mathematicians could hence simply completely ignore the last two fields when getting a feel as to what a preorder is (I am more used to partial orders). A preorder is just a category whose objects are terms of alpha and for which there is at most one morphism between any two objects; it's weaker than a partial order because there can be objects which are isomorphic but not equal. A Galois connection is no more and no less than a pair of adjoint functors between two such categories. Have I got all this straight?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252175):
<p>Why are the maps called <code>l</code> and <code>u</code> in the Galois connection stuff? <code>l</code> and <code>r</code> I would understand...</p>

#### [ Kevin Buzzard (Sep 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252362):
<p>What does <code>notation </code>⨆<code> binders </code>, <code> r:(scoped f, supr f) := r</code> mean?</p>

#### [ Johan Commelin (Sep 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252436):
<p>I think it was <code>l</code>ower and <code>u</code>pper?</p>

#### [ Johan Commelin (Sep 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252453):
<p>But also <code>l</code>eft and <code>u</code>nderlying...</p>

#### [ Johannes Hölzl (Sep 03 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252862):
<p>Yes <code>l</code> for lower, and <code>u</code> for upper. But left and underlying is also nice<br>
I don't understand the <code>notation</code>-syntax myself. This specific case sets up <code>⨆</code> to behave like a lambda, and put a <code>supr</code> around it.<br>
I.e. <code>(⨆a, f a) := supr (λa, f a)</code></p>

#### [ Johannes Hölzl (Sep 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252917):
<p>That we want to overwrite <code>&lt;</code> is not necessary due to more efficient computation, but sometimes also easier proofs. For example for nat it is defined to be <code>a &lt; b := nat.succ a &lt;= b</code></p>

#### [ Reid Barton (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133254462):
<p>Kevin what you say is right. Also worth noting is that every preorder has a canonical equivalence (in the category theory sense) to a poset, so there's not much harm in treating posets and preorders as the same thing.</p>


{% endraw %}
