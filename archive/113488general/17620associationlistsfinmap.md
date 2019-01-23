---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17620associationlistsfinmap.html
---

## Stream: [general](index.html)
### Topic: [association lists, finmap](17620associationlistsfinmap.html)

---


{% raw %}
#### [ Sean Leather (Sep 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134290992):
As some people know, I've been working on association lists and finite maps for mathlib (https://github.com/spl/lean-finmap). Mario has decided he wants to get it into mathlib soon, so he has started rewriting it in his own fashion (https://github.com/leanprover-community/mathlib/tree/finmap). I wanted to open up the discussion to get feedback from anyone else who might be interested.

#### [ Sean Leather (Sep 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291300):
One question is whether there is  the need for a `structure` to wrap a list without duplicate keys. Mario thinks it might be useful:

```lean
structure alist (α : Type u) (β : α → Type v) : Type (max u v) :=
(val : list (sigma β))
(nd : val.knodup)
```

https://github.com/leanprover-community/mathlib/blob/e5ddd1d4dca984f6d7a77a87a1608b414296208f/data/list/alist.lean

I went down this path and found that, given that (a) there are so many useful definitions and theorems regarding lists and (b) the `structure` is such a thin wrapper, every definition or proof for the `structure` is simple, it created a large number of really simple statements. Considering that `alist` is really a list with a property and I believe it is useful to use other list definitions that don't involve this property, I think the `alist` structure either (a) makes it more difficult to work with the wrapped list or (b) creates the problem of scaling the number of statements about `alist` to match those already about `list`.

#### [ Sean Leather (Sep 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291437):
In another way of putting it, you could look at an `alist` as something unique on its own or you could look at a list  with a property that it has no duplicate keys. In the process of developing my library, I found the latter view much more useful.

#### [ Simon Hudon (Sep 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291494):
Why is latter more useful?

#### [ Sean Leather (Sep 20 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291573):
On a related note, that's also how I ended up with the `finmap` `structure`:

```lean
structure finmap (α : Type u) (β : α → Type v) : Type (max u v) :=
(val : multiset (sigma β))
(nodupkeys : val.nodupkeys)
```

https://github.com/spl/lean-finmap/blob/035f1faa218e47b9f411c4a243900955f4714a56/src/data/finmap.lean#L8-L10

You could say that this is a similar situation: a `finmap` is just a `multiset` with no duplicate keys. However, I found that it's more useful to look at it as a `finmap` because I didn't find a lot of the other `multiset` definitions to be very useful for a `finmap`.

#### [ Sean Leather (Sep 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291591):
```quote
Why is latter more useful?
```

The most important reason for me is that I care about the structure of the internal list: `nil`, `cons`, `append`, etc.

#### [ Sean Leather (Sep 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291598):
Also, regarding `finmap`, I don't care about the structure of the internal `multiset`.

#### [ Sean Leather (Sep 20 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291662):
... which makes sense, since a `multiset` is a `quotient`.

#### [ Sean Leather (Sep 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291736):
@**Simon Hudon** Thanks for that question, BTW. It gets to a key reason I don't think `alist` is useful, a reason that hadn't yet come to mind.

#### [ Sean Leather (Sep 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291871):
That is, I found that it was useful to wrap a `quotient` like `multiset` in a `structure` but not that useful to wrap a `list` in a `structure` because the structure of the list is important when working with the `structure`. I ended up creating definitions to wrap `nil`, `cons`, `append`, etc., and all of that already existed for the `list`, so I came to ask why it was necessary. I couldn't come up with a good answer.

#### [ Simon Hudon (Sep 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292027):
```quote
You could say that this is a similar situation: a finmap is just a multiset with no duplicate keys. However, I found that it's more useful to look at it as a finmap because I didn't find a lot of the other multiset definitions to be very useful for a finmap.
```

I don't get this nuance

#### [ Sean Leather (Sep 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292185):
```quote
I don't get this nuance
```

I think it's similar to how you don't see a lot of the `multiset` definitions used for `finset`. There's a particular subset (mostly starting with `nd`) that are used in `finset`, but many of them are not.

#### [ Sean Leather (Sep 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292261):
`multiset` seems to be useful as a substrate for `finset` and `finmap`, but it also has a larger API that is oriented towards counting duplicates.

#### [ Sean Leather (Sep 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292305):
Also, the subset of the `multiset` API used for `finset` is not useful for `finmap`.

