---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24083separatedquotient.html
---

## Stream: [maths](index.html)
### Topic: [separated quotient](24083separatedquotient.html)

---


{% raw %}
#### [ Patrick Massot (Sep 30 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134934490):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> why <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L185" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L185">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L185</a> is not an instance?</p>

#### [ Patrick Massot (Sep 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134934537):
<p>Oh! Why this completeness assumption?!</p>

#### [ Patrick Massot (Sep 30 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134934585):
<p>I love doing that with Lean: I removed the assumption and the proof still compiles!</p>

#### [ Johannes Hölzl (Sep 30 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935104):
<p>yeah should be instance</p>

#### [ Kevin Buzzard (Sep 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935220):
<p>Yeah for removing assumptions. You remove them in real life and then have to understand the proof all over again</p>

#### [ Patrick Massot (Sep 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935260):
<p>exactly</p>

#### [ Patrick Massot (Sep 30 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935707):
<p>I just noticed while reviewing my work that this unneeded assumption is simply copy-paste from the previous lemma (where it <em>is</em> needed).</p>

#### [ Patrick Massot (Sep 30 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935788):
<p>Anyway, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> please have a look at <a href="https://github.com/leanprover-community/mathlib/commit/cfb60c52739921a0a9b36bbe2a73400dc2fc372a" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/cfb60c52739921a0a9b36bbe2a73400dc2fc372a">https://github.com/leanprover-community/mathlib/commit/cfb60c52739921a0a9b36bbe2a73400dc2fc372a</a></p>

#### [ Patrick Massot (Sep 30 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935833):
<p>The nonempty quotient stuff will have to move to its proper place but I don't have courage right now (it means recompiling all mathlib since the proper place is very low in the tree).</p>

#### [ Patrick Massot (Sep 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935851):
<p>Kevin: this commit is still work towards ring completions. It's preparation for the isomorphism from <code>completion (separation_quotient a)</code> to <code>completion a</code>.</p>

#### [ Patrick Massot (Sep 30 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935907):
<p>We're getting really close. We may have ring completion tomorrow if I can hide from my secretary and from the head of my department. But first I need to sleep.</p>

#### [ Patrick Massot (Oct 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134954357):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I just noticed that some lemmas from my versions of uniform spaces completions didn't make it through your refactoring. In particular <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L266-L267" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L266-L267">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L266-L267</a> and <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L274" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L274">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L274</a> (I realized I forgot the analogue of the last one for the separation quotient yesterday). Is it on purpose? From a categorical point of view they are crucial.</p>

#### [ Johannes Hölzl (Oct 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134955431):
<p>sorry, both got lost. I will add them</p>

#### [ Patrick Massot (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957496):
<p>It's ok, I can add them back</p>

#### [ Patrick Massot (Oct 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957792):
<p>Just to make sure: Johannes, are you working on this?</p>

#### [ Johannes Hölzl (Oct 01 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957884):
<p>Not yet, I wanted to start now. Do you have some changes?</p>

#### [ Patrick Massot (Oct 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957928):
<p>No, I was about to start <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Patrick Massot (Oct 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957931):
<p>I'll let you do this, and work on the next steps</p>

#### [ Johannes Hölzl (Oct 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957949):
<p>okay</p>

#### [ Patrick Massot (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957952):
<p>Did you pull what I did yesterday?</p>

#### [ Johannes Hölzl (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957962):
<p>One thing I will also change: remove <code>is_ideal'</code>. I don't think it is necessary.</p>

#### [ Johannes Hölzl (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957966):
<p>yes, i just pulled</p>

#### [ Patrick Massot (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957973):
<p>Fine. I was worried that nobody reacted to this <code>is_ideal'</code></p>

#### [ Patrick Massot (Oct 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134958024):
<p>But I hope the topology proof won't become ugly</p>

#### [ Johannes Hölzl (Oct 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134958110):
<p>I hope so, too. That's why I plan to remove it again. If it gets ugly I will add a "constructor" function for <code>is_ideal</code> instead of the additional structure</p>

#### [ Patrick Massot (Oct 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134958121):
<p>Ok, great. I'll stop asking questions and let you work then</p>

