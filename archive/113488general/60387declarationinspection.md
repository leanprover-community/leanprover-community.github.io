---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60387declarationinspection.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [declaration inspection](https://leanprover-community.github.io/archive/113488general/60387declarationinspection.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Aug 15 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132184814):
<p>I'm still trying to discover what a Lean file can reveal about itself. I found <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean">https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean</a> and <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean">https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean</a> but there still very basic questions I can't answer. Say I have an environment and a declaration name. I can distinguish a lemma/theorem from a definition or constant (although I'm not sure what's the difference between definition and constant). But how can I distinguish between <code>def</code>, <code>class</code>, <code>instance</code>, <code>structure</code>, <code>inductive</code>? I saw the series of functions around <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean#L47" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean#L47">https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean#L47</a> but trying them on examples only confuses me.</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132184954):
<p><code>class</code> means <code>@[class] structure</code> so you can use the attribute</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132184971):
<p>similarly <code>@[instance]</code> is an attribute</p>

#### [ Patrick Massot (Aug 15 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185017):
<p>How do you get attributes of a declaration?</p>

#### [ Patrick Massot (Aug 15 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185129):
<p>Can one strip off <code>Pi</code> from an <code>expr</code> and get to the first function appearing next? (This would be to understand what an instance declaration is an instance of)</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185232):
<p><code>tactic.has_attribute</code></p>

#### [ Patrick Massot (Aug 15 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185432):
<p>Is it possible do use this outside of a tactic? (in meta land of course)</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185506):
<p>I doubt it, it looks like environment doesn't know anything about attributes</p>

#### [ Patrick Massot (Aug 15 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185695):
<p>Do you see away to get the list of classes defined in the currently opened file then?</p>

#### [ Edward Ayers (Aug 15 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185760):
<p>It also doesn't seem possible to get any information on what notation is defined.</p>

#### [ Mario Carneiro (Aug 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186062):
<div class="codehilite"><pre><span></span>import tactic.basic

class foo : Type.
structure bar : Type.
@[class] def baz : Type := nat

