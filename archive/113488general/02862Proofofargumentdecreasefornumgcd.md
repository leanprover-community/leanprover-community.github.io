---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02862Proofofargumentdecreasefornumgcd.html
---

## [general](index.html)
### [Proof of argument decrease for num.gcd](02862Proofofargumentdecreasefornumgcd.html)

#### [Seul Baek (Jun 07 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127717897):
I'm trying to define `gcd` for `num`. I've already defined `num.mod` and proved related lemmas (which you can check at https://github.com/skbaek/qelim/blob/master/src/common/num.lean), and here's my first attempt using those preliminary definitions :
```
def gcd : num → num → num
| 0       y := y
| (pos x) y := 
  have y % pos x < pos x, from mod_lt _ $ pos_pos _,  
  gcd (y % pos x) (pos x)
```
I get an error message saying that Lean failed to prove recursive application is decreasing. Apparently Lean is not using the proof of argument decrease provided by `have`. I'm not sure why this happens, since the definition of `nat.gcd` is almost identical. Any ideas?

#### [Gabriel Ebner (Jun 07 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127718228):
The error message shows what you need to prove: in this case, it's `num.sizeof (y % pos x) < pos_num.sizeof x + 1` (didn't clone the repo).

#### [Gabriel Ebner (Jun 07 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127718320):
The default termination measure for well-founded recursion in the equation compiler is lexicographic ordering of the `sizeof` values of the arguments.  You should probably define `has_sizeof` for `num` in a sensible way (i.e. the nat value).  Check out `#eval sizeof (1000:num)`

#### [Gabriel Ebner (Jun 07 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127718425):
Note that `#eval sizeof` is broken for nested and mutual inductives.  https://github.com/leanprover/lean/issues/1518

#### [Seul Baek (Jun 07 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127720042):
That worked. Thank you!

#### [Mario Carneiro (Jun 12 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127961269):
@**Seul Baek** The latest mathlib update includes `div` and `gcd` for `num` and `znum`. It is implemented in binary, rather than by repeated subtraction, so it should be exponentially faster than the transcribed `nat` definition, which is what it looks like you did. I think `gcd` should have something like `O((log n)^2)` performance in the kernel now

#### [Seul Baek (Jun 15 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/128092239):
@**Mario Carneiro** Thank you for the notice. This is very good news - I was only thinking about faster subtraction using binary representations.

