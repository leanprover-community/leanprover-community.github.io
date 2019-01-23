---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00534Howdidsimpprovemylemma.html
---

## Stream: [general](index.html)
### Topic: [How did simp prove my lemma?](00534Howdidsimpprovemylemma.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640952):
```lean
set_option trace.simp_lemmas true

example (i : ℤ) : i ≤ i + 1 := by simp
```
I think the consensus is that this example should not be proven by `simp`. Can Lean tell me what the *morally correct* proof is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640973):
`simp` does not prove it in the online version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640979):
The trace option spits out a lot of noise, but I didn't find the lemma that prove this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640991):
neither does it in my local copy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640993):
but you can use `set_option trace.simplify.rewrite true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641048):
My `simp` is stronger than yours!
```
0. [simplify.rewrite] [le_add_iff_nonneg_right]: i ≤ i + 1 ==> 0 ≤ 1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641052):
you imported stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 31 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641056):
Cheater!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641165):
O.o.... :distraught:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641187):
Apparently the category libs by Scott import stuff that give `simp` superpowers when dealing with integers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641248):
I didn't expect that that import would affect the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 31 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641265):
Don't forget that one import can hide thousands imports

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641352):
Yes, that is true. I think that means I should always import Scott's category libs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jul 31 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641543):
Eek, I have no idea how or why I could be responsible. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 31 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641639):
/me mumbles something about synergy...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 31 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641738):
interesting
`example : (0 : ℤ) ≤ 1 = true := rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641790):
because `(0 : ℤ) ≤ 1` can be lifted to `bool`, because it is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641797):
but you already know this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641839):
There is no bool in this example, the proposition is indeed definitionally equal to true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641857):
`bool` isn't involved here. `true` is `true : Prop`
`example : (0 : ℕ) ≤ 1 = true := rfl --doesn't work`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641891):
oops, I misread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641897):
https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/int/order.lean#L13-L17


{% endraw %}
