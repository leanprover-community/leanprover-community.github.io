---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15619implementationissues.html
---

## [general](index.html)
### [implementation issues](15619implementationissues.html)

#### [Kevin Buzzard (Sep 11 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133692574):
Implementation issues occasionally have knock-on effects. For example the coercion `of_nat` from `nat` to `int` is not a generic coercion from `nat` to a monoid with 0 and 1, and as a consequence all of the standard coercion lemmas like `\u(a+b)=\u a+\u b` have to be proved for `of_nat`separately, giving us `int.coe_nat_add` as well as `nat.cast_add`.

My understanding from conversations here is that `of_nat` is a special case, as it is actually a constructor for `int` and is hence more efficient. However when it comes to computations we all know that `nat` is absurdly inefficient, anyone who is doing computations will be using `pnum` or `num` or whatever -- the binary version of `nat` which has been specifically designed to be harder to reason with but more efficient to compute with.

When I arrived here I just assumed that `int` would be defined the way it's typically defined in a mathematics class -- the quotient of `nat x nat` by the usual equivalence relation. But it isn't, it's defined in a much more direct and probably quite sensible way. Similarly `rat` is actually defined as a pair `(n,d)` of an integer numerator, a positive nat denominator, and a proof that they're coprime. My impression from this is that for some reason quotients are to be avoided -- they are less efficient or less computable in some way. This came up today when discussing polynomials with undergraduates -- someone suggested that a polynomial in one variable could be implemented as a list of coefficients, and I pointed out that leading zeros meant that it would have to be a quotient of list and this might well make it less computationally efficient or something. But then it occurred to me that actually they're defined as finsupps, which need finsets, which are multisets plus a theorem, and a multiset is a nightmarish quotient of list by some extremely delicate and hard to work with equivalence relation which in practice anyone using multiset other than developers stays well away from. Looking at it this way, it looks to me that in terms of sheer content of what is going on, defining polynomials in 1 variable as lists modulo "we're the same modulo a bunch of zeros at the end" looks to have far less baggage associated with it than this finsupp/finset/multiset/list.perm.setoid approach.

So what exactly is informing these decisions? Why do we use nat at all? `num` is better, we could prove all the right induction etc lemmas for it, etc. Similarly, `list.perm.setoid` seems to ultimately rely on the fact that every automorphism of [0,n-1] can be written as a possibly huge product of swaps of consecutive nats, which is a terrible way to do permutation groups from the point of view of computation. As a mathematician all I care about is the theorems, but it seems to me that from a computational perspective Lean is in some sense a disaster -- it wasn't designed to do computations -- so why am I having to jump through all these hoops to prove results about coercions from nat to int?

#### [Reid Barton (Sep 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133693662):
So one thing is that anything that's a Prop doesn't exist at runtime at all. And a quotient is just represented by a value of the underlying type. So in the VM, a `multiset` just looks like a `list`--there are no actual big products of transpositions.

The issue with using quotients for `int` and `rat` is that you could then end up with arbitrarily large representations of the same value of Z (0 = "N - N" for large N) or of Q (1 = "N/N" for large N). This issue doesn't come up for `multiset` and its relatives because all of the equivalent representations have the same size.

#### [Reid Barton (Sep 11 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133693807):
> So what exactly is informing these decisions? Why do we use nat at all? num is better, we could prove all the right induction etc lemmas for it, etc.

You could prove the induction lemmas, but then when you define, say, factorial by induction, it would not be true *by definition* that (n+1)! = (n+1) * n!. It would be only a propositional equality.

#### [Kevin Buzzard (Sep 11 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133693881):
I don't even understand what we are trying to make "efficient" here. If I wanted to compute 100! I would not be using Lean. What I would like to be efficient in practice is that I would like mathlib to compile quickly, and I would like the orange bars to disappear more quickly when I am in the middle of a 200-line proof. Is this in any way related to decisions about using nat not num to represent naturals?

#### [Mario Carneiro (Sep 11 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694125):
> If I wanted to compute 100! I would not be using Lean.

Obviously this isn't how we build for the future! You can in fact calculate quite large factorials in lean. `#eval nat.fact 100` takes 26ms

#### [Mario Carneiro (Sep 11 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694178):
Note that this would be much *slower* if I used `num` instead of `nat`

#### [Kevin Buzzard (Sep 11 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694188):
:-)

#### [Kevin Buzzard (Sep 11 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694197):
I have no idea what `#eval` does -- but not that I have no idea what a VM is so I wouldn't launch into an explanation -- I am way behind.

#### [Kevin Buzzard (Sep 11 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694206):
I know epsilon about java bytecode and the JVM

#### [Mario Carneiro (Sep 11 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694283):
```
def num.fact : nat → num
| 0     := 1
| (n+1) := num.fact n * num.of_nat' (n+1)

#eval num.fact 100
```
takes 61ms

#### [Mario Carneiro (Sep 11 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694350):
Part of the problem is that you only see half the picture, since you are a mathematician with no interest in lean as a programming language. While that's fine, some design decisions will look strange or unmotivated from that angle

#### [Mario Carneiro (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694367):
A major part of it is that `#eval` should be fast on computable things in mathlib

#### [Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694387):
I thought that #eval was completely irrelevant.

#### [Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694388):
Do I ever use it?

#### [Mario Carneiro (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694390):
*you* don't

#### [Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694391):
I see

#### [Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694396):
I mean, does the code I write ever use it somehow?

#### [Mario Carneiro (Sep 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694403):
this may change in lean 4 when `vm_compute` arrives

#### [Kenny Lau (Sep 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694465):
you mean dec_trivial?

#### [Mario Carneiro (Sep 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694467):
Your biggest current contact with `#eval` is in tactic evaluation. When a tactic takes a long time it is running on the VM

