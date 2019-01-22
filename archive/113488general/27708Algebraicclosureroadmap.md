---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27708Algebraicclosureroadmap.html
---

## [general](index.html)
### [Algebraic closure roadmap](27708Algebraicclosureroadmap.html)

#### [Kenny Lau (Oct 14 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135781672):
I've created a roadmap for constructing an algebraic closure of a field: https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md

#### [Kenny Lau (Oct 14 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135781674):
@**Kevin Buzzard**

#### [Kenny Lau (Oct 14 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135782970):
I just thought of another approach that is very similar: we can construction the "perfect closure" of a ring of char p > 0, and then for a field F we consider its perfect closure Fp, and then do the big polynomial ring thing to Fp instead, and we obtain the field K, and we prove that K is algebrically closed. This would require transitivity of integrality though.

#### [Kenny Lau (Oct 14 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135783254):
Never mind, forget this other approach.

#### [Kenny Lau (Oct 14 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135783607):
Do we even have char p?

#### [Kenny Lau (Oct 14 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135783619):
lol no we don't have

#### [Kevin Buzzard (Oct 14 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135786179):
So you prefer this approach to the "now repeat steps 22-27 infinitely often and take the direct limit"? Integral elements form a subring -- you will have to wait a bit for this I guess. The direct limit approach avoids this. I guess Mario already explained why he thinks your approach is better though.

#### [Kenny Lau (Oct 14 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135787184):
@**Kevin Buzzard** do you like perfect closure?

#### [Kenny Lau (Oct 14 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135787223):
```lean
import data.padics.padic_norm data.nat.binomial

universe u

class char_p (α : Type u) [has_zero α] [has_one α] [has_add α] (p : ℕ) : Prop :=
(cast_eq_zero : (p:α) = 0)

theorem add_pow_char {α : Type u} [comm_ring α] {p : ℕ} (hp : nat.prime p)
  [char_p α p] (x y : α) : (x + y)^p = x^p + y^p :=
begin
  rw [add_pow, finset.sum_range_succ, nat.sub_self, pow_zero, choose_self],
  rw [nat.cast_one, mul_one, mul_one, add_left_inj],
  transitivity,
  { refine finset.sum_eq_single 0 _ _,
    { sorry },
    { intro H, exfalso, apply H, exact finset.mem_range.2 hp.pos } },
  rw [pow_zero, nat.sub_zero, one_mul, choose_zero_right, nat.cast_one, mul_one]
end

def frobenius (α : Type u) [monoid α] (p : ℕ) (x : α) : α :=
x^p

instance {α : Type u} [comm_ring α] (p : ℕ) (hp : nat.prime p) [char_p α p] : is_ring_hom (frobenius α p) :=
{ map_one := one_pow p,
  map_mul := λ x y, mul_pow x y p,
  map_add := add_pow_char hp }

def perfect_closure (α : Type u) [monoid α] (p : ℕ) : Type u :=
@quotient (ℕ × α)
⟨λ x y, ∃ n, x.2^(p^(y.1+n)) = y.2^(p^(x.1+n)),
λ _, ⟨0, rfl⟩, λ _ _ ⟨n, H⟩, ⟨n, H.symm⟩,
λ ⟨n₁, x₁⟩ ⟨n₂, x₂⟩ ⟨n₃, x₃⟩ ⟨w₁, h₁⟩ ⟨w₂, h₂⟩, ⟨n₂ + w₁ + w₂,
calc  x₁ ^ p ^ (n₃ + (n₂ + w₁ + w₂))
    = (x₁ ^ p ^ (n₂ + w₁)) ^ (p ^ (n₃ + w₂)) :
        by rw [← pow_mul, ← nat.pow_add]; simp only [add_assoc, add_left_comm]
... = (x₂ ^ p ^ (n₁ + w₁)) ^ (p ^ (n₃ + w₂)) : by dsimp only at h₁; rw h₁
... = (x₂ ^ p ^ (n₃ + w₂)) ^ (p ^ (n₁ + w₁)) : by rw [← pow_mul, ← pow_mul, mul_comm]
... = (x₃ ^ p ^ (n₂ + w₂)) ^ (p ^ (n₁ + w₁)) : by dsimp only at h₂; rw h₂
... = x₃ ^ p ^ (n₁ + (n₂ + w₁ + w₂)) :
        by rw [← pow_mul, ← nat.pow_add]; simp only [add_comm, add_left_comm]⟩⟩
```

