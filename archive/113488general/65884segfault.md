---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65884segfault.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [segfault](https://leanprover-community.github.io/archive/113488general/65884segfault.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rob Lewis (Aug 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131243767):
<p>I just managed to crash Lean, and realized it's been quite a while since the last time!</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">wlog</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">wlog</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span> <span class="kn">using</span> <span class="o">[</span><span class="n">x</span> <span class="n">x</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Aug 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131243856):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> This isn't really your problem in the end, but maybe it's possible to work around in <code>wlog</code>?</p>

#### [ Kevin Buzzard (Aug 10 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131244268):
<p>Oh nice! I absolutely agree -- Lean has been super-stable since they fixed some memory leak several months ago, it's been a joy to use. I do get the occasional segfault, almost always because my input file is garbage (e.g. I'm deleting hundreds of lines of a file and Lean just started to read a file which starts in the middle of a proof, or possibly even the middle of a word), and furthermore I've never been able to reproduce. It's very rare to get a reproducible segfault nowadays. I can reproduce here BTW.</p>

#### [ Mario Carneiro (Aug 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833394):
<p>Found it</p>
<div class="codehilite"><pre><span></span>open tactic
example (x : ℕ) : true :=
by do x ← get_local `x, revert_lst [x, x]
</pre></div>

#### [ Mario Carneiro (Aug 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833409):
<p>don't revert the same variable twice, I guess</p>

#### [ Kevin Buzzard (Aug 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833419):
<p>I remember my mother telling me that as a child</p>

#### [ Mario Carneiro (Aug 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833424):
<p>note that using <code>revert x</code> twice causes a regular error in the second call</p>

#### [ Kevin Buzzard (Aug 10 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833506):
<p><code>revert_lst</code> has no docstring :-(</p>

#### [ Mario Carneiro (Aug 10 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833511):
<p>presumably it reverts a list</p>

#### [ Kevin Buzzard (Aug 10 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833614):
<p>or a <code>lst</code></p>

#### [ Simon Hudon (Aug 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131842254):
<blockquote>
<p>don't revert the same variable twice, I guess</p>
</blockquote>
<p>I'll do what I want!</p>

#### [ Kevin Buzzard (Sep 06 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133463161):
<p>another wloggy segfault:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">wlog</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">):</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">wlog</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">m</span><span class="o">,</span> <span class="c1">-- segv</span>
<span class="kn">end</span>
</pre></div>


<p>(as you can guess this is the first time I used wlog, I was just trying things out)</p>

#### [ Simon Hudon (Sep 06 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133463196):
<p>Dang! I don't remember putting segfault as one of the features</p>

#### [ Simon Hudon (Sep 06 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133463264):
<p>Can you edit the <code>mathlib</code> sources?</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464351):
<p>fixed</p>

#### [ Simon Hudon (Sep 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464363):
<p>What was the issue?</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464406):
<p>it triggered the <code>x &lt;= y</code> special case and assumed <code>n + n</code> was a variable</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464424):
<p>I am not sure what happened after that, but possibly this got passed into <code>revert</code></p>

#### [ Mario Carneiro (Sep 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464482):
<p>that's what caused the last segfault, at least</p>

#### [ Simon Hudon (Sep 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464486):
<p>I see. That was not a source of segfault I thought of</p>

#### [ Simon Hudon (Sep 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464510):
<p>Did you add Kevin's example to the test suite?</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464520):
<p>I think <code>wlog</code> parsing is currently way too complicated. It should be broken up and documented</p>

#### [ Simon Hudon (Sep 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464532):
<p>That makes sense, I really don't understand the tactic anymore.</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464737):
<p>This test fails now:</p>
<div class="codehilite"><pre><span></span>example {x y z : ℕ} : true :=
begin
  suffices : false, trivial,
  wlog h : x ≤ y + z,
  { guard_target x ≤ y + z ∨ x ≤ z + y,
    admit },
  { guard_hyp h := x ≤ y + z,
    guard_target false,
    admit }
end
</pre></div>


<p>what the heck is this supposed to do?</p>

#### [ Simon Hudon (Sep 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464783):
<p>Can you show the state right after <code>wlog</code>?</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464784):
<p>it fails</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464841):
<p>the error is <code>To generate cases at least two permutations are required, i.e. `using [x y, y x]` or exactly 0 or 2 variables</code> but the problem is that the given pattern <code>x ≤ y + z</code> has 3 variables</p>

#### [ Simon Hudon (Sep 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464866):
<p>It tries to prove false just to make sure that no call to <code>trivial</code> or assumption finishes the goal before we can see the result</p>

#### [ Simon Hudon (Sep 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464900):
<p>Ah I see. That's from when we only considered two variables</p>

#### [ Simon Hudon (Sep 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464914):
<p>It guessed <code>x</code> and <code>y</code>.</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464971):
<p>My question is, what is this supposed to do in the first place? It used to just take the last two variables and permute them, as you can see from the asserted target</p>

#### [ Simon Hudon (Sep 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464977):
<p>I'm surprised it hasn't failed before</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464999):
<p>It was previously just matching the list of variables against <code>(x :: y :: _)</code> i.e. &gt;= 2 vars, take the first 2</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465010):
<p>I changed this to <code>[x, y]</code> and now this test fails</p>

#### [ Simon Hudon (Sep 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465041):
<p>Why are you changing it to <code>[x,y]</code>?</p>

#### [ Simon Hudon (Sep 06 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465126):
<p>You were the one suggesting we guess the last two variables of the pattern.</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465136):
<p>No, that's what it was doing before I touched it</p>

#### [ Mario Carneiro (Sep 06 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465154):
<p>I don't understand why the code is written that way, but there is a test asserting this behavior</p>

#### [ Simon Hudon (Sep 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465303):
<p>I'm looking at master right now and what I see is <code>(x :: y :: _)</code>, not <code>[x, y]</code></p>

#### [ Mario Carneiro (Sep 06 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465862):
<p><a href="https://github.com/leanprover/mathlib/blob/master/tactic/wlog.lean#L203" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/wlog.lean#L203">https://github.com/leanprover/mathlib/blob/master/tactic/wlog.lean#L203</a></p>

#### [ Simon Hudon (Sep 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466307):
<p>My mistake, I must have done something wrong</p>

#### [ Simon Hudon (Sep 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466314):
<p>What happens if you switch it back to <code>(x :: y :: _)</code>?</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466399):
<p>then it works, although the behavior in that case is peculiar</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466434):
<p>it just permutes the last two variables discovered in the term, which is a bit weirdly nondeterministic</p>

#### [ Simon Hudon (Sep 06 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466559):
<p>What would you expect it to do in this case?</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466711):
<p>fail, or do all permutations of the n variables</p>

#### [ Johan Commelin (Sep 06 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466801):
<p>permutations are now in mathlib. Does that help?</p>

#### [ Johan Commelin (Sep 06 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466835):
<p>Ooh, wait. They were already for a long time... it is the signs that are new.</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466842):
<p>we already had <code>list.permutations</code></p>

#### [ Simon Hudon (Sep 06 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467037):
<p>I'm not sure if you recall but we have had that conversation before. You were in favor of guessing the variables, I was in favor of requiring that the user specify them</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467099):
<p>Actually both options are available here</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467319):
<p>honestly I have no idea why it's so complicated. 2 variables seems to be special cased in the parsing, so <code>wlog h : x ≤ y + z using x y z</code> just fails (previously it would just permute <code>x</code> and <code>y</code>)</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467406):
<p>Part of the problem is that I don't know the specification of the tactic, and the code is so ad hoc it's hard to tell what is intended and what is accident</p>

#### [ Simon Hudon (Sep 06 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467904):
<p>It's probably that I started it intending to support only two variables and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> probably didn't want to disturb too much</p>

#### [ Simon Hudon (Sep 06 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467916):
<p>Do you want to settle on a specification now?</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467987):
<p>I'm trying to get one out of the docstring now</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133468471):
<p>There are I guess 24 combinations resulting from the parse:</p>
<div class="codehilite"><pre><span></span>wlog h? (: pat)? (:= r)? (using x y z)?
wlog h? (: pat)? (:= r)? (using [x y z, z y x])?
</pre></div>


<ul>
<li><code>h</code> is just a name. If it is omitted, the default name is <code>case</code> (Although from the code it looks like if <code>r</code> is the name of a local constant then it is renamed to <code>h</code>?)</li>
</ul>

#### [ Mario Carneiro (Sep 06 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133468600):
<ul>
<li>If <code>pat</code> and <code>r</code> are both omitted there is an error</li>
<li>If <code>pat</code> is given but not <code>r</code> it becomes a subgoal</li>
<li>If <code>r</code> is given but not <code>pat</code> it is reconstructed as the first disjunct of <code>r</code>'s type</li>
</ul>

#### [ Mario Carneiro (Sep 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133468776):
<ul>
<li>If <code>using</code> list is omitted it is inferred as the set of distinct variables in <code>pat</code></li>
<li>If <code>using</code> is a list of variables then all permutations of those variables are considered</li>
<li>If <code>using</code> is a nonempty list of permutations then the first permutation is considered as the list of variables (and the rest must actually be permutations)</li>
<li>If <code>using</code> is an empty list of permutations it is treated as omitted</li>
</ul>

#### [ Mario Carneiro (Sep 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469008):
<p>Oh, I think this is the justification for the last two variables thing:</p>
<div class="codehilite"><pre><span></span>(4) `wlog : R x y using x y` and `wlog : R x y`
  Produces the case `R x y ∨ R y x`. If `R` is ≤, then the disjunction discharged using linearity.
  If `using x y` is avoided then `x` and `y` are the last two variables appearing in the
  expression `R x y`. -/
</pre></div>

#### [ Simon Hudon (Sep 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469052):
<p>Yes, I think that was the entirety of the docstring before Johannes worked on <code>wlog</code></p>

#### [ Mario Carneiro (Sep 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469109):
<p>I guess this is to allow for when the relation is itself parameterized in some variables</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469133):
<p>I wonder whether we can use type information to eliminate some permutations</p>

#### [ Simon Hudon (Sep 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469134):
<p>I think we can map those notations to a set of core parameters. Sometimes they are specified by the user, sometimes they have to be guessed. Working from there, we should say how they are guessed and what is done with those core parameters.</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469179):
<p>There is already a notion of core parameters, I think, which are used in <code>tactic.wlog</code> (noninteractive)</p>

#### [ Simon Hudon (Sep 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469201):
<p>Ah good so now we're only struggling with parsing / guessing</p>

#### [ Simon Hudon (Sep 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469273):
<p>Actually <code>R x y</code> was just a way of writing <code>x ≤ y</code> while not involving a specific relation.</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469274):
<p>Right, the parser is the behemoth</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469287):
<p>I think there was some example where a relation like <code>x = y [mod n]</code> came up</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469307):
<p>but even <code>has_le.le</code> can use variables, like the type or instance - we don't want to permute these</p>

#### [ Simon Hudon (Sep 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469395):
<p>That's true</p>

#### [ Mario Carneiro (Sep 06 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469448):
<p>I was thinking we can use permutations for which the permuted relation is well typed, but this has exponential growth for large relations</p>

#### [ Mario Carneiro (Sep 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469562):
<p>Alternatively, we can require that permuted variables have the same type as each other, but maybe there are counterexamples where you permute a&lt;-&gt;b and c&lt;-&gt;d where <code>c : T a</code> and <code>d : T b</code></p>

#### [ Mario Carneiro (Sep 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469606):
<p>then again, in this case you will certainly be providing the permutation list explicitly so we don't have to guess it</p>

#### [ Mario Carneiro (Sep 06 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133470142):
<p>actually, <code>tactic.wlog</code> is also doing some fancy footwork, and it has no segfault protection of its own</p>

#### [ Mario Carneiro (Sep 06 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133470276):
<p>The signature is</p>
<div class="codehilite"><pre><span></span>meta def wlog (vars&#39; : list expr) (h_cases fst_case : expr) (perms : list (list expr)) : tactic unit
</pre></div>


<p>where <code>vars'</code> is the set of variables being permuted, <code>h_cases</code> is a local constant with the proof of the disjunction, <code>fst_case</code> is the pattern (with variables in the same order as the first permutation), and <code>perms</code> is a list of permutations of <code>vars'</code></p>

#### [ Kevin Buzzard (Sep 06 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471151):
<p>Is there a case for splitting off the case of two variables and having two tactics? What I actually want to do is <code>wlog degree f ≤ degree g</code>. Is that not possible? (my goal is symmetric in the polynomials <code>f</code> and <code>g</code>).</p>

#### [ Mario Carneiro (Sep 06 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471336):
<p>It is possible, indeed the default behavior of wlog should do what you want</p>

#### [ Mario Carneiro (Sep 06 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471354):
<p>if not, just put <code>using f g</code> at the end</p>

#### [ Mario Carneiro (Sep 06 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471434):
<p>This example blows my mind:</p>
<div class="codehilite"><pre><span></span>  have h : p n i ∨ p i m ∨ p m i, from sorry,
  wlog : p n i := h using n m i,
</pre></div>


<p>It infers the permutation list <code>[n m i, i m n, m i n]</code></p>

#### [ Mario Carneiro (Sep 06 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471727):
<p>Oh! The example (and tactic) is actually broken, the test doesn't actually finish the proof so it doesn't notice</p>

#### [ Simon Hudon (Sep 06 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133472124):
<p>It's sometimes baffling how much we can live with bugs in proof tactics</p>


{% endraw %}
