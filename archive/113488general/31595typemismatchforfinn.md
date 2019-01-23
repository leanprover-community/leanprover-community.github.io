---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31595typemismatchforfinn.html
---

## Stream: [general](index.html)
### Topic: [type mismatch for fin n](31595typemismatchforfinn.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579325):
I am surprised that this doesn't typecheck:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579326):
```
def subtypeadd {m : ℕ} {n : ℕ} (A : fin m) (B : fin n) : fin (m+n) := 
  ⟨A.val+B.val,add_lt_add A.is_lt B.is_lt⟩

example (A : fin 3) (B : fin 4) (C : fin 7) 
  : A = ⟨2,dec_trivial⟩ → B = ⟨0,dec_trivial⟩ → C = subtypeadd A B → C = ⟨2,dec_trivial⟩ := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579333):
It complains at `subtypeadd` that `A` has type `fin 3` and it expects it to have type `fin 6`??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 11 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579423):
I think this is the default elaboration strategy's fault

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579425):
It's hard for me to see what's going on because it doesn't typecheck so I don't have any term to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579430):
Obviously I can fix it with @

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579431):
but here -- hey -- can you be the elaborator like you sometimes do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579432):
You can make it typecheck by writing `@subtypeadd _ _ A B` or adding `@[elab_simple]` to the definition of subtypeadd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579433):
You have to figure out what m and n are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579434):
and the only clues you have are that A : fin m and A : fin 3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579435):
what do you think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579472):
mr elaborator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 11 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579497):
It sees that the goal is `fin 7` and so has to solve `7 =?= ?m1 + ?m2`. I think if you unfold 7 enough (`bit1 (bit1 one)`) you get `bit0 (bit1 one) + 1`, i.e. `6+1`. So it's the most obvious split and lean takes it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579501):
Aah excellent!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579541):
so in fact this is a fun game

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579542):
guess the error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579543):
```
example (A : fin 3) (B : fin 5) (C : fin 8) 
  : A = ⟨2,dec_trivial⟩ → B = ⟨0,dec_trivial⟩ → C = subtypeadd A B → C = ⟨2,dec_trivial⟩ := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579544):
you have to guess the spurious complaint that Lean makes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 11 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579594):
for `fin 2n` it wants `A : fin n` and for `fin (2n+1)` it wants `A : fin (2n)`

