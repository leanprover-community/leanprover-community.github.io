---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00887tacticlookaround.html
---

## Stream: [general](index.html)
### Topic: [tactic look around](00887tacticlookaround.html)

---

#### [Patrick Massot (Mar 06 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123344266):
Assume I write
```lean
class foo :=
(bar : nat)

instance : foo :=
{ bar := by magic }
```

#### [Patrick Massot (Mar 06 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123344320):
Can I write a tactic `magic` which knows that the instance I'm trying to create has type `foo` and the current field I'm working on is called `bar`?

#### [Patrick Massot (Mar 06 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123344599):
The motivation for this question is https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean (look at all lines containing `funext`)

#### [Scott Morrison (Mar 06 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123350559):
I'm also interested in this question! As far as I understand, this isn't possible, but it seems quite desirable for tactics to be able to know the "reason" they have been invoked.

#### [Simon Hudon (Mar 06 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123362941):
The closest I can find is `decl_name` which tells you the name of the declaration being elaborated. I haven't tried but I'm not sure `resolve_name` would work on it to then get the type

#### [Simon Hudon (Mar 06 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123363136):
What you could try is 

```
instance : foo :=
begin magic ... end
```

Where magic acts a bit like `refine` and use `structure_fields` to apply `funext ; ...` for every fields for which it works and leaves the other ones untouched.

#### [Scott Morrison (Mar 07 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123375425):
@**Simon Hudon**, `decl_name` works fine, but feeding that into `resolve_name` just gets an error message `identifier not found`. Oh well!

#### [Simon Hudon (Mar 07 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123375435):
I'm not too surprised. I'm looking at that file right now and I think `target` is more promising.

#### [Simon Hudon (Mar 07 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123375437):
I think the tactic will look like:

```
instance monoid [∀ i, monoid $ f i] : monoid (Π i : I, f i) :=
by lifted_instance [indexed_product.has_one,indexed_product.semigroup]
```

#### [Simon Hudon (Mar 07 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123376745):
Here's what I ended up with: https://github.com/PatrickMassot/lean-differential-topology/pull/1

#### [Simon Hudon (Mar 07 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20look%20around/near/123376765):
The Lean developers added `pexpr.mk_structure_instance` after I complained about it but I never got around to using it. I think it's a very nice feature.

