---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74575Forwarddeclarations.html
---

## Stream: [general](index.html)
### Topic: [Forward declarations](74575Forwarddeclarations.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227150):
Is it possible to forward declare definitions in lean? I'd like to write something like
````
structure some_data -- forward declare structure because lean can't look ahead

def mutator_fn := some_data → some_data 

structure some_data :=
  (the_data : list nat)
  (data_mutator : mutator_fn)

def some_data.mutate (my_data : some_data) : some_data := my_data.data_mutator my_data
````
and that way `my_data.mutate` would be able mutate itself, for example.

If you can't I'm pretty sad. :( Has it ever been asked for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227260):
I'm not exactly sure what you're after yet, but "mutual defs" may be what you want, and I think are as close as you're going to get.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227578):
I'm now all about mutual definitions!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227588):
This sounds like an obvious source of unsoundness, so it's definitely by design that this isn't doable. I think you should explain in more detail what you are trying to do - there is likely a standard "functional" approach to your problem that does not require forward declaration.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227747):
Rather than forward declaration, the structure can just refer to itself. Since this makes it recursive you have to define it with `inductive`:
```
meta inductive some_data
| mk (the_data : list nat)
     (data_mutator : some_data → some_data) : some_data
```
This has to be `meta`, though, because it *is* unsound

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227775):
Sure, this was just for programming in lean just like another functional language (i.e. with reckless abandon). Often functions invoke each other, for example. I was willing to sell my soul to the `meta`s :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227827):
here is the mutator:
```
meta def some_data.mutate : some_data → some_data
| ⟨d, m⟩ := m ⟨d, m⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227844):
cheers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227848):
what does `meta` mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227901):
Roughly that you are doing *raw* Lean. Without proof checking. So all tactics are written in `meta` land.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227918):
But Mario can give you a definition that is a lot better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227919):
It turns off the safety

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227946):
you can do unbounded recursion and non-positive inductives and other unsound things, as well as being able to call meta constants that have a definition in C++

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227961):
Actually, how might I solve a related problem, like declaring (toy example):
````
meta structure vertex :=
( color : string )
( adj_list : list edge )

meta structure edge :=
( start end : vertex )
( weight : nat )
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227962):
mutual inductive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228003):
(thanks again for the practically instant help)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228007):
beat me!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228035):
```
meta mutual inductive vertex, edge
with vertex : Type
| mk (color : string) (adj_list : list edge) : vertex
with edge : Type
| mk (start end_ : vertex) (weight : nat) : edge
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228039):
`end` is a keyword

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228161):
Note that these are dangerous even in pure programming lean, because the pointer structure has cycles and lean is reference counted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229142):
(In principle) there are countermeasures against rc cycles though, right? Are you saying that lean isn't able to find them at the moment?---if so, appreciate the heads up. thanks again :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229209):
Well, lean is pretty explicitly designed to make rc cycles impossible as a result of the type system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229223):
I don't know if it does something special for meta mutual inductives, but I doubt it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229297):
the goal is to have a strong enough type system that lean can assume powerful things about your code. Functional stuff like common subexpression evaluation is one simple example


{% endraw %}
