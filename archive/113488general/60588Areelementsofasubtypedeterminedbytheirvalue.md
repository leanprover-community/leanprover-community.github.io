---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60588Areelementsofasubtypedeterminedbytheirvalue.html
---

## Stream: [general](index.html)
### Topic: [Are elements of a subtype determined by their value?](60588Areelementsofasubtypedeterminedbytheirvalue.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915156):
```lean
import order.bounds algebra.ordered_group analysis.real analysis.topology.infinite_sum
noncomputable theory

definition nnreal := {r : ℝ // 0 ≤ r}
notation ` ℝ≥0 ` := nnreal

lemma val_eq_val (r₁ r₂ : ℝ≥0) : r₁ = r₂ ↔ r₁.val = r₂.val := sorry
```
I want to mutter something about proof-irrelevance... and of course I'm working classical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 22 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915217):
yes. `subtype.eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915243):
Ok, thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915244):
That is helpful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915299):
I expected that to be right after the definition of a subtype, but I should have thought of looking for a separate file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 22 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915302):
mathlib vs core :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915312):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915354):
All methods have advantages and disadvantages but the reason I'm mentioning this is that it's important to get into the right mindset.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915355):
The logic is "it's important, so it's probably there already, so I could either plough through subtype.lean, or guess what the theorem might be called and try and find it with the ctrl-space dance, or just ask here"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915364):
my posts are appearing in random orders

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915428):
I asked here too much in the early days and it took me a while to figure out the other algorithms, it's a sort of "give a man a fish" thing, and of course asking here is a super-helpful resource, but somehow I understand the other possibilities better now and once you understand them you become more powerful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915432):
And of course from where you're sitting you have no idea about what will be in core and what will be in mathlib, so sometimes it's just less frustrating to ask

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915441):
What it took me a long time to understand was "if it's natural, it's already there, and is almost certainly named well"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916503):
Ok, so I applied your strategy, and expected there to be a `subtype.neq`. But it's not there...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 22 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916508):
someone is being too classical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 22 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916512):
it's just a `rw` for the other direction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916574):
You should add it :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916577):
subtype.eq is an iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916584):
Hmm, so I should `rw`, instead of `apply`...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 22 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916595):
There aren't a lot of negated theorems like that, since `mt` is literally two characters and turns any A -> B into \not B -> \not A

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 22 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916596):
`congr_arg subtype.val`, whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916652):
If H is A <-> B then H.1 is A -> B and H.2 is B -> A, if this helps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916657):
(this is because the _definition_ of <-> is what you think it is)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916672):
Wait, how do I use `mt`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916716):
`#print mt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916718):
Hmmz, I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916720):
or `#check mt` if you just want to see the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916727):
Some questions of the form "how do I use X" are really "what is its type?" and some are "what is its definition?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916728):
Stuff isn't typechecking over here... I'll have to work a bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916729):
so you use `#check` or `#print`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916730):
That's another thing I learnt -- when I get errors now I read them carefully

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916733):
because they tell you exactly what you have got wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 22 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916842):
Ok, so my subtype.eq is not an iff, it's something from core saying
```lean
protected lemma eq : ∀ {a1 a2 : {x // p x}}, val a1 = val a2 → a1 = a2
| ⟨x, h1⟩ ⟨.(x), h2⟩ rfl := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126921269):
OK great -- I just assumed it was an iff from something someone said earlier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126921310):
I guess it's protected because if you open subtype then all of a sudden you have clobbered the definition of eq


{% endraw %}
