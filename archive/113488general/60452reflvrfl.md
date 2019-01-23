---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60452reflvrfl.html
---

## Stream: [general](index.html)
### Topic: [refl v rfl](60452reflvrfl.html)

---

#### [Kevin Buzzard (Nov 26 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl%20v%20rfl/near/148383637):
I've always had it in the back of my mind that `refl` was slightly more general than `rfl`, because the tactic works with anything tagged `@[refl]`. But I've been trying to write a blog post about equality and I ran into this -- `rfl` working but `refl` not working.

```lean
example : set_of (λ x, x = 3) 3 := rfl

example : set_of (λ x, x = 3) 3 := by refl -- fails
```

What's happening there? For some reason `refl` is deciding not to unfold `set_of`, but it is not marked `irreducible`. There's something I'm not understanding correctly.

#### [Chris Hughes (Nov 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl%20v%20rfl/near/148383903):
My guess is that it doesn't know that the relation in question is equality