open tactic
run_cmd do
  env ← get_env,
  env.fold skip $ λ d t, do
    when (env.in_current_file&#39; d.to_name) $ try $
      tactic.has_attribute `class d.to_name &gt;&gt;
      trace d.to_name,
    t
-- foo baz
</pre></div>

#### [ Mario Carneiro (Aug 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186126):
<p>alternatively:</p>
<div class="codehilite"><pre><span></span>run_cmd do
  env ← get_env,
  l ← attribute.get_instances `class,
  l.mmap&#39; $ λ n, do
    when (env.in_current_file&#39; n) (trace n)
-- baz foo
</pre></div>

#### [ Mario Carneiro (Aug 15 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186311):
<p>as I'm sure you've heard by now, this introspection stuff is getting an overhaul in lean 4, so fingers crossed</p>

#### [ Patrick Massot (Aug 15 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186593):
<p>Thanks!</p>

#### [ Patrick Massot (Aug 15 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186636):
<p>What is the difference between <code>run_cmd</code> and <code>#eval</code> here?</p>

#### [ Patrick Massot (Aug 15 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132187368):
<p>Inside a function which will ultimately return a <code>tactic unit</code> can I have some <code>if</code> consuming a <code>tactic Prop</code> or <code>tactic bool</code>?</p>

#### [ Mario Carneiro (Aug 15 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132187933):
<p>there is <code>mcond</code> as a shortcut for this, but you can always do <code>b &lt;- tac, if b then ... else ...</code></p>

#### [ Patrick Massot (Aug 15 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188027):
<p>thanks</p>

#### [ Patrick Massot (Aug 15 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188037):
<p>I'm sorry I'm very slowly getting used to monads</p>

#### [ Patrick Massot (Aug 15 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188081):
<p>Do you have ideas to traverse an <code>expr</code> until you see what an instance is an instance of?</p>

#### [ Mario Carneiro (Aug 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188330):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">expr</span><span class="bp">.</span><span class="n">get_pi_app_fn</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">e</span><span class="bp">.</span><span class="n">get_pi_app_fn</span>
<span class="bp">|</span> <span class="n">e</span>                 <span class="o">:=</span> <span class="n">e</span><span class="bp">.</span><span class="n">get_app_fn</span>

<span class="n">run_cmd</span> <span class="n">do</span>
  <span class="n">d</span> <span class="err">←</span> <span class="n">get_decl</span> <span class="bp">``</span><span class="n">option</span><span class="bp">.</span><span class="n">decidable_eq</span><span class="o">,</span>
  <span class="n">expr</span><span class="bp">.</span><span class="n">const</span> <span class="n">n</span> <span class="bp">_</span> <span class="err">←</span> <span class="n">return</span> <span class="n">d</span><span class="bp">.</span><span class="n">type</span><span class="bp">.</span><span class="n">get_pi_app_fn</span><span class="o">,</span>
  <span class="n">trace</span> <span class="n">n</span>
<span class="c1">-- decidable_eq</span>
</pre></div>

#### [ Patrick Massot (Aug 15 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188717):
<p>great!</p>

#### [ Patrick Massot (Aug 15 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188810):
<p>I think I even understand this code (but wouldn't have none where to search)</p>

#### [ Patrick Massot (Aug 15 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132189258):
<p>Two last questions and then I cook dinner: how would you distinguish between <code>inductive</code> and <code>structure</code> declarations? What does constant mean in the definition of the declaration type? How is is more constant than a definition?</p>

#### [ Patrick Massot (Aug 15 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197062):
<p>Mario, do you also have hints for me?</p>

#### [ Rob Lewis (Aug 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197217):
<p><code>declaration.cnst</code> is the kind of declaration you get if you write <code>constant A : ℕ</code>. It's an undefined constant, basically the same as an axiom.</p>

#### [ Rob Lewis (Aug 15 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197290):
<p>You can have a <code>meta constant</code> but not a <code>meta axiom</code>. I'm not sure if there are any other differences between the two.</p>

#### [ Patrick Massot (Aug 15 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197349):
<p>I'm sorry but this doesn't match what I'm seeing</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197431):
<p>I think <code>constant</code> is to <code>axiom</code> as <code>def</code> is to <code>theorem</code></p>

#### [ Rob Lewis (Aug 15 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197478):
<p>What are you seeing?</p>

#### [ Rob Lewis (Aug 15 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197543):
<p>The differences between def and theorem are when the bodies get elaborated, right? But there are no bodies in a constant or axiom.</p>

#### [ Rob Lewis (Aug 15 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197609):
<p>And you can have axioms with non-<code>Prop</code> type.</p>

#### [ Rob Lewis (Aug 15 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197749):
<p>Actually, it looks like using the <code>axiom</code> command with a non-<code>Prop</code> type creates a <code>declaration.cnst</code> in the end. (edit- scratch that, typo)</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197798):
<p>I'm going through the code now, trying to figure out the difference</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197808):
<p>it is disambiguated in loads of places just so it can print <code>constant</code> instead of <code>axiom</code> but that's not so helpful</p>

#### [ Patrick Massot (Aug 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198136):
<p>Sorry I was interrupted. Maybe there is a misunderstanding, I'm talking about <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean#L67" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean#L67">https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean#L67</a></p>

#### [ Patrick Massot (Aug 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198153):
<p>See </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">environment</span> <span class="n">declaration</span>

<span class="kn">structure</span> <span class="n">toto</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">tata</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">eval</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">local_decls</span> <span class="o">:=</span> <span class="n">decls</span><span class="bp">.</span><span class="n">filter</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">environment</span><span class="bp">.</span><span class="n">in_current_file&#39;</span> <span class="n">curr_env</span> <span class="o">(</span><span class="n">to_name</span> <span class="n">x</span><span class="o">)</span> <span class="bp">&amp;&amp;</span> <span class="n">not</span> <span class="o">(</span><span class="n">to_name</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">is_internal</span><span class="o">),</span>
   <span class="n">local_decls</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">decl</span> <span class="o">:</span> <span class="n">declaration</span><span class="o">,</span>
       <span class="k">match</span> <span class="n">decl</span> <span class="k">with</span>
   <span class="bp">|</span> <span class="o">(</span><span class="n">thm</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">trace</span> <span class="s2">&quot;theorem&quot;</span>
   <span class="bp">|</span> <span class="o">(</span><span class="n">defn</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">trace</span> <span class="s2">&quot;def&quot;</span>
   <span class="bp">|</span> <span class="o">(</span><span class="n">cnst</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">trace</span> <span class="s2">&quot;cnst&quot;</span>
   <span class="bp">|</span> <span class="o">(</span><span class="n">ax</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">trace</span> <span class="s2">&quot;ax&quot;</span>
  <span class="kn">end</span><span class="o">)</span>
</pre></div>


<p>lots of cnst there</p>

#### [ Rob Lewis (Aug 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198311):
<p>"Built-ins" are implemented as constants too. So when you declare an inductive type, the constructors, recursor, etc. are constants.</p>

#### [ Rob Lewis (Aug 15 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198325):
<p>If you change a line to <code>| (cnst nm _ _ _) := do trace "cnst", trace nm</code> you can see what the constants are called.</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198345):
<p>Did you know about <code>#print definition</code>?</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198404):
<p>I just discovered that you can print definitions with <code>#print definition foo</code>. it's the same as <code>#print foo</code> but the printout is slightly different and it doesn't work on constants</p>

#### [ Rob Lewis (Aug 15 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198494):
<p>I had no idea, heh.</p>

#### [ Patrick Massot (Aug 15 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198658):
<p>I know, maybe it's clearer with </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">environment</span> <span class="n">declaration</span>

<span class="kn">structure</span> <span class="n">toto</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">tata</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">eval</span>
<span class="n">do</span> <span class="n">curr_env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">decls</span> <span class="o">:=</span> <span class="n">curr_env</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">local_decls</span> <span class="o">:=</span> <span class="n">decls</span><span class="bp">.</span><span class="n">filter</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">environment</span><span class="bp">.</span><span class="n">in_current_file&#39;</span> <span class="n">curr_env</span> <span class="o">(</span><span class="n">to_name</span> <span class="n">x</span><span class="o">)</span> <span class="bp">&amp;&amp;</span> <span class="n">not</span> <span class="o">(</span><span class="n">to_name</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">is_internal</span><span class="o">),</span>
   <span class="n">local_decls</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">decl</span> <span class="o">:</span> <span class="n">declaration</span><span class="o">,</span>
       <span class="k">match</span> <span class="n">decl</span> <span class="k">with</span>
   <span class="bp">|</span> <span class="o">(</span><span class="n">cnst</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">trace</span> <span class="n">decl</span><span class="bp">.</span><span class="n">to_name</span>
   <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">skip</span>
  <span class="kn">end</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Aug 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198673):
<p>you see that <code>toto</code> is also <code>cnst</code></p>

#### [ Mario Carneiro (Aug 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198710):
<p>Oh, <span class="user-mention" data-user-id="110031">@Patrick Massot</span> I found out that even lean internally doesn't store the list of attributes associated to a definition. When printing a definition with <code>#print</code>, it gets the list of all attributes and just asks for each whether <code>foo</code> has that attribute</p>

#### [ Patrick Massot (Aug 15 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198786):
<p>but where does the answer come from then?</p>

#### [ Rob Lewis (Aug 15 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198801):
<p>Yeah. When you declare an inductive type <code>T</code>, you're basically saying, "there is a type <code>T</code>. This is how you create a <code>T</code> (the constructors). This is how you use a <code>T</code> (the recursors)."</p>

#### [ Rob Lewis (Aug 15 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198813):
<p>You're not defining <code>T</code> in terms of something else, so there's no value for the declaration <code>T</code> to have.</p>

#### [ Patrick Massot (Aug 15 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198884):
<p>Makes sense, thanks</p>

#### [ Patrick Massot (Aug 15 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198896):
<p>Do you have an idea to distinguish between <code>inductive</code> and <code>structure</code>?</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199003):
<p>I'm working on it</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199047):
<p>in the meantime, I found something odd:</p>
<div class="codehilite"><pre><span></span>structure foo : Type.
#print foo
-- inductive foo : Type
-- constructors:
-- foo.mk : foo
</pre></div>

#### [ Mario Carneiro (Aug 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199052):
<p>lean does not remember structureness</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199131):
<p>or at least, nullary structures don't count as structures</p>

#### [ Patrick Massot (Aug 15 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199175):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">toto</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">tata</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">toto</span>
</pre></div>

#### [ Patrick Massot (Aug 15 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199245):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">toto</span> <span class="o">:</span> <span class="kt">Type</span> <span class="mi">1</span>
<span class="n">fields</span><span class="o">:</span>
<span class="n">toto</span><span class="bp">.</span><span class="n">tata</span> <span class="o">:</span> <span class="n">toto</span> <span class="bp">→</span> <span class="kt">Type</span>
</pre></div>

#### [ Mario Carneiro (Aug 15 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199271):
<p>Lean reconstructs structurehood based on structure like things</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199282):
<p>specifically, the projections</p>

