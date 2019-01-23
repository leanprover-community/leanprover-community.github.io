---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29013TopologyBeginner.html
---

## Stream: [maths](index.html)
### Topic: [Topology - Beginner](29013TopologyBeginner.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129159440):
Hello, I am a beginner and I am trying to define a path (in particular a path from `x` to `y` on a topological space).
I am sorry for the (temporary) maths notation of topological spaces and definitions.
Not knowing the syntax/ best way to impose the conditions  for the continuous function (f : I = [0,1] --> X)  to be a path I thought of having a product ```lean X  × (I → X) ×  Prop ``` as output. 

This is my code: 

```lean
import analysis.topology.continuity
import analysis.topology.topological_space
import analysis.topology.infinite_sum
import analysis.topology.topological_structures
import analysis.topology.uniform_space

open set filter lattice classical
universe u

-- ambient space 
variable {X : Type*}
#check X 
------ variable x : X

-- topological space (X, T)
variable T : topological_space X 

-- Interval [0, 1]
definition I : set ℝ := λ x, x ≤ 1 ∧ x ≥ 0  
#check I 

variable E : topological_space ℝ

-- Define inclusion map 
definition i (x: I) : ℝ  := x 

-- Define subspace topology [for Euclidean subspace topology?]
def S : topological_space I := 
topological_space.induced  i E 

-- PATH
variable f : I → X

def path_topological2  {x : X} {y : X} (t : I) : X  × (I → X) ×  Prop := 
λ t, ( f t ) × f × (continuous f ∧ f 0 = x ∧ f 1 = y)             

/-   type mismatch at application
  prod (f t)
term
  f t
has type
  X : Type u_1
but is expected to have type
  Type ? : Type (?+1)  -/ 

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129159458):
What would be the best way to define a path? Also avoiding the ** type mismatch ** that arises in the definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 05 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129160116):
I don't understand what you are trying to do. But you could have a look at `data/sets/intervals` in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 05 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129160140):
But actually it may be better to have path as a structure bundling a map from reals to X and the condition that it is continuous on [0, 1].

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129161964):
```quote
But actually it may be better to have path as a structure bundling a map from reals to X and the condition that it is continuous on [0, 1].
```
I was not too sure whether use create as a structure or create a definition (later I would like define homotopy;  so I was thinking that (ideally) my definition of path would allow me to retrieve starting/ending points and the actual path (function f : I --> X): this for possible re-parameterisations ( I --> I ) )

I know very little about structure, but I may try to look into your suggestion. Many Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129162181):
```quote
I don't understand what you are trying to do. But you could have a look at `data/sets/intervals` in mathlib
```
PS: Are you referring to the part before the definition or the definition itself? 
I included the code before definition  just to provide more information on the interval I (and the induced  subspace topology - which is meant to be induced from Euclidean topology on R ) and the topological space X of interest.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 06 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129185328):
A path is just a continuous function `I \to X`, right? Or do you want a Type for paths from `x` to `y`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129186563):
It looks like he wants the end points to be parameters of the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187672):
Hey Luca. So just to comment that `set ℝ` is a type so `I` is "only" a term. So when you make `topological_space I` something magic is happening: the term is being somehow promoted to a type. What's happening is that the term `  {x : ℝ | x ≤ 1 ∧ x ≥ 0}`(which is really a function) is being interpreted as the type `{x : ℝ // x ≤ 1 ∧ x ≥ 0}` implicitly (and this is a so-called subtype).  So when you write `t : I` then `t` might not be what you think it is -- it's a term of the subtype, so it has a value `t.val` which is the real number, and then a proof too, called `t.property`.

The type mismatch is because `\times`, the little cross, is for making types, not terms; a term of type `α × β` looks like `(a,b)`, like in maths.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 06 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187690):



