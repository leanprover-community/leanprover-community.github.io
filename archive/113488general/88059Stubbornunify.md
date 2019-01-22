---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88059Stubbornunify.html
---

## [general](index.html)
### [Stubborn unify](88059Stubbornunify.html)

#### [Keeley Hoek (Sep 21 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Stubborn unify/near/134372143):
I've been experimenting with some of the `tactic.*` namespace, which I'm admittedly pretty scared of since some of it seems like magic. In trying to accomplish my nefarious goals, I'm running into quite a wall with `unify` and friends. It's seeming more and more like `unify` is more stubborn (an idiot?) than I first thought; for example, the following happens when I try to `unify` two metavar-containing types (which I think is sensible?)
````
unify tactic failed, failed to unify
  ?m_1 ⥤ ?m_3 : Type (max ? ? ? ?)
and
  D ⥤ C : Type (max (?+1) ? (?+1))
````
(There are hypotheses `D` and `C` with type `Type (?+1)` .)

Why is `unify` not compelled to assign the values of `?m_1` and `?m_3` in this situation?

#### [Simon Hudon (Sep 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Stubborn unify/near/134390656):
Unifying complex universe terms is often a mess. If you can manage to avoid `max` and `imax` in your universe terms, I would go for that. Otherwise, you may need to specifying universes explicitly when resolving constants.

#### [Scott Morrison (Sep 22 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Stubborn unify/near/134414211):
Yeah, get rid of all your ?s in exchange for explicit named universes, and you'll probably see what the obstruction is.