#### [ Patrick Massot (Aug 15 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199802):
<p>where do you see the code of <code>#print</code>?</p>

#### [ Patrick Massot (Aug 15 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132200606):
<p>are you looking at <a href="https://github.com/leanprover/lean/blob/703d12d594f1591296d529e72794a00ba42dbade/src/frontends/lean/structure_cmd.cpp#L111" target="_blank" title="https://github.com/leanprover/lean/blob/703d12d594f1591296d529e72794a00ba42dbade/src/frontends/lean/structure_cmd.cpp#L111">https://github.com/leanprover/lean/blob/703d12d594f1591296d529e72794a00ba42dbade/src/frontends/lean/structure_cmd.cpp#L111</a>?</p>

#### [ Mario Carneiro (Aug 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132200886):
<p>I think this replicates lean's <code>is_structure</code> function</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">name</span><span class="bp">.</span><span class="n">deinternalize_field</span> <span class="o">:</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">name</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">name</span><span class="bp">.</span><span class="n">mk_string</span> <span class="n">s</span> <span class="n">name</span><span class="bp">.</span><span class="n">anonymous</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">i</span> <span class="o">:=</span> <span class="n">s</span><span class="bp">.</span><span class="n">mk_iterator</span> <span class="k">in</span>
  <span class="k">if</span> <span class="n">i</span><span class="bp">.</span><span class="n">curr</span> <span class="bp">=</span> <span class="err">&#39;</span><span class="bp">_</span><span class="err">&#39;</span> <span class="k">then</span> <span class="n">i</span><span class="bp">.</span><span class="n">next</span><span class="bp">.</span><span class="n">next_to_string</span> <span class="k">else</span> <span class="n">s</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">n</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">environment</span><span class="bp">.</span><span class="n">is_structure</span> <span class="o">(</span><span class="n">env</span> <span class="o">:</span> <span class="n">environment</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span>