#### [ Johannes Hölzl (Oct 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964418):
<p>So I restructured a little bit and replaced the proof for <code>is_ideal (closure _)</code>, by adding nicer rules for membership in <code>closure</code>.</p>

#### [ Patrick Massot (Oct 01 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964465):
<p>I see you pushed while I was writing a link to the previous version :)</p>

#### [ Johannes Hölzl (Oct 01 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964571):
<p>Hehe good. I guess you want to work now on the ring completion without assuming Hausdorff?</p>

#### [ Patrick Massot (Oct 01 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964596):
<p>Yes, and then you'll have the pleasure to refactor it</p>

#### [ Johannes Hölzl (Oct 01 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964669):
<p>No problem. I'm sure it will be in a good state!</p>

#### [ Patrick Massot (Oct 01 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964686):
<p>I'm a bit sad that the proof of <code>ideal_closure</code> is no unrecognizable for mathematicians</p>

#### [ Patrick Massot (Oct 01 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964708):
<p>I don't know why you and Mario don't like equalities between functions.</p>

#### [ Patrick Massot (Oct 01 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964765):
<p>It's really going against main stream mathematics to replace function equality with elements equality everywhere</p>

#### [ Johannes Hölzl (Oct 01 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964766):
<p>No I'm confused. I think it is much more readable than before. We state what kind of steps we proof (is it the zero, add, or mul case) and we say how we proof the membership in the <code>closure</code>. Before it was just a sequence of tactics, not mentioning which case is proved.</p>

#### [ Patrick Massot (Oct 01 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964783):
<p>Category theory tells us that elements are confusing, only arrows matter</p>

#### [ Patrick Massot (Oct 01 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964857):
<p>I agree that stating which case we are proving is nice. What I'm talking about is hiding that the proof key is <code>image_closure_subset_closure_image</code></p>

#### [ Patrick Massot (Oct 01 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964869):
<p>that you've hidden in <code>mem_closure</code></p>

#### [ Patrick Massot (Oct 01 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964887):
<p>also that name is much harder to find than image_closure_subset_closure_image</p>

#### [ Johannes Hölzl (Oct 01 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134966165):
<p>why is it harder to find? You ask, "is there anything to prove membership in <code>closure</code>" then you find it. if you ask: is there anything w.r.t. subset of closure you don't find it. But both are valid. Your proof might be more categorical. But only halfway, you proof something about subsets, not about arrows. You still use <code>closure_mono</code>, instead of arguing about an mono-homomorphism into another type.</p>

#### [ Johannes Hölzl (Oct 01 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134966222):
<p><code>closure</code> is very set based, so for me it doesn't make sense to argue about arrows.</p>

#### [ Patrick Massot (Oct 01 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134970528):
<blockquote>
<p>No problem. I'm sure it will be in a good state!</p>
</blockquote>
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> it's your turn: <a href="https://github.com/leanprover-community/mathlib/commit/b0592fe97e74ef4e9af8158052d30053914d639b" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/b0592fe97e74ef4e9af8158052d30053914d639b">https://github.com/leanprover-community/mathlib/commit/b0592fe97e74ef4e9af8158052d30053914d639b</a></p>

#### [ Patrick Massot (Oct 01 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134970540):
<p>I'm sure you'll find better names <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kevin Buzzard (Oct 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134975072):
<p>I find these conversations very interesting. Patrick is absolutely right from a mathematical point of view. Grothendieck stressed that the arrows were more important than the objects. People talked about geometric objects being smooth but Grothendieck argued that the correct definition was that of a map being smooth, and an object being smooth just meant that the map from this object to the one point set was smooth. On the other hand Johannes thinks about mathematics in a completely different way. Do people properly understand how Grothendieck's ideas should influence type theory?</p>

#### [ Patrick Massot (Oct 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134989929):
<p>Hum, I built a ring structure on the separation quotient of a topological ring, but forgot to prove that it's a <em>topological</em> ring</p>

#### [ Patrick Massot (Oct 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134989951):
<p>I'll need that projection on a quotient group is open</p>

#### [ Patrick Massot (Oct 01 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134989996):
<p>Do we have open maps in mathlib?</p>

