---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/59003generators.html
---

## Stream: [kbb](index.html)
### Topic: [generators](59003generators.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838138):
I just saw Kenny's work on generating SL2Z. It looks impressive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838160):
But I wonder how to properly generalize it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838169):
```quote
I just saw Kenny's work on generating SL2Z. It looks impressive
```
thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838236):
I would have expected to see a predicate saying: this set generate this group. And then a mechanism constructor the eliminator from this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838249):
Is this counter-intuitive order related to constructivity?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838264):
not constructivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838278):
it's just the same reason we don't take quot.exists_rep as an axiom, but rather quot.ind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838398):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838466):
it's easier to use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838826):
Do you think there could be some tactic consuming a proof of generation and building the eliminator?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838930):
I don't know about tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838972):
Maybe a tactic is not needed, I'm only trying to understand whether there could be an interface which looks more natural (to me at least)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839028):
@**Mario Carneiro** Do you have any insight? We are discussing https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L49 and https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L97

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839676):
```
protected theorem induction_on {C : SL2Z → Prop} (A : SL2Z)
  (H1 : C 1) (HS : ∀ B, C B → C (S * B))
  (HT : ∀ B, C B → C (T * B)) : C A :=
```
It's amazing how little this tells me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839680):
everything is letters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839695):
S and T are explicit elements of SL2Z defined a few lines earlier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839707):
So this theorem is a really weird way to state those elements generate SL2Z

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839714):
there is an `SL2Z` attribute?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839766):
https://github.com/semorrison/kbb/blob/master/src/modular_group.lean#L6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839773):
seems like a fine induction statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839785):
Sure. But the question is: what is the proper general context and interface? Dealing with generating sets for groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839796):
I don't think we have `span` for groups yet, I'm working on improving span for modules and we can do something similar in groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839840):
I guess it's usually called closure in groups?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839844):
I did spans for group a *very* long time ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839848):
in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839849):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839850):
I think I recall

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839853):
I think closure is in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839856):
It's the first thing I did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839858):
you were doing something with norms in groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839885):
https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/invariant_norms.lean#L107

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839888):
But we don't need the general theory for this theorem, and it won't make the proof any easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839892):
given what is currently available, this theorem is fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839935):
Yes. I was trying to formalize the trivial part of https://arxiv.org/abs/1803.07997

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839947):
if and when we get spans in groups it would be natural to state `span {S, T} = top`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839970):
guys, it's just closure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840001):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840002):
From `subgroup.lean` 
```lean
inductive in_closure (s : set α) : α → Prop
| basic {a : α} : a ∈ s → in_closure a
| one : in_closure 1
| inv {a : α} : in_closure a → in_closure a⁻¹
| mul {a b : α} : in_closure a → in_closure b → in_closure (a * b)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840007):
It's not my question though: I would like to first prove the span is everything, and then deduce the eliminator, not the other way around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840017):
the proofs will be the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840087):
Even better then. We can write things like we do in maths and have the same proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840112):
ah, okay so you can write `closure {S, T} = univ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840133):
and the proof is to prove `in_closure {S, T}` by exactly the same induction argument as used in that big proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840136):
Mario, did you follow both links of the messages when I pinged you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840151):
The second linked line contains `closure {S, T} = univ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840158):
ah, so it does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840236):
However, the induction statement is a bit stronger than what you get from `closure`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840251):
it says that `S` and `T` generate the group as a monoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840253):
My questions were: 1) could we directly prove `closure {S, T} = univ` without more pain (you seem to say yes) 2) could you generate the induction statement automatically from there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840273):
there is no mention of inverses in the induction theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840290):
but in the closure of a group you need to also assume closure by inverses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840314):
so the real equivalent statement would be `monoid.closure {S, T} = univ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840371):
Ok, let's assume we also define `monoid.closure`. How do we generate the eliminator?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840380):
Would that be a tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840383):
no, a theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840392):
`monoid.closure` would be defined by an inductive type just like `in_closure` is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840398):
and its eliminator is basically exactly that theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840409):
You would prove that {x | C x} is a monoid containing `{S, T}` and so deduce it is `univ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840477):
Would you need to redo that for every generating set of every group, or would you have a general theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840497):
the general theorem *is* the eliminator for `in_closure`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840526):
the part that needs to be redone is the unfolding of the set `{S, T}` into two induction hypotheses about multiplying by `S` and `T`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133841661):
I tried to do the exercise, but clearly I missed something because it looks very complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133841998):
I wrote, at the end of that file:
```lean
section
variables {α : Type*} [group α]
inductive monoid.in_closure (s : set α) : α → Prop
| basic {a : α} : a ∈ s → monoid.in_closure a
| one : monoid.in_closure 1
| mul {a b : α} : monoid.in_closure a → monoid.in_closure b → monoid.in_closure (a * b)


