---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/41672fullnames.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [full names](https://leanprover-community.github.io/archive/113488general/41672fullnames.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 17 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832050):
<p>Is there a way to ask Lean to list all fully qualified names (I mean including namespaces) defined by a particular file? I'd like to check I didn't messed up with name spaces</p>

#### [ Simon Hudon (Jul 17 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832621):
<p>The way I would do it is I would write a command in a <code>run_cmd</code> block and use <code>environment.fold</code> to iterate over all the visible declarations, get their names and use <code>environment.in_current_file</code> to filter out any declaration that comes from outside. It will give you a list of fully qualified names.</p>

#### [ Simon Hudon (Jul 17 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832647):
<p>Oh, and in a tactic, you use  <code>get_env</code> to get the current environment.</p>

#### [ Patrick Massot (Jul 17 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832672):
<p>Thanks Simon, but I'm afraid you assume too much knowledge from me.</p>

#### [ Simon Hudon (Jul 17 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832755):
<p>No worries, I like starting with a brief overview but I'm happy to go step by step with you if need be.</p>

#### [ Simon Hudon (Jul 17 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832776):
<p>Let's start with a script that just prints all the visible names (even the ones from other files).</p>

#### [ Simon Hudon (Jul 17 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832960):
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="bp">&lt;-</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span> <span class="c1">-- this loops over all the visible declarations and, using `list.cons`, accumulate them in a list</span>
   <span class="k">let</span> <span class="n">names</span> <span class="o">:=</span> <span class="n">decls</span><span class="bp">.</span><span class="n">map</span> <span class="n">declaration</span><span class="bp">.</span><span class="n">to_name</span><span class="o">,</span> <span class="c1">-- this takes the name of each declaration.</span>
   <span class="n">trace</span> <span class="n">names</span>
</pre></div>

#### [ Simon Hudon (Jul 17 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832979):
<p>Does it make sense so far?</p>

#### [ Patrick Massot (Jul 17 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833046):
<p>It makes sense to me but not to Lean</p>

#### [ Patrick Massot (Jul 17 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833049):
<p>"type of sorry macro is not a sort"</p>

#### [ Patrick Massot (Jul 17 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833051):
<p>probably missing import or open</p>

#### [ Simon Hudon (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833133):
<p>that makes sense. Try <code>open tactic</code>.</p>

#### [ Kevin Buzzard (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833146):
<div class="codehilite"><pre><span></span>
</pre></div>

#### [ Kevin Buzzard (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833150):
<p><code>deep recursion was detected at 'formatter' (potential solution: increase stack space in your system)</code></p>

#### [ Patrick Massot (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833151):
<p>"deep recursion was detected at 'formatter' (potential solution: increase stack space in your system)"</p>

#### [ Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833163):
<p><span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833183):
<p>Maybe we have infinitely nested namespaces</p>

#### [ Simon Hudon (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833186):
<p>Interesting. What if you just do <code>trace names.length</code>?</p>

#### [ Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833195):
<p>22573</p>

#### [ Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833201):
<p><span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Patrick Massot (Jul 17 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833250):
<p>Maybe we should jump to the filtered version</p>

#### [ Simon Hudon (Jul 17 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833253):
<p>Good. That will be good enough for now. The problem is that we have a lot of definitions but we don't care about all of them. Let's filter the list and then we can print them all out</p>

#### [ Simon Hudon (Jul 17 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833264):
<p>You're using so few words to express my idea. I'm jealous</p>

#### [ Simon Hudon (Jul 17 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833280):
<p>Do you have an idea on how to do the filtering?</p>

#### [ Patrick Massot (Jul 17 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833300):
<p>Yes: using <code>environment.in_current_file</code></p>

#### [ Patrick Massot (Jul 17 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833353):
<p>I'm such a good student <span class="emoji emoji-1f62e" title="open mouth">:open_mouth:</span></p>

#### [ Simon Hudon (Jul 17 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833372):
<p>You get an A! Good job!</p>

#### [ Simon Hudon (Jul 17 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833461):
<p>Once you've done that and defined a new list <code>local_names</code>, you can print them more nicely as <code>local_names.mmap' trace</code></p>

#### [ Patrick Massot (Jul 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833763):
<p>"code generation failed, VM does not have code for 'classical.choice'". I may have taken a wrong turn...</p>

#### [ Patrick Massot (Jul 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833821):
<p>I was trying to get rid of that damn <code>environment.in_current_file curr_env has type   name → bool but is expected to have type   name → Prop</code></p>

#### [ Patrick Massot (Jul 17 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833849):
<p>I'm probably beaten for my preamble</p>

#### [ Patrick Massot (Jul 17 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833920):
<p>Yeah, in a fresh file Lean complains it wants a decidable instance</p>

#### [ Patrick Massot (Jul 17 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833964):
<p>(deleted)</p>

#### [ Patrick Massot (Jul 17 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833972):
<p>(deleted)</p>

#### [ Patrick Massot (Jul 17 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129834267):
<p>I give up, it seems I don't know enough. I tried <code>let noms := names.filter (environment.in_current_file curr_env),</code> but Lean wants a decidable function to prop, not a function to bool</p>

#### [ Simon Hudon (Jul 17 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129834884):
<p>Try <code>let noms := names.filter (λ n, curr_env.in_current_file n)</code></p>

#### [ Patrick Massot (Jul 17 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129834993):
<p>This works if there is mathematics preamble</p>

#### [ Simon Hudon (Jul 17 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835012):
<p>Which preamble?</p>

#### [ Patrick Massot (Jul 17 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835022):
<p><code>local attribute [instance] classical.prop_decidable</code></p>

#### [ Mario Carneiro (Jul 17 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835067):
<p>that's obviously a bad idea if you are writing code</p>

#### [ Simon Hudon (Jul 17 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835078):
<p>You shouldn't need that. Booleans are decidable propositions</p>

#### [ Patrick Massot (Jul 17 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835119):
<p>Of course it means I should define the command in its own file and execute it where I need it</p>

#### [ Simon Hudon (Jul 17 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835136):
<p>If you use <code>classical.prop_decidable</code> try <code>local attribute [instance, priority 0] classical.prop_decidable</code>. This way, if you have computable instances they will be chosen instead.</p>

#### [ Patrick Massot (Jul 17 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835321):
<p>It mostly works, but I see the <code>quot</code> namespace is not filtered out</p>

