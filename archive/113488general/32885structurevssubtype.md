---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32885structurevssubtype.html
---

## Stream: [general](index.html)
### Topic: [structure vs. subtype](32885structurevssubtype.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073745):
I was wondering why one would choose a `structure` over a `subtype` (or vice versa) for `finset` or any similar construction. It seems like the two are equivalent, but I might be missing something. I don't see an advantage for using a `structure`. Using a `subtype` gives you a few existing simple lemmas that you wouldn't have to write, but that's the only advantage I see, and it's relatively minor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073788):
write the appropriate simp lemmas yourself :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073806):
Which simp lemmas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073819):
oh, I thought you meant simp lemma by simple lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073879):
No, I meant `init/data/subtype/basic.lean`, which is all the support I've found for `subtype`:

```lean
import init.logic
open decidable

universes u

namespace subtype

def exists_of_subtype {α : Type u} {p : α → Prop} : { x // p x } → ∃ x, p x
| ⟨a, h⟩ := ⟨a, h⟩

variables {α : Type u} {p : α → Prop}

lemma tag_irrelevant {a : α} (h1 h2 : p a) : mk a h1 = mk a h2 :=
rfl

protected lemma eq : ∀ {a1 a2 : {x // p x}}, val a1 = val a2 → a1 = a2
| ⟨x, h1⟩ ⟨.(x), h2⟩ rfl := rfl

@[simp] lemma eta (a : {x // p x}) (h : p (val a)) : mk (val a) h = a :=
subtype.eq rfl

end subtype

open subtype

instance {α : Type u} {p : α → Prop} {a : α} (h : p a) : inhabited {x // p x} :=
⟨⟨a, h⟩⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073887):
erase "simp" from my advice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073906):
Sure, you could write these yourself, which is why I said the advantage is relatively minor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073921):
So, given that, I'm wondering why choose one or the other.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073968):
then don't choose :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074046):
Oh, there are at least a couple other options, of course, depending on what you want: `exists` and (`p`)`sigma`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074052):
But, still, you have to make choice, assuming you want to do something and not nothing. :stuck_out_tongue_winking_eye:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074056):
write both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074058):
don't use choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074066):
Why, Kenny?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074072):
choice is non-constructive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074115):
It's a decidable choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074137):
Note that I'm talking about constructing something. :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074146):
```quote
I was wondering why one would choose a `structure` over a `subtype` (or vice versa) for `finset` or **any similar construction**.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074207):
never use choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074209):
even when it's decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074213):
it's evil

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074217):
Kenny, why did you choose to enroll at Imperial?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074227):
I didn't choose

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074272):
it just happened

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074283):
Just like you trolling this thread *just happens*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074288):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 04 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074308):
In CS they choose things all the time -- even to the point of breaking symmetry. For example they chose `lt` to be the important one and define `gt` through it. Here it doesn't matter which one to choose, but they had to choose one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 04 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074375):
For making more complex structures, it is dawning on me more and more that you do have to make a design decision -- what the "fundamental" way of doing it is -- and then you build other things on top. But I guess you only prove the lemmas for one implementation and then deduce for the others.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074387):
Kenny, I suggest that it *just happens* that you read the following article in the Journal of the American Philosophical Association: https://www.cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/aristotle-on-trolling/540BB557C82186C33BFFB61E35A0B5B6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074435):
Kevin, yes, and then write a solid API.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074441):
So the question is that in any specific case, e.g. fintype, topological spaces, valuations, whatever -- which construction do you make "fundamental"? And this seems to me to be a very delicate question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074449):
I am currently trying to grasp the math-API to mixed Hodge modules. There really is a lot of API there. A huge black box behind it, but a solid API.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074495):
Kevin, if the API is good, the question becomes a bit less delicate, I hope.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074505):
But lots of parts in mathlib are lacking good API's. (And I myself am very bad at writing good API's.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074509):
```quote
So the question is that in any specific case, e.g. fintype, topological spaces, valuations, whatever -- which construction do you make "fundamental"? And this seems to me to be a very delicate question.
```
For my question, I can only see a slight *practical* advantage to choosing `subtype` over `structure`. I was wondering if there was anything deeper.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074523):
By the way, this :arrow_up: is me trying to stay on the topic of the thread. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 04 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074585):
Though I'm happy to see other threads branch off on related topics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 09 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129344097):
The results of my `finset` `structure` → `subtype` experiment: https://github.com/leanprover/mathlib/pull/183

