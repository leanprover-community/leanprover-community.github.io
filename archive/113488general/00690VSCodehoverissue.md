---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00690VSCodehoverissue.html
---

## Stream: [general](index.html)
### Topic: [VS Code hover issue](00690VSCodehoverissue.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997129):
```lean
example (A C D : Type) (zzz : A → C) (g : C → C → D) (a : A) : D :=
begin
  apply g (zzz a) (zzz a),
end
```

If I try this in VS Code (on Ubuntu) and hover over the two `zzz`s in the `apply` tactic line, the first one doesn't give me a little transient window saying `zzz : A \to C` but the second one does. Can someone else reproduce? Should I expect the window to pop up for the first `zzz` as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 12 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997252):
I get the corresponding behavior in emacs too, so I guess it is an issue with Lean itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997256):
reproduced (Windows, VS Code)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997258):
`by exact g (zzz a) (zzz a)` has the issue, but just giving the term mode proof makes things work again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997300):
reproduced all three behaviours

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 12 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997657):
This is actually quite annoying whenever I do a `by haveI := _; exact _` proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997702):
So it's the Lean server which ships these little windows out?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997714):
can we have the complicated diagram again?


{% endraw %}
