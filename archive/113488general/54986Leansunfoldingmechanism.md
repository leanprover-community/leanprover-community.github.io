---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54986Leansunfoldingmechanism.html
---

## Stream: [general](index.html)
### Topic: [Lean’s unfolding mechanism](54986Leansunfoldingmechanism.html)

---


{% raw %}
#### [ Sarah Mameche (May 07 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%E2%80%99s%20unfolding%20mechanism/near/126219226):
Hi there, 

Is Lean’s unfolding of mutually recursive definitions any different than the unfolding of ‚normal‘ definitions?

I defined a mutually recursive function and have some equality which should hold definitionally, but the proof term doesn’t type. If I do the proof by hand, reflexivity or simp won’t solve the equation and I need an extra unfolding step of the mutually recursive definition. Tagging the definition with a reducible-attribute doesn’t change anything.

However, the proof goes through without the unfolding in a simpler setting without indexed types.

Is there a way to work around this? As I am using proof terms, it would also be helpful to know how to do the unfolding in a proof term.

Thanks in advance!
Sarah

#### [ Mario Carneiro (May 08 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%E2%80%99s%20unfolding%20mechanism/near/126249977):
Definitions by mutual recursion are compiled to well founded recursions, and the generated equations are not guaranteed to be definitional. The equation compiler generates equations for all the match branches; they are used automatically if you `rw [T]` or `simp [T]` where `T`is your definition.


{% endraw %}
