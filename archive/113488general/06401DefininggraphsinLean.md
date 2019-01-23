---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06401DefininggraphsinLean.html
---

## Stream: [general](index.html)
### Topic: [Defining graphs in Lean](06401DefininggraphsinLean.html)

---


{% raw %}
#### [ Hoang Le Truong (Jul 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129399957):
I definite a function on the certain domain as follow
```
def V: set ℕ := {1,2,3,4}

def g [has_one V][has_add V](e:V× V ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|_     :=0
end
```
I received the following  message
```
equation compiler failed (use 'set_option trace.eqn_compiler.elim_match true' for additional details)
``` 
and
```
invalid function application in pattern, it cannot be reduced to a constructor (possible solution, mark term as inaccessible using '.( )') 1
```
What is error?

#### [ Kenny Lau (Jul 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400000):
`V` is not an inductive type.

#### [ Kenny Lau (Jul 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400011):
you can't match it

#### [ Kenny Lau (Jul 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400050):
you can't just "make it work" by using `[has_one V] [has_add V]`

#### [ Hoang Le Truong (Jul 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400103):
I need make ```V``` as an inductive type, not is subset of ```\N```

#### [ Kenny Lau (Jul 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400106):
depends on your purpose

#### [ Kenny Lau (Jul 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400108):
I would just use if-then-else

#### [ Hoang Le Truong (Jul 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400153):
I need V is subset of ```\N```

#### [ Hoang Le Truong (Jul 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400171):
how are we use ```V``` is an inductive type and subset of ```\N```

#### [ Johan Commelin (Jul 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400248):
`def g : V \times V \to nat := \lam x, if x.1 * x.2 = 2 then 2 else 0`

#### [ Johan Commelin (Jul 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400252):
Something like that?

#### [ Kenny Lau (Jul 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400260):
```lean
inductive def V : \N \to Prop
| one : 1 \to V
| two : 2 \to V
| three : 3 \to V
| four : 4 \to V
```

#### [ Hoang Le Truong (Jul 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400408):
@**Johan Commelin**  It is ok but if I have function has domain is random and large. It is not good to make function when use ```if - then-else```

#### [ Kenny Lau (Jul 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400426):
maybe you should tell us what you want to do

#### [ Hoang Le Truong (Jul 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400490):
I want to make function with card V=100 and valued is random

#### [ Kenny Lau (Jul 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400496):
randomness doesn't exist

#### [ Kevin Buzzard (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400509):
(in Lean)

#### [ Kenny Lau (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400511):
randomness doesn't exist, period

#### [ Johan Commelin (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400514):
What do you mean with "valued is random", do you mean that `V` is an arbitrary subset of `\N`?

#### [ Kenny Lau (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400515):
a random variable is neither random nor a variable

#### [ Kevin Buzzard (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400519):
(I guess the quantum mechanics course is next year Kenny, right?)

#### [ Hoang Le Truong (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400558):
yes

#### [ Kenny Lau (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400562):
alright

#### [ Johan Commelin (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400565):
Kenny will *choose* not to follow QM...

#### [ Kenny Lau (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400567):
lol

#### [ Johan Commelin (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400572):
Hoang, ok, and what should your function do with `V`?

#### [ Johan Commelin (Jul 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400584):
You want a function `V \to \N`, is that right?

#### [ Hoang Le Truong (Jul 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400588):
yes is randomness doesn't exist
I want find example function ```g```

#### [ Hoang Le Truong (Jul 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400633):
```
def G (e:ℕ× ℕ ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end

```

#### [ Hoang Le Truong (Jul 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400641):
it is ok but I want to certain domains ```V```

#### [ Kevin Buzzard (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400649):
Maybe you should define your function on all of nat x nat

#### [ Kevin Buzzard (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400650):
and then just ignore its values on the elements you don't like

#### [ Johan Commelin (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400651):
Ok, so define the function on `\N \times \N`, and then restrict to `V`

#### [ Kenny Lau (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400652):
i'll say it isn't even a function

#### [ Johan Commelin (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400694):
Kenny, did you read that translation of the article by Aristotle?

#### [ Kevin Buzzard (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400699):
This is a standard trick in this game: for example the square root function in Lean is defined on all the reals, and returns the square root of x if x>=0 but just returns something random if x < 0

