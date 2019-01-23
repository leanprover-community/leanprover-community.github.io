---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06640sowhatiseqrec.html
---

## Stream: [general](index.html)
### Topic: [so what is eq.rec?](06640sowhatiseqrec.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134272):
I'm stuck in this state:
```
A : orbits G X,
x : X,
hx : ⟦x⟧ = A,
z : ↥(stab G X ↑⟨x, hx⟩)
⊢ ((eq.rec ⟨⟨x, rfl ⟦x⟧⟩, z⟩ hx).fst).val = x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134273):
I don't see any way to destruct `eq.rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134275):
`⟨⟨x, rfl ⟦x⟧⟩, z⟩` is subtype inside sigma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134314):
`pp.all`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134321):
You should probably `subst A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134322):
```
@eq.{v+1} X
    (@subtype.val.{v+1} X
       (λ (x : X),
          @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
            (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
            A)
       (@sigma.fst.{v u}
          (@subtype.{v+1} X
             (λ (x : X),
                @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                  (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                  A))
          (λ
           (a :
             @subtype.{v+1} X
               (λ (x : X),
                  @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                    (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                    A)),
             @subtype.{u+1} G
               (λ (x : G),
                  @has_mem.mem.{u u} G (set.{u} G) (@set.has_mem.{u} G) x
                    (@group_action.stab.{u v} G _inst_1 X _inst_2
                       (@coe.{(max 1 (v+1)) v+1}
                          (@subtype.{v+1} X
                             (λ (x : X),
                                @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                  (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                                  A))
                          X
                          (@coe_to_lift.{(max 1 (v+1)) v+1}
                             (@subtype.{v+1} X
                                (λ (x : X),
                                   @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                     (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                                     A))
                             X
                             (@coe_base.{(max 1 (v+1)) v+1}
                                (@subtype.{v+1} X
                                   (λ (x : X),
                                      @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                        (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                                        A))
                                X
                                (@coe_subtype.{v+1} X
                                   (λ (x : X),
                                      @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                        (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                                        A))))
                          a))))
          (@eq.rec.{(max v u)+1 v+1} (@group_action.orbits.{u v} G _inst_1 X _inst_2)
             (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
             (λ (_x : @group_action.orbits.{u v} G _inst_1 X _inst_2),
                @sigma.{v u}
                  (@subtype.{v+1} X
                     (λ (x : X),
                        @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                          (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                          _x))
                  (λ
                   (x :
                     @subtype.{v+1} X
                       (λ (x : X),
                          @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                            (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                            _x)),
                     @subtype.{u+1} G
                       (λ (x_1 : G),
                          @has_mem.mem.{u u} G (set.{u} G) (@set.has_mem.{u} G) x_1
                            (@group_action.stab.{u v} G _inst_1 X _inst_2
                               (@coe.{(max 1 (v+1)) v+1}
                                  (@subtype.{v+1} X
                                     (λ (x : X),
                                        @eq.{v+1}
                                          (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                          (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)
                                          _x))
                                  X
                                  (@coe_to_lift.{(max 1 (v+1)) v+1}
                                     (@subtype.{v+1} X
                                        (λ (x : X),
                                           @eq.{v+1}
                                             (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                             (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                                x)
                                             _x))
                                     X
                                     (@coe_base.{(max 1 (v+1)) v+1}
                                        (@subtype.{v+1} X
                                           (λ (x : X),
                                              @eq.{v+1}
                                                (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                                (@quotient.mk.{v+1} X
                                                   (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                                   x)
                                                _x))
                                        X
                                        (@coe_subtype.{v+1} X
                                           (λ (x : X),
                                              @eq.{v+1}
                                                (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                                (@quotient.mk.{v+1} X
                                                   (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                                   x)
                                                _x))))
                                  x)))))
             (@sigma.mk.{v u}
                (@subtype.{v+1} X
                   (λ (x_1 : X),
                      @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                        (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x_1)
                        (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)))
                (λ
                 (x_1 :
                   @subtype.{v+1} X
                     (λ (x_1 : X),
                        @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                          (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x_1)
                          (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x))),
                   @subtype.{u+1} G
                     (λ (x_2 : G),
                        @has_mem.mem.{u u} G (set.{u} G) (@set.has_mem.{u} G) x_2
                          (@group_action.stab.{u v} G _inst_1 X _inst_2
                             (@coe.{(max 1 (v+1)) v+1}
                                (@subtype.{v+1} X
                                   (λ (x_1 : X),
                                      @eq.{v+1} (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                        (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x_1)
                                        (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2) x)))
                                X
                                (@coe_to_lift.{(max 1 (v+1)) v+1}
                                   (@subtype.{v+1} X
                                      (λ (x_1 : X),
                                         @eq.{v+1}
                                           (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                           (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                              x_1)
                                           (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                              x)))
                                   X
                                   (@coe_base.{(max 1 (v+1)) v+1}
                                      (@subtype.{v+1} X
                                         (λ (x_1 : X),
                                            @eq.{v+1}
                                              (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                              (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                                 x_1)
                                              (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                                 x)))
                                      X
                                      (@coe_subtype.{v+1} X
                                         (λ (x_1 : X),
                                            @eq.{v+1}
                                              (@quotient.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2))
                                              (@quotient.mk.{v+1} X (@group_action.orbit_rel.{u v} G _inst_1 X _inst_2)
                                                 x_1)
                                              (@quotien

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134323):
lol too long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134365):
oh, lol, `subst` did the job

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134366):
how does it work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134368):
You have an equality assumption `[[x]] = A`, and a bunch of complicated stuff that depends on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134372):
to reduce an `eq.rec` you need the major premise to become `refl` somehow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134375):
that usually means finding the appropriate equality in the context and generalizing it until one side is a variable, and then `subst`, which is to say use `eq.rec` in the proof term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134465):
```
eq.rec ⟨⟨x, rfl ⟦x⟧⟩, z⟩ hx = ⟨⟨x, hx⟩, z⟩

is cleared by:

(eq.drec
   (λ (z : ↥(stab G X ↑⟨snd_fst_val, eq.refl ⟦snd_fst_val⟧⟩)),
      eq.refl
        (eq.rec_on (eq.refl ⟦snd_fst_val⟧)
           (((λ (z : Σ (x : X), ↥(stab G X x)),
             ⟨⟦z.fst⟧, ⟨⟨z.fst, rfl ⟦z.fst⟧⟩, z.snd⟩⟩)
            ((λ
              (z :
                Σ (A : orbits G X) (x : ↥{x : X | ⟦x⟧ = A}), ↥(stab G X ↑x)),
                ⟨((z.snd).fst).val, (z.snd).snd⟩)
               ⟨⟦snd_fst_val⟧, ⟨⟨snd_fst_val, eq.refl ⟦snd_fst_val⟧⟩, z⟩⟩)).snd)))
   snd_fst_property
   snd_snd)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134466):
I `print`ed to look at the proof term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134505):
so maybe `drec` would have worked?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/so%20what%20is%20eq.rec%3F/near/125134506):
I guess it uses `eq.drec` since you also need to replace `hx` in the term with `eq.refl`, but it's not necessary provided you generalize `hx` by proof irrelevance


{% endraw %}
