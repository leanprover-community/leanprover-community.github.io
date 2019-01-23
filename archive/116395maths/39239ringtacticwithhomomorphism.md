---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39239ringtacticwithhomomorphism.html
---

## Stream: [maths](index.html)
### Topic: [ring tactic with homomorphism](39239ringtacticwithhomomorphism.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125892370):
Consider the following MWE
```lean
import tactic.ring
import data.real.basic

open real

def f : ℤ → ℝ := λ x, (x : ℝ)

example (n : ℝ) : (n + 3) * (n + 4) = n * n + 10 + 7 * n + 2
:= by ring

example (n : ℤ) : f (n + 3) * f (n + 4) = (f n) * (f n) + 10 + 7 * (f n) + f 2
:= by ring -- fails
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125892380):
How hard would it be to teach the `ring` tactic to use the axioms for ring homomorphisms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897415):
You could start by making f part of the `is_ring_hom` class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897515):
`instance f_is_a_ring_hom : is_ring_hom f := { map_add := sorry,map_mul := sorry,map_one := sorry}` is how to start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897567):
and then you need to fill in the proofs, which are all already there, with names I can't quite remember yet, hang on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897592):
They are probably called things like `cast_mul`, `cast_add` and `cast_one`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 30 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125900450):
I think the difficult part is getting `ring` to recognize `f 2 + f3 = f 5`. Apart from the problem with literals you can just `simp[is_ring_hom.map_add]` etc first.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902537):
@**Kevin Buzzard** Right..., so maybe instead of defining `f`, I should actually just assume that it is a ring hom. Maybe Lean should be able to deduce itself that this determines `f` completely!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902564):
@**Chris Hughes** Yes, I understand. But I really want Lean to deal with these things using only one straightforward tactic. After all, it is one of these “mathematically trivial” steps.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 30 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902597):
I'm saying that it should be easy to add it to the ring tactic, if all it requires is a `simp` in the definition of `ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902666):
Aaah, I see. Yes, that is true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125920901):
I'm not so sure about adding this to `ring`. This is outside the scope of `ring` as I see it, which is to solve equations in the first order theory of rings. If you want something like this it should be a different tactic; as Chris says it may be as simple as just `simp` with an appropriate simp set followed by `ring`.