```quote
A path is just a continuous function `I \to X`, right? Or do you want a Type for paths from `x` to `y`?
```
Indeed, I would like the second one (a Type for paths from `x` to `y`) :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187750):
So you could build the type using a structure. You would have to decide whether to put things like `X` and `x` and `y` inside the structure or outside; this is the sort of question that I am terrible at.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187876):
So it could look like
```lean
structure paths (X : Type) [topological_space X] (x y : X) :=
(f : I \to X)...
```
or
```lean
structure paths (X : Type) [topological_space X] :=
(start_point : X)
(end_point : X)
(f : I \to X)...
```
or
```lean
structure paths :=
(X : Type)
(HX : topological_space X)
(start_point : X)
...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187887):
In this case you definitely want `x` and `y` outside the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187895):
Why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187906):
> a Type for paths from `x` to `y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187913):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187916):
```quote
Hey Luca. So just to comment that `set ℝ` is a type so `I` is "only" a term. So when you make `topological_space I` something magic is happening: the term is being somehow promoted to a type. What's happening is that the term `  {x : ℝ | x ≤ 1 ∧ x ≥ 0}`(which is really a function) is being interpreted as the type `{x : ℝ // x ≤ 1 ∧ x ≥ 0}` implicitly (and this is a so-called subtype).  So when you write `t : I` then `t` might not be what you think it is -- it's a term of the subtype, so it has a value `t.val` which is the real number, and then a proof too, called `t.property`.

The type mismatch is because `\times`, the little cross, is for making types, not terms; a term of type `α × β` looks like `(a,b)`, like in maths.
```
Thank you! I am in the process of digesting this...  I will try with the structure :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187924):
and Mario is saying that you want the first of my three options above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129187976):
I suspect that you might want to make `I`, the unit interval, into a subtype. If you don't then you'll have coercions everywhere. You'd perhaps be better off having the coercion from `I` to the reals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188095):
There is also the option of having the path "defined" on R but only use its values and continuity on I

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188102):
Minimal version would be:
```lean
import analysis.real

open filter

variables {X : Type*} [topological_space X] (x y : X)

structure path :=
(map : ℝ → X)
(start_pt : map 0 = x)
(end_pt : map 1 = y)
(cont : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → tendsto map (nhds t) (nhds (map t)))

instance : has_coe_to_fun (path x y) :=
⟨_, λ p, p.map⟩

example (f : path x y) : f 1 = y :=
f.end_pt
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188404):
Here's my suggestion:
```lean
def I01 := {x : ℝ // 0 ≤ x ∧ x ≤ 1}

instance : topological_space I01 := by unfold I01; apply_instance
instance : has_zero I01 := ⟨⟨0, le_refl _, zero_le_one⟩⟩
instance : has_one I01 := ⟨⟨1, zero_le_one, le_refl _⟩⟩

structure path {α} [topological_space α] (x y : α) :=
(to_fun : I01 → α)
(at_zero : to_fun 0 = x)
(at_one : to_fun 1 = y)
(cont : continuous to_fun)

instance {α} [topological_space α] (x y : α) : has_coe_to_fun (path x y) := ⟨_, path.to_fun⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188438):
@**Luca Gerolla** Patrick's suggestion is an interesting one. It's a very "non-maths" way to think about things, but sometimes in computer science this seems to be the way it's done. Note that `cont` is an explicit proof that the map is continuous (using things called filters, which is a trick to enable you to talk about things tending to other things even when there's no metric). Note also that there's a trick with variables here -- this really says `structure path {X : Type} [topological_space X] (x y : X) :=...` Note also that there is a problem with equality here -- you can have two different terms of type `path x y` which are not literally equal but which are "the same path" because the maps are different but agree on $$[0,1]$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188441):
I think that in this case it is best to build up the theory of the interval as a type in its own right rather than totalizing a la isabelle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188490):
Note again that mathlib does have a rudimentary theory of intervals (in totally ordered types).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188497):
Indeed you can prove that `I01` is compact in one line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188505):
I'm not saying my way is best, I only wanted to point it out because, as pointed out by Kevin, it's very unlikely a mathematician or math student beginning Lean would think of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188506):
Mario's version makes the interval a subtype, not a subset (so `I01` is a type), and the tricks beforehand with the instances make it a topological space and make it so you can talk about 0 and 1. His equality is equality of paths, however you are, I assume, not going to be interested in equality anyway, but homotopy equivalence, so you'll end up putting an equivalence relation on this structure anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188516):
The downside of Mario's version is it will be annoying to refer to any point in the interval, as seen in his definition of 0 and 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188567):
The solution to this is to define appropriate functions on `I01` so that you abstract away the proof stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188573):
For example you can probably get away with just a `has_mul` instance (the usual one) and a `has_neg` instance (the 1-x function)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188574):
If you are going for homotopy theory, there is a clear test case: prove that concatenation of homotopy classes of path is associative, using various modelisation choices.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188622):
Also 1/2 should be a point in [0,1]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188624):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188629):
from those I think you have enough to define everything else in homotopy theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188696):
Luca -- as far as I know nobody has done this sort of stuff in Lean, however it definitely looks possible to me and hopefully not too hard. I have to do admin today so I won't be hanging around in the computer room, but I will be in the department and will pop in occasionally. I think trying to define homotopy classes of paths etc would be a fabulous exercise for you or you/Rohan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188705):
It's not quite true: Johan tried it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188736):
https://github.com/leanprover/mathlib/pull/144

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188748):
this has some intersection with what Luca wants to try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188750):
Oh! Luca -- this is Johan Commelin. You might want to look at what he did (or you might want to figure it out yourself)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188752):
Thanks Patrick.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 06 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188758):
but it's geared towards homology, and biased towards abstraction (simplicial sets everywhere)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 06 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/129188888):
This is all very interesting, thank you very much everyone! :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 21 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051069):
Hello, I am trying to define a function (` f ` : X --> Y , where X and Y are topological spaces)  in terms of its restrictions; to then exploit the fact  later that if the restrictions of ``` f ```  (in this case fa : A --> Y, fb : B ---> Y - where A, B are closed ,  and they cover X) are continuous then the overall  function ``` f ```is continuous (theorem already proved by @**Kevin Buzzard**  ). 
Unfortunately I am struggling with set.inter and the coercions that "naturally" arise; in particular when I try to give a definition for the restrictions to match ` fun_match ` (i.e. fa = fb on ` A \and B  `) and to define f as fa on A and fb on B  `fun_pasting_closed `.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051111):
This is my code: 
```lean
--- Attempt to define function (f : α → β ) in terms of its restriction 
variables {X Y : Type} [topological_space X] 
[topological_space Y]
variable f : X → Y 
variables ( A : set X ) ( B : set X)
variables (ga : A → Y ) ( gb : B → Y )