#### [ Mario Carneiro (Sep 20 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308497):
I think the comparison is apt, and applicable to `alist`. A finset is just a multiset with a property, but the API is different (some basic operations are not applicable, like `cons`, and others are slightly weird and become more useful on the subtype, like `ndinsert`).

#### [ Mario Carneiro (Sep 20 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308618):
In the case of `alist`, there are some operations that don't work anymore, like `cons`, and others are slightly weird and have been prefixed with `k` for lists. `cons` is just not a valid `alist` operation, `insert` is.

#### [ Sean Leather (Sep 20 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308803):
```quote
I think the comparison is apt, and applicable to `alist`.
```

So does this mean you agree with me, since my comparison is apt, which is to say that `alist` is not a useful structure?

#### [ Sean Leather (Sep 20 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308937):
```quote
In the case of `alist`, there are some operations that don't work anymore, like `cons`, and others are slightly weird and have been prefixed with `k` for lists. `cons` is just not a valid `alist` operation, `insert` is.
```
This hints of disagreement. My point is that lists are constructed with `nil` and `cons`, and it is useful to have that construction, and therefore more useful to have a bare list with no duplicate keys than to have a structure hide that construction.

#### [ Mario Carneiro (Sep 20 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309076):
In short: I think `finset` is useful, and I think `alist` is useful

#### [ Mario Carneiro (Sep 20 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309171):
I don't see why `alist` should provide a nil/cons construction. It's not natural. If you want to do such a construction then you should unpack the `alist` first

#### [ Sean Leather (Sep 20 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309182):
That's kind of my point. :wink:

#### [ Mario Carneiro (Sep 20 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309185):
Instead it has `empty`/`insert`

#### [ Mario Carneiro (Sep 20 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309213):
My point is, why are you doing list things on `alist`s?

#### [ Sean Leather (Sep 20 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309308):
My point is that I want to construct lists with no duplicate keys as well as use any other existing definitions and theorems on lists.

#### [ Mario Carneiro (Sep 20 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309416):
then do so, on `list`. You don't need `alist` for that

#### [ Sean Leather (Sep 20 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309434):
Quite right, which is why I don't think `alist` is necessary.

#### [ Mario Carneiro (Sep 20 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309458):
`alist` provides a compositional structure for safety-preserving functions on lists

#### [ Mario Carneiro (Sep 20 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309526):
> as well as use any other existing definitions and theorems on lists.

Most list operations don't preserve the invariant. What do you do with these?

#### [ Sean Leather (Sep 20 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309548):
Well, if you want it, add it. I'm only trying to save you work.

#### [ Mario Carneiro (Sep 20 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309589):
This is an honest question. What is missing from the API of `alist` that you would want, that requires resorting to `list`?

#### [ Mario Carneiro (Sep 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309684):
Except for `union`, there's nothing I've missed that comes to mind

#### [ Sean Leather (Sep 20 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309698):
I'm not sure about `alist`, but I defined the minimum necessary to use `list`s with no duplicate keys. For example, `has_mem` and `append` don't need to be redefined. You only need some extra properties to use `append`, for example.

#### [ Mario Carneiro (Sep 20 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309747):
To answer your question from earlier, `alist` should also be available as a tool for programmers. "I need a map, I only have equality" -> use `alist` or `finmap`

#### [ Mario Carneiro (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309771):
Note that the `has_mem` on `alist` is different from the one on lists

#### [ Mario Carneiro (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309775):
and `append` doesn't apply

#### [ Sean Leather (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309778):
Which I don't think it should be.

#### [ Sean Leather (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309781):
As you'll see in my library.

#### [ Mario Carneiro (Sep 20 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309850):
I think in common programming parlance, `x \in m` where m is a dictionary / map / associative array, means `x` is a key contained in the map `m`, not `x` is a key-value pair in the map

#### [ Mario Carneiro (Sep 20 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309915):
The idiom for the other interpretation is `<x, y> \in m.val`, where `val` is the operation sometimes called `entries` in other libraries

#### [ Mario Carneiro (Sep 20 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309930):
(indeed, maybe it should be renamed to that)

#### [ Mario Carneiro (Sep 20 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310185):
Note also that if it meant membership in the underlying list, then it wouldn't be decidable unless you assume decidability of the values, which is not needed for anything else

