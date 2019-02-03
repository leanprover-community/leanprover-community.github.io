---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23770sneakinesswithautoparam.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [sneakiness with `auto_param`](https://leanprover-community.github.io/archive/113488general/23770sneakinesswithautoparam.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 08 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101629):
<p>I would like to be able to change the tactic specified via <code>auto_param</code> to fill in a structure field automatically.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101631):
<p>I know I can't actually do it, so I would like a nice workaround.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101653):
<p>Somehow I want to write</p>
<div class="codehilite"><pre><span></span>structure F :=
(t : Type . sneaky)
</pre></div>


<p>and then for a while during the development have <code>sneaky</code> do one thing, and then be able to utter a secret incantation, after which <code>sneaky</code> does something else.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101699):
<p>For example, the <code>sneaky</code> tactic could in some way inspect the environment, and delegate its actual work to a different tactic based on what it sees.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101703):
<p>Does anyone know what I'm looking for?</p>

#### [ Scott Morrison (Aug 08 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101717):
<p>I already do a little bit of this: my <code>tidy</code> tactic looks for definitions tagged with the <code>@[tidy]</code> attribute, and if they are of type <code>tactic unit</code> it also invokes them during it's attempt to solve a goal.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101773):
<p>But now I want something slight different: e.g. have <code>sneaky</code> call the last-to-be-defined tactic tagged with @[sneaky_implementation], or something like that.</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103723):
<p>Here's a way to do it if you want to have only one implementation at a given time:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">user_attribute</span><span class="o">]</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">sneaky_attr</span> <span class="o">:</span> <span class="n">user_attribute</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">name</span> <span class="o">:=</span> <span class="bp">`</span><span class="n">sneaky_impl</span><span class="o">,</span>
  <span class="n">descr</span> <span class="o">:=</span> <span class="s2">&quot;implementation for sneaky&quot;</span><span class="o">,</span>
  <span class="n">before_unset</span> <span class="o">:=</span> <span class="n">some</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span>
  <span class="n">after_set</span> <span class="o">:=</span> <span class="n">some</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">do</span>
    <span class="n">env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
    <span class="n">ns</span> <span class="err">←</span> <span class="n">attribute</span><span class="bp">.</span><span class="n">get_instances</span> <span class="n">sneaky_attr</span><span class="bp">.</span><span class="n">name</span><span class="o">,</span>
    <span class="n">ns</span><span class="bp">.</span><span class="n">mmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">when</span> <span class="o">(</span><span class="n">n</span> <span class="bp">≠</span> <span class="n">n&#39;</span><span class="o">)</span> <span class="err">$</span> <span class="n">unset_attribute</span> <span class="n">sneaky_attr</span><span class="bp">.</span><span class="n">name</span> <span class="n">n&#39;</span><span class="o">),</span>
    <span class="n">attribute</span><span class="bp">.</span><span class="n">get_instances</span> <span class="n">sneaky_attr</span><span class="bp">.</span><span class="n">name</span> <span class="bp">&gt;&gt;=</span> <span class="n">trace</span> <span class="o">}</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">sneaky</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="err">←</span> <span class="n">attribute</span><span class="bp">.</span><span class="n">get_instances</span> <span class="n">sneaky_attr</span><span class="bp">.</span><span class="n">name</span><span class="o">,</span>
  <span class="n">monad</span><span class="bp">.</span><span class="n">join</span> <span class="o">(</span><span class="n">mk_const</span> <span class="n">n</span> <span class="bp">&gt;&gt;=</span> <span class="n">eval_expr</span> <span class="o">(</span><span class="n">tactic</span> <span class="n">unit</span><span class="o">))</span>

<span class="kn">structure</span> <span class="n">F</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">.</span> <span class="n">sneaky</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">sneaky_impl</span><span class="o">]</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">mk_nat</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">trace</span> <span class="s2">&quot;running mk_nat&quot;</span> <span class="bp">&gt;&gt;</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="n">nat</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">F</span> <span class="o">:=</span> <span class="o">{}</span> <span class="c1">-- running mk_nat</span>

