---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78590namespacefieldnotation.html
---

## Stream: [general](index.html)
### Topic: [namespace field notation](78590namespacefieldnotation.html)

---

#### [Sean Leather (Apr 11 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921576):
Before I disappeared for a month to handle a visiting-family exception, I was experimenting with using more “namespace field notation.” That is, instead of using `list.map f l`, I would use `l.map f`. I like the conciseness gained by removing the namespace `list`.

However, I had started to sour on it then, and, after returning to my code and trying to refresh my working cache, I find that I no longer like it. Since the field notation differs from the definition notation and from the pretty-printed `lean` output in errors, going back and forth between notations requires repeatedly reorienting on the positions of arguments. (While `list.map` is a nice example for advocating use of the notation, when a definition has more than 2 parameters or typically needs bracketed arguments, the notation does not help.)

If we could write definitions using namespace field notation and if the notation were used by `lean` to pretty-print, I believe the benefit would become clear. Otherwise, I don't think I'll be using it much.

What do you think?

#### [Mario Carneiro (Apr 11 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921708):
It doesn't really make sense to use projection notation in definitions, since it requires that the variable already be declared and have known type. You certainly won't get this before you've even stated the theorem name

#### [Mario Carneiro (Apr 11 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921747):
projection in pretty printing would be nice, but I don't know how hard it is

#### [Mario Carneiro (Apr 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921757):
also it's one more thing that can break in inconvenient ways if the pretty printed expression doesn't quite typecheck due to too many implicit things

#### [Sean Leather (Apr 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921758):
```quote
It doesn't really make sense to use projection notation in definitions, since it requires that the variable already be declared and have known type. You certainly won't get this before you've even stated the theorem name
```
Perhaps there could be some alternative `notation`-like operation to allow being explicit about the projection instead of using the built-in rule that now exists.

#### [Mario Carneiro (Apr 11 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921798):
I don't follow

#### [Sean Leather (Apr 11 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921806):
In other words, perhaps the implicit projection rule could be replaced with an explicit projection declaration.

#### [Sean Leather (Apr 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921853):
It would (a) be more flexible and (b) add documentation of the projection notation for a particular definition.

#### [Sean Leather (Apr 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921862):
```quote
also it's one more thing that can break in inconvenient ways if the pretty printed expression doesn't quite typecheck due to too many implicit things
```
@**Mario Carneiro** What is “it” referring to here?

#### [Mario Carneiro (Apr 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921863):
What kind of flexibility are you thinking? Also I don't relish the idea of adding thousands of annotations for what is essentially redundant information, and having to keep it up to date. The current projection algorithm is easy to learn and completely uniform

#### [Mario Carneiro (Apr 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921948):
"it" is pp projection notation. The elaborator has less to go on with projection notation, so if it can't solve for the type of a variable immediately projections just halt the whole type inference process. I'm saying that this situation may occur with pp expressions, assuming you aren't using some `pp.all` type option

#### [Sean Leather (Apr 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921998):
```quote
What kind of flexibility are you thinking?
```

Declaring which parameter should be used for projection is the main one that comes to mind. I recall running into an issue where projection didn't work, but I think it would if I could explicitly declare how to do it. (I don't remember the exact issue, unfortunately.)

#### [Sean Leather (Apr 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922012):
```quote
"it" is pp projection notation. The elaborator has less to go on with projection notation, so if it can't solve for the type of a variable immediately projections just halt the whole type inference process. I'm saying that this situation may occur with pp expressions, assuming you aren't using some `pp.all` type option
```

Yes, I could see how that could be a problem if pretty-printing involves inferring the projection notation. But, given the above idea of an explicit projection notation, it would not need to infer anything.

#### [Mario Carneiro (Apr 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922016):
Projection was less powerful early in its history, because you could only project with the first explicit argument. That restriction has since been dropped, so make sure that isn't the issue you are thinking of

#### [Mario Carneiro (Apr 11 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922063):
it would still need to infer stuff even with projection annotations, since `x.bar` could mean either `list.bar x` if `x : list a` or `multiset.bar x` if `x : multiset a`, or even `x.bar` if `x` is a namespace

#### [Sean Leather (Apr 11 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922078):
```quote
Projection was less powerful early in its history, because you could only project with the first explicit argument. That restriction has since been dropped, so make sure that isn't the issue you are thinking of
```

No, I don't think that's relevant. My issue is with going back and forth between two different notations.

#### [Mario Carneiro (Apr 11 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922080):
That just sounds like a pp problem

