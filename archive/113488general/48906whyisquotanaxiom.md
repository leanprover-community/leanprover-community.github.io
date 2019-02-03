---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48906whyisquotanaxiom.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [why is quot an axiom?](https://leanprover-community.github.io/archive/113488general/48906whyisquotanaxiom.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Dec 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363029):
<p>Can't we just do it like this?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="c1">-- Lean has the &quot;quotient&quot; function to make equivalence classes.</span>
<span class="c1">-- Here I try to figure out why it is needed.</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">namespace</span> <span class="n">xena</span>

<span class="c1">-- this doesn&#39;t work with Prop but do I care?</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="c1">-- equiv reln closure of r</span>
<span class="kn">inductive</span> <span class="n">requiv</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">of_r</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">requiv</span> <span class="n">a</span> <span class="n">b</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">requiv</span> <span class="n">a</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">symm</span> <span class="o">⦃</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">⦄</span> <span class="o">:</span> <span class="n">requiv</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">requiv</span> <span class="n">b</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">trans</span> <span class="o">⦃</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">β</span><span class="o">⦄</span> <span class="o">:</span> <span class="n">requiv</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">requiv</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">requiv</span> <span class="n">a</span> <span class="n">c</span>

<span class="kn">definition</span> <span class="n">equiv_class</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">{</span><span class="n">c</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">|</span> <span class="n">requiv</span> <span class="n">r</span> <span class="n">b</span> <span class="n">c</span><span class="o">}</span>

<span class="kn">definition</span> <span class="n">quot</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">eq_cl</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span> <span class="bp">//</span> <span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv_class</span> <span class="n">r</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">eq_cl</span><span class="o">}</span>

<span class="kn">namespace</span> <span class="n">quot</span>

<span class="kn">definition</span> <span class="n">mk</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">),</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">quot</span> <span class="n">r</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">α</span> <span class="n">r</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">equiv_class</span> <span class="n">r</span> <span class="n">a</span><span class="o">,</span><span class="n">a</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">ind</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">quot</span> <span class="n">r</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">},</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="o">(</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span><span class="o">))</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">quot</span> <span class="n">r</span><span class="o">),</span> <span class="n">β</span> <span class="n">q</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">α</span> <span class="n">r</span> <span class="n">β</span> <span class="n">h</span> <span class="n">q</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">rcases</span> <span class="n">q</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">C</span><span class="o">,</span><span class="n">a</span><span class="o">,</span><span class="n">Ha</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">convert</span> <span class="n">h</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">Ha</span><span class="o">,</span>
<span class="kn">end</span>

<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">lift</span> <span class="o">:</span>
  <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">),</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="n">quot</span> <span class="n">r</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">α</span> <span class="n">r</span> <span class="n">β</span> <span class="n">f</span> <span class="n">h</span> <span class="n">q</span><span class="o">,</span><span class="k">begin</span>
  <span class="n">apply</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">q</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">C</span><span class="o">,</span><span class="n">HC</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="c1">-- cases HC with a Ha, MEH</span>
  <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">HC</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">Ha</span> <span class="o">:</span> <span class="n">equiv_class</span> <span class="n">r</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">C</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">HC</span><span class="o">,</span>
  <span class="c1">-- ask about better way</span>
  <span class="n">exact</span> <span class="n">a</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">definition</span> <span class="n">sound</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">b</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">α</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span><span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">mk</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="n">equiv_class</span> <span class="n">r</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">equiv_class</span> <span class="n">r</span> <span class="n">b</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">this</span><span class="o">],</span>
  <span class="n">ext</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">requiv</span> <span class="n">r</span> <span class="n">b</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">requiv</span><span class="bp">.</span><span class="n">trans</span> <span class="bp">_</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">requiv</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">requiv</span><span class="bp">.</span><span class="n">of_r</span><span class="o">,</span>
    <span class="n">assumption</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">requiv</span> <span class="n">r</span> <span class="n">a</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">requiv</span><span class="bp">.</span><span class="n">trans</span> <span class="bp">_</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">requiv</span><span class="bp">.</span><span class="n">of_r</span><span class="o">,</span>
    <span class="n">assumption</span><span class="o">,</span>
  <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">quot</span>

<span class="kn">end</span> <span class="n">xena</span>
</pre></div>


