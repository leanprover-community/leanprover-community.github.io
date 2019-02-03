---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43828Gabrielschallenge.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Gabriel's challenge](https://leanprover-community.github.io/archive/113488general/43828Gabrielschallenge.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 02 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504672):
<p>Can you do Gabriel's exercise?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504673):
<p><a href="#narrow/stream/113488-general/subject/elaborator" title="#narrow/stream/113488-general/subject/elaborator">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/elaborator</a></p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504678):
<p><code> theorem  very_easy : unit = unit :=
by  do exact $ ???</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504679):
<p>Can you make an expr which corresponds to <code>eq.refl unit</code>?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504716):
<p>Talking of tactics reminded me of this.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504720):
<p>I could only make a <code>tactic expr</code></p>

#### [ Simon Hudon (Apr 02 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504727):
<p>Is that against the rules of the game?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504764):
<p>I wasn't sure.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504768):
<p>because I know absolutely nothing about exprs</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504769):
<p>or whether it's possible to make them</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504770):
<p>I thought that <code>eq.refl unit</code> was an expression in Lean</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504776):
<p>but I don't think it has type expr</p>

#### [ Simon Hudon (Apr 02 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504777):
<p>For unit, you could do: <code>do exact $ expr.const ``unit.star []</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504819):
<p>stop at that one</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504820):
<p>that one works</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504824):
<p>were you having a backtick nightmare? ;-)</p>

#### [ Simon Hudon (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504830):
<p>Yeah and I don't have an anti-tick shampoo!</p>

#### [ Simon Hudon (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504832):
<p>How do you escape ticks?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504833):
<div class="codehilite"><pre><span></span>open tactic expr
definition  very_easy : unit :=
by  do exact $ expr.const ``unit.star []
</pre></div>

#### [ Kevin Buzzard (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504835):
<p>result!</p>

#### [ Simon Hudon (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504875):
<p>There should be only one tick before <code>unit.star</code> though</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504876):
<p><code>expr.const</code> wants a <code>name</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504877):
<p>oh we are doing the bad thing which Patrick complained about</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504878):
<p>he wants us to buzz off to another thread</p>

#### [ Simon Hudon (Apr 02 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504883):
<p>Co-opting a channel?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504885):
<p>topic</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504929):
<p>Oh that was clever. I didn't know you could change in the middle</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504937):
<p>So a constructor is a <code>const</code>?</p>

#### [ Simon Hudon (Apr 02 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504939):
<p><span class="emoji emoji-1f601" title="grin">:grin:</span> There's an option to change the topic of everything that comes after a certain post</p>

#### [ Simon Hudon (Apr 02 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504940):
<p>Yes, that's correct</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504979):
<p>so how to change something like eq.refl into an expr?</p>

#### [ Simon Hudon (Apr 02 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504980):
<p>Lean compiles <code>inductive</code> types into constants and axioms</p>

#### [ Simon Hudon (Apr 02 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504989):
<p>Same thing <code>const `eq.refl [`u]</code> ... with the exception of the universe level</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504991):
<p>because then you could use <code>expr.app</code> to apply the function</p>

#### [ Simon Hudon (Apr 02 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505033):
<p>Yes, you would first apply it to a <code>Sort u</code> and then to whatever term you want prove equal to itself</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505039):
<p><code> infer type failed, incorrect number of universe levels</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505040):
<p>woo, new error messages</p>

#### [ Simon Hudon (Apr 02 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505078):
<p>That's curious! I'm pretty sure there should be only one</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505083):
<p>I honestly think that playing around with this sort of thing would be a good introduction to tactics.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505089):
<p>because it gives you the idea of what an expr really is and begins to introduce stuff like the backtick hell before going meta</p>

#### [ Simon Hudon (Apr 02 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505090):
<p>What you can do to see what's wrong is:</p>
<div class="codehilite"><pre><span></span><span class="n">do</span> <span class="n">c</span> <span class="bp">&lt;-</span> <span class="n">mk_const</span> <span class="bp">`</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span><span class="bp">`</span><span class="o">,</span>
   <span class="n">trace</span> <span class="o">(</span><span class="n">c</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Apr 02 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505130):
<p>Interesting! Thanks for the suggestion. I'll add some of that to my tutorial</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505139):
<p>Am I right in thinking that tactics could really be said to be acting on the exprs</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505141):
<p>and that you really have to have some sort of clear idea of what an expr is before moving on to tactics?</p>

#### [ Simon Hudon (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505142):
<p>Yes, that's really the main data structure</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505146):
<p>so everyone has an informal idea of what one is</p>

#### [ Simon Hudon (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505147):
<p>Completely</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505148):
<p>because they have written some Lean code</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505189):
<p>and they are told that they are constructing expressions of certain types</p>

#### [ Simon Hudon (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505190):
<p>And maybe an explanation of what a proof goal is would also help</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505191):
<p>but actually they are not constructing the exprs themselves</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505192):
<p>What is a proof goal?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505193):
<p>There is some "interesting" comment in PIL</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505236):
<p>there it is, p38</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505237):
<p><code>8.5 Metavariables and Unification
[This section is still under construction. It will discuss the notion of a metavariable and
its local context, with the interesting bit of information that goals in the tactic state are
nothing more than metavariables. So the goal list is really just a list of metavariables,
which can help us make sense of the get_goals and set_goals tactics. It will also discuss
the unify tactic.]</code></p>

#### [ Simon Hudon (Apr 02 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505289):
<p>A proof goal is basically an unassigned meta variable. It has no special status. You can think of a proof in tactic mode as creating one metavariable, saying that it's the proof of the main goal and then telling you to assign a value to that metavariable <code>v</code> by calling <code>set_goals [v]</code></p>

