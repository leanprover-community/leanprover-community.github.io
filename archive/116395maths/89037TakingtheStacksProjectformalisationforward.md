---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/89037TakingtheStacksProjectformalisationforward.html
---

## Stream: [maths](index.html)
### Topic: [Taking the Stacks Project formalisation forward](89037TakingtheStacksProjectformalisationforward.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 09 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135477612):
I formalised the definition of a scheme -- in theory at least. I proved that an affine scheme was a scheme which gave me some sort of hope that I'd formalised the definition correctly. The files are a mess, some people were never happy with the names of the theorems or the names of the lean files, the whole thing needs a tidy. I have a Masters student who *might* be interested. What are the priorities here? He'd like to prove some more lemmas about schemes (and indeed we as a department would like to see some original material). But maybe I could use this as impetus to tidy the whole thing up. Does anyone have any ideas about what could be priorities here? @**Patrick Massot** and @**Johan Commelin** you probably both have clearer ideas than me about where this project should be going.

#### [ Patrick Massot (Oct 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135477722):
It should be going into mathlib

#### [ Patrick Massot (Oct 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135477729):
with mathlib quality

#### [ Kevin Buzzard (Oct 09 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478190):
I thought you'd say that.

#### [ Patrick Massot (Oct 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478389):
And we also need progress by @**Scott Morrison|110087** on sheaves

#### [ Kevin Buzzard (Oct 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478391):
A big question here is what to do with the sheaf theory. I defined a sheaf of rings and a presheaf of sets and a sheaf of sets on a basis of a topological space and blah blah blah; do we just sit and wait for more category theory stuff or use the fact that everything is a typeclass so the low-level approach is fine? How long will it be before mathlib contains all the machinery necessary to write "let F be a presheaf of rings on the topological space X" in a category-theory-like manner, so I don't have to also define morphisms of presheaves?

#### [ Kevin Buzzard (Oct 09 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478435):
two minds with a single thought :-)

#### [ Patrick Massot (Oct 09 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478531):
This is blocking for the perfectoid project as well (also blocked by ring completions, subring issue, etc...)

#### [ Johan Commelin (Oct 09 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481011):
Right. I think those presheaves are pretty close. As soon as @**Scott Morrison|110087**'s coauthors stop being grumpy, we will get `backwards_reasoning` and then all sorts of limits. After that a bunch of stuff about sheaves will be within reach.

#### [ Kevin Buzzard (Oct 09 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481109):
I managed just fine in the schemes project with no category theory. Part of me is scared that using the category theory stuff will actually make things more complicated! And unfortunately I must be completely honest and say that I have not been paying careful attention to exactly what is there and what is not there. I know that Scott's work seems to rely on a bunch of automation and I know that these things are very complicated to get right and that I know essentially nothing which would help. I would like to contribute to Scott's work by actually trying it out in some basic cases and then asking for advice when I can't get it to work.

Perhaps going back to the stacks project and doing it all again using the category-theoretic tools that we either have already or will have soon would be a good test case for this category theory stuff. I think that in particular getting the parts of category theory working which are used widely outside of pure category theory would be an important project.

#### [ Kevin Buzzard (Oct 09 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481135):
Golly so we need backwards reasoning and then limits and _then_ sheaves? Because the sheaf axiom says that some map to a limit is an isomorphism?

#### [ Patrick Massot (Oct 09 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481163):
Right, we need someone totally unrelated to GRU to visit Scott's collaborators towns for tourism

#### [ Johan Commelin (Oct 09 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481415):
@**Kevin Buzzard** I think we should certainly try to take advantage of category theory. After all, we want étale cohomology next, and then you don't want to have live in a parallel universe where you have no category theory available...

#### [ Patrick Massot (Oct 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481438):
Johan, I cannot allow you to bad mouth Bourbaki

#### [ Johan Commelin (Oct 09 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481489):
What did I say wrong? :cold_sweat:

#### [ Patrick Massot (Oct 09 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481497):
You don't like living in a parallel universe without category theory

#### [ Johan Commelin (Oct 09 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481512):
Bourbaki never wrote a volume on étale cohomology.

#### [ Patrick Massot (Oct 09 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481575):
Oh, I just received an email from Bourbaki

#### [ Patrick Massot (Oct 09 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481614):
But it's not about category theory

