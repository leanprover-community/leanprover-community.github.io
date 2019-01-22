---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68895Provingsomethingisasubfield.html
---

## [new members](index.html)
### [Proving something is a subfield](68895Provingsomethingisasubfield.html)

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154872747):
I'm trying to prove that the intersection of two subfields is a subfield -- the problem with using `subfield.mk`, or just using `{...}` directly, is that `subfield` is defined using `extends`, so I need to prove that it's a subring -- and by extension that it is an additive subgroup and a submonoid. What's the notation for this?

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154872763):
This is what I have:

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154872773):
```lean
import algebra.field 
import field_theory.subfield
theorem field_intersect (F1 F2 : set K) [h1 : is_subfield F1] [h2 : is_subfield F2] : is_subfield (F1 ∩ F2) :=
{   --do I need to put something here?
    inv_mem := (λ x ⟨hx1, hx2⟩, and.intro (is_subfield.inv_mem hx1) (is_subfield.inv_mem hx2))
}
```

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154874067):
Got it, it's `to_is_subring`.

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154876299):
Ok, I suppose one could do without that, too.

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154876309):
```lean
theorem field_intersect (F1 F2 : set K) [h1 : is_subfield F1] [h2 : is_subfield F2] : is_subfield (F1 ∩ F2) := {
    zero_mem := and.intro h1.zero_mem h2.zero_mem,
    one_mem := and.intro h1.one_mem h2.one_mem,
    add_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro 
        (by {have k := h1.add_mem, exact @k a b ha1 hb1}) 
        (by {have k := h2.add_mem, exact @k a b ha2 hb2}),
    mul_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro 
        (by {have k := h1.mul_mem, exact @k a b ha1 hb1})
        (by {have k := h2.mul_mem, exact @k a b ha2 hb2}),
    neg_mem := λ a ⟨ha1, ha2⟩, and.intro 
        (by {have k := h1.neg_mem, exact @k a ha1})
        (by {have k := h2.neg_mem, exact @k a ha2}), 
    inv_mem := (λ x ⟨hx1, hx2⟩, and.intro (is_subfield.inv_mem hx1) (is_subfield.inv_mem hx2))
}
```

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154876361):
I got confused because Lean doesn't point out which fields are to be provided when something extends something.

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154876596):
On a related note, why doesn't this work?
```lean
theorem field_intersect (F1 F2 : set K) [h1 : is_subfield F1] [h2 : is_subfield F2] : is_subfield (F1 ∩ F2) := {
    zero_mem := and.intro h1.zero_mem h2.zero_mem,
    one_mem := and.intro h1.one_mem h2.one_mem,
    add_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro (h1.add_mem ha1 hb1) (h2.add_mem ha2 hb2),
    mul_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro (h1.mul_mem ha1 hb1) (h2.mul_mem ha2 hb2),
    neg_mem := λ a ⟨ha1, ha2⟩, and.intro (h1.neg_mem ha1) (h2.neg_mem ha2),
    inv_mem := (λ x ⟨hx1, hx2⟩, and.intro (is_subfield.inv_mem hx1) (is_subfield.inv_mem hx2))
}
```
Or even this:
```lean
theorem field_intersect (F1 F2 : set K) [h1 : is_subfield F1] [h2 : is_subfield F2] : is_subfield (F1 ∩ F2) := {
    zero_mem := and.intro h1.zero_mem h2.zero_mem,
    one_mem := and.intro h1.one_mem h2.one_mem,
    add_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro (@h1.add_mem a b ha1 hb1) (@h2.add_mem a b ha2 hb2),
    mul_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro (@h1.mul_mem ha1 hb1) (@h2.mul_mem a b ha2 hb2),
    neg_mem := λ a ⟨ha1, ha2⟩, and.intro (@h1.neg_mem a ha1) (@h2.neg_mem a ha2),
    inv_mem := (λ x ⟨hx1, hx2⟩, and.intro (is_subfield.inv_mem hx1) (is_subfield.inv_mem hx2))
}
```
One has to do a `have` statement and then construct the statement with the local instance of `neg_mem`, etc. Why?

#### [Reid Barton (Jan 10 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154876635):
What exactly did you write the first time? with `to_is_subring`

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154876664):
Oh, I just nested them all in:
```lean
theorem field_intersect (F1 F2 : set K) [h1 : is_subfield F1] [h2 : is_subfield F2] : is_subfield (F1 ∩ F2) := {
    to_is_subring := {
        to_is_add_subgroup := {
            to_is_add_submonoid := {
                zero_mem := and.intro h1.zero_mem h2.zero_mem,
                add_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro 
                    (by {have k := h1.add_mem, exact @k a b ha1 hb1}) 
                    (by {have k := h2.add_mem, exact @k a b ha2 hb2}),
            },
            neg_mem := λ a ⟨ha1, ha2⟩, and.intro 
                (by {have k := h1.neg_mem, exact @k a ha1})
                (by {have k := h2.neg_mem, exact @k a ha2}), 
            },
        to_is_submonoid := {
            one_mem := and.intro h1.one_mem h2.one_mem,
            mul_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro 
                (by {have k := h1.mul_mem, exact @k a b ha1 hb1})
                (by {have k := h2.mul_mem, exact @k a b ha2 hb2}),
        },
    },
    inv_mem := (λ x ⟨hx1, hx2⟩, and.intro (is_subfield.inv_mem hx1) (is_subfield.inv_mem hx2))
}
```

