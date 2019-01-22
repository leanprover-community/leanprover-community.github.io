---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90057Floatingpointarithmetic.html
---

## [general](index.html)
### [Floating point arithmetic](90057Floatingpointarithmetic.html)

#### [Scott Morrison (Apr 13 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125010724):
A student here has a lovely suggestion for a simple application of machine learning to automation. I’d love to try implementing it with her, but quickly realised that we’d need to do floating point arithmetic (just some gradient descent problems, so essentially inverting numerical matrices).

#### [Scott Morrison (Apr 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125010780):
It seems the options would be:
1. Do this directly in Lean
2. Do it in C++, and have to compile our own branch of Lean to run it
3. Call external processes via the io monad

#### [Scott Morrison (Apr 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125010794):
If anyone has advice or suggestions choosing between these, I’d love to hear.

#### [Simon Hudon (Apr 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125010851):
Any chance that representing your numbers as fractions like Q does would be good enough?

#### [Simon Hudon (Apr 13 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125011141):
The other idea I can think of is to use the C api to call a lean function that takes the float type and its operations as parameters.

#### [Simon Hudon (Apr 13 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125011155):
In the second case, that means that you don't need your own branch of Lean which might make it easier to evolve along the successive versions of Lean

#### [Simon Hudon (Apr 13 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125011157):
(deleted)

#### [Andrew Ashworth (Apr 13 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125012392):
i would try and write it in C++ for now; when lean 4 rolls around there should be a ffi we can interface with

#### [Andrew Ashworth (Apr 13 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125012563):
ironically it might be less work, since there's no notion of matrix computations in lean

#### [Mario Carneiro (Apr 13 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125014205):
There is an experimental implementation of floating point arithmetic in `data.fp.basic` in mathlib. I'm not certain about all the modeling choices yet, especially considering how inconsistent hardware support is for floats, even when IEEE-conforming. I know Leo is also tackling this problem; the last version of the lean IR I saw supported floats at the low level, so I expect that Lean 4 will have a float datatype, and I'm not sure what he intends to do about the inconsistencies (probably just ignore them, but that means going meta which I'd like to avoid).

#### [Scott Morrison (Apr 13 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125017055):
```quote
The other idea I can think of is to use the C api to call a lean function that takes the float type and its operations as parameters.
```
@**Simon Hudon**, where can I read about / see an example of the C api?

#### [Simon Hudon (Apr 13 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125017243):
I don't know of any good documentation. Beside the source code, you could look at Joe Hendrix' Haskell binding for Lean: https://github.com/GaloisInc/lean-haskell-bindings/tree/master/src/Language/Lean/Internal

#### [Scott Morrison (Apr 13 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125017302):
Maybe before I get started: I'm looking to write most of my tactic in Lean, and just farm out the numerics to C. Is this API suitable for doing that kind of thing? Or just for calling Lean from C?

#### [Simon Hudon (Apr 13 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125017469):
I think just calling Lean from C should be sufficient. You can do a bit like the old IO interface and make a type class:

```
class float.interface :=
  (float : Type)
  (add : float -> float -> float)
  (mul : floal -> float -> float)
  -- ...
```

Then, on the lean side, all you need is `variable [float.interface]` at the beginning of the files that need access to float. On the C side, you create an instance and you call `main` with that instance as a parameter.

#### [Scott Morrison (Apr 13 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125017523):
Okay, but I want to initiate all this running from inside the tactic monad. How do I even tell Lean about the existence of that C code?

#### [Simon Hudon (Apr 13 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125017544):
I see, yeah, that's tricky. Maybe forking Lean would be easier for that

#### [Kevin Buzzard (Apr 13 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125022727):
Would the Lean Mathematica interface be useful here?

#### [Kevin Buzzard (Apr 13 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125022729):
[I don't really know what I'm talking about]

#### [Simon Hudon (Apr 13 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point%20arithmetic/near/125032505):
That sounds like a good idea to me. It might simplify things even more because matrix multiplication / inversion is already implemented in Mathematical