definition restriction {X Y : Type} (f : X → Y) (A : set X) : A → Y :=
λ a, f a.val 


def fun_match {X Y : Type} [topological_space X] 
[topological_space Y] {A B : set X} [topological_space A] [topological_space B] ( fa : A → Y ) ( fb : B → Y ) : Prop :=
sorry
--∀ x ∈  set.inter A B, fa x = fb x 
--∀ x ∈ set.inter A B, fa x.val = fb x.val 
--restriction fa ( set.inter A B) == restriction fb ( set.inter A B) 
-- ∀ x, (restriction fa ( set.inter A B) ) x = (restriction fb ( set.inter A B) ) x 


def fun_match2 {A B : set X} [topological_space A] [topological_space B] {fa : A → Y} { fb : B → Y} 
( Ha : fa = restriction f A ) ( Hb : fb = restriction f B ) : Prop :=
sorry

def fun_pasting_closed {X Y : Type} [topological_space X] 
[topological_space Y] {A B : set X} ( fa : A → Y ) ( fb : B → Y) { HAcont : continuous fa} { HBcont : continuous fb} 
{Hunion : A ∪ B = set.univ} {HAclosed : is_closed A} {HBclosed : is_closed B} 
{Hmatch : fun_match fa fb } : X → Y := sorry
--- λ t : X, if H : t ∈ A  then fa t else fb t
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051195):
there are way too many topological space arguments in `fun_match`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 21 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051196):
Any help would be greatly appreciated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051245):
```
def fun_match {X Y} {A B : set X} (fa : A → Y) (fb : B → Y) : Prop :=
∀ x h₁ h₂, fa ⟨x, h₁⟩ = fb ⟨x, h₂⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051367):
```
local attribute [instance] classical.prop_decidable

