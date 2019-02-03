---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/89037TakingtheStacksProjectformalisationforward.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Taking the Stacks Project formalisation forward](https://leanprover-community.github.io/archive/116395maths/89037TakingtheStacksProjectformalisationforward.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Oct 09 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135477612):
<p>I formalised the definition of a scheme -- in theory at least. I proved that an affine scheme was a scheme which gave me some sort of hope that I'd formalised the definition correctly. The files are a mess, some people were never happy with the names of the theorems or the names of the lean files, the whole thing needs a tidy. I have a Masters student who <em>might</em> be interested. What are the priorities here? He'd like to prove some more lemmas about schemes (and indeed we as a department would like to see some original material). But maybe I could use this as impetus to tidy the whole thing up. Does anyone have any ideas about what could be priorities here? <span class="user-mention" data-user-id="110031">@Patrick Massot</span> and <span class="user-mention" data-user-id="112680">@Johan Commelin</span> you probably both have clearer ideas than me about where this project should be going.</p>

#### [ Patrick Massot (Oct 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135477722):
<p>It should be going into mathlib</p>

#### [ Patrick Massot (Oct 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135477729):
<p>with mathlib quality</p>

#### [ Kevin Buzzard (Oct 09 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478190):
<p>I thought you'd say that.</p>

#### [ Patrick Massot (Oct 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478389):
<p>And we also need progress by <span class="user-mention" data-user-id="110087">@Scott Morrison</span> on sheaves</p>

#### [ Kevin Buzzard (Oct 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478391):
<p>A big question here is what to do with the sheaf theory. I defined a sheaf of rings and a presheaf of sets and a sheaf of sets on a basis of a topological space and blah blah blah; do we just sit and wait for more category theory stuff or use the fact that everything is a typeclass so the low-level approach is fine? How long will it be before mathlib contains all the machinery necessary to write "let F be a presheaf of rings on the topological space X" in a category-theory-like manner, so I don't have to also define morphisms of presheaves?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478435):
<p>two minds with a single thought :-)</p>

#### [ Patrick Massot (Oct 09 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135478531):
<p>This is blocking for the perfectoid project as well (also blocked by ring completions, subring issue, etc...)</p>

#### [ Johan Commelin (Oct 09 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481011):
<p>Right. I think those presheaves are pretty close. As soon as <span class="user-mention" data-user-id="110087">@Scott Morrison</span>'s coauthors stop being grumpy, we will get <code>backwards_reasoning</code> and then all sorts of limits. After that a bunch of stuff about sheaves will be within reach.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481109):
<p>I managed just fine in the schemes project with no category theory. Part of me is scared that using the category theory stuff will actually make things more complicated! And unfortunately I must be completely honest and say that I have not been paying careful attention to exactly what is there and what is not there. I know that Scott's work seems to rely on a bunch of automation and I know that these things are very complicated to get right and that I know essentially nothing which would help. I would like to contribute to Scott's work by actually trying it out in some basic cases and then asking for advice when I can't get it to work.</p>
<p>Perhaps going back to the stacks project and doing it all again using the category-theoretic tools that we either have already or will have soon would be a good test case for this category theory stuff. I think that in particular getting the parts of category theory working which are used widely outside of pure category theory would be an important project.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481135):
<p>Golly so we need backwards reasoning and then limits and _then_ sheaves? Because the sheaf axiom says that some map to a limit is an isomorphism?</p>

#### [ Patrick Massot (Oct 09 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481163):
<p>Right, we need someone totally unrelated to GRU to visit Scott's collaborators towns for tourism</p>

#### [ Johan Commelin (Oct 09 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481415):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think we should certainly try to take advantage of category theory. After all, we want étale cohomology next, and then you don't want to have live in a parallel universe where you have no category theory available...</p>

#### [ Patrick Massot (Oct 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481438):
<p>Johan, I cannot allow you to bad mouth Bourbaki</p>

#### [ Johan Commelin (Oct 09 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481489):
<p>What did I say wrong? <span class="emoji emoji-1f630" title="cold sweat">:cold_sweat:</span></p>

#### [ Patrick Massot (Oct 09 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481497):
<p>You don't like living in a parallel universe without category theory</p>

#### [ Johan Commelin (Oct 09 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481512):
<p>Bourbaki never wrote a volume on étale cohomology.</p>