def monoid.closure (s : set α) : set α := {a | monoid.in_closure s a }
end

@[elab_as_eliminator]
protected theorem induction_on' {C : SL2Z → Prop} (A : SL2Z)
  (H1 : C 1) (HS : ∀ B, C B → C (S * B))
  (HT : ∀ B, C B → C (T * B)) : C A :=
begin
  
  have : monoid.in_closure ({S, T} : set SL2Z) A := sorry,
  apply monoid.in_closure.rec_on this _ H1,
  sorry
end
```
The first sorry is irrelevant. But the tactic state after the first sorry is not what I was hoping for. I tried to move on but it looked too complicated to be what you suggested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133842668):
There is a theorem that `in_closure` can be generated by only left multiplication by the generators

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133842747):
If you want it to be by definition, you will need the following definition for `monoid.in_closure`
```
inductive monoid.in_closure (s : set α) : α → Prop
| one : monoid.in_closure 1
| mul_basic {a b : α} : a ∈ s → monoid.in_closure b → monoid.in_closure (a * b)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843061):
Ok, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843071):
That theorem is indeed what I saw I needed to prove, and I was confused because it seemed to contradict the announced triviality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843094):
With the stronger definition of `monoid.in_closure`, the new proof is
```lean
@[elab_as_eliminator]
protected theorem induction_on' {C : SL2Z → Prop} (A : SL2Z)
  (H1 : C 1) (HS : ∀ B, C B → C (S * B))
  (HT : ∀ B, C B → C (T * B)) : C A :=
begin
  have : monoid.in_closure ({S, T} : set SL2Z) A := sorry,
  apply monoid.in_closure.rec_on this H1,
  intros A B H,
  cases H ; intro h ; finish
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843118):
which looks like it could admit a general version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843177):
Now, I need to go to bed, but I'll probably come back to all this tomorrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 12 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843182):
Thanks again!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860592):
@**Kenny Lau** A really cool way to generalise this is to apply this strategy to the action of `SL2Z` on matrices with determinant `m`. You get the same sort of "Euclidean algorithm"-like induction steps. The end result is that you prove that every matrix is equivalent to $$\begin{pmatrix} a & b \\ 0 & d \end{pmatrix}$$, where $$a \cdot d = m,\quad a > 0,\quad d > 0$$, and $$0 \le b < d$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860598):
In particular, the set of orbits is finite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860606):
If you apply this to the case `m = 1` you recover the result that `S` and `T` generate `SL2Z`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860657):
Once we know this set is finite for arbitrary `m : int`, then we can define Hecke operators!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860676):
I think that would be a really cool move.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865425):
@**Kenny Lau** What do you think of this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865474):
great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865482):
How hard do you think it is to adapt your proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865538):
maybe 30% hard!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865539):
can't wait to see someone implement it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865541):
Lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865606):
Do we have notation for group actions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865720):
I used `\ci` a long time ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865802):
But it is not in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865874):
it isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865918):
Hmm, so I generalised the simp lemmas a bit. Now I need to cook up a new induction statement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865931):
Should `C 1` be replaced by the explicit representatives that I described above?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866151):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866338):
@**Kenny Lau** Does this look good?
```lean
protected theorem induction_on {C : (Mat m) → Prop} (A : Mat m)
  (H0 : ∀ {a b d : ℤ} (h1 : a * d = m) (h2 : 0 < a) (h3 : 0 < d) (h4 : 0 ≤ b) (h5 : b < d), C ⟨a,b,0,d,by simp [h1]⟩)
  (HS : ∀ B, C B → C (SL2Z_M_ m S B)) (HT : ∀ B, C B → C (SL2Z_M_ m T B)) : C A :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866356):
