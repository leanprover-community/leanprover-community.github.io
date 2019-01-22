---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62892WhatsnewinLeanmaths.html
---

## [maths](index.html)
### [What's new in Lean maths?](62892WhatsnewinLeanmaths.html)

#### [Kevin Buzzard (Sep 09 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133605485):
This thread is for people to occasionally announce or flag code which they or others have written, which is publically available, finished / usable, and which might be of general use or interest to the lean community. I'm starting it because I find looking through mathlib commits confusing and time-consuming, and because there are things which are happening other than mathlib commits.

#### [Kevin Buzzard (Sep 09 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133605676):
@**Chris Hughes** has proved quadratic reciprocity! This is a bit of a milestone because all proofs have some sort of a combinatorial / counting nature to them, and manipulating finite sets, whilst second nature to mathematicians, can be quite tough in Lean. The PR is still open; it's https://github.com/leanprover/mathlib/pull/327 . There's a bunch of other stuff too -- Fermat's Little Theorem, Wilson's Theorem, the Legendre symbol of course, multiplicative group of a finite field is cyclic and so on. This PR covers a serious chunk of the third year basic number theory course at Imperial College London.

#### [Kevin Buzzard (Sep 09 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133605778):
On a rather more mundane note, work of several people at https://github.com/leanprover/mathlib/commit/4421f46dc2e0ec818344bcd897c1ee75ff82cbad and https://github.com/leanprover/mathlib/commit/085c0125015c29058ce5a418e88a791cb232ee4b has given us the fact that submodules of the quotient module `M/N`biject with submodules of `M` containing `N` and we now also have basic definitions of Noetherian modules plus proofs that submodules and quotient modules of Noetherian modules are Noetherian.

#### [Johannes Hölzl (Sep 09 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133606251):
* `rcases` (and hence `rintros`) supports now also quotient types. This allows one to write `by rintro ⟨a⟩ ⟨b⟩; exact ...` instead of a sequence of `quotient.induction_on`
* (small change) more uniform naming `filter.vmap` is now `filter.comap`
* we have our first concrete categories in Lean: `CommRing`, `Top`, and `Meas`! Due to @**Scott Morrison** and @**Reid Barton**

#### [Patrick Massot (Sep 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133620485):
I think this thread is a very good idea. But we shouldn't forget to update documentation as well. Do we have an example of `rcases` using quotients in the tactic doc? I guess the quadratic reciprocity stuff should be mentioned in the theories folder of documentation

#### [Patrick Massot (Sep 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133620495):
It seems https://github.com/leanprover/mathlib/blob/master/docs/tactics.md mentions quotients but there are not so many examples there

#### [Mario Carneiro (Sep 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625180):
```lean
/-- `filter [t1, ⋯, tn]` replaces a goal of the form `s ∈ f.sets`
and terms `h1 : t1 ∈ f.sets, ⋯, tn ∈ f.sets` with `∀x, x ∈ t1 → ⋯ → x ∈ tn → x ∈ s`.

`filter [t1, ⋯, tn] e` is a short form for `{ filter [t1, ⋯, tn], exact e }`.
-/
meta def filter_upwards
  (s : parse types.pexpr_list)
  (e' : parse $ optional types.texpr) : tactic unit
```
Since when did we have the `near` tactic?

#### [Patrick Massot (Sep 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625225):
I was about to try to find this