#### [ Patrick Massot (Jul 17 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835352):
<p>For the record, I think I wrote the solution at some point, but was confused by the decidability related error message</p>

#### [ Patrick Massot (Jul 17 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835516):
<p>It would also be nice to filter out all <code>_proof_</code> and <code>_eqn_</code></p>

#### [ Simon Hudon (Jul 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835564):
<p>Let's say <code>quot.lift</code>is one of those that aren't filtered out. Try printing <code>`curr_env.in_current_file </code>quot.lift` just to double check.</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835591):
<p>you can use <code>name.is_internal</code> to filter</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835612):
<p>it checks that none of the name components have an initial underscore</p>

#### [ Patrick Massot (Jul 17 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835818):
<p>Simon, could you try to fix quotes in your last message? I don't know where to put them</p>

#### [ Patrick Massot (Jul 17 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835860):
<p><code>name.is_internal</code> does allow to get rid of underscored stuff</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835902):
<p><code>curr_env.in_current_file `quot.lift</code></p>

#### [ Mario Carneiro (Jul 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835957):
<p>better yet <code>curr_env.in_current_file ``quot.lift</code></p>

#### [ Patrick Massot (Jul 17 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836041):
<p>Lean indeed answers <code>tt</code></p>

#### [ Patrick Massot (Jul 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836105):
<p>To make sure we are on the same page, the current version I have is:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">print_names</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="bp">&lt;-</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="n">trace</span> <span class="o">(</span><span class="n">to_string</span> <span class="o">(</span><span class="n">curr_env</span><span class="bp">.</span><span class="n">in_current_file</span> <span class="bp">``</span><span class="n">quot</span><span class="bp">.</span><span class="n">lift</span><span class="o">)),</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span> <span class="c1">-- this loops over all the visible declarations and, using `list.cons`, accumulate them in a list</span>
   <span class="k">let</span> <span class="n">names</span> <span class="o">:=</span> <span class="n">decls</span><span class="bp">.</span><span class="n">map</span> <span class="n">declaration</span><span class="bp">.</span><span class="n">to_name</span><span class="o">,</span> <span class="c1">-- this takes the name of each declaration.</span>
   <span class="k">let</span> <span class="n">local_names</span> <span class="o">:=</span> <span class="n">names</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">environment</span><span class="bp">.</span><span class="n">in_current_file</span> <span class="n">curr_env</span> <span class="n">x</span> <span class="bp">&amp;&amp;</span> <span class="n">not</span> <span class="n">x</span><span class="bp">.</span><span class="n">is_internal</span><span class="o">),</span>
   <span class="n">local_names</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="n">trace</span>
</pre></div>

#### [ Mario Carneiro (Jul 17 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836290):
<p>you can see from the definition of <code>in_current_file</code> that it just checks that <code>decl_olean</code> returns none</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836307):
<p>but <code>quot.lift</code> was never defined, it magically comes into being from the <code>init_quotient</code> one-time command</p>

#### [ Reid Barton (Jul 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836558):
<p>If you also require that <code>decl_pos</code> is not <code>none</code>, that should get rid of <code>quot</code> stuff</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836623):
<p>in a new file, I get this:</p>
<div class="codehilite"><pre><span></span>open tactic
#eval do env ← get_env,
  env.fold skip $ λ d t,
  let n := d.to_name in
  when (env.in_current_file n) (trace n) &gt;&gt; t

-- quot.mk
-- quot.ind
-- quot
-- quot.lift
-- _main
</pre></div>

#### [ Mario Carneiro (Jul 17 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836631):
<p>I guess <code>_main</code> is the tactic I am <code>#eval</code>ing, the rest come from <code>init_quotient</code></p>

#### [ Simon Hudon (Jul 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836707):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You may want to use <code>mfold</code> instead of <code>fold</code> for monadic functions</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836719):
<p>there is no <code>env.mfold</code></p>

#### [ Mario Carneiro (Jul 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836802):
<p>If I use <code>(env.decl_pos n).is_none</code> instead, I get</p>
<div class="codehilite"><pre><span></span>interactive.loc.has_reflect
prod.has_reflect
quot.mk
quot.ind
bool.has_reflect
sum.has_reflect
quot
quot.lift
option.has_reflect
pos.has_reflect
</pre></div>

#### [ Simon Hudon (Jul 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836820):
<p>Sorry, you're right, I was thinking of expressions</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836848):
<p>I'm not sure why e.g. <code>option.has_reflect</code> has no position, but I can confirm that vscode F12 has no idea where it is</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836903):
<div class="codehilite"><pre><span></span>attribute [derive has_reflect] bool prod sum option interactive.loc pos
</pre></div>


<p>I see</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837051):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I am surprised to discover that there is no <code>add_decl</code> variant or option to set the position of a new declaration</p>

#### [ Sebastian Ullrich (Jul 17 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837226):
<p>Yes, well, the Lean 3 meta API is just that incomplete</p>

#### [ Patrick Massot (Jul 17 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837293):
<p>I know it's cheating, but can't we just filter out <code>quot.*</code> using a plain regex?</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837309):
<p>You can, but it would be more accurate to say that it is only those four definitions specifically, not everything in <code>quot</code></p>

#### [ Mario Carneiro (Jul 17 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837318):
<p>also it wouldn't be a regex exactly</p>

#### [ Patrick Massot (Jul 17 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837368):
<p>those four definitions specifically would be even better</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837376):
<p>it is easy enough to filter out those four by name</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837475):
<div class="codehilite"><pre><span></span>meta def environment.in_current_file&#39;
  (env : environment) (n : name) : bool :=
env.in_current_file n &amp;&amp; (n ∉ [``quot, ``quot.mk, ``quot.lift, ``quot.ind])
</pre></div>

#### [ Patrick Massot (Jul 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840382):
<p>I missed that last message. Thanks!</p>

#### [ Patrick Massot (Jul 18 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840429):
<p>I think this command is really useful</p>

#### [ Patrick Massot (Jul 18 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840507):
<p>It's much easier than trying to keep track of which namespaces we are in</p>

#### [ Patrick Massot (Jul 18 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840513):
<p>Do we have mathlib guidelines about nested namespaces?</p>

#### [ Patrick Massot (Jul 18 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840549):
<p>That command would be even nicer if we had versions listing only definitions or only instances or only lemmas/theorems</p>

#### [ Patrick Massot (Jul 18 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840589):
<p>But I need to sleep now</p>

#### [ Patrick Massot (Jul 18 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840615):
<p>We could even have a tree view</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840623):
<p>what kind of guidelines do you mean?</p>

#### [ Patrick Massot (Jul 18 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840680):
<p>it could be pushing towards flat hierarchy or deep hierarchy</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840688):
<p>I would say it's currently more flat than deep</p>

#### [ Patrick Massot (Jul 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840689):
<p>My completion file currently has:</p>
<div class="codehilite"><pre><span></span>uniform_space.completion_is_complete
uniform_space.completion_extension
uniform_space.completion_is_separated
uniform_space.completion_extension.lifts
uniform_space.completion_lift.uniform_continuity
uniform_space.completion_is_uniform_space
uniform_space.to_completion
uniform_space.eq_of_separated_of_uniform_continuous
uniform_space.completion_lift
uniform_space.completion_lift.unique
uniform_space.completion_extension.uniform_continuity
uniform_space.to_completion.dense
uniform_space.completion_lift.comp
uniform_space.completion_lift.lifts
uniform_space.completion_extension.unique
uniform_space.separated_of_uniform_continuous
uniform_space.nonempty_completion_iff
uniform_space.completion
uniform_space.to_completion.uniform_continuous
</pre></div>

#### [ Mario Carneiro (Jul 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840702):
<p>there are some instances of large scale namespaces like <code>measure_theory</code>, but most definitions are only one namespace deep</p>

#### [ Patrick Massot (Jul 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840703):
<p>everything is inside the uniform_space namespace. But then the completion, completion_lift and completion_extension get their sub-namespace</p>

#### [ Patrick Massot (Jul 18 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840757):
<p>but this sub-namespacing could be replaced by underscores</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840758):
<p>I think that makes sense - <code>completion</code> is defined on <code>uniform_space</code>, and theorems about <code>completion</code> should go in a namespace for it</p>

#### [ Patrick Massot (Jul 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840772):
<p>because there is no structure involved, so we can't use the projection trick</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840782):
<p>Even so I think that <code>uniform_space.completion</code> is better than <code>completion</code> because of the need for disambiguation here</p>

#### [ Patrick Massot (Jul 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840785):
<p>I could also put (almost) everything from that file in a <code>uniform_space.completion</code> namespace</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840831):
<p>you could use <code>completion.lift</code> instead of <code>completion_lift</code> for example</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840857):
<p>I would avoid repeating things from the namespace in the name though</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840859):
<p><code>lattice.lattice</code> reads redundantly</p>

#### [ Patrick Massot (Jul 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840914):
<p>There are two related but distinct thing. <code>completion_lift</code> is a definition, lifting a function (not necessarily uniformly continuous!) to completion, and a lemma <code>completion_lift.lifts</code>  saying that the lift indeed lifts the map, under uniform continuity assumption</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840920):
<p>I might say <code>lift_is_lift</code> for something like that</p>

#### [ Patrick Massot (Jul 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840922):
<p>Deciding and namespaces and names for these two things is exactly the kind of question I have</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840938):
<p>although depending on what exactly "lift" means it might have a more specific name</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840990):
<p>i.e. if it is something like <code>lift o mk = id</code> (I'm making things up) then I might call it <code>lift_comp_mk</code>, but if it is <code>is_lift lift</code> then I would say <code>is_lift_lift</code> or <code>lift_is_lift</code></p>

#### [ Patrick Massot (Jul 18 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841003):
<p><a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L187" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L187">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L187</a></p>

#### [ Patrick Massot (Jul 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841058):
<p>and its friend <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L136" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L136">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L136</a></p>

#### [ Mario Carneiro (Jul 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841063):
<p>I would write that the other way and say <code>lift_to_completion</code></p>

#### [ Mario Carneiro (Jul 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841075):
<p>(probably <code>to_completion</code> should be a coercion)</p>

#### [ Patrick Massot (Jul 18 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841138):
<p>I wouldn't be able to state those lemmas without writing <code>to_completion</code>, even with a coercion, right?</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841151):
<p>you can say <code>coe</code></p>

#### [ Patrick Massot (Jul 18 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841161):
<p>I fear it would obscure the statement. But I could still define the coercion for later use</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841215):
<p>Also I don't know if using all these composes in the statement doesn't make your work harder</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841229):
<p>I know that's how mathematicians like to write it but sometimes it is nicer to just put a point in</p>

#### [ Patrick Massot (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841231):
<p>Do you mean you would state <code>forall x, ...</code>?</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841252):
<p>yes</p>

#### [ Patrick Massot (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841255):
<p>True, I really think about this from a categorical perspective, there are no points at all</p>

#### [ Patrick Massot (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841258):
<p>Only morphisms</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841307):
<p>Certainly <code>completion_extension.lifts</code> should be stated as <code>completion_extension f \u x = f x</code></p>

#### [ Patrick Massot (Jul 18 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841309):
<p>Points would really obscure statements</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841334):
<p>maybe, but none of the work done in this file so far is really categorical in nature</p>

#### [ Patrick Massot (Jul 18 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841335):
<p>ok, that one could be clearer with a <code>forall x : a, completion_extension f  x = f x</code></p>

#### [ Patrick Massot (Jul 18 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841389):
<p>What? Everything building <code>completion_lift</code> from <code>completion_extension</code> is purely categorical</p>

#### [ Patrick Massot (Jul 18 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841429):
<p>With proper mathlib help, there would be a single tactic to invoke to build <code>completion_lift</code> from <code>completion_extension</code></p>

#### [ Mario Carneiro (Jul 18 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841430):
<p>looks like just specializing theorems to me</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841486):
<p><code>completion_lift</code> should be called <code>completion.map</code> though</p>

#### [ Patrick Massot (Jul 18 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841504):
<p>The composition proof has slightly more than specializing. <code>completion_extension.unique</code> is crucial</p>

#### [ Mario Carneiro (Jul 18 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841554):
<p>but it is just specializing - <code>completion_lift.unique</code> just applies <code>completion_extension.unique</code></p>

#### [ Patrick Massot (Jul 18 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841579):
<p>I'm talking about the proof of <code>completion_lift.comp</code>, not <code>completion_lift.unique</code></p>

#### [ Patrick Massot (Jul 18 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841594):
<p>Anyway, I really need to sleep now. But I'll probably use all these suggestions tomorrow (although I should also be doing real work...)</p>

#### [ Patrick Massot (Jul 18 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841636):
<p>Thanks!</p>

#### [ Patrick Massot (Jul 19 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957604):
<p>Returning to this full names thread since Kevin also had a use case, are we interested to have this in mathlib? The version I currently have here is:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">sort</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">string</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">open</span> <span class="n">tactic</span>

<span class="c">/-</span><span class="cm">- `run_cmd print_names` print all names defined in the current file.</span>
<span class="cm">    This is useful when checking namespaces and writing doc -/</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">print_names</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="bp">&lt;-</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">names</span> <span class="o">:=</span> <span class="n">decls</span><span class="bp">.</span><span class="n">map</span> <span class="n">declaration</span><span class="bp">.</span><span class="n">to_name</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">local_names</span> <span class="o">:=</span> <span class="n">names</span><span class="bp">.</span><span class="n">filter</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">environment</span><span class="bp">.</span><span class="n">in_current_file&#39;</span> <span class="n">curr_env</span> <span class="n">x</span> <span class="bp">&amp;&amp;</span> <span class="n">not</span> <span class="n">x</span><span class="bp">.</span><span class="n">is_internal</span><span class="o">),</span>
   <span class="k">let</span> <span class="n">sorted_names</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">merge_sort</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="o">(</span><span class="n">local_names</span><span class="bp">.</span><span class="n">map</span> <span class="n">to_string</span><span class="o">),</span>
   <span class="n">sorted_names</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="n">trace</span>
</pre></div>


<p>With some argument parsing skill we could make sorting optional, and have an optional prefix filtering.</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957823):
<p>I think it should return a <code>list name</code> rather than printing it if you want to make this more widely usable</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957834):
<p>why isn't it sorted in declaration order?</p>

#### [ Patrick Massot (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957907):
<p>yesterday my main goal was to check namespaces, and alphabetical order was therefore more useful</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957910):
<p>it all seems a bit ad hoc</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957920):
<p>Alphabetical order has been around for a while</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957926):
<p>but I guess you could call it ad hoc</p>

#### [ Patrick Massot (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957927):
<p>I'm not even sure it's in declaration order before sorting</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957933):
<p>It's not universe-independent</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957940):
<p>I think it's the right length for a small program that slices data the way you want</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957944):
<p>or even country-independent</p>

#### [ Patrick Massot (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957971):
<p>I don't understand what you mean by that length comment</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958036):
<p>there isn't much mathlib can do to make that definition shorter without getting too specific</p>

#### [ Patrick Massot (Jul 19 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958105):
<p>Ok, I'll keep it around here then</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958195):
<p>If I add that exact tactic to mathlib, then of course your definition becomes very short (just a reference to my definition) but it also becomes less flexible - if you want to print them in a different order or get type information for each definition or something else you will have to start from scratch again (or copy paste the mathlib tactic)</p>

#### [ Patrick Massot (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958219):
<p>I still have a question about that small function. I don't want to be rude, or break the etiquette of this fine place, by using words from imperative programming. But I don't really understand how the main l**p works. What does the first line do exactly?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958228):
<p><code>get_env</code>?</p>

#### [ Patrick Massot (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958229):
<p>What is <code>get_env</code> returning?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958234):
<p>a reference to the environment object</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958276):
<p>which is the thing that stores all definitions</p>

#### [ Patrick Massot (Jul 19 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958351):
<p>what's the point of not having directly the list that the second line creates?</p>

#### [ Patrick Massot (Jul 19 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958446):
<p>hitting F12 only gives meta constant everywhere</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958530):
<p>because the environment isn't stored as a list</p>

#### [ Patrick Massot (Jul 19 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958551):
<p>I understand that, my question is: how is it more than a list of stuff?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958597):
<p>for one thing, it should have an index to speed up looking up definitions by name</p>

#### [ Patrick Massot (Jul 19 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958655):
<p>Actually I understand nothing about this monad thing. What the difference between the first line and its arcane <code>a &lt;- b</code> syntax and the friendlier looking lines with <code>let a := b</code>?</p>

#### [ Patrick Massot (Jul 19 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958675):
<p>so it's closer to a python dictionary than list?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958982):
<p>Literally, <code>a &lt;- b</code> is syntax for the <code>bind</code> operator, while <code>let a := b</code> is just <code>let</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959029):
<p>Most operations which have a sequential character or otherwise non-functional behavior have to work inside a monad, and <code>bind</code> puts them together with a notation that is deliberately similar to <code>let a := b</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959114):
<p>yes, it is basically a dictionary, probably a hash map. In particular, looping over all definitions (which is what you are doing) is one of the least efficient things you can do with it, so it is rather slow</p>

#### [ Patrick Massot (Jul 19 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959174):
<p>I'm sorry but I still don't see any difference between: "I want to call <code>curr_env</code> the thing returned by <code>get_env</code>" and "I want to call <code>decls</code> the thing returned by <code>curr_env.fold [] list.cons</code>"</p>

#### [ Patrick Massot (Jul 19 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959182):
<p>but clearly I cannot switch between <code>&lt;-</code> and <code>let</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959252):
<p>probably <code>get_env</code> is a bad example since it's basically functional, so consider the following instead:</p>
<div class="codehilite"><pre><span></span>do a &lt;- random,
   b &lt;- random,
   c &lt;- random,
   return [a, b, c]
</pre></div>


<p>Let's say that <code>random</code> returns a random number. Then this program will probably return three different numbers</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959271):
<p>On the other hand, with</p>
<div class="codehilite"><pre><span></span>let a := random,
    b := random,
    c := random in
[a, b, c]
</pre></div>


<p>there is no implementation of <code>random</code> that will cause three different numbers to be produced</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959337):
<p>Patrick do you know all about this monad business?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959350):
<p>All of this <code>&lt;-</code> is sugar for <code>monad.bind</code> etc</p>

#### [ Patrick Massot (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959412):
<p>I don't see why you would get the same number with let</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959413):
<p>The part of "programming in Lean" about the state monad gave me some idea about what was going on here. The <code>&lt;-</code> can change the state of things.</p>

#### [ Patrick Massot (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959428):
<p>Kevin, I tried to read that part of PIL several time, but it doesn't stick at all</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959432):
<p>but in functional programming you can't change state</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959435):
<p>as there is no state</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959448):
<p><code>&lt;-</code> can expand to "...and let x = x + 1 while you're doing this"</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959454):
<p>notice that the second program is definitionally equal to <code>[random, random, random]</code> and <code>(\lam x, [x, x, x]) random</code></p>

#### [ Patrick Massot (Jul 19 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959537):
<p>Sure. But then what happens at execution? Isn't random called three times?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959543):
<p>with the same inputs maybe</p>

#### [ Patrick Massot (Jul 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959583):
<p>there is no input</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959587):
<p>right</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959594):
<p>so the same thing happens three time</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959603):
<p>but with <code>&lt;-</code> there are hidden variables</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959626):
<p>it's not a contradiction that "intro x" can do different things at different points in the middle of a tactic proof</p>

#### [ Kevin Buzzard (Jul 19 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959627):
<p>because the goal might be different</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959724):
<p>A very small example:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">counter</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span> <span class="bp">×</span> <span class="n">α</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">counter</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">pure</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">a</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">a</span><span class="o">),</span>
  <span class="n">bind</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span> <span class="n">g</span> <span class="n">n</span><span class="o">,</span> <span class="k">let</span> <span class="o">(</span><span class="n">n&#39;</span><span class="o">,</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">n</span> <span class="k">in</span> <span class="n">g</span> <span class="n">a</span> <span class="n">n&#39;</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">count</span> <span class="o">:</span> <span class="n">counter</span> <span class="n">nat</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">n</span><span class="o">)</span>

<span class="n">def</span> <span class="n">run</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">counter</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">(</span><span class="n">c</span> <span class="mi">0</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">run</span> <span class="err">$</span> <span class="n">do</span>
  <span class="n">a</span> <span class="err">←</span> <span class="n">count</span><span class="o">,</span>
  <span class="n">b</span> <span class="err">←</span> <span class="n">count</span><span class="o">,</span>
  <span class="n">c</span> <span class="err">←</span> <span class="n">count</span><span class="o">,</span>
  <span class="n">return</span> <span class="o">[</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="o">]</span>

<span class="c1">-- [0, 1, 2]</span>
</pre></div>

#### [ Mario Carneiro (Jul 19 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959800):
<p>If I <code>#check</code> instead, it says</p>
<div class="codehilite"><pre><span></span>run (count &gt;&gt;= λ (a : ℕ), count &gt;&gt;= λ (b : ℕ), count &gt;&gt;= λ (c : ℕ), return [a, b, c]) : list ℕ
</pre></div>

#### [ Patrick Massot (Jul 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959869):
<p>I have <em>no idea</em> what's going on in your snippet</p>

#### [ Kevin Buzzard (Jul 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959873):
<p><code>&lt;-</code> is running <code>bind</code> which can change the nat. The nat is a variable which is hidden in the notation but still exists. If you unravel you can see the nat. <code>&gt;&gt;=</code> also means bind</p>

#### [ Mario Carneiro (Jul 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959876):
<p>Start with the first line</p>

#### [ Mario Carneiro (Jul 20 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959884):
<p><code>counter A</code> is a function from <code>nat</code> to <code>nat x A</code></p>

#### [ Kevin Buzzard (Jul 20 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959887):
<p><code>do</code> puts you into monad mode, and the monad here is <code>counter</code> which is hiding a nat.</p>

#### [ Patrick Massot (Jul 20 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959894):
<p>Zulip just told me your snippet was written yesterday. I probably mean it's too late to understand this</p>

#### [ Patrick Massot (Jul 20 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129960051):
<p>I should really sleep. Since my family left for vacations, I'm drifting towards night. Today (Zulip claims I mean yesterday) I reached the point where I got up too late to have lunch with my colleagues. So I'll try to drift back. But I promise I'll try to understand your code tomorrow, after reading back a bit of PIL. Thank you!</p>

#### [ Mario Carneiro (Jul 20 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129960242):
<p>By the way, that code is roughly analogous to the following C code:</p>
<div class="codehilite"><pre><span></span>int state = 0;
int a = state++;
int b = state++;
int c = state++;
return [a, b, c]; // &lt;- okay, not really C style...
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130303691):
<blockquote>
<p>Returning to this full names thread since Kevin also had a use case, are we interested to have this in mathlib? The version I currently have here is:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">sort</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">string</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">open</span> <span class="n">tactic</span>

<span class="c">/-</span><span class="cm">- `run_cmd print_names` print all names defined in the current file.</span>
<span class="cm">    This is useful when checking namespaces and writing doc -/</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">print_names</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="bp">&lt;-</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">names</span> <span class="o">:=</span> <span class="n">decls</span><span class="bp">.</span><span class="n">map</span> <span class="n">declaration</span><span class="bp">.</span><span class="n">to_name</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">local_names</span> <span class="o">:=</span> <span class="n">names</span><span class="bp">.</span><span class="n">filter</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">environment</span><span class="bp">.</span><span class="n">in_current_file&#39;</span> <span class="n">curr_env</span> <span class="n">x</span> <span class="bp">&amp;&amp;</span> <span class="n">not</span> <span class="n">x</span><span class="bp">.</span><span class="n">is_internal</span><span class="o">),</span>
   <span class="k">let</span> <span class="n">sorted_names</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">merge_sort</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="o">(</span><span class="n">local_names</span><span class="bp">.</span><span class="n">map</span> <span class="n">to_string</span><span class="o">),</span>
   <span class="n">sorted_names</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="n">trace</span>
</pre></div>


</blockquote>
<p>Ooh this was just really handy for me. Faced with</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">is_ring_hom</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">is_subring</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">R</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">map_one</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">is_ring_hom</span>
</pre></div>


<p>and after 2 minutes of failing to guess what Lean might have called this instance, I ran the code and got it immediately. </p>
<div class="codehilite"><pre><span></span>
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130303706):
<p>Answers on a postcard</p>

#### [ Reid Barton (Jul 26 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130308592):
<p>In this case I think <code>#print instances is_ring_hom</code> will tell you too.</p>

#### [ Kevin Buzzard (Jul 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130327524):
<p>Aah! I use <code>#print prefix</code> a fair bit but I don't think I'd internalised <code>#print instances</code></p>

#### [ Patrick Massot (Aug 11 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131947719):
<p>So we have this <code>print_names</code> command. We can put it in a file, import that file in another file, run the command there, and get our answer in the Lean messages window. How could we get the same information from the command line without modifying the file we want to inspect?</p>

#### [ Simon Hudon (Aug 11 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131958856):
<p>In Haskell, ghc has the option <code>-e</code> which allows you to provide an expression to evaluate from the command line. Lean does not have that. What I would do is write a bash script to generate a .lean file that imports your <code>print_names</code> definition and the file you want to check, then call Lean on that file.</p>

#### [ Mario Carneiro (Aug 11 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131960186):
<p>lean has a <code>--run</code> option</p>

#### [ Simon Hudon (Aug 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131961097):
<p>I thought it only ran the <code>main</code> function</p>

#### [ Patrick Massot (Aug 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131965768):
<p>That's also what the documentation and experiment suggest</p>

#### [ Patrick Massot (Aug 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131965831):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> do you confirm there is no way to do what I asked?</p>

#### [ Patrick Massot (Aug 11 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131965902):
<p>More generally, it would help with documentation if we knew more about Lean's introspection capabilities. For instance, suppose we get hold of some definition of lemma using <code>get_env</code>, is there any way we could get a list of types of objects appearing in the statement or, even better, a list of all lemmas and definitions used in the proof (before it gets erased by proof irrelevance)?</p>

#### [ Simon Hudon (Aug 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966166):
<blockquote>
<p>is there any way we could get a list of types of objects appearing in the statement or, even better, a list of all lemmas and definitions used in the proof (before it gets erased by proof irrelevance)?</p>
</blockquote>
<p>I believe that is possible. Let me just work something out.</p>

#### [ Simon Hudon (Aug 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966604):
<p>Here's what I got. This version lists all the constants (definition, theorem, axiom or constant, actually) used in the <em>statement</em> of the theorem. I have worked out a version I thought would do the same about the proof but I run into weird errors.</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">list_constant</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">name</span> <span class="o">:=</span>
<span class="n">e</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">e</span> <span class="bp">_</span> <span class="n">cs</span><span class="o">,</span>
<span class="k">if</span> <span class="n">e</span><span class="bp">.</span><span class="n">is_constant</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">e</span><span class="bp">.</span><span class="n">const_name</span> <span class="err">∈</span> <span class="n">cs</span>
  <span class="k">then</span> <span class="n">e</span><span class="bp">.</span><span class="n">const_name</span> <span class="bp">::</span> <span class="n">cs</span>
  <span class="k">else</span> <span class="n">cs</span>

<span class="kn">open</span> <span class="n">declaration</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">const_in_def</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">(</span><span class="n">thm</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t</span> <span class="n">v</span><span class="o">)</span> <span class="err">←</span> <span class="n">get_decl</span> <span class="n">n</span><span class="o">,</span>
   <span class="c1">-- let v := v.get,</span>
   <span class="c1">-- trace v.is_constant,</span>
   <span class="n">trace</span> <span class="err">$</span> <span class="n">list_constant</span> <span class="n">t</span><span class="o">,</span>
   <span class="n">return</span> <span class="o">()</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">const_in_def</span> <span class="bp">`</span><span class="n">list</span><span class="bp">.</span><span class="n">reverse_append</span>
