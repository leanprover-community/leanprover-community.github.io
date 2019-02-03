---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/63153makinganequiv.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [making an equiv](https://leanprover-community.github.io/archive/116395maths/63153makinganequiv.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ali Sever (Sep 07 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133531588):
<p>I have <code>f : α → α → α → α → α → α → Prop</code> that says <code>a ≠ b ∧ c ≠ b ∧ d ≠ e ∧ f ≠ e ∧ blah</code>. I have shown <code>f</code>is reflexive, symmetric and transitive (i.e. an equiv on α × α × α), but only when <code>a ≠ b ∧ c ≠ b</code>. Now I want to make the equiv classes, I'm having trouble with deciding what to do.<br>
 If I set <code>f</code> to take a random value for <code>a = b</code>, then working with <code>f</code>is going to be annoying. If I make the equiv on <code>α × α × α</code> such that <code>a ≠ b ∧ c ≠ b</code>, then any time I talk about the class <code>a b c</code> I have to give proofs of <code>a ≠ b</code>and <code>c ≠ b</code>. Is there different method? </p>
<p>In GeoCoq they cheat, instead of making an equiv, they make a new function (which is what the book does too),</p>
<div class="codehilite"><pre><span></span><span class="kn">Definition</span> <span class="n">Q_CongA</span> <span class="n">a</span> <span class="o">:=</span>
  <span class="err">∃</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="n">A</span> <span class="err">≠</span> <span class="n">B</span> <span class="err">∧</span> <span class="n">C</span> <span class="err">≠</span> <span class="n">B</span> <span class="err">∧</span> <span class="err">∀</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span><span class="o">,</span> <span class="n">CongA</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="err">↔</span> <span class="n">a</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span><span class="o">.</span>
</pre></div>

#### [ Chris Hughes (Sep 07 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133532250):
<p>You could define the equivalence relation on the subtype. It sounds like you just have to give proofs that <code>a \ne b</code> and stuff. Lean is all about edge cases. Why do you consider the GeoCoq solution cheating? You can define quotients on non-equivalence relations in lean, but it's not recommended.</p>

#### [ Ali Sever (Sep 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133559910):
<p>I want to define a function from an equivalence class, but to give the value I first need an element from the class (but every element gives the same result), how would I do this? i.e. I want to make a function which I know is well-defined</p>

#### [ Reid Barton (Sep 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133560004):
<p>Assuming you're using <code>quot</code>/<code>quotient</code>, then <code>quot.lift</code>/<code>quotient.lift</code></p>

#### [ Kevin Buzzard (Sep 08 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133563238):
<p>Ali I don't know if this helps, but when Luca was learning about equivalence classes (because he wanted to define a group structure on pi_1(X,x), which is a quotient) I wrote <a href="https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean">https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean</a> to show him some basic tricks. For basic questions like how to define a function on a set of equivalence classes I could recommend the relevant docs <a href="https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients">https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients</a> from TPIL, however mathlib adds extra functions which one can use with quotients, and these are not documented here. The mathlib file is here <a href="https://github.com/leanprover/mathlib/blob/master/data/quot.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/quot.lean">https://github.com/leanprover/mathlib/blob/master/data/quot.lean</a> and it defines things such as <code>quotient.eq</code> which are very useful in practice.</p>

#### [ Ali Sever (Sep 08 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133570338):
<p>Thanks, I was reading up on these this morning. I don't think there's a way to use the "cheat" method Coq uses (above), because I can't use exists to eliminate into something that isn't Prop.</p>

#### [ Ali Sever (Sep 09 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608290):
<p>is there a way to do quot.lift on a set with a function that is constant over the set?</p>

#### [ Chris Hughes (Sep 09 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608428):
<p>You mean a computable function from <code>set \a</code> that's based on some arbitrary element of a set?</p>

#### [ Chris Hughes (Sep 09 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608436):
<p>The answer is probably no, because a set contains no computational content about it's elements.</p>

#### [ Ali Sever (Sep 09 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608502):
<p>Why does it work for quotient sets, but not just normal sets?</p>

#### [ Kevin Buzzard (Sep 09 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608553):
<p>Why don't you formalise exactly what you're asking in Lean and post it? It's good practice, and also good practice.</p>

#### [ Ali Sever (Sep 09 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133608945):
<p>Something like this, <br>
<code>def F {α β : Type} (A : set α) (f : α → β) : (∀ a b, a ∈ A → b ∈ A → f a = f b) → β := x</code></p>

#### [ Johannes Hölzl (Sep 09 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609193):
<p>This is not enough. You need to assume that <code>A</code> is not empty.</p>

#### [ Johannes Hölzl (Sep 09 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609197):
<p>Then you can use some form of choice. (or you know that <code>β</code> is not empty and chose a default element.</p>

#### [ Reid Barton (Sep 09 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609247):
<p>Or if you express the nonempty condition as <code>trunc A</code>, which is the quotient of <code>A</code> by the relation which identifies everything, then you can define <code>F</code> (computably) using <code>quotient.lift</code>.</p>

#### [ Reid Barton (Sep 09 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609264):
<p>If you use <code>choice</code>, then you don't even need the condition <code>(∀ a b, a ∈ A → b ∈ A → f a = f b)</code> to define <code>F</code>, which is mildly alarming, but you do need it to prove that <code>F</code> equals <code>f a</code> for any <code>a ∈ A</code>.</p>

#### [ Ali Sever (Sep 09 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609451):
<p>If I use <code>trunc</code>, will it be annoying to switch between <code>A</code> and <code>trunc A</code>?</p>

#### [ Reid Barton (Sep 09 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133609872):
<p>Well <code>trunc A</code> is an alternative to <code>nonempty A</code>, which you would need instead.<br>
The main annoyance of <code>trunc A</code> is that it isn't a proposition.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133610024):
<blockquote>
<p>Something like this, <br>
<code>def F {α β : Type} (A : set α) (f : α → β) : (∀ a b, a ∈ A → b ∈ A → f a = f b) → β := x</code></p>
</blockquote>
<p>You mean <code>:= sorry</code>? As others have pointed out this can't yet be done (alpha and beta could both be empty at this point). So in some sense you still haven't asked the question.</p>

#### [ Ali Sever (Sep 09 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133610381):
<p>I guess I'll have to try a different approach</p>

#### [ Kevin Buzzard (Sep 09 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/making%20an%20equiv/near/133610654):
<p>I'm not saying that any approach doesn't work, but I am saying that I've learnt from experience that actually formalising my question precisely as <code>definition : blah := sorry</code> or <code>theorem : blah := sorry</code> really helps me to understand what I am asking before I ask it.</p>


{% endraw %}
