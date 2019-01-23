---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60427Whydoesntdectrivialsolveprime3.html
---

## Stream: [new members](index.html)
### Topic: [Why doesn't dec_trivial solve `prime 3`?](60427Whydoesntdectrivialsolveprime3.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 24 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136416609):
In `prime.lean`, the following statements are made:

```lean
theorem prime_two : prime 2 := dec_trivial
theorem prime_three : prime 3 := dec_trivial
```

And both work. However if I reproduce the same code on another lean file, e.g.

```lean
import data.real.basic 
import data.nat.prime

open nat

theorem prime_two : prime 2 := dec_trivial
theorem prime_three : prime 3 := dec_trivial
```

Only `prime_two` works. What's going on?

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136417706):
The crucial line in `data.nat.prime` seems to be `local attribute [instance] decidable_prime_1`. If you include that, then `prime_three` works.

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136417744):
I guess what's initially surprising is how lean knows `prime 2` is decidable without that instance.

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136417839):
`decidable_prime_1` just says: 
```lean
def decidable_prime_1 (p : ℕ) : decidable (prime p) :=
decidable_of_iff' _ prime_def_lt'
```

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136418233):
Here's the definition of `prime`:
```lean
def prime (p : ℕ) := p ≥ 2 ∧ ∀ m ∣ p, m = 1 ∨ m = p
```
and here's the type of `prime_def_lt`:
```lean
theorem prime_def_lt' {p : ℕ} : prime p ↔ p ≥ 2 ∧ ∀ m, 2 ≤ m → m < p → ¬ m ∣ p 
```
When `p=2` it's obvious to lean that `prime p` is decidable, but when `p > 2` it needs the extra hint that you only need to check `m < p`.

#### [ Abhimanyu Pallavi Sudhir (Oct 24 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136418284):
Ah ok. Interestingly if the file contains `local attribute [instance] classical.prop_decidable` (and not `nat.decidable_prime_1`), then even `prime 2` gets messed up.

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136418800):
Yes, that makes sense. I don't think `dec_trivial` can do very much for you when every proposition is declared to be decidable.

#### [ Kevin Buzzard (Oct 24 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136425801):
If every proposition is declared to be decidable, but you still want to use `dec_trivial`, the trick is `local attribute [instance, priority 0] classical.prop_decidable`

#### [ Kevin Buzzard (Oct 24 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136425868):
Then the "fake" decidabilty is always used after the "real" one, if a real one can be found.

#### [ Abhimanyu Pallavi Sudhir (Oct 24 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136425939):
```quote
If every proposition is declared to be decidable, but you still want to use `dec_trivial`, the trick is `local attribute [instance, priority 0] classical.prop_decidable`
```
Yeah, I know that -- but I don't get why exactly it is that the fake decidability isn't enough for dec_trivial.

#### [ Kenny Lau (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426003):
because it uses `choice` and the VM can't evaluate `choice`

#### [ Kevin Buzzard (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426010):
fake decidability just confuses `dec_trivial`. We saw another instance of `dec_trivial` getting confused in the `even` thread a week or so ago. I am very much not an expert in these matters, but it's something to do with what the VM does

#### [ Kenny Lau (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426012):
`decidable` isn't a Prop, it's data

#### [ Kevin Buzzard (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426014):
what Kenny said

#### [ Kevin Buzzard (Oct 24 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426117):
Yeah. I don't understand this properly. I don't even really know what the kernel and the VM are. I suspect that this might be quite a good way of learning what the difference is between them.

#### [ Kevin Buzzard (Oct 24 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426264):
`decidable blah` usually encodes some sort of way of computing whether blah is true or false. But if you make a random instance of it using classical mathematics then the algorithm isn't actually there. What does the kernel think of this situation? What about the VM?

#### [ Kevin Buzzard (Oct 24 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426305):
What would happen if there were no VM? The kernel does all the typechecking, right? Why do we even need the VM?

#### [ Kevin Buzzard (Oct 24 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426361):
Sorry for my dumb questions -- given that we are on the "new members" stream I figure they would be OK.

#### [ Chris Hughes (Oct 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426424):
The VM is faster than the kernel. This is useful for executing tactics.

#### [ Reid Barton (Oct 24 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426930):
```quote
```quote
If every proposition is declared to be decidable, but you still want to use `dec_trivial`, the trick is `local attribute [instance, priority 0] classical.prop_decidable`
```
Yeah, I know that -- but I don't get why exactly it is that the fake decidability isn't enough for dec_trivial.
```
The idea behind `dec_trivial` is basically that the value of type `decidable P` given by the instance is going to reduce to either `is_false p` (where `p : not P`) or `is_true p` (where `p : P`). But if you use an axiom to define the instance, like `classical.prop_decidable` does, then that axiom won't be reducible.