noncomputable def paste {X Y} {A B : set X} (Hunion : A ∪ B = set.univ) (fa : A → Y) (fb : B → Y) (t : X) : Y :=
if h₁ : t ∈ A then fa ⟨t, h₁⟩ else
have t ∈ A ∪ B, from set.eq_univ_iff_forall.1 Hunion t,
have h₂ : t ∈ B, from this.resolve_left h₁,
fb ⟨t, h₂⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051387):
we don't really need topology to define these functions; it only comes in for the continuity proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051589):
Here's how you can prove it has the right values:
```
theorem paste_left {X Y} {A B : set X} (Hunion : A ∪ B = set.univ)
  (fa : A → Y) (fb : B → Y) (t : X) (h : t ∈ A) :
  paste Hunion fa fb t = fa ⟨t, h⟩ :=
dif_pos _

theorem paste_right {X Y} {A B : set X} (Hunion : A ∪ B = set.univ)
  (fa : A → Y) (fb : B → Y) (H : fun_match fa fb)
  (t : X) (h : t ∈ B) :
  paste Hunion fa fb t = fb ⟨t, h⟩ :=
by by_cases h' : t ∈ A; simp [paste, h']; apply H
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051606):
do we really want to use the name `fun_match`? It is really similar to the internally generated variable `_fun_match`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051616):
that's fair

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130051623):
mathlib uses `eq_on` for something very similar

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 23 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130141208):
Thank you very much @**Mario Carneiro** 
For the time being I renamed ` fun_match ` to ` match_of_fun `. 
With your code the theorem ` cont_of_paste ` followed easily using (part of ) the pasting lemma; however, since this was done in terms of ` restriction _ _ `, do you see an easy way to prove that the pasted ` fa `, `fb ` are indeed ` restriction f A `, ` restriction f B` respectively?  
```lean
lemma rest_of_paste {X : Type* } {Y : Type*} {A B : set X} {Hunion : A ∪ B = set.univ} (fa : A → Y) (fb : B → Y)
{ f : X → Y } ( Hf : f = paste Hunion fa fb ) : 
fa = restriction f A ∧ fb = restriction f B := 
begin split, 

sorry, 

sorry 
end 