#### [Kenny Lau (Oct 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135790417):
@**Mario Carneiro** @**Kevin Buzzard** For any field F, according to my approach, I build a big field extension L, and then extract the maximally purely inseparable subfield K, and then use this K to make things work. Here, K turns out to be the perfect closure of F. However, I can define the perfect closure of F constructively as a direct limit of F, as I have typed above. We can do the big field extension on top of the perfect closure of F instead of directly over F. This would increase the complexity of the definition of algebraic closure, but I feel like this approach is better because we can have a computable perfect closure.

#### [Kenny Lau (Oct 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135790424):
What do you think?

#### [Kevin Buzzard (Oct 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135790852):
Can you remind me what "the maximally purely inseparable subfield" of a field extension is? I thought maximal separable subextensions behaved well but inseparable extensions behaved less well. But as I told you once before I don't know this stuff at all; I only know what I lecture in Galois theory. I don't need to know about inseparable extensions at all in my work.

#### [Kenny Lau (Oct 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791109):
Let's call this big operation Big(F). So if F is a field, then Big(F) is an algebraic extension of F. The shortcut way to construct algebraic closure is basically direct limit of Big(...Big(Big(F))...).

The defining property of Big(F) is that **everything in F[X] has a root in Big(F)**.

Now, for the proper way, we still look at Big(F), but we extract the maximal purely inseparable subextension of Big(F) and call it Perf(F). Yes, in general you shouldn't look at the maximal purely inseparable subextension, but for this case it works fine. Now, we prove that **everything in Perf(F)[X] has a root in Big(F)**.

My observation is that this Perf(F) turns out to be the perfect closure of F, and is potentially useful, but unfortunately it's noncomputable here.

My new proposal is that we should define Perf(F) computable as I've defined above, and look at Big(Perf(F)) as the algebraic closure of F instead. I'm saying that this increases complexity but we're using the same property anyway (i.e. **everything in Perf(F)[X] has a root in _**) and if we do this then we have a computable perfect cosure.

#### [Kenny Lau (Oct 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791523):
@**Kevin Buzzard** I hope you can understand this and then explain this in a better way. I'm not particularly good at explaining stuff.

#### [Kevin Buzzard (Oct 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791628):
I don't know anything about char p.

#### [Kevin Buzzard (Oct 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791632):
I am still confused about this inseparable sub

#### [Kevin Buzzard (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791637):
I don't even know what inseparable means. Does it mean "not separable"?

#### [Kevin Buzzard (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791644):
You'll have to send me some links or something. I'm distracted by real life

#### [Kenny Lau (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791650):
For K/F and x in K, x is "purely inseparable" if x^(p^n) in F for some n.

#### [Kenny Lau (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791698):
https://stacks.math.columbia.edu/tag/09HD

#### [Kenny Lau (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791700):
https://stacks.math.columbia.edu/tag/046W

#### [Kevin Buzzard (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791704):
perfect thanks

#### [Kenny Lau (Oct 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135791719):
right, the second link is about perfect closure

#### [Kevin Buzzard (Oct 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792161):
Ok I understand what you're doing.

#### [Kenny Lau (Oct 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792164):
nice

#### [Kenny Lau (Oct 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792166):
maybe you should start caring about char p :P

#### [Kevin Buzzard (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792176):
Is it true that if L/K is some finite extension of fields and the maximal purely inseparable subextension of L is K again, then L/K is separable? I suspect that this is not true.

#### [Kenny Lau (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792184):
no it isn't true, I think

#### [Kenny Lau (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792187):
again, I'm not talking about the maximal purely inseparable subextension in general.

#### [Kevin Buzzard (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792193):
Ok so we have finally isolated the thing which I was worried about.

#### [Kevin Buzzard (Oct 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792198):
(deleted)

#### [Kenny Lau (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792235):
I'm talking about the perfect closure.

#### [Kenny Lau (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792240):
(deleted)

#### [Kevin Buzzard (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792241):
yes sorry, it's max insep sub you can't do, right?

#### [Mario Carneiro (Oct 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792242):
by the way your definition of char p is nonstandard, although I'm not sure whether I should care

#### [Kenny Lau (Oct 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792252):
make up your mind @**Mario Carneiro** :P

