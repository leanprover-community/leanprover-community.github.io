---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17585whyisthisslow.html
---

## [general](index.html)
### [why is this slow?](17585whyisthisslow.html)

#### [Kenny Lau (Sep 16 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134047650):
```lean
import data.polynomial
import linear_algebra.multivariate_polynomial
import ring_theory.associated

universe u

namespace algebraic_closure

variables (k : Type u) [field k] [decidable_eq k]

def irred : set (polynomial k) :=
{ p | irreducible p }

def big_ring : Type u :=
mv_polynomial (irred k) k

instance : comm_ring (big_ring k) :=
mv_polynomial.comm_ring

set_option profiler true
def big_ideal : set (big_ring k) :=
span $ ⋃ p : irred k, { polynomial.eval₂ mv_polynomial.C (mv_polynomial.X p) p.1 }
/-
parsing took 0.154ms
elaboration of big_ideal took 7.53s
type checking of big_ideal took 9.17ms
decl post-processing of big_ideal took 11.1ms
compilation of algebraic_closure.big_ideal took 0.205ms
-/

end algebraic_closure
```

#### [Kenny Lau (Sep 16 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134047652):
is there any way to make this faster?

#### [Kenny Lau (Sep 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134047761):
@**Chris Hughes**

#### [Chris Hughes (Sep 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134048125):
This compiles in no time. I don't know the solution though.
```lean
def big_ideal : set (mv_polynomial (irred k) k) :=
span $ ⋃ p : irred k, { polynomial.eval₂ mv_polynomial.C (mv_polynomial.X p) p.1 }
```

#### [Kenny Lau (Sep 16 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049306):
@**Kevin Buzzard** @**Chris Hughes** I suspect Chris's span is the wrong one, which means we will have to once again wait for the refactoring

#### [Kevin Buzzard (Sep 16 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049357):
So what exactly is being refactored? Yeah I am putting "research level" coding on hold at the minute and thinking more about organisational stuff. The question of why it's slow is still of independent interest. What is causing the hold-up? Is it type class inference?

#### [Kenny Lau (Sep 16 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049370):
if we specify that we're talking about the span as an ideal (which is this case) or that we're talking about the span as a k-module (which is not this case) then it would be more convenient

#### [Kevin Buzzard (Sep 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049729):
@**Mario Carneiro** is this another +1 for saying which ring we're talking about explicitly? 

I guess there is also now the option of making the "ideal" version of things into its own little interface -- e.g. ideal.span could mean "the span of this subset of the ring R as an R-module"

#### [Kevin Buzzard (Sep 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049730):
I would love to be able to debug this sort of thing. Presumably the `by exact` insertion changes the elaboration strategy somehow. But in my mind this just raises a bunch of questions as to how it's working and how the change makes any difference.

#### [Kevin Buzzard (Sep 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049731):
```lean
def big_ideal' : set (big_ring k) :=
by exact (span $ ⋃ p : irred k, { polynomial.eval₂ mv_polynomial.C (mv_polynomial.X p) p.1 })

```

is much quicker for me and seems to give the same answer.

#### [Kevin Buzzard (Sep 16 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050085):
Stupid `#print notation ⋃` gives me a useless answer. I had to grep through the source code to find it's `set.Union`.

#### [Chris Hughes (Sep 16 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050127):
So in future presumably `span` will take the ring as an explicit argument?

#### [Kevin Buzzard (Sep 16 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050575):
hopefully. Hey I got Kenny's version working quickly:

```lean
def big_ideal' : set (big_ring k) :=
span $ ⋃ p : irred k, {@polynomial.eval₂ _ _ _ _ _ mv_polynomial.C _ (mv_polynomial.X p) p.1}
```

#### [Kevin Buzzard (Sep 16 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050576):
I'm hoping that `submodule` will as well.

#### [Kevin Buzzard (Sep 16 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050582):
In your polynomial code, `module R (polynomial R)` takes precedence over `module (polynomial R) (polynomial R)` making it really difficult to talk about ideals of polynomial rings!

#### [Chris Hughes (Sep 16 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050723):
Change it then. I didn't really think about that problem when I wrote it.

#### [Kevin Buzzard (Sep 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050770):
rofl
```lean
def big_ideal' : set (big_ring k) :=
span $ ⋃ p : irred k, {@polynomial.eval₂ k _ _ (big_ring k) _ mv_polynomial.C _ (mv_polynomial.X p) p.1}

```
breaks it again -- apparently explictly telling Lean to use `big_ring k` rather than letting it work it out for itself is a bad idea. @**Mario Carneiro** what is going on here?

#### [Kevin Buzzard (Sep 16 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050855):
Adding `instance : is_semiring_hom (mv_polynomial.C : k → big_ring k) := by apply_instance ` speeds Kenny's original code up a bit.

