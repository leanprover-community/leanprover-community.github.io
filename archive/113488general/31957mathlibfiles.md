---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31957mathlibfiles.html
---

## Stream: [general](index.html)
### Topic: [mathlib files](31957mathlibfiles.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152106884):
@**Mario Carneiro** and @**Johannes Hölzl** Would you be open to a PR reorganizing files in the analysis part of mathlib? There are huge files with a strange import graph. I would like to create new sub-folders  an move stuff around so that it get easier to guess what is in what file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 18 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152106974):
Do you know what you want to do specifically?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107218):
I'd like to have a list of folders inside analysis that looks like topological_space, uniform_spaces, metric_spaces, topological_structures, normed_spaces. In particular moving topological_structures down in the import graph (ie I don't want it to be imported by so many files)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107321):
The current graph looks approximately like https://www.yworks.com/yed-live/?file=https://gist.githubusercontent.com/PatrickMassot/05234c6c375bfd588c346f0dab9b626a/raw/topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107345):
(I removed a couple of redundant edges, and created the thing by hand, so there may be mistakes)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107442):
Of course it would be much easier to reorganize stuff after merging Sébastien's topology PRs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 18 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109554):
It looks to me that most of theses files depend on topological structures?! Is there no edge from topological structures to metric space (or maybe complex...) 
I don't know if splitting up these files into multiple files will help. Some of this stuff is interdependent, forcing it into a hierarchy may be hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109636):
For instance, completion depends on topological structures because we complete groups and rings, but we could have the dependency the other way around, it would make more mathematical sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 18 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109673):
How would topological structures depend on completion of groups and rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109821):
We could have a folder `topological_structures` with files `topological_groups`, `topological_rings`, `normed_spaces`. Each file would contain the relevant completed structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109848):
Mathematically, the construction of the completion of a uniform space doesn't need anything from algebra

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109859):
It is a fundamental construction that is then applied to topological structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Dec 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152110224):
`topological_structures` are used everywhere. The completion operation is a special one. I don't see why we should have the completion at a lower place than topological structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 18 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152110272):
If you are worried that completions get imported everywhere then we can have files topological_group_completion etc inside the topological_structure folder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286325):
I just tried to move files around in the analysis folder, without splitting or joining any file. I get:
```
analysis
├── complex.lean
├── ennreal.lean
├── exponential.lean
├── limits.lean
├── measure_theory
│   ├── borel_space.lean
│   ├── integration.lean
│   ├── lebesgue_measure.lean
│   ├── measurable_space.lean
│   ├── measure_space.lean
│   └── outer_measure.lean
├── metric_space
│   ├── default.lean
│   └── emetric_space.lean
├── nnreal.lean
├── normed_space
│   ├── bounded_linear_maps.lean
│   └── default.lean
├── polynomial.lean
├── probability_mass_function.lean
├── real.lean
├── topological_algebra
│   ├── default.lean
│   ├── infinite_sum.lean
│   ├── quotient_topological_structures.lean
│   └── topological_groups.lean
├── topological_space
│   ├── continuity.lean
│   ├── continuous_map.lean
│   ├── default.lean
│   └── stone_cech.lean
└── uniform_space
    ├── completion.lean
    └── default.lean
```
Note that I didn't increase the depth, only gathered stuff. My next move would be to split topological algebra into `group` and `ring`, and then `group_completion` and `ring_completion`, as well as splitting `uniform_space/completion` into manageable files. Is there any hope to get something like this merged?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286444):
Note also that Lean inserts `default` automatically, so importing the definition of topological space is done by `import analysis.topological_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286538):
There are still some mess at the root of `analysis` above, but it's still a start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286719):
I should say I'm ready to redo this work after PRs with Sébastien and Jeremy get merged (it's very easy to change imports using VScode "replace in files")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286947):
I would also update the documentation of course. I think it would be really nice to have a general cleanup and documentation effort before the Amsterdam workshop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 20 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287198):
This looks appealing!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287836):
what's the difference between `continuity` and `continuous_map`? Also where's basic topology gone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287896):
`continuous_map` is what Johannes renamed my file on the compact-open topology on mapping spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287906):
First question: compare https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean and https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuous_map.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287916):
(it's already there)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287968):
Basic topology is in `topological_space/default.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287987):
I'm not sure that's a good answer... just because it's what's there doesn't mean it's good, especially in a thread on reorganization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287999):
Oh sure, the above is the first step, moving files around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288053):
Then will come split and merge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288069):
I don't like the idea of putting basic stuff in a `default.lean`, these files are usually the supremum of their folders' contents

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288095):
because `import folder.default` = `import folder`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288115):
I think both semantics make sense, and it avoids long names

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288121):
the convention is to put basic stuff in a `basic.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288173):
this would be very easy to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 20 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152290014):
It seems a reorganization could be merged, so I'll wait for the big topology merges and then try something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jan-David Salchow (Dec 21 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152351499):
I like it! Have you considered moving topology out of analysis though?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 21 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152354230):
:slight_smile: of course this was my first reaction. But I don't want to fight here...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jan-David Salchow (Dec 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152360300):
Interesting. Is there a rationale for keeping it in there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198452):
I'm doing the file reorganization for analysis. In the end I think that the separation between topology and analysis doesn't look good. The split is pretty much arbitrary, and files about specialized topics like the compact-open topology end up at the same level as folders like `uniform_space` and `metric_space`. It looks a bit weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198530):
and the instances folder doesn't know where to go

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198555):
I think I'll PR something a bit closer to my original proposal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198789):
there is no rule that a folder must have only files or only folders in it; in fact I would expect that specialized topics end up in loose files alongside folders where the theory is more developed. `data` is like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198804):
so I don't see a problem with `topology/uniform_space/` being sibling to `topology/compact_open.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198836):
I have a commit strictly implementing (the move only part) of the proposal. Now I'm trying something slightly different. We'll see what looks best

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199564):
Let me remark again that for 25 years I had no idea that topology was a subset of analysis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199744):
But then where is analysis starting?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199808):
Of course I can also rename analysis to topology. But soon we'll have derivative, and it's not really topology either (unless you include differential topology in the same folder)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199911):
Maybe I should leave these questions to the topologist :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199940):
aha, deriv is definitely analysis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199944):
so it's nonempty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199946):
I PR'ed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199960):
unless deriv is calculus...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199989):
It is indeed calculus

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199999):
This is the name of that file in my differential topology repository

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200087):
but integrals are also calculus and I don't know where to draw the line from measure theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200131):
in French we have "calcul différentiel" including derivatives and "calcul intégral"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200149):
but elementary courses are about "real analysis", and involve both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200161):
```quote
files about specialized topics like the compact-open topology end up at the same level as folders like `uniform_space` and `metric_space`.
```
I guess this is because we have TOPOLOGY, the top-level classification, and topology as opposed to metric spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200188):
We could also follow Johannes, and have only one mathlib file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200219):
https://github.com/leanprover/mathlib/pull/598

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200432):
wait, so this PR is still putting everything in `analysis/`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200524):
we could have `topology/basic/` for separating topology and TOPOLOGY

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200926):
Or `topology.topology` or even `topology.topological_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155201233):
or `general_topology.topology`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155202935):
what do you mean "everything in analysis"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203005):
Travis seems to be confused by old oleans...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203573):
I'm sorry I don't understand what Reid and you suggest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203587):
I can also rename `analysis` to `topology`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203601):
I think topology and analysis should be separate folders

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203635):
I'm not sure why this is in any way strange

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203695):
That's not the question. The question is how do you choose which files go into which folder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203705):
depends on the file...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203754):
Do you like https://github.com/leanprover/mathlib/tree/ede7943feb0c5a8fa6ea481c8d08adf49104d55e/src ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203828):
I think `metric_space` and `normed_space` can go in analysis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203852):
I realize it's a border case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203903):
I prefer the name `topology`  to `general_topology` for the top level folder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203938):
unless there are any plans for `specific_topology` folders at the top level, it's a meaningless distinction which just makes names longer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203948):
It's much easier to exclude metric spaces if we call it general topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204076):
well it can still mean general topology, I am just objecting to the extra letters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204154):
In lean 2 there were package .md files for all the subfolders, we could bring that back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204190):
As a maintainer for the topology section of mathlib I volunteer to decide which things are or are not topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204197):
Great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204223):
I wanted to ask about this new maintainer list: does it mean you have push access?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204233):
not yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204255):
(My plan is just to follow the MSC)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204262):
Leo has to act to make that happen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204348):
I thought I was elected the documentation dictator, will I get push access?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204718):
Reid, could you tell us what the file organization would look like then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204783):
I can confirm I can build from scratch here, and Travis is confused

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205083):
As a first approximation, I would suggest moving all of `analysis` to `topology` except for `exponential.lean`, `normed_space` and `specific_limits.lean`, leaving the directory structure intact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205106):
That doesn't leave much in `analysis` but I think it's just because we don't have much analysis yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205175):
Isn't this what I had in my first commit?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205231):
Let me check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205298):
As far as the analysis/topology split is concerned, it's exactly the same. (I didn't peek first!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205407):
So I would just suggest bringing back the `topological_space` subdirectory and renaming the top-level directory to `topology` (with the understanding that it really *means* general topology).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205452):
Oh, except for the `instances` directory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205479):
Where would you put those?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205482):
I guess this is a bit awkward, because some of these are also normed spaces. Hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205495):
yes, that's where I started doubting again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205991):
I like keeping `analysis.real` etc where they are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206015):
unless there is a reason to split the file up into topology and analysis stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206097):
Actually it turns out there are no instances related to normed spaces in any of those files. So the whole directory could move to `topology`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206180):
I'm okay with that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206254):
The question will be when we define $$L^p$$ spaces and so on which are normed spaces and therefore also have a topology, what do we do. I think we can just stick everything related to those in the `analysis` directory though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206275):
I agree, that sounds like analysis to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206299):
the whole construction of the space will be an analysis thing anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Jan 16 2019 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155222805):
All this sounds good to me. I agree with Mario that `topology` is better than `general_topology`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 16 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155237245):
I just renamed general_topology to topology, and moved instances there. Is everybody happy?


{% endraw %}