#### [Mario Carneiro (Oct 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792256):
you forgot to say that `(n : A) != 0` for `n < p`

#### [Mario Carneiro (Oct 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792261):
In the case where p is prime and 1 != 0, it's actually equivalent

#### [Kenny Lau (Oct 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792305):
I know

#### [Kenny Lau (Oct 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792311):
```quote
yes sorry, it's max insep sub you can't do, right?
```
I'll have to ask my friend

#### [Mario Carneiro (Oct 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792316):
but we will need a classification theorem about the existence of a characteristic, and I don't think there is any way to make that constructive

#### [Kevin Buzzard (Oct 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792326):
So we have this abstract (and non-constructive) construction in 22-27 of https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md which goes from a field F to an algebraic extension L/F with the property that every irred poly in F[X] has a root in L.

#### [Kenny Lau (Oct 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792329):
@**Mario Carneiro** but if we know the char then we can make it constructive

#### [Kevin Buzzard (Oct 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792372):
Kenny's observation is that a second way to construct L would be to start with F, then build its perfect closure (which is the direct limit F -> F -> F -> ... where all the maps are x->x^p)

#### [Kevin Buzzard (Oct 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792380):
and then apply the non-constructive construction to the perfection instead. Kenny is observing that this "spits out the same L"

#### [Kenny Lau (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792616):
```quote
yes sorry, it's max insep sub you can't do, right?
```
my friend says if K/F is insep then the max insep sub is K/F

#### [Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792659):
It's the phrase "the max insep sub" which I'm objecting to. I have no doubt it exists sometimes

#### [Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792663):
I'm not objecting, I'm trying to remember what one can and cannot do.

#### [Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792665):
There's some Keith Conrad notes on this stuff I think.

#### [Kenny Lau (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792666):
ok.

#### [Kenny Lau (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792669):
in general you can find the max sep sub and the max purely insep sub

#### [Kevin Buzzard (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792670):
right

#### [Kenny Lau (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792673):
given K/F, if S(K) is the max sep sub, then [S(K):F] = [K:F]_s

#### [Kenny Lau (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792678):
(is this an adjunction?)

#### [Mario Carneiro (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792688):
Yes, if you even know the negation of `char_zero` you can construct a finite characteristic

#### [Mario Carneiro (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792737):
Unfortunately I think a lot of ring theory is hard to do on characteristic almost-zero

#### [Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792749):
what do you mean by almost-zero

#### [Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792754):
```quote
Yes, if you even know the negation of `char_zero` you can construct a finite characteristic
```
that's nice

#### [Mario Carneiro (Oct 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792826):
I mean in that intuitionistic middle ground between finite and zero characteristic, where you've looked for a while and it looks pretty zero but you can't be sure

#### [Kenny Lau (Oct 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792833):
I see

#### [Mario Carneiro (Oct 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135792878):
I think a lot of arguments can be rephrased to "react to the discovery" that the ring is actually finite characteristic and rearrange the proof, but that's too much work for most mathematicians

#### [Kenny Lau (Oct 15 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135795521):
https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md

#### [Kenny Lau (Oct 15 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135795522):
@**Chris Hughes** you're the master of finiteness. How would you do 1?

#### [Kevin Buzzard (Oct 15 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796600):
The maths proof I know goes via observing that this finite group has the property that for all n there are at most n elements of order dividing n (because the poly $$X^n-1$$ has at most $$n$$ roots) and cyclic groups are the only finite groups with this property. Morally that's because of the structure theorem for finitely generated modules over a PID ;-)

#### [Kevin Buzzard (Oct 15 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796725):
What is this discussion doing in #general by the way? How did Chris prove it for Z/pZ? I'm pretty sure he needed it for QR.

#### [Kenny Lau (Oct 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796739):
oh right, lemme see...

#### [Kenny Lau (Oct 15 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796907):
ok it's proved in [`field_theory/finite.lean`](https://github.com/leanprover/mathlib/blob/master/field_theory/finite.lean#L148-L155) that the units group of every finite field is cyclic.

#### [Kevin Buzzard (Oct 15 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796911):
That's not strong enough for you

#### [Kenny Lau (Oct 15 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796912):
@**Mario Carneiro** the same proof can be used to prove that any finite subgroup of the units group of a field is cyclic, so this is not in the maximal generality.