-- prove continuity when pasted continuous restrictions on closed sets 
theorem cont_of_paste {X : Type* } {Y : Type*} [topological_space X] [topological_space Y]  
{ A B : set X } { Hunion : A ∪ B = set.univ} {fa : A → Y } { fb : B → Y }
{HAclosed : is_closed A} {HBclosed : is_closed B}  { Hmatch : match_of_fun fa fb }  
{ f : X → Y } ( Hf : f = paste Hunion fa fb ) : 
continuous fa → continuous fb → continuous f := 
begin 
intros Ca Cb,
have ResA : fa = (restriction f A) , exact (rest_of_paste fa fb Hf ).1, 
have ResB : fb = (restriction f B), exact (rest_of_paste fa fb Hf ).2, 
rw ResA at Ca, rw ResB at Cb, 
exact continuous_closed_union f Hunion HAclosed HBclosed Ca Cb
end 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 23 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130141517):
PS:  has ` cont_of_paste ` the right arguments?  Is  
```lean
{ f : X → Y } ( Hf : f = paste Hunion fa fb )
```
the best way to specify ` f ` as a paste? Asking this because I have employed a similiar method to specify arguments which were functions of certain properties/definitions, and don't know if this makes things unnecessarily more convoluted.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 23 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130170170):
If you want to prove two functions are equal, the `funext` tactic reduces you to checking their values are equal on every input. This might be what you need?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jul 24 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130182032):
@**Luca Gerolla** what about removing those two arguments and substituting `f` in directly? so your result would be `continuous (paste Hunion fa fb)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130200013):
```quote
If you want to prove two functions are equal, the `funext` tactic reduces you to checking their values are equal on every input. This might be what you need?
```
` funext ` does help, together with `rw ` and ` unfold ` leads to much more progress. Here is my "nearly completed" proof: 
```lean
lemma rest_of_paste {X : Type* } {Y : Type*} {A B : set X} {Hunion : A ∪ B = set.univ} (fa : A → Y) (fb : B → Y)
{ f : X → Y } ( Hf : f = paste Hunion fa fb ) : 
fa = restriction f A ∧ fb = restriction f B := 
begin split, 
  funext, unfold restriction, rw Hf, unfold paste, rw dif_pos, -- exact subtype.rec fa, exact subtype.rec_on, 
  have H :  x.val = (⟨ x.val, _ ⟩ : A ).val ,  trivial, 
  have H1 : x = ⟨x.val, _ ⟩,  exact subtype.eq ( H ), exact x.2, --rw H1, 
  sorry,  exact x.2, 
sorry 
end 
```
Is there a way to prove ` fa x = fa ⟨x.val, ?m_1⟩ `?  (I thought the `have`s should do the job but then `rw H1` fails )

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130200168):
have you tried `simp` or `rw subtype.eta x.1 x.2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130200179):
`cases x` will make this a lot easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130200222):
Yes, simp does work! Thank you Chris, very silly of me not trying it.. sorry!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130201370):
```lean
lemma rest_of_paste {X : Type* } {Y : Type*} {A B : set X} {Hunion : A ∪ B = set.univ} (fa : A → Y) (fb : B → Y)
{ f : X → Y } (H : match_of_fun fa fb) ( Hf : f = paste Hunion fa fb )  : 
fa = restriction f A ∧ fb = restriction f B := 
begin split, 
  funext, unfold restriction, rw Hf,  
  apply eq.symm _, simp [paste_left Hunion fa fb x.val x.2], 
  funext, unfold restriction, rw Hf, 
  apply eq.symm _, simp [paste_right Hunion fa fb H x.val x.2],  
end 
```
Needed also the H hypotheses to complete the proof for `fb` , then `paste_**` simplified the proof further  :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 24 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130201385):
@**Nicholas Scheel** do you mean to  rewrite the statement as 
```lean
theorem cont_of_paste {X : Type* } {Y : Type*} [topological_space X] [topological_space Y]
{ A B : set X } { Hunion : A ∪ B = set.univ} {fa : A → Y } { fb : B → Y }
{HAclosed : is_closed A} {HBclosed : is_closed B}  { Hmatch : match_of_fun fa fb }
( CA : continuous fa ) ( CB : continuous fb)  : continuous (paste Hunion fa fb) := ... 
```
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 24 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130204505):
```quote
Is there a way to prove ` fa x = fa ⟨x.val, ?m_1⟩ `?  (I thought the `have`s should do the job but then `rw H1` fails )
```
Luca I mentioned this in my talk yesterday. The problem here is that x is `\<x.val,x.property\>` but you're trying to compare `x` with `\<x.val,h\>` for `h` some (un-named, that's why it says ?m_1) other proof of the thing that `x.property` is a proof of. Because these are both proofs of the same thing, they're definitionally equal by definition, so actually `x = ⟨x.val, ?m_1⟩` . Take a look at theorems like `subtype.eq` and `subtype.eta` to see the various tricks that can be used, but remember  that `simp` will know all the important ones.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 24 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130204515):
the easy proof is `cases x, refl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 24 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130204566):
I usually do cases on a variable like this before proofs, because everything becomes definitionally true that way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jul 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130220203):
@**Luca Gerolla** yes that’s what I meant, but it‘s not a big deal either way – looks like you’re making progress on it already :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130245778):
So I am a bit confused as to why typeclass inference doesn't put a topology on the subtype of a topological space. Here's some non-pasteable code:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130245786):
```lean
#check Spv.is_continuous -- Spv.is_continuous : Spv ?M_1 → Prop

