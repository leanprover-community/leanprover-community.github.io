---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22908forcingstructuralrecursion.html
---

## Stream: [general](index.html)
### Topic: [forcing structural recursion](22908forcingstructuralrecursion.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064431):
I have a mutually inductive type of tree (which is not a type family) and I'm trying to define a recursive function on it but the termination checker seems to default to well founded recursion while it should be clear that structural recursion works. Is there a way to nudge Lean in the right direction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064513):
In case that helps, here's my type definition and my function:

```lean 
mutual inductive proxy_v, proxy_leaf_v (var : Type (max u v+1)) (α : Type u)
with proxy_v : Type (max u v+1)
  | ret {} : α → proxy_v
  | action {} : ∀ β, m β → (β → proxy_leaf_v) → proxy_v
  | yield {}  : y' → (y → proxy_leaf_v)  → proxy_v
  | await {} :  x  → (x' → proxy_leaf_v) → proxy_v
  | think {} : proxy_leaf_v → proxy_v
with proxy_leaf_v : Type (max u v+1)
  | hole {} : var → proxy_leaf_v
  | more {} : proxy_v → proxy_leaf_v

@[reducible]
def proxy  : Type (max u v+1) :=
proxy_v (proxy_intl α) α

@[reducible]
def proxy_leaf  : Type (max u v+1) :=
proxy_leaf_v (proxy_intl α) α
```

```lean 
mutual def to_intl_aux, to_intl
with to_intl_aux : proxy_leaf x x' y y' m α → proxy_intl x x' y y' m α
 | (hole x) := x
 | (more x) := to_intl x
with to_intl : proxy x x' y y' m α → proxy_intl x x' y y' m α
 | (ret i) := cofix.mk (proxy_node.ret i) empty.rec'
 | (action β cmd f) := cofix.mk (proxy_node.action cmd) (λ i, to_intl_aux (f i))
 | (yield o f) := cofix.mk (proxy_node.yield o) (λ i, to_intl_aux (f i))
 | (await o f) := cofix.mk (proxy_node.await o) (λ i, to_intl_aux (f i))
 | (think cmd) := cofix.mk (proxy_node.think) (λ _, to_intl_aux cmd)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 28 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064798):
The equations compiler does not support mutual structural recursion https://github.com/leanprover/lean/blob/8a93d2770e5e4c349d761ded334f8fb7119e7082/src/library/equations_compiler/compiler.cpp#L52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064927):
Arrg! *tears hair out*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064943):
I have a feeling that recursion based on `sizeof` will be difficult because of that components of type `something -> proxy_v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064944):
Any advice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065002):
I don't think I've really used mutual recursion so far

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065237):
Ok here's my next attempt: I'm inlining the function `to_intl_aux` 

```lean
def to_intl : proxy x x' y y' m α → proxy_intl x x' y y' m α
 | (ret i) := cofix.mk (proxy_node.ret i) empty.rec'
 | (action β cmd f) := cofix.mk (proxy_node.action cmd) (λ i,
   match (f i) with
    | (hole x) := x
    | (more x) := to_intl x
   end )
 | (yield o f) := cofix.mk (proxy_node.yield o) (λ i,
   match (f i) with
    | (hole x) := x
    | (more x) := to_intl x
   end )
 | (await o f) := cofix.mk (proxy_node.await o) (λ i,
   match (f i) with
    | (hole x) := x
    | (more x) := to_intl x
   end )
 | (think cmd) := cofix.mk (proxy_node.think) (λ _,
   match cmd with
    | (hole x) := x
    | (more x) := to_intl x
   end )
```

Again, it's falling back on well founded recursion and trying to prove that, in many cases `sizeof x < 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065334):
Is there any theoretical limitation that prevents the use of structural recursion in mutually recursive functions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065741):
Good news everyone! I made it work by hardcoding the details of the mutually inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123066278):
Is there any plan to make `io` universe polymorphic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123083059):
```quote
Is there any theoretical limitation that prevents the use of structural recursion in mutually recursive functions?
```
I don't think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123083113):
```quote
Is there any plan to make `io` universe polymorphic?
```
No plans, but I don't see why not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 01 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123152522):
With regards to structural recursion, would it be any better if instead of having a `proxy_leaf_v` branch, I would just use `⊕`? Would that block my structural recursion then too?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 01 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123157356):
Ah, that should probably work...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 01 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123157415):
Maybe that's better than coding my own mutually inductive type then. I'll give it a try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 25 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125670451):
@**Simon Hudon** Did you ever make progress on this issue? Should mutual inductives in Lean 3 simply be avoided?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125670898):
I ended up encoding my mutually inductive type by hand using an inductive family. I think that was the only way to do it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125671041):
It's been a few months since I touched that project but I'm wondering if the situation would improved if `has_well_founded` had two type parameter. When you're using polymorphic recursion, i.e. your function `foo` has type `foo : Π {α : Type*}, my_type α` and that your recursive call is on `my_type β`, I wonder if that would make well founded recursion work nonetheless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 25 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125672470):
Good to know, thanks. I'm not sure I understand your `has_well_founded` idea. Do you not have a (monomorphic) measure on your type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125672886):
Yes, the one based on `has_sizeof` should do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125673041):
What I mean is that `has_well_founded.r x y` might be the appropriate proof obligation in situations where `x : my_type α` and `y : my_type β` but that's not well typed. That where the only solution is structural recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 25 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125676961):
I think the current equation compiler may actually be... acceptable... if we had tactics that could deal with these usually very simple inequations. We don't currently, do we? :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125685933):
Are you suggesting that it could be fixed using a `using_well_founded` clause?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 26 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125695965):
Yes. The first issue is that the default wf tactic pair uses the sum of the measures of all arguments, which makes the inequations harder, or possibly even contradictory. So the first step may be a `rel_tac` tactic that uses the measure of only a single argument (probably the first one that is discriminated), which should generate inequations of the form `x < ... + x + ... + 1`. It should not be too hard to write a `dec_tac` to solve those. With that we should get a wf tactic pair that proves all mutual structural recursions over a single argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125696149):
Nice! Do you think there might be a way to integrate it to the default well founded recursion tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 26 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125696389):
Well, I hope that in the next version of Lean there will simply be native support for mutual structural recursion