#### [ Reid Barton (Oct 01 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134990070):
<p>Don't think so, there's <code>embedding_open</code> I think which says that an embedding of an open subspace is an open map, but just spelled out explicitly.</p>

#### [ Patrick Massot (Oct 01 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134990159):
<p>I'm not sure how to get back the fact that addition on a group quotient group is defined by <code>quotient.lift</code>. Should I <code>dunfold</code> until I see it or is there a better way?</p>

#### [ Chris Hughes (Oct 01 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991135):
<p>use <code>show</code></p>

#### [ Johannes Hölzl (Oct 01 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991253):
<p><code>dsimp</code> could also help.</p>

#### [ Patrick Massot (Oct 01 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991543):
<p>I'm completely lost in our maze of quotient structures. Do we have the quotient of a commutative additive group by a subgroup? Is it related in anyway with quotient rings? Or should I be doing topological modules?</p>

#### [ Johannes Hölzl (Oct 01 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991736):
<p><code>quotient_add_group.add_group</code> (<a href="https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L46" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L46">https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L46</a>)<br>
is for normal subgroups, but as far as I understand a normal subgroup is just a subgroup in the commutative case?</p>

#### [ Patrick Massot (Oct 01 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991739):
<p>yes, every group is normal in this case</p>

#### [ Johannes Hölzl (Oct 01 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991843):
<p>so you can use <code>quotient_add_group</code>?</p>

#### [ Johannes Hölzl (Oct 01 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991886):
<p>Ah there is also <code>quotient_add_group.add_comm_group</code> it is just not setup as an <code>instance</code></p>

#### [ Patrick Massot (Oct 01 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991969):
<p>What about <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L53" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L53">https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L53</a>?</p>

#### [ Patrick Massot (Oct 01 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991981):
<p>It looks good but I haven't managed to use it yet</p>

#### [ Johannes Hölzl (Oct 01 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992188):
<p>Yes, that's it, but the multiplicative version. Afterwards the additive version is derived (line 63). But for the additive version the instance attribute is missing</p>

#### [ Patrick Massot (Oct 01 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992244):
<p>Oh</p>

#### [ Patrick Massot (Oct 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992526):
<p>Now it seems to work without the attribute, strange...</p>

#### [ Johannes Hölzl (Oct 01 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992763):
<p>maybe its somewhere else?</p>

#### [ Patrick Massot (Oct 01 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992978):
<p>I need to stop for today, but at least I have some statement:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">topological_add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_subgroup</span> <span class="n">N</span><span class="o">]:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">quotient_add_group</span><span class="bp">.</span><span class="n">quotient</span> <span class="n">N</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dunfold</span> <span class="n">quotient_add_group</span><span class="bp">.</span><span class="n">quotient</span> <span class="bp">;</span> <span class="n">apply_instance</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">topological_add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_subgroup</span> <span class="n">N</span><span class="o">]:</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">quotient_add_group</span><span class="bp">.</span><span class="n">quotient</span> <span class="n">N</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">continuous_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Oct 01 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134993038):
<p>I wasn't able to get to the point where I can simply use continuity of lifts of continuous functions</p>

#### [ Johannes Hölzl (Oct 02 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135019838):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  fyi, I rebased the branch. So pull the new branch before continuing on it.</p>

#### [ Patrick Massot (Oct 03 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135113983):
<p>I tried to return to this topological quotient group, but I still have no idea how to unfold the definition of addition on the quotient. It uses a mysterious <code>quotient.lift_on2'</code> that I can't reach, even using change. The MWE is:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>
<span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">quotient_group</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">[</span><span class="n">topological_add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_subgroup</span> <span class="n">N</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">topological_add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_subgroup</span> <span class="n">N</span><span class="o">]:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">quotient_add_group</span><span class="bp">.</span><span class="n">quotient</span> <span class="n">N</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dunfold</span> <span class="n">quotient_add_group</span><span class="bp">.</span><span class="n">quotient</span> <span class="bp">;</span> <span class="n">apply_instance</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">quotient_add_group</span><span class="bp">.</span><span class="n">quotient</span> <span class="n">N</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">continuous_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 03 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114738):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Do you have a strategy in mind?</p>

#### [ Johan Commelin (Oct 03 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114755):
<p>Which ingredients would you want to apply?</p>

#### [ Johan Commelin (Oct 03 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114869):
<p>My guess would be that you first need to turn the addition into a map <code>quot × quot → quot</code>, then identify <code>quot × quot</code> with an appropriate quotient. And then apply some lemma about the universal property of quotients and continuous maps</p>

#### [ Johan Commelin (Oct 03 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114874):
<p>Of course this is very vague...</p>

#### [ Johannes Hölzl (Oct 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135115571):
<p>So, <code>quotient.lift_on2'</code> is just  <code>quotient.lift_on2</code> using a implicit parameter instead of a type class parameter. If this helps...</p>

#### [ Reid Barton (Oct 03 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135118401):
<p>I think the math strategy is to start with a commutative square involving the multiplication <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>×</mo><mi>G</mi><mo>→</mo><mi>G</mi></mrow><annotation encoding="application/x-tex">G \times G \to G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">G</span><span class="mbin">×</span><span class="mord mathit">G</span><span class="mrel">→</span><span class="mord mathit">G</span></span></span></span> and the multiplication <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi><mo>×</mo><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi><mo>→</mo><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">G/H \times G/H \to G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span><span class="mbin">×</span><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span><span class="mrel">→</span><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span>. Right?</p>

#### [ Reid Barton (Oct 03 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135118531):
<p>Where the vertical maps are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi><mo>×</mo><mi>q</mi></mrow><annotation encoding="application/x-tex">q \times q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.7777700000000001em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi></mrow><annotation encoding="application/x-tex">q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi><mo>:</mo><mi>G</mi><mo>→</mo><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">q : G \to G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span><span class="mrel">:</span><span class="mord mathit">G</span><span class="mrel">→</span><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span> is the quotient map. I think the fact that that square commutes is a definitional equality (for each pair <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><msub><mi>g</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>g</mi><mn>2</mn></msub><mo>)</mo><mo>∈</mo><mi>G</mi><mo>×</mo><mi>G</mi></mrow><annotation encoding="application/x-tex">(g_1, g_2) \in G \times G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">)</span><span class="mrel">∈</span><span class="mord mathit">G</span><span class="mbin">×</span><span class="mord mathit">G</span></span></span></span>). So you should not have to unfold the definition of the product in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span> if that is correct.</p>

