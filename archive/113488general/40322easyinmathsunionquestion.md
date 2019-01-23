---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40322easyinmathsunionquestion.html
---

## Stream: [general](index.html)
### Topic: [easy-in-maths union question](40322easyinmathsunionquestion.html)

---

#### [Kevin Buzzard (Apr 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196178):
```lean
import data.set 
universe u
example {X Y : Type u} (U : set X) (f : X → set Y) :
(⋃ (uu : {x // x ∈ U}), f uu.val) = ⋃₀(f '' U) := sorry
```

"Two ways of writing a union are the same".

#### [Kevin Buzzard (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196225):
This is a joy to prove in tactic mode using `set.subset.antisymm`

#### [Kenny Lau (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196229):
is "joy" sarcasm?

#### [Kevin Buzzard (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196232):
```lean
begin
  apply set.subset.antisymm,
  { intros y Hy,
    cases Hy with V HV,
    cases HV with HV HyV,
    cases HV with uu HuV,
    change V = f (uu.val) at HuV,
    existsi V,
    existsi _,
    exact HyV,
    existsi uu.val,
    exact ⟨uu.property,eq.symm HuV⟩
  },
  { intros y Hy,
    cases Hy with V HV,
    cases HV with HV HyV,
    cases HV with u HuV,
    existsi V,
    existsi _,
    exact HyV,
    existsi (⟨u,HuV.1⟩ : {x // x ∈ U}),
    exact eq.symm HuV.2
  }
```

#### [Kevin Buzzard (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196238):
no, not at all

#### [Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196248):
I feel like goals like this are ones that I know I can crush

#### [Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196250):
so it's a bit like grinding in the early Zeldas

#### [Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196251):
you know you can do it and it's quite fun to do

#### [Kevin Buzzard (Apr 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196252):
But for something of this form which is trivially true in maths

#### [Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196291):
my understanding is that one should seek a short "obfuscated" proof

#### [Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196301):
i.e. pull a couple of things out the library and you're done

#### [Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196302):
so I looked through `data.set.lattice`

#### [Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196303):
and I found

#### [Kevin Buzzard (Apr 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196308):
```lean
open set
#check @sUnion_image
#check @Union_eq_sUnion_image
#check @sUnion_eq_Union
#check @set.sUnion_eq_Union'
```

#### [Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196317):
all of which said "a union equals a union"

#### [Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196318):
but I just can't put them all together

#### [Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196322):
So I am wondering if this is a hole in the library or if I'm missing a trick

#### [Kevin Buzzard (Apr 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196324):
I don't know this file very well

#### [Kenny Lau (Apr 17 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196365):
```lean
example {X Y : Type u} (U : set X) (f : X → set Y) :
(⋃ (uu : {x // x ∈ U}), f uu.val) = ⋃₀(f '' U) :=
set.ext $ λ z, ⟨λ ⟨x1, ⟨⟨x2, H1⟩, H2⟩, H3⟩, ⟨x1, ⟨x2, H1, H2.symm⟩, H3⟩,
λ ⟨x1, ⟨x2, H1, H2⟩, H3⟩, ⟨x1, ⟨⟨x2, H1⟩, H2.symm⟩, H3⟩⟩

#### [Kevin Buzzard (Apr 17 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196369):
I need to be quick because my daughter just woke up (she is sick and off school)

#### [Kevin Buzzard (Apr 17 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196376):
but while I'm here let me mention the independent question that I was talking about `existsi _` yesterday or so and Mario advised me not to use it, saying it was better to go back and fill it in later.

#### [Kevin Buzzard (Apr 17 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196384):
However in my proof above, I used it because the thing that exists is another existsi

#### [Kevin Buzzard (Apr 17 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196391):
Aah excellent -- that looks much more like the 2-line obfuscated proof which this result deserves.

#### [Kevin Buzzard (Apr 17 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196437):
Should it be in the library?

#### [Kevin Buzzard (Apr 17 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196438):
Thanks Kenny.

#### [Kenny Lau (Apr 17 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196441):
```lean
example {X Y : Type u} (U : set X) (f : X → set Y) :
(⋃ (uu : {x // x ∈ U}), f uu.val) = ⋃₀(f '' U) :=
by finish [set.set_eq_def]
```

#### [Johannes Hölzl (Apr 17 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196452):
the simplifier also works: `by simp [set.set_eq_def]`

#### [Kenny Lau (Apr 17 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196454):
now we just switched camps :P

#### [Kevin Buzzard (Apr 17 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196507):
Aah! I tried to use simp a lot too, but my simp-fu is weak.

#### [Kevin Buzzard (Apr 17 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196511):
Thanks Johannes. How long did it take you to find that?

#### [Kevin Buzzard (Apr 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196522):
You see, the long tactic mode proof took me a very short time to write, because at each stage I just did the only thing which could be done.

#### [Kevin Buzzard (Apr 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196528):
I suspect that Kenny had a similar experience with the term proof.

#### [Kevin Buzzard (Apr 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196543):
But when I tried to find a short proof using library functions, all that happened was that I spent a long time looking through the library and noting down possibly useful functions

#### [Kevin Buzzard (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196584):
and then a long time failing to glue them together.

#### [Kevin Buzzard (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196587):
I want to get to the stage where if it's easy in maths, I can just nail it in Lean

#### [Kenny Lau (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196593):
```
example {X Y : Type u} (U : set X) (f : X → set Y) :
(⋃ (uu : {x // x ∈ U}), f uu.val) = ⋃₀(f '' U) :=
set.ext $ by simp

#### [Kevin Buzzard (Apr 17 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196596):
right

#### [Kevin Buzzard (Apr 17 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196604):
But this stinks because surely my strategy is basically the same

#### [Kevin Buzzard (Apr 17 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196607):
except I split the iff into two distinct implications

#### [Kevin Buzzard (Apr 17 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196609):
and then somehow simp failed to deal with either of them

#### [Kenny Lau (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196658):
`simp` simplifies iff's and equalities, lol

#### [Kevin Buzzard (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196659):
As I said, my simp-fu is weak

#### [Kevin Buzzard (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196664):
so that's the trick -- don't break the symmetry.

#### [Kevin Buzzard (Apr 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196665):
Thanks -- that was very instructive!

#### [Kenny Lau (Apr 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196674):
```lean
example {X Y : Type u} (U : set X) (f : X → set Y) :
(⋃ (uu : {x // x ∈ U}), f uu.val) = ⋃₀(f '' U) :=
set.ext $ λ z, ⟨λ hz, by simpa using hz, λ hz, by simpa using hz⟩
```

#### [Kenny Lau (Apr 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125196676):
splitting into two implications ^

#### [Kevin Buzzard (Apr 17 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125204693):
so to prove `X -> Y` using simp, you intro h and then `simpa using h`?

#### [Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125204786):
right

#### [Kevin Buzzard (Apr 17 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy-in-maths%20union%20question/near/125205075):
This trick is sufficiently important that it should be mentioned in the simp docs.

