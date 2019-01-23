---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/98209convergentsequencesarebounded.html
---

## Stream: [maths](index.html)
### Topic: [convergent sequences are bounded](98209convergentsequencesarebounded.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156388362):
How do I prove that a convergent sequence is bounded in Lean, in a way which is comprehensible to undergraduates? Say a_n tends to L. Setting epsilon=1 I know that for n>=N I have |a_n|<=|L|+1 by the triangle inequality. Now I need to let B be the max of |l|+1 and |a_n| for n<N (and then |a_n|<=B for all n). Mathematicians would say this was "trivial" so ideally I'd like to use as much automation as possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156388915):
[I'll just write the boilerplate now]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389440):
```lean
import data.real.basic
import tactic.linarith

noncomputable theory
local attribute [instance, priority 0] classical.prop_decidable

local notation `|` x `|` := abs x

definition is_limit (a : ℕ → ℝ) (l : ℝ) : Prop :=
∀ ε > 0, ∃ N, ∀ n ≥ N, | a n - l | < ε

definition is_bounded (a : ℕ → ℝ) : Prop := ∃ B : ℝ, ∀ n, |a n| ≤ B

theorem convergent_implies_bounded (a : ℕ → ℝ) : (∃ l, is_limit a l) → is_bounded a := sorry
```

I am a bit scared that my proof looks intimidating.

I was just watching Patrick proving that all epis were split in the category of sets and I thought it was going to be horrible but he just used this "choose" tactic and it was wonderful. I'm now wondering whether I can pull off something equally slick looking with this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jan 18 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389873):
A slick proof would be interesting. I tried doing a bit of basic analysis in Lean a long time ago, my proofs took me forever to write.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jan 18 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389882):
Just proving Cauchy sequences were bounded led me to:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jan 18 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389887):
```
-- Lemma 5.1.15 (Cauchy sequences are bounded). 
example : ∃ r, ∀ i, abv (f i) < r :=
let ⟨i, h⟩ := cauchy f zero_lt_one in 
let R := (finset.range (i+1)).sum (λ j, abv (f j)) in 
have h₁ : ∀ j ≤ i, abv (f j) ≤ R, from
  λ j ij, show (λ j, abv (f j)) j ≤ R, from 
  finset.single_le_sum 
    (λ k hk, is_absolute_value.abv_nonneg abv (f k)) 
    (by rwa [finset.mem_range, nat.lt_succ_iff]),
exists.intro (R + 1) (λ j, or.elim (lt_or_le j i) 
  (λ h₂, 
    let h₃ := le_of_lt h₂ in 
    lt_of_le_of_lt (h₁ j h₃) (lt_add_one R)) 
  (λ ij, 
    let h₃ := lt_of_le_of_lt (is_absolute_value.abv_add abv _ _)
      (add_lt_add_of_le_of_lt (h₁ _ (le_refl i)) (h j ij)) in 
    by rw [add_sub, add_comm] at h₃; simpa using h₃))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389989):
`finset.max` spits out a term of type `option alpha`. How come the one time I _want_ it to spit out zero (on the basis that forall x in X, x <= finset.max X would still be true when X is empty) it uses the option trick? :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390063):
Yeah, that code looks really intimidating. Obviously Lean code can become intimidating after a certain level, but I was hoping I had not got to that point yet, I'm trying to show the undergraduates how to use this thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390214):
How close can I get to $$X:=\max\{|a_n|\,|\,n\leq N\}$$ plus a theorem saying $$n\leq N\implies |a_n|\leq X$$?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390280):
I would like to avoid list.map list.range etc etc if possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390309):
you could use the real supremum of the set, that's pretty direct although you have less library assistance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390329):
I now realise that I want to take the sup in the set of non-negative reals, which exists even for the empty set. Do we have this trick in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390350):
eew but then I'd have to redefine `|x|` to take values in nnreal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390416):
just put 0 in the supremum

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390427):
Can I even make the set in a way that looks close to $$\{|a_n|\,|\,n\leq N\}$$?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390448):
not without using range

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390457):
I feel like my choice of notation might be about to bite me as well :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390467):
Can I avoid using map?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390474):
In python I can do quite fancy set comprehensions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390486):
I've just realised that I don't even know if I can do them in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390529):
lol, Simon will show you how to do fancy set comprehensions using do notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390546):
Are these lemmas actually trivial? Iirc, when I was following along these textbook proofs, each one required at least a paragraph of explanation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390568):
I agree actually, I've never seen this be a 0 line proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390634):
The fact that $$|a_n|\leq B_1$$ for $$n\geq N$$ implies that $$a_n$$ is bounded would be presented in a maths class like this: "let $$B_2$$ be the max of $$|a_n|$$ for $$n<N$$, then clearly $$B=\max\{B_1,B_2\}$$ works"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390649):
I have written this exact proof in mathlib somewhere, maybe you can make something of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390749):
Undergraduate mathematicians can fill in the proofs that there are only finitely many $$n<N$$, that the max exists, and that $$|a_n|\leq B$$ for all $$n$$, and they would be deemed sufficiently trivial as to be not worth mentioning.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390770):
https://github.com/leanprover/mathlib/blob/master/src/topology/metric_space/basic.lean#L531-L545

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390838):
One reason it's hard for all this Lean stuff to catch up with normal maths is that normal maths goes at what Lean people would think of as breakneck speed, with all sorts of side goals never dealt with. They're dealt with using the `undergraduate` tactic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390860):
It looks like I used `finset.range` and `finset.sup`, with `nndist` to stay in the nnreals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391073):
I guess I would say that in lean we write things in a particular way to prove side goals by type correctness when possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391179):
that's because you poor guys have to prove these goals :-) We just say they're obvious and hence not worth the time!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391196):
when you say "the max of |a_n| for n<N" there is a proof obligation that the set is bounded above, and has a max. When it's a finset this is obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391238):
You guys would probably point out that you need to prove it by induction or something :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391249):
because if I said "the max of |a_n| for n>N" it wouldn't be true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391262):
We don't even notice that we're using induction. We're even using recursion to define the max, I should think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391286):
that's one way to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391346):
There was a question on my M1F example sheet of the form "(i) Prove [blah] by induction (ii) now prove that I'm wasting your time and prove it directly without using induction"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391363):
and when I came to formalise it I realised that there was no way in hell that it was going to be proved without using induction :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391367):
Actually, I did have to prove that every finite sequence was bounded using induction, this was from Tao's UG analysis book "Analysis 1"...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391368):
If you prove this theorem by induction you can avoid any contact with finite suprema

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391372):
The question even had $$3^n$$ in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391375):
which you can't even really define without induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391408):
well, exp(n*log 3) is not inductive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391426):
heh, it's not nat-valued either :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391443):
of course it is, when the input is a natural number so is the output

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391449):
and I'd better check with Chris that he didn't use nat.rec anywhere in his definition of exp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391507):
```quote
of course it is, when the input is a natural number so is the output
```
 No! The output is a real number in the image of some coercion map, right? That's what you guys think anyway!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391510):
if you think it's not that's DTT lying to you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391516):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391575):
I'm going to have to spend some time thinking about this. I don't think these problems are unsolvable. Patrick proved that if f was surjective then it had a one-sided inverse using some simple `choose` tactic and it looked really good. Last year I proved this without that tactic to my UGs and it looked really horrible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391590):
Sometimes it's just a case of hiding all the true horror behind some simple interface.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391645):
like `finset.sup`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391657):
Maybe all you need are nice notations for it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391670):
finset.sup wants some semilattice_bot thing, and the reals aren't one of those

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391707):
`lattice.semilattice_sup_bot`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391720):
Can't we have `real.nnabs`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391736):
Yes. But of course that will cause problems somewhere else.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391745):
`finset.max` I think doesn't care, but it returns an option

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391758):
How come finset.max returns an option but 1 / 0 doesn't?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391828):
because it's on a generic type, there is no zero element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391829):
Is there a variant which returns default alpha if there's no elements?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391835):
but yes, you could do just that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391851):
I think there was one written at some point, not sure where it's gone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391860):
Maybe I'll write a little library with variants of these things which work better for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391867):
This has been helpful, thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391873):
you can define it as `(finset.max s).iget`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156392053):
It looks intimidating. I think that for my current purposes I just want to write some of my own functions which I'll hide in an import.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156392294):
that's what I mean you should do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156392350):
Oh I see. Of course. I have the weekend to do it, hopefully I will have it right by Tuesday.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156394768):
```lean
local notation `[0..` n `]` := finset.range n

#check [0..3] -- finset ℕ
```

I'm liking that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156394791):
You need more backticks :smiley:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395416):
```quote
I was just watching Patrick proving that all epis were split in the category of sets and I thought it was going to be horrible but he just used this "choose" tactic and it was wonderful. I'm now wondering whether I can pull off something equally slick looking with this.
```
This tactic was written specifically for this talk

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395499):
I know Johan, but I was between tube stations when this became clear :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395578):
except that set is {0,1,2}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395581):
Yes Patrick I remember you talking about it here. It seemed to work very well in practice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395587):
```quote
except that set is {0,1,2}
```
 *doh*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395599):
I mean I think it's useful to give talk and lectures where we want proofs to look nice. Because it pushes us to improve our tool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395618):
```
local notation `[0..` n `]` := finset.range (n + 1)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395711):
yeah but now how are you going to denote {|a_n| : n < N}?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395742):
We need that new parser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395766):
omg we could have something incredible