</pre></div>

#### [ Patrick Massot (Aug 11 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966679):
<p>Nice!</p>

#### [ Patrick Massot (Aug 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966724):
<p>I think I will play of lot with that function</p>

#### [ Simon Hudon (Aug 11 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966786):
<p>Cool! Please let me know if you manage to get <code>v.get</code> to work. What I think is that the proof tree might be stored nowhere so <code>v.get</code> can only fail. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> and <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> may shed some light on that.</p>

#### [ Gabriel Ebner (Aug 11 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967066):
<p>What error are you getting?  This works just fine for me:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">list_constant</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">name</span> <span class="o">:=</span>
<span class="n">e</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">e</span> <span class="bp">_</span> <span class="n">cs</span><span class="o">,</span>
<span class="k">if</span> <span class="n">e</span><span class="bp">.</span><span class="n">is_constant</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">e</span><span class="bp">.</span><span class="n">const_name</span> <span class="err">∈</span> <span class="n">cs</span>
  <span class="k">then</span> <span class="n">e</span><span class="bp">.</span><span class="n">const_name</span> <span class="bp">::</span> <span class="n">cs</span>
  <span class="k">else</span> <span class="n">cs</span>

<span class="kn">open</span> <span class="n">declaration</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">const_in_def</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">(</span><span class="n">thm</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t</span> <span class="n">v</span><span class="o">)</span> <span class="err">←</span> <span class="n">get_decl</span> <span class="n">n</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">v</span><span class="bp">.</span><span class="n">get</span><span class="o">,</span>
   <span class="n">trace</span> <span class="err">$</span> <span class="n">list_constant</span> <span class="n">v</span><span class="o">,</span>
   <span class="n">trace</span> <span class="err">$</span> <span class="n">list_constant</span> <span class="n">t</span><span class="o">,</span>
   <span class="n">return</span> <span class="o">()</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">const_in_def</span> <span class="bp">`</span><span class="n">list</span><span class="bp">.</span><span class="n">reverse_append</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">scratch20180811.lean:17:0: information trace output</span>