#### [ Sean Leather (Sep 20 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310257):
Fair enough. With `a : alist`, you can use `a.val`/`a.entries`.

#### [ Mario Carneiro (Sep 20 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310292):
right, I think this helps to view them as different things (a finite map vs a list of pairs)

#### [ Mario Carneiro (Sep 20 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310375):
You pointed out that it is possible to define operations like `append` if you assume side conditions (i.e. the key sets are disjoint). Does this come up often?

#### [ Sean Leather (Sep 20 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310406):
I don't know about “often,” but it has come up.

#### [ Sean Leather (Sep 20 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310494):
I'm now using `finmap` instead of association lists directly, and you have the same thing with union there.

#### [ Sean Leather (Sep 20 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310514):
I'm assuming you'll use `has_union` for `alist` instead of `has_append`?

#### [ Mario Carneiro (Sep 20 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310519):
yes

#### [ Mario Carneiro (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310530):
since it's union, not append :P

#### [ Mario Carneiro (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310581):
it's not even possible to give an `append` instance that uses `list.append`

#### [ Sean Leather (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310582):
Well, it's debatable that it's not a form of append.

#### [ Mario Carneiro (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310612):
I prefer set terminology when duplicates are being dropped

#### [ Sean Leather (Sep 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310633):
It's still appending. :slight_smile:

#### [ Sean Leather (Sep 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310663):
When it comes to the `finmap`, you can forget that there is any appending. But with `alist`, you can't.

#### [ Mario Carneiro (Sep 20 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310727):
Not sure what you mean. The underlying operation is not an append

#### [ Mario Carneiro (Sep 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310750):
It is true that `union` would be order-respecting on `alist`

#### [ Mario Carneiro (Sep 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310760):
but then again, so is `union` on `list`

#### [ Sean Leather (Sep 20 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310795):
```lean
def append : list α → list α → list α
| []       l := l
| (h :: s) t := h :: (append s t)

def kunion : list (sigma β) → list (sigma β) → list (sigma β)
| []         l := l
| (hd :: tl) l := hd :: kunion tl (kerase hd.1 l)
```

#### [ Sean Leather (Sep 20 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310838):
Are you doing it differently?

#### [ Mario Carneiro (Sep 20 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310876):
I think the `erase` makes that a rather different kind of operation. But also I think we need two functions here - that is `unionl`

#### [ Mario Carneiro (Sep 20 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310955):
`unionr` would be
```
def kunionr : list (sigma β) → list (sigma β) → list (sigma β)
| []         l := l
| (hd :: tl) l := kinsert hd.1 hd.2 (kunionr tl l)
```

#### [ Mario Carneiro (Sep 20 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310975):
I'm not even sure if it should get a `has_union` notation

#### [ Sean Leather (Sep 20 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311002):
I'm not sure if you need it. I don't foresee people asking for it.

#### [ Mario Carneiro (Sep 20 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311082):
You need left and right preference. For `finmap` you can ignore it since the order of parameters gives the preference, but on `alist` you have order and preference separately

#### [ Sean Leather (Sep 20 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311233):
Why do you need it? Just because it's possible doesn't make it a need.

#### [ Mario Carneiro (Sep 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311266):
I'm okay with just assuming right preference (which is what `list.union` does), but you want left preference?

#### [ Sean Leather (Sep 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311344):
I stuck with the Haskell `Data.Map` approach because it seemed to the most intuitive to me.

#### [ Mario Carneiro (Sep 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311402):
Keep in mind that haskell has laziness to contend with, making your definition more natural for them

#### [ Sean Leather (Sep 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311408):
Yep.

#### [ Sean Leather (Sep 20 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311479):
`∪` is `infixl`, so could that also indicate left-biased is preferred?

#### [ Mario Carneiro (Sep 20 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311485):
It seems like the difference between `foldl` and `foldr`

#### [ Mario Carneiro (Sep 20 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311497):
and we have both of those

#### [ Mario Carneiro (Sep 20 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311510):
I'd rather not commit to one camp here

#### [ Mario Carneiro (Sep 20 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311595):
particularly since there are also performance characteristics to worry about, and the lean 4 compiler may change this as well

#### [ Sean Leather (Sep 20 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311611):
You have to commit to one for `∪` at the very least.

#### [ Sean Leather (Sep 20 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311653):
I guess if you're going with the `list.union` precedent, you would go with the right-biased option.

