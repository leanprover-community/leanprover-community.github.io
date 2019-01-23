---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/17703536algebraovercommring.html
---

## Stream: [PR reviews](index.html)
### Topic: [#536 algebra over comm_ring](17703536algebraovercommring.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 10 2019 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154831785):
Changed the target to `ring` not `comm_ring`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901762):
So... `algebra` should probably be a class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901803):
als ik het verandere naar en class, wat zou de name zijn?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901811):
Why not keep calling it `algebra`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901813):
het naam von de morphisme dat het algebra defineeret

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901826):
waarhijdlijk?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901885):
dus als we hebben dat C is een R-algebra, het pi in C wordt “algebra C pi” heetet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901890):
I don't get it. What is the trouble with changing `structure algebra` on line 28 to `class algebra`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901913):
dat man kun niet meer “i x” zeggen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901919):
voor “i : algebra R A” en “x : R”

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901969):
Why not? Aaah, because coercions and type class inference don't play well together?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901976):
dat als algebra een class is, we zouden niet hebben een naam voor de instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902089):
Ok, so this is a question about the levels of bundling we want... is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902154):
nee, dit is over het naam van de morphism defineerend

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902156):
Wait, no. I really don't get it. We can just use classes as if they are structures, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902167):
nee nog

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902181):
je kunt niet zeggen “i : algebra R A” als algebra class is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902188):
(je kunt, maar het moet ons niet)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902322):
@**Reid Barton** What do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902418):
Somehow I would expect to use this as `{R S : Type} [comm_ring R] [algebra R S]`. But apparently that is rather hard. Because now we cannot map an `r : R` into `S` without awful contortions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902505):
@**Kenny Lau** If we had `S : Algebra R`, then you could write `S.hom r` to map `r : R` to `S`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902561):
@**Johan Commelin** waar ben je?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902576):
Somewhere in a train in Germany...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902585):
I had to travel back today, sorry.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902586):
dus je wil niet class hebben?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902605):
I no longer know what is good and what I want and what to do :confused:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902613):
lekker!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902678):
What was your reason for `algebra R S` instead of `S : Algebra R`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902684):
dat we kunnen zeggen dat S een korp is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902721):
Aah, of course, and you want to move between `R1`-algebra and `R2`-algebra structures if there is an `f : R1 -> R2` and `S` is an `R2`-algebra.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902728):
korp -> lichaam

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902809):
@**Assia Mahboubi** @**Cyril Cohen** What is the approach that canonical structures take in situations like these? I guess you have the bundled `Algebra R` version, and you will have to write explicitly the functors for moving between `Algebra R1` and `Algebra R2`. Is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902859):
@**Assia Mahboubi** @**Cyril Cohen** (I subscribed you to this stream. No sure if you want that... It's all about discussing PRs to mathlib.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156674418):
@**Johannes Hölzl** It looks like the instance `S : set R, h : is_subring S |- algebra S R` would never work if the first parameter of `algebra` is an out_param

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156674481):
should we reconsider making it a class instead of making it a structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 23 2019 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677314):
I think for algebra we cannot have it an `out_param` anymore. We already see that it is a problem for `module`, but for `algebra` it completely breaks down

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677450):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677473):
@**Johannes Hölzl** then why is module still using out_param?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 23 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677476):
What does this mean in practice for people like me who don't really know what an `out_param` is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 23 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679581):
@**Kenny Lau** its some work to change it right now, and it requires the user to annotate more types at inconvenient places

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679641):
@**Johannes Hölzl** well I tried to change it before, and then I got some error, and I posted it in the general chat, and nobody helped fix the error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679664):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module.20refactor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 23 2019 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679759):
Yes, we should revive this branch.

