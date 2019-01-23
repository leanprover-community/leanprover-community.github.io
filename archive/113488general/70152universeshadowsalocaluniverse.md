---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70152universeshadowsalocaluniverse.html
---

## Stream: [general](index.html)
### Topic: [universe shadows a local universe](70152universeshadowsalocaluniverse.html)

---


{% raw %}
#### [ Sean Leather (May 17 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684147):
In a file with only this:

```lean
universes u
variables α β : Type*
```

I get this:

```lean
error: invalid universe declaration, 'u_1' shadows a local universe
```

Why?

#### [ Kenny Lau (May 17 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684197):
This also annoys me but I just didn't bother to ask

#### [ Brendan Zabarauskas (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684203):
What does `Type*` do? Does it elaborate into introducing some hidden `u` universe?

#### [ Sean Leather (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684204):
Yeah, it happened once too often for me: passed the annoyance threshold. :wink:

#### [ Sean Leather (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684205):
```quote
What does `Type*` do? Does it elaborate into introducing some hidden `u` universe?
```
It uses an implicit universe, as far as I understand it.

#### [ Johan Commelin (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684207):
`set.option annoyance_threshold 100`

#### [ Johan Commelin (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684211):
Solves it

#### [ Brendan Zabarauskas (May 17 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684255):
I've kind of noticed that Lean's elaboration isn't hygenic... guessing that's by design though?

#### [ Sean Leather (May 17 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684324):
It's very powerful, but it does have some annoying corner cases in various places. I believe the idea is that as long as the kernel is safe and the core language is well-typed, elaboration and tactics can be less so.

#### [ Brendan Zabarauskas (May 17 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684451):
By hygiene I mean in the macro sense. Racket works hard to preserve it. It might make encapsulation harder and increase the chance of breaking things downstream due to updates in libraries.

#### [ Brendan Zabarauskas (May 17 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684503):
(warning, might be being imprecise in my language here, feel free to correct me)

#### [ Sean Leather (May 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684632):
I sometimes like to think of Lean as one big code generator. I tries by various means to produce kernel code for definitions and theorems. Elaboration is an advanced form of unification and uses definitional equality to try to convert terms into other terms. Tactics are like imperatively programming the code generation. Type class instance resolution is another code generation mechanism. All of these try to interpret what you want and produce some kernel code. But they are all imperfect and sometimes require fiddling to get what you want.

(*Edit*: Language is also imprecise, but the idea helps me comprehend it.)

#### [ Brendan Zabarauskas (May 17 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684811):
Yeah, definitely. That's how I'm starting to sort of see it. Just wondering if some of the learning from languages like Scheme and Racket into theorem provers. Not experienced enough with Coq to know how they handle hygiene (if they do any identifier generation in their tactics/elaboration). :thinking_face:

#### [ Mario Carneiro (May 17 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684948):
Hygenic macros are a planned feature in the next version of lean

#### [ Brendan Zabarauskas (May 17 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684951):
Oh nice!

#### [ Brendan Zabarauskas (May 17 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684962):
Yeah thought it might just be an intermediate state of affairs. Hard to do everything at once.

#### [ Mario Carneiro (May 17 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685006):
As for the given error, basically this is because `variables A B : Type*` desugars to
```
universe u_1
variable A : Type u_1
universe u_1
variable B : Type u_1
```
and universe shadowing is disallowed (for some reason...). This is a known bug, but it's unlikely to be addressed in the current version of lean

#### [ Mario Carneiro (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685019):
the workaround is to write `variables (A : Type*) (B : Type*)`

#### [ Brendan Zabarauskas (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685021):
So I'm guessing `universes u` does nothing to affect the issue?

#### [ Mario Carneiro (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685023):
no, it's unrelated

#### [ Mario Carneiro (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685027):
although I bet you can also get a name shadowing issue with only one `variable` if it was `universe u_1`

#### [ Sean Leather (May 17 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685065):
Yeah, I discovered that, too. What is the difference from this?

```lean
variable α : Type*
variable β : Type*
```

#### [ Mario Carneiro (May 17 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685071):
that desugars to
```
universe u_1
variable A : Type u_1
universe u_2
variable B : Type u_2
```
which is okay

#### [ Brendan Zabarauskas (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685081):
In the future, is the intention to make those generated `u_1` identifiers inaccessable?

#### [ Mario Carneiro (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685086):
the variable command in general is more than a little hackish

#### [ Sean Leather (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685090):
Ah. So, it's smart enough to create a fresh universe variable there.

#### [ Mario Carneiro (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685093):
inaccessible? Why?

#### [ Mario Carneiro (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685094):
I think "fresh" is more appropriate

#### [ Mario Carneiro (May 17 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685140):
In fact, they come up explicitly in proofs, although it's bad form to refer to autogenerated names

#### [ Mario Carneiro (May 17 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685141):
but the fact that they are literal names like `u_1` and not some mystery private thing is important

#### [ Brendan Zabarauskas (May 17 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685143):
Hah, I might be conflicting with an existing term by the use of 'inaccessable', but yeah, it seems like it could result in fragile code if you referred to those generated names.

#### [ Brendan Zabarauskas (May 17 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685195):
But happy to be persuaded otherwise - I'm still new to Lean and might not fully understand.

#### [ Sean Leather (May 17 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685197):
Here's my first experience with [variable name shadowing](https://groups.google.com/d/msg/lean-user/-Da6fPijAjY/ZK9JHUfyKAAJ).

#### [ Mario Carneiro (May 17 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685273):
I'm not advocating explicit reference to generated names, just the opposite (that's what I mean by "bad form"). But I can believe that sometimes it is necessary to refer to an autogenerated name, maybe because the tactic that produced the name doesn't have enough configuration space to supply nice names.

#### [ Brendan Zabarauskas (May 17 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685371):
What do you mean by 'configuration space'?

#### [ Mario Carneiro (May 17 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685432):
Some tactics have complicated logic for when they introduce new names, intro variables, etc, and it may not be easy to specify names at the top level so that after the tactic you know what you will get

#### [ Brendan Zabarauskas (May 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685475):
Interesting! That seems like a tantilising design problem to solve! :simple_smile:

#### [ Mario Carneiro (May 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685477):
The lazy option (for the tactic writer) is not to bother with providing names to the tactic, so you get what you get, and then after the tactic you might need to refer to those auto names (if only to rename them)

#### [ Mario Carneiro (May 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685487):
I think that `finish` has this problem, although it's not really designed for nonterminal use so it's not a big problem

#### [ Mario Carneiro (May 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685535):
Some tactics like `injections` just take a big list of names at the start and pull from that pool whenever something is intro'd

#### [ Patrick Massot (May 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126688626):
@**Brendan Zabarauskas** see https://github.com/leanprover/lean/issues/1674 which, I believe, is one the main issue Lean 4 is meant to solve, and contains "Hygienic macro system" in the title. Lean 4 is currently worked on (but won't come soon).

#### [ Brendan Zabarauskas (May 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126689678):
Very cool! And understandable that it will take time - good to know it's coming though.

#### [ Johan Commelin (May 17 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126690354):
Wow, I like the ideas in that issue! @**Patrick Massot** do you remember asking about tikzcd notation for commutative diagrams in lean? That might become a true option then! I like it (-;

#### [ Patrick Massot (May 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126692094):
Indeed I was thinking about this when I mentioned tikz-cd syntax


{% endraw %}
