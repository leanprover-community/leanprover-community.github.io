---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75934Conflictingtransitivecoercions.html
---

## Stream: [general](index.html)
### Topic: [Conflicting transitive coercions?](75934Conflictingtransitivecoercions.html)

---


{% raw %}
#### [ Nicholas Scheel (May 26 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127117518):
I have two terms that pretty-print the same but won't be considered equivalent because they seem to use slightly different coerce instances:
```
invalid type ascription, term has type
  @eq int
    ((@coe nat Zalpha
        (@coe_to_lift nat Zalpha (@coe_trans nat int Zalpha int.has_coe (@coe_base int Zalpha Zalpha.has_coe)))
        (fib (@has_add.add nat nat.has_add m 1))).r)
    0
but is expected to have type
  @eq int
    ((@coe nat Zalpha
        (@coe_to_lift nat Zalpha
           (@coe_base nat Zalpha (@nat.cast_coe Zalpha Zalpha.has_zero Zalpha.has_one Zalpha.has_add)))
        (fib (@has_add.add nat nat.has_add m 1))).r)
    0
```
(part of Kevin's project: https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/Zalpha.lean)
I'm giving up for tonight, but do you have any suggestions on how this could be resolved or avoided?

#### [ Kevin Buzzard (May 26 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127120917):
Polynomials: I think you have to avoid the general multivariate code because there is a whole bunch of theory specific to the one variable case. You can have a coercion to the multivariable case and prove it's injective and then you get some theorems for free

#### [ Kevin Buzzard (May 26 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127120965):
Coercions -- these are unfortunately one of the dark arts as far as mathematicians are concerned. You can't set it up the way we do it -- coercions and partial coercions invoked in all directions often without remark. Welcome to type theory. Your coercions I think in general all have to go in one direction, and if you coerce from X to Y and from Y to Z and from X to Z independently then the two maps X -> Z have to be *definitionally* equal or the entire system breaks.

#### [ Kevin Buzzard (May 26 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121012):
This leads to non-trivial problems with the entire system -- for example if you want to coerce a metric space into a topological space then this sounds harmless on the face of it, but if you want the product of metric spaces to be a metric space and the product of topological spaces to be a topological space then you are going to have to think hard whether the two induced topological structures on the product of two metric spaces are definitionally equal, and probably for the way you naively just set it up in your head the answer is "they are equal, but it's a theorem not a definition", which is not good enough.

#### [ Kevin Buzzard (May 26 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121071):
This whole thing falls into a general category of "easy in maths, hard in Lean" concepts which I think are extremely important to (a) isolate and (b) work around, because I believe that Lean should not just offer "what it is" to mathematicians, it should attempt to do the much harder job of offering Lean "what mathematicians do, the way they do it".

#### [ Mario Carneiro (May 26 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121114):
What is `Zalpha.has_coe`?

#### [ Mario Carneiro (May 26 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121118):
Looks like there are two coercions there, and there is a needed theorem to show they are the same

#### [ Mario Carneiro (May 26 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121128):
I wouldn't go so far as to say that all coercion chains have to be defeq, but you should have a theorem proving they are equal as a simp lemma to clean these kind of things up

#### [ Mario Carneiro (May 26 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121191):
From what I can see, there are two paths: you have a defined coercion `int -> Zalpha` which is composed with the natural map `nat -> int`, and then also there is a coercion `nat -> Zalpha` because `Zalpha` is a ring or ringlike thing

#### [ Mario Carneiro (May 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121241):
You can use `nat.eq_cast` to prove that they are equal

#### [ Kevin Buzzard (May 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121352):
Are they not defeq, and is this a problem?

#### [ Mario Carneiro (May 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121355):
They aren't even proven equal

#### [ Mario Carneiro (May 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121357):
there is a missing theorem here

#### [ Mario Carneiro (May 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121368):
I think you should remove `instance : has_coe ℤ ℤα := ⟨of_int⟩`, and then after proving it's a ring you should prove `of_int z = z`

#### [ Mario Carneiro (May 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121370):
where the right `z` is being coerced using the cast function

#### [ Mario Carneiro (May 26 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121460):
compare with how `rat.of_int` is handled in `rat.lean`

#### [ Nicholas Scheel (May 26 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127132931):
til `unfold_coes`

#### [ Nicholas Scheel (May 26 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127133498):
Thanks for the advice @**Mario Carneiro**! It seems to be working much much better :)

#### [ Nicholas Scheel (May 26 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127133604):
I guess when they write "canonical" in
> Canonical homomorphism from the integers to any ring(-like) structure `α`

They really mean *canonical* – don't use anything else!


{% endraw %}