<span class="bp">@</span><span class="o">[</span><span class="n">sneaky_impl</span><span class="o">]</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">mk_sorry</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">trace</span> <span class="s2">&quot;running mk_sorry&quot;</span> <span class="bp">&gt;&gt;</span> <span class="bp">`</span><span class="o">[</span><span class="n">sorry</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">F</span> <span class="o">:=</span> <span class="o">{}</span> <span class="c1">-- running mk_sorry</span>
</pre></div>

#### [ Mario Carneiro (Aug 08 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103757):
<p>Each time you define a tactic with <code>@[sneaky_impl]</code>, the last one to have it has it unset, and <code>sneaky</code> calls which ever definition has the attribute right now</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103813):
<p>Alternatively, you could have the attributes remain permanently, but you just check which was the last to be written</p>

#### [ Scott Morrison (Aug 08 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103847):
<p>awesome! I didn't know about those hooks on attributes.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104078):
<p>okay, so next I want approval to use this in mathlib. :-) Later in my category theory work, I really rely on most of the <code>functoriality</code> (oops, <code>map_comp</code> <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span>) and <code>naturality</code> fields being filled in automatically by <code>tidy</code> or <code>obviously</code>. Of course, it's going to be a little while before <code>tidy</code> is mathlib ready, and maybe much longer before <code>obviously</code> is. I'd really like to be able to keep using them in my work, however... (in particular, I'm going to need to leave in "in action" everywhere in my later category theory stuff while I try and get them ready mathlib ready).</p>

#### [ Scott Morrison (Aug 08 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104131):
<p>So... the hope is that I can have the <code>id_comp</code>, <code>comp_id</code>, <code>assoc</code>, <code>map_id</code>, <code>map_comp</code> and <code>naturality</code> fields all invoke a tactic defined like <code>sneaky</code> above.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104151):
<p>In mathlib for now they will do nothing. In my development they will hook into whatever I want them to. Eventually, hopefully, they will start doing something in mathlib too.</p>

#### [ Johan Commelin (Aug 08 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104206):
<p>But what would the first mathlib version of <code>sneaky</code> do?</p>

#### [ Scott Morrison (Aug 08 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104211):
<p>`[skip]</p>

#### [ Scott Morrison (Aug 08 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104221):
<p>So if you don't provide the field explicitly, you just get the usual error message about an unsolved goal.</p>

#### [ Johan Commelin (Aug 08 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104236):
<p>Hmmm. Sorry, I don't get what your strategy is.</p>

#### [ Johan Commelin (Aug 08 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104241):
<p>Does that mean that you still have to prove this stuff by hand in mathlib?</p>

#### [ Johan Commelin (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104264):
<p>If so, why would you want a <code>sneaky</code>?</p>

#### [ Scott Morrison (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104289):
<p>If you look at <a href="https://github.com/leanprover/mathlib/blob/master/category_theory/category.lean#L43" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/category_theory/category.lean#L43">https://github.com/leanprover/mathlib/blob/master/category_theory/category.lean#L43</a></p>

#### [ Mario Carneiro (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104290):
<p>because he wants the auto param for a structure defined in mathlib to call his tactic</p>

#### [ Scott Morrison (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104296):
<p>you'll see that <code>category.assoc</code> is already marked with the auto_param <code>obviously</code>.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104301):
<p>it's just that <code>obviously</code> in mathlib is just defined to be <code>skip</code>. ( a few lines above!)</p>

#### [ Scott Morrison (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104311):
<p>I want to leave it like that in mathlib (for now), but still be able to use it outside while I'm getting it ready.</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104324):
<p>I'm okay with this in principle. I always thought that the static nature of auto params made them a bit limited, but this is a nice way to forward reference</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104334):
<p>I just need to figure out how to structure it nicely</p>

#### [ Scott Morrison (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104336):
<p>obviously it would make sense to write something slightly more general than sneaky above :-)</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104404):
<p>One thing which bothers me about this proposal is that you probably want to have just one <code>sneaky</code> which then goes everywhere</p>

