---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47427M1M1MathematicalMethodsinLean.html
---

## Stream: [maths](index.html)
### Topic: [(M1M1) Mathematical Methods in Lean](47427M1M1MathematicalMethodsinLean.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 13 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729301):
The joint maths and computer science students at Imperial College London are doing four courses this term. One on Haskell, one on logic, my course M1F, and a course called M1M1, which is a mathematical methods course, where the derivative of sin is cos just like it was at school and nobody really bothers with why that's true.

#### [ Kevin Buzzard (Oct 13 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729358):
On the other hand, one of the questions on the first sheet was "define $$f(x) = 1+x+x^2/2!+x^3/3!+\cdots$$ and let's not worry about what it means to converge. By multiplying everything out and re-arranging without worrying about whether this is valid, prove $$f(x+y) = f(x) \times f(y)$$"

#### [ Kevin Buzzard (Oct 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729361):
and I thought " @**Chris Hughes**  did that properly, took him ages"

#### [ Kevin Buzzard (Oct 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729367):
I wonder how far we'll be able to get on the M1M1 example sheets by the end of term :-)

#### [ Kevin Buzzard (Oct 13 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729407):
One of the questions needed log and Chris did that a few weeks ago, so we're still just ahead

#### [ Kevin Buzzard (Oct 13 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729413):
Are double angle formulae in Lean? Tricks about sin(theta) in terms of tan(theta/2)?

#### [ Kevin Buzzard (Oct 13 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729471):
Stuff which is assumed in M1M1? Ability to define $$\int_0^\infty e^{-x^2/2} d x$$?

#### [ Chris Hughes (Oct 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729571):
It's not just methods that's like this. Try formally proving every permutation is the product of disjoint cycles.

#### [ Kevin Buzzard (Oct 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729697):
you show us up for the charlatains we are!

#### [ Kevin Buzzard (Oct 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729733):
But we're mathematicans. If your silly software cannot easily prove things which are intuitively obvious to us then the problem is surely with your software

#### [ Kevin Buzzard (Oct 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729750):
The proof is "choose an element, keep hitting with the permutation, eventually you'll get back to where you start, done by induction"

#### [ Kevin Buzzard (Oct 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729794):
(assuming we're talking about finite sets/types)

#### [ Kenny Lau (Oct 13 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729898):
that's what I did

#### [ Kevin Buzzard (Oct 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729986):
how many lines?

#### [ Kenny Lau (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730384):
26 lines

#### [ Kenny Lau (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730385):
https://github.com/kckennylau/Lean/blob/master/Sym.lean#L645-L670

#### [ Kenny Lau (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730387):
```lean
def list_step (σ : Sym n) : list (step n) :=
by refine well_founded.fix list_step.aux.wf _ σ; from
λ σ ih, if H : σ.support = ∅ then []
  else let ⟨i, hi⟩ := σ.support_choice H in
    step.mk' (σ i) i (support_def.1 hi)
    :: ih (swap (σ i) i * σ) (support_swap_mul hi)

@[simp] lemma list_step_prod (σ : Sym n) :
  (σ.list_step.map step.eval).prod = σ :=
well_founded.induction list_step.aux.wf σ $ λ σ ih,
begin
  dsimp [list_step],
  rw [well_founded.fix_eq],
  split_ifs,
  { ext, by_contra H,
    suffices : i ∈ (∅ : finset (fin n)),
    { simp at this, cc },
    rw [← h, support_def],
    exact mt eq.symm H },
  cases support_choice σ h with i hi,
  unfold list_step._match_1,
  specialize ih _ (support_swap_mul hi),
  dsimp [list_step] at ih,
  rw [list.map_cons, list.prod_cons, ih, ← mul_assoc],
  rw [step.eval_mk', swap_mul_self, one_mul]
end
```

#### [ Kevin Buzzard (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730390):
That sounds like a reasonable length to me.

#### [ Chris Hughes (Oct 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730559):
That's a proof of something different isn't it? It's a proof about products of swaps, not disjoint cycles.

#### [ Kenny Lau (Oct 13 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730680):
ah, right

#### [ Kevin Buzzard (Oct 13 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730742):
so the question remains

#### [ Chris Hughes (Oct 13 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135747465):
225 lines https://github.com/leanprover/mathlib/compare/master...dorhinj:cycles2?expand=1

#### [ Mario Carneiro (Oct 14 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135752321):
I like it, we're getting a lot of nice structure on `perm`

#### [ Mario Carneiro (Oct 14 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135752367):
Any chance of defining stuff about the finitely supported permutations? (i.e. it's a subgroup, and has most of the properties you have put on finite permutation groups like the alternating group or separation into disjoint cycles)

#### [ Kevin Buzzard (Oct 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135771386):
One would imagine that these are also situations where a mathematician would say "it's obvious" (like e.g. the fact that it's a subgroup).

#### [ Kenny Lau (Oct 14 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135771455):
I think at this point we all know that it's pointless to keep saying that so and so is obvious to a mathematician.

#### [ Kevin Buzzard (Oct 14 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135771526):
I don't think it's pointless at all Kenny. I think that if we isolate many of the things that are "obvious to a mathematician" and make sure that they are *relatively easy for a mathematician do in Lean* (even though we all know that they are in truth difficult to do from the actual axioms of mathematics) then this is a step towards making Lean more intuitive for mathematicians to use.

#### [ Chris Hughes (Oct 14 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775656):
```quote
Any chance of defining stuff about the finitely supported permutations? (i.e. it's a subgroup, and has most of the properties you have put on finite permutation groups like the alternating group or separation into disjoint cycles)
```
What's the best approach for this. Are you happy to lose computability in favour of generality? My `cycle_of` function can certainly be extended to infinite permutations, but not computably, though it is outrageously slow anyway. For `sign` and stuff, is it best to just create a new definition of `sign` for finitely supported permutations of infinite types. I imagine this is better than making a partial function which is actually a total function on most of the stuff people want to use it for.

#### [ Mario Carneiro (Oct 14 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775778):
`cycle_of` should be computable on infinite (finitely supported) permutations, assuming `decidable_eq` on the base set, although I would factor it into a `cycle_support` function that returns the list of iterates of the input

#### [ Mario Carneiro (Oct 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775883):
and then I guess there are also a bunch of noncomputable functions we might want in the truly infinite case, like `cycle_of` where the cycle is possibly isomorphic to Z

#### [ Mario Carneiro (Oct 14 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775946):
In fact it is still true that "every permutation is a product of cycles" in the truly infinite case, you just have to make sense of an infinite product of disjoint permutations

#### [ Kevin Buzzard (Oct 14 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135777622):
```quote
I think at this point we all know that it's pointless to keep saying that so and so is obvious to a mathematician.
```
Just adding to this thread that to a 1st year maths undergraduate it is "obvious" that the derivative of $$\sin(x)$$ is $$\cos(x)$$ (because they "learnt it at school") and I think that having this in Lean would be a very natural goal. It will be interesting to see if our new cohort of freshers were up to the task.


{% endraw %}