#### [ Mario Carneiro (Sep 20 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311734):
I think `alist` shouldn't have a notation, `finmap` can use left preference by default since the API properties take precedence there

#### [ Mario Carneiro (Sep 20 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311763):
I should look at other languages like java or python and see what preference is preferred

#### [ Sean Leather (Sep 20 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311849):
I would consider Haskell, ML, OCaml, Coq, Agda, Idris, etc. before looking at Java or Python.

#### [ Mario Carneiro (Sep 20 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311856):
hm, python has a mutation operation which makes the precedence obvious

#### [ Mario Carneiro (Sep 20 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311991):
Same with java. OCaml takes a merge function that resolves differences

#### [ Mario Carneiro (Sep 20 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134312238):
Haskell has both union (left bias) and unionWith that takes a merge function

#### [ Mario Carneiro (Sep 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134312504):
I couldn't find anything for Coq. Idris uses merge left bias and mergeWith

#### [ Mario Carneiro (Sep 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134312515):
ML is roll your own dict

#### [ Sean Leather (Sep 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134367053):
I'm coming to realize that what would be better for me than a `finmap` union that updates by `insert` or `erase` is something like an internal disjoint union. At least that's what I've gathered it would be called. [[1](https://math.stackexchange.com/a/1631405), [2](https://ncatlab.org/nlab/show/disjoint+union#internal_version)] For `finmap`, perhaps the simplest definition would be:

```lean
def djunion (f g : finmap α β) : finmap α β := if disjoint f.keys g.keys then f ∪ g else ∅
```

But a more efficient version would probably use `list.append` instead of `list.kunion` as `∪` does.

I'm only dealing with unions of disjoint `finmap`s, and it would simplify some things if I didn't have to track all of the `disjoint f.keys g.keys`.

#### [ Sean Leather (Sep 21 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134368101):
Likewise, a disjoint insert would be good. Conceptually:

```lean
def djinsert (a : α) (b : β a) (f : finmap α β) : finmap α β := if a ∉ f.keys then insert a b f else ∅
```

But `cons` would be better than `kinsert`.

#### [ Sean Leather (Oct 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406194):
@**Mario Carneiro** What is your plan with https://github.com/leanprover-community/mathlib/tree/finmap ? I'd like to see something get into mathlib. However, given the somewhat large difference between your rewrite and [my library](https://github.com/spl/lean-finmap), I'm a bit reluctant at this point to invest the time to port more definitions and theorems over to that branch without knowing what's going to happen to it. Do you plan to continue working on that branch?

#### [ Mario Carneiro (Oct 08 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406729):
would you like me to merge it?

#### [ Sean Leather (Oct 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406861):
```quote
would you like me to merge it?
```
“It” being the `leanprover-community/mathlib` branch? Sure, if you're happy with it in its current state. I would feel more comfortable extending it at that point.

#### [ Mario Carneiro (Oct 08 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406969):
I noticed you renamed some things. Not a fan of `knodup`?

#### [ Sean Leather (Oct 08 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407006):
```quote
I noticed you renamed some things. Not a fan of `knodup`?
```
:slight_smile: No. I think `nodupkeys` is better.

#### [ Mario Carneiro (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407143):
when I look at it I think "nine letters is long for a name segment"

#### [ Mario Carneiro (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407208):
You could have `nodup_keys` but then it confuses with `nodup` of `keys`

#### [ Mario Carneiro (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407221):
what about `nodup_fst`?

#### [ Sean Leather (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407228):
```quote
You could have `nodup_keys` but then it confuses with `nodup` of `keys`
```
Exactly.

#### [ Sean Leather (Oct 08 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407279):
```quote
what about `nodup_fst`?
```
How is that better than `nodupkeys` since `nodup` and `keys` already exist?

#### [ Sean Leather (Oct 08 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407304):
... exist in the association list/finmap API that is.

#### [ Mario Carneiro (Oct 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407323):
I mean for the list version, before the "map" interpretation

#### [ Sean Leather (Oct 08 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407650):
I'd prefer `nodupkeys` for both for consistency's sake. I think the name is clear in that it links `nodup` and `keys` and as short as it's needed to be.

#### [ Sean Leather (Oct 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407709):
Anyway, I have to go now. If you want to discuss any other issues, I'll pick it up tomorrow.


{% endraw %}