#### [ Patrick Massot (Oct 09 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481575):
<p>Oh, I just received an email from Bourbaki</p>

#### [ Patrick Massot (Oct 09 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481614):
<p>But it's not about category theory</p>

#### [ Johan Commelin (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481632):
<blockquote>
<p>Oh, I just received an email from Bourbaki</p>
</blockquote>
<p>He invites you to give a seminar talk about interactive theorem proving?</p>

#### [ Patrick Massot (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481634):
<p>He wants another seminar talk</p>

#### [ Johan Commelin (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481640):
<blockquote>
<p>He wants another seminar talk</p>
</blockquote>
<p>Congratulations!</p>

#### [ Patrick Massot (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481645):
<p>No, unfortunately it's another topic</p>

#### [ Patrick Massot (Oct 09 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481714):
<p>Hales gave a Bourbaki seminar on proof assistants not so long ago</p>

#### [ Patrick Massot (Oct 09 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481720):
<p>so I don't think they'll want another one before seeing real progress here</p>

#### [ Patrick Massot (Oct 09 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481745):
<p><a href="http://www.bourbaki.ens.fr/seminaires/2014/Prog_juin14.html" target="_blank" title="http://www.bourbaki.ens.fr/seminaires/2014/Prog_juin14.html">http://www.bourbaki.ens.fr/seminaires/2014/Prog_juin14.html</a></p>

#### [ Patrick Massot (Oct 09 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481892):
<p>What's funny is I wanted to write Bourbaki an email asking whether he currently think he left a gap about that completion map thing or whether he claims this is only an ellipsis</p>

#### [ Patrick Massot (Oct 09 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481916):
<p>Of course there is a risk he doesn't remember</p>

#### [ Patrick Massot (Oct 09 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135481945):
<p>he wrote that GT book in 1971</p>

#### [ Johan Commelin (Oct 09 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135482138):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> What does "original" mean for a masters project? Is computing an example enough? Or do we need a new lemma? Because that will be extremely hard to do in Lean.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135482981):
<p>Proving some basic lemmas about schemes and completely fixing up the schemes code is definitely enough.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135482985):
<p>Oh talking of schemes, you're not going to believe this: I've been asked to give a talk on them!</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483047):
<p><a href="http://aitp-conference.org/2019/" target="_blank" title="http://aitp-conference.org/2019/">http://aitp-conference.org/2019/</a> :D</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483058):
<p>So it needs to be fixed up by then!</p>

#### [ Johan Commelin (Oct 09 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483616):
<p>That's nice!</p>

#### [ Johan Commelin (Oct 09 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483634):
<p>So I suggest that this master student turns it into a project to get schemes into mathlib. And then prove the Gamma_Spec adjunction.</p>

#### [ Johan Commelin (Oct 09 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135483666):
<p>Alternatively, define smooth morphisms. Or something like that.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484086):
<p>I'd forgotten about gamma spec adjunction! That's an excellent project</p>

#### [ Kevin Buzzard (Oct 09 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484098):
<p>I never even did locally ringed spaces</p>

#### [ Kevin Buzzard (Oct 09 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484202):
<p>Because spec of a ring is automatically locally ringed and I never defined a morphism of schemes :-)</p>

#### [ Johan Commelin (Oct 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484402):
<p>Right, so we need some category theory (-;</p>

#### [ Johan Commelin (Oct 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135484434):
<p>Another non-trivial but fundamental thing: fibre products of schemes.</p>

#### [ Reid Barton (Oct 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135488955):
<blockquote>
<p>"let F be a presheaf of rings on the topological space X"</p>
</blockquote>
<p>As it happens, we have this specific thing already. Not sure how far that will actually get you though.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposites</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">topological_spaces</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">rings</span>

<span class="kn">open</span> <span class="n">category_theory</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="n">Ring</span><span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Oct 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135489039):
<p>But we can't look at its stalks, right?</p>

#### [ Reid Barton (Oct 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135489043):
<p>except it looks like <code>open_set</code> already has the order reversed for some reason</p>

#### [ Reid Barton (Oct 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135489065):
<p>Right, basically anything past this involves either limits or colimits of some kind.</p>

#### [ Scott Morrison (Oct 09 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135500370):
<p>I'm listening. :-) I've tried once or twice to just make my code on limits not need backwards_reasoning, but it felt pretty painful to me. <code>backwards_reasoning</code> \ <code>back</code> is actually quite close. Simon has ideas to make it efficient, but hopefully an inefficient PR can make it into mathlib if there's a promise we know how to make it fast, later.</p>

