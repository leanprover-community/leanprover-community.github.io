---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30186detectingterminalgoals.html
---

## Stream: [general](index.html)
### Topic: [detecting terminal goals](30186detectingterminalgoals.html)

---


{% raw %}
#### [ Scott Morrison (Apr 26 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718057):
<p>I have a little tactic that is meant to determine with the current goal is "terminal", that is, no other goals depend on it.</p>

#### [ Scott Morrison (Apr 26 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718058):
<p>Unfortunately it is not working at the moment.</p>

#### [ Scott Morrison (Apr 26 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718069):
<p>(The idea is just that if you know your current goal is terminal, you can be much more aggressive in discharging it, because nothing can go wrong later.)</p>

#### [ Scott Morrison (Apr 26 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718108):
<p>I currently have</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">metavariables</span> <span class="o">:</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">r</span> <span class="err">←</span> <span class="n">result</span><span class="o">,</span>
   <span class="n">pure</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">e</span> <span class="bp">_</span> <span class="n">l</span><span class="o">,</span>
     <span class="k">match</span> <span class="n">e</span> <span class="k">with</span>
     <span class="bp">|</span> <span class="n">expr</span><span class="bp">.</span><span class="n">mvar</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">insert</span> <span class="n">e</span> <span class="n">l</span>
     <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">l</span>
     <span class="kn">end</span><span class="o">)</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">terminal_goal</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
  <span class="n">do</span> <span class="n">goals</span> <span class="err">←</span> <span class="n">get_goals</span><span class="o">,</span>
     <span class="k">let</span> <span class="n">current_goal</span> <span class="o">:=</span> <span class="n">goals</span><span class="bp">.</span><span class="n">head</span><span class="o">,</span>
     <span class="n">other_goals</span> <span class="err">←</span> <span class="n">metavariables</span><span class="o">,</span>
     <span class="k">let</span> <span class="n">other_goals</span> <span class="o">:=</span> <span class="n">other_goals</span><span class="bp">.</span><span class="n">erase</span> <span class="n">current_goal</span><span class="o">,</span>
     <span class="n">other_goals</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="o">(</span><span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">g</span><span class="o">,</span> <span class="n">d</span> <span class="err">←</span> <span class="n">kdepends_on</span> <span class="n">t</span> <span class="n">current_goal</span><span class="o">,</span>
                                  <span class="n">monad</span><span class="bp">.</span><span class="n">whenb</span> <span class="n">d</span> <span class="err">$</span> <span class="n">pp</span> <span class="n">t</span> <span class="bp">&gt;&gt;=</span> <span class="bp">λ</span> <span class="n">s</span><span class="o">,</span> <span class="n">fail</span> <span class="o">(</span><span class="s2">&quot;This is not a terminal goal: &quot;</span> <span class="bp">++</span> <span class="n">s</span><span class="bp">.</span><span class="n">to_string</span> <span class="bp">++</span> <span class="s2">&quot; depends on it.&quot;</span><span class="o">))</span>
</pre></div>

#### [ Scott Morrison (Apr 26 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718118):
<p>And this works great detecting when the current goal appears in the form <code>?m_1</code> in a later goal.</p>

#### [ Scott Morrison (Apr 26 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718123):
<p>But fails to detect that the current goal appears as something like <code>?m_1[_]</code> in a later goal.</p>

#### [ Scott Morrison (Apr 26 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718134):
<p>Q1. Is this already implemented somewhere, better?</p>

#### [ Scott Morrison (Apr 26 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718136):
<p>Q2. Any suggestions how I fix it?</p>

#### [ Scott Morrison (Apr 26 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718312):
<p>Here's a MWE:</p>
<div class="codehilite"><pre><span></span>private structure D :=
 ( w : ℕ → Type )
 ( x : list (w 0) )

 private def test_terminal_goal : D :=
 begin
    split,
    swap,
    success_if_fail { terminal_goal }, -- succeeds, because terminal_goal correctly fails
    intros,
    success_if_fail { terminal_goal }, -- fails, because terminal_goal incorrectly succeeds
    exact ℕ,
    exact []
 end
</pre></div>

#### [ Simon Hudon (Apr 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125723861):
<p>I think I would do it as:</p>
<div class="codehilite"><pre><span></span>meta def terminal_goal&#39; : tactic unit :=
do g :: gs ← get_goals,
   gs.for_each $ λ g&#39;, guard (g&#39;.occurs g)
