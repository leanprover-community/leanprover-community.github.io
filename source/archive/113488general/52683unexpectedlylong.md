---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52683unexpectedlylong.html
---

## [general](index.html)
### [unexpectedly long](52683unexpectedlylong.html)

#### [Kenny Lau (Sep 28 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134828020):
```lean
import data.finset

open finset lattice

set_option profiler true

variables {α : Type*} {β : Type*} {s : finset β} {f : β → α} [semilattice_sup_bot α]

lemma sup_le {a : α} : (∀b ∈ s, f b ≤ a) → s.sup f ≤ a :=
by letI := classical.dec_eq β; from
finset.induction_on s (λ _, bot_le) (by simp {contextual := tt})
-- why so long?
```

#### [Kenny Lau (Sep 28 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134828031):
takes somewhere between 5s and 30s to compile

#### [Simon Hudon (Sep 28 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829320):
Is the time spent on `simp`?

#### [Kenny Lau (Sep 28 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829840):
I think so

#### [Kenny Lau (Sep 28 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829940):
btw that's `finset.sup_le`

#### [Kenny Lau (Sep 28 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829952):
that's right, a 10s-lemma is inside mathlib

#### [Simon Hudon (Sep 28 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839187):
I'm planning on writing a tactic today `squeeze_simp` that will call `simp` and print a minimized `simp only` version. That might help in your endeavor

#### [Simon Hudon (Sep 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839219):
I can automate the application of the suggestion in emacs but I don't know how to do the same with VS code

#### [Johan Commelin (Sep 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839421):
Register it as a hole command, like `tidy` does.

#### [Simon Hudon (Sep 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839603):
Is that a mechanism of VS Code?

#### [Johan Commelin (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840062):
No, it's a Lean thing

#### [Johan Commelin (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840104):
I think it is a type class

#### [Johan Commelin (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840132):
But I guess IDE's also have to hook into it. But this is a one time thing that has been done already

#### [Simon Hudon (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840140):
Thanks! I'm looking at the `tidy` code, it's actually an attribute

#### [Simon Hudon (Sep 28 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840156):
Cool

#### [Reid Barton (Sep 28 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840173):
Simon have you determined yet whether the emacs mode already supports hole commands? I haven't looked

#### [Johan Commelin (Sep 28 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840284):
I thought emacs always supported the supremum of the features of all other IDE's
By definition

#### [Simon Hudon (Sep 28 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840326):
It is indeed emacs definition

#### [Simon Hudon (Sep 28 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840382):
It does support hole commands, at least three that I have seen

#### [Johan Commelin (Sep 28 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840401):
Since `tidy` there should be 4

#### [Simon Hudon (Sep 28 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840430):
I confirm that I can now see tidy in that list too

#### [Simon Hudon (Sep 28 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840456):
I like the idea of the type hole but it has a down side: if you're replacing `simp` in a file, you have to do it one at a time.

#### [Reid Barton (Sep 28 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840547):
Aha I see, I have to be inside the hole and then invoke `lean-hole`.

#### [Reid Barton (Sep 28 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840568):
I misunderstood the docstring "Ask Lean for a list of holes, then ask the user which to use."

#### [Johan Commelin (Sep 28 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840701):
@**Simon Hudon** Agreed. Still it could be nice for the future. Because then one can use it during the golfing phase of a proof that one just finished.

#### [Johan Commelin (Sep 28 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840725):
For squeezing entire files you might not even want to focus on editor integration.

#### [Simon Hudon (Sep 28 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840941):
I agree with your first point Johan. For the second point, the reason I'm thinking about editor integration is out of laziness. The slow files are really big and applications of `simp` vary a lot so search and replace alone doesn't cut it

#### [Johan Commelin (Sep 28 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134841018):
Ok, fair enough

#### [Simon Hudon (Sep 28 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134841064):
What I want to do is search and replace `simp` (not preceded by a square bracket) with `squeeze_simp` which will output all the required substitutions with line numbers and then emacs can do a very targeted replacement of all the `squeeze_simp`

#### [Simon Hudon (Sep 28 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134841212):
But now that I know about `hole_command` attributes, I think I might start with that to test out my idea

