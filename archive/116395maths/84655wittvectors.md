---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/84655wittvectors.html
---

## Stream: [maths](index.html)
### Topic: [witt vectors](84655wittvectors.html)

---


{% raw %}
#### [ Johan Commelin (Jul 24 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216141):
Anyone interested in sharpening his teeth on polynomials is encouraged to look here: https://gist.github.com/jcommelin/77240367c2815ca0c45da188ba78be19

#### [ Johan Commelin (Jul 24 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216160):
A bunch of stuff from the preamble will be obsolete as soon as Mario pushes his latest mathlib edits.

#### [ Johan Commelin (Jul 24 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216186):
In the final lemma there are a bunch of `sorry`s. The proof is extremely slow, and I am continuously struggling with deterministic timeouts.

#### [ Johan Commelin (Jul 24 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216194):
I have no idea why. It didn't feel to me like I was pushing limits.

#### [ Johan Commelin (Jul 24 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216304):
So there is about 180 lines of preamble. And then about 50 lines of interesting stuff :wink:

#### [ Johan Commelin (Jul 24 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216538):
(A bit of motivation for these crazy polynomials: They are useful for defining rings of Witt vectors, and those show up all over the place in number theory. For example, the ring of p-adic integers turns out to be the ring of Witt vectors of the finite field with p elements.)

#### [ Kevin Buzzard (Jul 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130220198):
```quote
In the final lemma there are a bunch of `sorry`s. The proof is extremely slow, and I am continuously struggling with deterministic timeouts.
```
There is sometimes a reason for this ("your code is crappy for a reason which you didn't realise") but typically you have to get lucky with an expert looking at it and spotting what you did wrong. My valuation stuff got slow recently and I don't know why, but I didn't even bother posting 200 lines of Lean code and saying "why does this take three seconds to compile and I had to put some type class thing up to 100 to make it work?" because it's such a boring question; if I really cared I would try and minimise; currently I just grit my teeth and work around it.

#### [ Johan Commelin (Jul 24 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130221163):
So how do you work around deterministic timeouts? What determines such a timeout? Can I set some option to let Lean work harder?

#### [ Kevin Buzzard (Jul 24 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130221200):
Did you see the `1 <= k <= n` example? That one seemed to debate some discussion from the experts

#### [ Kevin Buzzard (Jul 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130221240):
Here's a conjecture: these things are almost always caused by the type class inference system. @**Mario Carneiro** what do you think about my conjecture?

#### [ Mario Carneiro (Jul 25 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130259324):
that's a bit of a general claim. Another way to make lean take a long time is to use lots of definitional equality or kernel computation, possibly on accident; and elaboration can often take a suspiciously long time to complete (not crazy but like 10-15 seconds for a term proof) for reasons I don't well understand

#### [ Kevin Buzzard (Jul 25 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130263224):
There's a file in the perfectoid repo which takes 10 seconds to compile and I was half-thinking about trying to work out why so really I was looking for clues here.

#### [ Johan Commelin (Aug 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131034587):
Anyone care to take a look at https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L107 ? That file is self-contained, but depends on the latest mathlib.

#### [ Kevin Buzzard (Aug 07 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131036884):
I don't know what the type of anything is, but the lemma you're applying needs that the things you're applying it to are in a multiplicative group and the elements you're talking about look suspicious to me

#### [ Kevin Buzzard (Aug 07 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131036897):
A field is not a group under multiplication. Are you using the right lemma?

#### [ Mario Carneiro (Aug 07 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037022):
oh, good call

#### [ Mario Carneiro (Aug 07 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037035):
there are mirror versions of all the group lemmas for fields with namespace `division_ring` or `field`

#### [ Kevin Buzzard (Aug 07 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037136):
This has happened to me so many times :-)

#### [ Kevin Buzzard (Aug 07 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037218):
"I can't find an instance of exactly what it says in the goal" usually for me means "the thing you want me to match with doesn't match because of something in square brackets"

#### [ Mario Carneiro (Aug 07 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037272):
heh, I remember so many questions from you like that

#### [ Johan Commelin (Aug 07 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131038606):
I'm slowly making progress... `conv` is still confusing me.