#### [Mario Carneiro (Jan 10 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877108):
`@h1.neg_mem` doesn't work because you can't mix field notation and `@` notation

#### [Mario Carneiro (Jan 10 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877121):
you have to write `@neg_mem h1`

#### [Mario Carneiro (Jan 10 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877252):
also you shouldn't project out of a typeclass argument, because it's implicit

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877259):
Re:(@,.) -- I thought so, but I tried that and it doesn't work either -- it just doesn't find `is_subfield.neg_mem`

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877297):
```quote
also you shouldn't project out of a typeclass argument, because it's implicit
```
 What do you mean?

#### [Mario Carneiro (Jan 10 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877317):
what do you get when you try it?

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877398):
`unknown identifier 'is_subfield.add_mem'`

#### [Mario Carneiro (Jan 10 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877407):
that means it's not called that

#### [Mario Carneiro (Jan 10 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877424):
what is the def of `is_subfield`?

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877432):
I tried with `is_add_submonoid` too.

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877442):
```lean
type mismatch at application
  is_add_submonoid.add_mem
term
  h1
has type
  is_subfield F1 : Type
but is expected to have type
  Type ? : Type (?+1)
```

#### [Mario Carneiro (Jan 10 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877453):
you don't pass in `h1` at all

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877513):
I did.

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877517):
This is what I'm trying:
```lean
theorem field_intersect (F1 F2 : set K) [h1 : is_subfield F1] [h2 : is_subfield F2] : is_subfield (F1 ∩ F2) := {
    zero_mem := and.intro h1.zero_mem h2.zero_mem,
    one_mem := and.intro h1.one_mem h2.one_mem,
    add_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro ((@is_add_submonoid.add_mem h1) a b ha1 hb1) (@h2.add_mem a b ha2 hb2),
    mul_mem := λ a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩, and.intro (@h1.mul_mem ha1 hb1) (@h2.mul_mem a b ha2 hb2),
    neg_mem := λ a ⟨ha1, ha2⟩, and.intro (@h1.neg_mem a ha1) (@h2.neg_mem a ha2),
    inv_mem := (λ x ⟨hx1, hx2⟩, and.intro (is_subfield.inv_mem hx1) (is_subfield.inv_mem hx2))
}
```

#### [Mario Carneiro (Jan 10 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877518):
i know, stop

#### [Mario Carneiro (Jan 10 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877523):
just call it without passing in `h1`

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877543):
Ah.

#### [Mario Carneiro (Jan 10 2019 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877546):
like `is_add_submonoid.add_mem ha1 hb1`

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877642):
I see, yes this works.

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877652):
But why? What's wrong with trying to feed Lean the class?

#### [Mario Carneiro (Jan 10 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877684):
the class is implicit, you aren't supposed to give it, lean finds it by typeclass inference

#### [Mario Carneiro (Jan 10 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877696):
you can give it if you use `@`

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877758):
Yes, why wasn't that working?

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877771):
Using `@` and feeding the class?

#### [Mario Carneiro (Jan 10 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877782):
that should work, you just need a few more arguments that way, like the types

#### [Mario Carneiro (Jan 10 2019 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877802):
I guess it looks something like `@is_add_submonoid.add_mem F1 h1 a b ha1 hb1`

#### [Mario Carneiro (Jan 10 2019 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877891):
oh wait, no it should be something more complicated than just `h1` there

#### [Mario Carneiro (Jan 10 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154877921):
because `h1` is a `is_subfield` and it needs a `is_add_monoid`, it does some typeclass inference to fill the gap

#### [Abhimanyu Pallavi Sudhir (Jan 10 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/154878002):
Oh ok. I think I see why it's best to leave things to Lean's class inference.

#### [Abhimanyu Pallavi Sudhir (Jan 16 2019 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155280441):
I'm proving a similar theorem and having the same problem again, except this time just leaving Lean to do its type class inference doesn't work (only `zero_mem` and `one_mem` work):