#### [ Scott Morrison (Aug 08 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104410):
<p>I'm not sure what you mean?</p>

#### [ Scott Morrison (Aug 08 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104447):
<p>I'm imagining we could set up an attribute that you use like <code>@[replace tidy] meta def foo : tactic unit := ...</code></p>

#### [ Scott Morrison (Aug 08 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104458):
<p>and then as an auto_param you put in <code>(field : Type . invoke_tidy)</code></p>

#### [ Scott Morrison (Aug 08 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104513):
<p>and <code>invoke_tidy</code> goes and finds the latest declaration tagged with @[replace tidy].</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104524):
<p>is <code>tidy</code> parametric here? what else can you <code>replace</code></p>

#### [ Scott Morrison (Aug 08 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104665):
<p>well, I was imagining that other people might want to replace other things</p>

#### [ Scott Morrison (Aug 08 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104677):
<p>but maybe that's not helpful...</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104681):
<p>I agree. But how would that work?</p>

#### [ Scott Morrison (Aug 08 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104762):
<p>I don't really know about parameters to attributes, so I was just dreaming there.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104790):
<p>I was imagining that you'd only define an attribute once, just like <code>sneaky</code> but taking a parameter.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104806):
<p>For each value of that parameter you'd have to make a definition of an <code>invoke_XXX</code> tactic</p>

#### [ Scott Morrison (Aug 08 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104888):
<p>that would then invoke the last thing tagged with <code>@[replace XXX]</code></p>

#### [ Scott Morrison (Aug 08 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104918):
<p>For me, I'm happy to have a single tactic for all of those fields (and many others later)</p>

#### [ Scott Morrison (Aug 08 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104924):
<p>as long as I can still hook into it post mathlib</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104925):
<p>Oh wow, I tried using <code>sneaky_impl</code> with local attributes and it actually went back to the old definition after the section closed</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104983):
<div class="codehilite"><pre><span></span>@[sneaky_impl] meta def mk_nat : tactic unit :=
trace &quot;running mk_nat&quot; &gt;&gt; `[exact nat]

example : F := {} -- running mk_nat

section
meta def mk_sorry : tactic unit :=
trace &quot;running mk_sorry&quot; &gt;&gt; `[sorry]
local attribute [sneaky_impl] mk_sorry

example : F := {} -- running mk_sorry
end

example : F := {} -- running mk_nat
</pre></div>

#### [ Scott Morrison (Aug 08 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105029):
<p>Nice! (I think?)</p>

#### [ Mario Carneiro (Aug 08 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105046):
<p>I guess that's the power of functional data structures, you get "time travel" for free</p>

#### [ Johan Commelin (Aug 08 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105102):
<p>That means that you could add particular superpowers, but not others, to <code>tidy</code>, depending on the file you are working in?</p>

#### [ Scott Morrison (Aug 08 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105180):
<p>Yes</p>

#### [ Scott Morrison (Aug 08 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105231):
<p>I already do this all the time, actually, just at a whole file level.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105243):
<p>For me so far the definition of <code>tidy</code> has been invariant, except that it looks up everything marked with @[tidy] and tries those tactics too.</p>

#### [ Scott Morrison (Aug 08 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105253):
<p>Mario's observation means you can do it at section level too, which I hadn't really appreciated.</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131113251):
<p>Check out <a href="https://github.com/leanprover/mathlib/blob/master/tactic/replacer.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/replacer.lean">https://github.com/leanprover/mathlib/blob/master/tactic/replacer.lean</a> for my attempt at a general framework</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131113386):
<div class="codehilite"><pre><span></span>def_replacer tidy
structure T := (t : Type . tidy)

@[tidy] meta def tac1 := tactic.trace &quot;tac1&quot;
example : T := {} -- tac1

@[tidy] meta def tac2 (prev : tactic unit) := prev &gt;&gt; tactic.trace &quot;tac2&quot;
example : T := {} -- tac1 tac2

@[tidy] meta def tac3 := tactic.trace &quot;tac3&quot;
example : T := {} -- tac3
</pre></div>


{% endraw %}
