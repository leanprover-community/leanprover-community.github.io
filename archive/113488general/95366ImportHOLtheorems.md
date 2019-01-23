---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95366ImportHOLtheorems.html
---

## Stream: [general](index.html)
### Topic: [Import HOL theorems](95366ImportHOLtheorems.html)

---

#### [Martin Kolář (Nov 02 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/137040429):
Hi, I'm new here, and I have a question regarding LEAN's versatility.

Is it possible to import Isabelle/HOL proofs into LEAN? How could this be achieved?

The benefit would be the availability of the [archive of formal proofs](https://www.isa-afp.org/) within LEAN, which contains over 118'600 lemmas, many of which are very handy.

#### [Johan Commelin (Nov 02 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/137045958):
@**Martin Kolář** Welcome! I am certainly not an expert on Lean or Isabelle. There are others around who will have more to say on this. What I do know is that there is not currently any link between Lean and other theorem provers. Also, it seems that porting proofs would result in non-idiomatic Lean. (I am not enough of an expert to know if this is a big problem.)

#### [Andrew Ashworth (Nov 02 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/137067110):
Isabelle would be quite difficult. It is more feasible for a Coq-Lean bridge to be built since the logical foundations (CIC) are the same.

#### [Andrew Ashworth (Nov 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/137067194):
Also, in a sense, even if you were to model Isabelle/HOL in Lean, then transfer the proofs over - then to build on it you would necessarily need to keep working in that Isabelle/HOL world. So there would be no advantage to switching, I think.

#### [Martin Kolář (Nov 08 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/147297379):
@**Johan Commelin** Thanks for your quick reply. So we would need to add axioms to Lean to accept Isabelle proofs? That sounds inconvenient, but feasible.

#### [Johan Commelin (Nov 08 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/147297642):
No, I am not talking about adding axioms. I think you would need to write some sort of transpiler.

#### [Johan Commelin (Nov 08 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/147297669):
And I think that becomes very painful, and the results are usually even less readable then what we have in mathlib now.

#### [Rob Lewis (Nov 08 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/147297875):
This sort of proof import/translation is possible in principle, and there are people who have investigated/are investigating it. See e.g. http://logipedia.inria.fr/about/about.php which is based on Dedukti. It doesn't necessarily require extra axioms. The biggest problem, that keeps it from being usable in practice right now, is that e.g. Lean's current library and natural Lean style don't match Isabelle's current library and natural Isabelle style. If you could import the AFP and Isabelle standard library directly into Lean, you wouldn't get something that uses mathlib. You'd get an image of Isabelle in Lean, using Isabelle's `nat`, `int`, etc etc. It would have no connection to anything formalized in Lean and would be extremely hard to work with.

#### [Rob Lewis (Nov 08 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Import%20HOL%20theorems/near/147297963):
In principle, you can try to match Isabelle concepts to Lean concepts, and a good enough interpreter could produce a usable Lean development from elsewhere. This doesn't exist yet and would be extremely hard to do.

