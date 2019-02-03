---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31957mathlibfiles.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mathlib files](https://leanprover-community.github.io/archive/113488general/31957mathlibfiles.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Dec 18 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152106884):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Would you be open to a PR reorganizing files in the analysis part of mathlib? There are huge files with a strange import graph. I would like to create new sub-folders  an move stuff around so that it get easier to guess what is in what file</p>

#### [ Mario Carneiro (Dec 18 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152106974):
<p>Do you know what you want to do specifically?</p>

#### [ Patrick Massot (Dec 18 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107218):
<p>I'd like to have a list of folders inside analysis that looks like topological_space, uniform_spaces, metric_spaces, topological_structures, normed_spaces. In particular moving topological_structures down in the import graph (ie I don't want it to be imported by so many files)</p>

#### [ Patrick Massot (Dec 18 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107321):
<p>The current graph looks approximately like <a href="https://www.yworks.com/yed-live/?file=https://gist.githubusercontent.com/PatrickMassot/05234c6c375bfd588c346f0dab9b626a/raw/topology" target="_blank" title="https://www.yworks.com/yed-live/?file=https://gist.githubusercontent.com/PatrickMassot/05234c6c375bfd588c346f0dab9b626a/raw/topology">https://www.yworks.com/yed-live/?file=https://gist.githubusercontent.com/PatrickMassot/05234c6c375bfd588c346f0dab9b626a/raw/topology</a></p>

#### [ Patrick Massot (Dec 18 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107345):
<p>(I removed a couple of redundant edges, and created the thing by hand, so there may be mistakes)</p>

#### [ Patrick Massot (Dec 18 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152107442):
<p>Of course it would be much easier to reorganize stuff after merging Sébastien's topology PRs</p>

#### [ Johannes Hölzl (Dec 18 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109554):
<p>It looks to me that most of theses files depend on topological structures?! Is there no edge from topological structures to metric space (or maybe complex...) <br>
I don't know if splitting up these files into multiple files will help. Some of this stuff is interdependent, forcing it into a hierarchy may be hard.</p>

#### [ Patrick Massot (Dec 18 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109636):
<p>For instance, completion depends on topological structures because we complete groups and rings, but we could have the dependency the other way around, it would make more mathematical sense</p>

#### [ Johannes Hölzl (Dec 18 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109673):
<p>How would topological structures depend on completion of groups and rings?</p>

#### [ Patrick Massot (Dec 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109821):
<p>We could have a folder <code>topological_structures</code> with files <code>topological_groups</code>, <code>topological_rings</code>, <code>normed_spaces</code>. Each file would contain the relevant completed structures</p>

#### [ Patrick Massot (Dec 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109848):
<p>Mathematically, the construction of the completion of a uniform space doesn't need anything from algebra</p>

#### [ Patrick Massot (Dec 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152109859):
<p>It is a fundamental construction that is then applied to topological structures</p>

#### [ Johannes Hölzl (Dec 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152110224):
<p><code>topological_structures</code> are used everywhere. The completion operation is a special one. I don't see why we should have the completion at a lower place than topological structures</p>

#### [ Patrick Massot (Dec 18 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152110272):
<p>If you are worried that completions get imported everywhere then we can have files topological_group_completion etc inside the topological_structure folder</p>

#### [ Patrick Massot (Dec 20 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286325):
<p>I just tried to move files around in the analysis folder, without splitting or joining any file. I get:</p>
<div class="codehilite"><pre><span></span>analysis
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
</pre></div>


<p>Note that I didn't increase the depth, only gathered stuff. My next move would be to split topological algebra into <code>group</code> and <code>ring</code>, and then <code>group_completion</code> and <code>ring_completion</code>, as well as splitting <code>uniform_space/completion</code> into manageable files. Is there any hope to get something like this merged?</p>

#### [ Patrick Massot (Dec 20 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286444):
<p>Note also that Lean inserts <code>default</code> automatically, so importing the definition of topological space is done by <code>import analysis.topological_space</code></p>

#### [ Patrick Massot (Dec 20 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286538):
<p>There are still some mess at the root of <code>analysis</code> above, but it's still a start</p>

