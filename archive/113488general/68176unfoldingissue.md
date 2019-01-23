---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68176unfoldingissue.html
---

## Stream: [general](index.html)
### Topic: [unfolding issue](68176unfoldingissue.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947033):
`(presheaf_of_types_pullback_under_open_immersion {F := F, res := res, Hid := Hid, Hcomp := Hcomp} id _).res`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947036):
Why can't I unfold that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947054):
`lam X, presheaf_of_types_pullback_under_open_immersion X f H` is a function from a structure to itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947111):
I explicitly write down the definition, I say what F and res and Hid and Hcomp are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947116):
I don't see any reason why Lean can't evaluate that res

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947121):
My goal is `[mess above] == res`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947128):
and this should just unravel to be, hopefully, something trivial.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947148):
This is another one of those insane "trivial in maths, hard in Lean" things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947234):
I am trying to prove that if you pull back a sheaf by the identity function, you get the same sheaf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947235):
this statement is fraught with difficulties though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947236):
and this is definitely not refl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947238):
because I am claiming for example that F U = F (id '' U)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126948909):
What's the definition of `presheaf_of_types_pullback_under_open_immersion`? I think the functions like `.res` only unfold when applied to something of the form `{F := _, ...}.res` and not  `x.res` for example. Have you tried `show`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 23 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126948980):
Is it because it doesn't know what the underscore is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949066):
The underscore is a horrible proof term.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949069):
I have realised there's another approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949071):
so this question is no longer relevant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949077):
Again I have to use something very counterintuitive to a mathematician

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949115):
Instead of trying to claim that the identity map is a map `F U -> F (id '' U)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949141):
I use the actual map `F U -> F (id '' U)` which a mathematician would call "the identity map" but which in dependent type theory is known as "restriction from U to the open subset id '' U"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949220):
it's unbelievable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949230):
all my hitherto impossible goals magically become refl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949245):
```
⊢ {morphism := λ (U : set (X R)) (HU : is_open zariski.open U),
                   ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id '' U) HU
                     (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id '' U))) (set.image_id U))) HU)
                     (eq.mpr (id (eq.rec (eq.refl (id '' U ⊆ U)) (set.image_id U))) (set.subset.refl U)),
     commutes := λ (U V : set (X R)) (HU : is_open zariski.open U) (HV : is_open zariski.open V) (Hsub : V ⊆ U),
                   eq.refl
                     (((presheaf_of_rings_pullback_under_open_immersion (zariski.structure_presheaf_of_rings R) id
                            H).to_presheaf_of_types).res
                          U
                          V
                          HU
                          HV
                          Hsub ∘
                        (λ (HU : is_open zariski.open U),
                           ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id '' U) HU
                             (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id '' U))) (set.image_id U))) HU)
                             (eq.mpr (id (eq.rec (eq.refl (id '' U ⊆ U)) (set.image_id U))) (set.subset.refl U)))
                          HU)}.morphism
      U
      HU
      (x * y) =
    {morphism := λ (U : set (X R)) (HU : is_open zariski.open U),
                     ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id '' U) HU
                       (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id '' U))) (set.image_id U))) HU)
                       (eq.mpr (id (eq.rec (eq.refl (id '' U ⊆ U)) (set.image_id U))) (set.subset.refl U)),
       commutes := λ (U V : set (X R)) (HU : is_open zariski.open U) (HV : is_open zariski.open V) (Hsub : V ⊆ U),
                     eq.refl
                       (((presheaf_of_rings_pullback_under_open_immersion (zariski.structure_presheaf_of_rings R) id
                              H).to_presheaf_of_types).res
                            U
                            V
                            HU
                            HV
                            Hsub ∘
                          (λ (HU : is_open zariski.open U),
                             ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id '' U) HU
                               (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id '' U))) (set.image_id U))) HU)
                               (eq.mpr (id (eq.rec (eq.refl (id '' U ⊆ U)) (set.image_id U))) (set.subset.refl U)))
                            HU)}.morphism
        U
        HU
        x *
      {morphism := λ (U : set (X R)) (HU : is_open zariski.open U),
                     ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id '' U) HU
                       (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id '' U))) (set.image_id U))) HU)
                       (eq.mpr (id (eq.rec (eq.refl (id '' U ⊆ U)) (set.image_id U))) (set.subset.refl U)),
       commutes := λ (U V : set (X R)) (HU : is_open zariski.open U) (HV : is_open zariski.open V) (Hsub : V ⊆ U),
                     eq.refl
                       (((presheaf_of_rings_pullback_under_open_immersion (zariski.structure_presheaf_of_rings R) id
                              H).to_presheaf_of_types).res
                            U
                            V
                            HU
                            HV
                            Hsub ∘
                          (λ (HU : is_open zariski.open U),
                             ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id '' U) HU
                               (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id '' U))) (set.image_id U))) HU)
                               (eq.mpr (id (eq.rec (eq.refl (id '' U ⊆ U)) (set.image_id U))) (set.subset.refl U)))
                            HU)}.morphism
        U
        HU
        y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949246):
proof is refl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 23 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126955573):
it seems you discover cool new things daily! perhaps you can include a mathematician's tips and tricks section in the textbook you want to write this summer


{% endraw %}
