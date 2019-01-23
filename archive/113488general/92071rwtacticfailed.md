---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92071rwtacticfailed.html
---

## Stream: [general](index.html)
### Topic: [rw tactic failed](92071rwtacticfailed.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840698):
```
rewrite tactic failed, did not find instance of the pattern in the target expression
  @has_add.add.{?l_1} ?m_2
    (@add_semigroup.to_has_add.{?l_1} ?m_2
       (@add_monoid.to_add_semigroup.{?l_1} ?m_2 (@add_group.to_add_monoid.{?l_1} ?m_2 ?m_3)))
    (@has_smul.smul.{0 ?l_1} int ?m_2 (@add_group.has_smul.{?l_1} ?m_2 ?m_3) ?m_4 ?m_5)
    (@has_smul.smul.{0 ?l_1} int ?m_2 (@add_group.has_smul.{?l_1} ?m_2 ?m_3) ?m_6 ?m_5)


⊢ [..]
          (@has_add.add.{u₁} α₁
             (@add_semigroup.to_has_add.{u₁} α₁
                (@add_monoid.to_add_semigroup.{u₁} α₁
                   (@add_comm_monoid.to_add_monoid.{u₁} α₁
                      (@add_comm_group.to_add_comm_monoid.{u₁} α₁
                         (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)))))
             (@has_smul.smul.{0 u₁} int α₁
                (@add_group.has_smul.{u₁} α₁
                   (@add_comm_group.to_add_group.{u₁} α₁
                      (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)))
                n
                (f (@prod.fst.{v w} β γ (@prod.mk.{v w} β γ x y₁))
                   (@prod.snd.{v w} β γ (@prod.mk.{v w} β γ x y₁))))
             (@has_smul.smul.{0 u₁} int α₁
                (@add_group.has_smul.{u₁} α₁
                   (@add_comm_group.to_add_group.{u₁} α₁
                      (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)))
                n
                (f (@prod.fst.{v w} β γ (@prod.mk.{v w} β γ x y₂))
                   (@prod.snd.{v w} β γ (@prod.mk.{v w} β γ x y₂)))))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840702):
Lean, it's right there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840706):
I know you want ` (@add_group.to_add_monoid.{?l_1} ?m_2 ?m_3) `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840714):
but isn't ` (@add_comm_monoid.to_add_monoid.{u₁} α₁
                      (@add_comm_group.to_add_comm_monoid.{u₁} α₁
                         (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)) ` good enough for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840765):
they don't look the same to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840772):
they're both justifying why I have addition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840785):
specifically here they're justifying why I have an add_monoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840789):
can you do some BS "change" or "show" beforehand?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840855):
Is this one of these dreaded diamond things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840877):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840945):
I think the main concern is the one in the `gsmul` thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840947):
overloading is not good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840956):
This is Mario's doing, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840967):
So probably he will have some sensible solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840979):
well but that bullet wasn't in the global namespace before Lean updated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840988):
oh so it's Leo's doing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840991):
I would say so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840993):
So probably Mario will have some clever workaround.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841050):
I blame myself for all this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841057):
you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841059):
I should never have mentioned that `^` had the wrong associativity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841066):
what happened

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841075):
I got annoyed that `2^3^2` was 64 not 512

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841079):
so I opened an issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841091):
and all of a sudden there were lots of changes to `^`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841100):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841109):
https://github.com/leanprover/lean/issues/1951

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841168):
led to https://github.com/leanprover/lean/commit/d387103aa2bebfc98220733d9607a16663ec1ef2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841186):
and then to https://github.com/leanprover/lean/commit/8f55ec4c50379c612731ced2424fd3eda0cf69a6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841195):
and hmm I don't see the bullet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841205):
maybe it's not my fault after all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841287):
nice to see presheaves being pulled into core lean though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841289):
https://github.com/leanprover/lean/commit/6e0bf8473b1980e6692a61a924b4c6eae195619d

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841295):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841296):
what a subversion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841420):
Talking of presheaves, thanks for trying to fix that tensor product file. Presumably that's where this issue arose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124849118):
I removed the `has_smul` typeclass from `group_power`, which should fix the notation overloading problem. This puts us back at square one `local infix` type solutions for using `gsmul`, but it shouldn't interfere with the module smul notation now. I'm not sure about registering every abelian group as a Z-module with an instance, since module still uses an `out_param` for the scalar ring which might get stuck on `int`