#### [ Patrick Massot (Dec 20 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286719):
<p>I should say I'm ready to redo this work after PRs with Sébastien and Jeremy get merged (it's very easy to change imports using VScode "replace in files")</p>

#### [ Patrick Massot (Dec 20 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152286947):
<p>I would also update the documentation of course. I think it would be really nice to have a general cleanup and documentation effort before the Amsterdam workshop</p>

#### [ Scott Morrison (Dec 20 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287198):
<p>This looks appealing!</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287836):
<p>what's the difference between <code>continuity</code> and <code>continuous_map</code>? Also where's basic topology gone</p>

#### [ Reid Barton (Dec 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287896):
<p><code>continuous_map</code> is what Johannes renamed my file on the compact-open topology on mapping spaces</p>

#### [ Patrick Massot (Dec 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287906):
<p>First question: compare <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean">https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean</a> and <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuous_map.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuous_map.lean">https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuous_map.lean</a></p>

#### [ Patrick Massot (Dec 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287916):
<p>(it's already there)</p>

#### [ Patrick Massot (Dec 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287968):
<p>Basic topology is in <code>topological_space/default.lean</code></p>

#### [ Mario Carneiro (Dec 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287987):
<p>I'm not sure that's a good answer... just because it's what's there doesn't mean it's good, especially in a thread on reorganization</p>

#### [ Patrick Massot (Dec 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152287999):
<p>Oh sure, the above is the first step, moving files around</p>

#### [ Patrick Massot (Dec 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288053):
<p>Then will come split and merge</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288069):
<p>I don't like the idea of putting basic stuff in a <code>default.lean</code>, these files are usually the supremum of their folders' contents</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288095):
<p>because <code>import folder.default</code> = <code>import folder</code></p>

#### [ Patrick Massot (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288115):
<p>I think both semantics make sense, and it avoids long names</p>

#### [ Mario Carneiro (Dec 20 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288121):
<p>the convention is to put basic stuff in a <code>basic.lean</code></p>

#### [ Patrick Massot (Dec 20 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152288173):
<p>this would be very easy to do</p>

#### [ Patrick Massot (Dec 20 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152290014):
<p>It seems a reorganization could be merged, so I'll wait for the big topology merges and then try something</p>

#### [ Jan-David Salchow (Dec 21 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152351499):
<p>I like it! Have you considered moving topology out of analysis though?</p>

#### [ Patrick Massot (Dec 21 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152354230):
<p><span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span> of course this was my first reaction. But I don't want to fight here...</p>

#### [ Jan-David Salchow (Dec 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/152360300):
<p>Interesting. Is there a rationale for keeping it in there?</p>

#### [ Patrick Massot (Jan 15 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198452):
<p>I'm doing the file reorganization for analysis. In the end I think that the separation between topology and analysis doesn't look good. The split is pretty much arbitrary, and files about specialized topics like the compact-open topology end up at the same level as folders like <code>uniform_space</code> and <code>metric_space</code>. It looks a bit weird</p>

#### [ Patrick Massot (Jan 15 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198530):
<p>and the instances folder doesn't know where to go</p>

#### [ Patrick Massot (Jan 15 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198555):
<p>I think I'll PR something a bit closer to my original proposal</p>

#### [ Mario Carneiro (Jan 15 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198789):
<p>there is no rule that a folder must have only files or only folders in it; in fact I would expect that specialized topics end up in loose files alongside folders where the theory is more developed. <code>data</code> is like that</p>

#### [ Mario Carneiro (Jan 15 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198804):
<p>so I don't see a problem with <code>topology/uniform_space/</code> being sibling to <code>topology/compact_open.lean</code></p>

#### [ Patrick Massot (Jan 15 2019 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155198836):
<p>I have a commit strictly implementing (the move only part) of the proposal. Now I'm trying something slightly different. We'll see what looks best</p>

#### [ Kevin Buzzard (Jan 15 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199564):
<p>Let me remark again that for 25 years I had no idea that topology was a subset of analysis.</p>