#### [ Chris Hughes (Oct 03 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135118773):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> the fact that <code>quotient_group.mk</code> is a <code>group_hom</code> should mean that you don't need to unfold mul. The proof that it is a <code>group_hom</code> is just <code>rfl</code> anyway, so everything's definitionally equal to what you want it to be.</p>

#### [ Reid Barton (Oct 03 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135119108):
<p>The point is that the multiplication on the quotient is ultimately defined in terms of <code>quot.lift</code>, and <code>quot.lift</code> applied to something made from <code>quot.mk</code> reduces.</p>

#### [ Johan Commelin (Oct 03 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135119477):
<p>Ok, so first of all we need to know that the quotient map is ctu. Is this already there?</p>

#### [ Reid Barton (Oct 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135120140):
<p>Assuming "ctu" = continuous then <code>continuous_quot_mk</code></p>

#### [ Reid Barton (Oct 03 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135120393):
<p>By the way, this one is not simply a formal consequence of the universal property of the quotient, because the product of two quotient maps is not in general a quotient map (although in this case I guess it probably is)</p>

#### [ Reid Barton (Oct 03 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135120428):
<p>For <code>continuous_neg</code>, you can argue along those lines.</p>

#### [ Patrick Massot (Oct 03 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135124484):
<p>Sorry, I was away. Indeed the quotient projection is continuous, and addition is continuous, so I want to use <a href="https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L811" target="_blank" title="https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L811">https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L811</a> applied to <a href="http://quotient.mk" target="_blank" title="http://quotient.mk">quotient.mk</a> \circ addition. My problem is to get Lean to swallow that</p>

#### [ Patrick Massot (Oct 03 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135124910):
<p>oh maybe I misunderstood. Do you mean I could use <a href="https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L383" target="_blank" title="https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L383">https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L383</a>?</p>

