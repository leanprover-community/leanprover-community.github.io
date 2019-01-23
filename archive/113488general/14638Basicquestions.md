---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14638Basicquestions.html
---

## Stream: [general](index.html)
### Topic: [Basic questions](14638Basicquestions.html)

---


{% raw %}
#### [ Charles Rezk (Oct 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010459):
How would I go about proving things about functions between sets, especially finite sets?  I see some machinery for sets (really, "subsets" of a given type), but nothing about functions between them.  On the other hand, I can certainly have functions between types, but I don't see a convenient way to produce a particular "finite type".

#### [ Mario Carneiro (Oct 18 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010589):
what do you want to do with them exactly?

#### [ Mario Carneiro (Oct 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010606):
for the most part you can just write functions between types

#### [ Mario Carneiro (Oct 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010607):
which happen to be finite

#### [ Charles Rezk (Oct 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010704):
Let's say I want to construct a particular finite type, e.g., of size n.  How do I do it?

#### [ Charles Rezk (Oct 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010713):
And how do I prove things about it?

#### [ Mario Carneiro (Oct 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010720):
`fin n` is a type of size n

#### [ Mario Carneiro (Oct 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010771):
and functions out of `fin n` have various properties not shared by general types, for example `list.of_fn` turns a function out of `fin n` into a list of values

#### [ Charles Rezk (Oct 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010780):
Where is the code for fin?

#### [ Mario Carneiro (Oct 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010858):
`init/data/fin` I think

#### [ Mario Carneiro (Oct 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010862):
it's imported by default

#### [ Charles Rezk (Oct 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010937):
I don't see "list" in there.

#### [ Mario Carneiro (Oct 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010957):
that definition is in `data.list.basic`

#### [ Charles Rezk (Oct 18 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011168):
How would I go about constructing a function out of a S:fin n ?

#### [ Mario Carneiro (Oct 18 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011570):
You can just define the function as a lambda...

#### [ Mario Carneiro (Oct 18 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011581):
or you can use `fin.cases`

#### [ Charles Rezk (Oct 18 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011725):
Not sure how to construct anything other than identity function that way.  Because I don't know what the "elements" of fin n are called.

#### [ Mario Carneiro (Oct 18 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011734):
`0`, `1`, `2`, ...

#### [ Charles Rezk (Oct 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011786):
Where in the code for fin does it say that I can do that?

#### [ Mario Carneiro (Oct 18 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011836):
`has_one` and `has_add` give you that for free

#### [ Mario Carneiro (Oct 18 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011845):
`init.fin.ops` I think

#### [ Charles Rezk (Oct 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011997):
Nothing about looking at the code would suggest why that's the case

#### [ Mario Carneiro (Oct 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012053):
The code that actually causes `2` to be parsed as `bit0 1` is in the parser (C++ code), and `bit0` is defined in `init.core`

#### [ Charles Rezk (Oct 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012063):
okay

#### [ Charles Rezk (Oct 18 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012088):
I'd rather read the documentation than look at the code, but there doesn't seem to be any.

#### [ Mario Carneiro (Oct 18 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012104):
Every type that has a 0 and 1 and addition has all numerals

#### [ Charles Rezk (Oct 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012310):
So I can treat elements of a fin n as natural numbers, e.g., add them and such?

#### [ Mario Carneiro (Oct 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012314):
yes

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012316):
Here's the definition of `fin` in `init/data/fin/basic.lean`:
```lean
structure fin (n : nat) := (val : nat) (is_lt : val < n)
```
This says that `fin` takes as input `n`, which should be a `nat` (natural number). `fin n` is then a structure (a certain simple kind of inductive type) which contains a field called `val` (which takes values in `nat`) and a field called `is_lt` (which is a proof that `val < n`). So I would say that `(val : nat)` tells you that the elements of `fin n` can be written as natural numbers.

#### [ Charles Rezk (Oct 18 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012324):
I see.

#### [ Mario Carneiro (Oct 18 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012374):
when you write `10 : fin 3` you actually get `1 = 10 % 3`

#### [ Charles Rezk (Oct 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012414):
Suppose I have an a:nat and an h:a<10.  How do I construct an element of fin 10 from that?

#### [ Mario Carneiro (Oct 18 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012503):
`\langle a, h\rangle`

#### [ Charles Rezk (Oct 18 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012514):
Nothing more readable than than?

#### [ Charles Rezk (Oct 18 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012516):
than that?

#### [ Mario Carneiro (Oct 18 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012543):
There are several ways to write constructors for structures