<span class="cm">[list.append_assoc,</span>
<span class="cm"> list.reverse_cons,</span>
<span class="cm"> list.cons_append,</span>
<span class="cm"> list.cons,</span>
<span class="cm"> trivial,</span>
<span class="cm"> eq_self_iff_true,</span>
<span class="cm"> propext,</span>
<span class="cm"> list.append_nil,</span>
<span class="cm"> list.reverse_nil,</span>
<span class="cm"> eq.refl,</span>
<span class="cm"> has_append,</span>
<span class="cm"> list.nil_append,</span>
<span class="cm"> congr_arg,</span>
<span class="cm"> congr,</span>
<span class="cm"> eq.trans,</span>
<span class="cm"> id,</span>
<span class="cm"> true,</span>
<span class="cm"> list.nil,</span>
<span class="cm"> eq.mpr,</span>
<span class="cm"> list.has_append,</span>
<span class="cm"> has_append.append,</span>
<span class="cm"> list.reverse,</span>
<span class="cm"> eq,</span>
<span class="cm"> list.rec,</span>
<span class="cm"> list]</span>
<span class="cm">[list.has_append, has_append.append, list.reverse, eq, list]</span>

<span class="cm">-/</span>
</pre></div>

#### [ Simon Hudon (Aug 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967321):
<div class="codehilite"><pre><span></span>excessive memory consumption detected at &#39;replace&#39; (potential solution: increase memory consumption threshold)
</pre></div>