#### [ Patrick Massot (Oct 03 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135124969):
<p>lemma quotient_map.continuous_iff {f : α → β} {g : β → γ} (hf : quotient_map f) : continuous g ↔ continuous (g ∘ f)</p>

#### [ Patrick Massot (Oct 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135125165):
<p>I'm waiting for mathlib to compile...</p>

#### [ Chris Hughes (Oct 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135125502):
<p>Is <code>continuous_quot_mk</code> the right <code>quot_mk</code>? I see no mention of groups anywhere around it</p>

#### [ Patrick Massot (Oct 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135125527):
<p>The topology on the quotient group is the quotient topology (I hope)</p>

#### [ Reid Barton (Oct 03 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127345):
<p>You can't use <code>continuous_quotient_lift</code> or <code>quotient_map.continuous_iff</code> because <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi><mo>×</mo><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">G/H \times G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span><span class="mbin">×</span><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span> is not (obviously) a quotient of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>×</mo><mi>G</mi></mrow><annotation encoding="application/x-tex">G \times G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">G</span><span class="mbin">×</span><span class="mord mathit">G</span></span></span></span></p>

#### [ Reid Barton (Oct 03 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127429):
<p>I thought you were doing the proof which goes like: <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi></mrow><annotation encoding="application/x-tex">q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> is an open map (because <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>q</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>q</mi><mo>(</mo><mi>U</mi><mo>)</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">q^{-1}(q(U))</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">q</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">q</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span><span class="mclose">)</span></span></span></span> is a union of translates of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span>, hence open), so <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi><mo>×</mo><mi>q</mi></mrow><annotation encoding="application/x-tex">q \times q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.7777700000000001em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> is an open map, and then you can check that the preimage of an open subset of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span> under multiplication is again open by chasing around the square</p>

#### [ Patrick Massot (Oct 03 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127544):
<p>Indeed this is what I wanted to do the other day (I even asked whether we have a definition of open maps in mathlib) and then I forgot what I was doing...</p>

#### [ Patrick Massot (Oct 03 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127598):
<p>But I guess the map from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>×</mo><mi>G</mi></mrow><annotation encoding="application/x-tex">G \times G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">G</span><span class="mbin">×</span><span class="mord mathit">G</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi><mo>×</mo><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">G/H \times G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span><span class="mbin">×</span><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span> should still be a quotient map</p>

#### [ Patrick Massot (Oct 03 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127616):
<p>I need to think on paper</p>

#### [ Patrick Massot (Oct 03 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135128893):
<p>I decided that every proof will need to first prove that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>→</mo><mi>G</mi><mi mathvariant="normal">/</mi><mi>H</mi></mrow><annotation encoding="application/x-tex">G \to G/H</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mrel">→</span><span class="mord mathit">G</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.08125em;">H</span></span></span></span> is open anyway.</p>

#### [ Kenny Lau (Oct 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135128980):
<p>why do I feel like I've proved that</p>

#### [ Patrick Massot (Oct 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135128997):
<p>I'd be very interested</p>

#### [ Patrick Massot (Oct 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129011):
<p>Do you remember if this is in mathlib?</p>

#### [ Kenny Lau (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129246):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">topological_group</span><span class="bp">.</span><span class="n">coinduced</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>
  <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">group</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">hf1</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">surjective</span> <span class="n">f</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hf2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">S</span><span class="o">)))</span> <span class="o">:</span>
  <span class="n">topological_group</span> <span class="n">β</span> <span class="o">:=</span>
</pre></div>


<p><code>hf2</code> seems to say that it is an open map</p>

