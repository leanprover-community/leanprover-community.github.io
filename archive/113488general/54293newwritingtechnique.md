---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54293newwritingtechnique.html
---

## Stream: [general](index.html)
### Topic: [new writing technique](54293newwritingtechnique.html)

---


{% raw %}
#### [ Patrick Massot (Jul 04 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102181):
I've found a nice new trick to write obfuscated^W concise code:
```lean
lemma chart_chart_inv {φ : chart X} {x : φ.target} : x ∈ φ.range → φ (φ.inv x) = x
| ⟨y, ⟨y_in, φ_y⟩⟩ := inv_fun_on_eq ⟨y, ⟨y_in, φ_y⟩⟩
```

#### [ Patrick Massot (Jul 04 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102241):
Why not writing `assume H, inv_fun_on_eq H`? Well, the sequences of pointy brackets in the pattern matching and body don't represent the same (anonymized) constructor.

#### [ Simon Hudon (Jul 04 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102445):
Would it make you happy if Lean gave you a warning about using the anonymous constructors in disjoint expressions to build expressions of different types?

#### [ Patrick Massot (Jul 04 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102464):
I don't know.

#### [ Patrick Massot (Jul 04 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102472):
I'm not complaining about anything.

#### [ Patrick Massot (Jul 04 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102520):
I do think that if I read this code later than a few days away from now, I'll be thinking WTF?

#### [ Simon Hudon (Jul 04 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102522):
Sorry, I'm highjacking your conversation. I've been saying for a while that we need a linter tool to find dubious code

#### [ Simon Hudon (Jul 04 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102528):
And I'm wondering how to define "dubious code"

#### [ Chris Hughes (Jul 04 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102619):
Maybe the type of the two `⟨y, ⟨y_in, φ_y⟩⟩`s is different.

#### [ Simon Hudon (Jul 04 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102865):
Yes, that's what Patrick was pointing out

#### [ Patrick Massot (Jul 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129103273):
Here is a minimized example for the curious readers:
```lean
import data.set.basic
open set

example (α β : Type) (s : set α) (f : α → β) (b) (h : ∃a∈s, f a = b) : b ∈ f '' s  := 
begin
  -- rw mem_image, exact h,
  -- rw mem_image_eq, exact h,
  rw mem_image,
  rcases h with ⟨a, ⟨b, c⟩⟩,
  exact ⟨a, ⟨b, c⟩⟩
end
```
The two commented out lines are nice tries that don't work.

#### [ Patrick Massot (Jul 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129103278):
And it's in tactic mode so you can see everything

#### [ Patrick Massot (Jul 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129103357):
@**Mario Carneiro** Is there a variation on `mem_image` that I'm missing here?

#### [ Mario Carneiro (Jul 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104411):
I see nothing wrong with `chart_inv_inv`

#### [ Mario Carneiro (Jul 04 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104523):
```
example (α β : Type) (s : set α) (f : α → β) (b) (h : ∃a∈s, f a = b) : b ∈ f '' s  :=
by simpa using h
```

#### [ Patrick Massot (Jul 04 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104604):
How does this work? What is `simpa` magically doing here? I know `mem_image` is a simp lemma. And then?

#### [ Chris Hughes (Jul 04 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104678):
`∃ (H : a ∈ s), f a = b ==> a ∈ s ∧ f a = b` ` exists_prop`


{% endraw %}
