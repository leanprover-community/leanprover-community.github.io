---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/81809classinstanceresdepthreachedfintypeclassicalsome.html
---

## Stream: [new members](index.html)
### Topic: ["class-instance res. depth reached" fintype + classical.some](81809classinstanceresdepthreachedfintypeclassicalsome.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 29 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871036):
Hi guys, I am trying to model ssreflects 'pick' method using classical.some. The code I came up with reads:

```lean
import data.set.finite
import ring_theory.matrix

universes u v

def vec (m : Type u) [fintype m] (α : Type v) : Type (max u v) :=
m → α 

local attribute classical.prop_decidable
set_option class.instance_max_depth 60
-- set_option trace.class_instances true

noncomputable def get_sample_or_zero (α : Type) [ordered_ring α] [decidable_eq α] [has_zero α]: Π (m), vec (fin m) α  → α
| m V := 
  let S := { i  | V i = 0 } in
  if h : ∃ x, x ∈ S
    then classical.some h
    else (0 : α)
```

but triggers a "maximum class-instance resolution depth has been reached". Any pointers what could go wrong here?

#### [ Simon Hudon (Sep 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871101):
Try removing `has_zero`. It should be implied by the ordered ring.

#### [ Simon Hudon (Sep 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871141):
This is the kind of problem that arises when your instances overlap in conflicting ways

#### [ Tobias Grosser (Sep 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871197):
Thanks @**Simon Hudon** , unfortunately this does not help.

#### [ Tobias Grosser (Sep 29 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871251):
Still the same error
Dropping the ordered_ring instead also does not help.

#### [ Tobias Grosser (Sep 29 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871252):
I can also drop the matrix import, this does not change anything either.

#### [ Simon Hudon (Sep 29 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871307):
I think you should need anything beside `has_zero` actually.

#### [ Simon Hudon (Sep 29 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871347):
Is it important that the default value be `0`? If not, you can replace the `if` with `classical.epsilon S`.

#### [ Mario Carneiro (Sep 29 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871348):
```
local attribute classical.prop_decidable
```
since when is this valid syntax?

#### [ Mario Carneiro (Sep 29 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871355):
oh wait, now I see... this doesn't do anything

#### [ Mario Carneiro (Sep 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871395):
you want `local attribute [instance] classical.prop_decidable`

#### [ Mario Carneiro (Sep 29 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871454):
I don't think you need classical anything for this definition, if I read it correctly

#### [ Simon Hudon (Sep 29 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871499):
You can do without classical reasoning but you need to implement a search

#### [ Mario Carneiro (Sep 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871527):
Also the `then` part is not type correct
```
import data.set.finite data.equiv.encodable

def get_sample_or_zero (α : Type) [decidable_eq α] [has_zero α] : Π (m), vec (fin m) α  → α
| m V := if h : ∃ i, V i = 0 then V (encodable.choose h) else 0
```

#### [ Mario Carneiro (Sep 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871530):
note the `V` in the middle

#### [ Mario Carneiro (Sep 29 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871576):
then again, this function is always 0, so maybe that's not what you meant

#### [ Mario Carneiro (Sep 29 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871588):
but if this returns a `fin m` then you have a problem since `0 : fin m` only holds if `m>0`

#### [ Mario Carneiro (Sep 29 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871701):
wasn't ssreflect's pick function something like this?
```
noncomputable def pick (α : Type*) : option α :=
by haveI := classical.dec (nonempty α); exact
if h : nonempty α then some (classical.choice h) else none
```

#### [ Tobias Grosser (Sep 29 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871708):
SSReflects pick is: "[pick x in A] == Some x, with x \in A, or None if A is empty. "

#### [ Tobias Grosser (Sep 29 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871709):
Here the definition: http://ssr.msr-inria.inria.fr/doc/ssreflect-1.5/Ssreflect.fintype.html

#### [ Mario Carneiro (Sep 29 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871756):
right, isn't that what I wrote?

#### [ Tobias Grosser (Sep 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871758):
Honestly, I need some more time to think about these solutions.

#### [ Tobias Grosser (Sep 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871804):
I mostly was concerned about the then path and therefore just returned zero in the else.

#### [ Mario Carneiro (Sep 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871810):
Maybe `A` is a subset of a type instead of just a type; in that case you have
```
noncomputable def pick {α} (p : α → Prop) : option α :=
by haveI := classical.dec (∃ a, p a); exact
if h : ∃ a, p a then some (classical.some h) else none
```

