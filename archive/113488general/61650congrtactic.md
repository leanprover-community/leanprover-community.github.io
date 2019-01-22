---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61650congrtactic.html
---

## [general](index.html)
### [congr tactic](61650congrtactic.html)

#### [Sean Leather (Mar 01 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr tactic/near/123137699):
How do I know when to use the `congr` tactic? It's not in the Lean reference. Are there any good examples? I should've [learned](https://gitter.im/leanprover_public/Lobby?at=5a8d2134c3c5f8b90de5020b) already, but I'm slow. :simple_smile:

#### [Gabriel Ebner (Mar 01 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr tactic/near/123137723):
As a motivating example you could try it on `a + b + c = a + c + b` and see what subgoals you get.

#### [Sean Leather (Mar 01 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr tactic/near/123137799):
```lean
state:
2 goals
a b c : ℕ
⊢ b = c

a b c : ℕ
⊢ c = b
```

#### [Gabriel Ebner (Mar 01 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr tactic/near/123137804):
With regards to the other thread: congr (and all other uses of congruence lemmas in lean such as `cc` and `simp`) skips all arguments that are have a `subsingleton` instance.  For `congr` and `cc` this means you don't need to explicitly show that they're equal.  For `simp` this means you can't rewrite there.

#### [Gabriel Ebner (Mar 01 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr tactic/near/123137911):
Looking back, this may have been a bad example.  The point is: if you have an equality, then `congr` stubbornly reduces it to equalities of subterms (the topmost positions where the two sides differ, that is).

