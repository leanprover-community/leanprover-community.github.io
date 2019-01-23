---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40518tidylostmymetavars.html
---

## Stream: [general](index.html)
### Topic: [tidy lost my metavars](40518tidylostmymetavars.html)

---

#### [Johan Commelin (Nov 29 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148774987):
Somehow `tidy` claims it closed all goals, but the kernel says there are still metavariables left. Is there a good approach to debugging this? Somewhere a metavariable got removed from the goal-list without being fully instantiated. I guess it should be possible to track this, right?

#### [Mario Carneiro (Nov 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148776730):
it is possible to write a tactic that will tell you if the current tactic state is broken, but you will have to sprinkle it around and it will often give false positives because of `focus` and such

#### [Mario Carneiro (Nov 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148776794):
the `recover` tactic does this, essentially

#### [Johan Commelin (Nov 29 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148776998):
Thanks. Didn't know about `recover`. I'll try it out.

#### [Johan Commelin (Nov 29 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148782330):
Oh by the way, `recover` worked. It figured out that there was some naturality condition that wasn't proven. I don't know how it got lost.

#### [Keeley Hoek (Nov 29 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148782541):
It'd be really great to see a reproducible case of that Johan, probably there is a bug in a tactic somewhere

#### [Johan Commelin (Nov 29 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148783366):
@**Keeley Hoek** https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L113
Voila. I retried this with a freshly restarted Lean. Problem still occurs. I have no idea how I could build a MWE out of this. It's pretty deep down in ugly maths.

#### [Keeley Hoek (Nov 29 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148786857):
Seems like a bug in `constructor` to me

#### [Keeley Hoek (Nov 29 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148786936):
For anyone who is interested:
````lean
def oopsie (F : C ⥤ D) : functor.id (presheaf C) ⟹ yoneda_extension F ⋙ restricted_yoneda F :=
begin
  constructor,
  -- One goal
  recover,
  -- Two goals :O
  sorry
end
````

#### [Johan Commelin (Nov 29 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148786989):
But I guess this ties in to the auto_params, doesn't it?

#### [Keeley Hoek (Nov 29 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787002):
I'm not sure I understand

#### [Keeley Hoek (Nov 29 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787009):
I mean, surely it shouldn't erase a metavar it creates from history

#### [Johan Commelin (Nov 29 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787015):
Maybe `constructor` is throwing away goals that have an auto_param attached to them?

#### [Keeley Hoek (Nov 29 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787126):
I wonder if the `extract_opt_auto_param` in `get_constructors_for` has anything to do with it
Actually, I bet it is the `mk_const` on line 23 of constructor_tactic.lean in lean core

#### [Keeley Hoek (Nov 29 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787138):
That could create metavariables which don't get fully bound by the `apply` maybe

#### [Johan Commelin (Nov 29 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787258):
Thanks for debugging this!

