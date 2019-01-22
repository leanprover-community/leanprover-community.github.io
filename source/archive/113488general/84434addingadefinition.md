---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84434addingadefinition.html
---

## [general](index.html)
### [adding a definition](84434addingadefinition.html)

#### [Keeley Hoek (Sep 14 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133939240):
I'd like implement a `[user_command]` which adds a definition to the environment at the place where the `[user_command]` is executed. Of course, there is `environment.add`, but I have to build a `declaration` and in particular pass a `name`. This won't act the same way as writing `def blah : type = foo ...` on that line because the latter will have a "full name" `me.my_namespace.blah` if this all goes on inside `namespace me.my_namespace`. Is there a way to fix this: either to get the current namespace, or to make a declaration as if it happened using a `def`?

#### [Mario Carneiro (Sep 14 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133939576):
:four_leaf_clover:

#### [Mario Carneiro (Sep 14 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133939698):
there is a command `get_current_definition` that tells you the name of the currently elaborating definition, from which you can derive the namespaces, but it doesn't work in a user command

#### [Keeley Hoek (Sep 14 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133942021):
@**Mario Carneiro** Hallelujah! According to the source code (see `src/library/tactic/tactic_state.cpp`), it turns out that the first element returned by `open_namespaces` is *always* the namespace of the current line, as long as you're in a command! WHOOP WHOOP

#### [Keeley Hoek (Sep 14 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133942101):
*as long as youre being run in *some* namespace, but of course there is a hack to check if this is the case...

#### [Scott Morrison (Sep 14 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133943119):
This will probably all break again in :four_leaf_clover:, but I guess we'll cope. :-)

#### [Keeley Hoek (Sep 14 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133947033):
Ok I was wrong again because my "easy hack" to check you're in the default namespace doesn't work and I can't fix it. But, I just discovered `with_input command_like` in the `lean.parser` monad. It's a backdoor into.... everything! So I can just emit `def blah : type = blah` from the command!

#### [Keeley Hoek (Sep 14 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133947101):
---no silly hack required!

#### [Scott Morrison (Sep 14 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133947786):
oooh... can we add `rfl` lemmas from commands using this??

#### [Keeley Hoek (Sep 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948698):
Yes, you can do anything

#### [Keeley Hoek (Sep 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948710):
It saves the current parser state, then literally hands a string to the parser as if it was the next line of the file, then restores it

#### [Keeley Hoek (Sep 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948714):
@**Scott Morrison**

#### [Keeley Hoek (Sep 14 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948766):
Ill cook up a demo

#### [Scott Morrison (Sep 14 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948866):
I've been wanting to do that for a while; I have lots of boilerplate `rfl` lemmas that just repeat a structure field.

#### [Scott Morrison (Sep 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948933):
I do wonder whether this is a good idea, considering :four_leaf_clover:, but I'm still tempted.

#### [Keeley Hoek (Sep 14 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949017):
when it comes time we could always turn on printing what the command outputs and go and replace them with their content
or every write a script to if there are lots

#### [Keeley Hoek (Sep 14 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949024):
what needs to go in and what needs to come out?

#### [Scott Morrison (Sep 14 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949122):
Here's a prototypical example:
```
def equivalence_inverse (F : C ⥤ D) [full F] [faithful F] [ess_surj F] : D ⥤ C := 
{ obj  := λ X, F.obj_preimage X,
  map' := λ X Y f, F.preimage ((F.fun_obj_preimage_iso X).hom ≫ f ≫ (F.fun_obj_preimage_iso Y).inv),
  map_id' := λ X, begin apply F.injectivity, obviously, end,
  map_comp' := λ X Y Z f g, begin apply F.injectivity, obviously, end }.

-- FIXME pure boilerplate...
@[simp] private lemma equivalence_inverse_map 
  (F : C ⥤ D) [full F] [faithful F] [ess_surj F]
  {X Y : D} (f : X ⟶ Y) : (equivalence_inverse F).map f = F.preimage ((F.fun_obj_preimage_iso X).hom ≫ f ≫ (F.fun_obj_preimage_iso Y).inv) := rfl.
```

#### [Scott Morrison (Sep 14 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949131):
I would like to write: `generate_rfl_lemma equivalence_inverse map`

#### [Keeley Hoek (Sep 14 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951214):
@**Scott Morrison** ok I think I can do that, just sorry, who is getting rid of the primes on (e.g.) `map'`? I've always wondered

#### [Scott Morrison (Sep 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951439):
Yeah, that's a real hack. Unfortunately sometimes it's necessary to state something, and then restate it. (e.g. to clean up the mess that autoparam leaves, or to restate something using a coercion that can only be introduced later).

#### [Scott Morrison (Sep 14 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951460):
The "convention" is now to at first name the declaration with a prime at the end of the name, and then to remove it for the "real" declaration.

#### [Scott Morrison (Sep 14 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951479):
The `restate_axiom` user command does this.

#### [Scott Morrison (Sep 14 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951533):
If it's not given an explicit new name, it inspects the old name, removes a prime if it finds one, and otherwise adds "_lemma".

#### [Keeley Hoek (Sep 14 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951769):
And so you have to prove that what is generated is actually equal to what was there originally all the time?

#### [Keeley Hoek (Sep 14 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951865):
Also, sorry going to cook it up now, just writing library functions and testing they work
The only quirk is that when there is an attribute error, the red line appears on the first line of the file.... But I think there is a way to fix that maybe

#### [Keeley Hoek (Sep 14 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951895):
but we also have a command `suggestion category_theory` now

#### [Keeley Hoek (Sep 14 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133964431):
I don't even think we need my thing to do this actually Scott, since we could always just put the lemma in the same namespace as wherever the parameter (e.g. `equivalence_inverse`) lives

#### [Keeley Hoek (Sep 14 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133966107):
I think I should talk to you more about what exactly it should do, since it seems hard to decide whether for example `{X Y : D}` in the above example should have curly brackets instead of parentheses.

