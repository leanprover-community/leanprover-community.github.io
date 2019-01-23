---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00342efficiency.html
---

## Stream: [general](index.html)
### Topic: [efficiency](00342efficiency.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570420):
Hi @**Mario Carneiro**, @**Keeley Hoek**  and I are having some "fun" profiling `rewrite_search`, and discovered that all the arithmetic is slow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570429):
don't generate proofs during the search

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570430):
We're going to experiment to see if typeclass resolution is partly to blame, but I'm also wondering if you have a sense of whether it's better to use `nat` or `int`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570435):
how are you proving things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570438):
Maybe Keeley can tell me that `nat` won't actually do for our purposes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570441):
Nope, everything is in meta land.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570457):
oh --- sorry, it's not that part that is slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570486):
it is the edit distance calculations that are slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570489):
so this has nothing to do with proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570491):
they should both be pretty fast

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570510):
We could use `nat` I think
I just have to find all the typeclass names I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570511):
for numbers less than 2^30 or so it's just using the C++ addition which should be super fast

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570517):
ok, all our numbers should be small enough, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570540):
do you have any idea why `min` could be (relatively speaking) slow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570542):
there is a lot of overhead for VM stuff but no more than anything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570604):
You can look at the code generated for a definition using `set_option trace.compiler.optimize_bytecode true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 13 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570617):
oooh...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570676):
If you inline the definition of `min` it's almost as fast as it possibly could be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570686):
if you don't inline there is possible inefficiency in creating and destroying the `nat.decidable_linear_ordered_semiring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570729):
but I don't know how significant it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570739):
(And by inline I mean `attribute [inline] min`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 13 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570933):
ooooh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 13 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570948):
can you inline instances?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 13 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570951):
like where they are used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 13 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147571233):
you don't want to inline instances, you want to inline projections. My experiments with `min` on `nat` show exactly the kind of simplification you would want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 13 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147582312):
Just for the record: we ended up getting a factor-of-three speedup by inlining a bunch of important things in the hotpath, and eliminating some pesky table lookups in favor of using more memory---and parallelisation is to come!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 13 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147582752):
finally someone more clever than me is using a more clever approach to speed up things! :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147668689):
@**Keeley Hoek** would you have any insight as to how I could speed up [this](https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293) without doing what I did?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 14 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669081):
Unfortunately not without contriving a tactic kenny
---but I must get to bed!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 14 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669084):
:O the string `@mv_polynomial σ α (@comm_ring.to_comm_semiring α _inst_3)` appears 31 times!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 14 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669239):
But its definitely something to think about
`(@comm_ring.to_comm_semiring α _inst_3)` 67 times!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 14 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669365):
Can you think of a general way to hint about this kind of stuff? 
Maybe you could say "use `comm_ring.to_comm_semiring` everywhere you can first"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 14 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669375):
To some tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147670232):
I don't write tactics...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147670331):
:D
It's on the list, then!


{% endraw %}