</pre></div>


<p>It works with your example but does it work with your use cases?</p>

#### [ Scott Morrison (Apr 27 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125757828):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, this doesn't seem to work in other cases. My tests are here: &lt;<a href="https://gist.github.com/semorrison/5188f3c3e508148657be4d66f4875d8d" target="_blank" title="https://gist.github.com/semorrison/5188f3c3e508148657be4d66f4875d8d">https://gist.github.com/semorrison/5188f3c3e508148657be4d66f4875d8d</a>&gt; if you want to have a look. I have to run now, but will try to decipher why your version isn't working on the other tests later.</p>

#### [ Simon Hudon (Apr 27 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125758036):
<p>Ok, I'll have a look when I wake up :)</p>

#### [ Scott Morrison (Apr 27 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125758093):
<p>I don't really understand the logic of your suggestion: surely you meant <code>guard (¬ g.occurs g')</code> not <code>guard (g'.occurs g)</code>? In any case neither of those work. Sleep well. :-)</p>

#### [ Simon Hudon (Apr 27 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125758109):
<p>Thanks :)</p>

#### [ Scott Morrison (Apr 28 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125804165):
<p>When I see a goal with a "parametrised metavariable" like <code>?m_1[0]</code>, what does the underlying <code>expr</code> look like?  I can't decipher what it should be.</p>

#### [ Scott Morrison (Apr 28 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125804217):
<p>Is it just an <code>app</code> of an <code>mvar</code>?</p>

#### [ Scott Morrison (Apr 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125805155):
<p>Okay --- I've worked this all out. For anyone keeping score:</p>
<div class="codehilite"><pre><span></span>meta def metavariables : tactic (list expr) :=
do r ← result,
   pure (r.fold [] $ λ e _ l,
     match e with
     | expr.mvar _ _ _ := insert e l
     | _ := l
     end)

meta def propositional_goal : tactic unit :=
do goals ← get_goals,
   let current_goal := goals.head,
   current_goal_type ← infer_type current_goal,
   p ← is_prop current_goal_type,
   guard p

meta def subsingleton_goal : tactic unit :=
do goals ← get_goals,
   let current_goal := goals.head,
   current_goal_type ← infer_type current_goal &gt;&gt;= instantiate_mvars,
   to_expr ``(subsingleton %%current_goal_type) &gt;&gt;= mk_instance &gt;&gt; skip

meta def terminal_goal : tactic unit :=
propositional_goal &lt;|&gt; subsingleton_goal &lt;|&gt;
do goals ← get_goals,
   let current_goal := goals.head,
   other_goals ← metavariables,
   let other_goals := other_goals.erase current_goal,
   other_goals.mmap&#39; $ λ g, (do t ← infer_type g, t ← instantiate_mvars t, trace t, d ← kdepends_on t current_goal,
                                monad.whenb d $ pp t &gt;&gt;= λ s, fail (&quot;This is not a terminal goal: &quot; ++ s.to_string ++ &quot; depends on it.&quot;))
</pre></div>

#### [ Simon Hudon (Apr 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806640):
<p>I don't know if you still need the answer but <code>?m_1[0]</code> is a regular meta variable. I think <code>[0]</code>signals the context that the variable can see. I don't know how to decode it though.</p>

#### [ Scott Morrison (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806851):
<p>Thanks <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, all sorted out. <code>?m_1[0]</code> is encoded simply as an application of an <code>mvar</code> on the expressions appearing inside the <code>[ ... ]</code>. It turned out that I was missing an <code>instantiate_mvars</code>, which was preventing successfully detection of these sort of "dependent mvars". I've made a PR for my <code>terminal_goal</code> tactic and some relatives. <a href="https://github.com/leanprover/mathlib/pull/125" target="_blank" title="https://github.com/leanprover/mathlib/pull/125">https://github.com/leanprover/mathlib/pull/125</a></p>

#### [ Simon Hudon (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806862):
<p>Oh, good! Sorry I couldn't help you any more than that</p>

#### [ Simon Hudon (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806864):
<p>You have to be careful with those variables. They sneak up on you</p>

#### [ Scott Morrison (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806959):
<p>I can't believe that I've written code that successfully uses <code>instantiate_mvars</code>. What it actually means is still voodoo to me.</p>

#### [ Simon Hudon (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807129):
<p>I can try to demystify if you like</p>

