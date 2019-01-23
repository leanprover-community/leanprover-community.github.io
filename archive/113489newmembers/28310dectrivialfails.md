---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28310dectrivialfails.html
---

## Stream: [new members](index.html)
### Topic: [dec_trivial fails](28310dectrivialfails.html)

---


{% raw %}
#### [ Kenny Lau (Oct 30 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136806175):
```lean
import data.rat

def rat.sqrt (q : ℚ) : ℚ :=
rat.mk (nat.sqrt $ int.to_nat q.num) (nat.sqrt q.denom)

example : rat.sqrt 2 = 1 := dec_trivial -- fails

#eval rat.sqrt 2 -- 1
```

#### [ Kenny Lau (Oct 30 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136806191):
Why does `dec_trivial` fail?

#### [ Kenny Lau (Oct 30 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136806337):
@**Chris Hughes**

#### [ Kenny Lau (Oct 30 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807285):
```lean
example : nat.sqrt (int.to_nat 2) = 1 := dec_trivial -- fails
example : nat.sqrt 1 = 1 := dec_trivial -- fails
example : rat.mk 1 1 = 1 := dec_trivial -- succeeds
```

#### [ Kenny Lau (Oct 30 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807385):
ok so the problem boils down to this

#### [ Kenny Lau (Oct 30 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807389):
```lean
import data.nat.sqrt

example : nat.sqrt 1 = 1 := dec_trivial -- fails
```

#### [ Scott Olson (Oct 30 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807651):
Looks like it goes `nat.sqrt -> nat.size -> nat.binary_rec` and `binary_rec` reduces very slowly, so `dec_trivial` gives up

#### [ Kevin Buzzard (Oct 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807739):
From `data.nat.sqrt`:

```lean
def sqrt (n : ℕ) : ℕ :=
match size n with
| 0      := 0
| succ s := sqrt_aux (shiftl 1 (bit0 (div2 s))) 0 n
end
```

```lean
import data.nat.sqrt

open nat

#eval size (1 : ℕ) -- 1
#check size (1 : ℕ) -- ℕ

example : nat.sqrt 1 = 1 := dec_trivial -- fails

example : sqrt_aux (shiftl 1 (bit0 (div2 0))) 0 1 = 1 := dec_trivial -- works?
```

#### [ Kevin Buzzard (Oct 30 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807780):
Yes Scott has seen the right path -- `example : size 1 = 1 := dec_trivial` fails

#### [ Scott Olson (Oct 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807877):
I get failure for the `sqrt_aux` line

#### [ Kevin Buzzard (Oct 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807887):
Did you open nat?

#### [ Scott Olson (Oct 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807888):
Yes

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808002):
hmm

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808015):
this is troublesome

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808032):
because we can't change `nat.binary_rec`

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808036):
well maybe we can write `nat.binary_rec'` just like we do other functions

#### [ Kevin Buzzard (Oct 30 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808291):
```lean
example : binary_rec 0 (λ_ _, succ) 1 = 1 := begin
  unfold binary_rec,
  split_ifs,
    cases h,
  refl,
end
```

Maybe you can add some sort of decidability instance for `size`?

#### [ Kevin Buzzard (Oct 30 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808370):
I don't think you need to go down as far as `binary_rec`.

#### [ Kenny Lau (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808446):
I don't see how we can just add decidability instance.

#### [ Kevin Buzzard (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808451):
You know more about decidability than me.

#### [ Kevin Buzzard (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808459):
`decidable (size a = b)`?

#### [ Kenny Lau (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808465):
that wouldn't be useful

#### [ Kenny Lau (Oct 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808470):
because I can have another function that calls `size`

#### [ Kevin Buzzard (Oct 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808471):
Or "computability" or something? I have no idea how these things work.

#### [ Kenny Lau (Oct 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808498):
I don't see any other solution than rewriting some functions in the chain, but maybe @**Mario Carneiro** would have some idea

#### [ Kevin Buzzard (Oct 30 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808581):
So what's going on here? You need to make sure that the...kernel? VM? can compute `size a`?

#### [ Kevin Buzzard (Oct 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808629):
I don't really understand how `a = b` can fail to be proved by `dec_trivial` (if a and b are explicit computable nats). Equality on nat is decidable, so whatever runs `dec_trivial` just has to work out what `a` and `b` are and then check that they're equal.

#### [ Kevin Buzzard (Oct 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808676):
and any nat in Lean is reducible to succ succ ... succ zero

#### [ Kevin Buzzard (Oct 30 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808918):
Aah I understand more about the problem now. `#reduce size 1` is a deterministic timeout.

#### [ Kevin Buzzard (Oct 30 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808927):
and then a segfault ;-)

#### [ Kevin Buzzard (Oct 30 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809025):
[ten seconds later]

#### [ Scott Olson (Oct 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809162):
Yeah, my understanding is `dec_trivial` should never fail on closed terms, but it gives up when reduction takes too long

#### [ Kevin Buzzard (Oct 30 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809269):
```lean
open nat

example : binary_rec 0 (λ_ _, succ) 1 = 1 :=
begin
  unfold binary_rec,
  exact dec_trivial
end -- works

example : binary_rec 0 (λ_ _, succ) 1 = 1 :=
begin
  exact dec_trivial
end -- fails
```

#### [ Scott Olson (Oct 30 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809462):
That does seem a bit... artificial. I wish I knew more about how the reductions worked

#### [ Scott Olson (Oct 30 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809536):
But I can confirm `#reduce binary_rec 0 (λ_ _, succ) 1` times out but `#reduce` on the goal after `unfold binary_rec` (copy/pasted out with `set_option pp.proofs true` and `set_option pp.implicit true`) does give you `1`

#### [ Mario Carneiro (Oct 31 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136814397):
This is because proofs are irreducible by default. I think there is an option for this, I forget the name

#### [ Mario Carneiro (Oct 31 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136814432):
It is almost never necessary to reduce a proof during evaluation, but well founded definitions require recursion on proofs of wellfoundedness

#### [ Kenny Lau (Oct 31 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136814666):
then what should we do?

#### [ Mario Carneiro (Oct 31 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136815767):
give up? This definition is not intended for kernel reduction

#### [ Mario Carneiro (Oct 31 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136815862):
If you need to calculate these things, you can either use the definition, or if we need larger scale computation we can add another `norm_num` add-on for this (I really need to make it extensible via annotation...)


{% endraw %}
