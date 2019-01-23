---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48727customizingtidy.html
---

## Stream: [general](index.html)
### Topic: [customizing tidy](48727customizingtidy.html)

---


{% raw %}
#### [ Reid Barton (Jun 03 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127504066):
@**Scott Morrison** I used your `tidy` tactic to automatically generate a bunch of continuity proofs that I was formerly writing out manually like
```lean
continuous_subtype_mk _ $                                                                                                                                                     
  continuous_max                                                                                                                                                              
    (continuous_mul continuous_const (continuous.comp (continuous.comp continuous_fst continuous_subtype_val) continuous_norm))                                               
    (continuous_sub continuous_const (continuous.comp continuous_snd continuous_subtype_val))                                                                                 
```
However, in order to make it run in a reasonable amount of time, I had to create a custom version of `tidy` that only uses a small number of the tactics (I don't need anything even as fancy as `dsimp`).

#### [ Reid Barton (Jun 03 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127504112):
Do you have any thoughts about making `tidy` easier to customize like this? I see that there's an option for adding tactics to the list that `tidy` uses, but to remove tactics I had to copy the definition of `tidy`.

#### [ Reid Barton (Jun 03 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127504531):
Maybe just a matter of making `tidy` a bit more modular at the source level

#### [ Scott Morrison (Jun 04 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520034):
That's a good idea. How about I just pass the list of tactics as a configuration variable, and then in different contexts people can provide a wrapper tactic that installs their preferred list?

#### [ Reid Barton (Jun 04 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520036):
Yes, I think that would be simplest.

#### [ Scott Morrison (Jun 04 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520084):
Maybe I'll rename it `generic_tidy`, to allow specialised variants to still be called `tidy`. (An alternative would be that specialised variations be called `category_tidy` or `topology_tidy`, etc.)

#### [ Reid Barton (Jun 04 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520091):
Another feature I can imagine wanting is to have separate `applicable` and `tidy`attributes for different "instances" of `tidy` (e.g., I might want my `continuity` tactic to only apply the lemmas that prove continuity), but I haven't found just having a single set to be an actual problem yet.

#### [ Scott Morrison (Jun 04 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520135):
My plan with my Lean time at the moment is to 1) get a PR for a small fraction of my category theory library ready, with no automation, 2) try to get my automation into mathlib, 3) get the rest of the category theory library in, with automation

#### [ Scott Morrison (Jun 04 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520139):
Okay --- are there parameters for attributes? I haven't really explored this.

#### [ Reid Barton (Jun 04 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520145):
I've seen attributes that appear to take arguments

#### [ Scott Morrison (Jun 04 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520148):
My inclination though is that this can wait, and namespacing is a better solution: just make sure only the things you want to have tidy use are actually in scope.

#### [ Scott Morrison (Jun 04 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520170):
Also -- a lot of `applicable` will be removed after I get to my "use `ext`" TODO.

#### [ Scott Morrison (Jun 04 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520215):
But it will still be needed in places.

#### [ Reid Barton (Jun 04 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520227):
Definitely it can wait.
Is `applicable` affected by namespacing? I hadn't realized that

#### [ Reid Barton (Jun 04 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520234):
I mean, by which namespaces are open; as opposed to just what files have been imported (which is generally "pretty much everything")

#### [ Scott Morrison (Jun 04 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127520460):
Oh, actually you're probably right, and that it ignores namespacing. At some point I'll investigate whether that is good or bad!

#### [ Scott Morrison (Jun 04 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127521929):
Okay, there's a new commit of `lean-tidy`, that now allows calling `tidy { tactics := [ ... ] }`, to replace my default (carefully curated!) list of tactics.

#### [ Scott Morrison (Jun 04 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/customizing%20tidy/near/127521936):
I'd also be very happy to try to improve my list so it also works on your continuity problems. Having the best possible "out of the box" tidying is nice. :-)


{% endraw %}