def Cont (R : Type) [comm_ring R] [topological_space R] [topological_ring R]
  := {vs : Spv R // Spv.is_continuous vs}

example (R : Type) [comm_ring R] [topological_space R] [topological_ring R] :
topological_space (Spv R) := by apply_instance -- works

--example (R : Type) [comm_ring R] [topological_space R] [topological_ring R] :
--topological_space (Cont R) := by apply_instance -- fails

instance (R : Type) [comm_ring R] [topological_space R] [topological_ring R] :
topological_space (Cont R) := subtype.topological_space

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130245821):
`Spv R` is a topological space, and type class inference knows this. I then make a subtype, and even though `subtype.topological_space` is marked as an instance, type class inference doesn't seem to work. Is this to do with `topological_space` being a structure with the class attribute rather than a class?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130245882):
```lean
import analysis.topology.topological_space

example (X : Type) [topological_space X] (p : X → Prop) : 
topological_space {x : X // p x} := by apply_instance 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130245885):
My MWE works :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 25 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130246071):
It can infer a topological space structure on `{vs : Spv R // Spv.is_continuous vs}` but not if you give it a different names.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 25 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130246074):
because type class inference looks at the `expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130246087):
So am I OK to make the instance like I did?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130246091):
I don't want to make diamonds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 25 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130246138):
Don't see why not. It's a defeq diamond, and it's not even a diamond really because there's only one path it will choose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130246147):
Thanks Chris.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 25 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130259969):
You will notice the pattern `by unfold foo; apply_instance` used for this sort of situation (although an alternative is to do the first step of instance work yourself, as you did)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130262773):
I think I prefer your solution -- it sounds safer. I hadn't really internalised this type class inference fact though -- so it's picky about defeq like `rw`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130262843):
yes, it only unfolds `reducible` definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 25 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130262867):
This is a good thing, because it means you can attach different typeclasses to defeq things, like `with_top A = with_bot A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 25 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130262892):
So naming a def is a way of controlling what typeclasses you want to inherit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130262934):
I guess it sometimes makes sense to make definitions reducible. What do you think about `Cont`? Might that be a case where `reducible` makes sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 25 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130262943):
I find that it is almost never a good idea to mark a definition `reducible`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130263136):
You make it reducible and any goal with `Cont` in just gets unfolded and looks more unreadable. I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130263163):
Yes, so let's not do that. After all, `unfold`ing isn't very hard to do, if we need it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413232):
Hello, has it been proved anywhere that a closed interval  [r, s]  is indeed closed?
 I am stuck proving that a subset  ` T r s Hrs `( closed subinterval [r,s] ) of  ` I01 ` ( unit interval [0, 1] ) is closed 
