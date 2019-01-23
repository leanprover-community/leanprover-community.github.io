---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03821isthereatactic.html
---

## Stream: [general](index.html)
### Topic: [is there a tactic?](03821isthereatactic.html)

---

#### [Sean Leather (Sep 12 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785751):
Is there a tactic for (part of) this?

```lean
by cases l; apply exists.intro; assumption; assumption
```

#### [Johan Commelin (Sep 12 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785823):
Will `tidy` do this? Or can it not yet do `exists.intro`?

#### [Sean Leather (Sep 12 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785841):
I've never used `tidy`.

#### [Johan Commelin (Sep 12 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785855):
It is really cool. You'll need `import tactic.tidy`.

#### [Kenny Lau (Sep 12 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785901):
I'd just write the whole thing in term mode

#### [Sean Leather (Sep 12 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786086):
Kenny: I had that, but the tactic is more robust to changes in `l`, which are happening.

#### [Sean Leather (Sep 12 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786206):
Also, `l` has a lot of fields, so either using pattern matching or `cases l with ...` is annoyingly long.

#### [Johan Commelin (Sep 12 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786220):
Does `tidy` work?

#### [Sean Leather (Sep 12 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786279):
` by cases l; tidy` works

#### [Sean Leather (Sep 12 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786383):
` by cases l; tidy {trace_result:=tt}` doesn't print anything. :concerned:

#### [Johan Commelin (Sep 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786679):
Huh, so `tidy` won't do the `cases` for you? I expected that it would try that, as some last resort...

#### [Johan Commelin (Sep 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786702):
@**Sean Leather** You can use hole commands to let VScode replace `tidy` with the proof it generated.

#### [Sean Leather (Sep 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786713):
I suppose that would be listed here if it did:

```lean
meta def default_tactics : list (tactic string) :=
[ reflexivity                                 >> pure "refl", 
  `[exact dec_trivial]                        >> pure "exact dec_trivial",
  propositional_goal >> assumption            >> pure "assumption",
  `[ext1]                                     >> pure "ext1",
  intros1                                     >>= λ ns, pure ("intros " ++ (" ".intercalate (ns.map (λ e, e.to_string)))),
  auto_cases,
  `[apply_auto_param]                         >> pure "apply_auto_param",
  `[dsimp at *]                               >> pure "dsimp at *",
  `[simp at *]                                >> pure "simp at *",
  fsplit                                      >> pure "fsplit", 
  injections_and_clear                        >> pure "injections_and_clear",
  propositional_goal >> (`[solve_by_elim])    >> pure "solve_by_elim",
  `[unfold_aux]                               >> pure "unfold_aux",
  tidy.run_tactics ]
```

#### [Johan Commelin (Sep 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786720):
what does `auto_cases` do?

#### [Sean Leather (Sep 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786728):
No idea. :slight_smile:

#### [Sean Leather (Sep 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786771):
```lean
  t' ← whnf t',
  let use_cases := match t' with
  | `(empty)     := tt
  | `(pempty)    := tt
  | `(unit)      := tt
  | `(punit)     := tt
  | `(ulift _)   := tt
  | `(plift _)   := tt
  | `(prod _ _)  := tt
  | `(and _ _)   := tt
  | `(sigma _)   := tt
  | `(subtype _) := tt
  | `(Exists _)  := tt
  | `(fin 0)     := tt
  | `(sum _ _)   := tt -- This is perhaps dangerous!
  | `(or _ _)    := tt -- This is perhaps dangerous!
  | _            := ff
```

#### [Sean Leather (Sep 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786777):
Looks like it's restricted to certain patterns.

#### [Johan Commelin (Sep 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786786):
Right... I guess that makes sense.

#### [Johan Commelin (Sep 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786795):
Anyway, we still golfed your proof (-;

#### [Johan Commelin (Sep 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786812):
It makes sense that `cases l` remains in the proof. It is probably an "idea". After that it is "follow your nose"

#### [Sean Leather (Sep 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786813):
Yep, thanks! I learned something new.

#### [Sean Leather (Sep 12 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786871):
It would be nice to see what `tidy` is doing, though.

#### [Keeley Hoek (Sep 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786948):
Sean, are you using a version of mathlib which incorporates this commit?
https://github.com/leanprover/mathlib/commit/e95111d38c0b2d666f70624ce25a5d728e0db376

#### [Sean Leather (Sep 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133787037):
@**Keeley Hoek** No, certainly not. Thanks!