#### [Patrick Massot (Sep 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625233):
But I was never able to use it :(

#### [Mario Carneiro (Sep 09 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625255):
I recall Cyril showing a very nice version of this tactic in Coq

#### [Johannes Hölzl (Sep 10 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133632944):
I added this 6 month ago. It's just a cheap version of Cyril's near tactic. Its more a reimplementation of Isabelle's `eventually` tactic

#### [Mario Carneiro (Sep 10 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133643643):
Cross reference: [abel tactic](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/abel.20tactic/near/133643278)

#### [Kevin Buzzard (Sep 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133648808):
Oh this is great news. Summary: the situation before this tactic was that we could prove things like $$(x+y)^2=x^2+2xy+y^2$$ if $$x$$ and $$y$$ were elements of a commutative ring (or even a commutative semiring) using the `ring` tactic, but for analogous questions about abelian groups the `ring` tactic did not work, and until now, if `simp` did not solve the goal, then one had to get one's hands dirty.

#### [Kevin Buzzard (Sep 17 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/134103969):
We have `linarith`, a new tactic that @**Rob Lewis** has written, which should definitely be mentioned here. It proves a bunch of things which hitherto were quite annoying / fiddly to prove. See it in action here: https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Feedback.20(Heine.20Borel.20in.20progress)/near/134050573 (e.g. proving that if `0 <= x` then `x/2 <= x`).

#### [Johan Commelin (Sep 21 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/134356908):
Today Kevin Buzzard is turning 50 :birthday:. [Congratulate him here](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Happy.20birthday.2C.20Kevin!)!
With a group of people we have been hacking like crazy to give him some birthday presents:
* @**Chris Hughes** Made immense (really immense!) progress on his `exp` branch in the community fork. We now have `exp`, `cos`, `sin` (all both complex and real), basic identities like `sin_add`, a proof that these functions are continuous, the intermediate value theorem, and finally `pi`. Yeah! :thumbs_up: :clink: 
* Other people have worked hard in a secret repository that is now public: https://github.com/semorrison/kbb (I sincerely apologize if you would have liked to participate but didn't know about this. I tried to contact as many people as I thought would be interested out of band, but of course I couldn't start a thread about this in the `#general` stream.)
* This repository contains a definition of `det` (determinant of matrices) and a proof that it is a monoid morphism. Thanks @**Kenny Lau** 
* @**Jack Crawford** has a bunch of stuff on a different implementation of matrices. Well done! (There seems to be a trade-off, the current implementation of matrices is nice to prove things with, his could well be better for computations.)
* A way to extract a matrix from a linear map between finite-dimensional vector spaces with bases.
* Characteristic polynomials of square matrices. (But no properties at all.)
* A proof that PID's are UFD's. Thanks @**Johannes Hölzl** (This result might be helpful for constructing splitting fields, because you want to know that an arbitrary (nonzero) polynomial factors into a product of irreducibles.)
* A (admittedly ad-hoc) definition of the modular group, plus a boatload of facts about it (e.g., we have a finite set of representatives of the action of `SL2Z` on matrices (over `int`) with determinant `m > 0`).
* A definition of complex derivatives, holomorphic function, modular forms.
* A proof that holomorphic functions form a subring of the ring of functions (on an arbitrary open domain in the complex numbers).
* A proof that modular forms form a submodule of functions on the upper half plane.
* An almost definition of Hecke operators. (Sorry Kevin, Lean was fighting back hard.)
Congratulations (and disucssions of about the maths!) can go [here](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Happy.20birthday.2C.20Kevin!)

#### [Johan Commelin (Oct 02 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135037903):
It's time for an update in this thread. And someone should also start the corresponding thread in `#general`.

#### [Johan Commelin (Oct 02 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135037915):
We now have Hensel's Lemma, thanks to @**Rob Lewis**

#### [Johan Commelin (Oct 02 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038009):
We also have `holor`. A `holor` is a generalisation of vectors and matrices. It is what the physicists would call a "tensor".

#### [Johan Commelin (Oct 02 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038047):
@**Reid Barton** Did a bunch of topology. Stuff on locally compact spaced. He also contributed groupoids.

#### [Johan Commelin (Oct 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038119):
Quadratic reciprocity has been merged. Once again: thanks @**Chris Hughes**

#### [Rob Lewis (Oct 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038132):
For the sake of completeness, the `holor` library is from @**Alexander Bentkamp** based on his work in Isabelle: https://link.springer.com/chapter/10.1007/978-3-319-66107-0_4

#### [Patrick Massot (Oct 02 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135039245):
I don't see holors, locally compact spaces and quadratic reciprocity in https://github.com/leanprover/mathlib/tree/master/docs/theories :sad:

#### [Kevin Buzzard (Oct 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135415885):
Thanks to Chris and Kenny, and inspired by work of my UROP students over the summer (especially @**Morenikeji Neri** ) we now have determinants! #404

#### [Mario Carneiro (Oct 08 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135415959):
next stop characteristic polynomials?

#### [Johan Commelin (Oct 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135415986):
Done in `kbb`

#### [Kevin Buzzard (Oct 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135416119):
My birthday present just keeps on giving

#### [Johan Commelin (Oct 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135416125):
You only turn 50 once...

#### [Johan Commelin (Oct 15 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135843390):
Thanks to the hard work Johannes we now have a nice start on Lebesgue integration: https://github.com/leanprover/mathlib/commit/0fe284916a73ce92227f77826ad9655b1329eb83

#### [Johan Commelin (Oct 15 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135843426):
Patrick and Johannes have worked very hard on quotient topologies on algebraic structures: https://github.com/leanprover/mathlib/commit/2395183b5b424371d5170f6c7bca691a654ae5bb

#### [Johan Commelin (Oct 15 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135843497):
Chris proved that subgroups of cyclic groups are cyclic: https://github.com/leanprover/mathlib/commit/c5930f574c54e3fd157b1ef8b93da8b1f50c8ed4

#### [Patrick Massot (Oct 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135846567):
Uniform spaces have Hausdorff completions https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535. More precisely, there is a completion functor which is left-adjoint to the inclusion of complete Hausdorff spaces into all uniform spaces.

#### [Patrick Massot (Oct 15 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135846763):
Abelian topological groups have a uniform space structure https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27 characterized by uniform continuity of substraction. The completion of such a topological group is a topological group with its canonical uniform structure (in particular the later is complete). Separated topological ring also have completions with the expected properties

#### [Johannes Hölzl (Oct 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135954996):
I merged #386 Chris' PR about trigonometric functions. So we have pi, exp, etc now

#### [Kenny Lau (Oct 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135955257):
looks like I messed up something. Could someone help reset `leanprover-community/mathlib`?

#### [Johannes Hölzl (Oct 17 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135955276):
fixed

#### [Kenny Lau (Oct 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135955325):
thanks

#### [Johannes Hölzl (Oct 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/136026140):
each PID is a UFD is now in mathlib

#### [Johan Commelin (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817351):
Ok, who is up for a summary of today?

#### [Johan Commelin (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817362):
First of all: the module refactor landed!

#### [Johan Commelin (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817368):
Second: Perfect closure has been merged.

#### [Kevin Buzzard (Nov 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817388):
This is a green light for algebraic closure and Galois theory

#### [Johan Commelin (Nov 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817519):
We now have all facts about `irrational` numbers that you would ever want to know.

#### [Johan Commelin (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817550):
(Ok, ok, we don't yet have irrationality op `pi`.)

#### [Johan Commelin (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817557):
We have Stone-Cech compactification.

#### [Patrick Massot (Nov 19 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/147997742):
Simon's monotonicity tactic has been merged in mathlib.
```lean
import tactic.monotonicity

example (x y z k m n : ℤ)
  (h₀ : z ≤ 0)
  (h₁ : y ≤ x)
: (m + x + n) * z + k ≤ z * (y + n + m) + k :=
by ac_mono*
```

#### [Patrick Massot (Nov 19 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/147998023):
We can combine with norm_num too:
```lean
example (α : Type) [linear_ordered_ring α] (x y z k : α)
  (h : z ≤ y) :
  (k + 3 + x) - y ≤ (k + 4 + x) - z := by mono* ; norm_num
```

#### [Johan Commelin (Nov 20 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/148016023):
Great news! Thanks @**Simon Hudon**! This is going to be very helpful. I really want to go back to the simplicial project now. Monotone functions are all over the place there.

#### [Simon Hudon (Nov 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/148016136):
Please keep me posted of ups and downs of using the tactic :)

#### [Scott Morrison (Dec 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/150739441):
(co)limits, and (co)limits in the category of Types!

#### [Scott Morrison (Dec 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/150739443):
There's still more to come (support for all the special shapes, products, equalizers, etc).

#### [Scott Morrison (Dec 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/150739492):
Also recently: equivalences of categories, along with a new tactic `slice`, for `conv`ing your way into long compositions, without having to use `rw category.assoc` by hand.

#### [Patrick Massot (Jan 05 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/154468807):
Sébastien's bounded continuous function has been merged :tada: Thank you so much Sébastien and Mario! This was a large PR, adding more than 600 lines to mathlib, even after getting Mario-compressed. 
> The type of bounded continuous functions from a topological space to a metric space, with the corresponding uniform distance. We prove basic statements such as the completeness of the space when the target is complete, and the Arzela-Ascoli theorem saying that a set of functions with a common modulus of continuity is compact. When the target space is a normed space, we also put the canonical normed space structure on the space of bounded continuous functions, working pointwise and checking that everything is compatible with the distance.

#### [Sebastien Gouezel (Jan 05 2019 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/154469138):
Thanks a lot Mario, this is awesome!

#### [Patrick Massot (Jan 18 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156374379):
@**Johannes Hölzl** could you tell us something about this Giry monad?

#### [Johannes Hölzl (Jan 18 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156375691):
Yep, with the newest commits the Giry monad is in mathlib In category speak, its the monad for the `measure` functor in the category of `measurable` spaces and functions. With this we get a straight forward way to construct product: `prod M1 M2 := do { x <- M1, y <- M2, return (x, y) }` 
Also I added measurable equivalences, which are helpful to adopt measurability proofs to different (but isomorphic) spaces

#### [Johannes Hölzl (Jan 18 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156375770):
the Giry monad will be also important to write down probabilistic programs or constructions. Especially in the theorem of Ionescu-Tulcea it provides a construction mechanism for discrete-time stochastic processes out of Markov kernels

#### [Simon Hudon (Jan 18 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156396464):
Can you use it in the category `types`?

#### [Kevin Buzzard (Jan 19 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156408538):
@**Luca Gerolla** do you understand a word of this? Luca formalised some stochastic stuff in Lean

#### [Luca Gerolla (Jan 19 2019 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156432294):
I can understand the probability notions (after googling) - in class we just focused on Kolmogorov extension theorem since we only studied discrete time-homogeneous Markov processes. 
Fascinating to see this general approach to formalise discrete-time stochastic processes :-)