#### [ Jeremy Avigad (Oct 18 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012546):
@**Mario Carneiro** This is how I would do it:
```
def foo : fin 3 → nat
| ⟨0, _⟩   := 7
| ⟨1, _⟩   := 5
| ⟨2, _⟩   := 6
| ⟨n+3, h⟩ := absurd h (by simp)
```
Is there a better way?

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012547):
In VS code when you start typing `\langle`, you can hit tab and it will autocomplete into the left angle bracket unicode symbol `⟨`

#### [ Charles Rezk (Oct 18 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012595):
What is "by simp" doing there?

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012604):
And you can always put in an explicit type ascription if you're worried that the ⟨⟩ syntax is too obscure.

#### [ Charles Rezk (Oct 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012620):
Assume I know nothing.  What is an explicit type ascription?

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012632):
e.g. `let f := (⟨a : nat ,h : a < 10⟩ : fin 10)`

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012704):
A type ascription is this colon syntax; basically the stuff to the right of the colon is the type of the stuff to the left.

#### [ Mario Carneiro (Oct 18 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012719):
@**Jeremy Avigad** That's the nicest way to define functions out of `fin n` currently (and you can use `dec_trivial` in place of `by simp`), although if you want to prove properties about it `fin.cases` gives a slightly better reasoning

#### [ Mario Carneiro (Oct 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012766):
I've been wondering whether we should have an explicit `fin2 n` type defined as an inductive type so that you get a nice recursion principle

#### [ Mario Carneiro (Oct 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012772):
(This type actually exists in `dioph.lean` but is unused elsewhere)

#### [ Charles Rezk (Oct 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012859):
@**Jeremy Avigad** When I put in that code, it says "simplify tactic failed to simplify"

#### [ Charles Rezk (Oct 18 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012903):
@**Jeremy Avigad**  When I put in that code it says "simply tactic failed to simplify"

#### [ Jeremy Avigad (Oct 18 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012904):
Each element of `fin 3` is something of the form `fin.mk n h` where `n` is a natural number and `h : n < 3`. We can abbreviate `fin.mk n h` as `⟨n, h⟩` because Lean can figure out the relevant constructor from the context.
The style of writing functions using definition by cases is described in Chapter 8 of Theorem Proving in Lean: https://leanprover.github.io/theorem_proving_in_lean/. In the last case, `h` is of the form `n + 3 < n`. We can rule out the case by showing that it is never true. `by simp` calls some built in automation to do that. As Mario points out, `dec_trivial` does something similar. It recognizes that there is a built-in procedure for evaluating inequalities, and uses that to determine that the negation of `n + 3 < 3` is true.

#### [ Mario Carneiro (Oct 18 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012912):
@**Charles Rezk**  does `absurd h dec_trivial` work in place of that code?

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012921):
Yes, replacing `(by simp)` with `dec_trivial` works.

#### [ Mario Carneiro (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012924):
you may need some simp lemmas from mathlib

#### [ Charles Rezk (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012927):
yes

#### [ Charles Rezk (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012929):
grrr

#### [ Mario Carneiro (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012948):
do you not use mathlib?

#### [ Charles Rezk (Oct 18 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012992):
Sure I use mathlib.

#### [ Scott Olson (Oct 18 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012994):
@**Jeremy Avigad** I think you mean `n + 3 < 3`

#### [ Charles Rezk (Oct 18 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013000):
I probably haven't gotten to it.  I'm still trying to figure out functions from finite sets.

#### [ Mario Carneiro (Oct 18 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013008):
gotten to what

#### [ Charles Rezk (Oct 18 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013039):
I don't know.  I started trying to look at groups, then I went backwards because i didn't know how to do anything.

#### [ Jeremy Avigad (Oct 18 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013102):
@Scott thanks, fixed. @Charles, you are right. If you add `import filter.order` to the top of the file it should work. As Mario points out, `absurd h dec_trivial` also works without importing anything.

#### [ Mario Carneiro (Oct 18 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013165):
it's in filter.order? That's embarrasing

#### [ Jeremy Avigad (Oct 18 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013191):
It's probably in something more basic, I just happened to have `filter.order` open and that was sufficient.

#### [ Mario Carneiro (Oct 18 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013200):
also, I think you mean `order.filter`

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013424):
Using `squeeze_simp`, it's `simp only [not_lt, zero_le, le_add_iff_nonneg_left]`, where `not_lt` is in `algebra.order` and the other two are in `algebra.ordered_group`.

