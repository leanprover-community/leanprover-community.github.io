---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18763suprandrange.html
---

## Stream: [maths](index.html)
### Topic: [supr and range](18763suprandrange.html)

---

#### [Sebastien Gouezel (Nov 13 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147609120):
There are the following definitions in mathlib:
```lean
def supr (s : ι → α) : α := Sup {a : α | ∃i : ι, a = s i}

def range (f : ι → α) : set α := {x | ∃y, f y = x}
```
You can see that the order after the existential quantifiers is swapped. Therefore, `supr f`and `Sup (range f)` are not defeq. Is this on purpose or by accident? More importantly, if I want to unify the two, which one should I choose? I would rather use the first one `∃i, a = s i`, which could help the simplifier to rewrite `a` if at some point we end up with an assumption of the form `a = s i`, but there might be some reason I am missing for the current definition of `range`.

#### [Sebastien Gouezel (Nov 13 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147609524):
Additional data point:
```lean
def image (f : α → β) (s : set α) : set β := {b | ∃ a, a ∈ s ∧ f a = b}
```

#### [Johannes Hölzl (Nov 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147609790):
oops, I never realized this. I would keep `range` (as it is similar to `image`), and change `supr`.

#### [Mario Carneiro (Nov 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147610281):
the variable on the right thing is also consistent with the definition of `eq`

#### [Sebastien Gouezel (Nov 13 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147611469):
```quote
the variable on the right thing is also consistent with the definition of `eq`
```
 Not sure I get it (too many variables around :). Do you mean that you also think that the definition of `supr` and `image` is right, and that I should fix `range`?

#### [Johannes Hölzl (Nov 13 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612064):
`range` and `image` are the same (the function application is left, and the set-comprehension variable is right). For `supr` it is the other way round

#### [Johan Commelin (Nov 13 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612160):
Shouldn't `supr` be redefined to use `range` explicitly?

#### [Johannes Hölzl (Nov 13 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612244):
Yes, `def supr (s : ι → α) : α := Sup (range s)`

#### [Johan Commelin (Nov 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612351):
Maybe then we should rename `infi` to `infr`, and then the `r` stands for `range` :upside_down: :see_no_evil:

#### [Sebastien Gouezel (Nov 14 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147655093):
```quote
Yes, `def supr (s : ι → α) : α := Sup (range s)`
```
Done in #PR474. It was slightly more painful than I expected, as I had to fix the library all over the place...

