---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92086computevalueoffunction.html
---

## [general](index.html)
### [compute value of function](92086computevalueoffunction.html)

#### [jmc (Mar 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932056):
Hi. Lean-newbie here. I've got a function f : \N \to \Z with a pretty involved definition. I would like to see what Lean thinks that the value of f is on 0,1,2,3 for example.
My current approach has been:
```lean
example : f 0 = n := refl
```
and then just trying different values of n, until I am lucky. But there should be a better way...

(Ok, I just saw there is a "new members" stream. If someone can move this topic overthere, please feel free to do so.)

#### [Simon Hudon (Mar 19 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932203):
Try:

```lean
#eval f 0
#eval f 1
#eval f 2
#eval f 3
```

#### [Moses Schönfinkel (Mar 19 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932204):
You can just `#eval f x`

#### [jmc (Mar 19 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932212):
Aah, thanks!

#### [Simon Hudon (Mar 19 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932223):
It uses the virtual machine so if `f` is computation intensive, this will ensure swift execution

#### [Moses Schönfinkel (Mar 19 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932268):
If you want slow execution, you can try `#reduce f x` ;).

#### [Moses Schönfinkel (Mar 19 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932273):
(Also your `refl` trick made me giggle so you're awarded a pointless internet point.)

#### [Simon Hudon (Mar 19 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932327):
(I think we can use octopuses to award those internet points)

#### [Moses Schönfinkel (Mar 19 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932332):
What an excellent idea.

#### [jmc (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932348):
Thanks for the point!

#### [Simon Hudon (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932349):
thanks)

#### [Andrew Ashworth (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932352):
the `rfl` thing is considered good style if you go by "Software Foundations"

#### [Andrew Ashworth (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932357):
it's basically inline unit testing

#### [Moses Schönfinkel (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932360):
I have no recollection of that in SF o_O?

#### [Moses Schönfinkel (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932361):
Aaah right.

#### [Moses Schönfinkel (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932362):
You mean his auto-tests.

#### [Andrew Ashworth (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932423):
yeah, for ex

#### [Andrew Ashworth (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932425):
```coq
Definition hd (default:nat) (l:natlist) : nat :=
  match l with
  | nil ⇒ default
  | h :: t ⇒ h
  end.
Definition tl (l:natlist) : natlist :=
  match l with
  | nil ⇒ nil
  | h :: t ⇒ t
  end.
Example test_hd1: hd 0 [1;2;3] = 1.
Proof. reflexivity. Qed.
Example test_hd2: hd 0 [] = 0.
Proof. reflexivity. Qed.
Example test_tl: tl [1;2;3] = [2;3].
Proof. reflexivity. Qed.
```

#### [Moses Schönfinkel (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932428):
Yeah absolutely.

#### [Moses Schönfinkel (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932431):
Oh boy that book is such an excellent introduction to these things.

#### [Moses Schönfinkel (Mar 19 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932446):
Compare that to CPDT... :-\.

#### [Moses Schönfinkel (Mar 19 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932448):
(Sorry Adam...)

#### [Andrew Ashworth (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932498):
yeah, if you do 2 semesters of software foundations

#### [Andrew Ashworth (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932500):
first

#### [Andrew Ashworth (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932503):
maybe you can understand cpdt, except you still won't

#### [jmc (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute value of function/near/123932504):
Anyway, the function in question is the Ramanujan tau function (https://en.wikipedia.org/wiki/Ramanujan%27s_tau_function)
Already `#reduce \tau 2` is extremely slow for my implementation.
But `#eval \tau 4` is pretty fast. And the first 5 values are correct (^;

