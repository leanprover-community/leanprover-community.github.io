---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52419typemismatcherror.html
---

## Stream: [general](index.html)
### Topic: [type mismatch error](52419typemismatcherror.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375133):
I don't have a good strategy for debugging errors like this:
```lean
type mismatch at application
  galois_connection.l_supr opens.gc
term
  opens.gc
has type
  galois_connection subtype.val opens.interior
but is expected to have type
  galois_connection ?m_5 ?m_6
```
My initial reaction is: Hey Lean, look, you just figured out what `?m_5` and `?m_6` are. Unify, and move on.
But apparently Lean thinks otherwise...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375216):
I would `set_option pp.all true`, but that's me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375240):
I'll try, but I fear that I get something extremely long and complicated.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375263):
I'm not afraid of that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 09 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375316):
This pattern shows up a lot when there's a type class argument to `galois_connection.l_supr` that `opens.gc` doesn't satisfy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375361):
Hmmm, it's even reasonable short:
```
type mismatch at application
  @galois_connection.l_supr.{?l_1 ?l_2 ?l_3} ?m_4 ?m_5 ?m_6 ?m_7 ?m_8 ?m_9 ?m_10
    (@topological_space.opens.gc.{?l_11} ?m_12 ?m_13)
term
  @topological_space.opens.gc.{?l_1} ?m_2 ?m_3
has type
  @galois_connection.{?l_1 ?l_1}
    (@subtype.{(max (?l_1+1) 1)} (set.{?l_1} ?m_2) (λ (s : set.{?l_1} ?m_2), @is_open.{?l_1} ?m_2 ?m_3 s))
    (set.{?l_1} ?m_2)
    (@subtype.preorder.{?l_1} (set.{?l_1} ?m_2)
       (@partial_order.to_preorder.{?l_1} (set.{?l_1} ?m_2)
          (@lattice.order_bot.to_partial_order.{?l_1} (set.{?l_1} ?m_2)
             (@lattice.bounded_lattice.to_order_bot.{?l_1} (set.{?l_1} ?m_2)
                (@lattice.complete_lattice.to_bounded_lattice.{?l_1} (set.{?l_1} ?m_2)
                   (@set.lattice_set.{?l_1} ?m_2)))))
       (λ (s : set.{?l_1} ?m_2), @is_open.{?l_1} ?m_2 ?m_3 s))
    (@partial_order.to_preorder.{?l_1} (set.{?l_1} ?m_2)
       (@lattice.order_bot.to_partial_order.{?l_1} (set.{?l_1} ?m_2)
          (@lattice.bounded_lattice.to_order_bot.{?l_1} (set.{?l_1} ?m_2)
             (@lattice.complete_lattice.to_bounded_lattice.{?l_1} (set.{?l_1} ?m_2) (@set.lattice_set.{?l_1} ?m_2)))))
    (@subtype.val.{(max (?l_1+1) 1)} (set.{?l_1} ?m_2) (λ (s : set.{?l_1} ?m_2), @is_open.{?l_1} ?m_2 ?m_3 s))
    (@topological_space.opens.interior.{?l_1} ?m_2 ?m_3)
but is expected to have type
  @galois_connection.{?l_1 ?l_2} ?m_3 ?m_4
    (@partial_order.to_preorder.{?l_1} ?m_3
       (@lattice.order_bot.to_partial_order.{?l_1} ?m_3
          (@lattice.bounded_lattice.to_order_bot.{?l_1} ?m_3
             (@lattice.complete_lattice.to_bounded_lattice.{?l_1} ?m_3 ?m_5))))
    (@partial_order.to_preorder.{?l_2} ?m_4
       (@lattice.order_bot.to_partial_order.{?l_2} ?m_4
          (@lattice.bounded_lattice.to_order_bot.{?l_2} ?m_4
             (@lattice.complete_lattice.to_bounded_lattice.{?l_2} ?m_4 ?m_6))))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375378):
@**Rob Lewis** That's probably what's going on here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375392):
when I can't handle it, I use https://text-compare.com

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375456):
and in some rare cases it's some universe issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375481):
Otoh, I think all typeclass instances ought to be satisfied.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375700):
@**Kenny Lau** There are two `sorry`s in `sheaf.lean`. They are math-trivial, but I find them Lean-hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375716):
link?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375725):
If you have some time, I would be really happy if you could take a look.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375762):
https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L262

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375817):
I think you have a rather different definition of "math-trivial"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375819):
What this is saying is, you've got an open set `V` and a cover `Us` of an open set `U`. And `V ⊆ U`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375831):
Now you intersect all the `Ui` in `Us` with `V`, and the result covers `V`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375838):
can you show me the context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375850):
You mean explain the context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375853):
no, the context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375866):
Aaah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375878):
```lean
X : Type u,
_inst_1 : topological_space X,
U V : opens X,
i : V ⟶ U,
Us : covering_family U,
Us_cover : U = ⨆ (u : over U) (H : u ∈ Us), u.left
⊢ V.val ≤ (⨆ (Ui : over U) (H : Ui ∈ Us), ((over.comap i).obj Ui).left).val
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375942):
So I want to show that `V ⊆ ⨆ Ui, (V ∩ Ui)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375950):
That is the math version of the goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375958):
where is V on the right hand side?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375972):
`V : opens X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375980):
Aah, it is hidden in `comap i`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375990):
Which in this setting just means: `V ∩ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376084):
Now I would think that `opens.gc` should let me transform the right hand side from
`(⨆ (Ui : over U) (H : Ui ∈ Us), ((over.comap i).obj Ui).left).val` into
`⨆ (Ui : over U) (H : Ui ∈ Us), (((over.comap i).obj Ui).left).val`.
(I moved a parentheses to before `over.comap`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376244):
do you know what it is definitionally equivalent to?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376250):
if not can you just unfold everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376252):
If this goal could be transformed into `V.val ∩ Ui.left.val ≤ (over.comap i) blah).val` for all `Ui`, then I could take it from there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376399):
if you `intro x`, then `i x` says that `x \in U` right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376408):
then you rewrite `Us_cover`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376455):
Ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376463):
so now it says `x \in set.bUnion _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376471):
~~Make that an `x`~~

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376502):
then `set.mem_bUnion_iff` or something should give you something useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376505):
Now I want to extract a `Ui` that contains `x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376520):
Aah, let me try to find that one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376595):
Except that it is a `supr` instead of a `bUnion`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376607):
aren't they defeq?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376616):
There should be a `lattice.mem_supr_iff`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376618):
Aah, probably yes. I'll try.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376619):
you can't be the member of just any supremum

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376886):
Yay! First use of `erw` in my Lean-life. Context is now
```lean
X : Type u,
_inst_1 : topological_space X,
U V : opens X,
i : V ⟶ U,
Us : covering_family U,
Us_cover : U = ⨆ (u : over U) (H : u ∈ Us), u.left,
x : X,
hx : x ∈ V.val,
this :
  ∃ (x_1 : order_dual (opens X)),
    x_1 ∈ {a : opens X | ∃ (i : over U), a = (λ (u : over U), ⨆ (H : u ∈ Us), u.left) i} ∧ x ∈ x_1.val
⊢ x ∈ (⨆ (Ui : over U) (H : Ui ∈ Us), ((over.comap i).obj Ui).left).val
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376921):
That looks encouraging, right? Especially that `order_dual` that is leaking through.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 09 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147377202):
Ok, need to go. But now I think I can complete this. Thanks a lot!