<span class="n">option</span><span class="bp">.</span><span class="n">is_some</span> <span class="err">$</span> <span class="n">do</span>
  <span class="n">guardb</span> <span class="o">(</span><span class="n">env</span><span class="bp">.</span><span class="n">is_inductive</span> <span class="n">n</span><span class="o">),</span>
  <span class="n">d</span> <span class="err">←</span> <span class="o">(</span><span class="n">env</span><span class="bp">.</span><span class="n">get</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">to_option</span><span class="o">,</span>
  <span class="o">[</span><span class="n">intro</span><span class="o">]</span> <span class="err">←</span> <span class="n">pure</span> <span class="o">(</span><span class="n">env</span><span class="bp">.</span><span class="n">constructors_of</span> <span class="n">n</span><span class="o">)</span> <span class="bp">|</span> <span class="n">none</span><span class="o">,</span>
  <span class="n">guard</span> <span class="o">(</span><span class="n">env</span><span class="bp">.</span><span class="n">inductive_num_indices</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">),</span>
  <span class="k">let</span> <span class="n">nparams</span> <span class="o">:=</span> <span class="n">env</span><span class="bp">.</span><span class="n">inductive_num_params</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">di</span> <span class="err">←</span> <span class="o">(</span><span class="n">env</span><span class="bp">.</span><span class="n">get</span> <span class="n">intro</span><span class="o">)</span><span class="bp">.</span><span class="n">to_option</span><span class="o">,</span>
  <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">iterate</span> <span class="o">(</span><span class="n">expr</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">unit</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">f</span> <span class="n">e</span><span class="o">,</span> <span class="n">do</span>
      <span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">body</span> <span class="err">←</span> <span class="n">pure</span> <span class="n">e</span> <span class="bp">|</span> <span class="n">none</span><span class="o">,</span>
      <span class="n">f</span> <span class="n">body</span><span class="o">)</span> <span class="n">nparams</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">do</span>
      <span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">x</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">←</span> <span class="n">pure</span> <span class="n">e</span> <span class="bp">|</span> <span class="n">none</span><span class="o">,</span>
      <span class="k">let</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">n</span> <span class="bp">++</span> <span class="n">x</span><span class="bp">.</span><span class="n">deinternalize_field</span><span class="o">,</span>
      <span class="n">env</span><span class="bp">.</span><span class="n">is_projection</span> <span class="n">f</span> <span class="err">$</span><span class="bp">&gt;</span> <span class="o">())</span>
    <span class="n">di</span><span class="bp">.</span><span class="n">type</span>
</pre></div>

#### [ Patrick Massot (Aug 16 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132226399):
<p>Nice!</p>

#### [ Patrick Massot (Aug 21 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132487331):
<blockquote>
<p>I think this replicates lean's <code>is_structure</code> function</p>
</blockquote>
<p>I'm sorry, I wasted your time. For some mysterious reason I missed <a href="https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/library/init/meta/environment.lean#L87" target="_blank" title="https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/library/init/meta/environment.lean#L87">https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/library/init/meta/environment.lean#L87</a> (and its implementation <a href="https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/src/library/vm/vm_environment.cpp#L227" target="_blank" title="https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/src/library/vm/vm_environment.cpp#L227">https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/src/library/vm/vm_environment.cpp#L227</a>)</p>

#### [ Patrick Massot (Aug 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132542303):
<p>Does Lean keep any trace of whether something was declared as a lemma or a theorem? Or are they purely synonym from the parsing stage on?</p>

#### [ Mario Carneiro (Aug 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132542417):
<p>pure synonyms</p>

#### [ Patrick Massot (Aug 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132542484):
<p>thanks</p>


{% endraw %}