#### [ Johan Commelin (Aug 07 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131038649):
`conv in (λ _, _)` gives an error:
```lean
invalid mk_pattern, #1 expr parameter does not occur in the target or (other) expr parameter types
state:
_inst_1 : nat.Prime,
n n : ℕ,
H : ∀ (m : ℕ), m < n → eval₂ C witt_polynomial (X_in_terms_of_W m) = X m
⊢ witt_polynomial n =
      C (↑p ^ (n + 1)) * X n +
        finset.sum finset.univ
          (λ (x : fin n),
             eval₂ C witt_polynomial (C ↑p ^ x.val) *
               eval₂ C witt_polynomial (X_in_terms_of_W (x.val) ^ p ^ (n - x.val))) =
    ?m_1
```

#### [ Johan Commelin (Aug 07 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131038700):
But there is clearly a lambda in there...

#### [ Johan Commelin (Aug 07 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039097):
Ok, I navigated to the lambda by hand.

#### [ Johan Commelin (Aug 07 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039113):
Then I did some rewrites using ring homomorphisms, but Lean couldn't find an instance for them, nor for some rings.

#### [ Johan Commelin (Aug 07 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039123):
Outside the `conv`, Lean found those instances without any trouble.

#### [ Johan Commelin (Aug 07 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039128):
Is this a known issue?

#### [ Kevin Buzzard (Aug 07 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131041397):
I have this gut feeling that I've gone from never using `conv` (because I had no idea how it worked or what it did, before Patrick and I pushed the experts to explain it and then Patrick wrote `conv.md`) to over-using it. I tend to use it to do rewrites under a lambda -- but remember that `simp` does this too, so perhaps `simp only` will do what you're trying to do without having to use `conv`. One problem with `conv` is that if you're trying to find `f x = g x` in some `lam x, f x = g x` then `conv` won't match `f x` because it complains it doesn't know what `x` is. I don't know what your problem is but I look at pretty much every Lean function and it's some sort of lambda, so trying to match a lambda with so many holes sounds a bit scary to me, and trying to fill in the holes also looks hard for the reason I just mentioned above. Will `simp` not work for you?

#### [ Johan Commelin (Aug 07 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131041784):
"I worked my way around it..."

#### [ Johan Commelin (Aug 07 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042169):
@**Mario Carneiro** I have the feeling that I can not extract sublemmas for this proof. Yet I'm constantly plagued with deterministic timeouts. https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L108

#### [ Johan Commelin (Aug 07 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042206):
I fought the mess (and the mess won)

#### [ Mario Carneiro (Aug 07 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042285):
I wanted to ask: why are you using a `finset.univ.sum` over `fin n` when the function to sum over does not depend on the assumption `x.2`?

#### [ Mario Carneiro (Aug 07 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042296):
It would be much easier to use `(finset.range n).sum (\lam x, ...)`

#### [ Johan Commelin (Aug 07 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042395):
Ok. The answer is: I've never used `finset.range` before, and didn't know about it.

#### [ Kevin Buzzard (Aug 07 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042772):
deterministic time-outs usually mean that you've made a mistake in your code and Lean, instead of saying "look an error", is trying to coerce an int into a nat or something else that it can't do but is unfortunately bad at spotting that it can't do.

#### [ Kevin Buzzard (Aug 07 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042792):
bad coercions, and trying to prove things which aren't refl by refl, are sometimes the cause

#### [ Kevin Buzzard (Aug 07 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042797):
(even if they look refl)

#### [ Johan Commelin (Aug 07 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042913):
@**Mario Carneiro** Ok, in the definition after the `witt_polynomial` I am using `i.2`.

#### [ Johan Commelin (Aug 07 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042956):
So now I need some hackery to make that recursive definition work.

#### [ Mario Carneiro (Aug 07 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042975):
I see that... I'm working on the hackery