#### [Mario Carneiro (Apr 11 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922130):
I just always use projections in the code, and replace anything I copy after pp with projections

#### [Sean Leather (Apr 11 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922135):
```quote
That just sounds like a pp problem
```

A bit too simplistic of a view, I think. I'm pretty sure we don't want to pretty-print everything in projection notation.

#### [Mario Carneiro (Apr 11 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922141):
so there's no back and forth unless I'm doing a lot of copy paste from pp anyway, which produces non-human output for several reasons, that's not the only thing I want to change in general

#### [Sean Leather (Apr 11 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922435):
Here's a simple example:

1. Projection:
```lean
t.open ts = subst_list xs ts (t.open (xs.map varf))
```

2. No projection:
```lean
typ.open ts t = subst_list xs ts (typ.open (list.map varf xs) t)
```

The first option is less verbose, but I only ever see it in code I write. The second is what the pretty-printer shows.

#### [Sean Leather (Apr 11 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922436):
Here are some questions and thoughts prompted by the discussion above:

Why shouldn't I be able to tell Lean to pretty-print the projection notation as in 1? I can already tell it to use some other `notation` or `infix`. I don't see how the inference problem is different.

Once I am allowed to say I want definition `d` to be pretty-printed with projection notation, why shouldn't I be able to declare which parameter is the projection target? Consequently, the declaration to “use projection notation” becomes another `notation` or `infix` but specialized to projection.

#### [Mario Carneiro (Apr 11 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922714):
> The first option is less verbose, but I only ever see it in code I write. The second is what the pretty-printer shows.
> Why shouldn't I be able to tell Lean to pretty-print the projection notation as in 1? 

Like I said, a pp problem. There's nothing wrong with this in principle, except this is a core lean issue so it's not going to happen until lean 4, and that only if Leo thinks of this himself

#### [Mario Carneiro (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922804):
> Once I am allowed to say I want definition d to be pretty-printed with projection notation, why shouldn't I be able to declare which parameter is the projection target? Consequently, the declaration to “use projection notation” becomes another notation or infix but specialized to projection.

There isn't really any choice in what argument can be the projection argument, except in definitions which, say, take in more than one `list` parameter. If you think the second argument is a better projection target than the first, then I suggest you reorder the parameters

#### [Sean Leather (Apr 11 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922826):
```quote
Like I said, a pp problem. There's nothing wrong with this in principle, except this is a core lean issue so it's not going to happen until lean 4, and that only if Leo thinks of this himself
```

Right, but I don't think that means that I can't bring it up here and discuss it, does it? :wink:

#### [Sean Leather (Apr 11 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922879):
```quote
There isn't really any choice in what argument can be the projection argument, except in definitions which, say, take in more than one `list` parameter. If you think the second argument is a better projection target than the first, then I suggest you reorder the parameters
```

I disagree. You could expand projection to include things outside the namespace of the definition.

#### [Mario Carneiro (Apr 11 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922930):
No, that doesn't really work with the way projections are resolved. It gets the type of the argument, and uses that as a namespace to look up projections. If you want a projection to work on a certain argument, make sure the namespace lines up

#### [Sean Leather (Apr 11 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922944):
But it *could* work that way with explicit projection notation. :simple_smile:

#### [Mario Carneiro (Apr 11 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922946):
It obviously has to key on *something*, since otherwise it has to go through all the definitions, and the only available information at that point is the type of the variable

#### [Mario Carneiro (Apr 11 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923047):
I don't see the difference between an explicit projection notation and naming the definition appropriately so the automatic method picks out the desired argument. Do you have a concrete example where you think it would be difficult to do otherwise?

#### [Sean Leather (Apr 11 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923160):
I did at one point. It had to do with a list parameter, I think, but I don't remember it now.

#### [Sean Leather (Apr 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923432):
Generally, though, suppose you have a definition that is not for general `list`s but has a `list` parameter and you want projection on an `list` argument, you would need to put the definition in the `list` namespace. Slightly more concretely, suppose you have something like `def n.d : list n → Prop`. So, to get projection notation, you would need to rename `n.d` to `list.d`. That seems wrong.

#### [Patrick Massot (Apr 11 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923698):
Sean, since you seem to care about this projection notation, have you seen https://github.com/leanprover/mathlib/pull/96 ? Don't hesitate to propose any further clarification or new tricks in [the relevant section](https://github.com/PatrickMassot/mathlib/blob/8bf2648418549d605a18fe5d38a67eb725e66317/docs/extras/structures.md#about-the-namespace-shortcut)