#### [ Scott Morrison (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135500456):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, Should I revert <code>open_set</code> to the usual definition? I guess I was just thinking "no one ever uses the forward direction, just the opposite category, lets just cut out the middleman".</p>

#### [ Scott Morrison (Oct 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135500470):
<p>(Perhaps the explicit opposites were causing some pain, but I don't think so.)</p>

#### [ Reid Barton (Oct 09 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135501687):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span>, if the many different shapes of limit are causing some difficulty, I know that I would find it already very helpful to have just general (co)limits. Perhaps it would even be possible to do a version of these before <code>back</code> is merged (I might take another shot at this in a couple of days--I tried to set up a branch with all the limit types but it turned into too much work).</p>

#### [ Reid Barton (Oct 09 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135501770):
<p>Basically everything I want to formalize for locally presentable categories and model categories involves some kind of limits or colimits but a large fraction of it only needs general (co)limits (some other parts do need specific shapes like pushouts).</p>

#### [ Reid Barton (Oct 09 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135501785):
<p>I guess the situation for perfectoid spaces may be similar</p>

#### [ Scott Morrison (Oct 10 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135502648):
<p>Ok, I'll keep that in mind. There are a few missing sections on equalizers and pullbacks, but I was intending to leave those out at first anyway. Really the only thing to do for the PR is deal with the dependency on <code>back</code>.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534437):
<p>getting closer. The new <code>back</code> works fine in my limits code, now it's just a matter of copying and pasting all the sequences of rewrites <code>rewrite_search</code> finds into the source code... :-(</p>

#### [ Scott Morrison (Oct 10 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534445):
<p>It's not like <code>rewrite_search</code> is going to be merged anytime soon. :-)</p>

#### [ Johan Commelin (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534730):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> This copy-pasting should/can be automated.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534746):
<p>Meh... it should be made unnecessary. :-)</p>

#### [ Johan Commelin (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534748):
<p>Anyway, I'm really glad to hear that <code>back</code> is converging to mathlib.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534750):
<p>But okay, I agree.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534765):
<p>I wrote a substitution script that takes coordinates and replacement text and patches up your file.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534766):
<p>We need to learn how to have tactics talk directly to VS Code.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534770):
<p>It is a sort of poor man's diff-patch.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534771):
<p>command line scripts are too messy</p>

#### [ Scott Morrison (Oct 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135534779):
<p>I think Gabriel and Mario were talking about exactly this</p>

#### [ Mario Carneiro (Oct 10 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135560201):
<p>Could <span class="user-mention" data-user-id="110087">@Scott Morrison</span> or someone explain why limits are difficult to formalize or require <code>back</code>? Seems like the basics are just more definitions, and everyone I have seen talking about (co)limits don't seem to expect more than that</p>

#### [ Johan Commelin (Oct 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135560302):
<p>I think it is mostly to make <code>obviously</code> do the right thing as auto_param.</p>

#### [ Johan Commelin (Oct 10 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135560330):
<p>But I'm only guessing.</p>

#### [ Scott Morrison (Oct 11 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135571576):
<p>Yeah, it is mostly me being lame, and not wanting to give up my automation. Sorry for making everyone wait. I made <code>limits.lean</code> itself mathlib ready last night, and as it turned out removing the dependency on <code>rewrite_search</code> was much more painful than removing <code>back</code> would have been.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727023):
<p>I am doing a review of the stacks project code, because this is far more interesting than all the crappy reference letter requests I have piling up and I can now legitimately claim that is part of a work project, because I have an MSc student who is going to work on it and I am speaking about it at AITP 2019.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727025):
<p>Are open immersions of topological spaces in mathlib?</p>

#### [ Kevin Buzzard (Oct 13 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727035):
<p>Basic things such as composition of two open immersions is an open immersion, that sort of thing.</p>

#### [ Patrick Massot (Oct 13 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135727250):
<p>The closest that we almost have is <a href="https://github.com/leanprover-community/mathlib/blob/9d743bbb864234821c4ec881d4dc930ac3631838/analysis/topology/continuity.lean#L401" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/9d743bbb864234821c4ec881d4dc930ac3631838/analysis/topology/continuity.lean#L401">https://github.com/leanprover-community/mathlib/blob/9d743bbb864234821c4ec881d4dc930ac3631838/analysis/topology/continuity.lean#L401</a></p>