#### [Johannes Hölzl (Jan 19 2019 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156443607):
the next step is to work on projective families, then Ionescu-Tulcea isn't far.

#### [Johannes Hölzl (Jan 19 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156443615):
@**Simon Hudon** no, we need the category of measurable spaces

#### [Simon Hudon (Jan 19 2019 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156446651):
Doesn't that limit the applicability to writing programs?

#### [Johannes Hölzl (Jan 20 2019 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156458525):
Yes, the need to have a probability measure limits the program. Measurability is a very wide and adaptible concept. If you really want your program to be outside of measurability the Giry monad can't help you

#### [Simon Hudon (Jan 20 2019 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156489827):
I was wondering if you could embed it in type with a trick like:

```lean
structure M (a : Type) := 
(s : measurable_space)
(x : Giry s)
(f : s -> a)
```

#### [Simon Hudon (Jan 20 2019 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156490029):
That allows you to implement `pure`, `map` and (i believe) `bind`

#### [Kevin Buzzard (Jan 20 2019 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156491890):
A scheme is a topological space equipped with some structure and satisfying some axioms. It makes sense to talk about morphisms of schemes (which are continuous maps on the topological spaces plus some other data involving the extra structure plus some axioms), and schemes form a category.

The category of schemes has finite products. In short, if $$S$$ and $$T$$ are schemes, then there's a product scheme $$S\times T$$, defined up to unique isomorphism, and satisfying the usual universal property. However the underlying topological space of a product of schemes is *not* the product of the underlying topological spaces (and the underlying type of a product is not the product of the underlying types).

I have no idea what monads have got to do with measure theory, but it occurred to me last week when talking to Ramon that with our `scheme X` idea (this is "unbundled", right?) where `X` is the underlying type, one can't use instances like `scheme X -> scheme Y -> scheme X \times Y` because that's the wrong product. Can I use monads in some crazy way to help here? @**Johannes Hölzl**  seems to think that monads can help with products in this measurable situation...

What do products look like when everything gets bundled? Oh -- it's just a map `scheme \times scheme -> scheme`, right?

@**Johan Commelin** Why are you having trouble extending a sheaf on a basis to a sheaf on the space, when I managed to do it without using categories? Is this anything to do with bundling or is this just universe issues?

#### [Johannes Hölzl (Jan 21 2019 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156502444):
@**Simon Hudon** What is `Giry s` in your case? Is `x` a measure on `s`? And what is the measurable space on`a`?

#### [Johannes Hölzl (Jan 21 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156502565):
@**Kevin Buzzard** I want to construct the usual product of the shape `measure A -> measure B -> measure (A x B)`. This would be the expected product from measure theory (assuming sigma finite measures). Here the Giry monad allows a factored proof.
I don't see how monads will help with your problem...

#### [Chris Hughes (Jan 21 2019 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156542773):
(deleted)