#### [ Johan Commelin (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481632):
```quote
Oh, I just received an email from Bourbaki
```
He invites you to give a seminar talk about interactive theorem proving?

#### [ Patrick Massot (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481634):
He wants another seminar talk

#### [ Johan Commelin (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481640):
```quote
He wants another seminar talk
```
Congratulations!

#### [ Patrick Massot (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481645):
No, unfortunately it's another topic

#### [ Patrick Massot (Oct 09 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481714):
Hales gave a Bourbaki seminar on proof assistants not so long ago

#### [ Patrick Massot (Oct 09 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481720):
so I don't think they'll want another one before seeing real progress here

#### [ Patrick Massot (Oct 09 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481745):
http://www.bourbaki.ens.fr/seminaires/2014/Prog_juin14.html

#### [ Patrick Massot (Oct 09 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481892):
What's funny is I wanted to write Bourbaki an email asking whether he currently think he left a gap about that completion map thing or whether he claims this is only an ellipsis

#### [ Patrick Massot (Oct 09 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481916):
Of course there is a risk he doesn't remember

#### [ Patrick Massot (Oct 09 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481945):
he wrote that GT book in 1971

#### [ Johan Commelin (Oct 09 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135482138):
@**Kevin Buzzard** What does "original" mean for a masters project? Is computing an example enough? Or do we need a new lemma? Because that will be extremely hard to do in Lean.

#### [ Kevin Buzzard (Oct 09 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135482981):
Proving some basic lemmas about schemes and completely fixing up the schemes code is definitely enough.

#### [ Kevin Buzzard (Oct 09 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135482985):
Oh talking of schemes, you're not going to believe this: I've been asked to give a talk on them!

#### [ Kevin Buzzard (Oct 09 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483047):
http://aitp-conference.org/2019/ :D

#### [ Kevin Buzzard (Oct 09 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483058):
So it needs to be fixed up by then!

#### [ Johan Commelin (Oct 09 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483616):
That's nice!

#### [ Johan Commelin (Oct 09 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483634):
So I suggest that this master student turns it into a project to get schemes into mathlib. And then prove the Gamma_Spec adjunction.

#### [ Johan Commelin (Oct 09 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483666):
Alternatively, define smooth morphisms. Or something like that.

#### [ Kevin Buzzard (Oct 09 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484086):
I'd forgotten about gamma spec adjunction! That's an excellent project

#### [ Kevin Buzzard (Oct 09 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484098):
I never even did locally ringed spaces

#### [ Kevin Buzzard (Oct 09 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484202):
Because spec of a ring is automatically locally ringed and I never defined a morphism of schemes :-)

