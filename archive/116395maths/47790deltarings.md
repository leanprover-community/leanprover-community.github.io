---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47790deltarings.html
---

## [maths](index.html)
### [delta rings](47790deltarings.html)

#### [Johan Commelin (Jul 20 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993188):
Fix a prime `p`.

#### [Kenny Lau (Jul 20 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993189):
57

#### [Johan Commelin (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993230):
Consider the following attempt at a definition:
```lean
class delta_ring {A : Type*} extends comm_ring A :=
(δ : A → A)
(add_prop : ∀ {a b}, δ (a + b) = δ(a)^p + δ(b)^p + (a^p + b^p - (a+b)^p)/p)
```

#### [Johan Commelin (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993244):
How should one explain to Lean that `(a^p + b^p - (a+b)^p)/p` in fact makes sense?

#### [Kenny Lau (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993254):
must that expression have a unique value?

#### [Kenny Lau (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993256):
yes

#### [Kenny Lau (Jul 20 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993260):
you can define a function that spits out that value?

#### [Johan Commelin (Jul 20 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993265):
Yes, you can. But doesn't that make the definition extremely convoluted?

#### [Kenny Lau (Jul 20 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993273):
delta_ring.aux : A \to A \to prime \to A

#### [Johan Commelin (Jul 20 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993326):
And I guess Lean gets happier if I give an explicit definition? Instead of just claiming that the value exists because certain binomial coefficients will always have a factor `p`?

#### [Kenny Lau (Jul 20 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993331):
at least I would be happier

#### [Johan Commelin (Jul 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993446):
Here is the full "definition":
```lean
class delta_ring {A : Type*} extends comm_ring A :=
(δ : A → A)
(zero_prop : δ(0) = 0)
(one_prop : δ(1) = 0)
(add_prop : ∀ {a b}, δ(a+b) = δ(a)^p + δ(b)^p + (a^p + b^p - (a+b)^p)/p)
(mul_prop : ∀ {a b}, δ(a*b) = a^p*δ(b) + b^p*δ(a) + p*δ(a)*δ(b))
```

#### [Kenny Lau (Jul 20 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993460):
would you say that including `^` make the definition more convoluted?

#### [Johan Commelin (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993517):
What do you mean?

#### [Johan Commelin (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993524):
Ok, I see what you are getting at...

#### [Kenny Lau (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993526):
`^` is also an auxiliary function that doesn't follow from the ring axioms

#### [Johan Commelin (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993538):
Well, as a mathematician, I am used to the notation `^`, but not to the function `delta_ring.aux`.

#### [Kenny Lau (Jul 20 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993539):
that's an arbitrary distinction

#### [Johan Commelin (Jul 20 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993552):
By that logic every definition in maths is arbitrary.

#### [Kenny Lau (Jul 20 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993609):
alright

#### [Johan Commelin (Jul 20 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993628):
Anyway, do you think it is easy to define `aux` constructively?

#### [Kenny Lau (Jul 20 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993631):
I think the function ((a+b)^p-a^p-b^p)/p might be useful more generally

#### [Kenny Lau (Jul 20 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993686):
hmm, let me think about that

#### [Johan Commelin (Jul 20 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993702):
I guess I first need to prove that `binom p i` is divisible by `p` for `0 < i < p`.

#### [Kenny Lau (Jul 20 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993748):
can we somehow extend that definition to all natural numbers?

#### [Kevin Buzzard (Jul 20 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993814):
no, p has to be prime (if you are working over an arbitrary ring)

#### [Kevin Buzzard (Jul 20 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993818):
Kenny didn't you already write this function somehow?

#### [Kevin Buzzard (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993832):
I think Chris did some binomial / factorial things

#### [Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993835):
f(a,b,2) = ab
f(a,b,3) = aab+abb
f(a,b,5) = aaaab+2aaabb+2aabbb+abbbb
f(a,b,7) = aaaaaab+3aaaaabb+5aaaabbb+5aaabbbb+3aabbbbb+abbbbbb

#### [Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993838):
there's nothing that can go between the lines?

#### [Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993841):
hmm

#### [Kevin Buzzard (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993843):
no

#### [Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993849):
what does a mathematician think about this function?