#### [ Kevin Buzzard (Oct 16 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135906728):
<p>I want to define a locally ringed space in Lean (or rather get a student to define it). So this is a topological space plus a sheaf of rings plus an axiom about some direct limits (see <a href="https://stacks.math.columbia.edu/tag/01HA" target="_blank" title="https://stacks.math.columbia.edu/tag/01HA">stacks project</a> for more info). I don't see that we have to wait for categories for this to happen. But when categories arrive, will this work somehow be wasted? I am assuming not. I didn't ever define a locally ringed space in the schemes repo, I dodged it, but I think I want to do things more properly this time.</p>

#### [ Reid Barton (Oct 16 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910198):
<p>Well, what work is there? Certainly the bits to do with defining local rings and local ring maps will not be made redundant.</p>

#### [ Reid Barton (Oct 16 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910259):
<p>We already have all the ingredients for presheaves of rings in mathlib.</p>

#### [ Reid Barton (Oct 16 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910412):
<p>There is an oper PR which includes equalizers and products and another WIP one which constructs them for rings, so then you can define sheaves in that language. Johan seemed interested in defining sites for the perfectoid space project, and that seems like a reasonably small amount of effort to "future-proof" sheaves for the zariski topology</p>

#### [ Johan Commelin (Oct 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910505):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think all the category theory will be there before your student has learned enough Lean to start working on this project.</p>

#### [ Reid Barton (Oct 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910520):
<p>I think the remaining bit is to construct directed colimits of rings. Here you probably cannot avoid spending some effort which, eventually, could be superseded by some general machinery on finitary algebraic theories</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910526):
<p>My student is a 4th year joint maths and computing student that spent the summer working with Coq</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910571):
<p>The issue is that he has to learn some commutative algebra</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910634):
<blockquote>
<p>We already have all the ingredients for presheaves of rings in mathlib.</p>
</blockquote>
<p>So what does the definition of a locally ringed space look like now? It's going to be a structure consisting of a topological space, and then a presheaf of rings -- but I shouldn't define this by hand myself now? And then some lemma about a direct limit being local.</p>

#### [ Johan Commelin (Oct 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910706):
<p>Well, stalks are also done by Scott. This should land within a couple of weeks (at most).</p>

#### [ Johan Commelin (Oct 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910719):
<p>So you have to define a ring structure on the stalk. Local rings are already in mathlib.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910833):
<p>Stalks for sheaves of sets I guess?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135910842):
<p>or types in this case</p>

#### [ Johan Commelin (Oct 16 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135911308):
<p>Yes, exactly. That's what I meant with "you have to define a ring structure on the stalk". I really think that this project should try to make schemes mathlib-ready. And as corollary, use all the machinery that is (almost) available.</p>

#### [ Reid Barton (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135912622):
<p>And the fact that you can define a ring structure on the stalk clearly has very little to do with the specific definition of a ring.</p>

#### [ Reid Barton (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135912651):
<p>So if you do it for rings in particular, then in the long run that particular effort is "wasted" (in some sense)</p>

#### [ Scott Morrison (Oct 17 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135944821):
<p>I have no idea what compiles here, but<br>
<a href="https://github.com/semorrison/lean-category-theory/blob/working/src/category_theory/presheaves/locally_ringed.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/working/src/category_theory/presheaves/locally_ringed.lean">https://github.com/semorrison/lean-category-theory/blob/working/src/category_theory/presheaves/locally_ringed.lean</a></p>

#### [ Scott Morrison (Oct 17 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135945243):
<p>Certainly filtered colimits of rings is not done yet, and should be. Your student, Kevin, should do this!</p>

#### [ Mario Carneiro (Oct 17 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135948225):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think that it would be best to do this with categories. Now that they are there, they should be put to some use! I recall you using this as an argument in favor of category theory last time this came up</p>

#### [ Kevin Buzzard (Oct 17 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954315):
<p>I think that when I was trying to write the code last Feb I would just keep saying "look these things are a category" without ever really thinking about what advantage this would actually give me. Here's a concrete question. A locally ringed space is a topological space, a functor from the category of open sets to the category of rings, an axiom about this functor (a statement about the values of the functor on open covers of open sets -- some kernel equals some image) and another axiom about this functor (about direct limits of rings which are values of the functor being local rings). I can write all of that without ever mentioning categories, but the language (functors, direct limits) is everywhere. I am still unclear about what the modern way to define this structure is (independent of my usual confusion about what should be bundled).</p>

