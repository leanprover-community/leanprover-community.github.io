---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/80156shouldmonotonebeaclass.html
---

## [maths](index.html)
### [should monotone be a class?](80156shouldmonotonebeaclass.html)

#### [Johan Commelin (May 28 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196629):
Should
```lean
def monotone (f : α → β) := ∀⦃a b⦄, a ≤ b → f a ≤ f b
```
be a class? I need compositions of these guys (and then applying a functor to them)...

#### [Johan Commelin (May 28 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196637):
I wouldn't mind if the type class inference system helped me a bit (-;

#### [Johan Commelin (May 28 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196644):
Ooh, this is line 37 of `order/basic.lean`

#### [Andrew Ashworth (May 28 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196934):
would type class inference even help? don't you just need a lemma that says the composition of two monotonically increasing functions is also monotonic?

#### [Johan Commelin (May 28 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127197054):
That exists. But now I need to explicitly refer to it every time I use functoriality

#### [Johan Commelin (May 28 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127197061):
I'dd rather just have that transparently dealt with by Lean

#### [Andrew Ashworth (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127197325):
ahhh. I'm surprised you would reach for type class inference in this case, it's not my first choice. I would try parameters in sections, auto params, and figuring out how to write a mini tactic or helper lemma as well

#### [Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198037):
Ok, I don't really understand what you mean.

#### [Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198050):
I have proved that the simplicial complex is a complex, up to 1 sorry: https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L15-L22

#### [Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198057):
The only thing in that proof is pulling some identity through a functor

#### [Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198061):
I have no idea how to do that.

#### [Johan Commelin (May 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198116):
See https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L80 for the corresponding identity in the source category.

#### [Johan Commelin (May 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202542):
```lean
class simplicial_set :=
(objs : Π n : ℕ, Type*)
(maps {m n : ℕ} {f : [m] → [n]} (hf : monotone f) : objs n → objs m)
(comp {l m n : ℕ} {f : [l] → [m]} {g : [m] → [n]} (hf : monotone f) (hg : monotone g) :
  (maps hf) ∘ (maps hg) = (maps (monotone_comp hf hg)))

namespace simplicial_set
def δ {X : simplicial_set} {n : ℕ} (i : [n+1]) :=
maps (simplex_category.δ_monotone i)

lemma simplicial_identity₁ {X : simplicial_set} {n : ℕ} (i j : [n + 1]) (H : i ≤ j) :
(@δ X n) i ∘ δ j.succ = δ j ∘ δ i.raise :=
begin
unfold δ,
rw comp,
rw comp,
sorry
end
```

#### [Johan Commelin (May 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202543):
How do I remove the final sorry in my file?

#### [Johan Commelin (May 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202612):
In `simplex_category.lean`, I have
```lean
lemma simplicial_identity₁ (i j : [n+1]) (H : i ≤ j) : δ j.succ ∘ δ i = δ i.raise ∘ δ j := "long proof"
```

#### [Johan Commelin (May 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202623):
I just want to pull this through `maps`, but I have no clue at all how to do it.

#### [Patrick Massot (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202700):
I would need to get your files to try to help you

#### [Johan Commelin (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202716):
I linked them a few posts up

#### [Johan Commelin (May 28 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202725):
But generic pointers are also welcome

#### [Johan Commelin (May 28 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202927):
Also, why does my state look like
```lean
X : simplicial_set,
n : ℕ,
i j : fin (n + 1 + 1),
H : i ≤ j
⊢ maps _ ∘ maps _ = maps _ ∘ maps _
```
after I `unfold δ`?

#### [Johan Commelin (May 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202946):
Why the underscores?

#### [Johan Commelin (May 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202977):
I expected something more useful, like `maps (simplex_category.δ_monotone i) ∘ maps (simplex_category ... etc`

#### [Patrick Massot (May 28 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203036):
```lean
lemma simplicial_identity₁ {X : simplicial_set} {n : ℕ} (i j : [n + 1]) (H : i ≤ j) :
(@δ X n) i ∘ δ j.succ = δ j ∘ δ i.raise :=
by finish [δ, comp, simplex_category.simplicial_identity₁]
```

#### [Johan Commelin (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203158):
Brilliant!

#### [Johan Commelin (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203160):
I need to understand `finish`

#### [Johan Commelin (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203163):
But this is awesome, thanks!

#### [Patrick Massot (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203167):
No! Don't try to understand it, it's magic!

#### [Mario Carneiro (May 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127218334):
> Why the underscores?

The only explicit arg in `maps` is `monotone f`, which is a proof. Lean hides proof arguments by default, but this makes it hard to understand these goals unless the `f` is explicit too

#### [Mario Carneiro (May 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127218337):
You can enable proof printing with `set_option pp.proofs true`

#### [Johan Commelin (May 28 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127218384):
Ok, thanks for the explanation!

#### [Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222060):
Johan, those `_`s used to really confuse me. Everyone has told you all the right things but let me tell you the stupid version

#### [Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222097):
All proofs are the same

#### [Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222100):
and are instantly forgotten

#### [Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222101):
so don't even get names

#### [Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222104):
and this is kind of good but kind of annoying

#### [Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222108):
because if you have a subtype, so a value and then a proof, it might well just get displayed as <a,_>

#### [Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222119):
and this is annoying because sometimes you want to change the goal to something defeq with show, so you cut and paste the output from the pretty printer and write "show <the goal>"

#### [Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222120):
and it doesn't work

#### [Mario Carneiro (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222121):
it's not instantly forgotten

#### [Mario Carneiro (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222123):
it's there, it's a term

#### [Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222125):
because Lean can't reconstruct the _s

#### [Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222126):
yes so Lean is only pretending it forgot

#### [Mario Carneiro (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222128):
it's just a big and ugly term

#### [Kevin Buzzard (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222173):
and if you set_option pp.proofs true

#### [Mario Carneiro (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222175):
lean can reconstruct the _

#### [Kevin Buzzard (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222181):
then you can see them all and cut and paste them all again

#### [Kevin Buzzard (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222184):
and it turns out sometimes they're really ugly and long