#### [ Patrick Massot (Jan 15 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199744):
<p>But then where is analysis starting?</p>

#### [ Patrick Massot (Jan 15 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199808):
<p>Of course I can also rename analysis to topology. But soon we'll have derivative, and it's not really topology either (unless you include differential topology in the same folder)</p>

#### [ Kevin Buzzard (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199911):
<p>Maybe I should leave these questions to the topologist :-)</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199940):
<p>aha, deriv is definitely analysis</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199944):
<p>so it's nonempty</p>

#### [ Patrick Massot (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199946):
<p>I PR'ed</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199960):
<p>unless deriv is calculus...</p>

#### [ Patrick Massot (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199989):
<p>It is indeed calculus</p>

#### [ Patrick Massot (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155199999):
<p>This is the name of that file in my differential topology repository</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200087):
<p>but integrals are also calculus and I don't know where to draw the line from measure theory</p>

#### [ Patrick Massot (Jan 15 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200131):
<p>in French we have "calcul différentiel" including derivatives and "calcul intégral"</p>

#### [ Patrick Massot (Jan 15 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200149):
<p>but elementary courses are about "real analysis", and involve both</p>

#### [ Reid Barton (Jan 15 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200161):
<blockquote>
<p>files about specialized topics like the compact-open topology end up at the same level as folders like <code>uniform_space</code> and <code>metric_space</code>.</p>
</blockquote>
<p>I guess this is because we have TOPOLOGY, the top-level classification, and topology as opposed to metric spaces</p>

#### [ Patrick Massot (Jan 15 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200188):
<p>We could also follow Johannes, and have only one mathlib file</p>

#### [ Patrick Massot (Jan 15 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200219):
<p><a href="https://github.com/leanprover/mathlib/pull/598" target="_blank" title="https://github.com/leanprover/mathlib/pull/598">https://github.com/leanprover/mathlib/pull/598</a></p>

#### [ Mario Carneiro (Jan 15 2019 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200432):
<p>wait, so this PR is still putting everything in <code>analysis/</code>?</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200524):
<p>we could have <code>topology/basic/</code> for separating topology and TOPOLOGY</p>

#### [ Reid Barton (Jan 15 2019 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155200926):
<p>Or <code>topology.topology</code> or even <code>topology.topological_space</code></p>

#### [ Reid Barton (Jan 15 2019 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155201233):
<p>or <code>general_topology.topology</code></p>

#### [ Patrick Massot (Jan 15 2019 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155202935):
<p>what do you mean "everything in analysis"?</p>

#### [ Patrick Massot (Jan 15 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203005):
<p>Travis seems to be confused by old oleans...</p>

#### [ Patrick Massot (Jan 15 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203573):
<p>I'm sorry I don't understand what Reid and you suggest</p>

#### [ Patrick Massot (Jan 15 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203587):
<p>I can also rename <code>analysis</code> to <code>topology</code></p>

#### [ Mario Carneiro (Jan 15 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203601):
<p>I think topology and analysis should be separate folders</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203635):
<p>I'm not sure why this is in any way strange</p>

#### [ Patrick Massot (Jan 15 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203695):
<p>That's not the question. The question is how do you choose which files go into which folder</p>

#### [ Mario Carneiro (Jan 15 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203705):
<p>depends on the file...</p>

#### [ Patrick Massot (Jan 15 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203754):
<p>Do you like <a href="https://github.com/leanprover/mathlib/tree/ede7943feb0c5a8fa6ea481c8d08adf49104d55e/src" target="_blank" title="https://github.com/leanprover/mathlib/tree/ede7943feb0c5a8fa6ea481c8d08adf49104d55e/src">https://github.com/leanprover/mathlib/tree/ede7943feb0c5a8fa6ea481c8d08adf49104d55e/src</a> ?</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203828):
<p>I think <code>metric_space</code> and <code>normed_space</code> can go in analysis</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203852):
<p>I realize it's a border case</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203903):
<p>I prefer the name <code>topology</code>  to <code>general_topology</code> for the top level folder</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203938):
<p>unless there are any plans for <code>specific_topology</code> folders at the top level, it's a meaningless distinction which just makes names longer</p>