<p>I think I do all the basic theory of <code>quot</code>. I've been teaching quotients (in ZFC) in my class and I was trying to figure out how to explain to mathematicians why all this <code>quot.sound</code> stuff all had to be dealt with via extra axioms, but I've just done it all myself. The two sacrifices I had to make were: (1) it doesn't work for props (but who takes a quotient on proofs of a prop?) and (2) <code>lift</code> (the map which mathematicians think of as a "descent", quite the other direction to the computer science word) is noncomputable. What does <code>quot.sound</code> offer that my set-up doesn't but which I want or need?</p>

#### [ Kevin Buzzard (Dec 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363044):
<p>I just make the quotient type as a bunch of equivalence classes.</p>

#### [ Kevin Buzzard (Dec 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363092):
<p>A subtype of <code>set β</code> consisting of the equiv classes.</p>

#### [ Reid Barton (Dec 21 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152363322):
<p>The differences are that <code>lift</code> is computable, and <code>lift f _ (mk r x) = f x</code>(which it looks like you haven't proved, but I'm sure you can) hold definitionally (this is <code>quot.lift_beta</code>).</p>

#### [ Kevin Buzzard (Dec 22 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152364358):
<p>Actually I'm struggling with the theorem about lift:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- the computation principle</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">,</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">thm</span> <span class="o">:</span> <span class="n">lift</span> <span class="n">f</span> <span class="n">h</span> <span class="o">(</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">rcases</span> <span class="o">(</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span><span class="o">)</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">C</span><span class="o">,</span><span class="n">HC</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- HC has nothing to do with a now.</span>
  <span class="k">let</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">HC</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">Hb</span> <span class="o">:</span> <span class="n">equiv_class</span> <span class="n">r</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">C</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">HC</span><span class="o">,</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">α : Type u,</span>
<span class="cm">r : α → α → Prop,</span>
<span class="cm">β : Type v,</span>
<span class="cm">f : α → β,</span>
<span class="cm">a : α,</span>
<span class="cm">h : ∀ (a b : α), r a b → f a = f b,</span>
<span class="cm">C : set α,</span>
<span class="cm">HC : ∃ (a : α), equiv_class r a = C,</span>
<span class="cm">b : α := classical.some HC,</span>
<span class="cm">Hb : equiv_class r b = C</span>
<span class="cm">⊢ lift f h ⟨C, HC⟩ = f a</span>
<span class="cm">-/</span>
  <span class="k">show</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">h</span> <span class="n">b</span> <span class="n">a</span><span class="o">,</span>
  <span class="c1">-- but I don&#39;t know a ∈ C</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Dec 22 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152367268):
<p>Also, your proof of <code>sound</code> uses <code>quot.sound</code></p>

#### [ Kevin Buzzard (Dec 22 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152386750):
<p>Oh does it? I suppose that's cheating :-)</p>

#### [ Mario Carneiro (Dec 22 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152387461):
<p>You use set extensionality in the proof, which is an axiom in ZFC and is derived from <code>propext</code> and <code>quot.sound</code> in lean</p>

#### [ Kevin Buzzard (Dec 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152462524):
<p>OK so I proved <code>xena.quot.thm</code>. I think definitional equality is overrated, and if I have my maths hat on I'd say the same about computability. I am concerned about Chris' comment though. I am doing this to try and figure out how to explain to mathematicians why Lean wants quotients to be an extra axiom. But set extensionality is implied by function extensionality, right? Would another approach have been to make funext and/or propext axioms and then get quotients using my method? At least if we decide not to care about computability and definitional equality and be 100% mathematician.</p>

#### [ Mario Carneiro (Dec 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463063):
<p>yes, that's called zfc</p>

#### [ Mario Carneiro (Dec 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463066):
<p>you make set.ext an axiom</p>

#### [ Mario Carneiro (Dec 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463070):
<p>and derive funext and the others by constructing everything from sets</p>

#### [ Mario Carneiro (Dec 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20quot%20an%20axiom%3F/near/152463123):
<p>if you want to convince yourself, make a copy of <code>set.ext</code> as an actual axiom, and then derive all that and check that you didn't use propext or quot.sound in <code>#print axioms</code></p>


{% endraw %}