#### [ Kenny Lau (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400701):
what about it

#### [ Johan Commelin (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400705):
something *random* <-- Kevin

#### [ Kevin Buzzard (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400706):
you are just making noise Kenny, not contributing, that's what about it

#### [ Hoang Le Truong (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400707):
yes I want it

#### [ Kevin Buzzard (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400716):
When I thought more like a mathematician, I really thought I wanted the square root function to be only defined on the non-negative reals

#### [ Hoang Le Truong (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400720):
I want same as @**Kevin Buzzard**

#### [ Kenny Lau (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400727):
I don't even know what function he wants to build. My understanding is that he wants some kind of a function defined on N x N, and then he just randomly gives some values in the two examples he gave us

#### [ Kevin Buzzard (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400729):
but after building such a function myself, and then discovering how hard it was to use it, I started coming round to the methods which Mario and others were preaching.

#### [ Kenny Lau (Jul 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400777):
he wants an arbitrary function N x N -> N, that's all I can make of it

#### [ Kevin Buzzard (Jul 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400779):
right, so let's listen to him and find out more.

#### [ Hoang Le Truong (Jul 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400846):
In fact, I have function with certain properties. I want example from such function

#### [ Kenny Lau (Jul 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400850):
what properties?

#### [ Kevin Buzzard (Jul 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400904):
What do you mean by "example"? You mean an example of the function, or example of a value, or example of a definition, or... ? When you say "I have function" -- you mean you have the definition of the function already? In Lean or on paper? Or you just have some properties which you want the function to satisfy?

#### [ Kevin Buzzard (Jul 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400908):
We are still trying to understand your question.

#### [ Sean Leather (Jul 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129401005):
I think one property of the function Hoang wants is the type: `ℕ × ℕ → ℕ`.

#### [ Sean Leather (Jul 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129401126):
Or perhaps the type should have subsets of `ℕ`?

#### [ Sean Leather (Jul 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129401214):
`{ns : ℕ × ℕ // p ns} → ℕ` for some `p : ℕ × ℕ → Prop`?

#### [ Hoang Le Truong (Jul 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402299):
graph is connected

#### [ Hoang Le Truong (Jul 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402300):
I want check the definition of graph is correct

#### [ Hoang Le Truong (Jul 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402301):
I think g is graph

#### [ Kevin Buzzard (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402359):
What does this have to do with nat?

#### [ Hoang Le Truong (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402375):
```
variables {α : Type }   
variable graph: α × α → ℕ 
```

#### [ Hoang Le Truong (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402387):
I think function```graph``` is graph

#### [ Kevin Buzzard (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402388):
Is alpha the vertices of the graph? What is nat doing there?

#### [ Hoang Le Truong (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402393):
yes

#### [ Kevin Buzzard (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402404):
What is a graph? For me it is vertices and edges, and there is no `ℕ`

#### [ Hoang Le Truong (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402418):
```
def G (e:ℕ× ℕ ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
```

#### [ Hoang Le Truong (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402421):
is example of graph

#### [ Kevin Buzzard (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402426):
What is a graph for you?

#### [ Hoang Le Truong (Jul 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402490):
vertices ```def V: set ℕ := {1,2,3,4}```

#### [ Kenny Lau (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402507):
so every graph is countable

#### [ Hoang Le Truong (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402530):
I do not know

#### [ Hoang Le Truong (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402623):
I have that definition of connected graph. I want check such definition in lean which I make is true or fail. I make an example of such definition

#### [ Hoang Le Truong (Jul 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402765):
I make example of graph
```
def G (e:ℕ× ℕ ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
````
it is ok. but 
```
def V: set ℕ := {1,2,3,4}