#### [ Patrick Massot (Jan 15 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155203948):
<p>It's much easier to exclude metric spaces if we call it general topology</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204076):
<p>well it can still mean general topology, I am just objecting to the extra letters</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204154):
<p>In lean 2 there were package .md files for all the subfolders, we could bring that back</p>

#### [ Reid Barton (Jan 15 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204190):
<p>As a maintainer for the topology section of mathlib I volunteer to decide which things are or are not topology</p>

#### [ Patrick Massot (Jan 15 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204197):
<p>Great!</p>

#### [ Patrick Massot (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204223):
<p>I wanted to ask about this new maintainer list: does it mean you have push access?</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204233):
<p>not yet</p>

#### [ Reid Barton (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204255):
<p>(My plan is just to follow the MSC)</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204262):
<p>Leo has to act to make that happen</p>

#### [ Patrick Massot (Jan 15 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204348):
<p>I thought I was elected the documentation dictator, will I get push access?</p>

#### [ Patrick Massot (Jan 15 2019 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204718):
<p>Reid, could you tell us what the file organization would look like then?</p>

#### [ Patrick Massot (Jan 15 2019 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155204783):
<p>I can confirm I can build from scratch here, and Travis is confused</p>

#### [ Reid Barton (Jan 15 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205083):
<p>As a first approximation, I would suggest moving all of <code>analysis</code> to <code>topology</code> except for <code>exponential.lean</code>, <code>normed_space</code> and <code>specific_limits.lean</code>, leaving the directory structure intact</p>

#### [ Reid Barton (Jan 15 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205106):
<p>That doesn't leave much in <code>analysis</code> but I think it's just because we don't have much analysis yet.</p>

#### [ Patrick Massot (Jan 15 2019 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205175):
<p>Isn't this what I had in my first commit?</p>

#### [ Reid Barton (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205231):
<p>Let me check</p>

#### [ Reid Barton (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205298):
<p>As far as the analysis/topology split is concerned, it's exactly the same. (I didn't peek first!)</p>

#### [ Reid Barton (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205407):
<p>So I would just suggest bringing back the <code>topological_space</code> subdirectory and renaming the top-level directory to <code>topology</code> (with the understanding that it really <em>means</em> general topology).</p>

#### [ Reid Barton (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205452):
<p>Oh, except for the <code>instances</code> directory</p>

#### [ Patrick Massot (Jan 15 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205479):
<p>Where would you put those?</p>

#### [ Reid Barton (Jan 15 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205482):
<p>I guess this is a bit awkward, because some of these are also normed spaces. Hmm</p>

#### [ Patrick Massot (Jan 15 2019 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205495):
<p>yes, that's where I started doubting again</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155205991):
<p>I like keeping <code>analysis.real</code> etc where they are</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206015):
<p>unless there is a reason to split the file up into topology and analysis stuff</p>

#### [ Reid Barton (Jan 15 2019 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206097):
<p>Actually it turns out there are no instances related to normed spaces in any of those files. So the whole directory could move to <code>topology</code></p>

#### [ Mario Carneiro (Jan 15 2019 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206180):
<p>I'm okay with that</p>

#### [ Reid Barton (Jan 15 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206254):
<p>The question will be when we define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>L</mi><mi>p</mi></msup></mrow><annotation encoding="application/x-tex">L^p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span></span></span></span></span></span></span></span> spaces and so on which are normed spaces and therefore also have a topology, what do we do. I think we can just stick everything related to those in the <code>analysis</code> directory though.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206275):
<p>I agree, that sounds like analysis to me</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155206299):
<p>the whole construction of the space will be an analysis thing anyway</p>

#### [ Jeremy Avigad (Jan 16 2019 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155222805):
<p>All this sounds good to me. I agree with Mario that <code>topology</code> is better than <code>general_topology</code>.</p>

#### [ Patrick Massot (Jan 16 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20files/near/155237245):
<p>I just renamed general_topology to topology, and moved instances there. Is everybody happy?</p>


{% endraw %}