#### [Sean Leather (Apr 11 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923908):
@**Patrick Massot** I saw it. It was part of the reason, other than that I've been thinking about it for a while, that I brought up the subject.

I think the only change I would make is that “first explicit argument” is not correct. As @**Mario Carneiro** said, the argument (or what I prefer to call “parameter”) need not be explicit. In other words, you could have this:

```lean
def sum (α : Type) [has_add α] : point α → α := λ p, p.x + p.y
#reduce p.sum α
```

#### [Patrick Massot (Apr 11 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923954):
What would you write then?

#### [Sebastian Ullrich (Apr 11 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924022):
@**Sean Leather** 
> So, to get projection notation, you would need to rename n.d to list.d. That seems wrong.

But this is how it works in OOP languages the notation was borrowed from, if you interpret classes as introducing namespaces. How would we know to look in the namespace `n` for `d`?

#### [Sean Leather (Apr 11 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924026):
@**Patrick Massot** The simplest change would be to remove “explicit” and to give an example in which the argument is not explicit. You could use the one above, though you should check it first to make sure I didn't make a mistake.

#### [Sebastian Ullrich (Apr 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924080):
@**Gabriel Ebner** Btw, have we ever discussed a notation like `xs.(map f).(filter g)` to solve the chaining issue? I might have to experiment with a macro for that in Lean 4 :laughing: .

#### [Patrick Massot (Apr 11 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924122):
Actually I don't know how to call that kind of argument that lingers right of the colon. My explicit was rather referring to `(x : X)` vs `{x : X}`.

#### [Patrick Massot (Apr 11 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924127):
```quote
But this is how it works in OOP languages the notation was borrowed from, if you interpret classes as introducing namespaces. How would we know to look in the namespace `n` for `d`?
```
At last, someone confess FP is trying to mimic OOP greatness

#### [Sean Leather (Apr 11 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924136):
@**Patrick Massot** Ah, okay. I may have misinterpreted it then. :simple_smile:

#### [Sean Leather (Apr 11 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924137):
@**Sebastian Ullrich**:
```quote
But this is how it works in OOP languages the notation was borrowed from, if you interpret classes as introducing namespaces. How would we know to look in the namespace `n` for `d`?
```
I don't follow. In OOP, you wouldn't find a method with the type `list n` in a `list` class.

#### [Patrick Massot (Apr 11 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924183):
But I'm interested in explaining how far that projection notation extends. So I'll definitely try that `def sum (α : Type) [has_add α] : point α → α := λ p, p.x + p.y
`

#### [Patrick Massot (Apr 11 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924188):
But right now I'm typing notes on the Nash-Kuiper embedding theorem, not playing with Lean or chatting on Zulip

#### [Sebastian Ullrich (Apr 11 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924193):
@**Sean Leather** In Java, `x.f` will look up `f` in the class of `x` and pass `x` as the `this` argument. Basically what happens in Lean.

#### [Sebastian Ullrich (Apr 11 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924311):
The whole point of field notation is to hide the namespace. I don't see the benefit of `p.sum` over `sum p`.

#### [Sean Leather (Apr 11 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924433):
```quote
In Java, `x.f` will look up `f` in the class of `x` and pass `x` as the `this` argument. Basically what happens in Lean.
```

Right. It also extends the lookup to superclasses. But still, that's rather limiting, I think.

#### [Sebastian Ullrich (Apr 11 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924449):
> It also extends the lookup to superclasses.

As we do

#### [Sean Leather (Apr 11 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924452):
What's a superclass in Lean?

#### [Sebastian Ullrich (Apr 11 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924502):
The thing after `extends` :)

#### [Sean Leather (Apr 11 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924513):
Are you talking about `class` or `namespace`? I wasn't aware a `namespace` could `extends` something.

#### [Gabriel Ebner (Apr 11 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924570):
```quote
@**Gabriel Ebner** Btw, have we ever discussed a notation like `xs.(map f).(filter g)` to solve the chaining issue? I might have to experiment with a macro for that in Lean 4 :laughing: .
```
No I don't think so.  I think the only proposal that aimed to simplify chaining was my Agda-like `xs .map f .filter g`, which many people apparently found abhorrent.

#### [Sebastian Ullrich (Apr 11 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924578):
@**Sean Leather** Ah sorry, I was thinking of the basic field notation, which will pick up fields from super structures as well. But it doesn't work with functions in the namespace... yet