#### [ Johan Commelin (Oct 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484402):
Right, so we need some category theory (-;

#### [ Johan Commelin (Oct 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484434):
Another non-trivial but fundamental thing: fibre products of schemes.

#### [ Reid Barton (Oct 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135488955):
> "let F be a presheaf of rings on the topological space X"

As it happens, we have this specific thing already. Not sure how far that will actually get you though.
```lean
import category_theory.opposites
import category_theory.examples.topological_spaces
import category_theory.examples.rings

open category_theory category_theory.examples

variables {X : Top} {F : (open_set X)ᵒᵖ ⥤ Ring}
```

#### [ Patrick Massot (Oct 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135489039):
But we can't look at its stalks, right?

#### [ Reid Barton (Oct 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135489043):
except it looks like `open_set` already has the order reversed for some reason

#### [ Reid Barton (Oct 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135489065):
Right, basically anything past this involves either limits or colimits of some kind.

#### [ Scott Morrison (Oct 09 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135500370):
I'm listening. :-) I've tried once or twice to just make my code on limits not need backwards_reasoning, but it felt pretty painful to me. `backwards_reasoning` \ `back` is actually quite close. Simon has ideas to make it efficient, but hopefully an inefficient PR can make it into mathlib if there's a promise we know how to make it fast, later.

#### [ Scott Morrison (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135500456):
@**Reid Barton**, Should I revert `open_set` to the usual definition? I guess I was just thinking "no one ever uses the forward direction, just the opposite category, lets just cut out the middleman".

#### [ Scott Morrison (Oct 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135500470):
(Perhaps the explicit opposites were causing some pain, but I don't think so.)

#### [ Reid Barton (Oct 09 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135501687):
@**Scott Morrison|110087**, if the many different shapes of limit are causing some difficulty, I know that I would find it already very helpful to have just general (co)limits. Perhaps it would even be possible to do a version of these before `back` is merged (I might take another shot at this in a couple of days--I tried to set up a branch with all the limit types but it turned into too much work).

#### [ Reid Barton (Oct 09 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135501770):
Basically everything I want to formalize for locally presentable categories and model categories involves some kind of limits or colimits but a large fraction of it only needs general (co)limits (some other parts do need specific shapes like pushouts).

#### [ Reid Barton (Oct 09 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135501785):
I guess the situation for perfectoid spaces may be similar

#### [ Scott Morrison (Oct 10 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135502648):
Ok, I'll keep that in mind. There are a few missing sections on equalizers and pullbacks, but I was intending to leave those out at first anyway. Really the only thing to do for the PR is deal with the dependency on `back`.

#### [ Scott Morrison (Oct 10 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534437):
getting closer. The new `back` works fine in my limits code, now it's just a matter of copying and pasting all the sequences of rewrites `rewrite_search` finds into the source code... :-(

#### [ Scott Morrison (Oct 10 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534445):
It's not like `rewrite_search` is going to be merged anytime soon. :-)

#### [ Johan Commelin (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534730):
@**Scott Morrison|110087** This copy-pasting should/can be automated.

#### [ Scott Morrison (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534746):
Meh... it should be made unnecessary. :-)

#### [ Johan Commelin (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534748):
Anyway, I'm really glad to hear that `back` is converging to mathlib.

#### [ Scott Morrison (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534750):
But okay, I agree.

#### [ Johan Commelin (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534765):
I wrote a substitution script that takes coordinates and replacement text and patches up your file.

#### [ Scott Morrison (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534766):
We need to learn how to have tactics talk directly to VS Code.

#### [ Johan Commelin (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534770):
It is a sort of poor man's diff-patch.

#### [ Scott Morrison (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534771):
command line scripts are too messy

#### [ Scott Morrison (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534779):
I think Gabriel and Mario were talking about exactly this

#### [ Mario Carneiro (Oct 10 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135560201):
Could @**Scott Morrison** or someone explain why limits are difficult to formalize or require `back`? Seems like the basics are just more definitions, and everyone I have seen talking about (co)limits don't seem to expect more than that

#### [ Johan Commelin (Oct 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135560302):
I think it is mostly to make `obviously` do the right thing as auto_param.

#### [ Johan Commelin (Oct 10 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135560330):
But I'm only guessing.

#### [ Scott Morrison (Oct 11 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135571576):
Yeah, it is mostly me being lame, and not wanting to give up my automation. Sorry for making everyone wait. I made `limits.lean` itself mathlib ready last night, and as it turned out removing the dependency on `rewrite_search` was much more painful than removing `back` would have been.

#### [ Kevin Buzzard (Oct 13 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727023):
I am doing a review of the stacks project code, because this is far more interesting than all the crappy reference letter requests I have piling up and I can now legitimately claim that is part of a work project, because I have an MSc student who is going to work on it and I am speaking about it at AITP 2019.

#### [ Kevin Buzzard (Oct 13 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727025):
Are open immersions of topological spaces in mathlib?

#### [ Kevin Buzzard (Oct 13 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727035):
Basic things such as composition of two open immersions is an open immersion, that sort of thing.

#### [ Patrick Massot (Oct 13 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727250):
The closest that we almost have is https://github.com/leanprover-community/mathlib/blob/9d743bbb864234821c4ec881d4dc930ac3631838/analysis/topology/continuity.lean#L401

#### [ Kevin Buzzard (Oct 16 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135906728):
I want to define a locally ringed space in Lean (or rather get a student to define it). So this is a topological space plus a sheaf of rings plus an axiom about some direct limits (see [stacks project](https://stacks.math.columbia.edu/tag/01HA) for more info). I don't see that we have to wait for categories for this to happen. But when categories arrive, will this work somehow be wasted? I am assuming not. I didn't ever define a locally ringed space in the schemes repo, I dodged it, but I think I want to do things more properly this time.

#### [ Reid Barton (Oct 16 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910198):
Well, what work is there? Certainly the bits to do with defining local rings and local ring maps will not be made redundant.

#### [ Reid Barton (Oct 16 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910259):
We already have all the ingredients for presheaves of rings in mathlib.

#### [ Reid Barton (Oct 16 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910412):
There is an oper PR which includes equalizers and products and another WIP one which constructs them for rings, so then you can define sheaves in that language. Johan seemed interested in defining sites for the perfectoid space project, and that seems like a reasonably small amount of effort to "future-proof" sheaves for the zariski topology

#### [ Johan Commelin (Oct 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910505):
@**Kevin Buzzard** I think all the category theory will be there before your student has learned enough Lean to start working on this project.

#### [ Reid Barton (Oct 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910520):
I think the remaining bit is to construct directed colimits of rings. Here you probably cannot avoid spending some effort which, eventually, could be superseded by some general machinery on finitary algebraic theories

#### [ Kevin Buzzard (Oct 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910526):
My student is a 4th year joint maths and computing student that spent the summer working with Coq

#### [ Kevin Buzzard (Oct 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910571):
The issue is that he has to learn some commutative algebra

#### [ Kevin Buzzard (Oct 16 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910634):
```quote
We already have all the ingredients for presheaves of rings in mathlib.
```
So what does the definition of a locally ringed space look like now? It's going to be a structure consisting of a topological space, and then a presheaf of rings -- but I shouldn't define this by hand myself now? And then some lemma about a direct limit being local.

#### [ Johan Commelin (Oct 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910706):
Well, stalks are also done by Scott. This should land within a couple of weeks (at most).

#### [ Johan Commelin (Oct 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910719):
So you have to define a ring structure on the stalk. Local rings are already in mathlib.

#### [ Kevin Buzzard (Oct 16 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910833):
Stalks for sheaves of sets I guess?

#### [ Kevin Buzzard (Oct 16 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910842):
or types in this case

#### [ Johan Commelin (Oct 16 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135911308):
Yes, exactly. That's what I meant with "you have to define a ring structure on the stalk". I really think that this project should try to make schemes mathlib-ready. And as corollary, use all the machinery that is (almost) available.

#### [ Reid Barton (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135912622):
And the fact that you can define a ring structure on the stalk clearly has very little to do with the specific definition of a ring.

#### [ Reid Barton (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135912651):
So if you do it for rings in particular, then in the long run that particular effort is "wasted" (in some sense)

#### [ Scott Morrison (Oct 17 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135944821):
I have no idea what compiles here, but
https://github.com/semorrison/lean-category-theory/blob/working/src/category_theory/presheaves/locally_ringed.lean

#### [ Scott Morrison (Oct 17 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135945243):
Certainly filtered colimits of rings is not done yet, and should be. Your student, Kevin, should do this!

#### [ Mario Carneiro (Oct 17 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135948225):
@**Kevin Buzzard** I think that it would be best to do this with categories. Now that they are there, they should be put to some use! I recall you using this as an argument in favor of category theory last time this came up

#### [ Kevin Buzzard (Oct 17 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954315):
I think that when I was trying to write the code last Feb I would just keep saying "look these things are a category" without ever really thinking about what advantage this would actually give me. Here's a concrete question. A locally ringed space is a topological space, a functor from the category of open sets to the category of rings, an axiom about this functor (a statement about the values of the functor on open covers of open sets -- some kernel equals some image) and another axiom about this functor (about direct limits of rings which are values of the functor being local rings). I can write all of that without ever mentioning categories, but the language (functors, direct limits) is everywhere. I am still unclear about what the modern way to define this structure is (independent of my usual confusion about what should be bundled).

#### [ Johan Commelin (Oct 17 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954380):
Kevin, you saw that I could extend a presheaf from a basis in 10 lines. Otoh now I'm struggling with topological bases, and it's a real pain.

#### [ Kevin Buzzard (Oct 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954459):
I am not reading these technical threads carefully right now, I am really snowed under. I write in the beginner threads because those are the only ones where I can understand what's going on easily and quickly. I do remember your post though. And you can do this because you defined a presheaf to be a functor?

#### [ Johan Commelin (Oct 17 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954738):
I can do this because of all Scott's magic. The automation takes care of a lot of painful noise.

#### [ Kevin Buzzard (Oct 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135955243):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628 (for my own reference)

#### [ Kevin Buzzard (Oct 22 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274105):
[presheaf stuff](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628)

#### [ Kevin Buzzard (Oct 22 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274134):
(deleted)

#### [ Kevin Buzzard (Oct 22 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274294):
@**Johan Commelin** it's time that the people at Imperial College began to understand how presheaves work now. @**Ramon Fernandez Mir** is hopefully going to be formalising a locally ringed space soon.

#### [ Ramon Fernandez Mir (Oct 22 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274857):
Hello, I'm Ramon. I'm doing my Master's project with Kevin and we'll be formalising more parts of the Stacks project. As he said, I'm currently trying to formalise a locally ringed space. I was wondering where I could find the
```quote
[presheaf stuff](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628)
```
@**Johan Commelin**

#### [ Johan Commelin (Oct 22 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136279420):
@**Ramon Fernandez Mir** Hi, nice to meet you! I'm pretty busy until next week Wednesday (2 guests are visiting), but after that I hope to return to this stuff. In the mean time I'll keep an I on these threads.

#### [ Kevin Buzzard (Oct 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343084):
So to do locally ringed spaces we need that stalks are local, so we need colimits in the category of commutative rings. If we were doing this in a category free way then I'd know what to do. How does this all work within the category theory framework? This would be a colimit over the set of all open sets containing a fixed point `a` in a topological space `X`.

#### [ Reid Barton (Oct 23 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343514):
I assume you also want a specific explicit description of the stalk. So under the current/near future state of category theory in mathlib, I would suggest just doing the "category-free" construction, and then if it seems useful or interesting, also show that what you built is actually a colimit, i.e., fits in a cocone with the expected universal property.

#### [ Reid Barton (Oct 23 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343663):
I guess proving that the stalk is a colimit should help you prove that a morphism of ringed spaces does induce maps on stalks, for example.

#### [ Reid Barton (Oct 23 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343856):
But given the state of limits right now, "should" in that sentence is more of a design criterion for limits, not an assertion.

#### [ Reid Barton (Oct 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136345079):
Ah, but the *input* to the construction of a filtered (or directed) colimit of rings should already be in the category theory language.

#### [ Reid Barton (Oct 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136345498):
Let me check what is actually in mathlib so far...

#### [ Reid Barton (Oct 23 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136345838):
I suggest starting from here
```lean
import category_theory.functor
import category_theory.examples.rings

universe u

/- Copied from https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/filtered.lean -/
/- Name collides with mathlib `directed`... -/
class directed_preorder (α : Type u) [preorder α] :=
(bound (x₁ x₂ : α) : α)
(i₁ (x₁ x₂ : α) : x₁ ≤ bound x₁ x₂)
(i₂ (x₁ x₂ : α) : x₂ ≤ bound x₁ x₂)

open category_theory.examples

def directed_colimit_of_rings {J : Type u} [preorder J] [directed_preorder J]
  (F : J ⥤ Ring) : Ring :=
sorry
```

#### [ Reid Barton (Oct 23 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346013):
and then also constructing morphisms in `Ring` from `F j` to `directed_colimit_of_rings F`, and checking that these are compatible with the diagram maps `F j -> F k`, and then also that `directed_colimit_of_rings F` has the universal property

#### [ Reid Barton (Oct 23 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346088):
(and possibly you want to do filtered colimits instead, though directed ones would be enough for Zariski)

#### [ Reid Barton (Oct 23 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346609):
Then, I would suggest building the indexing category for the colimit "opens containing `x`" by hand, or possibly using `full_subcategory`, and check that its opposite category is filtered, and then define `stalk x F` as the `directed_colimit_of_rings` of `F` composed with the inclusion of "opens containing `x`" in `opens X`

#### [ Reid Barton (Oct 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346750):
Oh, I see that that `directed_preorder` is missing the `inhabited` constraint

#### [ Reid Barton (Oct 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346863):
(I'm also not sure that `directed_preorder` should really contain data, rather than being a Prop or subsingleton)

#### [ Kevin Buzzard (Oct 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136348068):
Oh thanks a lot Reid! This is all for @**Ramon Fernandez Mir** who knows a bunch of Coq but is just starting with Lean.


{% endraw %}