#### [Kevin Buzzard (Oct 15 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796957):
yes it would not surprise me if the same proof could be made to work

#### [Kevin Buzzard (Oct 15 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135796960):
It's great that mathlib is so readable though, isn't it.

#### [Kevin Buzzard (Oct 15 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797132):
OK super-basic question: I've opened that file in Lean. How do I see the definition of `univ.filter` painlessly? If I right click on it I get sent to the definition of `finset.univ`

#### [Bryan Gin-ge Chen (Oct 15 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797137):
finset.filter is what you want, presumably

#### [Kevin Buzzard (Oct 15 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797138):
right, but I want to get there painlessly

#### [Kevin Buzzard (Oct 15 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797200):
The key result is `card_order_of_eq_totient` just before the one you linked to

#### [Kevin Buzzard (Oct 15 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797253):
```quote
finset.filter is what you want, presumably
```
*doh* only just realised that this has nothing to do with filters

#### [Kevin Buzzard (Oct 15 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797327):
Maybe the proof of `card_order_of_eq_totient` works with any finite subgroup of the units of alpha if alpha is any field.

#### [Kenny Lau (Oct 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797439):
I think it would be best for @**Chris Hughes** to re-prove this in more generality instead of us speculating what could be done

#### [Johan Commelin (Oct 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797742):
```quote
I think it would be best for @**Chris Hughes** to re-prove this in more generality instead of us speculating what could be done
```
We all know what is possible. Isn't this admitting defeat that mathlib is write-only code? Only the person that wrote the code can maintain it. That doesn't seem good to me.

#### [Kenny Lau (Oct 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797744):
wat kunnen we doen

#### [Johan Commelin (Oct 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797809):
In Engels praten?

#### [Kenny Lau (Oct 15 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797926):
what can we do

#### [Johan Commelin (Oct 15 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135797990):
We can think really hard about what we mean with "readable". @**Mario Carneiro** and @**Johannes Hölzl** say they can read mathlib, and I believe them. @**Patrick Massot** and I complain that we cannot read mathlib, and I hope others believe us. @**Kevin Buzzard** says he cannot read mathlib and he doesn't care (and I believe him). But in the end I think people should be able to maintain other peoples code.
The only other option is to seriously look into how we can clone Mario.

#### [Kevin Buzzard (Oct 15 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135799250):
I find it very hard to read, and impossible without it being open in Lean in front of me. I could probably struggle through a proof with lean though. The fact that I don't see why readability is important is perhaps a slightly different issue. If readability is important then I still don't really understand why we're not all writing lengthy tactic proofs, which are to be honest still my favourite proofs. But I am in no position to comment because it's the maintainers who know what's best so clearly they should (and do) have the final say -- I shall defer to their judgement on these issues.

#### [Kevin Buzzard (Oct 15 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135799291):
I guess a related issue is that I encourage undergraduates to write tactic proofs -- however Chris and Kenny made the switch no problem

#### [Kenny Lau (Oct 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135799712):
It actually surprises me that it took me quite a few hours to type out this document despite knowing the construction from top to bottom

#### [Kenny Lau (Oct 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135799713):
I guess it's just hard for me to organize my thoughts

