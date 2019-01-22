---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35960VariousVMquestions.html
---

## [general](index.html)
### [Various VM questions](35960VariousVMquestions.html)

#### [Neil Strickland (Dec 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/150999916):
I have been working on several different approaches to partitions of finite sets and other finite combinatorial structures.  I would like to do things in such a way that the VM can compute with examples that are moderately large.  For this I would like to understand better how the VM works and what it can do.  I have not managed to find any relevant documentation, but I have looked a little bit at the VM-related source code.
* Is there any documentation that I have not found?
* Is there a way to get Lean to print information about what the VM can do with a given definition?
* Any comments or corrections on the following?
 * It seems best to do serious computation with partitions of `fin n`, and then set things up so that one can deal with partitions of a general fintype by using an equivalence with `fin n`.
 * It looks like the VM will deal efficiently with `fin n` but not with `fin2 n`.  On the other hand, if you were willing to add stuff to the lean core, it looks like you could easily implement an efficient VM version of fin2.
 * It looks like it is probably efficient to work with the quotient of a simple type by a complicated equivalence relation,  because the complexity is all hidden in Props which are erased by the VM. 
 * It looks like the VM cannot handle `fin n -> X` efficiently, but should be happy with `list X` or `array n X`
 * The VM has support for `rb_map`.  It is not clear to me whether this only comes into play if you use `rb_map` explicitly, or whether it some how gets used for other kinds of structures.

#### [Bryan Gin-ge Chen (Dec 06 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/151021786):
This doesn't address any of your questions about the VM, but regarding partitions of finite sets, @**Mario Carneiro**  [suggested a more efficient recursive approach to enumeration](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/tutorial/near/135302235) than the one I took in the tutorial branch. Perhaps this is already something you've done though.

#### [Mario Carneiro (Dec 06 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/151022735):
1. There isn't too much documentation about the VM, although for basic use it's quite simple: just use `#eval` and the VM runs any lean function.
2. Lean can evaluate any definition that is not marked `noncomputable` (which is a really obvious and required marking on any definition).
3. ...
4. That's debatable. Working over arbitrary types also means working parametrically in the data representation, abstracting away the details like the reason why a type is finite. What representation is "best" depends on the application.
5. This is true. `fin2 n` will be a linked list of pointers, and `fin n` will be a number stored as a 32 bit integer if it is small enough. The recommended approach here is to put together VM primitive types to get the data representation you would like - a type describes its data representation, so if you want a different representation you need a different type.
6. This is true. A quotient is represented using the underlying type, with the relation appearing nowhere. It is a zero cost abstraction. However, depending on what you want to do with the relation this may not be a good thing. For example you can't easily enumerate the elements of a quotient type unless you know something about the relation. It is a tool in the box, but its usefulness depends on the application.
7. This is also application dependent. A `fin n -> X` is a function that takes a number and returns a value in `X`. A `list X` is a linked list of values of type `X`. An `array n X` is a literal array in memory whose elements have type `X`. They all have their own performance characteristics, and it isn't too hard to guess what they are, roughly.
8. The VM has support for several `meta` data structures beyond `rb_map`, such as `tactic_state`, `expr`, `environment` and so on. There is a non-meta version of `rb_map`, called `rbmap`, which has no special support. I think the sense is that it wasn't really necessary to implement `rb_map` as a C data structure when lean can do it well enough. Not counting `meta` data structures, the only types/functions with native support are `nat`, `int`, `array` and `quot` (maybe I'm forgetting something but I'm sure others will point it out).

#### [Scott Morrison (Dec 06 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/151041032):
... and perhaps in this context it's worth mentioning that everything will likely be different when Lean 4 arrives :four_leaf_clover: .

