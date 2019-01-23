---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74219Multipleusesofexistsi.html
---

## Stream: [new members](index.html)
### Topic: [Multiple uses of existsi](74219Multipleusesofexistsi.html)

---


{% raw %}
#### [ Calle Sönne (Nov 20 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148043024):
I have the following goal:
```lean
∃ (s : ℕ) (H : s ∈ S), ∀ (k : ℕ), k ∈ S → s ≤ k
```
Now I have an element s which has all required properties to prove this goal. I would like to provide this s using existsi. Of course I also have to provide the fact that s is in S (my hypothesis Hs). However using existsi s Hs doesnt seem to work, and I need to call existsi two times. That is existsi s, existsi Hs. Is there anyway to make this into a one-liner?

#### [ Johan Commelin (Nov 20 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148043187):
`refine \<s, Hs, _\>`

#### [ Rob Lewis (Nov 20 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148043189):
`existsi` takes an expression or a list of expressions. Try `existsi [s, Hs]`.

#### [ Calle Sönne (Nov 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148044104):
Thank you! Both methods worked fine :). What would be the pro of using refine instead of existsi? That its more general?

#### [ Johan Commelin (Nov 20 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148044259):
See also https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.60existsi.60.20is.20so.20dumb

#### [ Calle Sönne (Nov 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148044703):
Thanks :)

#### [ Kevin Buzzard (Nov 21 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148078885):
```lean
theorem easy : ∃ x : ℤ, x = x :=
begin
--  existsi 23, -- lean says "that's not an integer!"
    refine ⟨23,_⟩, -- works fine
    refl
end
```
I have almost given up on `existsi`, it doesn't try hard enough.


{% endraw %}
