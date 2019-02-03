---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56592strictification.html
---

## Stream: [maths](index.html)
### Topic: [strictification](56592strictification.html)

---


{% raw %}
#### [ Reid Barton (May 26 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137722):
<p>If <code>α</code> is a type, then as <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> describes near <a href="#narrow/stream/116395-maths/subject/affine.20schemes.20are.20schemes/near/126963972" title="#narrow/stream/116395-maths/subject/affine.20schemes.20are.20schemes/near/126963972">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/affine.20schemes.20are.20schemes/near/126963972</a>, we can interpret <code>α</code> as a groupoid whose objects are the "inhabitants of α up to defeq" and whose morphisms are propositional equalities, that is, the morphisms from <code>a</code> to <code>b</code> are the inhabitants of <code>a = b</code> (and so a morphism from <code>a</code> to <code>b</code> is unique if it exists, by proof irrelevance).<br>
Suppose now <code>α</code> is a <code>monoid</code>. Then associativity is a propositional equality <code>(a * b) * c = a * (b * c)</code> and not necessarily a defeq, so under this interpretation <code>α</code> corresponds to a monoidal groupoid which is not necessarily strict.</p>

#### [ Reid Barton (May 26 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137817):
<p>But we can replace <code>α</code> with a strict monoidal groupoid using standard strictification results. Here, for example, <code>α</code> acts on itself by left multiplication, and then <code>α</code> is isomorphic to the image of this action in the endomorphism monoid <code>α → α</code>, which is strictly associative and unital.</p>

#### [ Reid Barton (May 26 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137818):
<p>For the monoid <code>list t</code>, this is basically the "difference list" construction</p>

#### [ Reid Barton (May 26 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137825):
<p>More generally, any <code>category</code> is isomorphic to a <code>category</code> whose composition is strictly associative and unital.</p>

#### [ Reid Barton (May 26 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127138069):
<p>I wonder how useful this observation is. I encountered it in a situation similar to the following. Consider a type indexed on a monoid, like <code>def vector (α : Type u) (n : ℕ) := { l : list α // l.length = n }</code>. Then <code>append</code> is an operation <code>{n m : nat} : vector α n → vector α m → vector α (n + m)</code>. In order to state associativity of <code>append</code>, we need to use transport across the equality <code>(n + m) + k = n + (m + k)</code>, or use heterogeneous equality.<br>
If we replaced <code>ℕ</code> with a "strictly associative" version, we wouldn't need to do this.</p>

#### [ Reid Barton (May 26 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127138073):
<p>I haven't yet tried putting this plan into practice, though.</p>

#### [ Reid Barton (May 26 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127139315):
<p>Actually, this is kind of funny. This construction gives you a monoid which is strictly associative, but not strictly unital.</p>

#### [ Reid Barton (May 26 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127139698):
<p><a href="https://gist.github.com/rwbarton/658ccdd57986b32fd8be0c155c63d47e#file-strictification-lean-L21" target="_blank" title="https://gist.github.com/rwbarton/658ccdd57986b32fd8be0c155c63d47e#file-strictification-lean-L21">https://gist.github.com/rwbarton/658ccdd57986b32fd8be0c155c63d47e#file-strictification-lean-L21</a></p>

#### [ Reid Barton (May 26 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127139758):
<p>Now as soon as I write this I realize I actually need the additive version, hah.</p>


{% endraw %}
