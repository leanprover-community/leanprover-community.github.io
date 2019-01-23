---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/77646Workingwithfinnandite.html
---

## Stream: [maths](index.html)
### Topic: [Working with `fin n` (and `ite`?)](77646Workingwithfinnandite.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534552):
How should I do this:
```lean
definition helpme {n : ℕ} (i : fin (n+1)) (f: fin n → ℝ) : fin (n+1) → ℝ := sorry
-- λ k, if k < i then f ⟨k, sorry⟩ else if k = i then 0 else f (nat.pred k)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534604):
As you can see, I have a definition that almost works. (And I could get rid of the `sorry` in the middle by digging through some files in mathlib.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534611):
if `k : fin n` then `k` is a pair consisting of a nat and a proof that the nat is less than `n`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534614):
You can access each element of the pair with `k.1` and `k.2` for example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534617):
But I am not sure if this is the right way to define this... for example, I want to prove that `helpme f` takes positive values if `f` does...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534630):
And I just get a goal `0 < ite ...` and I have no way how to tackle that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534685):
yeah, these CS people don't like `if`, I think it must be the new `goto` (for people old enough to remember that command)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534688):
@**Johan Commelin** the first step is to simplify the problem: I guess you want a function like `fin n -> fin (n+1)`. This can be done by doing it on the naturals (see `raise_fin` in `mathlib`s `data/fin.lean`).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534708):
I like `if` and `if h :` the problem is that we don't have a if-splitter tactic (a tactic which looks for a `if` in your goal and introduces a cases for it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534755):
No, I'm going in the opposite direction of `raise_fin`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534756):
@**Johan Commelin** if you see a `ite` and don't know how to continuous: do the case distinction by `by_cases p` and then rewrite using `if_pos` and `if_neg` (or if it is a dependent if then `dif_neg` and `dif_pos`).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534767):
like `fin.succ`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534881):
No, I just want to skip one `i : fin (n+1)`, and in this way get a function on `n` elements... I then collapse the domain to `fin n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534923):
Sorry, I see that I messed up my types...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534924):
Let me fix it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534937):
```lean
def fin.lift {n : ℕ} (i : fin (n + 2)) (j : fin n) : fin (n + 1) :=
⟨if i.1 < j.1 then j.1 + 1 else j.1,
  begin
    by_cases (i.1 < j.1),
    { rw [if_pos h], exact (nat.succ_lt_succ j.2) },
    { rw [if_neg h], exact (nat.lt_succ_of_lt j.2) }
  end⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534978):
Argh, sorry wrong way around... (CORRECTED)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534980):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534982):
That gives me the idea on how to work with this stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535054):
I also fixed my type signature

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 14 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535116):
I was working a little bit on cubes and chains (see: https://gist.github.com/johoelzl/ace6a2304b58f77a561777f6ac411647 )
I didn't yet continue it, but it might be worthwhile to use `vector n R` instead of `fin n -> R`. I'm still unsure about this...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535129):
In the end, I think `fin n` is a particularly good choice for this. Because `fin n` are the objects of the simplex category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535176):
We just need to define all the maps `fin n \to fin m`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535182):
And I am currently struggling with the incarnation in the singular chain complex...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535564):
Anyway, I am voting for an `ite` tactic. Maybe I'll try to cargo-cult it myself after I've defined singular homology.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535796):
@**Johan Commelin** You are running into the same sort of issues, in a broad sense, that I am currently running into. You want to model certain things (e.g. R^n) and there are several equivalent ways of doing it (e.g. lists of length n, "vector n", or an inductive definition). My impression is that it's a bit of a dark art to see which definition is "best". As mathematicians we regard all these definitions as trivially equivalent, and indeed are capable of switching between various ways of thinking about one underlying idea without ever even fussing about the details, because we all know how to switch. In this game, every time you switch then all of a sudden the lemma or definition you had in one of the contexts becomes unavailable and you either end up writing infrastructure which will help you to switch between the notions, or (and my impression is that this is what the CS people advocate) deciding what the "best" way to do it is (you see that this is the question Johannes raises -- it is far far more important for CS people than for maths people) and writing everything for this decision and then writing the functions which translate to and from other situations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535805):
I'm now just about sufficiently competent at Lean to be able to make a really lousy decision about how to model a situation and then struggle through all the proofs I need using this model.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535850):
If you want my advice then find some mathlib functions related to what you're doing and see how a CS person does it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535851):
Yes, I think I agree. (Though your problems are way bigger then mine...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535854):
This morning I wanted to say something was compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535856):
so I just wrote down some random definition of compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535857):
and then wrote 100 lines of code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535861):
and then I actually wanted to use some compactness result from the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535870):
and then found that they had a trivially equivalent but in some sense completely different way of saying "finite subcover"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535921):
and of course it's at this point that you realise that their way of doing it is mathematically equivalent but, in terms of usability, much better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 14 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535932):
So before you write too much more code you might want to explain what you want to do and suggest some basic definitions which will be at the foundation of everything, and then see what the CS people think of them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126550609):
Re: `fin`, I did a lot of index work like this in `dioph`, using `fin2` for convenience. It might help to look at stuff like `insert_perm` and `remap_left`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 14 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126552700):
Thanks!


{% endraw %}