#### [ Simon Hudon (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807154):
<p>Have you used <code>get_goals</code> and <code>set_goals</code>?</p>

#### [ Scott Morrison (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807155):
<p>Yes, many times!</p>

#### [ Simon Hudon (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807201):
<p>Good! And do you know that <code>get_goals</code> returns a list of expressions that are in fact unassigned meta variables?</p>

#### [ Scott Morrison (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807208):
<p>Yes!</p>

#### [ Scott Morrison (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807213):
<p>(If I were Kevin, I'd be promising to write documentation in exchange for your explanation. :-)</p>

#### [ Simon Hudon (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807272):
<p>(Haha! Where's Kevin when we need him!)</p>
<p>Good. So think of the proof state as being made of two parts (for the sake of this explanation): list of goals which is an arbitrary list of meta variables and the set of all allowed meta variables, some of which are assigned a value.</p>

#### [ Scott Morrison (Apr 28 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807316):
<p>Great!</p>

#### [ Simon Hudon (Apr 28 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807363):
<p>The relationship between the proof state and whatever you're trying to prove is that, when you enter tactic mode, you create an unassigned variable, put it in the list of goals and that variable is in fact the proof that you're supposed to return. From that point on, the assertion you're trying to prove does not matter. Only the variables and the goals do.</p>

#### [ Simon Hudon (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807371):
<p>I don't know if you've ever had that problem but sometimes, you succeed in leaving a tactic block and when you finish the proof, you're told that your proof contains unassigned variables. Does this ring a bell?</p>

#### [ Simon Hudon (Apr 28 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807911):
<p>Long story short, <code>instantiate_mvar</code> finds all the <code>mvar</code> nodes in your expression and, if the meta variable has a value (or type <code>expr</code>) in the proof state it replaces <code>mvar</code> with it. That means that, if you're pattern matching (using <code>match</code>) on an expression and you're looking for <code>expr.app (expr.app (const </code>eq _) e0) e1<code> and that you mean </code>mvar<code> instead, even if that variable is assigned to a value that matches exactly what you're looking for, the pattern matching will fail. That's why it's prudent to use </code>instantiate_mvar<code> before matching on a </code>expr` of which you don't know for sure that it doesn't contain meta variables.</p>

#### [ Simon Hudon (Apr 28 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807919):
<p>I realize my explanation was a bit round about. I just needed to introduce the idea that the life span of meta variables is a whole proof and that it doesn't disappear once it's assigned.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808197):
<p>I see.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808200):
<p>I've encountered needing it in another strange place, as well, which I think matches with your explanation.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808204):
<p>I was writing a tool for finding _all_ the possible rewrites of a given expression by a given rule.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808210):
<p>Unfortunately the built-in rewrite has some problems --- once it has matched some of the parameters of your rewrite rule a particular way, it will subsequently only match the parameters the same way, when looking for further places the rule matches.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808211):
<p>This even persists between different invocations of <code>rewrite_core</code>, because this information is actually stored in the tactic state.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808251):
<p>To solve this, I had to write a tactic <code>lock_tactic_state (t : tactic A) : tactic A</code> which just discards any changes to the tactic state after invocation.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808255):
<p>This throws away any information the tactic state was storing about how rewrite parameters had to match.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808262):
<p>Unfortunately, the proofs that rewrite_core produced where suddenly full of metavariables!</p>

#### [ Scott Morrison (Apr 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808263):
<p>I understand now that this is because these metavariables were _assigned_, but not _instantiated_, so when I discarded the <code>tactic_state</code> those assignments were being lost.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808300):
<p>Calling <code>instantiate_mvars</code> on the proof term, before discarding the state, saved those assignments.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808303):
<p>phew! :-)</p>

#### [ Scott Morrison (Apr 28 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808308):
<p>(Sorry I missed the end  of your explanation; family things happening at this end. I'm going to ping you <span class="user-mention" data-user-id="110026">@Simon Hudon</span> as I expect you'll find this other example interesting.)</p>

#### [ Simon Hudon (Apr 28 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808470):
<p>I'd be curious to see how you implemented <code>lock_tactic_state</code>. Did you deconstruct the tactic value and extract the expected proof?</p>

#### [ Simon Hudon (Apr 28 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808523):
<p>I'm looking forward to your next example. I'll probably see it when I wake up. Incidentally, Australia is way too far! Someone should move it closer to Europe and America, that way our days would overlap!</p>


{% endraw %}