#### [ Simon Hudon (Aug 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967322):
<p>I'm invoking it from within emacs. Does that matter?</p>

#### [ Patrick Massot (Aug 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967371):
<p>Gabriel's code also works here (in VScode).</p>

#### [ Patrick Massot (Aug 11 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967379):
<p>and in command line as well</p>

#### [ Gabriel Ebner (Aug 11 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967430):
<p>No it doesn't matter which editor you use.  Make sure you run <code>leanpkg build</code> before, this reduced the required amount of memory.  Typically, when you see excessive memory usage errors, the only way forward is to restart the server.</p>

#### [ Simon Hudon (Aug 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967502):
<p>The plot thickens: I just called <code>#print list.reverse_append</code> and got:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse_append</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">),</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="o">(</span><span class="n">s</span> <span class="bp">++</span> <span class="n">t</span><span class="o">)</span> <span class="bp">=</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">t</span> <span class="bp">++</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">s</span> <span class="o">:=</span>
<span class="o">[</span><span class="n">incorrect</span> <span class="k">proof</span><span class="o">]</span>
</pre></div>


<p>So I'll delete all the <code>.olean</code> files and build from scratch.</p>

#### [ Simon Hudon (Aug 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967760):
<p>It did solve the problem. Thanks <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> !</p>

