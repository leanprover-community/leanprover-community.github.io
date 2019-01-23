---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03072hidingwhenimport.html
---

## Stream: [general](index.html)
### Topic: [hiding when import?](03072hidingwhenimport.html)

---

#### [Zesen Qian (Jun 27 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737287):
Hi, is there some way to hiding a name when importing a module?

#### [Simon Hudon (Jun 27 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737350):
You can do that on a namespace scale: `open my_namespace hiding (clashing_def)`

#### [Simon Hudon (Jun 27 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737357):
You can also do selective opening of namespaces

#### [Zesen Qian (Jun 27 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737377):
thank you, I'm still new to the name space space. But what if a name is at the top level of a module?

#### [Zesen Qian (Jun 27 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737390):
or module itself is a namespace?

#### [Simon Hudon (Jun 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737479):
The top most namespace is called `_root_`. Anything in that namespace can be hard to deal with. I'm not sure what the best approach is for dealing with name clashes in the root namespace. The best advice I have is: avoid

#### [Simon Hudon (Jun 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737536):
A module itself is not a namespace. It would be interesting if it was though. Maybe we can request that feature

#### [Zesen Qian (Jun 27 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737637):
OK, maybe I'm wrong, but it seems that parser in  data.buffer.parser is at top level.

#### [Zesen Qian (Jun 27 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737654):
I guess that means this name will be there for all modules recursively importing it,

#### [Zesen Qian (Jun 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737665):
and there is no way to hide it?

#### [Mario Carneiro (Jun 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737681):
hide in what sense?

#### [Mario Carneiro (Jun 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737689):
do you want to name something else `parser` at the top level?

#### [Zesen Qian (Jun 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737736):
A import B, B has a top level name which clashes with a name A wants to use.

#### [Zesen Qian (Jun 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737750):
@**Mario Carneiro** exactly.

#### [Mario Carneiro (Jun 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737759):
that's bad, avoid it

#### [Mario Carneiro (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737772):
`hide` does not change actual names, this will cause a name conflict

#### [Zesen Qian (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737795):
maybe we should ask the author of standard library to avoid it first.

#### [Zesen Qian (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737797):
then we can ask the users to avoid it too.

#### [Mario Carneiro (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737804):
sadly the core lib is frozen

#### [Mario Carneiro (Jun 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737829):
so you will have to work around it

#### [Mario Carneiro (Jun 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737888):
but it's a global coordination problem, it's not a problem until someone else wants the name

#### [Simon Hudon (Jun 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737890):
If you define your own `parser` in your local namespace, doesn't that make it the default definition that will be used as `parser`?

#### [Mario Carneiro (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737901):
yes, that will work fine

#### [Mario Carneiro (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737918):
but it means you can never define `_root_.parser`

#### [Mario Carneiro (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737922):
since it's been defined already

#### [Simon Hudon (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737931):
Right

#### [Zesen Qian (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737985):
to solve it once and for all, we need qualified import, like in haskell.

#### [Mario Carneiro (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737988):
The moral of the story is that you should define most of your stuff in your own namespace

#### [Zesen Qian (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737989):
so you can rename a namespace/module

#### [Mario Carneiro (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737998):
that way core or mathlib can't get in your way

#### [Zesen Qian (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737999):
well again, I don't see the std lib doing it,  so I don't feel obligated to do it either.

#### [Mario Carneiro (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738004):
you aren't stdlib

#### [Zesen Qian (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738009):
why his parser is more fundenmental than mine?

#### [Simon Hudon (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738014):
I think if we could have a qualification to a module like `import data.buffer.parser within buffer` as a way of putting all the definitions directly in the `parser` module in a new `buffer` namespace, that might help manage this situation

#### [Mario Carneiro (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738031):
To be fair, I agree that that parser definition should be in the `buffer` namespace, but in general corelib will take lots of top level names

#### [Reid Barton (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738032):
Unlike in Haskell, though, modules and namespaces are orthogonal in Lean. A module might define names in many namespaces and many modules might define names in the same namespace. So renaming a module doesn't make a lot of sense, in general.

#### [Zesen Qian (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738034):
@**Simon Hudon** that's the "qualified import" I was talking about.

#### [Simon Hudon (Jun 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738102):
That would be a bit different from Haskell though. In Haskell, `qualified` is a form of renaming

#### [Zesen Qian (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738107):
@**Reid Barton** how about this: import A as B. then the top-level def. foo in A becomes B.foo, ns.foo becomes B.ns.foo.

#### [Mario Carneiro (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738137):
and then you define a top level def?

#### [Mario Carneiro (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738150):
because then what happens to files C importing A?

#### [Zesen Qian (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738152):
yes, I'm the king.

#### [Mario Carneiro (Jun 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738204):
Or worse, a file C that imports A and B?

#### [Zesen Qian (Jun 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738238):
it might conflict with the current semantics of import in lean.

#### [Mario Carneiro (Jun 27 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738244):
it sure does

#### [Zesen Qian (Jun 27 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738261):
but since lean always break old stuffs, I see that as a good thing.

#### [Mario Carneiro (Jun 27 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738271):
I mean, what's your solution?

#### [Mario Carneiro (Jun 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738319):
if A has foo, B imports A as A and also defines foo, and C imports A and B, what happens?

#### [Reid Barton (Jun 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738321):
there's also the type-directed `.` notation to worry about

#### [Simon Hudon (Jun 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738386):
I think like in Haskell, the qualification must only be local

#### [Zesen Qian (Jun 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738389):
a practical solution would need thorough consideration of all factors, esp. the ability of .olean format.

#### [Zesen Qian (Jun 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738439):
but I would naively believe there must be a better way.

#### [Reid Barton (Jun 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738534):
A bigger annoyance IMO is that after you have given up and put your own `parser` name inside your own namespace, Lean will still consider `_root_.parser` to be a possible overload for `parser` (as far as I know?)

#### [Mario Carneiro (Jun 27 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738576):
Not inside your namespace

#### [Mario Carneiro (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738629):
and if it gives you trouble you can always make `parser` a local notation

#### [Mario Carneiro (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738639):
that will clobber any overloads

#### [Reid Barton (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738643):
hmm I feel like I've had trouble with this before... but can't recall the details. Maybe inside tactic mode?

#### [Reid Barton (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738650):
And yeah, I used local notation to work around it