#### [Kenny Lau (Oct 15 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135800612):
```lean
import data.padics.padic_norm data.nat.binomial

universe u

class char_p (α : Type u) [has_zero α] [has_one α] [has_add α] (p : ℕ) : Prop :=
(cast_eq_zero : (p:α) = 0)

theorem add_pow_char {α : Type u} [comm_ring α] {p : ℕ} (hp : nat.prime p)
  [char_p α p] (x y : α) : (x + y)^p = x^p + y^p :=
begin
  rw [add_pow, finset.sum_range_succ, nat.sub_self, pow_zero, choose_self],
  rw [nat.cast_one, mul_one, mul_one, add_left_inj],
  transitivity,
  { refine finset.sum_eq_single 0 _ _,
    { sorry },
    { intro H, exfalso, apply H, exact finset.mem_range.2 hp.pos } },
  rw [pow_zero, nat.sub_zero, one_mul, choose_zero_right, nat.cast_one, mul_one]
end

def frobenius (α : Type u) [monoid α] (p : ℕ) (x : α) : α :=
x^p

instance {α : Type u} [comm_ring α] (p : ℕ) (hp : nat.prime p) [char_p α p] : is_ring_hom (frobenius α p) :=
{ map_one := one_pow p,
  map_mul := λ x y, mul_pow x y p,
  map_add := add_pow_char hp }

inductive perfect_closure.r (α : Type u) [monoid α] (p : ℕ) : (ℕ × α) → (ℕ × α) → Prop
| intro : ∀ n x, perfect_closure.r (n, x) (n+1, x^p)

def perfect_closure (α : Type u) [monoid α] (p : ℕ) : Type u :=
quot (perfect_closure.r α p)

namespace perfect_closure

variables (α : Type u)

instance [comm_monoid α] (p : ℕ) : comm_monoid (perfect_closure α p) :=
{ mul := begin
    refine quot.lift (λ x:ℕ×α, quot.lift (λ y:ℕ×α, quot.mk _
      (x.1 + y.1, x.2^p^y.1 * y.2^p^x.1)) _) _,
    { intros y1 y2 H, cases H with n y,
      apply quot.sound,
      dsimp only,
      rw [← pow_mul, nat.mul_comm, pow_mul],
      rw [nat.pow_succ, pow_mul, ← mul_pow],
      constructor },
    intros x1 x2 H, cases H with m x,
    ext i,
    apply quot.induction_on i,
    rintro ⟨n, y⟩,
    apply quot.sound,
    dsimp only,
    rw [← pow_mul, nat.mul_comm, pow_mul],
    rw [nat.pow_succ, pow_mul, ← mul_pow, nat.succ_add],
    constructor
  end,
  mul_assoc := begin
    intros e f g,
    apply quot.induction_on e, rintro ⟨m, x⟩,
    apply quot.induction_on f, rintro ⟨n, y⟩,
    apply quot.induction_on g, rintro ⟨r, z⟩,
    simp only [add_assoc, mul_pow, nat.pow_add,
      (pow_mul _ _ _).symm, nat.mul_comm, mul_assoc],
  end,
  one := quot.mk _ (0, 1),
  one_mul := λ e, quot.induction_on e (λ ⟨n, x⟩,
    by simp only [nat.zero_add, one_pow, nat.pow_zero, one_mul, pow_one]),
  mul_one := λ e, quot.induction_on e (λ ⟨n, x⟩,
    show quot.mk _ _ = _,
    by simp only [nat.add_zero, one_pow, nat.pow_zero, mul_one, pow_one]),
  mul_comm := λ e f, quot.induction_on e (λ ⟨m, x⟩,
    quot.induction_on f (λ ⟨n, y⟩,
    show quot.mk _ _ = quot.mk _ _,
    by simp only [add_comm, mul_comm])) }

end perfect_closure
```

#### [Scott Morrison (Oct 15 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135803490):
I find it very hard to read most of mathlib, and I think we're making a mistake leaving things so unreadable!

#### [Mario Carneiro (Oct 15 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135803507):
I don't try to read mathlib without lean running

#### [Mario Carneiro (Oct 15 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135803512):
and I don't think that we can reasonably achieve that level of readability (I don't think it's the direction we are going)

#### [Mario Carneiro (Oct 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135803562):
Tactic proofs are readable since you can step through all the steps, and term proofs are readable because they have bounded complexity, as long as you can get at the types of things

#### [Mario Carneiro (Oct 15 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135803615):
```quote
```quote
I think it would be best for @**Chris Hughes** to re-prove this in more generality instead of us speculating what could be done
```
We all know what is possible. Isn't this admitting defeat that mathlib is write-only code? Only the person that wrote the code can maintain it. That doesn't seem good to me.
```
I assume the reason Kenny said this is because Chris has the best understanding of the formalization choices and relevant proof approaches, not because he's the only one who can read his proof

#### [Johan Commelin (Oct 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135806498):
Readable with Lean open is good enough for me. But I can't even read term-mode proofs with Lean open. (Unless I work really really hard, but usually I just give up.)

#### [Bryan Gin-ge Chen (Oct 15 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135807472):
I have noticed the following trade-off in functionality of the VS code extension. If I hover over some defined variables / hypotheses in a tactic mode proof, often lean just gives me something useless like the definition of `exact` or `rw` or `intro`. Hovering is more reliably useful inside term mode proofs.

