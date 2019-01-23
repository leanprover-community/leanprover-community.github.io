---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/18383overridingcoersions.html
---

## Stream: [new members](index.html)
### Topic: [overriding coersions](18383overridingcoersions.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 10 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overriding%20coersions/near/147433140):
Is there a way to define a coercion which takes priority over another one? I tried `@[priority 10]` but it doesn't seem like it does anything to a `has_coe` instance (and I don't know what it should do in any case)

#### [ Floris van Doorn (Nov 10 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overriding%20coersions/near/147436582):
Yes, that is exactly how it works. The default priority is 1000 though, so you have to make a priority higher than that to use that instance.

#### [ Floris van Doorn (Nov 10 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overriding%20coersions/near/147436593):
Example:
```
set_option pp.all true
example (n : ℕ) : (n : ℤ) = int.zero := begin end
instance my_coe : has_coe ℕ ℤ := ⟨int.of_nat⟩
example (n : ℕ) : (n : ℤ) = int.zero := begin end
@[priority 500] instance my_coe2 : has_coe ℕ ℤ := ⟨int.of_nat⟩
example (n : ℕ) : (n : ℤ) = int.zero := begin end
attribute [instance] [priority 1100] int.has_coe
example (n : ℕ) : (n : ℤ) = int.zero := begin end
attribute [instance] [priority 2000] my_coe2
example (n : ℕ) : (n : ℤ) = int.zero := begin end
```

#### [ Floris van Doorn (Nov 10 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overriding%20coersions/near/147436645):
(note: using `attribute` to change priority of a definition defined in a different file is probably bad design, because then the priority depends on whether you import that file)

#### [ Keeley Hoek (Nov 12 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overriding%20coersions/near/147511794):
Thanks very much @**Floris van Doorn** , the fact that everything starts at `1000` was what I was totally missing.


{% endraw %}