#### [ Johan Commelin (Oct 17 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954380):
<p>Kevin, you saw that I could extend a presheaf from a basis in 10 lines. Otoh now I'm struggling with topological bases, and it's a real pain.</p>

#### [ Kevin Buzzard (Oct 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954459):
<p>I am not reading these technical threads carefully right now, I am really snowed under. I write in the beginner threads because those are the only ones where I can understand what's going on easily and quickly. I do remember your post though. And you can do this because you defined a presheaf to be a functor?</p>

#### [ Johan Commelin (Oct 17 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135954738):
<p>I can do this because of all Scott's magic. The automation takes care of a lot of painful noise.</p>

#### [ Kevin Buzzard (Oct 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/135955243):
<p><a href="#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628" title="#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628</a> (for my own reference)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274105):
<p><a href="#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628" title="#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628">presheaf stuff</a></p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274134):
<p>(deleted)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274294):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> it's time that the people at Imperial College began to understand how presheaves work now. <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> is hopefully going to be formalising a locally ringed space soon.</p>

#### [ Ramon Fernandez Mir (Oct 22 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136274857):
<p>Hello, I'm Ramon. I'm doing my Master's project with Kevin and we'll be formalising more parts of the Stacks project. As he said, I'm currently trying to formalise a locally ringed space. I was wondering where I could find the</p>
<blockquote>
<p><a href="#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628" title="#narrow/stream/116395-maths/subject/extend.20presheaf.20from.20basis/near/135546628">presheaf stuff</a></p>
</blockquote>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span></p>

#### [ Johan Commelin (Oct 22 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136279420):
<p><span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> Hi, nice to meet you! I'm pretty busy until next week Wednesday (2 guests are visiting), but after that I hope to return to this stuff. In the mean time I'll keep an I on these threads.</p>

#### [ Kevin Buzzard (Oct 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343084):
<p>So to do locally ringed spaces we need that stalks are local, so we need colimits in the category of commutative rings. If we were doing this in a category free way then I'd know what to do. How does this all work within the category theory framework? This would be a colimit over the set of all open sets containing a fixed point <code>a</code> in a topological space <code>X</code>.</p>

#### [ Reid Barton (Oct 23 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343514):
<p>I assume you also want a specific explicit description of the stalk. So under the current/near future state of category theory in mathlib, I would suggest just doing the "category-free" construction, and then if it seems useful or interesting, also show that what you built is actually a colimit, i.e., fits in a cocone with the expected universal property.</p>

#### [ Reid Barton (Oct 23 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343663):
<p>I guess proving that the stalk is a colimit should help you prove that a morphism of ringed spaces does induce maps on stalks, for example.</p>

#### [ Reid Barton (Oct 23 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136343856):
<p>But given the state of limits right now, "should" in that sentence is more of a design criterion for limits, not an assertion.</p>

#### [ Reid Barton (Oct 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136345079):
<p>Ah, but the <em>input</em> to the construction of a filtered (or directed) colimit of rings should already be in the category theory language.</p>

#### [ Reid Barton (Oct 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136345498):
<p>Let me check what is actually in mathlib so far...</p>