#### [Bryan Gin-ge Chen (Oct 15 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135807534):
It also would be nice if that type info from hovering could be displayed in the infoview window, so that it's not just completely blank when I'm examining a term-mode proof.

#### [Mario Carneiro (Oct 15 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135807689):
It will actually give you term mode information if it's actually an expr parser in the tactic (such as after `exact` or in `rw` brackets)

#### [Mario Carneiro (Oct 15 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135807692):
but the name parser doesn't give you any information, so `intro` hovering doesn't work

#### [Bryan Gin-ge Chen (Oct 15 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135808091):
What do you mean by an "expr parser"? 

Sometimes I get useful info in exact, but I find that [more often than not I don't:](/user_uploads/3121/36syMjdcu-ypF40akvYCYOVf/Screenshot-2018-10-15-01.16.27.png) 

The cursor disappeared when I took the screenshot, but it's hovering over the `ha` near the bottom left corner of the popup.

#### [Kevin Buzzard (Oct 15 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135809910):
This thread arguably isn't the right place for this conversation -- which I do think is interesting. I think there could be a place for Lean which is comprehensible to humans -- but maybe that's not mathlib. [Here's the answer to some homework](https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/example_sheet_01/Sht1Q2/S0102.lean). I'm not sure anyone reads Bourbaki either.

#### [Chris Hughes (Oct 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135826061):
```quote
@**Mario Carneiro** the same proof can be used to prove that any finite subgroup of the units group of a field is cyclic, so this is not in the maximal generality.
```
https://github.com/leanprover/mathlib/pull/423

#### [Chris Hughes (Oct 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135826105):
@**Kenny Lau**

#### [Johan Commelin (Oct 15 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135826327):
@**Chris Hughes** Nice! But I think that what Kenny is after is more general. For any arbitrary field `K` it is true that every finite subgroup of `units K` is cyclic.

#### [Kevin Buzzard (Oct 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135833000):
Sure but it [subgroup of cyclic is cyclic]'s pretty darn useful!

#### [Kevin Buzzard (Oct 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135833012):
It's used all the time in 2nd year algebra, which I would imagine Chris is learning now.

#### [Kenny Lau (Oct 15 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135861242):
```lean
def frobenius (α : Type u) [monoid α] (p : ℕ) (x : α) : α :=
x^p
```
@**Mario Carneiro** do you think I should make this definition at all?

#### [Mario Carneiro (Oct 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135861271):
Only if you can layer some additional structure on it

#### [Kenny Lau (Oct 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135861281):
what do you mean?

#### [Mario Carneiro (Oct 15 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135861357):
like if you define a bundled homomorphism or something

#### [Kenny Lau (Oct 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135861497):
```lean
inductive perfect_closure.r (α : Type u) [monoid α] (p : ℕ) : (ℕ × α) → (ℕ × α) → Prop
| intro : ∀ n x, perfect_closure.r (n, x) (n+1, frobenius α p x)
```

#### [Kenny Lau (Oct 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135861499):
like this?

#### [Kenny Lau (Oct 16 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135866443):
```lean
theorem frobenius_mul (α : Type u) [comm_monoid α] (p : ℕ) (x y : α) :
  frobenius α p (x * y) = frobenius α p x * frobenius α p y := mul_pow x y p
theorem frobenius_iterate_mul (α : Type u) [comm_monoid α] (p n : ℕ) (x y : α) :
  frobenius α p^[n] (x * y) = (frobenius α p^[n] x) * (frobenius α p^[n] y) :=
by induction n; [simp only [nat.iterate_zero], simp only [nat.iterate_succ', frobenius_mul, *]]
theorem frobenius_one (α : Type u) [monoid α] (p : ℕ) :
  frobenius α p 1 = 1 := one_pow _
theorem frobenius_iterate_one (α : Type u) [comm_monoid α] (p n : ℕ) :
  frobenius α p^[n] 1 = 1 :=
by induction n; [simp only [nat.iterate_zero], simp only [nat.iterate_succ', frobenius_one, *]]
```

#### [Kenny Lau (Oct 16 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135866446):
what's the right way to achieve maximum generality?

#### [Johan Commelin (Oct 16 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135869283):
My first personal reaction is that `p` should be the first parameter.

#### [Kenny Lau (Oct 16 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135914776):
https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean

#### [Kenny Lau (Oct 16 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135914788):
@**Mario Carneiro** how is this? Is it mathlib ready?

#### [Mario Carneiro (Oct 16 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135919893):
It's okay, I have some comments but they would be best put on a PR. But sure, there is no structural problem with having this in mathlib

#### [Kenny Lau (Oct 17 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/135956262):
https://github.com/leanprover/mathlib/pull/425

#### [Chris Hughes (Oct 18 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136062832):
I generalized my theorem to any finite subgroup of an integral domain. What file should it go in since it's no longer particular to finite fields?

#### [Kenny Lau (Oct 18 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136066001):
@**Mario Carneiro**

#### [Mario Carneiro (Oct 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136066041):
Not sure, what's the most advanced stuff you use?

#### [Mario Carneiro (Oct 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136066092):
Maybe somewhere in `ring_theory` basics or something

#### [Chris Hughes (Oct 18 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136066451):
Polynomials and `group_theory.order_of_element`.

#### [Mario Carneiro (Oct 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136066599):
do either of those depend on the other?

#### [Chris Hughes (Oct 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/136067170):
No.

#### [Kenny Lau (Nov 05 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146801908):
The first step is merged!

#### [Kenny Lau (Nov 05 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146801910):
@**Kevin Buzzard**

#### [Kevin Buzzard (Nov 05 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146802277):
Nice! Algebraic closures are so key to everything. I would like to one day start stating non-trivial facts about p-adic Galois representations, which are representations of the absolute Galois group of a number field -- these things are a key part of the Langlands philosophy. Galois theory and algebraic closures are a key part of this dream. I would imagine that many other theorem provers have Galois theory and algebraic closures and p-adic numbers in some form, but with Lean it sort-of feels like they will all be in the same place at the same time and one could start thinking about these far deeper things once they're there.

#### [Kenny Lau (Nov 05 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146803609):
https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md

#### [Kenny Lau (Nov 05 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146808711):
and we have perfect closure now! @**Kevin Buzzard**

#### [Kenny Lau (Nov 06 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146889094):
@**Kevin Buzzard** I have finished proving hilbert basis theorem

#### [Kevin Buzzard (Nov 06 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146889213):
nice! Now you can prove that if B is a finitely-generated algebra over a noetherian ring then B is Noetherian

#### [Johan Commelin (Nov 06 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146889239):
Also... do we already know that `int` is noetherian :lol:

#### [Kevin Buzzard (Nov 06 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146889310):
One should prove that PID's are Noetherian and that int is a PID I guess

#### [Kevin Buzzard (Nov 06 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146889320):
Both of these might be in / easy

#### [Johan Commelin (Nov 06 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146889347):
The latter is in.

#### [Patrick Massot (Nov 06 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146890579):
It seems like https://github.com/leanprover-community/mathlib/blob/f7fde9faf98efa91d49e8f699263d72b3c4d5b0f/ring_theory/hilbert_basis.lean begins with lots of lemmas that should be moved to other files

#### [Patrick Massot (Nov 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146894970):
@**Kenny Lau** could you comment on how you felt that our API to polynomials and modules was behaving during your proof of Hilbert basis?

#### [Kenny Lau (Nov 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146894976):
eh... can be better

#### [Patrick Massot (Nov 06 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146895260):
do you have specific ideas?

#### [Kenny Lau (Nov 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146904524):
Actually there isn't many problems, it's just some missing lemmas.

#### [Kenny Lau (Nov 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/146904535):
which isn't a big deal at all, because one can just add them in

#### [Kenny Lau (Nov 09 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147365605):
@**Kevin Buzzard** @**Johan Commelin** We will have integral closure by tonight

#### [Johan Commelin (Nov 09 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147366017):
Cool!

#### [Kevin Buzzard (Nov 09 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147368104):
Shouldn't you be catching up on all the lectures you missed while you were absent from your course? ;-)

#### [Kenny Lau (Nov 10 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147412357):
I shall continue tomorrow.

#### [Kenny Lau (Nov 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449421):
We have integral closure now.

#### [Kevin Buzzard (Nov 10 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449645):
Can you prove that the integers of a number field are a Dedekind domain?

#### [Kenny Lau (Nov 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449656):
wow you keep pushing me

#### [Kevin Buzzard (Nov 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449665):
There are a bunch of equivalent definitions

#### [Kevin Buzzard (Nov 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449709):
The one which would be easiest would be to show that if K is a field of char 0 which is finite-dimensional over Q then the integral closure of Z in this field (the ring of integers) is Noetherian, an integral domain, integrally closed, and that every non-zero prime ideal is maximal.

#### [Kevin Buzzard (Nov 10 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449719):
The latter follows from the fact that a non-zero ideal contains an integer and hence the quotient of the ring of integers by a non-zero ideal is a finite set, and then observe that a finite integral domain is a field.

#### [Kevin Buzzard (Nov 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449759):
The reason this is of interest is that one of the main theorems in an undergraduate algebraic number theory course is that every non-zero ideal in the integers of a number field factors uniquely into prime ideals

#### [Kevin Buzzard (Nov 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449765):
however the correct generality in which this theorem should be proved is that it's true for all Dedekind domains

#### [Kevin Buzzard (Nov 10 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449774):
Ok here is a more reasonable question: can you prove that the integral closure of the integral closure is the integral closure?

#### [Kevin Buzzard (Nov 10 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449777):
I mean if $$R\subseteq S$$ and $$R'$$ is the integral closure of $$R$$ in $$S$$ and then $$R''$$ is the integral closure of $$R'$$ in $$S$$ then $$R'=R''$$.

#### [Kevin Buzzard (Nov 10 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147449816):
Then you'd know that the ring of integers of a number field is integrally closed in its field of fractions

#### [Kenny Lau (Nov 10 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147450331):
sure, give me another weekend...

#### [Kevin Buzzard (Nov 10 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451036):
I must be honest, I would rather see Gal(Q-bar/Q)...

#### [Kevin Buzzard (Nov 10 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451038):
no wait

#### [Kevin Buzzard (Nov 10 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451041):
I would rather see all of these things

#### [Kevin Buzzard (Nov 10 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451096):
Kenny here is a genuine much harder challenge. I would like to see a continuous group homomorphism from the absolute Galois group of $$\mathbb{Q}$$ to $$GL_n(\mathbb{Z}_p)$$, unramified outside a finite set $$S$$ of places.

#### [Kevin Buzzard (Nov 10 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451104):
Everything you are doing is in some sense working up to this; it's a fundamental object in Langlands' philosophy.

#### [Kevin Buzzard (Nov 10 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451108):
I'm sure Johan would be equally pleased to see this. One motivation for doing it is, just like perfectoid spaces, it is a fundamental object in modern number theory which seems to me to be a million miles from anything in any theorem prover at this point. And it really is not that difficult to do, in some sense. All the things you're doing are important for the definition of this object.

#### [Kevin Buzzard (Nov 10 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451221):
I think we have $$GL_n(\mathbb{Z}_p)$$, the topology is not hard, and you are working towards the absolute Galois group.

#### [Kevin Buzzard (Nov 10 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451293):
An even longer term goal would to be to formalise the statement of the conjecture that Toby and I make in https://arxiv.org/abs/1009.0785 (conjecture 3.2.1). This is a rigorous statement which one could argue is a formalisation of what part of Langlands' philosophy is.

#### [Kevin Buzzard (Nov 10 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147451343):
Before this paper, everyone knew that something like 3.2.1 should be true but nobody had stated it precisely, and several people were well aware that more naive guesses as to what the conjecture should be were provably false.

#### [Kevin Buzzard (Nov 11 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147452506):
This thread should be in #maths, by the way. Is it possible to change it?

#### [Kevin Buzzard (Nov 11 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147452517):
Kenny, here's another reasonable suggestion: https://en.wikipedia.org/wiki/Going_up_and_going_down . I have Bruns-Herzog in my office if you need a copy.

#### [Kevin Buzzard (Nov 11 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147452559):
This is the correct way to prove that non-zero prime ideals are maximal in the integers of a number field.

#### [Kevin Buzzard (Nov 11 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147452566):
And Matsumura

#### [Kenny Lau (Nov 11 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Algebraic closure roadmap/near/147479317):
```quote
I mean if $$R\subseteq S$$ and $$R'$$ is the integral closure of $$R$$ in $$S$$ and then $$R''$$ is the integral closure of $$R'$$ in $$S$$ then $$R'=R''$$.
```
@**Kevin Buzzard** @**Johan Commelin** done