#### [ Mario Carneiro (Aug 07 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043298):
This should get you started:
```lean
theorem range_sum_eq_fin_univ_sum {α} [add_comm_monoid α] (f : ℕ → α) (n) :
  (finset.range n).sum f = finset.univ.sum (λ i : fin n, f i.1) :=
show _ = @multiset.sum α _ ↑(list.map _ _),
by rw [list.map_pmap, list.pmap_eq_map]; refl

def witt_polynomial (n : ℕ) : mv_polynomial ℕ R :=
(finset.range (n+1)).sum (λ i, (C p ^ i * X i ^ (p^(n-i))))

def X_in_terms_of_W : ℕ → mv_polynomial ℕ ℚ
| n := (X n - (finset.sum finset.univ (λ i : fin n,
  have _ := i.2, (C p^i.val * (X_in_terms_of_W i.val)^(p^(n-i.val)))))) * C (1/p^n)

lemma X_in_terms_of_W_eq {n : ℕ} : X_in_terms_of_W n =
    (X n - (finset.range n).sum (λ i, C p ^ i * X_in_terms_of_W i ^ p ^ (n - i))) *
      C (1 / ↑p ^ n) :=
by rw [X_in_terms_of_W, range_sum_eq_fin_univ_sum]
```

#### [ Mario Carneiro (Aug 07 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043305):
@**Kevin Buzzard** Hey look, a nontrivial equation lemma

#### [ Johan Commelin (Aug 07 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043423):
Thanks!

#### [ Johan Commelin (Aug 07 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043492):
That's a really sweet example of equation lemma hackery!

#### [ Kevin Buzzard (Aug 07 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046126):
`finset.sum finset.univ (λ i : fin (n+1), (C p^i.val * (X i.val)^(p^(n-i.val))))`

Is this really still the best way to sum from 0 to n? It's the constant mentioning of `.val` which is a bit irritating. Is there some big operator or something which makes this better-looking?

#### [ Chris Hughes (Aug 07 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046219):
No, the best way is `(range (n+1)).sum ...`

#### [ Johan Commelin (Aug 07 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046245):
@**Kevin Buzzard** Mario suggested a better way. I'll push my current file.

#### [ Kevin Buzzard (Aug 07 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046341):
Oh yes I see the post now. I ignored it initially because I'd not even begun to look at the file, but I have WiFi for the next 10 minutes so I downloaded the version on GH and am now looking through it.

#### [ Johan Commelin (Aug 07 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046344):
https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L114