```lean
-- May be needed / useful for Guillermo - Heine-Borel Thm
theorem is_closed_int { r s : ℝ } ( Hrs : r < s ) : is_closed (int_clos Hrs) := 
begin sorry end 


lemma T_is_closed  { r s : ℝ } ( Hrs : r < s ): is_closed (T r s Hrs) := 
begin unfold T,  
    exact is_closed_iff_nhds.2 
        (begin intros a H , --by_contradiction,  

        sorry ,
    end), 
end 

lemma T_is_closed2  { r s : ℝ } ( Hrs : r < s ): is_closed (T r s Hrs) :=  
begin unfold T, 
-- Write in terms of intersection with I01 (i.e. T r s Hrs =  I01 ∧  closed_int Hrs), resolving subset nesting problem 
    -- Prove auxilliary lemma that (closed_int Hrs) is indeed closed 
        -- Use is_closed_inter to prove this lemma  
--have Int : {x : ↥I01 | r ≤ x.val ∧ x.val ≤ s} = set.inter univ  (closed_int Hrs) , 
sorry, 
end 
```

With the underlying definitions 
```lean
def I01 := {x : ℝ | 0 ≤ x ∧ x ≤ 1}

definition T ( a b : ℝ ) ( Hab : a < b ) : set I01 :=  { x : I01 | a ≤ x.val ∧ x.val ≤ b }

def int_clos { r s : ℝ } ( Hrs : r < s ) : set ℝ := {x : ℝ  | r ≤ x ∧ x ≤ s}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413243):
it's even compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413266):
```quote
it's even compact
```
Indeed! :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413279):
what I mean is it's even proved that it is compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413304):
Check out the stuff around `ordered_topology` in `analysis.topology.topological_structures`, such as `is_closed_le`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413315):
Oh, haven't thought to approach it from compactness..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130413384):
that isn't what I mean either, what I mean is that we even proved that it is compact, so I would expect it to be proved that it is closed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130414100):
Luca -- what Kenny means is "the answer to your first question is almost certainly yes". Here are some things which should be in mathlib *somewhere* : (1) interval [r,s] as a subspace of [0,1] with subspace topology will be closed in [0,1] if it is closed in R (2) interval [r,s] is closed in R. Reid is suggesting some places in mathlib where you might well find the theorems you want.

As a rule of thumb, when you are working on "high level" stuff like this, your first instinct should be to look in the library to see what is there. I know it sometimes feels a bit daunting but you could do worse than looking at a whole bunch of those topology files and looking through them. They are often long and complex, and written by experts so the proofs are often incomprehensible. But the trick is to find such a file, then to scan over it once and try and find the *definitions*, and see if you can figure out what they are supposed to be (because they are kind of like notation -- they are the language the file is written in, in some sense) and then scan over it again and try and find the *statements of the main theorems*.  Some clues as to whether a theorem is a "main theorem" -- it might be called "theorem" rather than "lemma", it might have a docstring (a comment starting with `/-- ... -/` -- note two dashes not one), or it might have a long proof. *DO NOT TRY TO READ ANY LONG PROOFS!*. You will get depressed and it will all seem much harder. If you find that you simply cannot understand a file because e.g. the definitions are constantly using things you've not heard of, then perhaps you started too late; look at the files which are imported at the very top and try reading one of those instead. Remember also that if a file compiles perfectly then you should be able to hover over anything and see its definition, or right click on it and see it in context. 

I remember finding the files where rationals and reals were defined very intimidating to read, but that was before I started picking up some of the tricks I mention above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130415106):
`is_closed_Icc`
https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_structures.lean#L282-L283

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130415280):
mathlib doesn't really use `theorem` vs `lemma` distinction (or at least I don't like to make this distinction)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130415388):
I'm not sure it's worth focusing on "important theorems" either when reading mathlib files - you will usually be interested in easy theorems anyway. `is_closed_Icc` is an easy theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130415529):
```quote
Check out the stuff around `ordered_topology` in `analysis.topology.topological_structures`, such as `is_closed_le`
```
Thank you very much, `is_closed_le' ` and  `is_closed_ge'  allowed me to prove [r, s] is closed without getting to use nhds and filters!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Jul 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Topology%20-%20Beginner/near/130415717):
`is_closed_Icc ` would have made it even quicker! (should have updated my mathlib to notice it!)  :)


{% endraw %}