#### [ Simon Hudon (Aug 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967822):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, if you want to restrict the output of that program to lemmas you can use  <code>tactic.is_proof</code> to filter those names. Other options can help you restrict it to types or functions.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967891):
<p>you mean filter the output of list_constant?</p>

#### [ Simon Hudon (Aug 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967962):
<p>Yes exactly.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967979):
<p>Since we're at it, how would you list all file imported by the current file. That one I could implement in python with regex  :-)</p>

#### [ Simon Hudon (Aug 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967980):
<p>for instance, you can do it as <code>cs.mfilter $ λ c, mk_const c &gt;&gt;= is_proof</code></p>

#### [ Simon Hudon (Aug 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967985):
<p>(if <code>cs</code> is the result of <code>list_constant</code>)</p>

#### [ Patrick Massot (Aug 11 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968030):
<p>What is the m doing in <code>mfilter</code>? Does it mean meta? Wouldn't it work with regular filter?</p>

#### [ Patrick Massot (Aug 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968084):
<p>I would have simply written <code>cs.filter is_proof</code></p>

#### [ Simon Hudon (Aug 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968163):
<p>No the <code>m</code> is for monad becaus <code>mk_const</code> and <code>is_proof</code> use the <code>tactic</code> monad.</p>

#### [ Simon Hudon (Aug 11 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968171):
<p>It works in trusted functions as well.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968218):
<p>That's what I meant. To me monad = tactic monad = meta. I may try to refine that vision at some point</p>