#### [Mario Carneiro (Sep 11 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694474):
it's dec_trivial in the VM

#### [Mario Carneiro (Sep 11 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694482):
meaning that we could prove `nat.fact 100 = ...` in 21ms instead of whatever it is now

#### [Kevin Buzzard (Sep 11 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694529):
I see, so when I see orange bars because I used `ring` 10 times already in my proof and I've still not finished writing it, that's because of something to do with `num` or `#eval` or something?

#### [Mario Carneiro (Sep 11 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694531):
if I use `norm_num` on that I'm sure it will take several seconds at least and probably time out

#### [Mario Carneiro (Sep 11 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694535):
`#eval` is used to evaluate `ring` the tactic

#### [Mario Carneiro (Sep 11 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694600):
in particular, `ring` does computations on rational numbers, and those computations are evaluating `rat` in the VM

#### [Mario Carneiro (Sep 11 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694608):
this is distinct from proving things about `rat`, where the only thing running is typechecking the proofs

#### [Mario Carneiro (Sep 11 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694616):
and also distinct from evaluating expressions using `dec_trivial`, which evaluates in the kernel

#### [Mario Carneiro (Sep 11 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694774):
```
example : 8 * 10 = 10 * 8 := dec_trivial -- evaluates in the kernel

#reduce to_bool (8 * 10 = 10 * 8) -- evaluates in the kernel

#eval to_bool (8 * 10 = 10 * 8) -- evaluates in the VM

meta def test := if 8 * 10 = 10 * 8 then `[trivial] else sorry
example : true := by test -- evaluates in the VM

example : 8 * 10 = 10 * 8 := mul_comm 8 10 -- no evaluation, only typechecking
```

#### [Mario Carneiro (Sep 11 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133694921):
and :four_leaf_clover:
```
example : 8 * 10 = 10 * 8 := vm_trivial -- evaluates in the VM
```

#### [Kevin Buzzard (Sep 11 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695050):
I only really care about proving theorems, but I still want to occasionally check $$(x+y)^3=x^3+3x^2y+3xy^2+y^3$$ using `ring`. Is there a similar story here?

#### [Kevin Buzzard (Sep 11 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695084):
It seems to me that I am using `#eval` here.

#### [Kevin Buzzard (Sep 11 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695091):
without noticing.

#### [Kevin Buzzard (Sep 11 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695109):
which is irritating.

#### [Kevin Buzzard (Sep 11 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695203):
Actually what is irritating is that when my proofs get long, I get orange bars that don't go away for a few seconds. I had always assumed that this was because type class inference wasn't as quick as I wanted it to be, and kept forgetting all its calculations and then re-did them every time I pressed a key.

#### [Kevin Buzzard (Sep 11 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695231):
What is irritating for Chris is that mathlib gets one extra lemma and then when Chris needs it he has to pull mathlib and then wait for an hour for it to compile on his slow laptop.

#### [Reid Barton (Sep 11 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695577):
I expect most of that hour is spent in the elaborator/kernel doing typechecky things, not multiplying natural numbers.

#### [Reid Barton (Sep 11 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695725):
That is, I doubt choices about data representation affect mathlib build time much.

#### [Simon Hudon (Sep 11 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133695746):
@**Reid Barton** I'm not so sure. Maybe it's not multiplying that many numbers but I suspect that a large portion of proof checking is proof search which is done by functional programs (the tactics) using data structures like lists and natural numbers.

#### [Kenny Lau (Sep 11 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133696034):
I guess it's ironic that in the Lean "theorem prover", the proofs are given the least relevance. They don't even exist in the VM

#### [Simon Hudon (Sep 11 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133696379):
They exist in the kernel. They have a central role in the kernel. I think we can't say that they have the least relevance. I would say they have the most relevance though

#### [Scott Morrison (Sep 11 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133711908):
We really need distributable binary `olean` files. :-(

#### [Kevin Buzzard (Sep 11 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/133713478):
Can we get Travis to make them for Ubuntu?

#### [Minchao Wu (Oct 23 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136340858):
@**Mario Carneiro** Is there any current workaround for emulating `vm_compute`?

#### [Mario Carneiro (Oct 23 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136343558):
```lean

namespace tactic

meta def mk_axiom (n : name) (ty : expr) : tactic expr :=
do env ← get_env,
  let us := expr.collect_univ_params ty,
  add_decl (declaration.ax n us ty),
  return (expr.const n (level.param <$> us))

meta def vm_trivial : tactic unit :=
do t ← target,
  d ← mk_instance `(decidable %%t),
  eval_expr bool `(@to_bool %%t %%d) >>= guardb,
  n ← new_aux_decl_name,
  mk_axiom n t >>= exact

end tactic

example : 200 + 200 = 400 := by tactic.vm_trivial
example : nat.prime 134513481061 := by tactic.vm_trivial
```

#### [Minchao Wu (Oct 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136345082):
Great. The only concern is that it's actually introducing the thing being proved as an axiom?

#### [Minchao Wu (Oct 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136345490):
Hmm... but this should be sufficient for my purpose. Thanks Mario!

#### [Rob Lewis (Oct 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136346985):
Note that this will only work for `example` and `def`. Any changes you make to the environment when proving a `theorem` get discarded at the end. New declarations will get inlined if possible, but this isn't possible with axioms.

#### [Rob Lewis (Oct 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136347048):
The reason being, elaboration of theorems happens in parallel/out of order, and changing the environment needs to be sequential.

#### [Reid Barton (Oct 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136347178):
Is this basically: To prove a decidable statement, have the VM evaluate the decision procedure and then add an axiom which says that we trust that the result of VM execution was correct in this case?

#### [Rob Lewis (Oct 23 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation issues/near/136347448):
Yeah. It's using the VM as an oracle for decidable statements.