#### [ Reid Barton (Oct 24 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426949):
I *think* the VM is actually not involved here. But some things about `dec_trivial` still confuse me.

#### [ Reid Barton (Oct 24 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427170):
(Like why do we need this tactic ``meta def triv : tactic unit := mk_const `trivial >>= exact``? Could we just have defined ``notation `dec_trivial` := of_as_true trivial``?)

#### [ Reid Barton (Oct 24 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427226):
Maybe this is the `by exact` trick to defer type checking a term, in the hopes that its expected type will be known later?

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427709):
I'm intrigued. I've never heard of the `by exact` trick. Where (else) is it used?

#### [ Reid Barton (Oct 24 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427741):
whenever Lean is being dumb

#### [ Reid Barton (Oct 24 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427796):
that is to say, I don't really understand when or why it works--I have used it successfully once or twice though

#### [ Reid Barton (Oct 24 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427913):
I guess something like: if there is a subterm which should type check, but Lean is rejecting it, and there are metavariables in its expected type, then maybe wrapping the subterm in `by exact` will cause those metavariables to be solved for earlier relative to Lean trying to check the subterm

#### [ Reid Barton (Oct 24 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427965):
I think it's the kind of thing which only crops up in situations which are a bit complicated

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136428220):
I did a search for "`by exact`" in mathlib and it looks like [there's a concrete example](https://github.com/leanprover/mathlib/blob/fedee9835e73df24a367163e87c9c70284acf4f2/set_theory/cardinal.lean#L309) in `set_theory/cardinal.lean`:
```lean
theorem add_one_le_succ (c : cardinal) : c + 1 ≤ succ c :=
begin
  refine quot.induction_on c (λ α, _) (lt_succ_self c),
  refine quot.induction_on (succ (quot.mk setoid.r α)) (λ β h, _),
  cases h.left with f,
  have : ¬ surjective f := λ hn,
    ne_of_lt h (quotient.sound ⟨equiv.of_bijective ⟨f.inj, hn⟩⟩),
  cases classical.not_forall.1 this with b nex,
  refine ⟨⟨sum.rec (by exact f) _, _⟩⟩,
  { exact λ _, b },
  { intros a b h, rcases a with a|⟨⟨⟨⟩⟩⟩; rcases b with b|⟨⟨⟨⟩⟩⟩,
    { rw f.inj h },
    { exact nex.elim ⟨_, h⟩ },
    { exact nex.elim ⟨_, h.symm⟩ },
    { refl } }
end
```
Removing `by exact` from the line `refine ⟨⟨sum.rec (by exact f) _, _⟩⟩,` causes lean to complain:
```lean
type mismatch at application
  sum.rec ⇑f
term
  ⇑f
has type
  has_coe_to_fun.F f : Type u_1
but is expected to have type
  Π (val : ?m_1), ?m_2 (sum.inl val) : Sort (imax (?+1) ?)
```
I guess this is what you're describing?

(on the other hand, [the `by exact` at line 296](https://github.com/leanprover/mathlib/blob/fedee9835e73df24a367163e87c9c70284acf4f2/set_theory/cardinal.lean#L296) can be removed, at least when I play around with this in VS code.)

#### [ Reid Barton (Oct 24 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136428283):
Yeah, there are metavariables in the expected type, and in this case those prevent the coercion from triggering, I guess

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429224):
Returning to your question about why `dec_trivial` isn't just notation for `of_as_true trivial`, the `prime 2` and `prime 3` examples can be proved with `of_as_true trivial`, which is also disposing of all the other `dec_trivial` examples I'm throwing at it at the moment.  Can we cook up an example where `of_as_true trivial` fails and the current `dec_trivial` works?

#### [ Rob Lewis (Oct 24 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429357):
```lean
example : 0 = 0 := dec_trivial
example : 0 = 0 := of_as_true trivial
```

#### [ Rob Lewis (Oct 24 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429714):
But returning to the original original question: I think there's something wrong with the current `nat.decidable_prime` instance. For `n > 2` it depends on  evaluating `min_fac`, and reducing `min_fac 3` takes an implausible amount of time.

#### [ Reid Barton (Oct 24 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429866):
I remember being confused by exactly this original issue about `is_prime 2` and `is_prime 3` as well when I was starting out using Lean. It would be nice if it could be fixed somehow.

#### [ Rob Lewis (Oct 24 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429876):
`nat.decidable_prime` should evaluate faster than `nat.decidable_prime_1` in the VM, I think, but apparently not in the kernel.

#### [ Rob Lewis (Oct 24 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429966):
Maybe this isn't "wrong," it could be the right default for the way `prime` is used right now.

#### [ Rob Lewis (Oct 24 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429969):
But it is confusing.

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430222):
This works:
```lean
example : 0 = 0 := of_as_true (by exact trivial)
```
Is the current definition of `dec_trivial` using ``meta def triv : tactic unit := mk_const `trivial >>= exact`` equivalent to `of_as_true (by exact trivial)`?

#### [ Mario Carneiro (Oct 24 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430285):
yes, this is just the situation. `decidable_prime_1` is faster in the kernel, `decidable_prime` is faster in the VM (and also incorporates some tricks to speed up the checking of largeish numbers)

#### [ Mario Carneiro (Oct 24 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430327):
I recommend using `by norm_num` if you want a proof that a number is prime, though, since this builds a proof using similar tricks but the kernel will accept it

#### [ Rob Lewis (Oct 24 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430389):
Oh, cool, I didn't know `norm_num` did primality proofs.

#### [ Mario Carneiro (Oct 24 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430397):
it's a recently added module

#### [ Reid Barton (Oct 24 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430418):
```quote
Is the current definition of `dec_trivial` using ``meta def triv : tactic unit := mk_const `trivial >>= exact`` equivalent to `of_as_true (by exact trivial)`?
```
It should be, though maybe `tactic.interactive.exact` is not available yet when `dec_trivial` is being defined

#### [ Kevin Buzzard (Oct 24 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431051):
```quote
Oh, cool, I didn't know `norm_num` did primality proofs.
```
https://xenaproject.wordpress.com/2018/07/26/617-is-prime/ -- last line!

#### [ Reid Barton (Oct 24 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431192):
Now I'm wondering: what's the largest number formally proven to be prime

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431228):
I would definitely start with the largest known Mersenne prime (i.e. the largest known prime).

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431242):
Aren't the primality tests pretty low-level and trivial?

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431260):
I think they take a couple of weeks to run though :-/

#### [ Reid Barton (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431264):
You'd probably have to do a bit of elementary number theory to prove they are correct

#### [ Kenny Lau (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431268):
```quote
Aren't the primality tests pretty low-level and trivial?
```
...

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431270):
right

#### [ Kevin Buzzard (Oct 24 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431314):
They are specific primality tests for Mersenne numbers

#### [ Reid Barton (Oct 24 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431334):
A separate question is, if I gave you a "random" 256-bit prime, could we prove it's prime using the AKS primality test or something like that

#### [ Mario Carneiro (Oct 24 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431355):
The current algorithm is just trial division with some optimizations

#### [ Mario Carneiro (Oct 24 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431364):
so it is still exponential in the bits of the number

#### [ Mario Carneiro (Oct 24 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431416):
I thought about implementing AKS, but it probably won't show an advantage until at least 15-digit primes

#### [ Rob Lewis (Oct 24 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431457):
http://www.lix.polytechnique.fr/~werner/publis/flops06.pdf has some benchmarks.

#### [ Reid Barton (Oct 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432039):
Apparently the answer was probably the 20th Mersenne prime $$2^{4423} - 1$$, at least as of whenever that paper was written

#### [ Kevin Buzzard (Oct 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432178):
Is that all??

#### [ Kevin Buzzard (Oct 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432183):
People aren't trying hard enough

#### [ Reid Barton (Oct 24 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432377):
If I understood the paper correctly, they are using a mode of Coq with a VM implementation of reduction in the kernel, so it's a rather large trusted kernel code base as well

#### [ Reid Barton (Oct 24 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432418):
though apparently they don't use native machine arithmetic, so I'm not really sure

#### [ Kevin Buzzard (Oct 28 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136669712):
So I finally had a chance to look at the paper Rob linked to. So they seem to be doing lots of things at once. They have implemented a generic primality test (this is before AKS I guess -- IIRC that was discovered around the same time). But I am not sure if people care about 10 more primes being verified prime -- people care about the *biggest* one. So forget Pocklington -- one wants to go straight for the Mersenne primes and probably use the polynomial time Lucas method. So the thing to go for is $$P:=2^{9689}-1$$. This can be proved prime if one can knock off a proof of [the Lucas-Lehmer primality test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test), which looks well within reach, and then one has to basically square 9689 numbers modulo $$P$$. How feasible is that? I just ran the entire test in 217 ms in pari-gp.

#### [ Kevin Buzzard (Oct 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136669835):
The next question of course is how feasible it is to square 77232917 numbers modulo $$2^{77232917}-1$$.

#### [ Kevin Buzzard (Oct 28 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136670082):
It's probably worth pointing out that if numbers are somehow being stored in binary, then reducing modulo a number of the form $$2^n-1$$ can be done using specialised code which would perhaps be more efficient than usual Euclid? But I have no idea whatsoever how reasonable it would be to expect Lean to do any arithmetic at all with numbers so large.


{% endraw %}