#### [ Simon Hudon (Aug 11 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968221):
<blockquote>
<p>Since we're at it, how would you list all file imported by the current file. That one I could implement in python with regex  :-)</p>
</blockquote>
<p>I'm stumped. I think there is very little information available about the file / module structure.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968236):
<p>That's great. The only thing which is easy to do with regex is hard in Lean!</p>

#### [ Simon Hudon (Aug 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968240):
<p>Ah! I see. a monad is a category theoretic concept of which <code>tactic</code> is only one instance. It's a good way of structuring programs when you want to prove things about them.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968284):
<p>I'm half joking, I know there are other monads</p>

#### [ Simon Hudon (Aug 11 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968294):
<p>Haha! Using the parser framework, you may decide to read the current file and do some of your regex work that way. And it all stays in Lean. I wouldn't call it a proper way but it would get the job done.</p>

#### [ Simon Hudon (Aug 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968350):
<blockquote>
<p>I'm half joking, I know there are other monads</p>
</blockquote>
<p>The pedantic explanation that people throw around might actually clarify things for you :P "it's simple! A monad is just a monoid in the category of endofunctors"</p>
<p>... speaking of only half understanding ... :P</p>

#### [ Patrick Massot (Aug 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968362):
<p>What is <code>mk_const</code> doing in your filtering stuff?</p>

#### [ Patrick Massot (Aug 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968408):
<p>Actually I can't used the filtered list, I get <code>failed to synthesize type class instance for has_to_tactic_format (tactic (list name))</code></p>

#### [ Simon Hudon (Aug 11 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968517):
<p>I assume you tried <code>trace (mfilter ... )</code>. The <code>mfilter</code> expression is a monadic command so you have to execute it before using its result:</p>
<div class="codehilite"><pre><span></span><span class="n">r</span> <span class="bp">&lt;-</span> <span class="n">mfilter</span> <span class="c">/-</span><span class="cm"> rest -/</span><span class="o">,</span>
<span class="n">trace</span> <span class="n">r</span>
</pre></div>

#### [ Patrick Massot (Aug 11 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968535):
<p>indeed this works better</p>

#### [ Simon Hudon (Aug 11 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968593):
<p>The comma here is as if you were using <code>&gt;&gt;=</code>, that is the sequential composition of two commands: the <code>mfilter</code> expression and the <code>trace</code> expression:</p>
<div class="codehilite"><pre><span></span><span class="n">mfilter</span> <span class="c">/-</span><span class="cm"> stuff -/</span> <span class="bp">&gt;&gt;=</span> <span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="n">trace</span> <span class="n">r</span>
</pre></div>


<p>or</p>
<div class="codehilite"><pre><span></span><span class="n">mfilter</span> <span class="c">/-</span><span class="cm"> stuff -/</span> <span class="bp">&gt;&gt;=</span> <span class="n">trace</span>
</pre></div>


<p>after η-reduction.</p>