what if m is negative?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866357):
or 0?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866417):
Hmm, good point, I guess I should drop my requirement on `d`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866422):
Let me think it through...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866507):
For `m = 0` the statement might be false.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866514):
You have matrices `(a, 0, 0, 0)`. And I think they are not sharing orbits, are they?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866572):
So I drop `h3`, and `h5` becomes `b < (abs d)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866862):
What is the general strategy to kill this goal:
```lean
H : C {a := B.a, b := B.b, c := B.c, d := B.d, det := _}
⊢ C B
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866866):
`exact H` doesn't work. Somehow I'dd like to prove it by some extensionality or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867094):
Did you try convert H ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867109):
`cases B; exact H`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867838):
Kenny's solution is more efficient. But I think it's still good to keep in mind that `convert H, cases B, congr` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867881):
Because `convert H` is a natural thing to try when `exact H` refuses to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867887):
I disagree

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867892):
`congr` can go uncontrollable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867893):
(`convert` is just a kind of `congr`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867908):
I'm not saying this will always work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867912):
I'm saying we shouldn't make `convert` our "first resort"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867952):
for lack of a better word

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868391):
Here is what I've got so far
```lean
@[elab_as_eliminator]
protected theorem induction_on {C : (Mat m) → Prop} (A : Mat m)
  (H0 : ∀ {a b d : ℤ} (h1 : a * d = m) (h2 : 0 ≤ a) (h3 : 0 ≤ b) (h4 : b ≤ d ∨ b ≤ -d), C ⟨a,b,0,d,by simp [h1]⟩)
  (HS : ∀ B, C B → C (SL2Z_M_ m S B)) (HT : ∀ B, C B → C (SL2Z_M_ m T B)) : C A :=
have hSid : ∀ B, (SL2Z_M_ m S (SL2Z_M_ m S (SL2Z_M_ m S (SL2Z_M_ m S B)))) = B, from λ B, by ext; simp [SL2Z_M_],
have HS' : ∀ B, C (SL2Z_M_ m S B) → C B,
  from λ B ih, have H : _ := (HS _ $ HS _ $ HS _ ih), by rwa hSid B at H,
have hTinv : ∀ B, SL2Z_M_ m S (SL2Z_M_ m S (SL2Z_M_ m S (SL2Z_M_ m T (SL2Z_M_ m S (SL2Z_M_ m T (SL2Z_M_ m S B)))))) = SL2Z_M_ m T⁻¹ B,
  from λ B, by repeat {rw [←is_monoid_action.mul (SL2Z_M_ m)]}; congr,
have HT' : ∀ B, C B → C (SL2Z_M_ m T⁻¹ B),
  from λ B ih, by {have H := (HS _ $ HS _ $ HS _ $ HT _ $ HS _ $ HT _ $ HS _ ih), by rwa [hTinv] at H},
-- have HT2 : ∀ n : ℤ, C (T^n),
--   from λ n, int.induction_on n H1
--     (λ i ih, by rw [add_comm, gpow_add]; from HT _ ih)
--     (λ i ih, by rw [sub_eq_neg_add, gpow_add]; from HT1 _ ih),
have HT3 : ∀ B, C (SL2Z_M_ m T B) → C B, from λ B ih,
  begin
    have H := HT' (SL2Z_M_ m T B) ih,
    rw [←is_monoid_action.mul (SL2Z_M_ m)] at H,
    simp at H,
    rw [is_monoid_action.one (SL2Z_M_ m)] at H,
    exact H
  end,
have HT4 : ∀ B, C (SL2Z_M_ m T⁻¹ B) → C B, from λ B ih,
  begin
    have H := HT (SL2Z_M_ m T⁻¹ B) ih,
    rw [←is_monoid_action.mul (SL2Z_M_ m)] at H,
    simp at H,
    rw [is_monoid_action.one (SL2Z_M_ m)] at H,
    exact H
  end,
have HT5 : ∀ B (n:ℤ), C (SL2Z_M_ m (T^n) B) → C B, from λ B n,
  int.induction_on n (by rw [gpow_zero, is_monoid_action.one (SL2Z_M_ m)]; from id)
    (λ i ih1 ih2, ih1 $ HT3 _ $ begin
      conv { congr, rw ←is_monoid_action.mul (SL2Z_M_ m) },
      conv at ih2 { congr, rw [add_comm, gpow_add, gpow_one] },
      assumption end)
    (λ i ih1 ih2, ih1 $ HT4 _ $ begin
      conv { congr, rw ←is_monoid_action.mul (SL2Z_M_ m) },
      conv at ih2 { congr, rw [sub_eq_neg_add, gpow_add, gpow_neg_one] },
      assumption end),
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868669):
Isn't it even more contrived to prove first the induction lemma in that case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868818):
I don't know. But if we want Hecke operators, we need it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868845):
Why don't you want to state the result you need in the way you would state it on paper, and then deduce the induction statement?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869045):
Is there an available written proof you are trying to follow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869613):
No, I just cooked up a proof this morning.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869619):
There are probably proofs around, but I haven't found one yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869714):
Do you need help here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870014):
I'm learning :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870584):
I've pushed a proof that has 1 `sorry` for the case `A.c = 0`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870594):
I still need to learn how to juggle around hypotheses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870643):
A mathematician says: Ooh, if `A.a ≤ 0` then replace `A` by `-A`. I find it hard to make such a step in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870668):
@**Kenny Lau** Do you want to teach me?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870692):
where did you push?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870698):
well `S*S*A = -A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870707):
so you prove it for `S*S*A` first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870708):
Fail... I only commited. Now I pushed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870763):
I have `hneg : ∀ (B : Mat m), SL2Z_M_ m S (SL2Z_M_ m S B) = -B` in my context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870798):
I also see `n n : ℕ,` which is a good recipe for confusion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870954):
That is because of the `strong_induction`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870981):
I don't understand why `strong_induction` does this, but we could safely forget about the first `n`. It has played it's role, and the new `n` took over.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870997):
Why don't you use another name for the new `n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133871066):
Anyway, I can't help with this sorry without knowing what is the paper proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133871215):
Never mind. I might have found a way out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133876350):
I did find a way out, but it is becoming pretty crazy. (I also had lunch. Please don't be worried that I kept banging my head against this wall for 3 hours.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133876357):
@**Kenny Lau** Would you want to take over?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133876502):
I’m not free now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133879346):
There are 3 `sorry`s left in https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L118-L125,

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133879350):
they should all be `by schoolkid`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133886099):
Let's say I try the first one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887384):
Ooh, I was just trying that one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887395):
I'm almost there!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887396):
I just finished a maths paper. So I am allowing myself some Lean time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887413):
@**Patrick Massot** I only need `1 ≤ A.d * A.d`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887417):
I'm at `this : A.d * A.d > 0
⊢ A.d * A.d - 1 ≥ 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887434):
Right, same place (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887447):
I'll move to sorry₂

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887464):
Oh no, for Lean it's not the same place

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887759):
I'm soo close `this : A.d * A.d > 0 ⊢ 1 ≤ A.d * A.d`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888301):
Done!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888383):
Should I move to the third one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888446):
Yes please.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888450):
Did you push?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888471):
Do you want me to push?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888556):
I pushed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888816):
This should be a standard lemma: `A.b / A.d * A.d ≤ A.b` But I can't find it...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888868):
What is this `/`? Euclidean quotient?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888951):
seems so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889038):
Right, so `(11 / (-3)) = -3`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 13 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889145):
`int.div_mul_le`? Are you working over `int`? I'm not really following the context.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889184):
bingo!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889768):
@**Johan Commelin** Are you sure this sorry is true?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889783):
It actually looks really weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889898):
I'm done with 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889907):
You're worried about 3?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889911):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890106):
Hmm, I think it is fine. Proof by example: `abs (101 - (101/13 * 13)) ≤ abs(13)`, which reduces to `10 ≤ 13`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890209):
By the way, I pushed my fix of sorry₂

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890585):
hold on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890611):
You sent me on a wrong track to make sure you'll be done first!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890810):
Guess what, I have to catch a train. So I won't be Leaning for the next 90 minutes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890829):
And now you set me a deadline!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890833):
And I haven't made any progress on sorry₃

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890842):
@**Kenny Lau** is online :time_ticking:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890852):
hi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133893902):
done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133893911):
so much suffering...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898166):
@**Patrick Massot** Thank you so much!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898533):
The stupid lemma in the middle is now in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898624):
I also removed a couple of simp that were in the middle of the proof hence frowned upon

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898828):
Ok, I realised that it might have been easier to assume `m > 0`. And then deduce the result for negative `m` via an `SL2Z`-equivariant isom between `Mat m` and `Mat -m`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898847):
Anyway, the next step would be to use this horrible lemma to prove that for `m ≠ 0` the set of orbits of `SL2Z_M_` is finite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898860):
Once we have that, we can define the Hecke operator.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133905932):
@**Kenny Lau** Are you interested in golfing what we came up with?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133905941):
after I finish with my PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133906100):
Which PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133906246):
https://github.com/leanprover/mathlib/pull/345

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133906679):
Nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133912059):
I made a small start on SL2Z\SL2ZM, simply telling Lean what this mean, and somehow stating what I think Johan told us we should prove in order to get finiteness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133912075):
But what is stated may be false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 13 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133912087):
and the names are stupid too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133922532):
Thanks! That is exactly what I had in mind. (I do think we might need a bit more conditions in `reps`. I think we can/should just copy the condition from `H0` in the induction lemma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133922587):
The set of orbits is only finite if `m ≠ 0`. Otherwise it is parameterised by pairs of coprime integers (up to ±1).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937043):
Done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937107):
Note that a small modification of the setup is required to recover the generation theorem for SL2. The relevant action is not the action of the full SL2 on Mat m, but only the monoid spanned by S and T. But otherwise the proof should be the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937363):
Cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937413):
I guess for the finiteness result that is still sorried, we could do the dual thing. Build an injection into a product of `fin`s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938572):
are we going to restate the SL2Z theorem as a special case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938580):
also, it doesn't compile because someone deleted mul_self_pos

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938658):
It does compile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938662):
`mul_self_pos` is now in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938669):
Did you try to compile using `leanpkg build`? (hint: the correct answer is yes)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938729):
Yes, we could restate the SL2Z theorem as a special case. It should cost much and will be convenient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938734):
Feel free to do so, I need to do real work now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938801):
```quote
`mul_self_pos` is now in mathlib
```
well I haven't updated mathlib, that's why

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133939553):
leanpkg will do that for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133939561):
Use leanpkg build

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133939915):
And restart Lean in VScode afterwards...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971124):
@**Patrick Massot**  you see... I might change your proof if you don't mind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971164):
I just pushed a first start on hecke operators...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971202):
@**Kenny Lau** Please assume `m > 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971249):
what do you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971264):
It will probably make your life easier. And I now realise that we won't ever use `m < 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971274):
Not in this project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971281):
oh well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971297):
And outside the project, the can deduce the result by an `SL2Z`-equivariant map `Mat m → Mat -m`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971327):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971438):
```quote
Patrick Massot  you see... I might change your proof if you don't mind
```
I have no idea what you are talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971446):
your whole induction_on proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971559):
It's not my proof, I only contributed a handful of schoolkid lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971567):
oh, @**Johan Commelin** then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971673):
@**Kenny Lau** Sure, go ahead!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133972834):
@**Johan Commelin** this is the original base case:
```lean
(H0 : ∀ {A : Mat m} (h0 : A.c = 0) (h1 : A.a * A.d = m) (h2 : 0 ≤ A.a) (h3 : 0 ≤ A.b) (h4 : int.nat_abs A.b ≤ int.nat_abs A.d), C A)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133972846):
it can be changed to:
```lean
(H0 : ∀ {A : Mat m} (h0 : A.c = 0) (h1 : A.a * A.d = m) (h2 : 0 < A.a) (h3 : 0 ≤ A.b) (h4 : int.nat_abs A.b < int.nat_abs A.d), C A)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133972966):
1) `h1` is redundant. It follows from `h0` and `A.det`. (I realised this half-way writing my own proof.)
2) Now you have no upper-bound on `A.b`. So how will you prove finiteness of orbits?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973018):
what do you mean I have no upper-bound on A.b?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973037):
I changed two `le` to `lt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973041):
it restricted things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973056):
Aah, sorry, I didn't see the `h4`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973068):
Yes, I know you could make those restrictions, but I didn't know if it would make the proof easier.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973071):
I thought things would get harder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973178):
I always do more work to ensure that the users do less work


{% endraw %}