#### [ Charles Rezk (Oct 18 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013630):
How would I write that without using any tactics?

#### [ Mario Carneiro (Oct 18 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013862):
`dec_trivial`

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013865):
~~`dec_trivial` isn't a tactic, technically, though it's true that it is kind of opaque.~~ I'll let someone more knowledgeable try to explain what precisely it's doing under the hood.

It looks like the term `(not_lt.mpr $ (le_add_iff_nonneg_left 3).mpr $ zero_le n)` also works, though I just reverse-engineered this from the `squeeze_simp` output above.

#### [ Mario Carneiro (Oct 18 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013876):
there are more efficient term proofs too

#### [ Mario Carneiro (Oct 18 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013883):
but that's the one that simp finds

#### [ Jeremy Avigad (Oct 18 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014109):
@Charles Writing out a fully detailed proof from basic lemmas is painful. Here is one way to do it:
```
example (n : nat) : ¬ (n + 3 < 3) :=
have h1 : 0 ≤ n, from nat.zero_le n,
have h2 : 0 + 3 ≤ n + 3, from nat.add_le_add_right h1 3,
have h3 : 3 ≤ n + 3, from h2,
show ¬ (n + 3 < 3), from not_lt_of_ge h3
```
But this is the sort of thing we really want automation to do: we should just say "this is obvious" and let Lean figure it out. The fact that we generally have to muck around to figure out what to do is a sign that interactive theorem proving is not yet ready for prime time. We are not yet where we want to be.
In fact, Scott Morrison has written an automated procedure called `tidy` that tries lots of "straightforward" things. In this case, it works:
```
import tactic.tidy

example (n : nat) : ¬ (n + 3 < 3) :=
by tidy
```

#### [ Charles Rezk (Oct 18 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014218):
I understand, but I'm trying to understand what is actually going on here.

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014236):
In this case, tidy just calls `dec_trivial` as you can see if you put in `tidy { trace_result:=tt}`.

#### [ Charles Rezk (Oct 18 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014375):
It's not clear to me why I should have to have anything there: defining a function out of fin 3, I wouldn't expect to have to say anything abut its values on 3,4,5,...

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014426):
But an element of `fin 3` is defined as a `nat` called `val` plus a proof that `val` is less than 3. So to define a function out of `fin 3` you need to tell it what to do for every `nat`.

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014492):
For `val`=3,4,5,... that means that you have to show that the proof that `val<3` can't exist.

#### [ Mario Carneiro (Oct 18 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136015055):
The `fin.cases` approach avoids this, although it can't use the equation compiler because it's not built in to lean.
```lean
def f : fin 3 → ℕ :=
fin.cases 7 $
fin.cases 5 $
fin.cases 6 $
λ x, x.elim0
```
```lean
def f : fin 3 → ℕ :=
fin.cases 7 $
fin.cases 5 $
λ _, 6
```

#### [ Mario Carneiro (Oct 18 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136015126):
the last one you can also do in the equation compiler version:
```lean
def foo : fin 3 → nat
| ⟨0, _⟩ := 7
| ⟨1, _⟩ := 5
| ⟨_, _⟩ := 6
```

#### [ Johan Commelin (Oct 18 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136019493):
@**Charles Rezk** Have you seen the tutorials by Neil Strickland? They are amazing. I think they can help you get up to speed with Lean. Besides that, most of us has learned everything we know by just being very persistent in asking questions here.

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136020103):
I would recommend slowly working through "Theorem Proving in Lean" as well. The lean-focused chapters of [Logic & Proof](http://avigad.github.io/logic_and_proof/) were also quite useful to me.

#### [ Kevin Buzzard (Oct 18 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136021426):
@**Charles Rezk** The thing about `fin 3` is that it's a theorem that it has three elements. If you make your own type which has three elements "by definition" then you could do this:

```lean
inductive threetype : Type
| zero : threetype
| one : threetype
| two : threetype

open threetype

definition f : threetype → ℕ
| zero := 59
| one := 65537
| two := 341
```

You can think of the `n + 3 > 3` story as just supplying the proof that there aren't any more elements of `fin 3`.

#### [ Kevin Buzzard (Oct 18 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136024546):
```quote
~~`dec_trivial` isn't a tactic, technically, though it's true that it is kind of opaque.~~ I'll let someone more knowledgeable try to explain what precisely it's doing under the hood.
```
The writers of TPIL probably fit the bill:

https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#decidable-propositions


{% endraw %}
