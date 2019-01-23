---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03873isleftassociative.html
---

## Stream: [general](index.html)
### Topic: [^ is left associative](03873isleftassociative.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 13 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123659529):
Is that normal? `#eval 2^3^2` gives 64. I don't know any other language where this is the case. I just tried python, pari, sage and they all give me 2^(3^2)=512.

#### [ Kevin Buzzard (Mar 13 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123670890):
Wikipedia page on associativity https://en.wikipedia.org/wiki/Operator_associativity explicitly mentions `^` as being essentially a canonical example of a right associative operator. This is a very bizarre implementation decision. Whatever reason is there for it? `(a^b)^c` is just `a^(b*c)` but `a^(b^c)` cannot be written in any simpler way and is hence the natural choice. Should I file an issue? Is this just an oversight? Should I just fix it and submit a PR?

#### [ Simon Hudon (Mar 13 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123670972):
I might be at fault for that issue. As far as I know, I was the first one to commit code for the exponential operator and I think I didn't put much thought into its associativity. It's worth filing an issue. It's also easy to fix so they might be happy if you file a PR that they just have to merge

#### [ Kevin Buzzard (Mar 13 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671027):
We're talking init/data/nat/basic.lean, copyright 2014 Floris van Doora and Leo de Moura

#### [ Andrew Ashworth (Mar 13 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671157):
i think this falls under the nitpicking issues will not be tolerated clause

#### [ Andrew Ashworth (Mar 13 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671166):
:/ but i agree ideally it should be right associative

#### [ Kevin Buzzard (Mar 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671419):
:/

#### [ Kevin Buzzard (Mar 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671428):
It's not a nitpicking issue, it's a nitpicking PR!

#### [ Kevin Buzzard (Mar 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671439):
If it breaks anything, the thing it breaks deserves to be broken!

#### [ Simon Hudon (Mar 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671737):
```quote
We're talking init/data/nat/basic.lean, copyright 2014 Floris van Doora and Leo de Moura
```
I initially put it in a `pow` file. They probably merged it with basic and dropped my name

#### [ Sebastian Ullrich (Mar 13 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123672684):
Wasn't there a discussion that this should be generalized to a typeclass anyway? If someone PRs those changes, they'll get a "looks good to me" from me.

#### [ Simon Hudon (Mar 13 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673194):
that type class exists in `mathlib`. It would be great indeed to move it to core. That would remove the operator clash

#### [ Sebastian Ullrich (Mar 13 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673243):
Alternatively, do a PR that removes the notation :P

#### [ Simon Hudon (Mar 13 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673328):
Isn't it used in core?

#### [ Simon Hudon (Mar 13 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673342):
I see that bitvec uses it

#### [ Simon Hudon (Mar 13 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673469):
Is that something that should be moved to `mathlib`?

#### [ Kevin Buzzard (Mar 13 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673796):
Well so far I have cloned lean, changed ``infix `^` := pow`` to ``infixr `^` := pow``, recompiled, and found that `#print notation ^` still reports ``_ `^`:80 _:80 := nat.pow #1 #0``

#### [ Kevin Buzzard (Mar 13 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673800):
I could have made a mistake I guess.

#### [ Kevin Buzzard (Mar 13 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123674953):
Ok so I did it again and the same thing happened. Changing line 204 of `library/init/data/nat/basic.lean` from ``infix `^` = pow`` to ``infixr `^` = pow` and then compiling lean and feeding a test file into it directly with `./lean ~/test.lean` still gives me left associativity. Aah well.

#### [ Kevin Buzzard (Mar 13 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675029):
PS It's needed as a map `G x Z -> G` (G a group, Z the integers), as a map `M x N -> M` (M a multiplicative monoid, N the naturals) etc. Is a typeclass the best solution? I think Mario explained all this once to me on gitter but I doubt I'll ever find it :-/

#### [ Mario Carneiro (Mar 13 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675077):
Your modification is correct, I think you aren't compiling something

#### [ Kevin Buzzard (Mar 13 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675099):
I'm just cut and pasting from the generic build instructions like a moron

#### [ Kevin Buzzard (Mar 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675109):
I surely don't have to use git in any way?

#### [ Kevin Buzzard (Mar 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675151):
I am just cloning, editing the file, and then making

#### [ Kevin Buzzard (Mar 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675216):
I've done it three times now so I suspect that it's not me failing to edit the file or failing to run the correct binary, I think now that it's more likely either that the generic build instructions are somehow clobbering my edits or that there's something else I'm missing. I've tried defining a new right associative operator to mean nat.pow and it works fine. It's just `^` that is still misbehaving


{% endraw %}