```lean
variables {K L : Type} [discrete_field K] [discrete_field L] (f : K → L) 
theorem field_intersect' (PL : set (set L)) [H : ∀ J ∈ PL, is_subfield J] : is_subfield (set.sInter PL) :=
{   zero_mem := by { simp, exact λ J HJ, (H J HJ).zero_mem },
    one_mem := by { simp, exact λ J HJ, (H J HJ).one_mem },
    add_mem := by { simp, exact λ a b ha hb J HJ, is_add_submonoid.add_mem (ha J HJ) (hb J HJ) },
    mul_mem := by { simp, exact λ a b ha hb J HJ, is_submonoid.mul_mem (ha J HJ) (hb J HJ) },
    neg_mem := by { simp, exact λ a h J HJ, is_add_subgroup.neg_mem (h J HJ) },
    inv_mem := by { simp, exact λ a h J HJ, is_subfield.inv_mem (h J HJ) } }
```

It worked with `set.Inter`:

```lean
theorem field_intersect (Fi : ι → set K) [hi : ∀ i, is_subfield (Fi i)] : is_subfield (set.Inter Fi) := 
{   zero_mem := by { simp, exact λ i, (hi i).zero_mem },
    one_mem := by { simp, exact λ i, (hi i).one_mem },
    add_mem := by { simp, exact λ a b ha hb i, is_add_submonoid.add_mem (ha i) (hb i) },
    mul_mem := by { simp, exact λ a b ha hb i, is_submonoid.mul_mem (ha i) (hb i) },
    neg_mem := by { simp, exact λ a h i, is_add_subgroup.neg_mem (h i) },
    inv_mem := by { simp, exact λ a h i, is_subfield.inv_mem (h i) } }
```

#### [Kevin Buzzard (Jan 16 2019 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155281908):
Can you post working code so I can cut and paste?

#### [Kevin Buzzard (Jan 16 2019 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155281909):
PS this "simp, ..." style is discouraged. There are always ways around it.

#### [Abhimanyu Pallavi Sudhir (Jan 16 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155282381):
```lean
import algebra.field
import field_theory.subfield
import data.polynomial
variables {K L : Type} [discrete_field K] [discrete_field L] (f : K → L)
theorem field_intersect' (PL : set (set L)) [H : ∀ J ∈ PL, is_subfield J] : is_subfield (set.sInter PL) :=
{   zero_mem := by { simp, exact λ J HJ, (H J HJ).zero_mem },
    one_mem := by { simp, exact λ J HJ, (H J HJ).one_mem },
    add_mem := by { simp, exact λ a b ha hb J HJ, is_add_submonoid.add_mem (ha J HJ) (hb J HJ) },
    mul_mem := by { simp, exact λ a b ha hb J HJ, is_submonoid.mul_mem (ha J HJ) (hb J HJ) },
    neg_mem := by { simp, exact λ a h J HJ, is_add_subgroup.neg_mem (h J HJ) },
    inv_mem := by { simp, exact λ a h J HJ, is_subfield.inv_mem (h J HJ) } }
```

#### [Abhimanyu Pallavi Sudhir (Jan 16 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155282401):
Doesn't that work (for copy-pasting, I mean)?

#### [Kevin Buzzard (Jan 16 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155283329):
```lean
import field_theory.subfield

variables {K L : Type} [discrete_field K] [discrete_field L] (f : K → L)
theorem field_intersect' (PL : set (set L)) [H : ∀ J ∈ PL, is_subfield J] : is_subfield (set.sInter PL) :=
{   zero_mem := λ J HJ, (H J HJ).zero_mem,
    one_mem := λ J HJ, (H J HJ).one_mem,
    add_mem := λ a b ha hb J HJ, let X := (H J HJ).add_mem in X (ha J HJ) (hb J HJ),
    mul_mem := sorry,
    neg_mem := sorry,
    inv_mem := sorry,
}
```

You don't need `simp` for stuff like this, you can just spell it out. Although I struggled with `add_mem` and I don't know why, it's something to do with classes that I don't understand properly.

#### [Abhimanyu Pallavi Sudhir (Jan 16 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155283540):
Yeah, the `simp` was a legacy from my code for `field_intersect` with indexed subsets.

#### [Abhimanyu Pallavi Sudhir (Jan 16 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155283598):
Interesting that the `let ... in` thing works, though -- I did notice that going `have` the `add_mem` statement (without feeding it any parameters) in tactic mode worked.

#### [Patrick Massot (Jan 16 2019 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155285644):
This is pretty weird. A more understandable solution would be `λ a b ha hb J HJ, by haveI := H J HJ ; exact is_add_submonoid.add_mem (ha J HJ) (hb J HJ),`

#### [Patrick Massot (Jan 16 2019 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Proving something is a subfield/near/155285877):
Of course you can also use the ugly direct term `@is_add_submonoid.add_mem _ _ _ (H J HJ).to_is_add_submonoid _ _ (ha J HJ) (hb J HJ)`

