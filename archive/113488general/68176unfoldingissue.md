---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68176unfoldingissue.html
---

## Stream: [general](index.html)
### Topic: [unfolding issue](68176unfoldingissue.html)

---


{% raw %}
#### [ Kevin Buzzard (May 22 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947033):
<p><code>(presheaf_of_types_pullback_under_open_immersion {F := F, res := res, Hid := Hid, Hcomp := Hcomp} id _).res</code></p>

#### [ Kevin Buzzard (May 22 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947036):
<p>Why can't I unfold that?</p>

#### [ Kevin Buzzard (May 22 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947054):
<p><code>lam X, presheaf_of_types_pullback_under_open_immersion X f H</code> is a function from a structure to itself</p>

#### [ Kevin Buzzard (May 22 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947111):
<p>I explicitly write down the definition, I say what F and res and Hid and Hcomp are</p>

#### [ Kevin Buzzard (May 22 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947116):
<p>I don't see any reason why Lean can't evaluate that res</p>

#### [ Kevin Buzzard (May 22 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947121):
<p>My goal is <code>[mess above] == res</code></p>

#### [ Kevin Buzzard (May 22 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947128):
<p>and this should just unravel to be, hopefully, something trivial.</p>

#### [ Kevin Buzzard (May 22 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947148):
<p>This is another one of those insane "trivial in maths, hard in Lean" things</p>

#### [ Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947234):
<p>I am trying to prove that if you pull back a sheaf by the identity function, you get the same sheaf</p>

#### [ Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947235):
<p>this statement is fraught with difficulties though</p>

#### [ Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947236):
<p>and this is definitely not refl</p>

#### [ Kevin Buzzard (May 22 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126947238):
<p>because I am claiming for example that F U = F (id '' U)</p>

#### [ Chris Hughes (May 23 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126948909):
<p>What's the definition of <code>presheaf_of_types_pullback_under_open_immersion</code>? I think the functions like <code>.res</code> only unfold when applied to something of the form <code>{F := _, ...}.res</code> and not  <code>x.res</code> for example. Have you tried <code>show</code>?</p>

#### [ Chris Hughes (May 23 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126948980):
<p>Is it because it doesn't know what the underscore is?</p>

#### [ Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949066):
<p>The underscore is a horrible proof term.</p>

#### [ Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949069):
<p>I have realised there's another approach</p>

#### [ Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949071):
<p>so this question is no longer relevant</p>

#### [ Kevin Buzzard (May 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949077):
<p>Again I have to use something very counterintuitive to a mathematician</p>

#### [ Kevin Buzzard (May 23 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949115):
<p>Instead of trying to claim that the identity map is a map <code>F U -&gt; F (id '' U)</code></p>

#### [ Kevin Buzzard (May 23 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949141):
<p>I use the actual map <code>F U -&gt; F (id '' U)</code> which a mathematician would call "the identity map" but which in dependent type theory is known as "restriction from U to the open subset id '' U"</p>

#### [ Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949220):
<p>it's unbelievable</p>

#### [ Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949230):
<p>all my hitherto impossible goals magically become refl</p>

#### [ Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949245):
<div class="codehilite"><pre><span></span>⊢ {morphism := λ (U : set (X R)) (HU : is_open zariski.open U),
                   ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id &#39;&#39; U) HU
                     (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id &#39;&#39; U))) (set.image_id U))) HU)
                     (eq.mpr (id (eq.rec (eq.refl (id &#39;&#39; U ⊆ U)) (set.image_id U))) (set.subset.refl U)),
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
                           ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id &#39;&#39; U) HU
                             (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id &#39;&#39; U))) (set.image_id U))) HU)
                             (eq.mpr (id (eq.rec (eq.refl (id &#39;&#39; U ⊆ U)) (set.image_id U))) (set.subset.refl U)))
                          HU)}.morphism
      U
      HU
      (x * y) =
    {morphism := λ (U : set (X R)) (HU : is_open zariski.open U),
                     ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id &#39;&#39; U) HU
                       (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id &#39;&#39; U))) (set.image_id U))) HU)
                       (eq.mpr (id (eq.rec (eq.refl (id &#39;&#39; U ⊆ U)) (set.image_id U))) (set.subset.refl U)),
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
                             ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id &#39;&#39; U) HU
                               (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id &#39;&#39; U))) (set.image_id U))) HU)
                               (eq.mpr (id (eq.rec (eq.refl (id &#39;&#39; U ⊆ U)) (set.image_id U))) (set.subset.refl U)))
                            HU)}.morphism
        U
        HU
        x *
      {morphism := λ (U : set (X R)) (HU : is_open zariski.open U),
                     ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id &#39;&#39; U) HU
                       (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id &#39;&#39; U))) (set.image_id U))) HU)
                       (eq.mpr (id (eq.rec (eq.refl (id &#39;&#39; U ⊆ U)) (set.image_id U))) (set.subset.refl U)),
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
                             ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types).res U (id &#39;&#39; U) HU
                               (eq.mpr (id (eq.rec (eq.refl (is_open zariski.open (id &#39;&#39; U))) (set.image_id U))) HU)
                               (eq.mpr (id (eq.rec (eq.refl (id &#39;&#39; U ⊆ U)) (set.image_id U))) (set.subset.refl U)))
                            HU)}.morphism
        U
        HU
        y
</pre></div>

#### [ Kevin Buzzard (May 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126949246):
<p>proof is refl</p>

#### [ Andrew Ashworth (May 23 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20issue/near/126955573):
<p>it seems you discover cool new things daily! perhaps you can include a mathematician's tips and tricks section in the textbook you want to write this summer</p>


{% endraw %}