#### [ Patrick Massot (Aug 11 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968936):
<p>Thank you very much. I think I'll learn of lot from this. But right now I'm required for shooting stars hunting.</p>

#### [ Simon Hudon (Aug 11 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131969262):
<p>Good luck!</p>

#### [ Scott Morrison (Aug 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131969820):
<blockquote>
<p>The pedantic explanation that people throw around might actually clarify things for you :P "it's simple! A monad is just a monoid in the category of endofunctors"</p>
</blockquote>
<p>But you also have to remember that if a computer scientist says that to you, they probably really mean "... in the category of endofuctors of the category of types"!</p>

#### [ Scott Morrison (Aug 11 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131969821):
<p>(similarly if they just say <code>functor</code> they mean endofunctor of the category of types: we even have this in mathlib)</p>

#### [ Simon Hudon (Aug 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970139):
<p>I stand corrected ... or my knowledge stands improved</p>

#### [ Simon Hudon (Aug 11 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970150):
<p>I should really start taking advantage of the fact that so many category theorists hang around here. I've been thinking of doing a categorical treatment of liveness properties in temporal logic but it doesn't bode well: I already mess up the terminology!</p>

#### [ Scott Morrison (Aug 11 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970246):
<p>Given that more computer scientists use "monad" now than mathematicians, my vote would be to give it to them (i.e. add "in the category of types" to the fancy-pants definition), and go back to using "triple", or "triad" from the earlier category theory literature for the general case)</p>

#### [ Simon Hudon (Aug 11 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970302):
<p>What a shame! I thought we might make friends with mathematicians with those category theoretic ideas! Now you're giving us "we knew about monad before it was cool"</p>

#### [ Scott Morrison (Aug 12 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970709):
<p>:-) I certainly learnt what a monad was from its CS usage before the category-theoretic obscurity.</p>

#### [ Scott Morrison (Aug 12 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970763):
<p>btw <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, would you object if I added <code>@[extensionality]</code> to <code>propext</code>?</p>

#### [ Simon Hudon (Aug 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970830):
<p>I find its CS usage has a pretty funny story. They didn't know how to do IO in a pure way in Haskell so they held they breath until someone unearthed an obscure category theory paper, found someone to explain it to computer scientists and help them translate those pies in the sky into physical world phenomena</p>

#### [ Simon Hudon (Aug 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970839):
<p>No objections. Do you see any downside to doing it?</p>

#### [ Scott Morrison (Aug 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970901):
<p>My whole research field (tensor categories, topological field theory) is the same: just a toy for mathematicians who couldn't cope with quantum field theory, until some physicists came along and said "we've discovered this stuff we call 'topological matter'"</p>

#### [ Patrick Massot (Aug 12 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131971051):
<blockquote>
<p>Good luck!</p>
</blockquote>
<p>We have been very lucky, including one amazing one. Now I'll go sleeping</p>

#### [ Simon Hudon (Aug 12 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131971107):
<p>I find it so mind blowing when that happens. My favorite example is Euler's number theory work being useful in cryptography after he had his fun with it.</p>

#### [ Patrick Massot (Aug 12 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/132010173):
<p>(deleted)</p>

#### [ Chris Hughes (Sep 09 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604168):
<p>I had a go at making Simon's code return all the definitions used transitively. Why doesn't this work? I think it has something to do with <code>list.mmap</code></p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">list_constant</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">name</span> <span class="o">:=</span>
<span class="n">e</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">e</span> <span class="bp">_</span> <span class="n">cs</span><span class="o">,</span>
<span class="k">if</span> <span class="n">e</span><span class="bp">.</span><span class="n">is_constant</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">e</span><span class="bp">.</span><span class="n">const_name</span> <span class="err">∈</span> <span class="n">cs</span>
  <span class="k">then</span> <span class="n">e</span><span class="bp">.</span><span class="n">const_name</span> <span class="bp">::</span> <span class="n">cs</span>
  <span class="k">else</span> <span class="n">cs</span>

<span class="kn">open</span> <span class="n">declaration</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">const_in_def</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">),</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">name</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">do</span> <span class="o">(</span><span class="n">thm</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t</span> <span class="n">v</span><span class="o">)</span> <span class="err">←</span> <span class="n">get_decl</span> <span class="n">n</span><span class="o">,</span>
<span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">v</span><span class="bp">.</span><span class="n">get</span><span class="o">,</span>
<span class="k">let</span> <span class="n">l</span> <span class="o">:=</span> <span class="n">list_constant</span> <span class="n">v</span><span class="o">,</span>
<span class="n">m</span> <span class="err">←</span> <span class="n">l</span><span class="bp">.</span><span class="n">mmap</span> <span class="n">const_in_def</span><span class="o">,</span>
<span class="n">return</span> <span class="o">(</span><span class="n">m</span><span class="bp">.</span><span class="n">bind</span> <span class="n">id</span><span class="o">)</span><span class="bp">.</span><span class="n">erase_dup</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">const_in_def&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">l</span> <span class="err">←</span> <span class="n">const_in_def</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">trace</span> <span class="n">l</span><span class="o">,</span>
  <span class="n">return</span> <span class="o">()</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">const_in_def&#39;</span> <span class="bp">`</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_add_div</span>
</pre></div>

#### [ Reid Barton (Sep 09 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604311):
<p>I see "match failed", is that what you mean by doesn't work?</p>

#### [ Reid Barton (Sep 09 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604318):
<p>I assume it's the match <code>(thm _ _ t v) ← get_decl n</code>, there are going to be constants reachable from anything as well as theorems.</p>

#### [ Reid Barton (Sep 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604372):
<p>If you add <code>trace n, </code> at the start of that line you can see that it's processing <code>trivial</code>, which is a <code>defn</code>, not a <code>thm</code></p>

#### [ Chris Hughes (Sep 09 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133606586):
<p>Thanks. got it working now.</p>

#### [ Patrick Massot (Sep 09 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133620373):
<p>You can have a look at <a href="https://github.com/leanprover-community/leancrawler/blob/master/src/leancrawler/deps.lean" target="_blank" title="https://github.com/leanprover-community/leancrawler/blob/master/src/leancrawler/deps.lean">https://github.com/leanprover-community/leancrawler/blob/master/src/leancrawler/deps.lean</a> for more stuff you can extract from Lean (and of course you can also use the python part)</p>


{% endraw %}