#### [ Tobias Grosser (Sep 29 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871856):
To give some context, what I actually want to write is:
```coq
Fixpoint Gaussian_elimination {m n} : 'M_(m, n) → 'M_m × 'M_n × nat :=
  match m, n with
  | _.+1, _.+1 ⇒ fun A : 'M_(1 + _, 1 + _) ⇒
    if [pick ij | A ij.1 ij.2 != 0] is Some (i, j) then
      let a := A i j in let A1 := xrow i 0 (xcol j 0 A) in
      let u := ursubmx A1 in let v := a^-1 *: dlsubmx A1 in
      let: (L, U, r) := Gaussian_elimination (drsubmx A1 - v ×m u) in
      (xrow i 0 (block_mx 1 0 v L), xcol j 0 (block_mx a%:M u 0 U), r.+1)
    else (1%:M, 1%:M, 0%N)
  | _, _ ⇒ fun _ ⇒ (1%:M, 1%:M, 0%N)
  end.
```

#### [ Tobias Grosser (Sep 29 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871864):
I am just taking baby steps, to learn these different things.

#### [ Tobias Grosser (Sep 29 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871874):
Will get back to try to play with your pick function and see how it can be used here.

#### [ Tobias Grosser (Sep 29 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871875):
Thanks for the pointers.

#### [ Mario Carneiro (Sep 29 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871976):
Maybe the nicest interface for that pick match is something like this:
```
@[elab_as_eliminator]
noncomputable def {u} classical.exists_cases (p : α → Prop) {C : Sort u} (H0 : C) (H : ∀ a, p a → C) : C :=
if h : ∃ a, p a then H (classical.some h) (classical.some_spec h) else H0
```

#### [ Mario Carneiro (Sep 29 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872035):
In your context it would be something like `classical.exists_cases (λ ij, A ij.1 ij.2 ≠ 0) (1, 1, 0) $ λ ⟨i, j⟩, ...`

#### [ Tobias Grosser (Sep 29 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872038):
OK. Even more things to try to integrate.

#### [ Tobias Grosser (Sep 29 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872058):
One last question. In the end I want a gaussian elimination which can compute solutions.

#### [ Tobias Grosser (Sep 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872104):
Am I on a wrong track here? Aka, can this evolve to something computable eventually?

#### [ Simon Hudon (Sep 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872106):
Then you're going to need to specialize that function so that you can implement it using a search function.

#### [ Mario Carneiro (Sep 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872108):
Not using the function I just gave you

#### [ Mario Carneiro (Sep 29 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872120):
You want to use `encodable.choose` to do choicy stuff decidably

#### [ Tobias Grosser (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872133):
What exactly is the difference.

#### [ Mario Carneiro (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872179):
Basically any function with `classical` in the name will not be computable, even if the inputs are

#### [ Tobias Grosser (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872180):
ssreflect seems to be a hybrid of both.

#### [ Tobias Grosser (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872183):
That's what I know.

#### [ Mario Carneiro (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872187):
`ssreflect` essentially embeds `encodable.choose` very low in their algebraic hierarchy

#### [ Tobias Grosser (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872194):
I see. So the counterpart in lean would be a "pick based on 'encodable.choose'?"

#### [ Mario Carneiro (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872195):
yes

#### [ Tobias Grosser (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872196):
I see.

#### [ Tobias Grosser (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872203):
Can I also get the nice { (i j) | ... } interface for such a pick?

#### [ Mario Carneiro (Sep 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872244):
You can pattern match on `i, j` in the then branch

#### [ Mario Carneiro (Sep 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872247):
like at the end of my example `λ ⟨i, j⟩, ...`

#### [ Tobias Grosser (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872260):
OK.

#### [ Mario Carneiro (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872262):
I think `[pick ij | A ij.1 ij.2 != 0]` is some composite notation which is basically `pick (λ ij, A ij.1 ij.2 != 0)`

#### [ Tobias Grosser (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872263):
But your example uses classical.choice

#### [ Mario Carneiro (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872270):
You can swap out `classical.some` with `encodable.choose` for great good

#### [ Tobias Grosser (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872271):
I see.

#### [ Tobias Grosser (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872312):
I think that's all I need. I will put the things together myself!

#### [ Tobias Grosser (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872314):
Thanks a lot.

#### [ Mario Carneiro (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872321):
We don't have a "choice type" typeclass like ssreflect, so it's one or the other here

#### [ Mario Carneiro (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872332):
but fin n is encodable so it's all good

#### [ Tobias Grosser (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872334):
:D

#### [ Tobias Grosser (Sep 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134896880):
Just to report back. I use for now the function:

```lean
def pick_encodable (α : Type) (p : α → Prop) [decidable_pred p]:
Π (m n), matrix (fin m) (fin n) α → option(fin m × fin n)
| x y V :=
  if h : ∃ (ij : fin x × fin y), p (V ij.1 ij.2)
    then let idx := encodable.choose h in
      some idx
    else
      none 
```

#### [ Tobias Grosser (Sep 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134896882):
This probably needs some more cleanup, but or now it does what I want.


{% endraw %}