#### [ Kenny Lau (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129261):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">quotient_group</span><span class="bp">.</span><span class="n">topological_group</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
  <span class="o">[</span><span class="n">topological_group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">normal_subgroup</span> <span class="n">N</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">topological_group</span> <span class="o">(</span><span class="n">left_cosets</span> <span class="n">N</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">left_rel</span> <span class="n">N</span><span class="bp">;</span> <span class="k">from</span>
<span class="n">topological_group</span><span class="bp">.</span><span class="n">coinduced</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exists_rep</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">S</span> <span class="n">hs</span><span class="o">,</span>
<span class="k">have</span> <span class="o">(</span><span class="err">⋃</span> <span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">},</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">S</span><span class="o">)</span>
    <span class="bp">=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="err">&#39;&#39;</span> <span class="n">S</span><span class="o">),</span>
  <span class="k">from</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">z</span><span class="o">,</span>
  <span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">S</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">g</span> <span class="bp">*</span> <span class="n">z</span><span class="o">,</span> <span class="n">h2</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span><span class="o">,</span> <span class="n">h1</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">]</span><span class="bp">;</span>
    <span class="k">from</span> <span class="n">quotient_group</span><span class="bp">.</span><span class="n">is_group_hom</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">g</span> <span class="bp">*</span> <span class="n">z</span><span class="bp">⁻¹</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span><span class="o">,</span> <span class="n">h2</span><span class="o">,</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">inv</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span><span class="o">,</span> <span class="n">mul_inv_self</span><span class="o">]</span><span class="bp">;</span>
    <span class="n">repeat</span> <span class="o">{</span> <span class="k">from</span> <span class="n">quotient_group</span><span class="bp">.</span><span class="n">is_group_hom</span> <span class="bp">_</span> <span class="o">}</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h1</span><span class="o">]</span><span class="bp">⟩⟩</span><span class="o">,</span>
<span class="n">this</span> <span class="bp">▸</span> <span class="n">is_open_Union</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">},</span>
<span class="n">continuous_mul</span> <span class="n">continuous_const</span> <span class="n">continuous_id</span> <span class="bp">_</span> <span class="n">hs</span><span class="o">)</span>
</pre></div>


<p>so this consistutes a proof</p>

#### [ Kenny Lau (Oct 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129329):
<p><a href="https://github.com/kckennylau/local-langlands-abelian/blob/master/src/topological_group.lean#L205-L221" target="_blank" title="https://github.com/kckennylau/local-langlands-abelian/blob/master/src/topological_group.lean#L205-L221">https://github.com/kckennylau/local-langlands-abelian/blob/master/src/topological_group.lean#L205-L221</a></p>

#### [ Kenny Lau (Oct 03 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129383):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> is this what you want?</p>

#### [ Patrick Massot (Oct 03 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129407):
<p>it looks very much like what I want</p>

#### [ Kenny Lau (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129453):
<p>nice</p>

#### [ Patrick Massot (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129455):
<p>I mean the statement of course</p>

#### [ Kenny Lau (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129475):
<p>I mean, it's not hard to prove</p>

#### [ Patrick Massot (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129481):
<p>the proof...</p>

#### [ Kenny Lau (Oct 03 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129505):
<p>a first year could learn that</p>

#### [ Patrick Massot (Oct 03 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129530):
<p>the math proof is easy yes</p>

#### [ Patrick Massot (Oct 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129603):
<p>reading a term mode proof is hard (for me)</p>

#### [ Kenny Lau (Oct 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129613):
<p>this proof is 3 months old btw</p>

#### [ Patrick Massot (Oct 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129722):
<p>I will need to redo it in my context and state intermediate lemmas for reuse anyway</p>

#### [ Patrick Massot (Oct 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129734):
<p>but it's still helpful to have one full proof</p>

#### [ Kenny Lau (Oct 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129752):
<p>ok</p>

#### [ Patrick Massot (Oct 03 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129831):
<p>thanks!</p>

#### [ Patrick Massot (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129991):
<p>Did you think about PRing stuff from this repo?</p>

#### [ Kenny Lau (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135130001):
<p>maybe</p>

#### [ Patrick Massot (Oct 03 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135130577):
<p>Remember your work is lost if you don't PR it</p>

#### [ Kevin Buzzard (Oct 04 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135155155):
<p>The first key thing we need from Kenny's repo is algebraic closure, and it's not in there yet. Kenny is waiting for module refactoring because the argument needs loads of ideals over loads of rings.</p>

#### [ Kevin Buzzard (Oct 04 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135155166):
<p>After that we need to take a level-headed look at how much is appropriate for mathlib and how much really just a wacky independent project</p>

#### [ Kevin Buzzard (Oct 04 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135155170):
<p>(and I don't know what the conclusion will be)</p>


{% endraw %}
