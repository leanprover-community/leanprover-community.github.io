---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59614VMdoesnothavecodeformultisetstronginductionon.html
---

## [general](index.html)
### [VM does not have code for 'multiset.strong_induction_on'](59614VMdoesnothavecodeformultisetstronginductionon.html)

#### [Kevin Buzzard (Jul 08 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129309672):
What's happening here? I'm defining a map from `multiset nat` to `nat` :

```lean
import data.multiset

#check @multiset.strong_induction_on 

/-
multiset.strong_induction_on :
  Π {α : Type u_1} {p : multiset α → Sort u_2} (s : multiset α),
    (Π (s : multiset α), (Π (t : multiset α), t < s → p t) → p s) → p s
-/

definition f (s : multiset ℕ) : ℕ := 
  multiset.strong_induction_on s (λ s' H,0)

#eval f {1,2,3} 
```

but the `#eval` fails with 

```
code generation failed, VM does not have code for 'multiset.strong_induction_on'
```

I must be honest, I don't really know what a virtual machine is. I don't really see an obstruction to evaluating the function, however I can see that there might be issues with dealing with the quotient type. Can't the VM just assume everything is well-defined on equivalence classes and have a punt? Or is the issue elsewhere?

#### [Andrew Ashworth (Jul 08 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129309806):
does `#reduce` produce the same error message?

#### [Mario Carneiro (Jul 08 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129309871):
`multiset.strong_induction_on` should not have been marked a `lemma` instead of a `def`

#### [Mario Carneiro (Jul 08 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129309913):
because it produces elements of type `p s : Sort*`

#### [Kevin Buzzard (Jul 08 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129309917):
Oh! :-)

#### [Kevin Buzzard (Jul 08 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129309929):
I should really add this to my list of "basic checks when something isn't working". I've been caught out in the past myself writing `have` instead of `let` and then wondering why something won't unfold.

#### [Mario Carneiro (Jul 08 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129310102):
This is a different issue. The VM constructs code for all definitions that are not `noncomputable`; this is what enables the use of `#eval` to run functions. But `lemma` and `theorem` definitions do not have code generated, which is usually okay since these are usually propositions which do not have any computational content anyway, but it causes problems if data is marked like this

#### [Mario Carneiro (Jul 08 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM does not have code for 'multiset.strong_induction_on'/near/129310119):
This can cause issues even if you don't use `#eval` at all:
```
lemma A : nat := 42
def B : nat := A
-- failed to generate bytecode for 'B'
-- code generation failed, VM does not have code for 'A'
```

