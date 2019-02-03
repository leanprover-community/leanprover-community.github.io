---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/63641Freshvariablescausingtrouble.html
---

## Stream: [new members](index.html)
### Topic: [Fresh variables causing trouble](63641Freshvariablescausingtrouble.html)

---


{% raw %}
#### [ Jack Crawford (Oct 24 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fresh%20variables%20causing%20trouble/near/136386136):
<p>I'm in a bit of a pickle right now trying to deal with one of those messy <code>__mlocal__fresh__1234_56789</code> variables.</p>
<p>I have the following relevant lines in my tactic state:<br>
<code>M N __mlocal__fresh_9046_21051 : matrix (fin m) (fin n) α,
r₁ : row_equivalent M __mlocal__fresh_9046_21051,
r₂ : row_equivalent_step __mlocal__fresh_9046_21051 N,
H₁ : row_equivalent.apply r₁ = __mlocal__fresh_9046_21051
⊢ elementary.apply (r₂.elem) (row_equivalent.apply r₁) = N</code><br>
Tantalisingly, I would love to perform some sort of rewrite or subst or simp with <code>H₁</code> to rewrite the goal as <code>⊢ elementary.apply (r₂.elem) __mlocal__fresh_9046_21051 = N</code>, but each of these fail. <br>
I think I could probably perform the rewrite (just via eq.trans) if I could <code>have</code> myself something of the form<br>
<code>have H₂ :  elementary.apply (r₂.elem) (row_equivalent.apply r₁) =  elementary.apply (r₂.elem) __mlocal__fresh_9046_21051</code> (and solve this with something like <code>congr, from H₁</code>), but unfortunately I cannot do this as I cannot explicitly write down the <code>__mlocal__fresh_9046_21051</code> (of course, the numbers change every time Lean recompiles). </p>
<p>Is there a way I can explicitly name my fresh variable in a less transient way?<br>
Or am I doing something else completely stupid and in bad practice and shouldn't even have this fresh variable popping up at all?</p>
<p>Here's the actual code that's giving me this tactic state (you can see the fresh variable comes out of my induction over <code>row_equivalent</code>, which has two constructors, of the form <code>nil : Π M, row_equivalent M M</code> and <code>cons : Π (r₁ : row_equivalent M N) (r₂ : row_equivalent_step N L) , row_equivalent M L</code>)</p>
<p><code>@[simp] lemma row_equivalent.apply_implements : Π {M N : matrix (fin m) (fin n) α} (r : row_equivalent M N), r.apply = N 
| M N (row_equivalent.nil) := by simp[row_equivalent.apply]
| M N (row_equivalent.cons r₁ r₂) := begin
  simp[row_equivalent.apply],
  have H₁, from row_equivalent.apply_implements r₁,
  -- Here is where I see the tactic state I provided above
  sorry,
end</code></p>

#### [ Mario Carneiro (Oct 24 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fresh%20variables%20causing%20trouble/near/136388270):
<p>You should use <code>| _ _ (@row_equivalent.cons M N L r₁ r₂)</code> in the pattern match</p>

#### [ Jack Crawford (Oct 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fresh%20variables%20causing%20trouble/near/136394125):
<p>Ah yes, I don't know why I didn't think of this myself -- silly question!<br>
Thanks @Mario!</p>


{% endraw %}