#### [Kevin Buzzard (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993887):
If Chris proved that binom p i * i! * (p-i)! = p! then proving it's a multiple of p is fine as long as you know that if p divides ab then p divides a or b.

#### [Kevin Buzzard (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993894):
You then prove that p doesn't divide i! for i<p and you're done

#### [Kenny Lau (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993914):
I know that "pCa is divisible by p for all a" iff p is a prime

#### [Kenny Lau (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993918):
i'm asking whether that function can be extended

#### [Kevin Buzzard (Jul 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993933):
sure it can be extended -- just define it to be 37 for n not prime

#### [Kenny Lau (Jul 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993941):
well

#### [Kenny Lau (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994038):
I think the GPOV is to define the relevant elements of Z[X,Y] first

#### [Kevin Buzzard (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994048):
You're inventing Witt vectors

#### [Kevin Buzzard (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994051):
you can do stuff for prime powers somehow

#### [Kenny Lau (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994052):
indeed

#### [Johan Commelin (Jul 20 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994100):
Alternatively, Kenny puts Witt vectors into mathlib (-;

#### [Johan Commelin (Jul 20 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994126):
I mean, we are doing this perfectoid stuff. But the mathematicians are already moving on...

#### [Kevin Buzzard (Jul 20 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994127):
The trendy way to do Witt vectors nowadays is to note that if k is a perfect field of char p and R is a k-algebra then the cotangent complex vanishes

#### [Kevin Buzzard (Jul 20 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994138):
a la Scholze perfectoid spaces paper

#### [Johan Commelin (Jul 20 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994141):
Nowadays you're only hot if you're doing diamonds or prisms...

#### [Patrick Massot (Jul 20 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994229):
Let's try perfectoid spaces first...

#### [Johan Commelin (Jul 20 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994239):
(Kevin, I think the perfectoid project is really cool. So I'm just trying to do some related things to the side, while you are wrapping up `Cont` et al.)

#### [Kenny Lau (Jul 20 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994278):
where are the prism emojis when I need them

#### [Kenny Lau (Jul 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994432):
do we have valuations of integers at a prime?

#### [Kenny Lau (Jul 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994437):
I think Alexandria has that

#### [Johan Commelin (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994447):
Ok, mathlib knows how to raise ring elements to `nat`-powers, right? Why is this failing?
```lean
def Frob {A : Type u} [ring A] (x : A) := x^p
```
Error:
```lean
failed to synthesize type class instance for
_inst_1 : nat.Prime,
A : Type u,
_inst_2 : ring A,
x : A
⊢ has_pow A ℕ
```

#### [Kenny Lau (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994461):
did you import the right things?

#### [Johan Commelin (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994463):
No

#### [Kenny Lau (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994465):
that's why

#### [Johan Commelin (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994467):
Hmmm, I want Lean to tell me what to import...

#### [Patrick Massot (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994468):
Johan, if you don't know what to do for the perfectoid project, you can do
```lean
variables (α : Type*) [uniform_space α] (β : Type*) [uniform_space β]

instance complete_space.prod [complete_space α] [complete_space β] : complete_space (α × β) := sorry
instance separated.prod [separated α] [separated β] : separated (α × β) := sorry
```
which is on my TODO list

#### [Kenny Lau (Jul 20 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994510):
imports? @**Patrick Massot**

#### [Kenny Lau (Jul 20 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994523):
and is that MWE?

#### [Kenny Lau (Jul 20 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994564):
never mind

#### [Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994623):
`import analysis.topology.uniform_space`

#### [Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994632):
and then you get a MWE

#### [Kenny Lau (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994637):
hmm

#### [Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994640):
I'm not saying this is difficult

#### [Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994650):
I see Johan is blocked because he waits for Kevin

#### [Kevin Buzzard (Jul 20 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995452):
I am dealing with universe issues raised by Mario. I have defined an "equivalence class of valuations" on (R : Type u) to be a pre-order on R which is induced from a valuation v : R -> M with M a certain kind of totally ordered monoid, with (M : Type u). I now have to prove that if M had type v then actually there's M' of type u inducing the same pre-order. I dug and dug, and I am now having to define universal properties of quotient groups. But I've screwed up:

https://github.com/kbuzzard/lean-perfectoid-spaces/blob/a0d3bd5de20ed91d2e318914bac742c073b3c4f7/src/for_mathlib/quotient_group.lean#L48

I need to prove that if G is commutative then so is G/N but I think I managed to define multiplication on G in two different ways. I'm spending all day dealing with admin though. If anyone wants to fix up my easy group theory stuff then feel free!

#### [Kevin Buzzard (Jul 20 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995483):
I will get back to all this this evening hopefully

#### [Johan Commelin (Jul 20 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995722):
Ok, I started doing this because I was watching Bhargav Bhatt's talk from the Gabber birthday conference.

#### [Johan Commelin (Jul 20 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995792):
It's quite fun! So far I've got: https://gist.github.com/jcommelin/b09dcc1c3494e123e84afc96a91fd61c

#### [Johan Commelin (Jul 20 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995813):
Making good use of `tactic.ring`!

#### [Kenny Lau (Jul 20 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995924):
```lean
theorem wtf (A B : Type) (S : set A) (T : set B) :
  set.prod S T = set.inter (prod.fst ⁻¹' S) (prod.snd ⁻¹' T) := rfl
```

#### [Kenny Lau (Jul 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995932):
```lean
import analysis.topology.uniform_space

variables (α : Type*) [uniform_space α] (β : Type*) [uniform_space β]

instance complete_space.prod [complete_space α] [complete_space β] : complete_space (α × β) :=
{ complete := λ f hf,
    let ⟨x1, hx1⟩ := complete_space.complete $ cauchy_map uniform_continuous_fst hf in
    let ⟨x2, hx2⟩ := complete_space.complete $ cauchy_map uniform_continuous_snd hf in
    ⟨(x1, x2), by rw [nhds_prod_eq, filter.prod_def];
      from filter.le_lift (λ s hs, filter.le_lift' $ λ t ht,
        have H1 : prod.fst ⁻¹' s ∈ f.sets := hx1 hs,
        have H2 : prod.snd ⁻¹' t ∈ f.sets := hx2 ht,
        filter.inter_mem_sets H1 H2)⟩ }
```

#### [Kenny Lau (Jul 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995939):
@**Patrick Massot**

#### [Kenny Lau (Jul 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995948):
26 minutes

#### [Patrick Massot (Jul 20 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129996119):
Thanks!

#### [Johan Commelin (Jul 20 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001219):
I still don't really know how to go about defining
```lean
def delta_ring.aux {A : Type u} [comm_ring A] : A → A → A := sorry
-- λ a b, (a^p + b^p - (a+b)^p)/p
```
I know how to do this in maths, but I don't know how to go forward in Lean.

#### [Kevin Buzzard (Jul 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001353):
I'm not saying it's the best way, but one way would be to define the function from fin (p-1) to nat sending i to (p choose i) / p, and then do a finset.sum [I guess you need p as an input for this function].

#### [Kevin Buzzard (Jul 20 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001422):
Presumably at some point though you'll need that p times your function is what you want it to be, and there you'll need the binomial theorem, which @**Chris Hughes** has done I believe. Looking at what he did might help.

#### [Johan Commelin (Jul 20 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001461):
Ok, I already have that property stated (and sorried). So I'm able to prove properties of delta rings already (-;

#### [Johan Commelin (Jul 20 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001483):
I'll take a look at what Chris did.

#### [Chris Hughes (Jul 20 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130004696):
```quote
Presumably at some point though you'll need that p times your function is what you want it to be, and there you'll need the binomial theorem, which @**Chris Hughes** has done I believe. Looking at what he did might help.
```
I can PR it, but I'm not sure whether to call it `binomial` or `add_pow`.

#### [Johan Commelin (Jul 20 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008512):
I wouldn't mind if well-known theorems with well-known names preserve their well-known names.

#### [Johan Commelin (Jul 20 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008530):
To me it would increase readability of proofs

#### [Kevin Buzzard (Jul 20 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008597):
How do you feel about a random German in 1992 deciding to call his seminorms valuations even though they are seminorms, and now we have this annoying problem that our definition of valuation in the perfectoid project is both standard and non-standard simultaneously? :-/

#### [Kevin Buzzard (Jul 20 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008664):
If someone told me that we were going to ditch that stupid bracket notation for quadratic residues, I would crack open the champagne.

#### [Kevin Buzzard (Jul 20 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008683):
Oh -- wait -- for binomial we can just call it both

#### [Kevin Buzzard (Jul 20 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008712):
that's what they do with left_distrib, right? That's the formally correct historical name, but add_mul (or mul_add, which ever one left distrib is) is a modern sensible name.

#### [Kevin Buzzard (Jul 20 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008795):
Chris -- do you prove that `binomial(a,b)*b!*(a-b)!=a!`?

#### [Kenny Lau (Jul 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008811):
do we have valuation of an integer over a prime?

#### [Kevin Buzzard (Jul 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008820):
It's `list.count p (factor n)` Kenny

#### [Johan Commelin (Jul 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008827):
Kevin, it is `choose(a,b)`, I think. So we can call the binomial theorem `binomial`, if we want...

#### [Kevin Buzzard (Jul 20 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008944):
`factors n` sorry

#### [Kevin Buzzard (Jul 20 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008945):
https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean

#### [Kevin Buzzard (Jul 20 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130009004):
lines 226 and 236 show that that's a list of the primes dividing n with multiplicity

#### [Kevin Buzzard (Jul 20 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130009294):
https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55 -- there's the factorial fact

#### [Chris Hughes (Jul 20 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130011551):
```quote
https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55 -- there's the factorial fact
```
@**Kevin Buzzard** It's also here https://github.com/leanprover/mathlib/blob/master/data/nat/choose.lean

#### [Kevin Buzzard (Jul 20 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130012395):
I couldn't find the binomial theorem though

#### [Chris Hughes (Jul 20 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130012405):
I haven't PRed it yet.

#### [Kevin Buzzard (Jul 20 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130012416):
I mean I couldn't find it in your github repo

#### [Mario Carneiro (Jul 20 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014183):
Question: Why is `(a^p + b^p - (a+b)^p)/p` uniquely defined? Is division by `p` always uniquely defined (when applied to multiples of `p`)? Seems like if the ring has characteristic `p` this will be a problem...

#### [Kenny Lau (Jul 20 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014372):
it isn't uniquely defined, but there's a canonical choice

#### [Kevin Buzzard (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014441):
It's good old informal mathematicians again, meaning "do it in Q, note the answer is in Z, now map it into any ring"

#### [Johan Commelin (Jul 20 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014936):
```quote
it isn't uniquely defined, but there's a canonical choice
```
Did you just use the word 'choice'?

#### [Johan Commelin (Jul 20 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015002):
I just realised that I think Witt vectors and Hensel's lemma are two very nice (and manageable, I hope) companions to the perfectoid project. They aren't logically necessary, but I think they might be really helpful if one wants to do some examples...

#### [Kenny Lau (Jul 20 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015089):
yeah, I chose the word "choice"

#### [Mario Carneiro (Jul 20 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015091):
I think it's a shame that you have to write it this roundabout way, since it loses the clarity

#### [Mario Carneiro (Jul 20 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015112):
Another way to say what you are trying to say is to form `x^p + y^p - (x+y)^p` as a multivariate polynomial in Z[x,y], divide by `p`, and evaluate it at `a,b`

#### [Johan Commelin (Jul 20 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015162):
Yes, I completely agree. But I don't know yet how to convince Lean that I can divide that polynomial by `p`

#### [Mario Carneiro (Jul 20 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015179):
As a polynomial in `Z[x,y]`, you can use `int.div` on the coefficients

#### [Johan Commelin (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015193):
Aah, and that is always defined, although it sometimes outputs 57. Is that right?

#### [Johan Commelin (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015200):
Or probably the floor of x / y.

#### [Mario Carneiro (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015202):
yes that

#### [Johan Commelin (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015206):
Ok, so then the definition is not hard.

#### [Kevin Buzzard (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015209):
```quote
Another way to say what you are trying to say is to form `x^p + y^p - (x+y)^p` as a multivariate polynomial, divide by `p`, and evaluate it at `a,b`
```
This is just some standard polynomial which shows up in some graduate commutative algebra thing, so mathematicians abuse notation. It means exactly what you said yes. The polynomials even have names -- they're in Z[x,y] but then they get coerced into R[x,y] for any comm_ring R

#### [Kenny Lau (Jul 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015277):
by GPOV

#### [Johan Commelin (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015306):
So then I only need to prove the property that `p * aux_poly = x^p + y^p - (x+y)^p`

#### [Johan Commelin (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015318):
And that requires the binomial theorem

#### [Kenny Lau (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015319):
aux_poly x y p

#### [Kevin Buzzard (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015326):
you're going to need the binomial theorem at some point

#### [Johan Commelin (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015329):
sure

#### [Chris Hughes (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015370):
It's in your stack project @**Kevin Buzzard**

#### [Kevin Buzzard (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015374):
I didn't think to look there

#### [Mario Carneiro (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015379):
I don't think you actually need the binomial theorem for this, but you mathematicians like your hammers

#### [Johan Commelin (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015386):
Why not?

#### [Mario Carneiro (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015389):
It's an easy proof by induction

#### [Kevin Buzzard (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015390):
if you define `aux_poly` to be the explicit `(choose p i) / p` etc etc then it's the same as the binomial theorem

#### [Kenny Lau (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015397):
it isn't because you can't fill in the gap that p causes

#### [Mario Carneiro (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015402):
forget that

#### [Kenny Lau (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015406):
you can't extend the definition of aux_poly to all nat

#### [Johan Commelin (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015419):
you can, he just did that... but you get nonsense

#### [Patrick Massot (Jul 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015505):
I'm trying to figure out what GPOV stand for (I mean understand the acronym, I understand the maths). Google is not very helpful

#### [Johan Commelin (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015601):
@**Kevin Buzzard** I just realised that trying to convert arithmetic geometers and/or number theorists to Lean is going to be futile. They start every talk with "For me all rings are commutative." If they can't do that at the top of their Lean files, and they really have to type `comm_ring` instead of `ring` all the time, they will drop out immediately...

#### [Johan Commelin (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015614):
@**Patrick Massot** General Point Of View?

#### [Johan Commelin (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015628):
There is also nPOV = n-categorical POV

#### [Kenny Lau (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015638):
Grothendieck's point of view

#### [Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015717):
you could always fork mathlib

#### [Mario Carneiro (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015731):
`comm_ring` is in core

#### [Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015735):
oh crap

#### [Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015738):
`comm_ring` -> `ring`

#### [Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015741):
`ring` -> `non_comm_ring`

#### [Kevin Buzzard (Jul 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015742):
that's what it should be

#### [Mario Carneiro (Jul 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015765):
``local notation `ring` := comm_ring`` should work

#### [Kevin Buzzard (Jul 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015784):
and then ``local notation `non_comm_ring` := ring``?

#### [Mario Carneiro (Jul 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015846):
do you actually care about that?

#### [Kevin Buzzard (Jul 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015854):
I will grudgingly confess to occasionally using the ring of 2 x 2 matrices

#### [Kenny Lau (Jul 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015863):
@**Kevin Buzzard** you're lucky all rings have unity

#### [Mario Carneiro (Jul 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015872):
maybe don't use stupid overrides in that file

#### [Mario Carneiro (Jul 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015972):
also, overriding the notation for `ring` doesn't prevent you from using matrix rings

#### [Mario Carneiro (Jul 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015986):
of course typeclass inference doesn't care about your notation

#### [Mario Carneiro (Jul 20 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130016100):
Now I am picturing some mathematician starting their talk with "in this lecture, all rings are commutative" and proceed to do amazing things by commuting matrices that don't commute

#### [Johan Commelin (Jul 20 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130018032):
```quote
of course typeclass inference doesn't care about your notation
```
It doesn't? I don't know if I am happy or sad about that...

#### [Mario Carneiro (Jul 20 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130018603):
well the alternative is the "commutative by fiat" lecture scenario I mentioned

#### [Johan Commelin (Jul 23 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135388):
Ok, so now I want to define the `aux_poly` in two variables. What would be the best way to do that? I currently have
```lean
section delta_ring_aux_poly

open mv_polynomial

def delta_ring.aux_poly1 : mv_polynomial (fin 2) ℤ :=
begin
  let X0 : mv_polynomial (fin 2) ℤ := X ⟨0, nat.zero_lt_succ 1⟩,
  let X1 : mv_polynomial (fin 2) ℤ := X ⟨1, nat.le_refl 2⟩,
  exact (X0^p + X1^p - (X0+X1)^p),
end

def delta_ring.aux_poly2 : mv_polynomial (fin 2) ℤ :=
finsupp.map_range (λ n:ℤ, n/p) (int.zero_div p) delta_ring.aux_poly1

end delta_ring_aux_poly

def delta_ring.aux {A : Type u} [comm_ring A] : A → A → A :=
(mv_polynomial.functorial int.cast delta_ring.aux_poly2).eval ∘
(λ a b,
begin
  intro i,
end
 : A → A → ((fin 2) → A))
--  sorry
-- λ a b, (a^p + b^p - (a+b)^p)/p
```

#### [Johan Commelin (Jul 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135453):
It it better to use `choose` here, and explicitly define it as  some `finset.sum`?

#### [Johan Commelin (Jul 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135463):
I don't really like the `finsupp.map_range`, but that is just *my* gut feeling.

#### [Mario Carneiro (Jul 23 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135543):
This looks like a pretty faithful rendition of my suggestion

#### [Mario Carneiro (Jul 23 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135548):
the last bit looks incomplete though

#### [Johan Commelin (Jul 23 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135588):
It is.

#### [Johan Commelin (Jul 23 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135602):
I don't know how to define functions out of `fin n`. Do we have to use if-then-else for that?

#### [Mario Carneiro (Jul 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135611):
there should be a `fin.cons` function

#### [Mario Carneiro (Jul 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135619):
you can also use a `match` block

#### [Mario Carneiro (Jul 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135625):
there is `fin.cases`

#### [Mario Carneiro (Jul 23 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135683):
Probably it is easier to use `bool` rather than `fin 2` here

#### [Johan Commelin (Jul 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135764):
Aah, that is a nice suggestion

#### [Johan Commelin (Jul 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135767):
I'll try that

#### [Mario Carneiro (Jul 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135777):
You can use `cond` to case on `bool`

#### [Johan Commelin (Jul 23 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135846):
Hmm, what exactly do you mean with that?

#### [Johan Commelin (Jul 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135892):
Aah

#### [Johan Commelin (Jul 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135898):
So `cond` is in fact my function. I want to look at `cond i a b`

#### [Mario Carneiro (Jul 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135907):
yes

#### [Johan Commelin (Jul 23 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130136703):
@**Chris Hughes** Are you planning on PR-ing your binomial theorem sometime soon?

#### [Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144619):
So, now I need to sum over `fin n`. Hooray! I don't even know how to deal with the case `n = 1`:
```lean
import data.finsupp

example (p : ℕ) (hp : p = 57) : finset.sum finset.univ (λ (x : fin (0 + 1)), finsupp.single (finsupp.single (x.val) 1) (p ^ x.val)) =
    finsupp.single (finsupp.single 0 1) 1 := sorry
```

#### [Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144647):
I would like to tell Lean that `finset.univ` is `singleton 0` in this case.

#### [Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144649):
But I don't know how to do that.

#### [Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144655):
(Technically `singleton \<0,_\>`...)

#### [Kenny Lau (Jul 23 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130145367):
```lean
import data.finsupp

example (p : ℕ) (hp : p = 57) : finset.sum finset.univ (λ (x : fin (0 + 1)), finsupp.single (finsupp.single (x.val) 1) (p ^ x.val)) =
    finsupp.single (finsupp.single 0 1) 1 :=
have H1 : (finset.univ : finset $ fin 1) = finset.singleton 0,
  from finset.ext' $ λ ⟨x, hx⟩, begin
    cases hx with hx hx1,
    { simp, refl },
    cases hx1
  end,
by rw [H1, finset.sum_singleton]; refl
```

#### [Johan Commelin (Jul 23 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130145441):
You were able to convince Lean that you get a singleton! I couldn't even get it to typecheck the type of H1.

#### [Johan Commelin (Jul 23 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130161570):
```quote
@**Chris Hughes** Are you planning on PR-ing your binomial theorem sometime soon?
```
Thanks! :clap: :octopus:

