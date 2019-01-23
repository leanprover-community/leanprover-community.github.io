---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99039Tacticasmacro.html
---

## Stream: [general](index.html)
### Topic: [Tactic as macro](99039Tacticasmacro.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622203):
Is there anyway I can define a tactic (or something local to a proof) that does a fixed number of steps, so I would not need to repeat the whole thing multiple times? For example, a tactic or local definition name `finish_it` that does the following:
```lean
cases ind1
; cases ind2
; cases ind3
; unfold func at hh
; try { contradiction }
; done
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622204):
`iterate`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622355):
I am concerned that your tactic might need to take some inputs (ind1, ind2 etc).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622356):
if it didn't take any inputs then Programming In Lean explains how to do this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622374):
``` lean
iterate 3 { cases ind1
; cases ind2
; cases ind3
; unfold func at hh
; try { contradiction }
; done }

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622432):
to define tactics locally, (make sure that the names will not change), and then just do
```lean
def finish_it : tactic unit := `[ code ]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622441):
see lines 88 to 91 of

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622442):
https://github.com/kbuzzard/mathlib/commit/5ff51dc6993990e600ddee4857a2e207e62f35d1#diff-26b4491c757c999172218bc6c4da2cb0R88

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622449):
to see how I wrote a basic tactic, knowing nothing about metaprogramming in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622460):
see lines 101 to 105 for the application

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125623024):
Thanks, ``` `[code]``` did the trick.
Now I can write `finish_it` and the proof is complete.
But suppose I remove the last two lines from `finish_it` (`try { contradiction }` and `done`). Why I cannot write `finish_it ; try { ... }`. I mean, `;` does not work, but `,` does.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125632538):
This is because `try { ... }` is an interactive mode tactic, so you need the interactive mode `;`, so `finish_it` needs to also be defined in the interactive namespace (`tactic.interactive.finish_it`) if you want to use it in tactics. If you say `finish_it` in a `begin ... end` or `by ...` block and `tactic.interactive.finish_it` doesn't exist, then it will assume it is a term of type `tactic unit` and will find it in the current namespace, but since it's using regular term parsing you won't get nice syntaxes like `try { ... }` that only work in interactive mode.

