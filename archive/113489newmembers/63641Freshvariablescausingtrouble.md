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
I'm in a bit of a pickle right now trying to deal with one of those messy `__mlocal__fresh__1234_56789` variables.

I have the following relevant lines in my tactic state:
``M N __mlocal__fresh_9046_21051 : matrix (fin m) (fin n) α,
r₁ : row_equivalent M __mlocal__fresh_9046_21051,
r₂ : row_equivalent_step __mlocal__fresh_9046_21051 N,
H₁ : row_equivalent.apply r₁ = __mlocal__fresh_9046_21051
⊢ elementary.apply (r₂.elem) (row_equivalent.apply r₁) = N``
Tantalisingly, I would love to perform some sort of rewrite or subst or simp with `H₁` to rewrite the goal as `⊢ elementary.apply (r₂.elem) __mlocal__fresh_9046_21051 = N`, but each of these fail. 
I think I could probably perform the rewrite (just via eq.trans) if I could `have` myself something of the form
`have H₂ :  elementary.apply (r₂.elem) (row_equivalent.apply r₁) =  elementary.apply (r₂.elem) __mlocal__fresh_9046_21051` (and solve this with something like `congr, from H₁`), but unfortunately I cannot do this as I cannot explicitly write down the `__mlocal__fresh_9046_21051` (of course, the numbers change every time Lean recompiles). 

Is there a way I can explicitly name my fresh variable in a less transient way?
Or am I doing something else completely stupid and in bad practice and shouldn't even have this fresh variable popping up at all?

Here's the actual code that's giving me this tactic state (you can see the fresh variable comes out of my induction over `row_equivalent`, which has two constructors, of the form `nil : Π M, row_equivalent M M` and `cons : Π (r₁ : row_equivalent M N) (r₂ : row_equivalent_step N L) , row_equivalent M L`)

``@[simp] lemma row_equivalent.apply_implements : Π {M N : matrix (fin m) (fin n) α} (r : row_equivalent M N), r.apply = N 
| M N (row_equivalent.nil) := by simp[row_equivalent.apply]
| M N (row_equivalent.cons r₁ r₂) := begin
  simp[row_equivalent.apply],
  have H₁, from row_equivalent.apply_implements r₁,
  -- Here is where I see the tactic state I provided above
  sorry,
end``

#### [ Mario Carneiro (Oct 24 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fresh%20variables%20causing%20trouble/near/136388270):
You should use `| _ _ (@row_equivalent.cons M N L r₁ r₂)` in the pattern match

#### [ Jack Crawford (Oct 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fresh%20variables%20causing%20trouble/near/136394125):
Ah yes, I don't know why I didn't think of this myself -- silly question!
Thanks @Mario!


{% endraw %}
