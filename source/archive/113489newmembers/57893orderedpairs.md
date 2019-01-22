---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/57893orderedpairs.html
---

## [new members](index.html)
### [ordered pairs](57893orderedpairs.html)

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077221):
I'm defining a subset of the Cartesian product of two types, specifically: 

```lean
def graph : set X × Y :=
    {(x : X, f x) | x : X}
```

(`f` is a function, `x` has not been separately defined) What's the right notation for this (the ordered pairs, and also the set builder itself)?

#### [Kenny Lau (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077285):
what do you mean by "right notation"?

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077288):
A notation that works in Lean.

#### [Kenny Lau (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077300):
do you mean `set (X × Y)`?

#### [Kenny Lau (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077303):
oh

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077304):
No, I mean for the ordered pairs.

#### [Kenny Lau (Oct 19 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077370):
```lean
universes u v
variables {X : Type u} {Y : Type v} (f : X → Y)
def graph : set (X × Y) :=
{ z | z.2 = f z.1 }
```

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077386):
Ah.

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077387):
Thanks.

#### [Kevin Buzzard (Oct 19 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077411):
It's kind of annoying that you can't write `{⟨x,y⟩ : X × Y | y = f x}`

#### [Kenny Lau (Oct 19 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077469):
you can't define that in ZFC either

#### [Kenny Lau (Oct 19 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077470):
you need to use specification and an existential

#### [Kevin Buzzard (Oct 19 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077487):
I guess you could use `set.image` or `set.range`, whatever it's called

#### [Kevin Buzzard (Oct 19 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077650):
`def graph' : set (X × Y) := set.range (λ x, ⟨x,f x⟩) `

#### [Kevin Buzzard (Oct 19 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077661):
(after `import data.set.basic`)

#### [Kenny Lau (Oct 19 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077723):
```lean
import data.set.lattice
universes u v
variables {X : Type u} {Y : Type v} (f : X → Y)
def graph : set (X × Y) :=
⨆ x : X, {(x, f x)}
```

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077827):
What's `⨆`?

#### [Kevin Buzzard (Oct 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077886):
```lean
import data.set.basic

variables (X Y : Type) (f : X → Y)

def graph  : set (X × Y) := {z : X × Y | z.2 = f z.1}

def graph' : set (X × Y) := set.range (λ x, ⟨x,f x⟩) 

example : graph = graph' := sorry
```

#### [Kenny Lau (Oct 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077894):
`set X` is a complete lattice

#### [Kevin Buzzard (Oct 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077913):
Abhi: `⨆` is notation so you can start with `#print notation ⨆`

#### [Kevin Buzzard (Oct 19 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077923):
but if you don't want to go down the lattice rabbithole you could try my homework :-)

#### [Kevin Buzzard (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077997):
I'd be able to do the homework myself if I knew how to prove `A = B iff B = A` :-/

#### [Kevin Buzzard (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077999):
`eq.symm` only goes one way

#### [Kenny Lau (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078000):
eq_comm

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078007):
I'm not sure how to interpret the results of #print notation. All I get is `'⨆':1024 binders ',':0 (scoped 0) := #0` What's a binder?

#### [Kevin Buzzard (Oct 19 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078057):
oh oops

#### [Kevin Buzzard (Oct 19 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078060):
yes that is impossible to interpret

#### [Kevin Buzzard (Oct 19 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078085):
A binder is something like forall or exists or lambda I think

#### [Kevin Buzzard (Oct 19 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078094):
Kenny is using `⨆` in the same sort of way that one would use those things.

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078137):
Yeah, I can tell it's something like forall, but I'm not sure what the difference is.

#### [Mario Carneiro (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078141):
I think you can click on the sup to go to definition

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078143):
I get "no definition found"

#### [Mario Carneiro (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078144):
It's the analogue of `\bigcup` for lattices

#### [Kevin Buzzard (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078146):
It's in `order/complete_lattice.lean`

#### [Kevin Buzzard (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078149):
`notation `⨆` binders `, ` r:(scoped f, supr f) := r`

#### [Kevin Buzzard (Oct 19 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078169):
I taught Abhi about bigcup today in lectures :-)

#### [Kevin Buzzard (Oct 19 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078211):
Glad to see my lectures are coming in handy in his day to day life

#### [Mario Carneiro (Oct 19 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078237):
"day to day life"

#### [Kevin Buzzard (Oct 19 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078244):
I don't understand that notation line at all. I think notation in Lean is somehow evil; most of it is fine and then there are some weird hacks which I don't get at all. The key point is `supr` somehow, and then everything else is some notation mantra I guess

#### [Kevin Buzzard (Oct 19 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078294):
`def supr [complete_lattice α] (s : ι → α) : α := Sup {a : α | ∃i : ι, a = s i}`