def G (e:V× V ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end

```
is it not run

#### [ Kevin Buzzard (Jul 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402771):
Aah

#### [ Mario Carneiro (Jul 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402779):
this is the konigsberg graph?

#### [ Kevin Buzzard (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402784):
rofl

#### [ Hoang Le Truong (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402787):
yes

#### [ Kevin Buzzard (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402792):
even more rofl

#### [ Mario Carneiro (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402799):
I would use custom inductive types for all of it

#### [ Hoang Le Truong (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402802):
no

#### [ Mario Carneiro (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402807):
`inductive vertices | north_shore | west_island | ...`

#### [ Kevin Buzzard (Jul 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402856):
@**Hoang Le Truong** -- he is saying that you should make your own type called `graph`

#### [ Kevin Buzzard (Jul 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402862):
and I would definitely agree with him

#### [ Mario Carneiro (Jul 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402871):
```
inductive edges : vertices -> vertices -> Type
| bridge1 : edges north_shore west_island
...
```

#### [ Hoang Le Truong (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402877):
yes I agree

#### [ Mario Carneiro (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402888):
It's self documenting and clear and unambiguous

#### [ Kevin Buzzard (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402894):
and then you could formalise what it means for a graph to be connected

#### [ Kevin Buzzard (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402901):
(for all vertices v1 and v2 there's a path from v1 to v2)

#### [ Kevin Buzzard (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402905):
and then you could prove it in this case just by a case by case check

#### [ Kevin Buzzard (Jul 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402954):
But for a big graph, it is not so clear that Lean is the tool for this.

#### [ Mario Carneiro (Jul 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402959):
This gets complicated for large graphs, but you will want to switch to a different encoding anyway in that case

#### [ Kevin Buzzard (Jul 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402961):
You might want to read about what algorithms are used to prove a graph is connected, and implement one of those, but probably you would not get good performance in comparison with a tool like python

#### [ Mario Carneiro (Jul 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402973):
For fabs this is not a big problem

#### [ Mario Carneiro (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403034):
If you were, say, trying to work with the graphs in the four color theorem this kind of encoding is far too dense

#### [ Hoang Le Truong (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403037):
Yes I begin graph in general. after I restrict example

#### [ Kevin Buzzard (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403038):
Mario I'm surprised you haven't implemented graphs in mathlib. It's just the sort of thing a computer scientist would like to do, I would have thought.

#### [ Mario Carneiro (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403046):
The problem (which I have had also in metamath) is that "graph" means something different every time it is used

#### [ Mario Carneiro (Jul 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403056):
and the different theories are hard to fit in the same framework

#### [ Mario Carneiro (Jul 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403064):
even though everyone pretends it is easy

#### [ Kevin Buzzard (Jul 10 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403220):
I wondered if this was why. You need directed and undirected graphs, graphs where you're allowed/not allowed to have an edge from v to v, graphs where you are/are not allowed to have more than one edge from v to w, and that's before we've even started worrying about whether all graphs are finite etc

#### [ Hoang Le Truong (Jul 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403293):
Of course, I go this way.

#### [ Hoang Le Truong (Jul 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403348):
Now I work only the above graph ```G```

#### [ Kevin Buzzard (Jul 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403361):
So maybe one way of proceeding is that you decide exactly what is a graph for you, and then make your own type, and then make a term of that type corresponding to Koenigsberg, and make a general definition for connected, and then prove that Koenigsberg is connected.

#### [ Mario Carneiro (Jul 10 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403368):
And those "not allowed" things are not just constraints, they *change the encoding completely*, i.e. if there are no multiple edges you can have a relation instead of a set of edges with dom/cod; if it is undirected then maybe you want a function on *un*ordered pairs, if you have hyperedges then maybe each edge maps to a set of vertices which may or may not have size 2, ...

#### [ Mario Carneiro (Jul 10 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403394):
I agree that this is what Hoang should do, and it's what I did for Koenigsberg in Metamath

#### [ Kevin Buzzard (Jul 10 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403442):
I can now envisage a 2500-line graph.lean which carefully does every single possibility ;-)

#### [ Mario Carneiro (Jul 10 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403446):
just define things that make sense for undirected multigraphs

#### [ Mario Carneiro (Jul 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403483):
and forget about all the other crazy stuff until the next project

#### [ Hoang Le Truong (Jul 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403495):
I begin graph directed multiple degree have loop graph

#### [ Hoang Le Truong (Jul 10 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403637):
After I restrict to undirected multiphaps
Now I only work on a above ```G```. I have two way to define ```G```. I want to known what is good.

#### [ Johan Commelin (Jul 10 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405050):
Hoang, that was a bit of an XY problem: https://mywiki.wooledge.org/XyProblem

#### [ Johan Commelin (Jul 10 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405067):
I suggest you start a new topic titled "Defining graphs in Lean"

#### [ Johan Commelin (Jul 10 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405121):
It would have helped a lot if you had mentioned the word "graph" in the first few posts. Instead of just "function with properties"

#### [ Hoang Le Truong (Jul 10 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405223):
How to change "function on certain domain " to ``` Defining graphs in Lean```

#### [ Hoang Le Truong (Jul 10 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405242):
Ok I changed it

#### [ Kevin Buzzard (Jul 10 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405450):
```quote
 I have two way to define ```G```. I want to known what is good.
```
I am a mathematician, and I find myself asking this question often in Lean. I think it is a very difficult and delicate question, and sometimes the computer scientist experts here answer things like "it depends on why you want this structure". My advice to you is to go ahead and formalise it in one way, and then post your actual working code and ask for comments.

#### [ Hoang Le Truong (Jul 10 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405782):
I have two ways to define ```G```. one is
```
inductive vertices 
| a | b | c | d

def g (e:vertices× vertices ): ℕ :=
match  e  with
|(vertices.a,vertices.b) :=2
|(vertices.b,vertices.a) :=2
|(vertices.a,vertices.c) :=2
|(vertices.c,vertices.a) :=2
|(vertices.b,vertices.d) :=1
|(vertices.d,vertices.b) :=1
|(vertices.c,vertices.d) :=1
|(vertices.d,vertices.c) :=1
|_ :=0
end
```
and another is
```
def G (e:ℕ × ℕ  ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
```
what is way in Lean good

#### [ Johan Commelin (Jul 10 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405788):
No, that is not the definition of a graph

#### [ Johan Commelin (Jul 10 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405791):
It is only 1 very specific example.

#### [ Johan Commelin (Jul 10 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405799):
First you should decide if you want a general definition, or only the Koenigsberg example.

#### [ Hoang Le Truong (Jul 10 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405872):
I want a general definition and after apply to example

#### [ Johan Commelin (Jul 10 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129407364):
So then, give a general definition, and not an example.

#### [ Johan Commelin (Jul 10 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129407410):
Can you first give a definition without using Lean? Just write down an informal definition here.

#### [ Hoang Le Truong (Jul 10 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408167):
```An Euler walk in an undirected graph is a walk that uses each edge exactly once.```

#### [ Hoang Le Truong (Jul 10 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408413):
this is a general definition. I formed it in Lean. Now I want to apply it to exactly example to check the definition Euler walk is correct or wrong in lean.

#### [ Johan Commelin (Jul 10 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408432):
How did you put that statement into Lean?

#### [ Hoang Le Truong (Jul 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408443):
yes

#### [ Johan Commelin (Jul 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408449):
Please show it to us.

#### [ Johan Commelin (Jul 10 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408514):
We can not help you with defining your Koenigsberg example if we don't know how you put "undirected graph" in Lean.

#### [ Hoang Le Truong (Jul 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408661):
```definition undirected_graph ( graph:α × α → ℕ  ): Prop := 
       ∀ u v:α, graph(u,v)=graph(v,u)
```

#### [ Hoang Le Truong (Jul 10 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408679):
```
definition undirected_graph ( graph:α × α → ℕ  ): Prop := 
       ∀ u v:α, graph(u,v)=graph(v,u)
```

#### [ Johan Commelin (Jul 10 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408771):
Right, so for your example, you need the following ingredients: a type `alpha`, a function `alpha \times alpha \to nat` and a proof that your graph is undirected.

#### [ Johan Commelin (Jul 10 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408782):
There is no reason at all to take a subset of nat for alpha.

#### [ Johan Commelin (Jul 10 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408796):
You could define an inductive type for the four vertices.

#### [ Johan Commelin (Jul 10 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408856):
And it will allow you to define your function encoding the graph with matching.

#### [ Johan Commelin (Jul 10 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408944):
Like Mario wrote above: `inductive vertices | north_shore | west_island | ... `

#### [ Hoang Le Truong (Jul 10 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409001):
Thank you for that. I understood

#### [ Johan Commelin (Jul 10 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409007):
So, that is the same thing as your first method, except Mario's suggestion is more readable

#### [ Johan Commelin (Jul 10 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409014):
(For people who have walked through Koenigsberg...; or those who looked at the map on Wikipedia...)

#### [ Johan Commelin (Jul 10 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409133):
Ok, so, afterwards you have to prove that the thing is undirected, and then you have to show us the formalisation of "Euler walk"


{% endraw %}
