---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73049notationandvariables.html
---

## Stream: [general](index.html)
### Topic: [notation and variables](73049notationandvariables.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148826839):
It suddenly occurs to me, about 10 hours before a lecture (and I intend to spend at least 7 of those hours sleeping) that it would be cool if I could do some examples of basic arguments with equivalence relations in Lean, live in the lecture. But actually I am not sure of the best way to do this. Here's the sort of thing I want to do -- prove, for example, that if `r` is an equivalence relation, and `r a b` and `r c b` and `r c d`, then `r a d`. But I want to do it with notation -- I want to write `a ~ b` or some -- any -- random symbol, rather than the prefix notation `r`. However when I define `r : S -> S -> Prop` as a variable I find that I can't use notation, because `r` is a local variable, and if I define `r` within an example -- `example (S : Type) (r : S -> S -> Prop)...` then I can't figure out how to get notation working before I state the theorem. What am I missing? This is for teaching purposes, so I want it to look as slick as possible.

```lean
variables (S : Type) (r : S → S → Prop)

example (H : equivalence r) : ∀ a : S, r a a := H.1
```

That is not ideal either -- `H.1` looks a bit weird to a mathematician :-/ But I think I'd rather have the notation, and worry about `H.1` later...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 30 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148827043):
You can use local notation. For example https://gist.github.com/rwbarton/7bd5b3b19d930f577355a596a5ed8b4d#file-crec-lean-L7
I don't think the fact that I used `parameter` rather than `variable` there matters for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148828911):
```lean
import tactic.interactive

variables (S : Type) (r : S → (S → Prop))

local notation a ` ~ ` b := r a b

example (H : equivalence r) (a b c d : S)
  (Hab : a ~ b) (Hcb : c ~ b) (Hcd : c ~ d) : a ~ d :=
begin
  rcases H with ⟨Hrefl,Hsymm,Htrans⟩,
  have Hbc : b ~ c,
    exact Hsymm Hcb,
  have Hac : a ~ c,
    exact Htrans Hab Hbc,
  exact Htrans Hac Hcd,
end
```

Works! I am in two minds about whether to use rcases or cases twice and save myself the import.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148828913):
Thanks Reid.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148829124):
don't save yourself the import

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 30 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148829126):
I think it is good to show off mathlib tactics when possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148830140):
Hey! I've just noticed that the pretty printer doesn't use my nice notation for r!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148830862):
aww man, that's a bit annoying. I definitely want to work with an arbitrary equivalence relation but I'd really like the notation.


{% endraw %}