#### [Kevin Buzzard (Oct 19 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078339):
so `supr s` is the supremum of the range of `s`

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078511):
Btw I'm trying `def p1 (g : graph) : X := g.1` based on the earlier definition of `graph`, but it doesn't work:

```lean
invalid field notation, type is not of the form (C ...) where C is a constant
  g
has type
  ⁇
```

```lean
universe u
variable {X : Type u}
variable {Y : Type u}
variable {f : X → Y}
def graph : set (X × Y) := { g | g.2 = f g.1 }
def p1 (g : graph) : X := g.1
```

I guess part of the problem is that `G` is not a type -- I tried coercing it as `↑G`, but that just produces more errors.

#### [Reid Barton (Oct 19 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078535):
I think the bigger problem is Lean doesn't know what you want to take the graph of

#### [Mario Carneiro (Oct 19 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078541):
I can't make sense of that definition

#### [Reid Barton (Oct 19 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078543):
I would make `f` an explicit argument and then pass it in `p1`

#### [Mario Carneiro (Oct 19 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078594):
what does `g : graph` mean?

#### [Mario Carneiro (Oct 19 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078596):
it's not a type

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078618):
```quote
what does `g : graph` mean?
```
Yeah, I realise that, but I want to show (separately from the definition) it's a bijection from `graph` to `X`.

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078677):
```quote
I would make `f` an explicit argument and then pass it in `p1`
```
Indeed that removes the first error. How, though?

#### [Mario Carneiro (Oct 19 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078690):
Keep in mind that `graph f`is not a type either, it's a set

#### [Mario Carneiro (Oct 19 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078699):
lean knows to coerce from a set to a type, but maybe you want the subtype instead?

#### [Kevin Buzzard (Oct 19 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078706):
a set is a term not a Type Abhi. Did you come to my lecture today?

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078759):
```quote
a set is a term not a Type Abhi. Did you come to my lecture today?
```
I realise that -- but how else would I later show it to be a bijection from graph to X?

#### [Kevin Buzzard (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078760):
If `X` is a type and `p : X -> Prop` then in Lean there are two very different ways to express what in set theory is just "the subset of X consisting of elements `a` for which `p a` is true"

#### [Kenny Lau (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078763):
it did took me some time to figure out that Kevin wants us to prove that the two big big functions `graph` and `graph'` are equal

#### [Kenny Lau (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078770):
so you should start with `ext X Y f`

#### [Kevin Buzzard (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078772):
One is the set `{x : X | p x}` and one is the subtype `{x : X // p x}`

#### [Kevin Buzzard (Oct 19 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078800):
I am in the middle of showing my `graph` is Kenny's `supr` thing

#### [Kenny Lau (Oct 19 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078861):
I bet `example : graph = graph' :=` isn't what Kevin wanted us to prove

#### [Kevin Buzzard (Oct 19 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078867):
I proved that using `eq.comm`

#### [Kenny Lau (Oct 19 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078880):
`example : graph X Y f = graph' X Y f :=`

#### [Kevin Buzzard (Oct 19 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079017):
```lean
import data.set.basic
import data.set.lattice

variables (X Y : Type) (f : X → Y)

def graph  : set (X × Y) := {z : X × Y | z.2 = f z.1}

def graph' : set (X × Y) := set.range (λ x, ⟨x,f x⟩) 

def graph'' : set (X × Y) := ⨆ x : X, {(x, f x)}

example : graph = graph' := sorry

example : graph = graph'' := sorry
```
I did them both :-)

#### [Kevin Buzzard (Oct 19 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079020):
I am not proud of the second one though.

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079102):
Re:the bijection, I *can* write `def p1 (g : graph f) := g.1`(still defining `graph` as a set because subtype gives me even more errors), but then `p1` for some reason has the wrong type. Apparently `g.1` isn't processed correctly (it still has type `X × Y` and not `X`).

#### [Mario Carneiro (Oct 19 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079129):
that has to do with the fact that it is a subtype

#### [Mario Carneiro (Oct 19 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079183):
`g` is a pair of an element of `X x Y` and a proof that this element satisfies `z.2 = f z.1`

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079184):
Is the notation for ordered pairs different for subtypes?

#### [Mario Carneiro (Oct 19 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079190):
so the X value is `g.1.1`

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079202):
That works, but I don't get why.

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079207):
(deleted)

#### [Reid Barton (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079216):
or `g.val.fst`

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079275):
Ok, I get the argument, but I'm not sure why it's defined that way (to include a proof).

#### [Reid Barton (Oct 19 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079360):
If you didn't have to provide a proof when constructing a value of the subtype, then it would just be the same as the entire original type.

#### [Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079477):
Why does the same convention not apply to sets?

#### [Reid Barton (Oct 19 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079571):
I don't really understand the question. A set is not a type; perhaps that's the answer