#### [ Johan Commelin (Aug 07 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046356):
Ok, make sure you download again (-;

#### [ Johan Commelin (Aug 07 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046430):
I've all sorts of rewrites that are failing, and it is beyond me why they fail...

#### [ Kevin Buzzard (Aug 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046616):
I see! Range is nice to look at, but summing over `fin n` is cool because `i.2` is exactly what you need to make the equation compiler swallow it. Then you switch back to get the equation lemma you really want.

#### [ Johan Commelin (Aug 07 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046705):
Yes. Pretty cool stuff, right? Kudos to Mario.

#### [ Johan Commelin (Aug 07 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046716):
I feel I've made progress today.

#### [ Johan Commelin (Aug 07 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046727):
But the proof is still extremely slow. And it is fragile beyond imagination.

#### [ Kevin Buzzard (Aug 07 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046820):
on line 135 or so you have two different `n`'s.

#### [ Mario Carneiro (Aug 07 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046849):
that's from the first two lines. You can ignore the first `n` after the first line

#### [ Johan Commelin (Aug 07 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046851):
Yes, I don't know why `strong_induction` introduces a new `n`

#### [ Johan Commelin (Aug 07 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046859):
I'll clear the first one

#### [ Kevin Buzzard (Aug 07 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047007):
Inserting `repeat {sorry},end #exit` on line 124 and the proof still takes forever to compile (a second or two). I can't work with Lean when it's like this. Something you're doing is taking far longer than it should, and rather than biting the bullet nowadays I try to fix it.

#### [ Kevin Buzzard (Aug 07 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047028):
It's line 119

#### [ Kevin Buzzard (Aug 07 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047040):
`  simp only [eval₂_mul, eval₂_add, eval₂_sub, eval₂_neg, eval₂_C, eval₂_X],`

#### [ Johan Commelin (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047098):
How do you figure out which line it is?

#### [ Kevin Buzzard (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047100):
`elaboration: tactic execution took 3.44s`.

#### [ Kevin Buzzard (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047112):
I just keep cutting and pasting `repeat {sorry}, end #exit` higher and higher up the file until I find it

#### [ Kevin Buzzard (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047125):
Nowadays when I write Lean code I notice it straight away and deal with the problem when it appears.

#### [ Johan Commelin (Aug 07 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047143):
Ok... so somehow I need to speed up that line...

#### [ Johan Commelin (Aug 07 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047196):
In mathspeak it says that the `eval2` is a ring homomorphism, and that it therefore commutes with mul and add.

#### [ Johan Commelin (Aug 07 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047210):
And thus the ring hom can be moved "inside".

#### [ Johan Commelin (Aug 07 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047369):
```lean
  rw [eval₂_mul, eval₂_C],
  simp only [eval₂_sub],
  rw eval₂_X,
```

#### [ Johan Commelin (Aug 07 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047376):
Somehow `simp only` succeeds, while `rw` doesn't...

#### [ Johan Commelin (Aug 07 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050069):
Ok, it is still really ugly... but progress: https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L115

#### [ Johan Commelin (Aug 07 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050137):
Now I need `i.property` but I no longer have access to it :sad:

#### [ Johan Commelin (Aug 07 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050148):
And the proof is still relatively slow.

#### [ Johan Commelin (Aug 07 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050156):
Anyway, I need to go home now. See you later!

#### [ Mario Carneiro (Aug 07 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050849):
After lots of testing, I think I know the problem: `eval₂_*` is a bad simp lemma, not because it is written incorrectly, but because it is too expensive to instantiate. It takes a second or so to figure out if one of these rules even applies, and simp has to go through tons of them at all parts of the expression

#### [ Kevin Buzzard (Aug 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131051808):
I've just been dropping these `sorry,end #exit` lines in near the beginning and even the rewrites are taking time. `simp only [eval₂_sub]` seems to take about 200ms but `rw @eval₂_sub _ _ _ _ _ _ (X n) (finset.sum (finset.range n) (λ (i : ℕ), C ↑p ^ i * X_in_terms_of_W i ^ p ^ (n - i))) _ _ C _ witt_polynomial` also takes about 200ms

#### [ Kevin Buzzard (Aug 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131051831):
and then `rw eval₂_X` takes about 600ms

#### [ Mario Carneiro (Aug 07 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131053242):
For me the `eval2_sub` proof works provided I have the `foobar` instance:
```
instance foobar : comm_ring (mv_polynomial ℕ ℚ) := by apply_instance
```

#### [ Kevin Buzzard (Aug 07 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054040):
```lean
definition inst_1 : decidable_eq ℕ := by apply_instance
definition inst_2 : decidable_eq ℚ := by apply_instance
definition inst_3 : comm_ring ℚ := by apply_instance
definition inst_4 : decidable_eq (mv_polynomial ℕ ℚ) := by apply_instance 
definition inst_5 : comm_ring (mv_polynomial ℕ ℚ) := by apply_instance 
definition inst_6 : is_ring_hom (C : ℚ → (mv_polynomial ℕ ℚ)) := by apply_instance

lemma X_in_terms_of_W_prop (n : ℕ) : (X_in_terms_of_W n).eval₂ C witt_polynomial = X n :=
begin
  apply nat.strong_induction_on n,
  clear n,
  intros n H,
  rw X_in_terms_of_W_eq,
  rw [eval₂_mul, eval₂_C],
  rw @eval₂_sub ℚ (mv_polynomial ℕ ℚ) ℕ inst_1 inst_2 inst_3 
    (X n) 
    (finset.sum (finset.range n) (λ (i : ℕ), C ↑p ^ i * X_in_terms_of_W i ^ p ^ (n - i)))
    inst_4 inst_5 C inst_6 witt_polynomial,
  sorry,end #exit
```

That last rw is taking 150ms. Is that a long time for a rewrite?

#### [ Kevin Buzzard (Aug 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054089):
I filled in every field.

#### [ Kevin Buzzard (Aug 07 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054347):
and `rw @eval₂_X ℚ (mv_polynomial ℕ ℚ) ℕ inst_1 inst_2 inst_3' inst_4' C inst_5' witt_polynomial n` (the line after) is taking over 300ms.

#### [ Kevin Buzzard (Aug 07 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054427):
```lean
definition inst_3' : comm_semiring ℚ := by apply_instance
definition inst_4' : comm_semiring (mv_polynomial ℕ ℚ) := by apply_instance 
definition inst_5' : is_semiring_hom (C : ℚ → (mv_polynomial ℕ ℚ)) := by apply_instance
```

I thought that `rw` looked at the head of the expression, and it's not hard to find `eval_2`, there's only two possibilities, and one of them fits perfectly. I don't understand why these rewrites are taking so long.

#### [ Johan Commelin (Aug 07 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054652):
That's exactly what I was thinking.

#### [ Mario Carneiro (Aug 07 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054696):
By the way, in the expression `(X_in_terms_of_W n).eval₂ C witt_polynomial = X n` are you aware that the `R` variable of `witt_polynomial` is instantiated as `Q`?

#### [ Mario Carneiro (Aug 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054768):
if you try to assert that it has type `mv_polynomial ℕ R` it doesn't typecheck

#### [ Mario Carneiro (Aug 07 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131055665):
Oh wow, this has a 1000% improvement in speed:
```
generalize e : eval₂ C witt_polynomial = f,
haveI : is_ring_hom f := by subst f; apply eval₂.is_ring_hom,
```
Most of the proof only uses that `f` is a ring hom. For the rest, you can use the equality to recover the eval

#### [ Johan Commelin (Aug 07 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131056663):
Mario, yes, I was aware of that. In the end, we want some identity over `\Z`. I only wrote the general definition of `witt_polynomial` so that I didn't constantly have to `map` them to other rings.

#### [ Johan Commelin (Aug 07 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131056734):
Ok, so I put that bit of code somewhere in the beginning of my proof? And then I get massive speedups, and afterwards it is recovered/unfolded towards the end?

#### [ Johan Commelin (Aug 07 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131058032):
@**Mario Carneiro** Does your suggestion classify as best practice or is it a fragile hack? Is this a sign that we need to improve `eval2`, or is there nothing to worry about?

#### [ Mario Carneiro (Aug 08 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131082758):
It is a hack, although not that fragile, it's just a weird workaround for inexplicable slowdown

#### [ Mario Carneiro (Aug 08 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131082897):
I found another weird way to speed things up:
```
set_option profiler true

instance eval_witt_hom : is_ring_hom (eval₂ C (witt_polynomial R)) :=
@mv_polynomial.eval₂.is_ring_hom _ _ _ _ _ _ _ _ _
  (@C.is_ring_hom R ℕ _ (λ a b, _inst_2 a b) _) _

lemma X_in_terms_of_W_prop (n : ℕ) : (X_in_terms_of_W n).eval₂ C (witt_polynomial ℚ) = X n :=
begin
  apply nat.strong_induction_on n,
  intros n H,
  rw [X_in_terms_of_W_eq],
  simp,
end
```
the `simp` application runs fine as long as you have that instance. The elaboration of `eval_witt_hom` takes about 500 ms written like this, but if I write `_inst_2` instead of eta expanded, elaboration jumps to 8.3 s. If I use `by apply_instance` it takes about 1 s

#### [ Mario Carneiro (Aug 08 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131082996):
@**Sebastian Ullrich** This stuff is closer to your area of expertise than mine, although I am not sure how easy it is to separate mathlib from this issue

#### [ Mario Carneiro (Aug 08 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131087058):
Okay, here's a complete proof with no unreasonable slowdowns:
```
instance eval_witt_hom : is_ring_hom (eval₂ C (witt_polynomial R)) :=
@mv_polynomial.eval₂.is_ring_hom _ _ _ _ _ _ _ _ _
  (@C.is_ring_hom R ℕ _ (λ a b, _inst_2 a b) _) _

lemma X_in_terms_of_W_prop'
  (f : mv_polynomial ℕ ℚ → mv_polynomial ℕ ℚ) [is_ring_hom f]
  (fC : ∀ (a : ℚ), f (C a) = C a)
  (fX : ∀ (n : ℕ), f (X n) = witt_polynomial ℚ n)
  (n : ℕ) : f (X_in_terms_of_W n) = X n :=
begin
  apply nat.strong_induction_on n,
  clear n, intros n H,
  rw [X_in_terms_of_W_eq],
  simp only [is_ring_hom.map_mul f, is_ring_hom.map_sub f, fC, fX, ring_hom_sum.finset f],
  rw [finset.sum_congr rfl, (_ : witt_polynomial ℚ n -
    (finset.range n).sum (λ i, C p ^ i * X i ^ p ^ (n - i)) = C (p ^ n) * X n)],
  { rw [mul_right_comm, ← C_mul, mul_one_div_cancel, C_1, one_mul],
    exact pow_ne_zero _ (nat.cast_ne_zero.2 $ ne_of_gt pp.pos) },
  { simp [witt_polynomial, nat.sub_self],
    rw ring_hom_powers (@C ℚ ℕ _ _ _) },
  { intros i h,
    simp [is_ring_hom.map_mul f, ring_hom_powers f, fC] at h ⊢,
    rw H _ h }
end

lemma X_in_terms_of_W_prop (n : ℕ) : (X_in_terms_of_W n).eval₂ C (witt_polynomial ℚ) = X n :=
begin
  letI : is_ring_hom (@C ℚ ℕ _ _ _) := by apply_instance,
  haveI H := @eval_witt_hom _ ℚ _ _,
  have fC := eval₂_C C (witt_polynomial ℚ),
  have fX := eval₂_X C (witt_polynomial ℚ),
  revert H fC fX, generalize : eval₂ C (witt_polynomial ℚ) = f,
  introsI, exact X_in_terms_of_W_prop' f fC fX n
end
```

#### [ Johan Commelin (Aug 08 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088141):
Wow! Thanks for your help Mario! I wouldn't have been able to come up with this myself.

#### [ Johan Commelin (Aug 08 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088204):
@**Mario Carneiro** Is it ok that your proof explicitly mentions `_inst_2`? I always assumed that was "forbidden".

#### [ Mario Carneiro (Aug 08 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088256):
You should see if `λ a b, by apply_instance` also works without slowdown. If not, you can just name the instance and refer to it

#### [ Johan Commelin (Aug 08 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088298):
Ok, I'll merge this into my file as soon as I'm back at work.

#### [ Johan Commelin (Aug 08 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131091024):
@**Mario Carneiro** You also changed the definition of `witt_polynomial` to make the ring `R` explicit, didn't you?

#### [ Mario Carneiro (Aug 08 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131091040):
I did, it was making things a bit confusing. You don't have to

#### [ Johan Commelin (Aug 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092231):
Is there a way to tease more information out of Lean when it gives the error `command expected`?

#### [ Mario Carneiro (Aug 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092296):
that means that the parser was reset, you are between definitions or something, and you give a non-keyword

#### [ Mario Carneiro (Aug 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092301):
Or it means you have `checking visible lines` mode enabled and you should scroll down to refresh the parser

#### [ Johan Commelin (Aug 08 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092457):
I see... a very descriptive error message :rolling_on_the_floor_laughing:

#### [ Kevin Buzzard (Aug 08 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131095998):
```quote
Or it means you have `checking visible lines` mode enabled and you should scroll down to refresh the parser
```
Johan -- we're talking about the little message in the blue bar at the bottom of the VS Code window which says something like "checking visible lines and above". I constantly refer to this as "evil mode" and it used to be the case that whenever I see a student whose blue bar said this, I would tell them to click on the blue bar and change it to "checking visible files". There is a place for the "visible lines and above" choice, but for my users it causes more trouble than it solves, because it means that sometimes the answer to "there's a red line -- what is wrong with my code?" is "nothing is wrong with your code, it's just that Lean isn't reading all of it". Nowadays I just show my students how to make it say "checking visible files" by selecting File->Preferences->Settings (ctrl-, on linux), then searching for `linesandabove` in the default user settings, hovering over `"lean.roiModeDefault": "linesAndAbove"` (if it says that -- you want it to say `visible`, clicking the little pencil just to the left of it [thus moving the variable into the part of the settings which you can edit], and then making sure it says `"lean.roiModeDefault": "visible"` in user settings.

#### [ Gabriel Ebner (Aug 08 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131096086):
> Nowadays I just show my students how to make it say "checking visible files"

BTW, this is the default now.

#### [ Kevin Buzzard (Aug 08 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131096702):
Thanks for switching it back Gabriel. It's fine if you know what you're doing, but experience indicated that it was confusing for new users. I love the way that you just sit there in the background occasionally making things better for me.

#### [ Johan Commelin (Aug 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131097020):
Thanks for the explanation Kevin!

#### [ Johan Commelin (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101387):
Aaaaahrg. I'm completely stuck again!
```lean
lemma quux {A : Type*} [add_comm_group A] (n : ℕ) (f : ℕ → A) : (finset.range (n+1)).sum f = f n + (finset.range n).sum f := by simp

lemma X_in_terms_of_W_prop₂ (k : ℕ) : (witt_polynomial k).eval X_in_terms_of_W = X k :=
begin
  apply nat.strong_induction_on k,
  clear k, intros k H,
  dsimp only [witt_polynomial],
  conv
  begin
    to_lhs,
    congr, skip,
    rw quux k (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i)),
  end,
  -- generalize e : eval X_in_terms_of_W = f,
  -- haveI : is_ring_hom f := by subst f; apply eval.is_ring_hom,
  -- simp only [ring_hom_sum.finset f],
  -- repeat {sorry}, end #exit
  sorry
end
```

#### [ Johan Commelin (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101390):
Yesterday's trick isn't working.

#### [ Johan Commelin (Aug 08 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101554):
~~After this sorry is removed, I think we are mostly good to go for the definition of witt vectors.~~ Meh... I forgot that I still need to convince Lean that I actually get a polynomial over `\Z` instead of `\Q`.

#### [ Johan Commelin (Aug 08 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101563):
But maybe we first need to figure out why Lean is misbehaving like a toddler...

#### [ Johan Commelin (Aug 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101710):
I pushed the stuff that I have right now: https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L135

#### [ Johan Commelin (Aug 08 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131102445):
Ok, so I have polynomials over `\Q`, but actually all their coefficients lie in `\Z`. What is the best way to extract this polynomial over `\Z`? I currently have the following:
```lean
def witt_structure_int (Φ : mv_polynomial bool ℤ) (n : ℕ) : mv_polynomial (bool × ℕ) ℤ :=
finsupp.map_range rat.num (rat.coe_int_num 0) (witt_structure_rat (map int.cast Φ) n)
```

#### [ Kevin Buzzard (Aug 08 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131103604):
Your rewrite on line 144 is, for me, trying to rewrite when the goal is `| X_in_terms_of_W`. But if I add another `skip` then I see Lean trying to do this:

```
_inst_1 : nat.Prime,
k : ℕ,
H : ∀ (m : ℕ), m < k → eval₂ C X_in_terms_of_W (witt_polynomial m) = X m
| finset.sum (finset.range (k + 1)) (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i))
scratch6.lean:145:4: error

rewrite tactic failed, did not find instance of the pattern in the target expression
  finset.sum (finset.range (k + 1)) (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i))
state:
10 goals
_inst_1 : nat.Prime,
k : ℕ,
H : ∀ (m : ℕ), m < k → eval₂ C X_in_terms_of_W (witt_polynomial m) = X m
⊢ finset.sum (finset.range (k + 1)) (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i)) = ?m_1
```

But when you `set_option pp.all true` I see a whole bunch of typeclass inference stuff which doesn't look like it matches up. The thing you're trying to rewrite has a whole bunch of unsolved metavariables. Your goal looks like this: 

```
 (@finset.sum.{0 0} nat
       (@mv_polynomial.{0 0} nat rat
...
```

and the thing you're trying to rewrite looks like this:

```
  @finset.sum.{0 ?l_1} nat (@mv_polynomial.{0 ?l_1} nat ?m_2 ?m_3) ...
```

Maybe if you are more precise with your rewrite it might help, i.e. throw in some `@`s and say exactly what the type of some more things are. I am kind of wondering whether the type class inference system doesn't know enough about what your types are, and is making some bad guesses about what instances it should use.

#### [ Kevin Buzzard (Aug 08 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105049):
https://gist.github.com/kbuzzard/5254103e5f33b022636a9491fb6719e9

That's the beginning of the `set_option pp.all true` output. The `quux` thing is the thing at the top. The goal is the much longer thing at the bottom, most of which I've truncated. The much longer thing at the bottom corresponds to just the first three lines of the top. Lines 3 and 50 match perfectly. Lines 1 and 2 are supposed to match with lines 16 to 49. We have a universe metavariable `?l_1` which can be zero, then a term metavariable `?m_2` which can be `rat`. What I'm worried about is line 2, which says that type class inference wants to prove something is an add_comm_monoid, and it's going to do this by showing it's an add_comm_group and then it will use an instance called `add_comm_group.to_add_comm_monoid`. But lines 25 to 42 seem to be showing that the rationals are an add_comm_monoid by showing that they're a field, and then a comm_ring, and then a comm_semiring (note that we have now diverged from the plan, because a comm_semiring isn't an add_comm_group) and then an add_comm_monoid.

Now this might not be the problem, but somehow it looks to me like it *might* be an obstruction to the rewrite succeeding. Can you somehow tell Lean that you're not working with `?m_2` but with `rat`?

#### [ Johan Commelin (Aug 08 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105249):
Like so?
```lean
rw quux k (λ (i : ℕ), ((C ↑p ^ i * X i ^ p ^ (k - i)) : mv_polynomial ℕ ℚ)),
```
Alas, that still fails.

#### [ Johan Commelin (Aug 08 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105757):
Hmm, now the output of `pp.all` shows an insane amount of similarities between the goal and what the rewrite offers.

#### [ Johan Commelin (Aug 08 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105807):
But it is not enough. The `rw` is using modules :scream: whereas the goal is sane, and just works with rings.

#### [ Kevin Buzzard (Aug 08 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105895):
What you're trying to rewrite: https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503

Goal: https://gist.github.com/kbuzzard/f515877383946b5eb84f03e31cb988c3

They're not the same. The question perhaps is which differences are superficial and which ones are stopping the rewrite

#### [ Johan Commelin (Aug 08 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131106029):
I'm scared by https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503#file-pattern-lean-L21

#### [ Johan Commelin (Aug 08 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131106164):
Sorry!!! I messed up. I did not have enough `skip`s in the `conv`. :sob:

#### [ Kevin Buzzard (Aug 08 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131106990):
Didn't I mention that? ;-)

#### [ Johan Commelin (Aug 08 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108053):
Hmmm, it seems to me that whenever I make any progress using `simp` or `dsimp`, afterwards everything breaks, because it cleans up to much.

#### [ Johan Commelin (Aug 08 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108058):
So I find my self doing long chains of `rw`s

#### [ Johan Commelin (Aug 08 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108116):
And now I have `(\lam i, f i) i`. And I need `f i`. How do I do that without `dsimp`?

#### [ Johan Commelin (Aug 08 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108302):
Ok, so I think this is called beta-reduction. Is there a tactic that will do beta-reduction, and nothing else?

#### [ Johan Commelin (Aug 08 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108886):
Ok! "I worked my way around it."

#### [ Johan Commelin (Aug 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108907):
All sorries are gone in this part! :octopus:

#### [ Johan Commelin (Aug 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108917):
Now I need to figure out how to get some polynomials that are defined over Q to believe that they actually live over Z.

#### [ Johan Commelin (Aug 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108918):
https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L218

#### [ Patrick Massot (Aug 08 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109022):
You can have a look at https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/library/init/meta/simp_tactic.lean#L71

#### [ Patrick Massot (Aug 08 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109042):
turning off everything but beta

#### [ Kenny Lau (Aug 08 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109241):
I think you only need to specify that beta is turned on

#### [ Kenny Lau (Aug 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109276):
but I'm not sure

#### [ Patrick Massot (Aug 08 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109373):
I think we could have a tactic doing only this and unfolding composition (ie `rw comp_app`)


{% endraw %}
