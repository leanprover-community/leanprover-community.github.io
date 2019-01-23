---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50034cancoercionsbeabused.html
---

## Stream: [general](index.html)
### Topic: [can coercions be abused?](50034cancoercionsbeabused.html)

---


{% raw %}
#### [ Edward Ayers (Sep 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514643):
I've added some questionable coercions to a lean file I am working on:
```lean
instance [partial_order α] : has_coe (a = b) (a ≤ b) := ⟨le_of_eq⟩
instance : has_coe (a = b) (b = a) := ⟨eq.symm⟩
```
They work great in the file that I am working on because it means I can now do things like
```lean
lemma (p :a ≤ b) (q:c = b) :a ≤ c  := le_trans p q
```
Within a bigger proof and I don't have to use any tactics or faff around making sure equalities match up.
Are there any pitfalls to this approach or is it good practice?

#### [ Kenny Lau (Sep 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514725):
wow

#### [ Edward Ayers (Sep 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514812):
In particular I am worried that stuff like `has_coe (a = b) (b = a)` will cause a loop of doom in the elaborator.

#### [ Mario Carneiro (Sep 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514910):
it will

#### [ Mario Carneiro (Sep 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514920):
you will probably get a timeout coercing `a = b` to `a = c`

#### [ Edward Ayers (Sep 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514993):
```lean
example (p : a = c) : a = b := p
```
doesn't loop forever with the above coercion. How can I get the bad behaviour?

#### [ Mario Carneiro (Sep 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515063):
hm, not sure in that case. I will downgrade from "bad" to "highly suspicious"

#### [ Edward Ayers (Sep 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515081):
I will leave it in and keep coding and see if it explodes anywhere.

#### [ Mario Carneiro (Sep 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515084):
seems reasonable

#### [ Edward Ayers (Sep 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515127):
It has saved me a lot of typing.

#### [ Mario Carneiro (Sep 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515134):
I can believe it

#### [ Patrick Massot (Sep 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515368):
Ed, have you tried Simon's mono tactic, from https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean (see also https://github.com/leanprover-community/mathlib-nursery/blob/master/docs/monotonicity.md)

#### [ Edward Ayers (Sep 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515866):
That's a nice tactic. I am now thinking that it is bad practice to use coercions to do reasoning because your code now depends directly on the minutiae of how the elaborator works, which is somewhat opaque and subject to change. Whereas the tactics have well-defined behaviour and can be tuned.
However it is cool that the elaborator was able deal with my coercion abuse nicely. Are there any docs which specify precisely what the elaborator is doing when it looks for coercions?

#### [ Patrick Massot (Sep 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515882):
source code?


{% endraw %}