#### [ Simon Hudon (Apr 02 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505326):
<p>But you can set any list of unassigned metavariables as the goals in a proof even if they are not relevant.</p>

#### [ Simon Hudon (Apr 02 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505385):
<p>Does that make sense?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505441):
<p>set_goals doesn't make sense, but I can guess what it means.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505442):
<p>so it makes some sort of sense</p>

#### [ Mario Carneiro (Apr 02 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505672):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> To construct an expr, you can use the <code> `(...)</code> syntax</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505679):
<p>There is one backtick and two backticks and three backticks and none of them really make much sense to me</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505680):
<p>I can read the definitions but they don't stick yet</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505681):
<p>I am wondering if playing with exprs like this without thinking about tactics would be a better way to explain how all the backticks work</p>

#### [ Simon Hudon (Apr 02 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505728):
<p>If you want to implement <code>have</code> for example, you could do it this way:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">my_have</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">(</span><span class="n">g</span> <span class="bp">::</span> <span class="n">gs</span><span class="o">)</span> <span class="bp">&lt;-</span> <span class="n">get_goals</span><span class="o">,</span>
   <span class="n">prf</span> <span class="bp">&lt;-</span> <span class="n">mk_meta_var</span> <span class="n">p</span><span class="o">,</span> <span class="c1">-- the side goal</span>
   <span class="n">g&#39;</span> <span class="bp">&lt;-</span> <span class="n">mk_mvar</span><span class="o">,</span> <span class="c1">-- not giving a type, we&#39;ll let `unify` guess it</span>
   <span class="k">let</span> <span class="n">prove_g</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">h</span> <span class="n">binder_info</span><span class="bp">.</span><span class="n">default</span> <span class="n">p</span> <span class="n">g&#39;</span><span class="o">)</span> <span class="n">prf</span><span class="o">,</span>
   <span class="n">unify</span> <span class="n">prove_g</span> <span class="n">g</span><span class="o">,</span>
   <span class="n">set_goals</span> <span class="o">(</span><span class="n">prf</span> <span class="bp">::</span> <span class="n">g&#39;</span> <span class="bp">::</span> <span class="n">gs</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505766):
<p>aah but now you're in tactic mode</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505771):
<p>I was wondering whether one could write something about creating raw exprs without ever mentioning the tactic monad</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505772):
<p>as an introduction to the backtick notation and to exprs</p>

#### [ Simon Hudon (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505774):
<p>Yes, for two reasons: so that we can set and get the goals and so that we can create metavariables that are valid within the scope of the current proof</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505775):
<p>without having to introduce them at the same time as introducing all the tactic monad stuff</p>

#### [ Simon Hudon (Apr 02 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505783):
<p>Oh ... and for unification. Since a meta variable is meaningful only in the context of a specific proof, you need the proof state when you assign a value to one.</p>

#### [ Mario Carneiro (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505822):
<div class="codehilite"><pre><span></span>open tactic
theorem very_easy : unit = unit :=
by do exact `(eq.refl unit)

theorem very_easy₂ : unit = unit :=
by do mk_eq_refl `(unit) &gt;&gt;= exact

theorem very_easy₃ : unit = unit :=
by do exact $
  (expr.const ``eq.refl [level.of_nat 2] : expr)
  (expr.sort $ level.of_nat 1)
  (expr.const ``unit [])
</pre></div>

#### [ Simon Hudon (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505823):
<p>But we're not discharging a goal completely here</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505824):
<p>it was <code>level.of_nat 1</code> I  was missing</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505825):
<p>Thanks Mario.</p>

#### [ Mario Carneiro (Apr 02 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505830):
<p>you can also write <code>level.succ level.zero</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505832):
<p>oh wow there is <code>mk_eq_refl</code></p>

#### [ Simon Hudon (Apr 02 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505873):
<p>Ah! That's the part I didn't think of! you were trying to prove <code>unit = unit</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505874):
<p>I was trying to learn basic stuff about how to build exprs without going into tactic mode</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505879):
<p>no <code>expr.app</code> in version 3?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505880):
<p>what's going on there?</p>

#### [ Mario Carneiro (Apr 02 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505881):
<p>The last example is a bit artifical though, since usually you will not construct a complete expr by hand like that. Here's a half-tactic way to construct it:</p>
<div class="codehilite"><pre><span></span>theorem very_easy₄ : unit = unit :=
by do
  u ← mk_const ``unit,
  e ← mk_app ``eq.refl [u],
  exact e
</pre></div>

#### [ Kevin Buzzard (Apr 02 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505883):
<p>I thought Lean was expecting one expr after the dollar sign and you passed three?</p>

#### [ Simon Hudon (Apr 02 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505924):
<p>It's because of:</p>
<div class="codehilite"><pre><span></span>meta instance : has_coe_to_fun (expr elab) :=
{ F := λ e, expr elab → expr elab, coe := λ e, expr.app e }
</pre></div>

#### [ Mario Carneiro (Apr 02 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505925):
<p><code>expr</code> has a lovely coe_fn instance that allows you to write applications like that</p>

#### [ Mario Carneiro (Apr 02 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505969):
<div class="codehilite"><pre><span></span>theorem very_easy₃&#39; : unit = unit :=
by do exact $
  expr.app (expr.app
    (expr.const ``eq.refl [level.of_nat 2])
    (expr.sort $ level.of_nat 1))
  (expr.const ``unit [])
</pre></div>


{% endraw %}
