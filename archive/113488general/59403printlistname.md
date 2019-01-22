---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59403printlistname.html
---

## [general](index.html)
### [print list name](59403printlistname.html)

#### [Johan Commelin (Aug 09 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155695):
My first attempt at writing a tactic. I want a tactic that will `fail` by printing a list of tactics. I've copy-pasted code by Scott:
```lean
meta def get_applicable_lemmas : tactic name :=
do cs ← attribute.get_instances `applicable,
   fail -- <what do I put here?>
```
(Whoops, there was still code that tried to apply the tactics, only failing if none applied. That's now gone.)

#### [Johan Commelin (Aug 09 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155709):
Oh, and maybe there is a far easier way to look up all the current applicable lemmas then by writing a failing tactic. If so, I'dd also like to learn that method (-;

#### [Mario Carneiro (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155768):
I don't quite get what you are tying to do

#### [Johan Commelin (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155771):
I want Lean to print me a list of all lemmas that are tagged with `applicable`.

#### [Johan Commelin (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155775):
Hmmm, can I do this with `#print attribute applicable` or something similar?

#### [Johan Commelin (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155837):
Where do I what sorts of things I can `#print` anyways? So far I've learned two or three incantations by osmosis in this chat. Is this documented anywhere?

#### [Johan Commelin (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155843):
`#print attribute` is not a valid print command )-;

#### [Johan Commelin (Aug 09 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156105):
So, I need to fold `\lam n, n.to_string` over this list, right? And I can just use the regular fold. I don't need some `meta`-fold.

#### [Johan Commelin (Aug 09 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156112):
Because monads are just cool mathematical goodies.

#### [Johan Commelin (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156361):
```lean
meta def get_applicable_lemmas : tactic unit :=
do cs ← attribute.get_instances `applicable,
   tactic.trace (list.foldl (λ s n, name.to_string n ++ ", " ++ s) "" cs)
```

#### [Johan Commelin (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156365):
That seems to do what I want (-;

#### [Kevin Buzzard (Aug 09 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131157813):
```quote
So, I need to fold `\lam n, n.to_string` over this list, right? And I can just use the regular fold. I don't need some `meta`-fold.
```
Whilst I'm kind-of out of my depth, I think that the fact that you can use regular fold is one thing that Lean has over Coq. I *think* that in Coq you have to learn one language to write proofs and then another language to write tactics.

#### [Mario Carneiro (Aug 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158150):
here's another way:
```
meta def get_applicable_lemmas : tactic unit :=
do cs ← attribute.get_instances `applicable,
   cs.mmap' tactic.trace
```

#### [Mario Carneiro (Aug 09 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158225):
or ``attribute.get_instances `applicable >>= list.mmap' tactic.trace`` if you want to be clever

#### [Johan Commelin (Aug 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158259):
Right! That's nice (-;

#### [Johan Commelin (Aug 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158315):
Of course I should have thought of looking for some `map`-like.

#### [Mario Carneiro (Aug 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158319):
here I am using a kind of "meta map" `mmap`

#### [Mario Carneiro (Aug 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158331):
although this is because I want to map from inside a monad

#### [Mario Carneiro (Aug 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158372):
`mmap'` is more of a "for each" or "scan" type function than a map - it doesn't return any output

#### [Johan Commelin (Aug 09 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158948):
What is the difference between `tactic unit` vs `tactic name` vs `tactic string`?

#### [Kevin Buzzard (Aug 09 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159099):
that's like asking what the difference is between `option unit` and `option nat` and `option real`

#### [Kevin Buzzard (Aug 09 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159156):
If you're passing information around between tactics then you might want to use `tactic blah` (which means "blah plus the extra option of failure"), but at the end of it all when you want to run the tactic you may as well return something of type "tactic unit" because no other tactic wants the output.

#### [Kevin Buzzard (Aug 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159165):
The changing of the state is not an output of the tactic, that all goes on within the monad

#### [Johan Commelin (Aug 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159173):
Right. That makes sense.