#### [ Reid Barton (Oct 23 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136345838):
<p>I suggest starting from here</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">functor</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">rings</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="c">/-</span><span class="cm"> Copied from https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/filtered.lean -/</span>
<span class="c">/-</span><span class="cm"> Name collides with mathlib `directed`... -/</span>
<span class="n">class</span> <span class="n">directed_preorder</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bound</span> <span class="o">(</span><span class="n">x₁</span> <span class="n">x₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">i₁</span> <span class="o">(</span><span class="n">x₁</span> <span class="n">x₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">x₁</span> <span class="bp">≤</span> <span class="n">bound</span> <span class="n">x₁</span> <span class="n">x₂</span><span class="o">)</span>
<span class="o">(</span><span class="n">i₂</span> <span class="o">(</span><span class="n">x₁</span> <span class="n">x₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">x₂</span> <span class="bp">≤</span> <span class="n">bound</span> <span class="n">x₁</span> <span class="n">x₂</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>

<span class="n">def</span> <span class="n">directed_colimit_of_rings</span> <span class="o">{</span><span class="n">J</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">J</span><span class="o">]</span> <span class="o">[</span><span class="n">directed_preorder</span> <span class="n">J</span><span class="o">]</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">Ring</span><span class="o">)</span> <span class="o">:</span> <span class="n">Ring</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Reid Barton (Oct 23 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346013):
<p>and then also constructing morphisms in <code>Ring</code> from <code>F j</code> to <code>directed_colimit_of_rings F</code>, and checking that these are compatible with the diagram maps <code>F j -&gt; F k</code>, and then also that <code>directed_colimit_of_rings F</code> has the universal property</p>

#### [ Reid Barton (Oct 23 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346088):
<p>(and possibly you want to do filtered colimits instead, though directed ones would be enough for Zariski)</p>

#### [ Reid Barton (Oct 23 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346609):
<p>Then, I would suggest building the indexing category for the colimit "opens containing <code>x</code>" by hand, or possibly using <code>full_subcategory</code>, and check that its opposite category is filtered, and then define <code>stalk x F</code> as the <code>directed_colimit_of_rings</code> of <code>F</code> composed with the inclusion of "opens containing <code>x</code>" in <code>opens X</code></p>

#### [ Reid Barton (Oct 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346750):
<p>Oh, I see that that <code>directed_preorder</code> is missing the <code>inhabited</code> constraint</p>

#### [ Reid Barton (Oct 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136346863):
<p>(I'm also not sure that <code>directed_preorder</code> should really contain data, rather than being a Prop or subsingleton)</p>

#### [ Kevin Buzzard (Oct 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/136348068):
<p>Oh thanks a lot Reid! This is all for <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> who knows a bunch of Coq but is just starting with Lean.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/156927907):
<p>Should it be <code>H : scheme S</code> or <code>S : scheme</code>? In CS language I think this is asking whether schemes should be bundled or unbundled.</p>
<p>Any seasoned algebraic geometer will tell you that whilst the set underlying a scheme is of key technical importance, it does not play a completely central role, unlike the set underlying a group. For example, the set underlying a scheme has a topology on it, but the topology is grotesque -- on an irreducible scheme every non-empty open set is dense, there are typically many non-closed points and so on. One essentially never uses standard useful results from topology on this topological space, a standard way to prove things about schemes is to reduce them to questions about commutative rings and then do some commutative ring theory.</p>
<p>To give another example -- the category of schemes has products, but the underlying set of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>×</mo><mi>T</mi></mrow><annotation encoding="application/x-tex">S\times T</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.13889em;">T</span></span></span></span> is essentially never the product of the underlying sets of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>T</mi></mrow><annotation encoding="application/x-tex">T</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">T</span></span></span></span>. So the kind of typeclass inference instances one sees for products of groups (<code>group G</code> and <code>group H</code> to <code>group (G x H)</code> ) is not correct for schemes.</p>
<p>Is this evidence that schemes should be bundled? I hope I got this the right way round -- I mean put the underlying topological space as a carrier and just have a structure called <code>scheme</code>? Or is the bundle/unbundle issue about other things?</p>
<p>We don't have much bundled stuff in mathlib. My naive understanding of what Cyril and Assia were telling us in Amsterdam was that perhaps if we did then we would begin to understand the power of unification hints. I am still very unclear about the general arguments for and against bundling, my impression is that when I ask a question of this nature the answer is often "try both and see which works best". But if we are to move forward with categories we'd better get the hang of bundling, right?</p>

#### [ Reid Barton (Jan 26 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/156928424):
<p>I would definitely recommend "bundled" (<code>S : scheme</code>)</p>

#### [ Reid Barton (Jan 26 2019 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/156928606):
<p>The underlying set of a scheme is basically never going to have any interesting kind of structure other than that which comes from being a scheme (this is related to the underlying set not commuting with products, so that the underlying set of a group scheme is not a group, etc.)</p>

#### [ Reid Barton (Jan 26 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/156928672):
<p>You can give <code>scheme</code> a <code>has_coe_to_sort</code> instance and write an instance for <code>(S : scheme) : topological_space S</code> so that you can still write <code>p : S</code>, <code>is_open U</code> where <code>U : set S</code>, etc.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Taking%20the%20Stacks%20Project%20formalisation%20forward/near/156928876):
<p><span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> the way I set it up in my schemes repo is perhaps a bad idea. Let's bundle!</p>


{% endraw %}
